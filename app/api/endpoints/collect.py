from fastapi import APIRouter
from app.schemas.performance import PerformanceEntry
from app.db.database import get_db
from datetime import datetime

router = APIRouter()

@router.post("/")
async def collect_performance_data(entry: PerformanceEntry):
    entry.time = datetime.now()  # 현재 시간 자동 추가
    db = get_db()
    db.collection.insert_one(entry.dict())
    return {"message": "Data collected successfully"}