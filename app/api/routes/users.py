from typing import Annotated

from fastapi import APIRouter, HTTPException, Depends

from domain.services import UserService
from domain.entities import User
from domain.extra.result import *

from app.api.core.service_provider import get_service


router = APIRouter()


@router.get(
    "/",
    responses={
        200: {"model": list[User]},
        500: {"description": "Internal Server Error"},
    },
)
async def get_users(
    user_service: Annotated[UserService, Depends(get_service(UserService))]
) -> list[User]:
    match await user_service.get_all_users():
        case Ok(users):
            return users
        case Err(err):
            # TODO: proper handling obviously
            raise HTTPException(status_code=500, detail=err)
