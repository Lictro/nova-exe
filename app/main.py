from app.core.agent import NovaAgent

from app.llm.ollama import OllamaProvider

from app.tools.filesystem import FileSystemTool
from app.tools.registry import ToolRegistry


def main():

    registry = ToolRegistry()

    registry.register(
        FileSystemTool()
    )

    nova = NovaAgent(
        OllamaProvider(),
        registry,
    )

    print("═══════════════════════════════")
    print("        Nova.EXE Online")
    print("═══════════════════════════════")

    while True:

        mission = input("\nMission > ")

        if mission.lower() == "exit":
            break

        result = nova.chat(mission)

        print(f"\nNova > {result}")


if __name__ == "__main__":
    main()