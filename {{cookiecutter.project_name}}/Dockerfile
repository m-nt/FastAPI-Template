FROM python:3.11-slim
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    supervisor

EXPOSE 3000
RUN pip install poetry

WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

RUN poetry install --no-dev
ENV WEB_CONCURRENCY=2

WORKDIR /app
COPY . /app/
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
