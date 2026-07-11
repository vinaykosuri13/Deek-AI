# ==========================
# DEEK AI REQUEST
# ==========================

class Request:

    def __init__(self, intent, question):

        self.intent = intent
        self.question = question

        # Stores the output of previous tools
        self.context = ""
