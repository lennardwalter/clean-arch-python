from typing import Protocol

from domain.entities import User
from domain.extra.types import EmailStr, UUID4
from domain.extra.result import Result

from .user_repository_errors import UserGetByEmailError, UserGetByIdError


class UserRepository(Protocol):
    async def get_by_email(self, email: EmailStr) -> Result[User, UserGetByEmailError]: ...
    async def get_by_id(self, id: UUID4) -> Result[User, UserGetByIdError]: ...
