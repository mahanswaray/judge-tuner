from pydantic import BaseModel, Field
from typing import List, Literal


class SetupExample(BaseModel):
    input: str
    output: str


class EvaluationSuiteSetupConfig(BaseModel):
    system_prompt: str
    examples: List[SetupExample]
    testcase_scenarios: str


class EvaluationCriteria(BaseModel):
    criterion: str = Field(
        ...,
        description="A concise, specific statement describing a single aspect of evaluation",
    )
    explaination: str = Field(
        "",
        description="A detailed explanation of the criterion's importance and potential evaluation methods",
    )
    evaluation_method: Literal["code", "llm"] = Field(
        "",
        description="The primary method for evaluating this criterion: 'code' for programmatic checks, 'llm' for language model-based assessment",
    )


class DataGenerationScenarios(BaseModel):
    scenarios_based_on: str = Field(
        ...,
        description="The type of scenarios based on which the data is generated, for example, it could be based on the type of user, or the type of task, or the type of data.",
    )
    scenarios: List[str] = Field(..., description="The list of scenarios.")


class Testcase(BaseModel):
    input: str
    output: str
    ground_truth: str
    description: str
    purpose: str


class EvaluationSuite(BaseModel):

    setup: EvaluationSuiteSetupConfig
    suite_description: str
    verified_testcases: List[Testcase]
    evaluation_criteria: List[EvaluationCriteria]
    data_generation_scenarios: List[str]
