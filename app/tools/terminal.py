import subprocess
from typing import Callable

from app.tools.base import Tool


class TerminalTool(Tool):

    name = "terminal"

    description = "Execute terminal commands."

    def run(
        self,
        command: str,
        timeout: int = 30,
    ) -> str:

        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=timeout,
            )

            output = [
                f"Exit Code: {result.returncode}"
            ]

            if result.stdout:
                output.append(
                    f"STDOUT:\n{result.stdout}"
                )

            if result.stderr:
                output.append(
                    f"STDERR:\n{result.stderr}"
                )

            return "\n\n".join(output)
        
        except subprocess.TimeoutExpired:
            return (
                f"ERROR: Command timed out after "
                f"{timeout} seconds."
            )

    def get_functions(self) -> dict[str, Callable]:

        return {
            "run": self.run,
        }