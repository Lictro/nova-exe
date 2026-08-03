from app.core.conversation import Conversation
from app.core.loop import AgentLoop


class NovaAgent:

    def __init__(
        self,
        llm,
        registry,
    ):
        self.loop = AgentLoop(
            llm,
            registry,
        )


    def chat(
        self,
        message: str,
    ):

        conversation = Conversation()

        conversation.add(
            "user",
            message,
        )

        return self.loop.run(
            conversation,
        )