# ==========================
# DEEK AI CONTROLLER
# ==========================

from decision import needs_web_search
from search import search_web, format_results
from ai import ask
from memory import add_message
from intent import detect_intent
from tool_manager import execute_tool


def process_request(question):

    # Save user message
    add_message("user", question)
    intent = detect_intent(question)

    print(f"Intent: {intent}")
    execute_tool(intent, question)

    # Decide if web search is needed
    if intent == "SEARCH":

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

    else:

        answer = ask(question)

    # Save AI response
    add_message("assistant", answer)

    return answer
