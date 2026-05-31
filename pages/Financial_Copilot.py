import streamlit as st

from services.copilot import (
    ask_financial_copilot
)

st.title("Financial Intelligence Copilot")

year = st.selectbox(
    "Select Year",
    [2018, 2019, 2020, 2021, 2022, 2023, 2024]
)

quarter = st.selectbox(
    "Select Quarter",
    [1, 2, 3, 4]
)

question = st.text_area(
    "Ask a question about the PhonePe data"
)

if st.button("Ask Copilot"):

    if question:

        with st.spinner("Analyzing data..."):

            response = ask_financial_copilot(
                question,
                year,
                quarter
            )

            st.write(response)