from fastapi import APIRouter, Depends, BackgroundTasks, Body
from pydantic import EmailStr
from starlette.responses import Response

from application.api.dependencies import get_current_user
from application.core.celery_app import celery_app
from application.database.models import User
from application.utils import send_test_email

router = APIRouter(tags=['utils'])


@router.post('/test-email', status_code=204)
def test_email(
        email_to: EmailStr,
        background_tasks: BackgroundTasks,
        _: User = Depends(get_current_user)
):
    background_tasks.add_task(send_test_email, email_to)
    return Response(status_code=204)


@router.post("/test-celery/", status_code=204)
def test_celery(
        message: str = Body(...),
        _: User = Depends(get_current_user)
):
    celery_app.send_task('application.worker.test_celery', args=[message])
    return Response(status_code=204)
