from celery import Celery
from celery.schedules import crontab
from random import randrange
from time import sleep
from config import config
import requests


celery = Celery(__name__,
                backend=config['celery']['result_backend'],
                broker=config['celery']['broker_url'])

# celery.conf.beat_schedule = {
#     'generate_random': {
#         'task': 'celery_worker.generate_random',
#         'schedule': 1
#     },
# }

@celery.task
def generate_random():
    delay = randrange(5, 10)
    sleep(delay)
    requests.get('http://127.0.0.1:3030/notify')
    print('Delay {}'.format(delay))


# @celery.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(1, generate_random)
