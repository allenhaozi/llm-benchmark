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

    def __str__(self):
        return f"model: {self.model}, server: {self.server}, stop: {self.stop}"
