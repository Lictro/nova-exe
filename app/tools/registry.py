import inspect
import json

from typing import Callable
from app.tools.base import Tool


class ToolRegistry:

    def __init__(self):

        self._functions: dict[str, Callable] = {}

    def register(self, tool: Tool):

        for name, function in tool.get_functions().items():

            key = f"{tool.name}.{name}"

            self._functions[key] = function

    def call(self, name: str, **kwargs):

        if name not in self._functions:
            raise ValueError(f"Unknown function: {name}")

        return self._functions[name](**kwargs)

    def list_functions(self):

        return list(self._functions.keys())
    
    def get_schema(self) -> str:
        schema = []

        for name, function in self._functions.items():

            signature = inspect.signature(function)

            arguments = {}

            for parameter in signature.parameters.values():

                annotation = parameter.annotation

                if annotation is inspect.Parameter.empty:
                    annotation = "any"

                elif hasattr(annotation, "__name__"):
                    annotation = annotation.__name__

                else:
                    annotation = str(annotation)

                arguments[parameter.name] = annotation

            schema.append({
                "name": name,
                "arguments": arguments,
            })

        return json.dumps(
            schema,
            indent=2,
        )