# ==========================
# DEEK AI SMART DECISION ENGINE
# ==========================

from ai import ask

def needs_web_search(question):

    prompt = f"""
You are a decision engine.

Question:
{question}

Reply with ONLY ONE WORD.

YES = Needs internet because it requires current or live information.

NO = Can be answered from general knowledge.

Answer:
"""

    decision = ask(prompt).strip().upper()

    return decision.startswith("YES")
