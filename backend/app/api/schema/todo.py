from typing import Optional

from domain.extra.types import BaseModelConfig, UUID4


class TodoResponse(BaseModelConfig):
    id: UUID4
    text: str
    completed: bool


class TodoUpdateRequest(BaseModelConfig):
    text: Optional[str] = None
    completed: Optional[bool] = None


class TodoCreateRequest(BaseModelConfig):
    text: str
