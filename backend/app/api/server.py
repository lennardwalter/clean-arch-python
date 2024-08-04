from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router


CORS_ORIGINS = ["http://localhost:5173"]


def create_app() -> FastAPI:
    app_ = FastAPI()

    app_.include_router(router)

    app_.add_middleware(
        CORSMiddleware,
        allow_origins=CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app_


def use_route_names_as_op_id(app: FastAPI) -> None:
    for route in app.routes:
        if isinstance(route, APIRoute):
            camel_case_name = "".join(
                word.capitalize() for word in route.name.split("_")
            )
            camel_case_name = camel_case_name[0].lower() + camel_case_name[1:]
            route.operation_id = camel_case_name


app = create_app()

use_route_names_as_op_id(app)
