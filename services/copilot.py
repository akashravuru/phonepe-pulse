from services.llm import ask_llm

from services.retriever import retrieve_context

from services.prompts import build_prompt

from services.rag import rag_answer


def detect_intent(question):

    question = question.lower()

    rag_keywords = [
        "rbi",
        "digital payments",
        "regulation",
        "policy",
        "payment system",
        "bbps",
        "e-rupi",
        "upi"
    ]

    for keyword in rag_keywords:

        if keyword in question:
            return "rag"

    growth_keywords = [
        "growth",
        "growing",
        "fastest growing",
        "increase",
        "increasing",
        "growth rate"
    ]

    for keyword in growth_keywords:

        if keyword in question:
            return "growth"

    category_keywords = [
        "category",
        "categories",
        "transaction type",
        "transaction types"
    ]

    for keyword in category_keywords:

        if keyword in question:
            return "category"

    if "state" in question:
        return "state"

    elif "district" in question:
        return "district"

    else:
        return "general"

def ask_financial_copilot(question, year, quarter):

    intent = detect_intent(question)

    print("INTENT:", intent)

    if intent == "rag":

        return rag_answer(question)

    context = retrieve_context(
        intent,
        year,
        quarter
    )

    prompt = build_prompt(
        question,
        context,
        year,
        quarter
    )

    return ask_llm(prompt)