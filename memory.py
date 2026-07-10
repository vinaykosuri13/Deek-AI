# ==========================
# DEEK AI MEMORY
# ==========================

conversation = []

def add_message(role, content):
    """
    Save a message to memory.
    """
    conversation.append({
        "role": role,
        "content": content
    })

def get_memory():
    """
    Return the conversation history.
    """
    return conversation

def clear_memory():
    """
    Clear the conversation history.
    """
    conversation.clear()
