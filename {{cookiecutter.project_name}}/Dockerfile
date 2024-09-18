FROM python:3.11-slim
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    supervisor \
    vim \
    net-tools

EXPOSE 3000
RUN pip install poetry

WORKDIR /app
COPY . /app/
COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
ENV WEB_CONCURRENCY=2

ADD ./src/{{ cookiecutter.project_slug }}/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
