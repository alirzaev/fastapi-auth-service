import logging
from typing import Dict, Any

import emails

from application.core.config import config


def send_email(
    email_to: str,
    subject: str = '',
    text: str = '',
    environment: Dict[str, Any] = {},  # noqa
) -> None:
    assert config.EMAILS_ENABLED, 'no provided configuration for email variables'
    message = emails.Message(
        mail_from=('Project', 'info@example.com'),
        subject=subject,
        text=text,
    )
    smtp_options = dict(host=config.SMTP_HOST, port=config.SMTP_PORT)
    if config.SMTP_TLS:
        smtp_options['tls'] = True
    if config.SMTP_USER:
        smtp_options['user'] = config.SMTP_USER
    if config.SMTP_PASSWORD:
        smtp_options['password'] = config.SMTP_PASSWORD
    response = message.send(to=email_to, render=environment, smtp=smtp_options)
    logging.info(f'send email result: {response}')


def send_test_email(email_to: str) -> None:
    send_email(
        email_to=email_to,
        subject='Test email',
        text='Test email',
    )
