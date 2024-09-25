from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp, Message, Receive, Scope, Send

# Optimized middleware
class StarletteExampleMiddleware:
    app: ASGIApp
    def __init__(
        self,
        app: ASGIApp,
    ):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        # init
        async def send_wrapper(message: Message) -> None:
            # do somethign...
            await send(message)
        await self.app(scope, receive, send_wrapper)

class ExampleMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app,
    ):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        return response
