from pydantic import EmailStr, UUID4, BaseModel as PydanticBaseModel


class BaseModelConfig(PydanticBaseModel):
    class Config:
        regex_engine = "python-re"


__all__ = ["EmailStr", "UUID4"]
