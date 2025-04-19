from fastapi import APIRouter
from app.services.open_dividend_scraper import scrape_open_dividend
from app.utils.file_handler import load_data, data_exists

router = APIRouter()

@router.get("/open-dividend")
def get_open_dividend():
    if not data_exists("open_dividend"):
        scrape_open_dividend()
    return load_data("open_dividend")
