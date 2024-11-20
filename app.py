import streamlit as st
import pandas as pd
import pickle

# Load the saved rules from the pickle file
with open('apriori_rules.pkl', 'rb') as f:
    saved_rules = pickle.load(f)

# Load the rules DataFrame
rules_df = pd.read_csv('Association_rules.csv')

# Function to recommend products based on a selected product
def recommend_products(product, rules_df, top_n=5):
    # Filter recommendations where the base item matches the product
    recommendations = rules_df[rules_df['Base Item'].apply(lambda x: product in x)]
    
    # Sort by highest confidence
    recommendations = recommendations.sort_values(by='Confidence', ascending=False)
    
    return recommendations.head(top_n)

# List of predefined products
products = [
    "Chocolate Cake", "Lemon Cake", "Casino Cake", "Opera Cake", "Strawberry Cake", 
    "Truffle Cake", "Chocolate Eclair", "Coffee Eclair", "Vanilla Eclair", "Napolean Cake", 
    "Almond Tart", "Apple Pie", "Apple Tart", "Apricot Tart", "Berry Tart", "Blackberry Tart", 
    "Blueberry Tart", "Chocolate Tart", "Cherry Tart", "Lemon Tart", "Pecan Tart", 
    "Ganache Cookie", "Gongolais Cookie", "Raspberry Cookie", "Lemon Cookie", 
    "Chocolate Meringue", "Vanilla Meringue", "Marzipan Cookie", "Tuile Cookie", 
    "Walnut Cookie", "Almond Croissant", "Apple Croissant", "Apricot Croissant", 
    "Cheese Croissant", "Chocolate Croissant", "Apricot Danish", "Apple Danish", 
    "Almond Twist", "Almond Bear_Claw", "Blueberry Danish", "Lemon Lemonade", 
    "Raspberry Lemonade", "Orange Juice", "Green Tea", "Bottled Water", "Hot Coffee", 
    "Chocolate Coffee", "Vanilla Frappucino", "Cherry Soda", "Single Espresso"
]

# Streamlit App
st.title("Product Recommendation System")

# Dropdown menu for product selection
product = st.selectbox("Select a product:", options=products)

# Slider to select the number of recommendations
top_n = st.slider("Select the number of recommendations:", min_value=1, max_value=10, value=5)

# Button to trigger recommendation
if st.button("Get Recommendations"):
    recommendations = recommend_products(product, rules_df, top_n)
    
    if not recommendations.empty:
        # Display recommendations as a DataFrame
        st.subheader("Recommendations as DataFrame:")
        st.dataframe(recommendations)
        
        # Display names of recommended products
        st.subheader("Recommended Products:")
        for item in recommendations['Add Item']:
            # Cleanly display the product name
            product_name = str(item).strip("(')").replace("',", "")
            st.write(f"- {product_name}")
    else:
        st.warning("No recommendations found for the selected product.")
