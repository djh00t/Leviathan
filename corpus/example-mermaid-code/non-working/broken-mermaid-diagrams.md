
# Collection of Broken Mermaid Diagrams

This document contains 25 intentionally incorrect or broken Mermaid diagrams for testing and training purposes. Each diagram has one or more errors that prevent it from rendering correctly.

## Diagram 1 - Flowchart with Missing Arrow
```mermaid
graph TD;
    A-->B
    B-- C
    C-->D
```

## Diagram 2 - Sequence Diagram with Incorrect Syntax - Semicolon after `sequenceDiagram`
```mermaid
sequenceDiagram;
    Alice->>John: Hello John, how are you?
    John-->>Alice: Great!
```

## Diagram 3 - Gantt Chart with Mismatched Dates
```mermaid
gantt
    title A Gantt Diagram
    dateFormat  YYYY-MM-DD
    section Section
    A task           :a1, 2014-01-01, 30d
    Another task     :after a1  45d
```

## Diagram 4 - Pie Chart with Missing Values
```mermaid
pie
    title Pets
    "Dogs" : 386
    "Cats" 
    "Birds" : 45
```

## Diagram 5 - Class Diagram with Undefined Classes
```mermaid
classDiagram
    Class01 <|-- AveryLongClassThatDoesNotExist
    Class03 *-- Class04
```

## Diagram 6 - State Diagram with Invalid Transitions
```mermaid
stateDiagram-v2
    [*] --> State1
    State1 --> State2
    State2 --> State3
    State3 -!-> [*]
```

## Diagram 7 - ER Diagram with Syntax Errors
```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    CUSTOMER }|..|{ DELIVERY-ADDRESS : uses
```

## Diagram 8 - Flowchart with Undefined Node
```mermaid
graph TD;
    Start --> Stop
    Stop --> End
    End --> UndefinedNode
```

## Diagram 9 - Sequence Diagram with Missing Participant
```mermaid
sequenceDiagram
    participant Alice
    Alice->>MissingParticipant: Hi there!
```

## Diagram 10 - Gantt Chart with Overlapping Tasks
```mermaid
gantt
    title Overlapping Gantt Chart
    dateFormat  YYYY-MM-DD
    section Section 1
    Task1           :2021-01-01, 10d
    Task2           :2021-01-05, 15d
```

## Diagram 11 - Pie Chart with Incorrect Labels
```mermaid
pie
    title Favorite Programming Languages
    "Python" : 600
    "JavaScript" : 300
    "C++" : "Two Hundred"
```

## Diagram 12 - Class Diagram with Circular Inheritance
```mermaid
classDiagram
    ClassA <|-- ClassB
    ClassB <|-- ClassA
```

## Diagram 13 - State Diagram with Non-existent State
```mermaid
stateDiagram-v2
    [*] --> State1
    State1 --> MissingState
    MissingState --> [*]
```

## Diagram 14 - ER Diagram with Inconsistent Cardinality
```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER }|--|{ PRODUCT : includes
    PRODUCT ||--o{ CUSTOMER : buys
```

## Diagram 15 - Flowchart with Incoherent Flow
```mermaid
graph TD;
    Start --&gt; Middle
    Middle --x End
    Start -->|Loop Back| Start
```