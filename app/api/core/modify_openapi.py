from typing import Any
from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.openapi.utils import get_openapi


def change_operation_ids(app: FastAPI) -> None:
    for route in app.routes:
        if isinstance(route, APIRoute):
            camel_case_name = "".join(word.capitalize() for word in route.name.split("_"))
            camel_case_name = camel_case_name[0].lower() + camel_case_name[1:]
            route.operation_id = camel_case_name


def add_security_definitions(schema: dict[str, Any]) -> dict[str, Any]:
    schema["components"]["securitySchemes"] = {
        "bearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }

    for path, path_value in schema["paths"].items():
        for value in path_value.values():
            if path != "/auth/login":
                # add bearer required
                value["security"] = [{"bearerAuth": []}]

                # add 401 response if not present
                if not value["responses"].get("401"):
                    value["responses"]["401"] = {"description": "Unauthorized"}

    return schema


def get_custom_schema_generator(app: FastAPI):
    def get_custom_schema():
        if app.openapi_schema:
            return app.openapi_schema

        openapi_schema = openapi_schema = get_openapi(
            title="OpenAPI schema",
            version="0.1.0",
            description="This is the OpenAPI schema for the API",
            routes=app.routes,
        )

        openapi_schema = add_security_definitions(openapi_schema)

        app.openapi_schema = openapi_schema

        return app.openapi_schema

    return get_custom_schema


def modify_openapi(app: FastAPI) -> None:
    change_operation_ids(app)
    app.openapi = get_custom_schema_generator(app)
