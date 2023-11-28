FROM python:3.10-slim
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    build-essential

RUN pip install poetry

WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

RUN poetry export --without-hashes -f requirements.txt > requirements.txt
RUN pip install -r requirements.txt


WORKDIR /app
COPY . /app/
CMD uvicorn {{ cookiecutter.project_slug }}.app:app --host 0.0.0.0 --port 3000 --workers 2
