from .todo_repository_protocol import TodoRepository


from .todo_repository_errors import (
    TodoNotFoundError,
    TodoCreateError,
    TodoUpdateError,
    TodoDeleteError,
    TodoGetByIdError,
    TodoGetCountByUserIdError,
    TodoGetAllByUserIdError,
)


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
