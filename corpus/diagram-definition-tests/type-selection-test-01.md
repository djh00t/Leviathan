### General Task Description
**Task: Market Share Distribution of Smartphone Manufacturers**

#### Description
Develop a diagram to display the market share distribution among leading smartphone manufacturers globally. The chart should visually represent the market share percentage held by each major brand, such as Samsung, Apple, Huawei, Xiaomi, and other smaller brands.

#### Expected Result
* **Structure:** Dependent on the chart type chosen:
  - **Pie/Doughnut Chart:** Each segment represents a different smartphone manufacturer.
  - **Bar Chart/Stacked Bar Chart:** Each bar or stacked segment represents a different manufacturer.
* **Labels:** Each segment/bar should be clearly labeled with the manufacturer's name and the percentage of market share they hold.
* **Semantic Accuracy:** The size of each segment/bar should accurately reflect the company's share of the market relative to the total.
* **Completeness:** The diagram should include all major players in the smartphone market that collectively hold significant market share.
* **Mermaid Examples:**
  - **Pie Chart:**
    ```mermaid
    pie
        title Smartphone Market Share in 2024
        "Samsung": 30
        "Apple": 25
        "Huawei": 15
        "Xiaomi": 10
        "Other": 20
    ```
  - **Bar Chart:**
    ```mermaid
    bar
        title Smartphone Market Share in 2024
        "Samsung", 30
        "Apple", 25
        "Huawei", 15
        "Xiaomi", 10
        "Other", 20
    ```
  - **Doughnut Chart:**
    ```mermaid
    pie
        title Smartphone Market Share in 2024
        "Samsung": 30
        "Apple": 25
        "Huawei": 15
        "Xiaomi": 10
        "Other": 20
        pieConfig {
        innerRadius: 50%  // Vary this value for different doughnut sizes
        }
    ```
* **Additional Notes:** 
  - Use distinct colors for each manufacturer to enhance readability and differentiation. Consider providing a legend if the diagram includes many small segments representing other smaller manufacturers.
  - The actual values assigned to each smartphone manufacturer are not critical when evaluating results of this test; focus on the structure, labels, completeness, and the appropriate chart type being chosen.

#### Scoring Weights
* **Component Matching:** 40%
* **Syntax Correctness:** 20%
* **Semantic Accuracy:** 20%
* **Completeness:** 20%
* **Extra Elements:** Deduct 5 points for each unnecessary element.

#### Chart Type Appropriateness Ranking
1. **Pie Chart:** Most appropriate for displaying parts of a whole, making it easy to understand the proportion each manufacturer holds in the market.
2. **Doughnut Chart:** Similar to pie charts but may be considered slightly more visually appealing; functionally equivalent for this use case.
3. **Bar Chart:** Effective for comparison, especially if many manufacturers are involved; it allows for easier reading of exact market share percentages.
4. **Stacked Bar Chart:** Less ideal unless additional categorization (like regional market share) is needed.

