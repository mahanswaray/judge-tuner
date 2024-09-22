from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from src.evaluation_suite_setup import EvaluationSuiteSetupConfig, SetupExample
from src.parse_setup import parse_setup

app = FastAPI()


class SetupTaskRequest(BaseModel):
    system_prompt: str
    examples: List[SetupExample]


@app.post("/set_up_task")
async def setup_task(request: SetupTaskRequest):
    try:
        setup_config = EvaluationSuiteSetupConfig(
            system_prompt=request.system_prompt, examples=request.examples
        )
        parsed_setup = parse_setup(setup_config)
        return parsed_setup
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
