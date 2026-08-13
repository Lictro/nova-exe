from app.core.models import ToolCall, TextResponse, ToolResult
from app.core.conversation import Conversation


class AgentLoop:

    MAX_ITERATIONS = 10

    def __init__(
        self,
        llm,
        registry,
    ):
        self.llm = llm
        self.registry = registry

    def run(
        self,
        conversation: Conversation,
    ):

        tools_schema = self.registry.get_schema()

        iteration = 0

        while iteration < self.MAX_ITERATIONS:

            iteration += 1

            response = self.llm.chat(
                conversation,
                tools_schema,
            )

            if isinstance(response, TextResponse):
                return response.text

            if isinstance(response, ToolCall):

                conversation.add_tool_call(
                    response.tool,
                    response.arguments,
                )

                result = self.registry.call(
                    response.tool,
                    **response.arguments,
                )

                tool_result = ToolResult(
                    tool=response.tool,
                    result=result,
                )

                conversation.add_tool(
                    tool_result.tool,
                    tool_result.result,
                )

        return "Maximum iterations reached."