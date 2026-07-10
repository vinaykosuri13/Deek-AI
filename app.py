from ai import ask
from search import search_web, format_results
from memory import add_message

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

    print("\n🔍 Searching Internet...")

    results = search_web(question)

    context = format_results(results)

    prompt = f"""
Use the following search results to answer the question.

Search Results:

{context}

Question:
{question}
"""

    answer = ask(prompt)

    add_message("assistant", answer)

    print("\nDeek:")
    print(answer)
