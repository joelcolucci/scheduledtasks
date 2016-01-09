#!/bin/bash
celery beat -A scheduledtasks.tasks
