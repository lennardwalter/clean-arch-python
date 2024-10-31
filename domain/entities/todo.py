from domain.extra.types import UUID4

from .base_model import EntityBaseModel


class Todo(EntityBaseModel):
    user_id: UUID4
    text: str
    completed: bool
