from dataclasses import dataclass

from starlette.middleware.base import BaseHTTPMiddleware

from fastapi import FastAPI

from {{ cookiecutter.project_slug }}.settings import get_settings
from {{ cookiecutter.project_slug }}.handler.{{ cookiecutter.resource_name }} import {{ cookiecutter.resource_name }}_Handler
from {{ cookiecutter.project_slug }}.db import {{cookiecutter.project_slug}}s_collection
_SETTINGS = get_settings()


@dataclass
class Context:
    {{ cookiecutter.resource_name }}_handler: {{ cookiecutter.resource_name }}_Handler

_{{ cookiecutter.resource_name }}_handler = {{ cookiecutter.resource_name }}_Handler(collection={{cookiecutter.project_slug}}s_collection)

class ExampleMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app,
    ):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        return response

def get_context() -> Context:
    return Context(
        {{ cookiecutter.resource_name }}_handler = _{{ cookiecutter.resource_name }}_handler,
    )


async def set_context(app: FastAPI) -> None:
    app.add_middleware(ExampleMiddleware)
    app.state.context = get_context()
