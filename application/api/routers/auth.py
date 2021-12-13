from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.responses import Response

from application import crud
from application import schemas
from application.api.dependencies import get_db, get_current_user, get_token_payload
from application.core.config import config
from application.core.security import create_access_token
from application.database.models import User
from application.database.redis_client import redis_client

router = APIRouter(tags=['auth'])


@router.post('/signup', response_model=schemas.User)
def create_user(
        user_in: schemas.UserCreate,
        db: Session = Depends(get_db)
):
    user = crud.user.get_by_email(db, user_in.email)

    if user is not None:
        raise HTTPException(
            status_code=400,
            detail='The user with this username already exists in the system.'
        )
    user = crud.user.create(db, user_in)

    return user


@router.post('/signin', response_model=schemas.Token)
def login_user(
        db: Session = Depends(get_db),
        form_data: OAuth2PasswordRequestForm = Depends()
):
    user = crud.user.authenticate(db, form_data.username, form_data.password)

    if user is None:
        raise HTTPException(status_code=400, detail='Incorrect email or password')

    return {
        'access_token': create_access_token(user.id),
        'token_type': 'bearer'
    }


@router.post('/checkToken', response_model=schemas.User)
def check_token(
        current_user: User = Depends(get_current_user)
):
    return current_user


@router.post('/revokeToken', status_code=204)
def revoke_token(
        token_payload: schemas.TokenPayload = Depends(get_token_payload)
):
    jwti = token_payload.jwti

    redis_client.setex(jwti, timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES), 'true')

    return Response(status_code=204)


@router.post('/refreshToken', response_model=schemas.Token)
def refresh_token(
        current_user: User = Depends(get_current_user)
):
    return {
        'access_token': create_access_token(current_user.id),
        'token_type': 'bearer'
    }
