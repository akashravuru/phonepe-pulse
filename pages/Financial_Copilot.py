import streamlit as st

from services.copilot import (
    ask_financial_copilot
)

st.title("AI Financial Intelligence Copilot")

st.markdown("""
Ask questions about:

- PhonePe transaction data
- State growth trends
- Transaction categories
- RBI reports
- UPI ecosystem
- Digital payment regulations
""")

year = st.selectbox(
    "Select Year",
    [2018, 2019, 2020, 2021, 2022, 2023, 2024]
)

quarter = st.selectbox(
    "Select Quarter",
    [1, 2, 3, 4]
)

question = st.text_area(
    "Ask anything about PhonePe analytics or RBI knowledge"
)

if st.button("Ask Copilot"):

    if question:

        with st.spinner(
            "Thinking..."
        ):

            response = ask_financial_copilot(
                question,
                year,
                quarter
            )

            st.write(response)