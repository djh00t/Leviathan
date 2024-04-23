# State Diagram Documentation

## Diagram Type: State Diagram

## Suitable Data Types for State Diagram
- System behaviors and state changes based on events.
- Workflow processes where states change based on actions or conditions.
- Life cycles of objects where the state reflects different phases of existence.
- Suitable for modeling the state changes in a system or an object over time, reflecting different states and transitions based on events.

## Unsuitable Data Types for State Diagram
- Not suitable for illustrating static structures like class relationships, non-temporal data, or physical layouts.
- Non-dynamic datasets without clear state changes or transitions, such as static data (e.g., demographic information).
- Hierarchical data structures, like organizational charts.
- Continuous quantitative data that does not have discrete state changes (e.g., temperature readings over time).

## Task #1 - Detailed Description (High Precision State Diagram)
Create a state diagram that models a simple login process for a web application. The process includes the following states and transitions:
- **Start**: Initial state when the user accesses the login page.
- **Entering Credentials**: User is prompted to enter username and password.
- **Credentials Submitted**: After user submits the credentials.
  - Transition to **Valid Credentials** if the credentials are correct.
  - Transition to **Invalid Credentials** if they are not.
- **Valid Credentials**: Leads to **Access Granted**.
- **Invalid Credentials**: Leads back to **Entering Credentials**, including a transition that increments a "retry" counter.
- **Access Granted**: User successfully logs in.
- **Session Timeout**: From **Access Granted**, if the user is inactive for a predefined period.
- End states: **Logged Out** from **Access Granted** upon user action or from **Session Timeout**.

## Task #2 - Moderately Detailed Description (User Authentication Flow)
Design a state diagram for an email system's user authentication process including states for multi-factor authentication. Here's the flow:
- **Start**: User hits the login screen.
- **Credentials Check**: User inputs their details.
  - If correct, proceed to **Two-Factor Authentication**.
  - If incorrect, return to **Start** and show an error.
- **Two-Factor Authentication**: User must confirm identity via phone or email.
  - If confirmed, proceed to **Logged In**.
  - If failed, return to **Credentials Check** (with a limit on retries).
- **Logged In**: Access to the mailbox.
- **Logged Out**: User opts to log out or due to inactivity.

## Task #3 - Vague Description (Simple Sign-in Process)
Make a state diagram showing a user sign-in process. It has states for when they start, input details, get it wrong, and finally get into their account. Make sure there's a way back if they mess up their password.
