import json


class ToolCallParser:

    @staticmethod
    def parse(response: str):

        try:
            return json.loads(response)

        except json.JSONDecodeError:
            return None