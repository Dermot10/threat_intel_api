from celery import Celery
from dotenv import load_dotenv
import os

load_dotenv()

RABBITMQ_URL = os.getenv("RABBITMQ_URL")

# Celery Configuration
celery_app = Celery(
    "intel_tasks",
    broker=RABBITMQ_URL,
    backend="rpc://"
)

celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)
