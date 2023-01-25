from dataclasses import dataclass

from fastapi import FastAPI

from {{ cookiecutter.project_slug }}.settings import get_settings
from {{ cookiecutter.project_slug }}.handler.{{ cookiecutter.resource_name }} import (
    {{ cookiecutter.resource_name }}_Handler
)
_SETTINGS = get_settings()


@dataclass
class Context:
    pass


def get_context() -> Context:
    return Context()


async def set_context(app: FastAPI) -> None:
    app.state.context = get_context()
