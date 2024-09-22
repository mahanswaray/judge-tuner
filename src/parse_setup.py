import os
from typing import Dict, List
import instructor
import openai
from pydantic import BaseModel, Field

from src.evaluation_suite import DataGenerationScenarios, EvaluationCriteria
from src.evaluation_suite_setup import EvaluationSuiteSetupConfig

PARSED_SETUP_SYSTEM_PROMPT = """You are a extremely intelligent member of a data annotation team tasked with completing the setup of an evaluation suite.
You are provided with a setup of an evaluation suite and you need to output a ParsedSetup object.
You will be given the following :
1. a task system prompt that defines the task, what is expected, how it's expected, and how it should be outputed -> this is the target task, that needs to be evaluated.
2. a list of input and output examples of the the target task. 

You need to output 
1. A detailed description of the task the user wants to evaluate on, summary of the requirements defined by the system prompt.
2. A list of evaluation criteria for the task.
3. A list of distinct input scenarios or categories that the task is expected to handle. This helps in generating diverse and representative test cases.

HERE IS THE SETUP DATA : 
{system_prompt}
{examples}
"""


class ParsedSetup(BaseModel):
    suite_description: str = Field(
        ...,
        description="Detailed description of the task the user wants to evaluate on, summary of the requirements defined by the system prompt.",
    )
    evaluation_criteria: List[EvaluationCriteria] = Field(
        ..., description="List of evaluation criteria for the task."
    )
    data_generation_scenarios: List[DataGenerationScenarios] = Field(
        ...,
        description="List of distinct input scenarios or categories that the task is expected to handle. This helps in generating diverse and representative test cases.",
    )


openai_client = instructor.from_openai(
    openai.OpenAI(
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url=os.getenv("OPENROUTER_BASE_URL"),
    )
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


def parse_setup(setup: EvaluationSuiteSetupConfig) -> ParsedSetup:
    messages = create_parsed_setup_messages(setup)
    parsed_setup = openai_client.chat.completions.create(
        model="gpt-4o-latest",
        response_model=ParsedSetup,
        messages=messages,
    )
    return parsed_setup


if __name__ == "__main__":
    from models.evaluation_suite_setup import SetupExample

    example_setup = EvaluationSuiteSetupConfig(
        system_prompt="""You are a customer support agent tasked with writing the first response to a user filing a support issue. Follow these guidelines:

    For content, begin with a warm greeting and thank the user for reaching out and acknowledge the issue they've reported.

    For format, limit the response to 1 short paragraph.

    For tone, maintain a professional yet friendly tone throughout.

    Use the user's name if provided in their inquiry.

    For additional rules, do not provide specific solutions in this first response.
    Always end with an open-ended question to encourage further dialogue.
    """,
        examples=[
            SetupExample(
                input="My shipment is delayed and I need it urgently.",
                output="Hello [User], Thank you for contacting our support team regarding your delayed shipment. I understand that this delay is causing you concern, especially given the urgency of your need. I sincerely apologize for any inconvenience this may be causing you. I want to assure you that I'm here to help and will do my best to address this situation as quickly as possible. Your satisfaction is important to us, and we take shipping delays very seriously. To better assist you, could you please provide me with your order number and the expected delivery date that was originally given to you? This information will help me investigate the status of your shipment more effectively.",
            ),
        ],
    )
