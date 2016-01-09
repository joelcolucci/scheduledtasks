# Scheduled Tasks with Python's Celery

## Setting up a Python Virtual Environment
##### Step 1: In your project directory create a new virtual environment
```
virtualenv venv
```

##### Step 2: Activate the environment
```
source venv/bin/activate
```

## Installing Dependencies
##### Step 1: Install project dependencies via requirements.txt
```
pip install -r requirements.txt
```
__Alternate__:
Manually install project dependenceies:
```
pip install -U celery[redis]
```

[See documentation for working with Celery and a Redis broker ](http://docs.celeryproject.org/en/latest/getting-started/brokers/redis.html)

## Getting Started
##### Step 1: Start up redis
```
redis-server
```

##### Step 2: Start up Celery
```
celery -A scheduledtasks.tasks worker --loglevel=info
```
See `run_celery.sh`

##### Step 3: Start up Celery Beat
```
celery beat -A scheduledtasks.tasks
```
See `run_beat.sh`
