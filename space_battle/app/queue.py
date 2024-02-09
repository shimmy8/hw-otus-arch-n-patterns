from queue import Queue

from app.commands.base import ICommand
from app.exception_handler import ExceptionHandler


def run(queue: Queue, exception_handler: ExceptionHandler) -> None:
    while True:
        if queue.empty():
            break
        cmd: ICommand = queue.get()
        try:
            cmd.execute()
        except Exception as exc:
            handle_cmd = exception_handler.handle(cmd, exc)
            queue.put(handle_cmd)
