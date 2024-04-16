
# State Diagram Documentation

## Diagram Type: State Diagram

### Data Presentation Capabilities
- Suitable for modeling the state changes in a system or an object over time, reflecting different states and transitions based on events.

### Data Presentation Limitations
- Not suitable for illustrating static structures like class relationships, non-temporal data, or physical layouts.

## Task Descriptions

### Task #1: Detailed State Diagram for Order Processing System
- **Description:** Create a state diagram that outlines the stages of an order processing system. States include 'Order Placed', 'Payment Processed', 'Order Shipped', 'Order Delivered', and 'Order Closed'. Transitions occur based on completion of the previous step. Include decision points such as 'Payment Successful?' leading to either 'Order Shipped' or 'Payment Rejected'.
- **Data:** States: Order Placed -> Payment Processed -> Payment Successful? -> {Yes: Order Shipped, No: Payment Rejected} -> Order Delivered -> Order Closed.

### Task #2: Simplified State Diagram for User Authentication
- **Description:** Draft a simplified state diagram for user authentication. Start with 'Login Attempt', transition to 'Credentials Verified', leading to either 'Access Granted' or 'Access Denied'.
- **Data:** States: Login Attempt -> Credentials Verified -> {Credentials Valid: Access Granted, Credentials Invalid: Access Denied}.

### Task #3: Basic State Diagram for a Light Switch
- **Description:** Provide a basic state diagram for a light switch with minimal details. Include states like 'Off' and 'On', and the transitions triggered by 'Switch Toggled'.
- **Data:** States: Off --Switch Toggled--> On --Switch Toggled--> Off.

