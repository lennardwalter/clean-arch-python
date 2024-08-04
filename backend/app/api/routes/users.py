from typing import Annotated, cast

from fastapi import APIRouter, HTTPException, Depends, Response

from domain.services import TodoService
from domain.entities import User
from domain.extra.result import *
from domain.extra.types import UUID4

from app.api.core.service_provider import get_service
from app.api.core.auth import get_current_user
from app.api.schema import TodoResponse, TodoUpdateRequest, TodoCreateRequest

router = APIRouter(responses={401: {"description": "Unauthorized"}})


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
    match await todo_service.get_todos_by_user_id(current_user.id):
        case Ok(value):
            return cast(list[TodoResponse], value)
        case Err(error):
            raise HTTPException(status_code=500, detail=error)


@router.post(
    "/@me/todos",
    responses={
        201: {"description": "Todo created successfully"},
        500: {"description": "Internal Server Error"},
    },
    status_code=201,
)
async def create_todo(
    todo: TodoCreateRequest,
    todo_service: Annotated[TodoService, Depends(get_service(TodoService))],
    current_user: Annotated[User, Depends(get_current_user)],
) -> TodoResponse:
    match await todo_service.create_todo(current_user.id, todo.text):
        case Ok(value):
            return cast(TodoResponse, value)
        case Err(error):
            raise HTTPException(status_code=500, detail=error)


@router.patch(
    "/@me/todos/{todo_id}",
    responses={
        200: {"description": "Todo updated successfully"},
        500: {"description": "Internal Server Error"},
    },
)
async def update_todo(
    todo_id: UUID4,
    todo: TodoUpdateRequest,
    todo_service: Annotated[TodoService, Depends(get_service(TodoService))],
) -> TodoResponse:
    # TODO: check if the todo belongs to the user
    update_res = await todo_service.update_todo(
        todo_id, **todo.model_dump(exclude_unset=True)
    )

    match update_res:
        case Ok(value):
            return cast(TodoResponse, value)
        case Err(error):
            raise HTTPException(status_code=500, detail=error)


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
):
    match await todo_service.delete_todo(todo_id):
        case Ok(_):
            return Response(status_code=204)
        case Err(error):
            raise HTTPException(status_code=500, detail=error)
