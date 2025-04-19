from fastapi import APIRouter
from app.services.open_ipo_scraper import scrape_open_ipo
from app.utils.file_handler import load_data, data_exists

router = APIRouter()

@router.get("/open-ipo")
def get_open_ipo():
    if not data_exists("open_ipo"):
        scrape_open_ipo()
    return load_data("open_ipo")
