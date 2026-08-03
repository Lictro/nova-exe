from abc import ABC, abstractmethod

from app.core.conversation import Conversation
from app.core.models import ToolCall, TextResponse


class LLMProvider(ABC):

    @abstractmethod
    @abstractmethod
    def chat(
        self,
        conversation: Conversation,
        tools_schema: str,
    ) -> ToolCall | TextResponse:
        pass