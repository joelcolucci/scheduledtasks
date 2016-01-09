# tasks.py
"""Module containing Celery config and tasks.
"""


from celery import Celery


app = Celery('scheduledtasks.tasks')
app.config_from_object('scheduledtasks.celeryconfig')


@app.task
def example():
    with open('/Users/joelcolucci/Desktop/hello.txt', 'a') as f:
        f.write('hello, world')


if __name__ == '__main__':
    app.start()
