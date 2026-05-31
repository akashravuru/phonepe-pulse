from services.vectordb import search_chunks
from services.llm import ask_llm


def rag_answer(question):

    results = search_chunks(
        question
    )

    context = "\n\n".join(
        results["documents"][0]
    )

    print("\n\nRETRIEVED CONTEXT\n")
    print(context[:5000])

    prompt = f"""
    You are an RBI financial research assistant.

    Answer the user's question using
    only the provided context.

    Context:

    {context}

    Question:

    {question}
    """

    return ask_llm(prompt)