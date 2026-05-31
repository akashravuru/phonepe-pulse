from services.llm import ask_llm

from services.analytics import (
    get_transaction_summary,
    get_user_summary,
    get_top_state,
    get_transaction_by_type,
    get_top_districts,
    get_state_growth
)


def detect_intent(question):

    question = question.lower()

    if "growth" in question:
        return "growth"

    elif "state" in question:
        return "state"

    elif "category" in question:
        return "category"

    elif "district" in question:
        return "district"

    else:
        return "general"


def ask_financial_copilot(question, year, quarter):

    intent = detect_intent(question)

    context = ""

    if intent == "growth":

        state_growth = get_state_growth(
            year,
            quarter
        )

        context = f"""
        State Growth Data:

        {state_growth.to_string(index=False)}
        """

    elif intent == "state":

        top_states = get_top_state(
            year,
            quarter
        )

        context = f"""
        Top States:

        {top_states.to_string(index=False)}
        """

    elif intent == "category":

        transaction_types = get_transaction_by_type(
            year,
            quarter
        )

        context = f"""
        Transaction Categories:

        {transaction_types.to_string(index=False)}
        """

    elif intent == "district":

        top_districts = get_top_districts(
            year,
            quarter
        )

        context = f"""
        Top Districts:

        {top_districts.to_string(index=False)}
        """

    else:

        tx = get_transaction_summary(
            year,
            quarter
        )

        users = get_user_summary(
            year,
            quarter
        )

        context = f"""
        Transaction Summary:

        {tx.to_string(index=False)}

        User Summary:

        {users.to_string(index=False)}
        """

    prompt = f"""
    You are a senior financial analyst.

    Year: {year}
    Quarter: {quarter}

    Context:

    {context}

    User Question:

    {question}

    Rules:
    - Answer only using the provided context.
    - If data is insufficient, say so.
    - Do not invent facts.
    - Be concise and analytical.
    """

    return ask_llm(prompt)