from typing import Callable, cast

from core.solve_dependencies import solve_services
from app.api.adapter_config import ADAPTER_CONFIG

_service_instances = solve_services(ADAPTER_CONFIG)


def get_service[T](service: T) -> Callable[[], T]:
    def _get_service():
        if service not in _service_instances:
            raise ValueError(f"Service {service} not found")
        return cast(T, _service_instances[service])  # type: ignore

    return _get_service
