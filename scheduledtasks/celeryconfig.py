# celeryconfig.py
"""Module containing Celery configuration variables.
"""


from celery.schedules import crontab

from config import REDIS_SERVER, REDIS_PORT, REDIS_DB


CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = 'US/Eastern'
BROKER_URL = 'redis://' + REDIS_SERVER + ':' + REDIS_PORT + '/' + REDIS_DB

CELERYBEAT_SCHEDULE = {
    'workdays-every-10-minutes': {
        'task': 'scheduledtasks.tasks.example',
        'schedule': crontab(hour='9-5', minute='*/1' , day_of_week='mon-sat'),
        'args': ()
    },
}
