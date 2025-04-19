from fastapi import FastAPI
from app.routes import open_ipo_api, open_fpo_api, open_dividend_api, open_right_api

app = FastAPI(
    title="Daily Web Scraper API",
    version="1.0.0",
    description="Scrapes and stores data daily in JSON format."
)

app.include_router(open_ipo_api.router, prefix="/api", tags=["Open IPO"])
app.include_router(open_fpo_api.router, prefix="/api", tags=["Open FPO"])
app.include_router(open_dividend_api.router, prefix="/api", tags=["Open Dividend"])
app.include_router(open_right_api.router, prefix="/api", tags=["Open Right Share"])


