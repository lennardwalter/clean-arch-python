from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.core.auth import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    AuthenticateUserFunctionType,
    create_access_token,
    get_authenticate_user,
)
from app.api.schema import AuthRequest, Token


router = APIRouter()


@router.post(
    "/login",
    responses={
        200: {"description": "Login successful"},
        401: {"description": "Unauthorized"},
    },
)
async def login(
    auth_req: AuthRequest,
    authenticate_user: Annotated[AuthenticateUserFunctionType, Depends(get_authenticate_user)],
) -> Token:
    user = await authenticate_user(auth_req.email, auth_req.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": str(user.id)}, expires_delta=access_token_expires)
    return Token(access_token=access_token, token_type="bearer")
