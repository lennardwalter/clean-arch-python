from pydantic import EmailStr, UUID4, BaseModel as PydanticBaseModel


class BaseModelConfig(PydanticBaseModel):
    class Config:
        pass


__all__ = ["EmailStr", "UUID4"]
