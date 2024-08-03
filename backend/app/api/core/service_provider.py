from typing import cast, Callable

from di import Container, bind_by_type
from di.dependent import Dependent
from di.executors import SyncExecutor

from domain.services import SERVICES

from .adapter_config import ADAPTER_CONFIG

container = Container()

# Bind all ports to their respective adapters
for iface, impl in ADAPTER_CONFIG.items():
    container.bind(bind_by_type(Dependent(impl, scope="singleton"), iface))

# Solve all services and store them
service_instances = {}
for service in SERVICES:
    solved = container.solve(
        Dependent(service, scope="singleton"),
        scopes=["singleton"],
    )

    # Instantiate the service
    with container.enter_scope("singleton") as state:
        service_instances[service] = solved.execute_sync(
            executor=SyncExecutor(), state=state
        )


def get_service[T](service: T) -> Callable[[], T]:
    return lambda: cast(T, service_instances[service])
