from app.commands.base import ICommand


class ExceptionHandler:
    __command_exception_handlers: dict[ICommand, dict[Exception, ICommand]] = {}

    def handle(self, cmd: ICommand, exc: Exception) -> ICommand:
        cmd_name, exc_name = cmd.__class__.__name__, exc.__class__.__name__
        handler = self.__command_exception_handlers[cmd_name][exc_name]
        print("H", handler)
        return handler

    def register_handler(
        self, cmd: ICommand, exc: Exception, handler: ICommand
    ) -> None:
        cmd_name, exc_name = cmd.__name__, exc.__name__
        if self.__command_exception_handlers:
            if cmd_name in self.__command_exception_handlers:
                self.__command_exception_handlers[cmd_name][exc_name] = handler
            else:
                self.__command_exception_handlers[cmd_name] = {exc_name: handler}
        else:
            self.__command_exception_handlers = {cmd_name: {exc_name: handler}}

    def _get_class_name(self, obj: ICommand | Exception) -> str:
        return obj.__name__
