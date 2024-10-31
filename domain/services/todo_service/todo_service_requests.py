from typing import Optional

from domain.extra.types import UUID4, BaseModelConfig


class TodoCreateRequest(BaseModelConfig):
    requesting_user_id: UUID4
    text: str


class TodoUpdateRequest(BaseModelConfig):
    id: UUID4
    requesting_user_id: UUID4
    text: Optional[str]
    completed: Optional[bool]


class TodoDeleteRequest(BaseModelConfig):
    id: UUID4
    requesting_user_id: UUID4
