
# Sequence Diagram Documentation

## Diagram Type: Sequence Diagram

### Data Presentation Capabilities
- Suitable for presenting interactions among processes or objects in a sequential order, focusing on the messages that are passed between entities.

### Data Presentation Limitations
- Not suitable for displaying non-linear processes without a clear sequence of interactions or for showing hierarchical relationships.

## Task Descriptions

### Task #1: Detailed Sequence Diagram for E-commerce Transaction
- **Description:** Create a sequence diagram for an e-commerce transaction. Start with the 'Customer' who sends a 'Search Product' request to the 'Server'. The 'Server' responds with 'Product List'. The customer then sends 'Add to Cart', receives confirmation 'Cart Updated', and then 'Proceeds to Checkout', receives 'Payment Options', chooses 'Make Payment', and finally receives 'Transaction Confirmation'.
- **Data:** Customer -> Server: Search Product -> Server -> Customer: Product List -> Customer -> Server: Add to Cart -> Server -> Customer: Cart Updated -> Customer -> Server: Proceed to Checkout -> Server -> Customer: Payment Options -> Customer -> Server: Make Payment -> Server -> Customer: Transaction Confirmation.

### Task #2: Technical Support Interaction
- **Description:** Draft a sequence diagram for a technical support call. The customer initiates the call, the support agent provides a greeting, and requests the issue details. The customer describes the problem, and the support agent offers a solution.
- **Data:** Customer -> Support Agent: Initiate Call -> Support Agent -> Customer: Greeting and Request for Details -> Customer -> Support Agent: Describe Problem -> Support Agent -> Customer: Offer Solution.

### Task #3: User Login Sequence
- **Description:** Create a sequence diagram for a user login. The user sends login credentials, the system validates them and either grants access or denies it.
- **Data:** User -> System: Send Credentials -> System -> User: {Credentials Valid: Grant Access, Credentials Invalid: Deny Access}.

