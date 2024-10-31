from domain.extra.types import UUID4, BaseModelConfig, EmailStr


class UserResponse(BaseModelConfig):
    id: UUID4
    email: EmailStr
