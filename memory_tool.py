# ==========================
# DEEK AI MEMORY TOOL
# ==========================

from memory import add_message


def memory_tool(role, message):

    add_message(role, message)

    return "Memory Updated"
