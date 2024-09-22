from pydantic import BaseModel, Field
from typing import List, Dict, Literal, Optional, Union
from src.evalforge.criterion_assertion_map import CriterionAssertionMap
from src.evalforge.instructor_models import Criterion, LLMAssertion, PythonAssertion


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


class AssertionWrapper(BaseModel):
    assertion: Union[LLMAssertion, PythonAssertion]


class EvaluationSuite(BaseModel):
    setup: EvaluationSuiteSetupConfig
    suite_description: str
    verified_testcases: List[Testcase]
    evaluation_criteria: List[Criterion]
    data_generation_scenarios: List[DataGenerationScenarios]
    assertions: Dict[str, AssertionWrapper]


class AssertionResult(BaseModel):
    assertion: str
    assertion_name: str
    type: str  # Literal["llm", "code"]
    score: int
    result: str  # Literal["PASS", "FAIL"]
    explanation: Optional[str] = None


class EvaluationRunResult(BaseModel):
    testcase: Testcase
    criterion_to_assertion_results: Dict[str, AssertionResult]


class RunEvaluationsRequest(BaseModel):
    testcase: Testcase
    evaluation_suite: EvaluationSuite


class UpdateTestcase(BaseModel):
    input: str
    output: str
    context: Optional[str] = None


class UpdateAssertion(BaseModel):
    instruction: str
    assertion_name: str


class UpdateEvaluationSuiteRequest(BaseModel):
    evaluation_suite: EvaluationSuite
    update_context: Union[UpdateTestcase, UpdateAssertion]
