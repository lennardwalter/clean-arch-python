from datetime import datetime, timedelta, timezone
from typing import Annotated, Optional, Callable, Awaitable, Any
from uuid import UUID

import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import Depends, HTTPException, status, Request
from passlib.context import CryptContext

from domain.entities import User
from domain.extra.types import EmailStr
from domain.extra.result import *
from domain.services import UserService

from app.api.core.service_provider import get_service
from app.api.schema import PasswordStr

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: PasswordStr, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: PasswordStr) -> str:
    return pwd_context.hash(password)


type AuthenticateUserFunctionType = Callable[
    [EmailStr, PasswordStr], Awaitable[Optional[User]]
]


def get_token(request: Request) -> str:

    exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Not authenticated",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token = request.headers.get("Authorization")

    if not token:
        raise exc

    split_token = token.split(" ")
    if len(split_token) != 2 or split_token[0] != "Bearer":
        raise exc

    return split_token[1]


def get_authenticate_user(
    user_service: Annotated[UserService, Depends(get_service(UserService))]
) -> AuthenticateUserFunctionType:

    async def authenticate_user(
        email: EmailStr, password: PasswordStr
    ) -> Optional[User]:
        user_result = await user_service.get_user_by_email(email)

        match user_result:
            case Ok(user):
                if not verify_password(password, user.hashed_password):
                    return None
                return user
            case Err(_):
                return None

    return authenticate_user


def create_access_token(data: dict[str, Any], expires_delta: timedelta) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(
    token: Annotated[str, Depends(get_token)],
    user_service: Annotated[UserService, Depends(get_service(UserService))],
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: Optional[str] = payload.get("sub")
        if user_id is None:
            raise credentials_exception

    except InvalidTokenError:
        raise credentials_exception

    user_result = await user_service.get_user_by_id(UUID(user_id))

    match user_result:
        case Ok(user):
            return user
        case Err(_):
            raise credentials_exception
