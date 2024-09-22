from pydantic import BaseModel, Field
from typing import List, Literal, Dict, Optional, Union

from src.evalforge.criterion_assertion_map import CriterionAssertionMap
from src.evalforge.instructor_models import Criterion


class SetupExample(BaseModel):
    input: str
    output: str


class EvaluationSuiteSetupConfig(BaseModel):
    system_prompt: str
    examples: List[SetupExample]


class DataGenerationScenarios(BaseModel):
    scenarios_based_on: str = Field(
        ...,
        description="The type of scenarios based on which the data is generated, for example, it could be based on the type of user, or the type of task, or the type of data.",
    )
    scenarios: List[str] = Field(..., description="The list of scenarios.")


class Testcase(BaseModel):
    input: str
    output: str
    description: Optional[str] = None
    purpose: Optional[str] = None


class EvaluationSuite(BaseModel):

    setup: EvaluationSuiteSetupConfig
    suite_description: str
    verified_testcases: List[Testcase]
    evaluation_criteria: List[Criterion]
    data_generation_scenarios: List[DataGenerationScenarios]
    assertions: CriterionAssertionMap
