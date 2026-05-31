from services.analytics import (
    get_transaction_summary,
    get_user_summary,
    get_top_state
)

from services.llm import ask_llm


def generate_financial_insights(year, quarter):

    tx = get_transaction_summary(
        year,
        quarter
    )

    users = get_user_summary(
        year,
        quarter
    )

    top_states = get_top_state(
        year,
        quarter
    )

    prompt = f"""
    You are a senior financial analyst.

    Year: {year}
    Quarter: {quarter}

    Transaction Summary:
    {tx.to_dict()}

    User Summary:
    {users.to_dict()}

    Top States:
    {top_states.to_dict()}

    Analyze the data and provide:

    1. Key Trend
    2. Growth Observation
    3. User Insight
    4. State-Level Observation
    5. Business Opportunity

    Keep the response concise and business-focused.
    """

    return ask_llm(prompt)