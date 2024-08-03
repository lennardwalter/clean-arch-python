from pydantic import BaseModel as PydanticBaseModel

from domain.extra.types import UUID4


class BaseModel(PydanticBaseModel):
    id: UUID4

    class Config:
        regex_engine = "python-re"
