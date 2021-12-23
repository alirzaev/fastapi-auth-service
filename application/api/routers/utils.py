from fastapi import APIRouter, Depends, BackgroundTasks
from pydantic import EmailStr
from starlette.responses import Response

from application.api.dependencies import get_current_user
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
