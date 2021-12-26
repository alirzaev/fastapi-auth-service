from application.core.celery_app import celery_app


@celery_app.task
def test_celery(word: str) -> str:
    return f'test task return "{word}"'
