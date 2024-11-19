## Market Basket Analysis Using Azure Cloud

### Overview
This project implements **Market Basket Analysis** using transaction data to uncover associations between frequently purchased items. It utilizes **association rule mining** to derive insights for cross-selling, up-selling, and promotional strategies. The analysis was performed on Azure Cloud for scalability and efficiency.

### Key Features
- **Association Rules**: Extracts item relationships based on support, confidence, and lift metrics.
- **Azure Integration**: Data preprocessing and analytics performed on Azure for large-scale transaction datasets.
- **Actionable Insights**: Highlights frequent item pairs and co-purchase trends.

---

### Assocation Rules Description
The dataset contains transaction records with the following columns:
- **Base Item**: Primary product in a transaction.
- **Add Item**: Associated product in the same transaction.
- **Confidence**: Probability that the Add Item is purchased when the Base Item is bought.
- **Lift**: Strength of the association between Base and Add Item.

**Sample Dataset:**

| **Base Item**            | **Add Item**              | **Confidence** | **Lift**   |
|---------------------------|---------------------------|----------------|------------|
| Almond Twist             | Apple Pie                | 0.497          | 4.934      |
| Apple Pie                | Almond Twist             | 0.496          | 4.934      |
| Almond Twist             | Coffee Eclair            | 0.511          | 3.603      |
| Coffee Eclair            | Almond Twist             | 0.362          | 3.603      |
| Raspberry Cookie         | Raspberry Lemonade       | 0.430          | 4.796      |

---

### Tools and Technologies
- **Azure Cloud**: For data storage, processing, and analytics.
- **Python**: Data preprocessing and association rule mining.
- **Libraries**: 
  - `pandas` for data manipulation.
  - `apyori` for association rule mining.
  - `matplotlib` and `seaborn` for visualizations.
- **Jupyter Notebooks**: Interactive environment for experimentation.

---

### Key Results
- **Strong Item Associations**: 
  - *Almond Twist → Coffee Eclair*: Confidence = 51%, Lift = 3.6.
  - *Raspberry Cookie → Raspberry Lemonade*: Confidence = 43%, Lift = 4.8.
- **Cross-Sell Opportunities**: Frequent pairs like *Walnut Cookie → Vanilla Frappuccino* provide opportunities for combo promotions.
- **Promotional Insights**: High-lift pairs indicate profitable associations for targeted discounts.

---





### Insights and Recommendations
1. Focus on cross-selling *high-lift* pairs.
2. Develop targeted promotions for frequently purchased combinations.
3. Use Azure's scalable infrastructure for real-time analytics on larger datasets.

---

