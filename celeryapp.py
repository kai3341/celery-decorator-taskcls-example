from celery import Celery
from celery_pool_asyncio import monkey as cpa_monkey
import celery_decorator_taskcls

import settings


cpa_monkey.patch()
celery_decorator_taskcls.patch_celery()

celeryapp = Celery()
celeryapp.config_from_object(settings.config['Celery'])
