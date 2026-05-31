from services.analytics import (
    get_transaction_summary,
    get_user_summary,
    get_top_state,
    get_transaction_by_type,
    get_top_districts,
    get_state_growth
)


def retrieve_context(intent, year, quarter):

    if intent == "growth":

        return get_state_growth(
            year,
            quarter
        ).to_string(index=False)

    elif intent == "state":

        return get_top_state(
            year,
            quarter
        ).to_string(index=False)

    elif intent == "category":

        return get_transaction_by_type(
            year,
            quarter
        ).to_string(index=False)

    elif intent == "district":

        return get_top_districts(
            year,
            quarter
        ).to_string(index=False)

    else:

        transaction_summary = get_transaction_summary(
            year,
            quarter
        )

        user_summary = get_user_summary(
            year,
            quarter
        )

        return f"""
        Transaction Summary

        {transaction_summary.to_string(index=False)}

        User Summary

        {user_summary.to_string(index=False)}
        """