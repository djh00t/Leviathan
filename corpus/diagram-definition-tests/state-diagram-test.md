### State Diagram Task Description
**Task: User Authentication System**

#### Description
Develop a comprehensive state diagram to model the user authentication process in a software application, including states from initial login attempt to successful login or failure, covering all potential outcomes.

#### Expected Result
* **Structure:** States and transitions that represent the user authentication lifecycle, including "Enter Credentials", "Credentials Validated", "Access Granted", and "Access Denied".
* **Labels:** Each state and transition must be clearly labeled with actions (e.g., "submit", "redirect", "logout").
* **Semantic Accuracy:** Correctly represent the flow and logic of user authentication, including timeouts and retries.
* **Completeness:** Diagram must include all possible states and transitions during the authentication process.
* **Mermaid Example:**
    ```mermaid
    stateDiagram-v2
        [*] --> LoginScreen
        LoginScreen --> CredentialsEntered: enter credentials
        CredentialsEntered --> Validation: submit
        Validation --> AccessGranted: valid
        Validation --> AccessDenied: invalid
        AccessDenied --> [*]: end session
        AccessDenied --> LoginScreen: retry
        AccessGranted --> UserDashboard: access granted
        UserDashboard --> Logout: logout
        Logout --> [*]: end session
        UserDashboard --> Timeout: session timeout
        Timeout --> [*]: end session
    ```
* **Additional Notes:** Consider including security features like CAPTCHA or multi-factor authentication as additional states if relevant.

#### Scoring Weights
* **Component Matching:** 40%
* **Syntax Correctness:** 20%
* **Semantic Accuracy:** 20%
* **Completeness:** 20%
* **Extra Elements:** Deduct 5 points for each unnecessary element.

