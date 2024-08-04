from uuid import uuid4

from pydantic import Field

from domain.extra.types import UUID4, BaseModelConfig


class EntityBaseModel(BaseModelConfig):
    id: UUID4 = Field(default_factory=uuid4)
