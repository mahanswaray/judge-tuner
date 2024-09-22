# Judge-Tuner: LLM Program Evaluation Suite Builder

Judge-Tuner is an application designed to create and improve evaluation suites for LLM (Large Language Model) programs. It leverages the EvalForge library to enhance its evaluation capabilities.

## LLM Program Structure
An LLM program consists of:
1. A system prompt
2. A set of examples (input and output)

## App Workflow

1. Initial Setup:
   The developer provides:
   - A system prompt
   - A set of examples (input and output)

2. Parsed Setup:
   The app uses an AI-powered system to parse the initial setup and generate:
   - A suite description
   - Evaluation criteria
   - Data generation scenarios

3. Evaluation Suite Creation:
   The app generates an evaluation suite using EvalForge, consisting of:
   a. LLM Program details
   b. A detailed requirements document (suite description)
   c. A list of evaluations, including LLM-based and code-based assertions
   d. A list of verified test cases

4. Suite Validation and Refinement:
   After the initial suite creation, the user goes through the following steps:
   a. Validate the suite setup
   b. Generate a new synthetic example (with or without feedback)
   c. Optionally edit the generated example to their preference
   d. Run all evaluations on the new example
   e. Provide feedback on the evaluation results
   f. Update the evaluation suite based on the feedback:
      - Refine evaluation prompts or code
      - Update data generation scenarios to include new scenarios if necessary
      - Ensure the suite can generate data for the new scenario

## Key Components

1. EvaluationSuiteSetupConfig:
   - system_prompt: str
   - examples: List[SetupExample]

2. ParsedSetup:
   - suite_description: str
   - evaluation_criteria: List[Criterion]
   - data_generation_scenarios: List[DataGenerationScenarios]

3. EvaluationSuite:
   - setup: EvaluationSuiteSetupConfig
   - suite_description: str
   - verified_testcases: List[Testcase]
   - evaluation_criteria: List[Criterion]
   - data_generation_scenarios: List[DataGenerationScenarios]
   - assertions: Dict[str, AssertionWrapper]

4. AssertionResult:
   - assertion: str
   - assertion_name: str
   - type: str
   - score: int
   - result: str
   - explanation: Optional[str]

5. EvaluationRunResult:
   - testcase: Testcase
   - criterion_to_assertion_results: Dict[str, AssertionResult]

## EvalForge Integration

The app incorporates the following components from EvalForge:

1. AssertionScorer: Combines LLM and code-based assertions for evaluation
2. LLMAssertionScorer: Evaluates outputs using LLM-based assertions
3. CodeAssertionScorer: Evaluates outputs using Python code-based assertions
4. CodeFormatter: Formats and lints Python code for assertions

## Technologies Used
- Pydantic for data validation and settings management
- Instructor and OpenAI for AI-powered parsing and generation
- FastAPI for the web framework
- Weave for data visualization and management

## API Endpoints

1. POST /set_up_task
   - Input: SetupTaskRequest (system_prompt, examples)
   - Output: EvaluationSuite

2. POST /run_evaluations
   - Input: RunEvaluationsRequest (testcase, evaluation_suite)
   - Output: EvaluationRunResult

3. POST /generate_examples
   - Input: GenerateExamplesRequest (evaluation_suite, num_examples, note)
   - Output: List[SetupExample]

4. POST /update_evaluation_suite
   - Input: UpdateEvaluationSuiteRequest (evaluation_suite, feedback)
   - Output: UpdatedEvaluationSuite

## Key Features

1. AI-powered parsing of initial setup
2. Generation of diverse evaluation criteria
3. Creation of both LLM-based and code-based assertions
4. Integration with EvalForge for advanced evaluation capabilities
5. Asynchronous processing for efficient handling of requests
6. Generation of new examples based on existing evaluation suite
7. Evaluation of test cases against generated assertions
8. Iterative refinement of the evaluation suite based on user feedback
9. Dynamic updating of data generation scenarios to cover new cases

The app provides a robust framework for creating and refining comprehensive evaluation suites for LLM programs, enabling developers to assess and enhance their models' performance across various scenarios. The iterative feedback loop allows for continuous improvement of the evaluation process, ensuring that the suite remains relevant and effective as new scenarios and edge cases are discovered.

## Current Task: Implement update_evaluation_suite API

Our next step is to implement a new API endpoint called `update_evaluation_suite`. This endpoint will take an existing EvaluationSuite and feedback, and return an updated EvaluationSuite.

### Specification:

1. Create a new API endpoint:
   - Path: `/update_evaluation_suite`
   - Method: POST

2. Input:
   - UpdateEvaluationSuiteRequest:
     - evaluation_suite: EvaluationSuite
     - update_context: Union[UpdateTestcase, UpdateAssertion]

3. Output:
   - UpdatedEvaluationSuite: An updated version of the input EvaluationSuite

4. Implementation steps:
   a. Create the necessary Pydantic models for the new structures (if not already existing)
   b. Implement the logic to update the EvaluationSuite based on the provided feedback:
      - If UpdateTestcase is provided, add or update the testcase in the suite
      - If UpdateAssertion is provided, update the specified assertion
   c. Use the EvalForge library to regenerate or update assertions if necessary
   d. Update data generation scenarios if the new testcase introduces a new scenario
   e. Create the new API endpoint in the FastAPI app
   f. Implement error handling and input validation

5. Additional considerations:
   - Ensure the API can handle both testcase updates and assertion updates
   - Implement proper error handling for invalid inputs or update failures
   - Consider adding optional parameters for customizing the update process (e.g., regenerate all assertions, update only specific criteria)

This new API endpoint will allow users to iteratively refine their evaluation suites based on new examples or improved assertions, ensuring that the suite remains up-to-date and effective as the LLM application evolves.