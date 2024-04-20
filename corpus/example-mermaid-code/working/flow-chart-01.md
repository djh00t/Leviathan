graph TD;
    A[Start] --> B{Decision?};
    B -->|Yes| C[Process 1];
    B -->|No| D[Process 2];
    C --> D[End];
