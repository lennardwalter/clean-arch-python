from fastapi import FastAPI

from app.api.routes import router


def create_app() -> FastAPI:
    app_ = FastAPI()
    app_.include_router(router)
    return app_


app = create_app()
