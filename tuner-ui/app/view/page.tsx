

const test = {
    suite_description: "Suite Description",
    evaluation_criteria: [{ criterion: "something", explaination: "something", evaluation_method: "code" }],
    data_generation_criteria: [{ scenarios_based_on: "something", scenarios: ["a", "b", "c"] }],
}

import testData from "./test.json"


function EvaluationCriteria({ criterion, explaination, evaluation_method }: { criterion: string, explaination: string, evaluation_method: string }) {
    return (
        <div>
            <p>Criterion: {criterion}</p>
            <p>Explaination: {explaination}</p>
            <p>Evaluation Method: {evaluation_method}</p>
        </div>
    )
}

function DataGenerationCriteria({ scenarios_based_on, scenarios }: { scenarios_based_on: string, scenarios: string[] }) {
    return (
        <div>
            <p>Scenarios Based On: {scenarios_based_on}</p>
            <p>Scenarios: {scenarios.join(", ")}</p>
        </div>
    )
}


function Test() {
    return (

        <div className="flex w-full h-16 bg-white gap-3">
            <div className="h-full w-4 bg-red-500"></div>
            <div className="h-full w-4 bg-green-500"></div>
            <div className="h-full w-4 bg-blue-500 ml-auto"></div>
        </div>

    )
}

export default function ViewPage() {
    return (
        <div>
            <Test />
            <p>{testData.suite_description}</p>
            {testData.evaluation_criteria.map((criterion) => (
                <EvaluationCriteria key={criterion.criterion} criterion={criterion.criterion} explaination={criterion.explaination} evaluation_method={criterion.evaluation_method} />
            ))}
            {testData.data_generation_criteria.map((criterion) => (
                <DataGenerationCriteria key={criterion.scenarios_based_on} scenarios_based_on={criterion.scenarios_based_on} scenarios={criterion.scenarios} />
            ))}
        </div>
    )
}