### Sequence Diagram Task Description
**Task: E-commerce Checkout Process**

#### Description
Create a detailed sequence diagram to illustrate the interaction between a customer, web application, payment service, and inventory system during the checkout process in an e-commerce platform.

#### Expected Result
* **Structure:** A sequence of interactions from adding items to the cart to receiving the order confirmation.
* **Labels:** Clearly label each interaction with method calls and responses, such as "addItem", "calculateTotal", "processPayment", etc.
* **Semantic Accuracy:** Each interaction should correctly represent the process logic and data flow between components.
* **Completeness:** The diagram should cover the entire checkout process, including error handling and success messages.
* **Mermaid Example:**
    ```mermaid
    sequenceDiagram
        participant C as Customer
        participant W as Web Application
        participant P as Payment Service
        participant I as Inventory System
        C->>W: addItem(itemID)
        W->>I: checkInventory(itemID)
        I-->>W: confirmAvailability
        W->>C: showCart(updated)
        C->>W: checkout
        W->>P: initiatePayment(details)
        P-->>W: paymentConfirmation
        W->>I: updateInventory(orderDetails)
        I-->>W: inventoryUpdated
        W->>C: orderConfirmation
    ```
* **Additional Notes:** Ensure the timing of interactions is logically depicted to reflect real-world e-commerce checkout flows.

#### Scoring Weights
* **Component Matching:** 40%
* **Syntax Correctness:** 20%
* **Semantic Accuracy:** 20%
* **Completeness:** 20%
* **Extra Elements:** Deduct 5 points for each unnecessary element.
