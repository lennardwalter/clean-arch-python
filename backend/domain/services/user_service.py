from domain.ports.repositories import UserRepository, RepositoryError

from domain.entities import User
from domain.extra.types import UUID4, EmailStr
from domain.extra.result import Result


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def get_user_by_id(self, id: UUID4) -> Result[User, RepositoryError]:
        return await self.user_repo.get_by_id(id)

    async def get_user_by_email(self, email: EmailStr) -> Result[User, RepositoryError]:
        return await self.user_repo.get_by_email(email)
