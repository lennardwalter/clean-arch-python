from infra import MockTodoRepository, MockUserRepository

from domain.ports import TodoRepository, UserRepository


ADAPTER_CONFIG = {
    UserRepository: MockUserRepository,
    TodoRepository: MockTodoRepository,
}
