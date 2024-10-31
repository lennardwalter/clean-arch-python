from typing import final
from uuid import UUID, uuid4

from domain.entities import Todo
from domain.ports.todo_repository import (
    TodoRepository,
    TodoNotFoundError,
    TodoCreateError,
    TodoUpdateError,
    TodoDeleteError,
    TodoGetByIdError,
    TodoGetCountByUserIdError,
    TodoGetAllByUserIdError,
)
from domain.extra.types import UUID4
from domain.extra.result import *


@final
class MockTodoRepository(TodoRepository):

    def __init__(self) -> None:
        self._entities = [
            Todo(
                id=uuid4(),
                user_id=UUID("f5f4b3b4-3b4b-4b3b-b43b-4b3b4b3b4b3b"),
                text="Buy milk",
                completed=False,
            ),
            Todo(
                id=uuid4(),
                user_id=UUID("f5f4b3b4-3b4b-4b3b-b43b-4b3b4b3b4b3b"),
                text="Buy eggs",
                completed=True,
            ),
        ]

    async def create(self, entity: Todo) -> Result[Todo, TodoCreateError]:
        self._entities.append(entity)
        return Ok(entity)

    async def update(self, entity: Todo) -> Result[Todo, TodoUpdateError]:
        for i, e in enumerate(self._entities):
            if e.id == entity.id:
                self._entities[i] = entity
                return Ok(entity)
        return Err(TodoNotFoundError())

    async def delete(self, id: UUID4) -> Result[None, TodoDeleteError]:
        for i, entity in enumerate(self._entities):
            if entity.id == id:
                del self._entities[i]
                return Ok(None)
        return Err(TodoNotFoundError())

    async def get_by_id(self, id: UUID4) -> Result[Todo, TodoGetByIdError]:
        for entity in self._entities:
            if entity.id == id:
                return Ok(entity)
        return Err(TodoNotFoundError())

    async def get_all_by_user_id(self, id: UUID4) -> Result[list[Todo], TodoGetAllByUserIdError]:
        todos = [todo for todo in self._entities if todo.user_id == id]
        return Ok(todos)

    async def get_count_by_user_id(self, id: UUID4) -> Result[int, TodoGetCountByUserIdError]:
        count = len([todo for todo in self._entities if todo.user_id == id])
        return Ok(count)
