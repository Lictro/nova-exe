from app.core.parser import ToolCallParser
from app.llm.provider import LLMProvider
from app.tools.registry import ToolRegistry


class NovaAgent:

    def __init__(
        self,
        llm: LLMProvider,
        registry: ToolRegistry,
    ):
        self.llm = llm
        self.registry = registry

    def chat(self, message: str) -> str:

        response = self.llm.chat(message)

        tool_call = ToolCallParser.parse(response)

        if tool_call is None:
            return response

        tool_name = tool_call["tool"]
        arguments = tool_call["arguments"]

        result = self.registry.call(
            tool_name,
            **arguments,
        )

        return result