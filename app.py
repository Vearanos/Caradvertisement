import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("vehicles_us.csv")

# Fill missing values & convert data types
df['paint_color'].fillna("unknown", inplace=True)
df['is_4wd'].fillna(0, inplace=True)
df['is_4wd'] = df['is_4wd'].astype(int)
df['model_year'].fillna(df['model_year'].median(), inplace=True)
df['cylinders'].fillna(df['cylinders'].mode()[0], inplace=True)
df['model_year'] = df['model_year'].astype(int)
df['cylinders'] = df['cylinders'].astype(int)

# Streamlit Header
st.header("Car Advertisement Data Analysis 🚗")

# Checkbox to filter price data
filter_expensive = st.checkbox("Show only cars priced under $50,000")

# Apply filter if checkbox is checked
if filter_expensive:
    df_filtered = df[df['price'] < 50000]
else:
    df_filtered = df

# Histogram: Distribution of Car Prices
st.subheader("Distribution of Car Prices")
fig_price = px.histogram(df_filtered, x="price", nbins=50, 
                         title="Car Price Distribution",
                         labels={"price": "Price ($)", "count": "Number of Cars"})
st.plotly_chart(fig_price)

# Scatterplot: Price vs Mileage
st.subheader("Price vs. Mileage")
fig_scatter = px.scatter(df_filtered, x="odometer", y="price", 
                         color="condition", 
                         title="Car Price vs. Mileage",
                         labels={"odometer": "Mileage (miles)", "price": "Price ($)"})
st.plotly_chart(fig_scatter)
