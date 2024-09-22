import asyncio
from typing import Dict, List
import weave
from src.evaluation_suite import EvaluationSuite
from src.evalforge.instructor_models import LLMAssertion, PythonAssertion
from src.evaluation_suite import Testcase, AssertionResult, EvaluationRunResult
from src.evalforge.criterion_assertion_map import CriterionAssertionMap
from src.evalforge.combined_scorer import AssertionScorer


@weave.op()
def run_evaluations(
    testcase: Testcase, evaluation_suite: EvaluationSuite
) -> EvaluationRunResult:
    wrapped_assertions = [
        (k, [v.assertion]) for k, v in evaluation_suite.assertions.items()
    ]
    scorer = AssertionScorer(
        criterion_assertion_map=CriterionAssertionMap.from_assertions(
            wrapped_assertions
        ),
        llm_model="gpt-4o-latest",
    )
    criterion_to_assertion_results: Dict[str, AssertionResult] = {}

    output = testcase.output
    if isinstance(testcase.output, str):
        output = {"output": testcase.output}

    results = asyncio.run(
        scorer.score(
            output,
            evaluation_suite.setup.system_prompt
            + "\n\n"
            + "Only grade the assertion defined below, do not try to grade any other insturction from the task description except for this one assertion",
            testcase.input,
        )
    )

    for criterion, criterion_results in results.items():
        for assertion_name, result in criterion_results.items():
            assertion_content = ""
            if isinstance(
                evaluation_suite.assertions[criterion].assertion, LLMAssertion
            ):
                assertion_content = evaluation_suite.assertions[criterion].assertion.text  # type: ignore
            elif isinstance(
                evaluation_suite.assertions[criterion].assertion, PythonAssertion
            ):
                assertion_content = evaluation_suite.assertions[criterion].assertion.code  # type: ignore
            else:
                raise ValueError(
                    f"Unknown assertion type: {type(evaluation_suite.assertions[criterion].assertion)}"
                )
            assertion_result = {
                "assertion": assertion_content,
                "assertion_name": assertion_name,
                "type": evaluation_suite.assertions[criterion].assertion.evaluation_type,  # type: ignore
                "score": result["score"],
                "result": result["result"],
                "explanation": result.get("reasoning"),
            }
            criterion_to_assertion_results[criterion] = AssertionResult(
                **assertion_result
            )

    return EvaluationRunResult(
        testcase=testcase, criterion_to_assertion_results=criterion_to_assertion_results
    )
