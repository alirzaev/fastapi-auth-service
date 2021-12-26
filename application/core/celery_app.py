from celery import Celery

from application.core.config import config

celery_app = Celery('worker', broker=config.CELERY_BROKER_URL)
