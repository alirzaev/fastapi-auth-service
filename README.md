# FastAPI auth service

An example of FastAPI backend with an authentication system

## Project setup

### Development

```shell script
poetry install

docker-compose up -d db redis queue mailhog
alembic upgrade head
# backend
python -m application.asgi
# celery worker
celery -A application.worker worker -l info -c 1
```

### Docker

```shell script
docker-compose up -d app
```

## API documentation

Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)