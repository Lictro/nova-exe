class Conversation:

    def __init__(self):
        self._messages = []

    def add(
        self,
        role: str,
        content: str,
    ):
        self._messages.append({
            "role": role,
            "content": content,
        })

    def add_tool(
        self,
        tool: str,
        result: str,
    ):
        self._messages.append({
            "role": "tool",
            "name": tool,
            "content": result,
        })

    @property
    def messages(self):
        return self._messages