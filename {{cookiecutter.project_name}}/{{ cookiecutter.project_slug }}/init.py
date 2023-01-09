from dataclasses import dataclass

from fastapi import FastAPI

from {{ cookiecutter.project_slug }} import db, settings
from {{ cookiecutter.project_slug }}.handlers import (
    {{ cookiecutter.resource_name }}
)
_SETTINGS = settings.Settings()


@dataclass
class Context:
    pass


def get_context() -> Context:
    return Context()


async def set_context(app: FastAPI) -> None:
    app.state.context = get_context()
