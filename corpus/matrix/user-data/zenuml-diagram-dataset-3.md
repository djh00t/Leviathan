- User: Opens Login Page
- User -> WebServer: Enters Username and Password
- WebServer -> AuthServer: Sends Credentials for Verification
- AuthServer -> Database: Checks Credentials
- Database -> AuthServer: Returns Verification Result
- AuthServer -> WebServer:
  - If credentials are invalid: Returns "Authentication Failed"
  - If credentials are valid: Returns "Authentication Successful"
- WebServer -> User:
  - If Authentication Failed:
    - User -> WebServer: Chooses to Try Again or Forgot Password
    - If Try Again:
      - User re-enters credentials
      - Sequence repeats
    - If Forgot Password:
      - WebServer -> User: Sends Password Reset Instructions
  - If Authentication Successful:
    - WebServer -> User: Prompts for Multi-factor Authentication Code
    - User -> WebServer: Enters MFA Code Received on Phone
    - WebServer -> MFAService: Validates MFA Code
    - MFAService -> WebServer:
      - If MFA Code is invalid: Returns "MFA Validation Failed"
      - If MFA Code is valid: Returns "MFA Validation Successful"
    - WebServer -> User:
      - If MFA Validation Failed:
        - User -> WebServer: Requests New MFA Code or Contacts Support
      - If MFA Validation Successful:
        - User is granted access to secure areas of the application
        - WebServer -> User: Navigates User to Dashboard

Chart Type: flowchart
User Role: Developer
User Story: As a developer, I want to understand the user authentication process in a web application, so that I can implement secure login functionality.