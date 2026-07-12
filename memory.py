# ==========================
# DEEK AI MEMORY
# ==========================

conversation = []


def add_message(role, message):

    conversation.append({
        "role": role,
        "message": message
    })


def get_memory():

    return conversation


def search_memory(query):

    query = query.lower()

    results = []

    for item in conversation:

        if query in item["message"].lower():
            results.append(item)

    return results
