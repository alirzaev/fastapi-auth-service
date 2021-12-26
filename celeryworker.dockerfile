FROM python:3.10
EXPOSE 80

WORKDIR /usr/src/project

COPY pyproject.toml poetry.lock* ./

RUN pip install --no-cache-dir poetry && poetry config virtualenvs.create false
RUN poetry install --no-root

COPY . .

CMD ["./docker/runworker.sh"]
