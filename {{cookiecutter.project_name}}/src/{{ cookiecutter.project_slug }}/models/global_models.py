from typing import Any, Optional
from pydantic import BaseModel


class GeneralResponse(BaseModel):
    message: Optional[Any] = None


class ExceptionModel(BaseModel):
    detail: str
