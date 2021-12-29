from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from application.core.config import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)
