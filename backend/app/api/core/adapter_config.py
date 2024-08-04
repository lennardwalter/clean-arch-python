from domain.ports.repositories import UserRepository, TodoRepository

from infra.repositories import MockUserRepository, MockTodoRepository

ADAPTER_CONFIG = {
    UserRepository: MockUserRepository,
    TodoRepository: MockTodoRepository,
}
