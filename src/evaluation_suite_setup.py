from pydantic import BaseModel
from typing import List


class SetupExample(BaseModel):
    input: str
    output: str


class EvaluationSuiteSetupConfig(BaseModel):
    system_prompt: str
    examples: List[SetupExample]
