from typing import Protocol

from domain.entities import Todo
from domain.extra.types import UUID4
from domain.extra.result import Result

from .todo_repository_errors import (
    TodoCreateError,
    TodoUpdateError,
    TodoDeleteError,
    TodoGetByIdError,
    TodoGetCountByUserIdError,
    TodoGetAllByUserIdError,
)


class TodoRepository(Protocol):
    async def create(self, entity: Todo) -> Result[Todo, TodoCreateError]: ...
    async def update(self, entity: Todo) -> Result[Todo, TodoUpdateError]: ...
    async def delete(self, id: UUID4) -> Result[None, TodoDeleteError]: ...
    async def get_by_id(self, id: UUID4) -> Result[Todo, TodoGetByIdError]: ...
    async def get_count_by_user_id(self, id: UUID4) -> Result[int, TodoGetCountByUserIdError]: ...
    async def get_all_by_user_id(
        self, id: UUID4
    ) -> Result[list[Todo], TodoGetAllByUserIdError]: ...
