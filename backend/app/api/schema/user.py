from domain.extra.types import BaseModelConfig, UUID4, EmailStr


class UserResponse(BaseModelConfig):
    id: UUID4
    email: EmailStr
