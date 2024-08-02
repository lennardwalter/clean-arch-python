from domain.extra.types import EmailStr, PasswordStr

from .base_model import BaseModel


class User(BaseModel):
    email: EmailStr
    password: PasswordStr
