import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from app.api.endpoints.collect import router as collect_router
from app.api.endpoints.search import router as search_router


app = FastAPI(title="Performance Beacon")

app.include_router(collect_router, prefix="/collect", tags=["collect"])
app.include_router(search_router, prefix="/search", tags=["search"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)