from re import compile
from typing import Annotated

from pydantic import StringConstraints

from domain.extra.types import BaseModelConfig, EmailStr


class Token(BaseModelConfig):
    access_token: str
    token_type: str


type PasswordStr = Annotated[
    str,
    StringConstraints(
        min_length=8,
        max_length=50,
        # at least one lowercase, one uppercase, one digit, one special character
        pattern=compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).*$"),
    ),
]


class AuthRequest(BaseModelConfig):
    email: EmailStr
    password: PasswordStr
