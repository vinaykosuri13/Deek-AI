# ==========================
# DEEK AI CALCULATOR RULE
# ==========================

import re


def match(request):

    question = request.question.lower().strip()

    keywords = [
        "calculate",
        "what is",
        "compute",
        "evaluate"
    ]

    # Natural language calculator
    if any(keyword in question for keyword in keywords):

        expression = question

        for keyword in keywords:
            expression = expression.replace(keyword, "")

        expression = expression.replace("?", "").strip()

        if re.fullmatch(r"[0-9+\-*/().% ]+", expression):

            request.question = expression

            return [
                {"tool": "CALCULATOR"}
            ]

    # Direct mathematical expression
    if re.fullmatch(r"[0-9+\-*/().% ]+", question):

        return [
            {"tool": "CALCULATOR"}
        ]

    return None
