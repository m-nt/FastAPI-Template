from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from {{cookiecutter.project_slug}}.init import set_context
from {{ cookiecutter.project_slug }}.settings import get_settings
from {{ cookiecutter.project_slug }}.routes.{{ cookiecutter.resource_name }} import {{ cookiecutter.resource_name }}_router
from {{ cookiecutter.project_slug }}.deps import ExampleMiddleware

_settings = get_settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup...
    print(f"\033[32;5mINFO:     \033[70;0mYeeePeee!")
    await set_context(app)
    yield
    print("\033[32;5mINFO:     \033[70;0mBYeYeeyeyye!")
    # Cleanups...

if _settings.ENV_MODE == "prod":
    app = FastAPI(root_path="/{{ cookiecutter.resource_name }}/v1", lifespan=lifespan)
else:
    app = FastAPI(lifespan=lifespan)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(ExampleMiddleware)

@app.get("/liveness")
def liveness():
    return "OK"

app.include_router({{ cookiecutter.resource_name }}_router)
