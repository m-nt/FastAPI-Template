import motor.motor_asyncio
from pymongo.collection import Collection

from {{ cookiecutter.project_slug }}.settings import get_settings

_settings = get_settings()

client = motor.motor_asyncio.AsyncIOMotorClient(_settings.DATABASE_URL)
_database = client.get_database("{{ cookiecutter.project_name }}")

{{cookiecutter.project_slug}}s_collection: Collection = _database.get_collection("{{ cookiecutter.resource_name }}")


