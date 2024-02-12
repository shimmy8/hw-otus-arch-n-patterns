from app.commands.base import ICommand


class MacroCommand(ICommand):
    commands: list[ICommand]

    def __init__(self, commands: list[ICommand]) -> None:
        self.commands = commands

    def execute(self) -> None:
        for cmd in self.commands:
            cmd.execute()
