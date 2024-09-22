import asyncio
from typing import Optional, Union, List, Dict
from src.evaluation_suite import (
    EvaluationSuite,
    UpdateAssertion,
    AssertionWrapper,
    DataGenerationScenarios,
)
from src.evalforge.instructor_models import LLMAssertion, PythonAssertion
from src.llm_utils import instructor_client
from pydantic import BaseModel, Field
import weave


class ScenarioUpdateResponse(BaseModel):
    analysis: str = Field(
        ...,
        description="Analysis of whether changes are needed, including any new aspects identified",
    )
    updated_scenarios: List[DataGenerationScenarios] = Field(
        ...,
        description="List of existing + updated scenarios (if changes are needed), or just existing scenarios if current scenarios are sufficient",
    )

@weave.op
def generate_updated_assertion(
    old_assertion: Union[LLMAssertion, PythonAssertion],
    instruction: str,
    suite_description: str,
) -> Union[LLMAssertion, PythonAssertion]:
    print("I AM HERERERERE")
    prompt = f"""
    Task: Update the following assertion based on the given instruction.

    Suite Description: {suite_description}

    Current Assertion:
    Name: {old_assertion.test_name}
    Type: {old_assertion.evaluation_type}
    Content: {old_assertion.text if isinstance(old_assertion, LLMAssertion) else old_assertion.code}

    Instruction for update: {instruction}

    Please provide an updated version of the assertion that addresses the instruction while maintaining its original purpose and evaluation type.
    """

    response = asyncio.run(
        instructor_client.chat.completions.create(
            model="gpt-4o-latest",
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI assistant tasked with updating assertions for an evaluation suite.",
                },
                {"role": "user", "content": prompt},
            ],
            response_model=type(old_assertion),
        )
    )

    return response

@weave.op
async def update_data_generation_scenarios(
    evaluation_suite: EvaluationSuite,
    updated_assertion: Union[LLMAssertion, PythonAssertion],
    instruction: str,
) -> ScenarioUpdateResponse:
    prompt = f"""
    Task: Analyze the updated assertion and determine if the data generation scenarios need to be updated.

    Suite Description: {evaluation_suite.suite_description}

    Updated Assertion:
    Name: {updated_assertion.test_name}
    Type: {updated_assertion.evaluation_type}
    Content: {updated_assertion.text if isinstance(updated_assertion, LLMAssertion) else updated_assertion.code}

    Instruction used for update: {instruction}

    Current Data Generation Scenarios:
    {evaluation_suite.data_generation_scenarios}

    Please analyze if the updated assertion introduces any new aspects or requirements that are not covered by the current data generation scenarios. If so, provide an updated list of data generation scenarios that incorporates these new aspects. If no significant changes are needed, state that the current scenarios are sufficient.

    Your response should be in the following format:
    1. Analysis: [Your analysis of whether changes are needed, including any new aspects identified]
    2. Updated Scenarios: [List of updated scenarios if changes are needed, or "No changes required" if current scenarios are sufficient]
    """

    response = await instructor_client.chat.completions.create(
        model="gpt-4o-latest",
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant tasked with analyzing and updating data generation scenarios for an evaluation suite.",
            },
            {"role": "user", "content": prompt},
        ],
        response_model=ScenarioUpdateResponse,
    )

    return response

@weave.op
def update_assertion(
    evaluation_suite: EvaluationSuite, update_context: UpdateAssertion
) -> Optional[EvaluationSuite]:
    for criterion, assertion_wrapper in evaluation_suite.assertions.items():
        if assertion_wrapper.assertion.test_name == update_context.assertion_name:
            # Update the assertion
            updated_assertion = generate_updated_assertion(
                assertion_wrapper.assertion,
                update_context.instruction,
                evaluation_suite.suite_description,
            )

            # Replace the old assertion with the updated one
            evaluation_suite.assertions[criterion] = AssertionWrapper(
                assertion=updated_assertion
            )

            # Update data generation scenarios if necessary
            scenarios_update = asyncio.run(
                update_data_generation_scenarios(
                    evaluation_suite, updated_assertion, update_context.instruction
                )
            )

            if scenarios_update.analysis.lower() != "no changes required":
                evaluation_suite.data_generation_scenarios = (
                    scenarios_update.updated_scenarios
                )

            break

    return evaluation_suite
