from domain.entities import Todo
from domain.extra.result import Err, Ok, Result, unwrap_if_never
from domain.extra.types import UUID4
from domain.ports.todo_repository import TodoRepository
from domain.services.shared import UnauthorizedError

from .todo_service_errors import (
    TodoCreateError,
    TodoDeleteError,
    TodoGetAllByUserIdError,
    TodoLimitReachedError,
    TodoUpdateError,
)
from .todo_service_requests import (
    TodoCreateRequest,
    TodoDeleteRequest,
    TodoUpdateRequest,
)


class TodoService:
    def __init__(self, todo_repo: TodoRepository):
        self.todo_repo = todo_repo

    async def get_todos_by_user_id(
        self, requesting_user_id: UUID4, requested_user_id: UUID4
    ) -> Result[list[Todo], TodoGetAllByUserIdError]:
        if requesting_user_id != requested_user_id:
            return Err(UnauthorizedError())

        return Ok(unwrap_if_never(await self.todo_repo.get_all_by_user_id(requested_user_id)))

    async def create_todo(self, todo_create_request: TodoCreateRequest) -> Result[Todo, TodoCreateError]:

        # check if the user has reached the maximum number of todos
        count = unwrap_if_never(
            await self.todo_repo.get_count_by_user_id(todo_create_request.requesting_user_id)
        )
        if count >= 10:
            return Err(TodoLimitReachedError())

        todo = Todo(
            user_id=todo_create_request.requesting_user_id,
            text=todo_create_request.text,
            completed=False,
        )

        return Ok(unwrap_if_never(await self.todo_repo.create(todo)))

    async def update_todo(self, todo_update_request: TodoUpdateRequest) -> Result[Todo, TodoUpdateError]:

        # first fetch the todo
        match await self.todo_repo.get_by_id(todo_update_request.id):
            case Err(e):
                return Err(e)
            case Ok(t):
                todo = t

        # check if the requesting user is the owner of the todo, if not return an UnauthorizedError
        if todo.user_id != todo_update_request.requesting_user_id:
            return Err(UnauthorizedError())

        # update the parts of the todo that are not None in the request
        if todo_update_request.text is not None:
            todo.text = todo_update_request.text
        if todo_update_request.completed is not None:
            todo.completed = todo_update_request.completed

        # finally update the todo
        match await self.todo_repo.update(todo):
            case Ok(updated_todo):
                return Ok(updated_todo)
            case Err(e):
                return Err(e)

    async def delete_todo(self, todo_delete_request: TodoDeleteRequest) -> Result[None, TodoDeleteError]:
        # first fetch the todo
        match await self.todo_repo.get_by_id(todo_delete_request.id):
            # if not found, it will return an EntityNotFoundError, return it
            case Err(e):
                return Err(e)
            case Ok(t):
                todo = t

        # check if the requesting user is the owner of the todo, if not return an UnauthorizedError
        if todo.user_id != todo_delete_request.requesting_user_id:
            return Err(UnauthorizedError())

        # finally delete the todo
        match await self.todo_repo.delete(todo.id):
            case Ok(_):
                return Ok(None)
            case Err(e):
                return Err(e)
