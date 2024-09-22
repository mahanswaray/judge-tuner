from typing import List, Optional
from pydantic import BaseModel, Field
from src.evaluation_suite import DataGenerationScenarios
from src.evaluation_suite import EvaluationSuite, SetupExample
from src.llm_utils import instructor_client


class GeneratedExample(BaseModel):
    input: str = Field(..., description="The input for the generated example")
    output: str = Field(..., description="The output for the generated example")


class GeneratedExamples(BaseModel):
    examples: List[GeneratedExample] = Field(
        ..., description="List of generated examples"
    )


async def generate_new_examples(
    evaluation_suite: EvaluationSuite, num_examples: int, note: Optional[str] = None
) -> List[SetupExample]:
    prompt = f"""
    Task: Generate {num_examples} new example(s) for the following evaluation suite.

    Suite Description: {evaluation_suite.suite_description}

    System Prompt: {evaluation_suite.setup.system_prompt}

    Existing Verified Examples:
    {format_examples(evaluation_suite.verified_testcases)}

    Data Generation Scenarios:
    {format_scenarios(evaluation_suite.data_generation_scenarios)}

    {f"Additional Note: {note}" if note else ""}

    Please generate {num_examples} new, diverse example(s) that cover different aspects of the task and align with the given criteria and scenarios. Ensure that the examples are distinct from the existing ones and provide a good representation of the task's complexity.

    Format your response as a JSON object with a list of examples, each containing 'input' and 'output' fields.
    """

    response = await instructor_client.chat.completions.create(
        model="gpt-4o-latest",
        response_model=GeneratedExamples,
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant tasked with generating new examples for an evaluation suite.",
            },
            {"role": "user", "content": prompt},
        ],
    )

    return [
        SetupExample(input=example.input, output=example.output)
        for example in response.examples
    ]


def format_examples(examples: List[SetupExample]) -> str:
    return "\n".join([f"Input: {ex.input}\nOutput: {ex.output}\n" for ex in examples])


def format_scenarios(scenarios: List[DataGenerationScenarios]) -> str:
    return "\n".join(
        [
            f"- {scenario.scenarios_based_on}:\n  {', '.join(scenario.scenarios)}"
            for scenario in scenarios
        ]
    )
