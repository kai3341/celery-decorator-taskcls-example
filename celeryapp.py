from celery import Celery
import celery_decorator_taskcls

# celery_pool_asyncio importing is optional
# It imports when you run worker or beat if you define pool or scheduler
# but it does not imports when you open REPL or when you run web application.
# If you want to apply monkey patches anyway to make identical environment
# when you use REPL or run web application app it's good idea to import
# celery_pool_asyncio module
import celery_pool_asyncio  # noqa
# Sometimes noqa does not disable linter (Spyder IDE)
celery_pool_asyncio.__package__

import settings


celery_decorator_taskcls.patch_celery()

celeryapp = Celery()
celeryapp.config_from_object(settings.config['Celery'])
