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
   - assertions: List[Union[LLMAssertion, PythonAssertion]]

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

POST /set_up_task
- Input: SetupTaskRequest (system_prompt, examples)
- Output: EvaluationSuite

This endpoint takes the initial setup configuration and returns a complete evaluation suite, including parsed setup, evaluation criteria, and generated assertions.

## Key Features

1. AI-powered parsing of initial setup
2. Generation of diverse evaluation criteria
3. Creation of both LLM-based and code-based assertions
4. Integration with EvalForge for advanced evaluation capabilities
5. Asynchronous processing for efficient handling of requests

The app provides a robust framework for creating comprehensive evaluation suites for LLM programs, enabling developers to assess and enhance their models' performance across various scenarios.

### API Request / Response 

POST /set_up_task

```"system_prompt":"You are a customer support agent tasked with writing the first response to a user filing a support issue. Follow these guidelines:\n\nFor content, begin with a warm greeting and thank the user for reaching out and acknowledge the issue they'\''ve reported.\n\nFor format, limit the response to 1 short paragraph.\n\nFor tone, maintain a professional yet friendly tone throughout.\n\nUse the user'\''s name if provided in their inquiry.\n\nFor additional rules, do not provide specific solutions in this first response.\nAlways end with an open-ended question to encourage further dialogue.","examples":[{"input":"My shipment is delayed and I need it urgently.","output":"Hello [User], Thank you for contacting our support team regarding your delayed shipment. I understand that this delay is causing you concern, especially given the urgency of your need. I sincerely apologize for any inconvenience this may be causing you. I want to assure you that I'\''m here to help and will do my best to address this situation as quickly as possible. Your satisfaction is important to us, and we take shipping delays very seriously. To better assist you, could you please provide me with your order number and the expected delivery date that was originally given to you? This information will help me investigate the status of your shipment more effectively."}]}```

```{"setup":{"system_prompt":"You are a customer support agent tasked with writing the first response to a user filing a support issue. Follow these guidelines:\n\nFor content, begin with a warm greeting and thank the user for reaching out and acknowledge the issue they've reported.\n\nFor format, limit the response to 1 short paragraph.\n\nFor tone, maintain a professional yet friendly tone throughout.\n\nUse the user's name if provided in their inquiry.\n\nFor additional rules, do not provide specific solutions in this first response.\nAlways end with an open-ended question to encourage further dialogue.","examples":[{"input":"My shipment is delayed and I need it urgently.","output":"Hello [User], Thank you for contacting our support team regarding your delayed shipment. I understand that this delay is causing you concern, especially given the urgency of your need. I sincerely apologize for any inconvenience this may be causing you. I want to assure you that I'm here to help and will do my best to address this situation as quickly as possible. Your satisfaction is important to us, and we take shipping delays very seriously. To better assist you, could you please provide me with your order number and the expected delivery date that was originally given to you? This information will help me investigate the status of your shipment more effectively."}]},"suite_description":"The task involves a customer support agent crafting an initial response to a user who has filed a support issue. The response must start with a warm greeting, thank the user for their communication, and acknowledge the problem they've reported. The message should be short, professionally friendly, and use the user's name if provided. No specific solutions should be given in this first message, and it must end with an open-ended question to further the dialogue.","verified_testcases":[{"input":"My shipment is delayed and I need it urgently.","output":"Hello [User], Thank you for contacting our support team regarding your delayed shipment. I understand that this delay is causing you concern, especially given the urgency of your need. I sincerely apologize for any inconvenience this may be causing you. I want to assure you that I'm here to help and will do my best to address this situation as quickly as possible. Your satisfaction is important to us, and we take shipping delays very seriously. To better assist you, could you please provide me with your order number and the expected delivery date that was originally given to you? This information will help me investigate the status of your shipment more effectively.","description":null,"purpose":null}],"evaluation_criteria":[{"criterion":"Warm Greeting","explanation":"The reply should start with a friendly and warm greeting to make the customer feel welcomed and valued.","evaluation_method":"llm"},{"criterion":"Acknowledgement of Issue","explanation":"It's important to recognize the customer's problem to show understanding and empathy, helping to build trust.","evaluation_method":"llm"},{"criterion":"Thanking User","explanation":"Thanking the customer for reaching out shows appreciation for their effort and patience, which can help defuse frustration.","evaluation_method":"llm"},{"criterion":"Professional Yet Friendly Tone","explanation":"Maintaining a balance between professionalism and friendliness ensures the message is approachable yet respectful.","evaluation_method":"llm"},{"criterion":"Use of User's Name","explanation":"Addressing the user by their name personalizes the message and makes the customer feel individually attended to.","evaluation_method":"llm"},{"criterion":"Limiting to One Short Paragraph","explanation":"Keeping the response concise ensures it respects the customer's time and maintains focus on the acknowledgement and next steps.","evaluation_method":"code"},{"criterion":"No Specific Solutions","explanation":"The first response should primarily address the issue and seek additional information or prompt further dialogue without providing direct solutions upfront.","evaluation_method":"llm"},{"criterion":"Ending with Open-Ended Question","explanation":"Concluding the message with an open-ended question invites the customer to provide more information, aiding further assistance.","evaluation_method":"llm"}],"data_generation_scenarios":[{"scenarios_based_on":"Type of Issue Reported","scenarios":["Delayed shipment","Wrong item received","Billing issue","Technical problem with a product"]},{"scenarios_based_on":"User Information Provided","scenarios":["User's name is provided","User's name is not provided"]},{"scenarios_based_on":"Urgency of the Issue","scenarios":["Urgent issue requiring immediate attention","Non-urgent issue"]},{"scenarios_based_on":"Tone of User's Message","scenarios":["User's message is polite and calm","User's message is frustrated and upset"]}],"assertions":{"name":null,"description":null,"criterion_to_assertions":{"Warm Greeting":[{"test_name":"test_warm_greeting","text":"Evaluate whether the response begins with a warm and friendly greeting to make the customer feel welcomed and valued. Check if the greeting uses polite language, acknowledges the user in a positive manner, and sets a tone of friendliness. Pass if the greeting fulfills these criteria, otherwise fail.","evaluation_type":"llm"}],"Acknowledgement of Issue":[{"test_name":"acknowledgement_of_issue","text":"Evaluate the given customer support response. Check if the response acknowledges the customer's reported issue clearly and empathetically. The response should directly mention understanding of the delay and the urgency stated by the user. Return 'PASS' if the response meets these criteria, otherwise return 'FAIL'.","evaluation_type":"llm"}],"Thanking User":[{"test_name":"evaluate_thanking_user_presence","text":"Given a customer support response, determine if the message includes a clear and explicit thanks to the user for reaching out or contacting support. This thanking should be evident within the body of the response.","evaluation_type":"llm"}],"Professional Yet Friendly Tone":[{"test_name":"test_professional_yet_friendly_tone","text":"Evaluate whether the LLM-generated customer support message maintains a balance between professionalism and friendliness. The message should start with a warm greeting, thank the user for their communication, and acknowledge the problem. It should be concise, use the user's name if provided, avoid offering specific solutions, and end with an open-ended question. Consider the overall tone of the message. Respond with 'PASS' if the tone is professional yet friendly, and 'FAIL' otherwise.","evaluation_type":"llm"}],"Use of User's Name":[{"test_name":"use_of_user_name","text":"Evaluate the output to determine if the user's name is used in a way that personalizes the message. The opening part of the message should address the user by name to create a personalized experience. If the name is missing, then no personalization has occurred. If the name is present and appropriately used in the greeting or elsewhere to personalize the message, return 'PASS'. Otherwise, return 'FAIL'.","evaluation_type":"llm"}],"Limiting to One Short Paragraph":[{"test_name":"test_output_within_one_short_paragraph","code":"def test_output_within_one_short_paragraph(self):\n    # Check if the number of sentences in the output is less than or equal to 4\n    output_text = self.output\n    sentences = output_text.split('.')\n    short_paragraph = len(sentences) <= 4  # Assuming a short paragraph contains 4 or fewer sentences\n    self.assertTrue(short_paragraph, \"Response should be limited to one short paragraph with a maximum of 4 sentences.\")","evaluation_type":"python"}],"No Specific Solutions":[{"test_name":"evaluate_no_specific_solutions","text":"Given the user's input and the LLM's response, evaluate whether the response adheres to the criteria of addressing the issue without providing specific solutions. The response should include a warm greeting, an acknowledgment of the problem, and an open-ended question prompting further dialogue, but it must avoid proposing any direct solutions. If these criteria are met, respond with 'PASS', otherwise respond with 'FAIL'.","evaluation_type":"llm"}],"Ending with Open-Ended Question":[{"test_name":"validate_ending_with_open_ended_question","text":"Evaluate the given customer support response and determine if it concludes with an open-ended question. An open-ended question is one that invites the recipient to provide more detailed information and cannot be answered with a simple 'yes' or 'no'. Review the final part of the response and check if it prompts the customer for more information about their issue in a way that keeps the conversation going. Return 'PASS' if the response ends with such a question, otherwise return 'FAIL'.","evaluation_type":"llm"}]},"assertion_to_criterion":{"test_warm_greeting":"Warm Greeting","acknowledgement_of_issue":"Acknowledgement of Issue","evaluate_thanking_user_presence":"Thanking User","test_professional_yet_friendly_tone":"Professional Yet Friendly Tone","use_of_user_name":"Use of User's Name","test_output_within_one_short_paragraph":"Limiting to One Short Paragraph","evaluate_no_specific_solutions":"No Specific Solutions","validate_ending_with_open_ended_question":"Ending with Open-Ended Question"}}}```


## Current Task: Implement run_evaluations API

Our next step is to implement a new API endpoint called `run_evaluations`. This endpoint will take a Testcase and a List[str, Union[LLMAssertion, PythonAssertion]] as input and return a new object called EvaluationRunResult.

### Specification:

1. Create a new API endpoint:
   - Path: `/run_evaluations`
   - Method: POST

2. Input:
   - Testcase: An object containing the input and output to be evaluated
   - List[str, Union[LLMAssertion, PythonAssertion]]: A map of evaluation criteria to their associated assertions

3. Output:
   - EvaluationRunResult: A new object containing the evaluation results

4. EvaluationRunResult structure:
   - testcase: The original Testcase object
   - criterion_to_assertion_results: A map where keys are criterion names and values are lists of AssertionResult objects

5. AssertionResult structure:
   - assertion: The original assertion string
   - passed: A boolean indicating whether the assertion passed or failed
   - explanation: A string explaining why the assertion passed or failed

6. Implementation steps:
   a. Create the necessary Pydantic models for the new structures (EvaluationRunResult, AssertionResult)
   b. Implement the logic to run each assertion against the given Testcase
   c. Use the EvalForge library to evaluate LLM-based assertions
   d. Create the new API endpoint in the FastAPI app
   e. Implement error handling and input validation

7. Additional considerations:
   - Ensure the API can handle both code-based and LLM-based assertions
   - Implement proper error handling for invalid inputs or evaluation failures
   - Consider adding optional parameters for customizing the evaluation process (e.g., LLM model selection)

This new API endpoint will allow users to run evaluations on specific test cases using the previously generated evaluation criteria and assertions. It will provide detailed results for each criterion and assertion, enabling users to assess the performance of their LLM programs across various evaluation criteria.