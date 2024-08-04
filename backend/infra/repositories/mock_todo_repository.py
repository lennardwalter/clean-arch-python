from typing import final
from uuid import UUID, uuid4

from domain.entities import Todo
from domain.ports.repositories import TodoRepository, RepositoryError
from domain.extra.types import UUID4
from domain.extra.result import *

from .mock_base_repository import MockBaseRepository


@final
class MockTodoRepository(TodoRepository, MockBaseRepository[Todo]):

    def __init__(self) -> None:
        super().__init__(
            [
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
        )

    async def get_all_by_user_id(
        self, id: UUID4
    ) -> Result[list[Todo], RepositoryError]:
        todos = [todo for todo in self._entities if todo.user_id == id]
        return Ok(todos)
