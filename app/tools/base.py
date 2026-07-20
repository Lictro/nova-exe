from abc import ABC, abstractmethod
from typing import Callable


class Tool(ABC):
    """Base class for every Nova tool."""

    name: str
    description: str

    @abstractmethod
    def get_functions(self) -> dict[str, Callable]:
        """Return the functions exposed by this tool."""
        pass