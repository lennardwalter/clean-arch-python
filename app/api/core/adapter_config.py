from domain.ports.repositories import UserRepository

from infra.repositories import MockUserRepository

ADAPTER_CONFIG = {
    UserRepository: MockUserRepository,
}
