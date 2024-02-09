import logging

from app.commands.base import ICommand


class LogException(ICommand):
    source_command: ICommand
    exception: Exception

    def __init__(self, source_command: ICommand, exception: Exception) -> None:
        self.source_command = source_command
        self.exception = exception

    def execute(self) -> None:
        logging.error(f"Command expception, {self.source_command}: {self.exception}")
