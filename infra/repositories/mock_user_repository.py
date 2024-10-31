from typing import final
from uuid import UUID

from domain.entities import User
from domain.ports.user_repository import (
    UserRepository,
    UserNotFoundError,
    UserGetByEmailError,
    UserGetByIdError,
)
from domain.extra.types import EmailStr
from domain.extra.result import *


@final
class MockUserRepository(UserRepository):

    def __init__(self) -> None:
        self._entities = [
            User(
                id=UUID("f5f4b3b4-3b4b-4b3b-b43b-4b3b4b3b4b3b"),
                email="test@example.com",
                hashed_password="$2b$12$uQ87CZvsyju3tA9YxVpwI.2BcexSTlgtq9uYqCb1Vm/smxJytyxBG",  # Testpassword!1
            )
        ]

    async def get_by_email(self, email: EmailStr) -> Result[User, UserGetByEmailError]:
        for user in self._entities:
            if user.email == email:
                return Ok(user)
        return Err(UserNotFoundError())

    async def get_by_id(self, id: UUID) -> Result[User, UserGetByIdError]:
        for user in self._entities:
            if user.id == id:
                return Ok(user)
        return Err(UserNotFoundError())
