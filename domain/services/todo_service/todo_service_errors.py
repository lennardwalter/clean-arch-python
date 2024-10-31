from typing import Union

from domain.ports.todo_repository import TodoNotFoundError
from domain.services.shared import RequestingUserNotFoundError, UnauthorizedError


class TodoLimitReachedError:
    pass


type TodoCreateError = Union[RequestingUserNotFoundError, TodoLimitReachedError]
type TodoUpdateError = Union[UnauthorizedError, RequestingUserNotFoundError, TodoNotFoundError]
type TodoDeleteError = Union[UnauthorizedError, RequestingUserNotFoundError, TodoNotFoundError]
type TodoGetByIdError = Union[UnauthorizedError, RequestingUserNotFoundError, TodoNotFoundError]
type TodoGetAllByUserIdError = Union[UnauthorizedError, RequestingUserNotFoundError]
