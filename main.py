import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.markdown("""
    <style>
    body {
        background-color: #0E1117;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

df = pd.read_csv("sales_data.csv")
df['total_sales'] = df['quantity'] * df['price']

st.title("📊 Retail Sales Dashboard")

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Revenue", df['total_sales'].sum())
col2.metric("📦 Total Orders", df.shape[0])
col3.metric("🏙️ Cities", df['city'].nunique())

city = st.selectbox("Select City", ["All"] + list(df['city'].unique()))

if city != "All":
    df = df[df['city'] == city]

st.subheader("📊 Sales by Product")
st.bar_chart(df.groupby('product')['total_sales'].sum())

st.subheader("📈 Sales Trend")
st.line_chart(df.groupby('order_date')['total_sales'].sum())

st.subheader("🧾 Category Distribution")
st.write(df.groupby('category')['total_sales'].sum())