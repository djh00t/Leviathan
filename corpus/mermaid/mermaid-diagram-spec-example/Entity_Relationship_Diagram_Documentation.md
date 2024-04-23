
# Entity Relationship Diagram Documentation

## Suitable Data Types for Entity Relationship Diagram
- Database schema designs showing tables, attributes, and relationships.
- Data modeling for systems analysis and design.
- Relationship mappings between different data entities.

## Unsuitable Data Types for Entity Relationship Diagram
- Sequential or process-oriented data flows which are better represented by flowcharts or sequence diagrams.
- Non-structured data that doesn't fit into relational database concepts, like unstructured text.
- Data without clear relationships or discrete entities, such as time series data.

## Task #1 - Detailed Description (Complex Database Schema)
Design an ER diagram for an e-commerce platform that includes the following entities and relationships:
- **User**: Attributes include `UserID`, `Username`, `Password`, `Email`.
- **Product**: Attributes include `ProductID`, `ProductName`, `Price`, `CategoryID`.
- **Category**: Attributes include `CategoryID`, `CategoryName`.
- **Order**: Attributes include `OrderID`, `UserID`, `OrderDate`, `TotalAmount`.
- Relationships:
  - Users can place multiple orders (`User` to `Order`: One-to-Many).
  - Each order can contain multiple products (`Order` to `Product`: Many-to-Many through `OrderDetail`).
  - Products belong to one category (`Product` to `Category`: Many-to-One).

## Task #2 - Moderately Detailed Description (Library System Schema)
Create an ER diagram for a library system, focusing on books and loans. The entities are:
- **Book**: Attributes include `BookID`, `Title`, `Author`, `ISBN`.
- **Member**: Attributes include `MemberID`, `Name`, `Email`.
- **Loan**: Attributes include `LoanID`, `BookID`, `MemberID`, `LoanDate`, `ReturnDate`.
- Relationships:
  - A member can borrow multiple books (`Member` to `Loan`: One-to-Many).
  - Each loan refers to a single book (`Loan` to `Book`: Many-to-One).

## Task #3 - Vague Description (School System Entities)
Sketch out an ER diagram for a school system. Include tables for students, teachers, and classes. Add in some typical relationships, but don't worry about being too specific about attributes or keys.
