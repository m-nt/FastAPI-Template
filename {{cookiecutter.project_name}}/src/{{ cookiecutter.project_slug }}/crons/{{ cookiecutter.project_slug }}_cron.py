import logging
import time
import schedule

from {{ cookiecutter.project_slug }}.settings import get_settings

logging.basicConfig(level=logging.INFO)
_settings = get_settings()

def cron_health():
    logging.info("{{ cookiecutter.project_slug }}:: cron liveness 200 OK")


schedule.every().second.do(cron_health)

while True:
    schedule.run_pending()
    time.sleep(_settings.CRON_INTERVAL)