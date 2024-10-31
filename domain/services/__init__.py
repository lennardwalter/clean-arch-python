from .todo_service.todo_service_impl import TodoService
from .todo_service.todo_service_requests import (
    TodoCreateRequest,
    TodoDeleteRequest,
    TodoUpdateRequest,
)
from .user_service.user_service_impl import UserService


SERVICES = [UserService, TodoService]

__all__ = [
    "SERVICES",
    # UserService
    "UserService",
    # TodoService
    "TodoService",
    "TodoCreateRequest",
    "TodoUpdateRequest",
    "TodoDeleteRequest",
]
