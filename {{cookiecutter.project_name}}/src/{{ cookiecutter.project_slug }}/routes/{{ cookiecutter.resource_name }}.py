from fastapi import APIRouter, Request, Response, status, Depends

{{cookiecutter.resource_name}}_router = APIRouter()
from {{ cookiecutter.project_slug }}.init import Context, get_context_from_request

@{{cookiecutter.resource_name}}_router.post("/", status_code=status.HTTP_204_NO_CONTENT)
async def root(
    request: Request,
    context: Context = Depends(get_context_from_request)
):
    return Response(status_code=status.HTTP_204_NO_CONTENT, content="")
