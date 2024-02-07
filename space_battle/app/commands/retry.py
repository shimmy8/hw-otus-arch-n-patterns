from app.commands.base import ICommand


class Retry(ICommand):
    source_command: ICommand

    def __init__(self, source_command: ICommand) -> None:
        self.source_command = source_command

    def execute(self) -> None:
        self.source_command.execute()


class RetryTwice(Retry):
    pass
