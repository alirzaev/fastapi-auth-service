from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from application import crud
from application.core import security
from application.core.config import config
from application.database.models import User
from application.database.session import SessionLocal
from application.schemas import TokenPayload

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl='/auth/signin')


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()  # noqa


def get_current_user(
        db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> User:
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=security.ALGORITHM)
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=403,
            detail='Could not validate credentials'
        )

    user = crud.user.get(db, token_data.sub)

    if user is None:
        raise HTTPException(status_code=404, detail='User not found')

    return user
