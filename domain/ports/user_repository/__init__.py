from .user_repository_protocol import UserRepository


from .user_repository_errors import (
    UserNotFoundError,
    UserGetByIdError,
    UserGetByEmailError,
)


__all__ = [
    # Protocol definition
    "UserRepository",
    # Error types
    "UserNotFoundError",
    # Aliases
    "UserGetByIdError",
    "UserGetByEmailError",
]
