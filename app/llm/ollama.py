import json
import ollama

from app.core.models import ToolCall, TextResponse
from app.core.prompt import SYSTEM_PROMPT
from app.llm.provider import LLMProvider


class OllamaProvider(LLMProvider):

    def __init__(self, model: str = "qwen3:4b"):
        self.model = model
        self.client = ollama


    def chat(
        self,
        message: str,
        tools_schema: str,
    ) -> ToolCall | TextResponse:
        
        prompt = SYSTEM_PROMPT.replace(
            "{tools}",
            tools_schema,
        )

        print(prompt)

        response = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": prompt,
                },
                {
                    "role": "user",
                    "content": message,
                }
            ],
            format="json",
        )

        content = response["message"]["content"]

        try:
            data = json.loads(content)

            print(data)

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