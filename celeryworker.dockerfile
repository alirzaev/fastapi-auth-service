FROM python:3.10-slim
EXPOSE 80

WORKDIR /usr/src/project

COPY pyproject.toml poetry.lock* ./

RUN pip install --no-cache-dir poetry && poetry config virtualenvs.create false
RUN poetry install --no-root

COPY . .

RUN chmod +x ./docker/runworker.sh

CMD ["./docker/runworker.sh"]
