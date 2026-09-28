import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_classic.prompts import PromptTemplate

# Load API Key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize Chat Model (GPT-4)
llm = ChatOpenAI(api_key=api_key, model="gpt-4")

# Prompt Template for Generating DB Test Cases
db_test_case_prompt = PromptTemplate(
    input_variables=["requirement"],
    template="""
    Given the following database/data warehouse enhancement requirement:

    "{requirement}"

    Generate a detailed set of test cases covering:
    - Functional test cases (schema validation, column additions, datatype/length changes)
    - Constraint validation (NOT NULL, UNIQUE, CHECK, FK)
    - Duplicate checks
    - Data quality checks (accuracy, completeness, consistency)
    - Business validation rules
    - Edge cases (boundary values, nulls, special characters)
    - Negative test cases (invalid data, constraint violations)
    - Regression test cases (ETL jobs, downstream reports, APIs)

    Provide structured output in this format:
    ```
    Test Case ID: TC-DB-001
    Description: [Test Scenario]
    Steps:
    1. [Step 1]
    2. [Step 2]
    Expected Result: [Expected Outcome]
    ```
    """
)

# Prompt Template for Generating DB Test Artifacts
db_artifact_prompt = PromptTemplate(
    input_variables=["requirement"],
    template="""
    Based on the following database/data warehouse enhancement requirement:

    "{requirement}"

    Generate the following test artifacts:
    1. **Test Plan**: Objectives, scope, impacted systems, regression areas.
    2. **User Scenarios**: Realistic data flows and interactions (ETL, reporting, APIs).
    3. **Test Data**: Sample rows covering positive, negative, edge, duplicate, and business-rule cases.

    Structure the output in Markdown format for readability.
    """
)

# Function to generate DB test cases
def generate_db_test_cases(requirement):
    prompt = db_test_case_prompt.format(requirement=requirement)
    response = llm.invoke([{"role": "user", "content": prompt}])
    return response.content

# Function to generate DB test artifacts
def generate_db_test_artifacts(requirement):
    prompt = db_artifact_prompt.format(requirement=requirement)
    response = llm.invoke([{"role": "user", "content": prompt}])
    return response.content

# Function to save generated documentation
def save_to_file(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Documentation saved as {filename}")

# Main Execution
if __name__ == "__main__":
    # Example DB Requirement
    requirement_text = """
    Enhancement in existing Customer_Master table:
    - Add new columns: customer_segment (VARCHAR 20), risk_score (INT)
    - Modify existing column: email VARCHAR 50 → VARCHAR 100
    - Add NOT NULL constraint on phone_number
    - Add CHECK constraint: risk_score BETWEEN 1 AND 100
    - Ensure ETL pipelines, dashboards, and downstream APIs continue working.
    - Validate duplicates, business rules, and data quality.
    """

    # Generate Documentation
    db_test_cases = generate_db_test_cases(requirement_text)
    db_test_artifacts = generate_db_test_artifacts(requirement_text)

    # Save Outputs
    save_to_file("db_test_cases.txt", db_test_cases)
    save_to_file("db_test_artifacts.md", db_test_artifacts)

    # Print Output
    print("\n Generated DB Test Cases:\n", db_test_cases)
    print("\n Generated DB Test Artifacts:\n", db_test_artifacts)
