import requests
from datetime import datetime
from app.utils.file_handler import data_exists, save_data
from app.config import settings

API_NAME = "open_dividend"
URL = "https://www.nepalipaisa.com/api/GetDividendRights?pageNo=1&itemsPerPage=100&pagePerDisplay=1"

def scrape_open_dividend():
    if data_exists(API_NAME):
        return None

    try:
        response = requests.get(URL)
        response.raise_for_status()
        json_data = response.json()
        
        dividend_data = []
        
        for index, dividend in enumerate(json_data.get("result", {}).get("data", [])):
            if dividend.get("bonus") or dividend.get("cash") or dividend.get("totalDividend"):
                data = {
                    "sn": index + 1,
                    "companyName": dividend.get("companyName"),
                    "stockSymbol": dividend.get("stockSymbol"),
                    "bonusDividend": f"{dividend.get("bonus")}%",
                    "cashDividend": f"{dividend.get("cash")}%",
                    "totalDividend": f"{dividend.get("totalDividend")}%",
                    "dividendBookCloseDateAD": dividend.get("dividendBookCloseDateAD"),
                    "dividendBookCloseDateBS": dividend.get("dividendBookCloseDateBS"),
                    "fiscalYearAD": dividend.get("fiscalYearAD"),
                    "fiscalYearBS": dividend.get("fiscalYearBS"),
                }
                dividend_data.append(data)
        
        data_to_save = {
            "scraped_at": datetime.now().isoformat(),
            "scraped_data": {
                "statusCode": "200",
                "message": "Success",
                "result": {
                    "data": dividend_data
                }
            }
        }

        save_data(API_NAME, data_to_save)
        return data_to_save
    except Exception as e:
        return {"error": str(e)}