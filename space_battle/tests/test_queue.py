from unittest import mock

from queue import Queue

from app.queue import run
from app.adapters.movable import MovableAdapter
from app.commands.log_exception import LogException
from app.commands.retry import Retry
from app.commands.retry import RetryTwice
from app.commands.move import Move
from app.exception_handler import ExceptionHandler


@mock.patch.object(LogException, "execute")
def test_log_queue_exception(mock_log_exception):
    queue: Queue = Queue()
    exception_handler: ExceptionHandler = ExceptionHandler()

    obj = object()
    movable_adapter = MovableAdapter(obj)
    cmd = Move(movable_adapter)

    exception_handler.register_handler(
        Move, AttributeError, LogException(Move, AttributeError)
    )

    queue.put(cmd)
    run(queue=queue, exception_handler=exception_handler)

    mock_log_exception.assert_called_once()


@mock.patch.object(Retry, "execute")
def test_retry_queue_exception(mock_retry):
    queue: Queue = Queue()
    exception_handler: ExceptionHandler = ExceptionHandler()

    obj = object()
    movable_adapter = MovableAdapter(obj)
    cmd = Move(movable_adapter)

    exception_handler.register_handler(Move, AttributeError, Retry(cmd))

    queue.put(cmd)
    run(queue=queue, exception_handler=exception_handler)

    mock_retry.assert_called_once()


@mock.patch.object(LogException, "execute")
def test_retry_and_log_exception(mock_log_exception):
    queue: Queue = Queue()
    exception_handler: ExceptionHandler = ExceptionHandler()

    obj = object()
    movable_adapter = MovableAdapter(obj)
    cmd = Move(movable_adapter)

    exception_handler.register_handler(
        Move,
        AttributeError,
        Retry(cmd),
    )
    exception_handler.register_handler(
        Retry,
        AttributeError,
        LogException(cmd, AttributeError),
    )

    queue.put(cmd)
    run(queue=queue, exception_handler=exception_handler)

    mock_log_exception.assert_called_once()


@mock.patch.object(LogException, "execute")
def test_retry_twice_and_log_exception(mock_log_exception):
    queue: Queue = Queue()
    exception_handler: ExceptionHandler = ExceptionHandler()

    obj = object()
    movable_adapter = MovableAdapter(obj)
    cmd = Move(movable_adapter)

    exception_handler.register_handler(
        Move,
        AttributeError,
        Retry(cmd),
    )
    exception_handler.register_handler(
        Retry,
        AttributeError,
        RetryTwice(cmd),
    )
    exception_handler.register_handler(
        RetryTwice,
        AttributeError,
        LogException(cmd, AttributeError),
    )

    queue.put(cmd)
    run(queue=queue, exception_handler=exception_handler)

    mock_log_exception.assert_called_once()
