from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from {{cookiecutter.project_slug}}.init import set_context
from {{ cookiecutter.project_slug }}.settings import get_settings
from {{ cookiecutter.project_slug }}.routes.{{ cookiecutter.resource_name }} import {{ cookiecutter.resource_name }}_router

_settings = get_settings()

if _settings.ENV_MODE == "prod":
    app = FastAPI(root_path="/{{ cookiecutter.resource_name }}/v1")
else:
    app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await set_context(app)

app.include_router({{ cookiecutter.resource_name }}_router)
