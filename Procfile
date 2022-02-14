web: gunicorn psql_jupyter.wsgi --chdir backend --limit-request-line 8188 --log-file -
worker: REMAP_SIGTERM=SIGQUIT celery --workdir backend --app=psql_jupyter worker --loglevel=info
beat: REMAP_SIGTERM=SIGQUIT celery --workdir backend --app=psql_jupyter beat -S redbeat.RedBeatScheduler --loglevel=info
