# Market Basket Analysis

## Overview
This project focuses on **Market Basket Analysis (MBA)**, a data mining technique used to uncover associations between products frequently purchased together by customers. The goal is to identify frequent itemsets (sets of products that appear together often) and generate association rules that can help improve product recommendations, inventory management, and targeted marketing strategies.

The project enhances the classic Apriori algorithm with optimizations such as parallel computing, rule pruning, and customer segmentation through clustering. The results are visualized and interacted with via a **Streamlit interface** for easier insights.

## Key Features
- **Market Basket Analysis** using the Apriori algorithm to uncover frequent itemsets and generate association rules.
- **Optimizations** like parallel processing and rule pruning to handle large datasets efficiently.
- **Customer Segmentation** using K-means clustering to provide personalized insights.
- **Azure Cloud Integration** for scalable data storage and processing.
- **Streamlit Dashboard** for visualizing and interacting with the results.




## Data Collection & Preprocessing

The dataset consists of transaction data that includes:
- **Transaction IDs**: Unique identifiers for each transaction.
- **Product IDs/Names**: The products bought in each transaction.
- **Quantity Purchased**: Number of units of each product.



### Preprocessing Steps:
1. **Data Cleaning**: Handling missing values and removing duplicates.
2. **Data Transformation**: Conversion of transaction data into a binary matrix format for MBA analysis.

## Market Basket Analysis

The **Apriori algorithm** is used to identify frequent itemsets and generate association rules. Key metrics include:
- **Support**: The proportion of transactions containing an itemset.
- **Confidence**: The likelihood of purchasing one item given that another is purchased.
- **Lift**: The ratio of observed support to expected support if the items were independent.

### Optimizations:
- **Parallel Processing**: Using Azure Databricks for distributed computing to speed up analysis.
- **Rule Pruning**: Filtering out low-confidence and low-lift rules to retain only meaningful insights.

## Azure Cloud Integration

Azure was used to:
- Store datasets in **BlobStorage** for easy access and secure management.
- Run **Apriori Algorithm** on **Azure Databricks** to utilize parallel computing.
- Track experiments and optimize models using **Azure Machine Learning**.

## Customer Segmentation with Clustering

To enhance the quality of the analysis, **K-means clustering** was applied to segment customers based on their purchasing behavior. This allowed for more personalized recommendations.

### Clustering Process:
1. **Feature Selection**: Choosing relevant features like product categories, quantities, and purchase frequency.
2. **K-means Algorithm**: Grouping customers with similar purchasing patterns.
3. **Apriori on Clusters**: Applying the Apriori algorithm separately to each cluster for more targeted insights.


- **Visualize Association Rules**: Display rules with metrics such as support, confidence, and lift.
- **Explore Clustering Insights**: View customer segments and their purchasing behaviors.
- **Real-time Exploration**: Adjust parameters like minimum support and confidence to refine the results.

