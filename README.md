# crawler


## worker

    pipenv run celery -A crawler_sam.worker worker --loglevel=info


## producer

    pipenv run python crawler_sam/producer.py
