import dataclasses
from pymongo.collection import Collection
from typing import Any

@dataclasses.dataclass
class {{ cookiecutter.resource_name }}_Handler:
    collection: Collection
    # TODO: add functions to handle requests
    async def get_{{ cookiecutter.resource_name }}(
        self,
        data: str,
    ) -> Any:
        return data