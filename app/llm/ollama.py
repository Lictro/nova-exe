import json
import os
import ollama
import platform

from app.core.conversation import Conversation
from app.core.models import ToolCall, TextResponse
from app.core.prompt import SYSTEM_PROMPT
from app.llm.provider import LLMProvider


class OllamaProvider(LLMProvider):

    def __init__(self, model: str = "qwen3:4b"):
        self.model = model
        self.client = ollama


    def chat(
        self,
        conversation: Conversation,
        tools_schema: str,
    ) -> ToolCall | TextResponse:
        
        system_info = f"""
        Operating System:
        {platform.system()}

        Machine:
        {platform.machine()}

        Shell:
        {os.environ.get("SHELL") or os.environ.get("COMSPEC", "Unknown")}

        Python:
        {platform.python_version()}
        """
        
        prompt = SYSTEM_PROMPT.replace(
            "{tools}",
            tools_schema,
        )

        response = self.client.chat(
            model=self.model,
            messages = [
                {
                    "role": "system",
                    "content": prompt + system_info,
                },
                *conversation.messages,
            ],
            format="json",
        )

        content = response["message"]["content"]

        try:
            data = json.loads(content)


        except json.JSONDecodeError:
            return TextResponse(
                text=content
            )

        if "tool" in data:

            return ToolCall(
                tool=data["tool"],
                arguments=data.get("arguments", {}),
            )

        return TextResponse(
            text=data.get("content", content)
        )