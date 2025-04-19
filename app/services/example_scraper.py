from app.utils.file_handler import data_exists, save_data
from datetime import datetime

def scrape_example_site():
    # Only scrape if data does not exist
    if data_exists("example_api"):
        return None
    
    # TODO: Replace this with actual scraping logic
    data = {
        "scraped_at": datetime.now().isoformat(),
        "data": ["example", "info"]
    }
    
    save_data("example_api", data)
    return data
