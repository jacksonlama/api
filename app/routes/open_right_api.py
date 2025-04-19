from fastapi import APIRouter
from app.services.open_right_scraper import scrape_open_right
from app.utils.file_handler import load_data, data_exists

router = APIRouter()

@router.get("/open-right")
def get_open_right():
    if not data_exists("open_right"):
        scrape_open_right()
    return load_data("open_right")
