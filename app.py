from ai import ask
from search import search_web, format_results
from memory import add_message
from decision import needs_web_search

print("=" * 40)
print("🤖 DEEK AI v0.1 Alpha")
print("Created by Vinay Kosuri")
print("=" * 40)

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("\nDeek: Goodbye!")
        break

    add_message("user", question)

    if needs_web_search(question):

    print("\n🔍 Searching Internet...")

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

    print("\n🧠 Using AI Knowledge...")

    answer = ask(question)

    add_message("assistant", answer)

    print("\nDeek:")
    print(answer)
