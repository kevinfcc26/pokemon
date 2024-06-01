FROM python:3.12

ENV PYTHONUNBUFFERED 1

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

RUN mkdir /app
WORKDIR /app
# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* /app/

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --only main ; fi"

ENV PYTHONPATH=/app



COPY ./app /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

CMD [ "python","manage.py","runserver", "0.0.0.0:8000" ]