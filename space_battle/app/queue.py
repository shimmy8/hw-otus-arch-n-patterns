from queue import Queue

from app.commands.base import ICommand
from app.exception_handler import ExceptionHandler


def run(queue: Queue, exception_handler: ExceptionHandler) -> None:
    while True:
        print(queue.qsize())
        if queue.empty():
            break
        cmd: ICommand = queue.get()
        print(cmd)
        try:
            cmd.execute()
        except Exception as exc:
            print(exc)
            handle_cmd = exception_handler.handle(cmd, exc)
            print("CMD", handle_cmd)
            queue.put(handle_cmd)
