from typing import cast

from di import Container, bind_by_type
from di.dependent import Dependent
from di.executors import SyncExecutor

from domain.services import SERVICES


def solve_services[Ks, Vs](adapter_config: dict[Ks, Vs]) -> dict[Ks, Vs]:
    container = Container()
    service_instances = {}

    # Bind all ports to their respective adapters
    for iface, impl in adapter_config.items():
        container.bind(bind_by_type(Dependent(impl, scope="singleton"), iface))  # type: ignore

    for service in SERVICES:
        solved = container.solve(
            Dependent(service, scope="singleton"),
            scopes=["singleton"],
        )

        # Instantiate the service
        with container.enter_scope("singleton") as state:
            service_instances[service] = solved.execute_sync(executor=SyncExecutor(), state=state)

    return cast(dict[Ks, Vs], service_instances)
