from asyncio import current_task
from typing import Any

from sanic import Sanic
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_scoped_session
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(
        self,
        app: Sanic | None = None,
        *,
        metadata: MetaData | None = None,
        engine_options: dict[str, Any] | None = None,
        session_options: dict[str, Any] | None = None,
    ):
        if session_options is None:
            session_options = {}

        self.session = self._sesion_factory(session_options)
        self.async_session = self._async_session_factory(session_options)

        self.metadatas: dict[str | None, MetaData] = {}
        if metadata is not None:
            metadata.info["bind_key"] = None
            self.metadatas[None] = metadata

        if engine_options is None:
            engine_options = {}

        self._engine_options = engine_options
        
        if app is not None:
            self.init_app(app)

    def __repr__(self) -> str:
        if not self.engine:
            return f"{type(self).__name__}"
        return f"{type(self).__name__} {self.engine.url}"

    def init_app(self, app: Sanic) -> None:
        db_uri: str | None = app.config["DB_URI"]
        db_echo: bool = app.config.get("DB_ECHO", False)

        self.engine = create_async_engine(db_uri, echo=db_echo)

    def _sesion_factory(
        self, options: dict[str, Any]
    ) -> async_scoped_session[AsyncSession]:
        options.setdefault("class_", AsyncSession)
        factory = sessionmaker(db=self, **options)
        return async_scoped_session(factory, current_task)

    def _async_session_factory(
        self, options: dict[str, Any]
    ) -> async_scoped_session[AsyncSession]:
        options.setdefault("class_", AsyncSession)
        factory = async_sessionmaker(db=self, **options)
        return async_scoped_session(factory, current_task)
