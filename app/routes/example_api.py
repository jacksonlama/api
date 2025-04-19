from fastapi import APIRouter
from app.services.example_scraper import scrape_example_site
from app.utils.file_handler import load_data, data_exists

router = APIRouter()

@router.get("/example-api")
def get_example_data():
    if not data_exists("example_api"):
        scrape_example_site()
    return load_data("example_api")
