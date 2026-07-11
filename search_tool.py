# ==========================
# DEEK AI SEARCH TOOL
# ==========================

from search import search_web, format_results
from ai import ask


def search_tool(question):

    results = search_web(question)

    context = format_results(results)

    prompt = f"""
Use these search results to answer the user's question.

Search Results:

{context}

Question:
{question}
"""

    answer = ask(prompt)

    return answer
