# C4 Diagrams Documentation

## Diagram Type: C4 Diagram

### Data Presentation Capabilities
- C4 diagrams are designed to represent software architecture at different levels of abstraction, including system context, containers, components, and deployment scenarios.
- Suitable for visualizing system architectures, showing how various components interact within software applications, systems, or services.
- Helps stakeholders understand software systems through clear, hierarchical representations.

### Data Presentation Limitations
- Less effective for non-architectural representations such as process flows, real-time interactions, or detailed data models.
- Not intended for depicting network infrastructure details or physical deployment beyond software components and containers.

## Task Descriptions

### Task #1 - Detailed Description (System Context Diagram)
#### Goal:
Create a detailed C4 System Context diagram for an Internet Banking System, showcasing all external and internal system interactions.
#### Expected Result:
- **Structure:** Clear identification and representation of all system entities and their interactions.
- **Labels:** Each entity (systems, users) must be correctly labeled with roles and interactions detailed.
- **Semantic Accuracy:** Accurately represent the nature of each relationship (e.g., data flow, control flow).
- **Completeness:** All relevant external users, systems, and system interactions are depicted.
- **Mermaid Example:**
    ```mermaid
    graph TD;
        A[Internet Banking System] -->|uses| B[Database]
        A -->|interacts with| C[Payment Gateway]
        D[Customer] -->|accesses| A
        E[External Services] -->|integrates with| A
    ```
- **Additional Notes:** Ensure clarity in the separation of boundaries and system layers.
#### Scoring Weights:
- **Component Matching:** 30%
- **Syntax Correctness:** 20%
- **Semantic Accuracy:** 30%
- **Completeness:** 20%
- **Extra Elements:** Deduct 5 points for each unnecessary element.

### Task #2 - Semi-Detailed Description (Container Diagram)
#### Goal:
Design a semi-detailed C4 Container diagram for the Internet Banking System, focusing on major software applications and data persistence solutions.
#### Expected Result:
- **Structure:** Illustrate main containers such as web applications, mobile apps, databases, and backend services.
- **Labels:** Properly label each container with its technology stack and primary responsibilities.
- **Semantic Accuracy:** Correctly depict the data flow between containers.
- **Completeness:** Include all primary containers that contribute to the system's functionality.
- **Mermaid Example:**
    ```mermaid
    graph TD;
        A[Web Application] -->|data| B[Application Server]
        B -->|persistent storage| C[Database]
        B -->|authentication| D[Authentication Server]
    ```
- **Additional Notes:** Highlight external interfaces and dependencies.
#### Scoring Weights:
- **Component Matching:** 40%
- **Syntax Correctness:** 15%
- **Semantic Accuracy:** 25%
- **Completeness:** 20%
- **Extra Elements:** Deduct 5 points for any irrelevant components.

### Task #3 - Vague Description (Deployment Diagram)
#### Goal:
Sketch out a basic C4 Deployment diagram for the Internet Banking System, showing its deployment across different hardware or virtual environments.
#### Expected Result:
- **Structure:** Identify key deployment nodes such as cloud infrastructures, servers, and client devices.
- **Labels:** Label each deployment node with relevant hardware or software environments.
- **Semantic Accuracy:** Depict the distribution of containers across the deployment nodes.
- **Completeness:** Cover all major physical or virtual environments involved in the system's operation.
- **Mermaid Example:**
    ```mermaid
    graph TD;
        A[Cloud Server] -->|hosts| B[Web Application]
        A -->|hosts| C[Database Server]
        D[Client Devices] -->|access| B
    ```
- **Additional Notes:** Emphasize on scalability and fault tolerance aspects.
#### Scoring Weights:
- **Component Matching:** 25%
- **Syntax Correctness:** 25%
- **Semantic Accuracy:** 25%
- **Completeness:** 25%
- **Extra Elements:** Deduct 10 points for any superfluous details.

## General Usage
- C4 diagrams are primarily used in software development for architectural documentation and communication across technical and non-technical stakeholders.
- They facilitate discussions about architectural decisions, system boundaries, and integration points.

### Advanced Configuration and Styling
- Mermaid supports advanced customization in C4 diagrams, allowing adjustments in layout, style, and interactions, enhancing the diagrams' effectiveness and readability.

### Practical Examples and Use Cases
- **System Context Diagrams:** Useful for stakeholders to understand external interactions at a system level.
- **Container Diagrams:** Helpful for developers and architects to understand the high-level technology choices and architecture.
- **Deployment Diagrams:** Crucial for operations and DevOps teams to manage and understand the deployment environment and infrastructure.

This documentation provides a clear framework for creating and evaluating C4 Diagrams, ensuring that they effectively communicate the architecture of the systems they represent.
