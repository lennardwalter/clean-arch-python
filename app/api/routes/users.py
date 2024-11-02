from typing import Annotated, NoReturn, cast

from fastapi import APIRouter, Depends, HTTPException, Response

from app.api.core.auth import get_current_user
from app.api.core.services import get_service
from app.api.schema import TodoCreateRequest, TodoResponse, TodoUpdateRequest

from domain.entities import User
from domain.extra.result import Err, Ok
from domain.extra.types import UUID4
from domain.services.todo_service import (
    RequestingUserNotFoundError,
    TodoCreateRequest as ServiceTodoCreateRequest,
    TodoDeleteRequest as ServiceTodoDeleteRequest,
    TodoLimitReachedError,
    TodoNotFoundError,
    TodoService,
    TodoUpdateRequest as ServiceTodoUpdateRequest,
    UnauthorizedError,
)


router = APIRouter()


def assert_never(x: NoReturn) -> NoReturn:
    assert False, "Unhandled type: {}".format(type(x).__name__)


@router.get(
    "/@me/todos",
    responses={
        200: {"model": list[TodoResponse], "description": "List of todos"},
        500: {"description": "Internal Server Error"},
    },
)
async def get_my_todos(
    todo_service: Annotated[TodoService, Depends(get_service(TodoService))],
    current_user: Annotated[User, Depends(get_current_user)],
) -> list[TodoResponse]:
    match await todo_service.get_todos_by_user_id(current_user.id, current_user.id):
        case Ok(value):
            return cast(list[TodoResponse], value)
        # TODO: do this without nesting match
        case Err(e):
            match e:
                case RequestingUserNotFoundError() | UnauthorizedError():
                    # this should never happen, the current user should always exist
                    # and the requesting user shold always have access to their own todos
                    raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post(
    "/@me/todos",
    responses={
        201: {"description": "Todo created successfully"},
        429: {"description": "Todo limit reached"},
        500: {"description": "Internal Server Error"},
    },
    status_code=201,
)
async def create_todo(
    todo: TodoCreateRequest,
    todo_service: Annotated[TodoService, Depends(get_service(TodoService))],
    current_user: Annotated[User, Depends(get_current_user)],
) -> TodoResponse:
    match await todo_service.create_todo(
        ServiceTodoCreateRequest(
            requesting_user_id=current_user.id,
            text=todo.text,
        )
    ):
        case Ok(value):
            return cast(TodoResponse, value)
        case Err(e):
            match e:
                case TodoLimitReachedError():
                    raise HTTPException(status_code=429, detail="Todo limit reached")
                case RequestingUserNotFoundError():
                    # the current user should always exist, this would be a bug -> server error
                    raise HTTPException(status_code=500, detail="Internal Server Error")


@router.patch(
    "/@me/todos/{todo_id}",
    responses={
        200: {"description": "Todo updated successfully"},
        404: {"description": "Todo not found"},
        500: {"description": "Internal Server Error"},
    },
)
async def update_todo(
    todo_id: UUID4,
    todo: TodoUpdateRequest,
    todo_service: Annotated[TodoService, Depends(get_service(TodoService))],
    current_user: Annotated[User, Depends(get_current_user)],
) -> TodoResponse:
    update_res = await todo_service.update_todo(
        ServiceTodoUpdateRequest(
            id=todo_id,
            requesting_user_id=current_user.id,
            text=todo.text,
            completed=todo.completed,
        )
    )

    match update_res:
        case Ok(value):
            return cast(TodoResponse, value)
        case Err(e):
            match e:
                case TodoNotFoundError():
                    raise HTTPException(status_code=404, detail="Todo not found")
                case UnauthorizedError():
                    raise HTTPException(status_code=401, detail="Unauthorized")
                case RequestingUserNotFoundError():
                    # the current user should always exist, this would be a bug -> server error
                    raise HTTPException(status_code=500, detail="Internal Server Error")


@router.delete(
    "/@me/todos/{todo_id}",
    responses={
        204: {"description": "Todo deleted successfully"},
        500: {"description": "Internal Server Error"},
    },
    status_code=204,
)
async def delete_todo(
    todo_id: UUID4,
    todo_service: Annotated[TodoService, Depends(get_service(TodoService))],
    current_user: Annotated[User, Depends(get_current_user)],
):
    match await todo_service.delete_todo(
        ServiceTodoDeleteRequest(
            id=todo_id,
            requesting_user_id=current_user.id,
        )
    ):
        case Ok(_):
            return Response(status_code=204)
        case Err(error):
            raise HTTPException(status_code=500, detail=error)
