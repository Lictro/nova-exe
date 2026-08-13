import json

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

    def add_tool_call(
        self,
        tool: str,
        arguments: dict,
    ):
        self._messages.append({
            "role": "assistant",
            "content": json.dumps({
                "type": "tool",
                "tool": tool,
                "arguments": arguments,
            }),
        })

    def add_tool(
        self,
        tool: str,
        result: str,
    ):
        self._messages.append({
            "role": "user",
            "content": json.dumps({
                "type": "tool_result",
                "tool": tool,
                "result": result,
            }),
        })

    @property
    def messages(self):
        return self._messages