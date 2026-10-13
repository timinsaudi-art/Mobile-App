import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Set page layout to adjust nicely to phone screens
st.set_page_config(page_title="My Dashboard", layout="wide")
st.title("📊 My Personal Dashboard")

# 2. Load your exported data
@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    return df

df = load_data()

# 3. Create an interactive filter/dropdown
st.sidebar.header("Filter Options")
# Replace 'CategoryColumn' with an actual column name from your data.csv
if 'CategoryColumn' in df.columns:
    categories = df['CategoryColumn'].unique()
    selected_cat = st.sidebar.selectbox("Select Category", categories)
    filtered_df = df[df['CategoryColumn'] == selected_cat]
else:
    filtered_df = df

# 4. Display a dynamic data metric and chart
st.metric(label="Total Rows Filtered", value=len(filtered_df))

# Replace 'X_Column' and 'Y_Column' with your actual column headings
if len(df.columns) >= 2:
    fig = px.bar(filtered_df, x=df.columns[0], y=df.columns[1], title="My Interactive Chart")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write("Data loaded successfully! Add more columns to generate a custom chart.")
