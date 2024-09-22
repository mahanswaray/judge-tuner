# Judge-Tuner: LLM Program Evaluation Suite Builder

We are building a new app called "Judge-Tuner" aimed at creating and improving evaluation suites for LLM (Large Language Model) programs.

## LLM Program Structure
An LLM program consists of:
1. A system prompt
2. A set of examples (input and output)

## App Workflow

1. Initial Setup:
   The developer provides:
   - A system prompt
   - A set of examples (input and output)
   - A vague concept of various scenarios the program's inputs fall into

2. Parsed Setup:
   The app uses an AI-powered system to parse the initial setup and generate:
   - A suite description
   - Evaluation criteria
   - Data generation scenarios

3. Evaluation Suite Creation:
   The app generates an evaluation suite consisting of:
   a. LLM Program details
   b. A detailed requirements document (suite description)
   c. A list of evaluations, where each evaluation:
      - Can be an LLM program or a programmatic function
      - Has a scoring configuration
      - Includes a description and purpose
   d. A list of verified test cases

4. Evaluation Criteria:
   Each criterion includes:
   - A specific aspect to evaluate
   - An explanation of its importance
   - The evaluation method (code or LLM-based)

5. Data Generation Scenarios:
   The app identifies distinct input scenarios or categories to help generate diverse and representative test cases.

6. Evaluation Playground:
   The app provides an evaluation playground that includes:
   - The evaluation suite object
   - Unverified synthetic inputs
   - Playground history

## Key Components

1. EvaluationSuiteSetupConfig:
   - system_prompt: str
   - examples: List[SetupExample]

2. ParsedSetup:
   - suite_description: str
   - evaluation_criteria: List[EvaluationCriteria]
   - data_generation_scenarios: List[DataGenerationScenarios]

3. EvaluationSuite:
   - setup: EvaluationSuiteSetupConfig
   - suite_description: str
   - verified_testcases: List[Testcase]
   - evaluation_criteria: List[EvaluationCriteria]
   - data_generation_scenarios: List[str]

## Technologies Used
- Pydantic for data validation and settings management
- Instructor and OpenAI for AI-powered parsing and generation
- Weave for data visualization and management (to be implemented)

This app aims to streamline the process of creating, managing, and improving evaluation suites for LLM programs, making it easier for developers to assess and enhance their models' performance across various scenarios.

### API Request / Response 

POST /set_up_task

```{
    "system_prompt": "You are a helpful assistant that can evaluate the correctness of code.",
    "examples": [
        {
            "input": "print('Hello, world!')",
            "output": "Hello, world!"
        }
    ]
}```

```{'suite_description': 'The task is to generate an initial response to a customer support inquiry. The response must include a warm greeting, acknowledgment of the issue, and an open-ended question for further engagement. The response should be professionally friendly, concise, and should not offer specific solutions in this initial message.',
 'evaluation_criteria': [{'criterion': 'Warm Greeting',
   'explaination': 'The response should start with a warm greeting to make the customer feel valued and acknowledged.',
   'evaluation_method': 'llm'},
  {'criterion': 'Acknowledgement of the Issue',
   'explaination': "Clearly acknowledging the customer's issue shows empathy and assures the customer that their concern is being taken seriously.",
   'evaluation_method': 'llm'},
  {'criterion': 'Professional and Friendly Tone',
   'explaination': 'A professional yet friendly tone is essential to ensure the customer feels comfortable and respected.',
   'evaluation_method': 'llm'},
  {'criterion': 'Conciseness',
   'explaination': 'The response should be limited to one short paragraph, making it straightforward and easy to read.',
   'evaluation_method': 'code'},
  {'criterion': 'Omission of Specific Solutions',
   'explaination': 'Specific solutions should not be provided in the first response to encourage further dialogue and information gathering.',
   'evaluation_method': 'llm'},
  {'criterion': 'Open-ended Question',
   'explaination': 'Ending with an open-ended question encourages the customer to provide more information, keeping the conversation active.',
   'evaluation_method': 'llm'}],
 'data_generation_scenarios': [{'scenarios_based_on': "User's Issue Type",
   'scenarios': ['Shipping delay',
    'Product issue',
    'Billing error',
    'Account support']},
  {'scenarios_based_on': "User's Information Availability",
   'scenarios': ['User provides name', 'User does not provide name']}]}```