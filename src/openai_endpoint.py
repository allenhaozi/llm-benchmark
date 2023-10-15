from typing import Optional


class OpenAIEndpoint:
    def __init__(
        self,
        server: str,
        model: str,
        enable_chat: Optional[bool] = True,
        stop: Optional[list] = None,
    ):
        self.server = server
        self.model = model
        self.enable_chat = enable_chat
        self.stop = stop
