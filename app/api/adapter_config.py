from domain.ports import UserRepository, TodoRepository

from infra import MockUserRepository, MockTodoRepository

ADAPTER_CONFIG = {
    UserRepository: MockUserRepository,
    TodoRepository: MockTodoRepository,
}
