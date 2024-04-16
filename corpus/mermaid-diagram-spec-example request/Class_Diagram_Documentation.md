
# Class Diagram Documentation

## Diagram Type: Class Diagram

### Data Presentation Capabilities
- Suitable for modeling the structure of systems by showing classes, attributes, operations, and the relationships among objects.

### Data Presentation Limitations
- Not suitable for illustrating the dynamic aspects of systems, such as time-based behaviors or sequential interactions.

## Task Descriptions

### Task #1: Detailed Class Diagram for an Online Library System
- **Description:** Develop a class diagram for an online library system. Include classes such as 'Book', 'User', 'Loan', and 'Author'. 'Book' should have attributes like title, author, and ISBN, and methods like checkAvailability(). 'User' should have userID, name, and methods like borrowBook(). 'Author' should have name, list of books, and bio. Relationships include User borrows Loan, Loan involves Book, and Book written by Author.
- **Data:** Classes: Book(title, author, ISBN, checkAvailability()), User(userID, name, borrowBook()), Loan(issueDate, returnDate), Author(name, books, bio). Relationships: User -- Loan, Loan -- Book, Book -- Author.

### Task #2: Simple Class Diagram for a Blog System
- **Description:** Sketch a class diagram for a blog system featuring classes for 'Post', 'Comment', and 'User'. Each 'Post' has multiple 'Comments', and each 'Comment' is made by a 'User'.
- **Data:** Classes: Post(title, content, postDate), Comment(content, commentDate, author), User(username, email). Relationships: Post "1" -- "*" Comment, Comment "*" -- "1" User.

### Task #3: Basic Class Diagram for a Shopping Cart
- **Description:** Draw a class diagram with minimal details for a shopping cart. Include classes like 'Product' and 'Cart', with simple attributes and basic relationships.
- **Data:** Classes: Product(name, price), Cart(items). Relationships: Cart contains Product.

