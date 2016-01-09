#!/bin/bash
celery -A scheduledtasks.tasks worker --loglevel=info

# Combined: Not recommended for production
# celery -A tasks worker --loglevel=info --beat
