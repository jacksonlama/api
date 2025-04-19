from fastapi import APIRouter
from app.services.open_fpo_scraper import scrape_open_fpo
from app.utils.file_handler import load_data, data_exists

router = APIRouter()

@router.get("/open-fpo")
def get_open_fpo():
    if not data_exists("open_fpo"):
        scrape_open_fpo()
    return load_data("open_fpo")
