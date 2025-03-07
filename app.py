# Load dataset
import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv("vehicles_us.csv")


# Replace NaN values in specified columns
df = df.assign(
    model_year=df['model_year'].fillna('unknown'),
    cylinders=df['cylinders'].fillna('unknown'),
    odometer=df['odometer'].fillna(0),
    paint_color=df['paint_color'].fillna('unknown'),
    is_4wd=df['is_4wd'].fillna(0)
)


# Convert model_year and cylinders columns to integer type
df['model_year'] = df['model_year'].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)
df['cylinders'] = df['cylinders'].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)

# Remove outliers from 'model_year' column
df = df[df['model_year'] > 1900]
df = df[df['model_year'] < 2023]

# Remove outliers from 'price' column
df = df[df['price'] > 1000]
df = df[df['price'] < 100000]

# Remove outliers from 'odometer' column
df = df[df['odometer'] > 1000]
df = df[df['odometer'] < 400000]

# Group by 'model' and calculate the median 'model_year' for each group
median_years = df.groupby('model')['model_year'].median()

# Group by 'model' and calculate the median 'cylinders' for each group
median_cylinders = df.groupby('model')['cylinders'].median()

# Group by 'model_year' and calculate the median 'odometer' for each group
median_odometer = df.groupby('model_year')['odometer'].median()

# Streamlit Header
st.header("Car Advertisement Data Analysis")

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
