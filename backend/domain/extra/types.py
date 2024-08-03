from typing import Annotated

from pydantic import StringConstraints, EmailStr, UUID4

PasswordStr = Annotated[
    str,
    StringConstraints(
        min_length=8,
        max_length=50,
        # at least one lowercase, one uppercase, one digit, one special character
        pattern=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).*$",
    ),
]


__all__ = ["EmailStr", "PasswordStr", "UUID4"]
