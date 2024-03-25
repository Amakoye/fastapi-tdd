import pathlib
from typing import Tuple
from fastapi import APIRouter, Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core import settings
from core.docs import docs_router


# from starlette.middleware.sessions import SessionMiddleware


class App:
    """
    Create an app instance
    """

    def __init__(
        self,
        app_name: str,
        routers: Tuple[APIRouter] = [],
        APP_HOME=None,
        description: str | None = None,
        prefix: str | None = None,
    ) -> None:
        self.app_name = app_name
        self.description = description
        self.routers = routers
        settings.APP_PREFIX = self.prefix = prefix

    def configure(self):
        app = FastAPI(
            debug="",
            title=self.app_name,
            description=self.description,
            openapi_url=self.prefix + "/openapi.json" if self.prefix else None,
        )

        origins = ["*"]

        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        base_router = APIRouter(prefix=self.prefix) if self.prefix else app

        for router in self.routers:
            base_router.include_router(router)

        base_router.include_router(docs_router)

        if self.prefix:
            app.include_router(base_router)

        return app
