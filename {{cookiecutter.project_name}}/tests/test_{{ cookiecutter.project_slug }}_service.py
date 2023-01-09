from {{ cookiecutter.project_slug }} import __version__
import pytest

from {{ cookiecutter.project_slug }}.handler import Handler
{{ cookiecutter.resource_name}}_hander = Handler()

def test_version():
    assert __version__ == "0.1.0"

@pytest.mark.asyncio()
async def test_api_{{ cookiecutter.resource_name }}():
    result = await {{ cookiecutter.resource_name }}_handler.get_{{ cookiecutter.resource_name }}(data="{{ cookiecutter.project_slug }}")
    assert result == "{{ cookiecutter.project_slug }}"