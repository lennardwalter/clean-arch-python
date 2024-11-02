from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.api.routes import router
from app.api.core.modify_openapi import modify_openapi

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


app = create_app()

modify_openapi(app)
