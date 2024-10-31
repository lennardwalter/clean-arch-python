from .todo_repository_errors import (
    TodoCreateError,
    TodoDeleteError,
    TodoGetAllByUserIdError,
    TodoGetByIdError,
    TodoGetCountByUserIdError,
    TodoNotFoundError,
    TodoUpdateError,
)
from .todo_repository_protocol import TodoRepository


__all__ = [
    # Protocol definition
    "TodoRepository",
    # Error types
    "TodoNotFoundError",
    # Aliases
    "TodoCreateError",
    "TodoUpdateError",
    "TodoDeleteError",
    "TodoGetByIdError",
    "TodoGetCountByUserIdError",
    "TodoGetAllByUserIdError",
]
