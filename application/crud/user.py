from sqlalchemy.orm import Session

from application.core.security import get_password_hash, verify_password
from application.database.models import User
from application.schemas import UserCreate


def create(db: Session, user_in: UserCreate) -> User:
    user = User(
        email=user_in.email,
        name=user_in.name,
        hashed_password=get_password_hash(user_in.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get(db: Session, id: int) -> User | None:  # noqa
    return db.query(User).filter(User.id == id).first()


def get_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()


def authenticate(db: Session, email: str, password: str) -> User | None:
    user = get_by_email(db, email)

    if user is None:
        return None
    elif not verify_password(password, user.hashed_password):
        return None
    else:
        return user
