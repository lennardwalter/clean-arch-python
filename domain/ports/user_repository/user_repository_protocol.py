from typing import Protocol

from domain.entities import User
from domain.extra.result import Result
from domain.extra.types import UUID4, EmailStr

from .user_repository_errors import UserGetByEmailError, UserGetByIdError


class UserRepository(Protocol):
    async def get_by_email(self, email: EmailStr) -> Result[User, UserGetByEmailError]: ...
    async def get_by_id(self, id: UUID4) -> Result[User, UserGetByIdError]: ...
