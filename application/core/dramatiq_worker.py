import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker

from application.core.config import config

rabbitmq_broker = RabbitmqBroker(url=config.MESSAGE_BROKER_URL)
dramatiq.set_broker(rabbitmq_broker)


@dramatiq.actor
def test_celery(word: str) -> None:
    print(f'test task return "{word}"')
