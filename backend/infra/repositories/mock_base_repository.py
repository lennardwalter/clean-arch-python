from domain.ports.repositories import BaseRepository, RepositoryError

from domain.entities import BaseModel

from domain.extra.types import UUID4
from domain.extra.result import *


class MockBaseRepository[T: BaseModel](BaseRepository[T]):

    def __init__(self, entities: list[T] = []) -> None:
        self._entities = entities

    async def get_by_id(self, id: UUID4) -> Result[T, RepositoryError]:
        for entity in self._entities:
            if entity.id == id:
                return Ok(entity)
        return Err("Entity not found")

    async def get_all(self) -> Result[list[T], RepositoryError]:
        return Ok(self._entities)

    async def create(self, entity: T) -> Result[T, RepositoryError]:
        raise NotImplementedError

    async def update(self, entity: T) -> Result[T, RepositoryError]:
        raise NotImplementedError

    async def delete(self, entity: T) -> Result[None, RepositoryError]:
        raise NotImplementedError
