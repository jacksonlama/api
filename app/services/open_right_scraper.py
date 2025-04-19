import requests
from datetime import datetime
from app.utils.file_handler import data_exists, save_data
from app.config import settings

API_NAME = "open_right"
URL = "https://www.nepalipaisa.com/api/GetDividendRights?pageNo=1&itemsPerPage=100&pagePerDisplay=1"

def scrape_open_right():
    if data_exists(API_NAME):
        return None

    try:
        response = requests.get(URL)
        response.raise_for_status()
        json_data = response.json()
        
        right_data = []
        
        for index, right in enumerate(json_data.get("result", {}).get("data", [])):
            if right.get("rightShare"):
                data = {
                    "sn": index + 1,
                    "companyName": right.get("companyName"),
                    "stockSymbol": right.get("stockSymbol"),
                    "rightShare": right.get("rightShare"),
                    "rightBookCloseDateAD": right.get("rightBookCloseDateAD"),
                    "rightBookCloseDateBS": right.get("rightBookCloseDateBS"),
                    "fiscalYearAD": right.get("fiscalYearAD"),
                    "fiscalYearBS": right.get("fiscalYearBS"),
                }
                right_data.append(data)
        
        data_to_save = {
            "scraped_at": datetime.now().isoformat(),
            "scraped_data": {
                "statusCode": "200",
                "message": "Success",
                "result": {
                    "data": right_data
                }
            }
        }

        save_data(API_NAME, data_to_save)
        return data_to_save
    except Exception as e:
        return {"error": str(e)}