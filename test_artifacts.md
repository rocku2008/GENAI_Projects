**Test Plan**

**Objectives**

The objective of this test plan is to verify that the login functionality performs as expected. The Verifications include:
- Redirecting users to the dashboard once they input correct credentials.
- Displaying an error message once incorrect credentials are entered.

**Scope**

This test plan covers the login functionality, including the user's email and password input mechanism, error message display, and successful login redirection process.

**Responsibilities**

QA's are responsible for preparing test data and performing tests. Developers are responsible for correcting any identified bugs and retest after issues fix.

---

**User Scenarios**

**Scenario 1: Successful login with correct credentials**

- The user navigates to the login page
- The user enters a valid email and password
- The user clicks on the 'Login' button
- The system verifies the credentials
- The user is redirected to the dashboard

**Scenario 2: Unsuccessful login with incorrect credentials**

- The user navigates to the login page
- The user enters an incorrect email or password
- The user clicks on the 'Login' button
- The system verifies the credentials
- An error message is displayed

**Scenario 3: Unsuccessful login with empty credentials**

- The user navigates to the login page
- The user leaves the email and/or password field blank
- The user clicks on the 'Login' button
- The system verifies the credentials
- An error message is displayed

---

**Test Data**

- **Valid credentials:**

    Email: john.doe@gmail.com

    Password: Password123

- **Invalid credentials:** 

    Email: jane.doe@gmail.com

    Password: WrongPassword

- **Empty credentials:**

    Email: ""

    Password: ""