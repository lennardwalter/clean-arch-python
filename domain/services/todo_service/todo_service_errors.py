from typing import Union

from domain.services.shared import UnauthorizedError, RequestingUserNotFoundError
from domain.ports.todo_repository import TodoNotFoundError


class TodoLimitReachedError:
    pass


type TodoCreateError = Union[RequestingUserNotFoundError, TodoLimitReachedError]
type TodoUpdateError = Union[UnauthorizedError, RequestingUserNotFoundError, TodoNotFoundError]
type TodoDeleteError = Union[UnauthorizedError, RequestingUserNotFoundError, TodoNotFoundError]
type TodoGetByIdError = Union[UnauthorizedError, RequestingUserNotFoundError, TodoNotFoundError]
type TodoGetAllByUserIdError = Union[UnauthorizedError, RequestingUserNotFoundError]
