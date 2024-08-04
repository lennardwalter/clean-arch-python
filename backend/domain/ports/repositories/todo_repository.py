from typing import Protocol

from domain.entities import Todo
from domain.extra.types import UUID4
from domain.extra.result import Result

from .base_repository import BaseRepository, RepositoryError


class TodoRepository(BaseRepository[Todo], Protocol):
    async def get_all_by_user_id(
        self, id: UUID4
    ) -> Result[list[Todo], RepositoryError]: ...
