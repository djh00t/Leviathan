# Sequence Diagram Documentation

## Diagram Type: Sequence Diagram

### Data Presentation Capabilities
- Ideal for detailing the interactions among processes or objects in a sequential order, focusing on the exchange of messages between entities.

### Data Presentation Limitations
- Not suited for displaying non-linear processes or hierarchical relationships that do not involve clear sequential interactions.

## Task Descriptions

### Task #1: Detailed Sequence Diagram for E-commerce Transaction

#### Description
Create a sequence diagram for an e-commerce transaction that captures the sequence of interactions from searching for a product to receiving a transaction confirmation.

#### Expected Result

* **Structure:** Sequential flow of messages between Customer and Server.
* **Labels:** Accurate labeling of each interaction point (e.g., 'Search Product', 'Add to Cart', 'Make Payment').
* **Semantic Accuracy:** Each message correctly represents its corresponding action within the transaction process.
* **Completeness:** All steps from product search to transaction confirmation are included.
* **Additional Notes:** Ensure that the timing and order of messages reflect a realistic e-commerce transaction.

#### Scoring Weights

* **Component Matching:** 40%
* **Syntax Correctness:** 20%
* **Semantic Accuracy:** 30%
* **Completeness:** 10%
* **Extra Elements:** Deduct 5 points for each unnecessary element included.

### Task #2: Technical Support Interaction

#### Description
Draft a sequence diagram to represent a typical technical support call from initiation to solution offer.

#### Expected Result

* **Structure:** Clear depiction of the exchange of messages between Customer and Support Agent.
* **Labels:** Each message step accurately labeled (e.g., 'Initiate Call', 'Describe Problem', 'Offer Solution').
* **Semantic Accuracy:** Proper representation of the logical flow of a support call.
* **Completeness:** Includes all phases from call initiation to the offering of a solution.
* **Additional Notes:** Pay particular attention to the realism and practicality of the interaction sequence.

#### Scoring Weights

* **Component Matching:** 50%
* **Syntax Correctness:** 20%
* **Semantic Accuracy:** 20%
* **Completeness:** 10%
* **Extra Elements:** Deduct 5 points per extraneous element.

### Task #3: User Login Sequence

#### Description
Create a sequence diagram detailing the user login process, from sending login credentials to the system's response based on the validation of those credentials.

#### Expected Result

* **Structure:** Linear sequence of message exchanges between User and System.
* **Labels:** Correctly labeled messages reflecting login actions (e.g., 'Send Credentials', 'Grant Access', 'Deny Access').
* **Semantic Accuracy:** Accurately depicts the decision-making process based on credential validation.
* **Completeness:** All key interactions related to the login process are covered.
* **Additional Notes:** Emphasize clarity in how the system handles both valid and invalid credentials.

#### Scoring Weights

* **Component Matching:** 30%
* **Syntax Correctness:** 30%
* **Semantic Accuracy:** 30%
* **Completeness:** 10%
* **Extra Elements:** Deduct 5 points for any non-essential components.
