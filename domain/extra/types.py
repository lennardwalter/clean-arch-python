from pydantic import UUID4, BaseModel as PydanticBaseModel, EmailStr


class BaseModelConfig(PydanticBaseModel):
    class Config:
        pass


__all__ = ["EmailStr", "UUID4"]
