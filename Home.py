import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3
import os

st.set_page_config(
    page_title="AI Financial Intelligence Platform",
    page_icon="📊",
    layout="wide"
)


from services.analytics import (
    get_transaction_summary,
    get_user_summary,
    get_transaction_by_type,
    get_state_analysis,
    get_top_users,
    get_transaction_trend,
    get_top_districts,
    get_user_engagement
)

# Setup database if it doesn't exist
conn = sqlite3.connect("phonepe_pulse.db")

if not os.path.exists("phonepe_data"):
    setup_database(conn)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stMetric {
        background-color: #F5F0FF;
        padding: 15px;
        border-radius: 10px;
        border-left: 4px solid #5F259F;
    }
    h1 {
        color: #5F259F;
        font-size: 2.5rem;
    }
    h2 {
        color: #1C1C2E;
        border-bottom: 2px solid #5F259F;
        padding-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Connect to database
conn = sqlite3.connect("phonepe_pulse.db")

# State name mapping
state_name_mapping = {
    "andaman-&-nicobar-islands": "Andaman & Nicobar Island",
    "andhra-pradesh": "Andhra Pradesh",
    "arunachal-pradesh": "Arunachal Pradesh",
    "assam": "Assam",
    "bihar": "Bihar",
    "chandigarh": "Chandigarh",
    "chhattisgarh": "Chhattisgarh",
    "dadra-&-nagar-haveli-&-daman-&-diu": "Dadra and Nagar Haveli",
    "delhi": "Delhi",
    "goa": "Goa",
    "gujarat": "Gujarat",
    "haryana": "Haryana",
    "himachal-pradesh": "Himachal Pradesh",
    "jammu-&-kashmir": "Jammu & Kashmir",
    "jharkhand": "Jharkhand",
    "karnataka": "Karnataka",
    "kerala": "Kerala",
    "ladakh": "Ladakh",
    "lakshadweep": "Lakshadweep",
    "madhya-pradesh": "Madhya Pradesh",
    "maharashtra": "Maharashtra",
    "manipur": "Manipur",
    "meghalaya": "Meghalaya",
    "mizoram": "Mizoram",
    "nagaland": "Nagaland",
    "odisha": "Odisha",
    "puducherry": "Puducherry",
    "punjab": "Punjab",
    "rajasthan": "Rajasthan",
    "sikkim": "Sikkim",
    "tamil-nadu": "Tamil Nadu",
    "telangana": "Telangana",
    "tripura": "Tripura",
    "uttar-pradesh": "Uttar Pradesh",
    "uttarakhand": "Uttarakhand",
    "west-bengal": "West Bengal"
}

# App title
st.title("AI Financial Intelligence Platform")

st.markdown("""
### Analytics • AI Insights • Financial Copilot • RBI Knowledge Base

An AI-powered financial intelligence platform built using:

- PhonePe Pulse transaction data
- SQL analytics
- Streamlit dashboards
- Gemini AI
- Retrieval-Augmented Generation (RAG)
- ChromaDB vector search
- RBI Annual Reports

Use the sidebar to explore analytics and AI-powered insights.
""")



# Sidebar filters
st.sidebar.title("Filters")

year = st.sidebar.selectbox(
    "Select Year",
    options=[2018, 2019, 2020, 2021, 2022, 2023, 2024]
)

quarter = st.sidebar.selectbox(
    "Select Quarter",
    options=[1, 2, 3, 4],
    format_func=lambda x: f"Q{x}"
)

# Summary metrics
col1, col2, col3 = st.columns(3)

df_summary = get_transaction_summary(
    year,
    quarter
)

df_users_summary = get_user_summary(
    year,
    quarter
)

with col1:
    st.metric("Total Transactions", f"{int(df_summary['total_count'][0]):,}")

with col2:
    st.metric("Total Amount", f"₹{df_summary['total_amount'][0]/1e9:.2f}B")

with col3:
    st.metric("Registered Users", f"{int(df_users_summary['total_users'][0]):,}")

# Section 1: Transaction Analysis
st.header("Transaction Analysis")

# Fetch data based on filters
df = get_transaction_by_type(
    year,
    quarter
)

# Bar chart
fig = px.bar(
    df,
    x="transaction_type",
    y="total_amount",
    title=f"Transaction Amount by Type — {year} Q{quarter}",
    color="transaction_type",
    labels={"transaction_type": "Transaction Type", "total_amount": "Total Amount (₹)"}
)

st.plotly_chart(fig)


# Pie chart
fig2 = px.pie(
    df,
    names="transaction_type",
    values="total_count",
    title=f"Transaction Count Distribution — {year} Q{quarter}"
)

st.plotly_chart(fig2)


# Section 2: State-wise Analysis
st.header("State-wise Analysis")

df_states = get_state_analysis(
    year,
    quarter
)

fig3 = px.bar(
    df_states,
    x="state",
    y="total_amount",
    title=f"Transaction Amount by State — {year} Q{quarter}",
    color="total_amount",
    color_continuous_scale="Blues"
)

fig3.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig3)

# Section 3: Geo Map
st.header("India Transaction Map")

df_states["state_mapped"] = df_states["state"].map(state_name_mapping)

fig4 = px.choropleth(
    df_states,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey="properties.ST_NM",
    locations="state_mapped",
    color="total_amount",
    color_continuous_scale="Reds",
    title=f"Transaction Amount by State — {year} Q{quarter}"
)

fig4.update_geos(fitbounds="locations", visible=False)
st.plotly_chart(fig4)


# Section 4: User Analysis
st.header("User Analysis")

df_users = get_top_users(
    year,
    quarter
)

fig5 = px.bar(
    df_users,
    x="state",
    y="total_users",
    title=f"Top 10 States by Registered Users — {year} Q{quarter}",
    color="total_users",
    color_continuous_scale="Greens"
)

fig5.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig5)

# Section 5: Growth Trend
st.header("Transaction Growth Over Time")

transaction_type = st.selectbox(
    "Select Transaction Type",
    options=["All", "Peer-to-peer payments", "Merchant payments", 
             "Recharge & bill payments", "Financial Services", "Others"]
)

df_trend = get_transaction_trend(
    transaction_type
)

df_trend["period"] = df_trend["year"].astype(str) + " Q" + df_trend["quarter"].astype(str)

fig6 = px.line(
    df_trend,
    x="period",
    y="total_amount",
    title=f"Transaction Amount Growth — {transaction_type}",
    markers=True
)

fig6.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig6)


# Section 6: Top Districts
st.header("Top Districts")

df_districts = get_top_districts(
    year,
    quarter
)

fig7 = px.bar(
    df_districts,
    x="entity_name",
    y="total_amount",
    title=f"Top 10 Districts by Transaction Amount — {year} Q{quarter}",
    color="total_amount",
    color_continuous_scale="Purples"
)

fig7.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig7)


# Section 7: App Opens vs Registered Users
st.header("App Opens vs Registered Users")

df_engagement = get_user_engagement(
    year,
    quarter
)

fig8 = px.scatter(
    df_engagement,
    x="total_users",
    y="total_app_opens",
    text="state",
    title=f"App Opens vs Registered Users — {year} Q{quarter}",
    labels={
        "total_users": "Registered Users",
        "total_app_opens": "App Opens"
    }
)

fig8.update_traces(textposition="top center")
st.plotly_chart(fig8)