from pathlib import Path
from typing import Callable

from app.tools.base import Tool


class FileSystemTool(Tool):

    name = "filesystem"

    description = "Read and write files."

    def create_file(
        self,
        path: str,
        content: str,
    ) -> str:

        Path(path).write_text(content)

        return f"Created {path}"

    def read_file(
        self,
        path: str,
    ) -> str:

        return Path(path).read_text()

    def get_functions(self) -> dict[str, Callable]:

        return {
            "create_file": self.create_file,
            "read_file": self.read_file,
        }