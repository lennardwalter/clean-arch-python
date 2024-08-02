from domain.ports.repositories import UserRepository


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def get_all_users(self):
        return await self.user_repo.get_all()
