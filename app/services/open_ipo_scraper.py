import requests
from datetime import datetime
from app.utils.file_handler import data_exists, save_data
from app.config import settings

API_NAME = "open_ipo"
URL = "https://www.nepalipaisa.com/api/GetIpos?pageNo=1&itemsPerPage=100&pagePerDisplay=1"

def scrape_open_ipo():
    if data_exists(API_NAME):
        return None

    try:
        response = requests.get(URL)
        response.raise_for_status()
        json_data = response.json()
        
        ipo_data = []
        
        for ipo in json_data.get("result", {}).get("data", []):
            data = {
                "ipoId": ipo.get("ipoId"),
                "companyName": ipo.get("companyName"),
                "stockSymbol": ipo.get("stockSymbol"),
                "shareRegistrar": ipo.get("shareRegistrar"),
                "sectorName": ipo.get("sectorName"),
                "fileName": ipo.get("fileName"),
                "shareType": ipo.get("shareType"),
                "pricePerUnit": ipo.get("pricePerUnit"),
                "rating": ipo.get("rating"),
                "units": ipo.get("units"),
                "minUnits": ipo.get("minUnits"),
                "maxUnits": ipo.get("maxUnits"),
                "localUnits": ipo.get("localUnits"),
                "generalUnits": ipo.get("generalUnits"),
                "promoterUnits": ipo.get("promoterUnits"),
                "mutualFundUnits": ipo.get("mutualFundUnits"),
                "otherUnits": ipo.get("otherUnits"),
                "totalAmount": ipo.get("totalAmount"),
                "openingDateAD": ipo.get("openingDateAD"),
                "openingDateBS": ipo.get("openingDateBS"),
                "closingDateAD": ipo.get("closingDateAD"),
                "closingDateBS": ipo.get("closingDateBS"),
                "closingDateClosingTime": ipo.get("closingDateClosingTime"),
                "extendedDateAD": ipo.get("extendedDateAD"),
                "extendedDateBS": ipo.get("extendedDateBS"),
                "extendedDateClosingTime": ipo.get("extendedDateClosingTime"),
                "status": ipo.get("status"),
                "fiscalYearAD": ipo.get("fiscalYearAD"),
                "fiscalYearBS": ipo.get("fiscalYearBS"),
                "cultureCode": ipo.get("cultureCode")
            }
            ipo_data.append(data)
        
        data_to_save = {
            "scraped_at": datetime.now().isoformat(),
            "scraped_data": {
                "statusCode": json_data.get("statusCode"),
                "message": json_data.get("message"),
                "result": {
                    "data": ipo_data
                }
            }
        }

        save_data(API_NAME, data_to_save)
        return data_to_save
    except Exception as e:
        return {"error": str(e)}