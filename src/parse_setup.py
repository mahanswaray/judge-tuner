import asyncio
from typing import Dict, List
from pydantic import BaseModel, Field

from src.evalforge.criterion_assertion_map import CriterionAssertionMap
from src.evaluation_suite import Testcase
from src.evalforge.instructor_models import Criterion
from src.evaluation_suite import (
    DataGenerationScenarios,
    EvaluationSuite,
)
from src.evaluation_suite import EvaluationSuiteSetupConfig, SetupExample
from src.evalforge.evalforge import EvalForge

PARSED_SETUP_SYSTEM_PROMPT = """You are a extremely intelligent member of a data annotation team tasked with completing the setup of an evaluation suite.
You are provided with a setup of an evaluation suite and you need to output a ParsedSetup object.
You will be given the following :
1. a task system prompt that defines the task, what is expected, how it's expected, and how it should be outputed -> this is the target task, that needs to be evaluated.
2. a list of input and output examples of the the target task. 

You need to output 
1. A detailed description of the task the user wants to evaluate on, summary of the requirements defined by the system prompt.
2. A list of evaluation criteria for the task.
    1.1. Focus on general aspects of quality that can be used across multiple outputs.
    1.2. Consider criteria that address potential misalignment between LLM outputs and human preferences.
    1.3. Include criteria that can be evaluated both by code and by LLM-based evaluators.
    1.4. Think about criteria that might reveal hallucinations, instruction-following, or other common LLM issues.
    1.5. Generate criteria that could help in debugging or improving the LLM pipeline.
3. A list of distinct input scenarios or categories that the task is expected to handle. This helps in generating diverse and representative test cases.

HERE IS THE SETUP DATA : 
{system_prompt}
{examples}
"""
from src.evalforge.llm_utils import client


class ParsedSetup(BaseModel):
    suite_description: str = Field(
        ...,
        description="Detailed description of the task the user wants to evaluate on, summary of the requirements defined by the system prompt.",
    )
    evaluation_criteria: List[Criterion] = Field(
        ..., description="List of evaluation criteria for the task."
    )
    data_generation_scenarios: List[DataGenerationScenarios] = Field(
        ...,
        description="List of distinct input scenarios or categories that the task is expected to handle. This helps in generating diverse and representative test cases.",
    )


def create_parsed_setup_messages(
    setup: EvaluationSuiteSetupConfig,
) -> List[Dict[str, str]]:
    examples = "\n".join(
        [
            f"Input: {example.input} Output: {example.output}"
            for example in setup.examples
        ]
    )
    messages = [
        {
            "role": "system",
            "content": PARSED_SETUP_SYSTEM_PROMPT.format(
                system_prompt=setup.system_prompt, examples=examples
            ),
        },
        {
            "role": "user",
            "content": "Please parse the setup data into a ParsedSetup object.",
        },
    ]
    return messages


def generate_assertions(
    parsed_setup: ParsedSetup, examples: List[SetupExample]
) -> CriterionAssertionMap:
    eval_forge = EvalForge()
    assertions = {}

    criteria: List[Criterion] = parsed_setup.evaluation_criteria
    formatted_data = "\n\n".join(
        [f"Task and Evaluation Description: {parsed_setup.suite_description}"]
        + [f"Input: {example.input} \nOutput: {example.output}" for example in examples]
    )
    assertions = asyncio.run(
        eval_forge.generate_all_assertions(criteria, formatted_data)
    )
    return assertions


def parse_setup(setup_config: EvaluationSuiteSetupConfig) -> EvaluationSuite:
    parsed_setup = asyncio.run(
        client.chat.completions.create(  # type: ignore
            model="gpt-4o-latest",
            response_model=ParsedSetup,
            messages=create_parsed_setup_messages(setup_config),  # type: ignore
        )
    )

    # Generate assertions using EvalForge
    assertions: CriterionAssertionMap = generate_assertions(
        parsed_setup, setup_config.examples
    )

    # Create EvaluationSuite object
    evaluation_suite = EvaluationSuite(
        setup=setup_config,
        suite_description=parsed_setup.suite_description,
        verified_testcases=[
            Testcase(input=example.input, output=example.output)
            for example in setup_config.examples
        ],
        evaluation_criteria=parsed_setup.evaluation_criteria,
        data_generation_scenarios=parsed_setup.data_generation_scenarios,
        assertions=assertions,
    )

    return evaluation_suite
