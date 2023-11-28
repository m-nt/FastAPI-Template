from {{ cookiecutter.project_slug }} import __version__
import pytest
from httpx import AsyncClient

BASE_URL = "http://localhost:8000"

def test_version():
    assert __version__ == "0.1.0"

async def get_test(url, headers, params, status):
    async with AsyncClient(base_url=BASE_URL) as client:
        res = await client.get(url=url, headers=headers, params=params)
    assert res.status_code == status


async def post_test(url, headers, params, body, status):
    async with AsyncClient(base_url=BASE_URL) as client:
        res = await client.post(url=url, headers=headers, params=params, json=body)
    assert res.status_code == status

@pytest.mark.asyncio()
async def test_api_{{ cookiecutter.resource_name }}():
    await get_test("/{{ cookiecutter.resource_name }}", {}, {}, 200)
