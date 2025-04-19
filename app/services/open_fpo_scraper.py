import requests
from datetime import datetime
from app.utils.file_handler import data_exists, save_data
from app.config import settings

API_NAME = "open_fpo"
URL = "https://www.nepalipaisa.com/api/GetFpos?pageNo=1&itemsPerPage=100&pagePerDisplay=1"

def scrape_open_fpo():
    if data_exists(API_NAME):
        return None

    try:
        response = requests.get(URL)
        response.raise_for_status()
        json_data = response.json()
        
        fpo_data = []
        
        for fpo in json_data.get("result", {}).get("data", []):
            data = {
                "fpoId": fpo.get("fpoId"),
                "companyName": fpo.get("companyName"),
                "stockSymbol": fpo.get("stockSymbol"),
                "shareRegistrar": fpo.get("shareRegistrar"),
                "sectorName": fpo.get("sectorName"),
                "fileName": fpo.get("fileName"),
                "shareType": fpo.get("shareType"),
                "pricePerUnit": fpo.get("pricePerUnit"),
                "rating": fpo.get("rating"),
                "units": fpo.get("units"),
                "minUnits": fpo.get("minUnits"),
                "maxUnits": fpo.get("maxUnits"),
                "localUnits": fpo.get("localUnits"),
                "generalUnits": fpo.get("generalUnits"),
                "promoterUnits": fpo.get("promoterUnits"),
                "mutualFundUnits": fpo.get("mutualFundUnits"),
                "otherUnits": fpo.get("otherUnits"),
                "totalAmount": fpo.get("totalAmount"),
                "openingDateAD": fpo.get("openingDateAD"),
                "openingDateBS": fpo.get("openingDateBS"),
                "closingDateAD": fpo.get("closingDateAD"),
                "closingDateBS": fpo.get("closingDateBS"),
                "closingDateClosingTime": fpo.get("closingDateClosingTime"),
                "extendedDateAD": fpo.get("extendedDateAD"),
                "extendedDateBS": fpo.get("extendedDateBS"),
                "extendedDateClosingTime": fpo.get("extendedDateClosingTime"),
                "status": fpo.get("status"),
                "fiscalYearAD": fpo.get("fiscalYearAD"),
                "fiscalYearBS": fpo.get("fiscalYearBS"),
                "cultureCode": fpo.get("cultureCode")
            }
            fpo_data.append(data)
        
        data_to_save = {
            "scraped_at": datetime.now().isoformat(),
            "scraped_data": {
                "statusCode": json_data.get("statusCode"),
                "message": json_data.get("message"),
                "result": {
                    "data": fpo_data
                }
            }
        }

        save_data(API_NAME, data_to_save)
        return data_to_save
    except Exception as e:
        return {"error": str(e)}