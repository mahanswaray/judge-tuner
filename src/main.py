import traceback
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from src.evaluation_suite import EvaluationSuiteSetupConfig, SetupExample, RunEvaluationsRequest, EvaluationRunResult
from src.parse_setup import parse_setup
from src.evaluation_suite import EvaluationSuite
from src.evaluation_runner import run_evaluations
import nest_asyncio
import weave

weave.init("judge-tuner-prototype")

nest_asyncio.apply()

app = FastAPI()

class SetupTaskRequest(BaseModel):
    system_prompt: str
    examples: List[SetupExample]

@app.post("/set_up_task")
@weave.op()
async def setup_task(request: SetupTaskRequest) -> EvaluationSuite:
    try:
        setup_config = EvaluationSuiteSetupConfig(
            system_prompt=request.system_prompt,
            examples=request.examples
        )
        evaluation_suite = parse_setup(setup_config)
        return evaluation_suite
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/run_evaluations")
@weave.op()
async def run_evaluations_endpoint(request: RunEvaluationsRequest) -> EvaluationRunResult:
    try:
        result = run_evaluations(request.testcase, request.evaluation_suite)
        return result
    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(status_code=400, detail=str(e))
    

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
