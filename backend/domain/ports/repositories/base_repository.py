from typing import Protocol

from domain.entities import EntityBaseModel

from domain.extra.types import UUID4
from domain.extra.result import Result


# TODO: proper error differentiation
type RepositoryError = str


class BaseRepository[T: EntityBaseModel](Protocol):
    async def get_by_id(self, id: UUID4) -> Result[T, RepositoryError]: ...
    async def create(self, entity: T) -> Result[T, RepositoryError]: ...
    async def update(self, entity: T) -> Result[T, RepositoryError]: ...
    async def delete(self, id: UUID4) -> Result[None, RepositoryError]: ...
    async def get_all(self) -> Result[list[T], RepositoryError]: ...
