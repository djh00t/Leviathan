# Flowchart Diagram Documentation

## Diagram Type: Entity Relationship Diagram

### Data Presentation Capabilities
- Database schema designs showing tables, attributes, and relationships.
- Data modeling for systems analysis and design.
- Relationship mappings between different data entities.

### Data Presentation Limitations
- Sequential or process-oriented data flows which are better represented by flowcharts or sequence diagrams.
- Non-structured data that doesn't fit into relational database concepts, like unstructured text.
- Data without clear relationships or discrete entities, such as time series data.

## Task Descriptions

### Task #1 - Detailed Description (Complex Database Schema)

#### Description
Design an ER diagram for an e-commerce platform that includes the following entities and relationships:
- **User**: Attributes include `UserID`, `Username`, `Password`, `Email`.
- **Product**: Attributes include `ProductID`, `ProductName`, `Price`, `CategoryID`.
- **Category**: Attributes include `CategoryID`, `CategoryName`.
- **Order**: Attributes include `OrderID`, `UserID`, `OrderDate`, `TotalAmount`.
- Relationships:
  - Users can place multiple orders (`User` to `Order`: One-to-Many).
  - Each order can contain multiple products (`Order` to `Product`: Many-to-Many through `OrderDetail`).
  - Products belong to one category (`Product` to `Category`: Many-to-One).

#### Expected Result

* **Structure:** Comprehensive representation of all entities with their attributes and relationships.
* **Labels:** All entity names and their attribute names as specified.
* **Semantic Accuracy:** Correct representation of relationship types (e.g., one-to-many, many-to-many).
* **Completeness:** All entities and relationships described must be included.
* **Additional Notes:** Pay special attention to the implementation of the `OrderDetail` entity for the many-to-many relationship.

#### Scoring Weights

* **Component Matching:** 40%
* **Syntax Correctness:** 20%
* **Semantic Accuracy:** 30%
* **Completeness:** 10%
* **Extra Elements:** -5 points per extraneous element

### Task #2 - Moderately Detailed Description (Library System Schema)

#### Description
Create an ER diagram for a library system, focusing on books and loans. The entities are:
- **Book**: Attributes include `BookID`, `Title`, `Author`, `ISBN`.
- **Member**: Attributes include `MemberID`, `Name`, `Email`.
- **Loan**: Attributes include `LoanID`, `BookID`, `MemberID`, `LoanDate`, `ReturnDate`.
- Relationships:
  - A member can borrow multiple books (`Member` to `Loan`: One-to-Many).
  - Each loan refers to a single book (`Loan` to `Book`: Many-to-One).

#### Expected Result

* **Structure:** Clear depiction of entities and their relationships.
* **Labels:** Attributes of each entity are accurately labeled.
* **Semantic Accuracy:** Correct relationship mappings with appropriate cardinalities.
* **Completeness:** Diagram must reflect all components as listed.
* **Additional Notes:** Emphasis on clarity in the relationships between members, loans, and books.

#### Scoring Weights

* **Component Matching:** 50%
* **Syntax Correctness:** 20%
* **Semantic Accuracy:** 20%
* **Completeness:** 10%
* **Extra Elements:** -5 points per extraneous element

### Task #3 - Vague Description (School System Entities)

#### Description
Sketch out an ER diagram for a school system. Include tables for students, teachers, and classes. Add in some typical relationships, but don't worry about being too specific about attributes or keys.

#### Expected Result

* **Structure:** Basic layout with essential entities.
* **Labels:** General labels for entities such as 'Student', 'Teacher', 'Class'.
* **Semantic Accuracy:** Depiction of typical relationships like teachers teach classes, students enroll in classes.
* **Completeness:** Include at least the basic entities and relationships.
* **Additional Notes:** The focus is on the general structure rather than detailed attributes.

#### Scoring Weights

* **Component Matching:** 30%
* **Syntax Correctness:** 30%
* **Semantic Accuracy:** 30%
* **Completeness:** 10%
* **Extra Elements:** -5 points per extraneous element
