from typing import Optional

from domain.ports.repositories import TodoRepository, RepositoryError
from domain.entities import Todo
from domain.extra.types import UUID4
from domain.extra.result import *


class TodoService:
    def __init__(self, todo_repo: TodoRepository):
        self.todo_repo = todo_repo

    async def get_todos_by_user_id(
        self, user_id: UUID4
    ) -> Result[list[Todo], RepositoryError]:
        return await self.todo_repo.get_all_by_user_id(user_id)

    async def create_todo(
        self, user_id: UUID4, text: str
    ) -> Result[Todo, RepositoryError]:
        todo = Todo(user_id=user_id, text=text, completed=False)
        return await self.todo_repo.create(todo)

    # TODO: think about how to handle patch, should repository accept partial entities? (need to maintain partial DTOs)
    # this is stupid obviously
    async def update_todo(
        self, id: UUID4, text: Optional[str] = None, completed: Optional[bool] = None
    ) -> Result[Todo, RepositoryError]:
        match await self.todo_repo.get_by_id(id):
            case Err(e):
                return Err(e)
            case Ok(t):
                todo = t

        if text is not None:
            todo.text = text
        if completed is not None:
            todo.completed = completed

        return await self.todo_repo.update(todo)

    async def delete_todo(self, id: UUID4) -> Result[None, RepositoryError]:
        return await self.todo_repo.delete(id)
