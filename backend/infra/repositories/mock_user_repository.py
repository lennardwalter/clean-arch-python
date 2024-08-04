from typing import final
from uuid import UUID

from domain.entities import User
from domain.ports.repositories import UserRepository, RepositoryError
from domain.extra.types import EmailStr
from domain.extra.result import *

from .mock_base_repository import MockBaseRepository


@final
class MockUserRepository(UserRepository, MockBaseRepository[User]):

    def __init__(self) -> None:
        super().__init__(
            [
                User(
                    id=UUID("f5f4b3b4-3b4b-4b3b-b43b-4b3b4b3b4b3b"),
                    email="test@example.com",
                    hashed_password="$2b$12$uQ87CZvsyju3tA9YxVpwI.2BcexSTlgtq9uYqCb1Vm/smxJytyxBG",  # Testpassword!1
                )
            ]
        )

    async def get_by_email(self, email: EmailStr) -> Result[User, RepositoryError]:
        for user in self._entities:
            if user.email == email:
                return Ok(user)
        return Err("User not found")
