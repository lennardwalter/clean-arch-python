from domain.ports.repositories import BaseRepository, RepositoryError

from domain.entities import EntityBaseModel

from domain.extra.types import UUID4
from domain.extra.result import *


class MockBaseRepository[T: EntityBaseModel](BaseRepository[T]):

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
        self._entities.append(entity)
        return Ok(entity)

    async def update(self, entity: T) -> Result[T, RepositoryError]:
        for i, e in enumerate(self._entities):
            if e.id == entity.id:
                self._entities[i] = entity
                return Ok(entity)
        return Err("Entity not found")

    async def delete(self, id: UUID4) -> Result[None, RepositoryError]:
        for i, entity in enumerate(self._entities):
            if entity.id == id:
                del self._entities[i]
                return Ok(None)
        return Err("Entity not found")
