from apscheduler.schedulers.background import BackgroundScheduler
from app.services.open_ipo_scraper import scrape_open_ipo
from app.services.open_fpo_scraper import scrape_open_fpo
from app.services.open_dividend_scraper import scrape_open_dividend
from app.services.open_right_scraper import scrape_open_right
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.main import app
import uvicorn

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scrape_open_ipo, 'cron', hour=settings.SCRAPE_HOUR, minute=settings.SCRAPE_MINUTE)
    scheduler.add_job(scrape_open_fpo, 'cron', hour=settings.SCRAPE_HOUR, minute=settings.SCRAPE_MINUTE)
    scheduler.add_job(scrape_open_dividend, 'cron', hour=settings.SCRAPE_HOUR, minute=settings.SCRAPE_MINUTE)
    scheduler.add_job(scrape_open_right, 'cron', hour=settings.SCRAPE_HOUR, minute=settings.SCRAPE_MINUTE)
    scheduler.start()

if __name__ == "__main__":
    if settings.DEBUG:
        start_scheduler()
    uvicorn.run(app, host="0.0.0.0", port=8000)
