import streamlit as st

from services.insights import generate_financial_insights

st.title("AI Financial Insights")

year = st.selectbox(
    "Select Year",
    [2018, 2019, 2020, 2021, 2022, 2023, 2024]
)

quarter = st.selectbox(
    "Select Quarter",
    [1, 2, 3, 4]
)

if st.button("Generate AI Insights"):

    with st.spinner("Analyzing PhonePe data..."):

        insights = generate_financial_insights(
            year,
            quarter
        )

        st.markdown(insights)