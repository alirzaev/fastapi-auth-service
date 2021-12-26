#!/bin/sh

celery -A application.worker worker -l info -c 1
