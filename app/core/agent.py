from app.core.conversation import Conversation
from app.core.models import ToolCall, TextResponse
from app.llm.provider import LLMProvider
from app.tools.registry import ToolRegistry


class NovaAgent:

    def __init__(
        self,
        llm,
        registry,
    ):
        self.llm = llm
        self.registry = registry


    def chat(self, message: str):

        tools_schema = self.registry.get_schema()

        conversation = Conversation()

        conversation.add(
            "user",
            message,
        )

        response = self.llm.chat(
            conversation,
            tools_schema,
        )


        if isinstance(response, TextResponse):
            return response.text


        if isinstance(response, ToolCall):

            result = self.registry.call(
                response.tool,
                **response.arguments,
            )

            conversation.add_tool(
                response.tool,
                result,
            )

            response = self.llm.chat(
                conversation,
                tools_schema,
            )

            if isinstance(response, TextResponse):
                return response.text
            
            print(response)

            return "Unexpected response after tool execution."