from pydantic import BaseSettings


class Config(BaseSettings):
    DEBUG: bool = True

    SQLALCHEMY_DATABASE_URL: str = 'postgresql://postgres:postgres@localhost:5432/postgres'

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    SECRET_KEY: str = 'very_secret_key'


config = Config()
