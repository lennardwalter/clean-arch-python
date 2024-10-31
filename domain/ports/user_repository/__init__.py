from .user_repository_errors import (
    UserGetByEmailError,
    UserGetByIdError,
    UserNotFoundError,
)
from .user_repository_protocol import UserRepository


__all__ = [
    # Protocol definition
    "UserRepository",
    # Error types
    "UserNotFoundError",
    # Aliases
    "UserGetByIdError",
    "UserGetByEmailError",
]
