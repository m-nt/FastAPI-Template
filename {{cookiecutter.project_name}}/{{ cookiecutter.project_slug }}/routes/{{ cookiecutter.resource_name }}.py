from fastapi import APIRouter, Request, Response, status

{{cookiecutter.resource_name}}_router = APIRouter()


@{{cookiecutter.resource_name}}_router.post("/", status_code=status.HTTP_204_NO_CONTENT)
async def root(request: Request):
    return Response(status_code=status.HTTP_204_NO_CONTENT, content="")
