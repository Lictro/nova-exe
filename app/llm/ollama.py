import ollama

from app.core.prompt import SYSTEM_PROMPT
from app.llm.provider import LLMProvider


class OllamaProvider(LLMProvider):

    def __init__(self, model: str = "qwen2.5-coder:3b"):
        self.model = model

    def chat(self, message: str) -> str:

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role":"system",
                    "content":SYSTEM_PROMPT
                },
                {
                    "role":"user",
                    "content":message
                }
            ],
            format="json"
        )

        return response["message"]["content"]