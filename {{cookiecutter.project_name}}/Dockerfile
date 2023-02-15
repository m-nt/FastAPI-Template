FROM python:3.9-alpine
WORKDIR /app

# RUN pip install poetry && poetry config virtualenvs.create false

# ADD pyproject.toml pyproject.toml
# ADD poetry.lock poetry.lock

# RUN poetry export --without-hashes -f requirements.txt > /app/requirements.txt
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ENV WEB_CONCURRENCY=2
COPY user_service /app/user_service

CMD ["uvicorn", "user_service.app:app", "--host", "0.0.0.0", "--port", "8000"]
