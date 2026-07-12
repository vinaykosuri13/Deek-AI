# ==========================
# DEEK AI RESPONSE
# ==========================

class Response:

    def __init__(
        self,
        success,
        message,
        source,
        data=None,
        results=None,
        metadata=None
    ):

        self.success = success
        self.message = message
        self.source = source

        self.data = data if data is not None else {}

        self.results = results if results is not None else []

        self.metadata = metadata if metadata is not None else {}
