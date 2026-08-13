from dataclasses import dataclass
from typing import Any


@dataclass
class ToolCall:
    tool: str
    arguments: dict[str, Any]


@dataclass
class TextResponse:
    text: str

@dataclass
class ToolResult:
    tool: str
    result: str