from pathlib import Path
from typing import Callable

from app.tools.base import Tool


class FileSystemTool(Tool):

    name = "filesystem"

    description = """
    Filesystem operations.

    Available functions:

    filesystem.create_file:
    Creates a new file.

    Arguments:
    - path: string
    - content: string


    filesystem.read_file:
    Reads an existing file.

    Arguments:
    - path: string
    """

    def create_file(
        self,
        path: str,
        content: str,
    ) -> str:
        """
        Creates a new text file.

        Args:
            path: Path of the file to create.
            content: Text to write into the file.
        """

        Path(path).write_text(content)

        return f"Created {path}"

    def read_file(
        self,
        path: str,
    ) -> str:
        """
        Reads a text file.

        Args:
            path: Path of the file to read.
        """

        return Path(path).read_text()

    def get_functions(self) -> dict[str, Callable]:

        return {
            "create_file": self.create_file,
            "read_file": self.read_file,
        }