from typing import Protocol

from domain.entities import User
from domain.extra.types import EmailStr
from domain.extra.result import Result

from .base_repository import BaseRepository, RepositoryError


class UserRepository(BaseRepository[User], Protocol):
    async def get_by_email(self, email: EmailStr) -> Result[User, RepositoryError]: ...
