from domain.extra.types import EmailStr

from .base_model import EntityBaseModel


class User(EntityBaseModel):
    email: EmailStr
    hashed_password: str
