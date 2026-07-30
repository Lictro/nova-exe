from abc import ABC, abstractmethod

from app.core.models import ToolCall, TextResponse


class LLMProvider(ABC):

    @abstractmethod
    @abstractmethod
    def chat(
        self,
        message: str,
        tools_schema: str,
    ) -> ToolCall | TextResponse:
        pass