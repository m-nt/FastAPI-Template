from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class ExampleMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app,
    ):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        return response
