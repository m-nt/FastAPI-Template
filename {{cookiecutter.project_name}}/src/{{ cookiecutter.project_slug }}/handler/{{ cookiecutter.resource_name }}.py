import dataclasses
from motor.motor_asyncio import AsyncIOMotorCollection
from typing import Any

@dataclasses.dataclass
class {{ cookiecutter.resource_name }}_Handler:
    {{ cookiecutter.resource_name }}: AsyncIOMotorCollection
    # TODO: add functions to handle requests
    async def get_{{ cookiecutter.resource_name }}(
        self,
        data: str,
    ) -> Any:
        return data