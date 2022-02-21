FROM python:3.10.2-slim-buster
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PATH=$HOME/.local/bin:$PATH

COPY . /code

WORKDIR /code

RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN poetry install --no-dev --no-ansi

CMD ["poetry", "run", "server"]
