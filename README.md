# Judge Tuner: LLM Example & Eval Metric Co-Tuner

Judge Tuner is a comprehensive tool for optimizing Large Language Model (LLM) performance by concurrently tuning example data and evaluation metrics. It provides an integrated approach to create, evaluate, and refine LLM evaluation suites.

## Features

- Create evaluation suites from prompts and examples
- Generate diverse criteria and assertions
- Produce synthetic examples
- Run evaluations with LLM and code-based assertions
- Update the suite based on feedback

## Prerequisites

- Python 3.12+
- Node.js 14+ (for the frontend)
- Poetry (for Python dependency management)
- npm or yarn (for frontend dependency management)

## Backend Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-repo/judge-tuner.git
   cd judge-tuner
   ```

2. Install dependencies using Poetry:
   ```
   poetry install
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory and add the following:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

4. Run the backend server:
   ```
   poetry run uvicorn src.main:app --reload
   ```

   The backend will be available at `http://localhost:8000`.

## Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   npm install
   ```
   or if you're using yarn:
   ```
   yarn install
   ```

3. Start the development server:
   ```
   npm run dev
   ```
   or with yarn:
   ```
   yarn dev
   ```

   The frontend will be available at `http://localhost:3000`.

## Usage

1. Open your browser and go to `http://localhost:3000`.
2. Use the interface to create a new evaluation suite or load an existing one.
3. Generate examples, run evaluations, and update the suite as needed.
4. View the results and iterate on your LLM's performance.

## API Endpoints

The backend provides the following API endpoints:

- `POST /set_up_task`: Create a new evaluation suite
- `POST /run_evaluations`: Run evaluations on a test case
- `POST /generate_examples`: Generate new examples for a suite
- `POST /update_evaluation_suite`: Update an existing evaluation suite

For detailed API documentation, visit `http://localhost:8000/docs` when the backend is running.

## Quick Demo Using Jupyter Notebook

To quickly try out Judge Tuner's functionality, you can use the provided `prototype.ipynb` Jupyter notebook:

1. Ensure you have Jupyter installed. If not, install it using:
   ```
   pip install jupyter
   ```

2. Navigate to the project root directory:
   ```
   cd judge-tuner
   ```

3. Start Jupyter Notebook:
   ```
   jupyter notebook
   ```

4. In the Jupyter interface, open the `prototype.ipynb` file.

5. Make sure your `.env` file is set up with the necessary API keys.

6. Run the cells in the notebook sequentially to see Judge Tuner in action:
   - The notebook demonstrates setting up an evaluation suite
   - Running evaluations on test cases
   - Generating new examples
   - Updating the evaluation suite

This notebook provides a hands-on demonstration of Judge Tuner's core functionalities without needing to set up the full backend and frontend.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.