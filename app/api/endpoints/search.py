from fastapi import APIRouter, HTTPException
from app.db.database import get_db

router = APIRouter()

@router.get("/")
async def search_performance_data(category: str, meta: str):
    db = get_db()
    results = db.collection.find({"category": category, "meta": meta})
    result_list = list(results)
    if not result_list:
        raise HTTPException(status_code=404, detail="No data found")
    return {"val": [x['value'] for x in result_list]}