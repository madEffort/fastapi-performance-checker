from datetime import datetime
from pydantic import BaseModel

class PerformanceEntry(BaseModel):
    category: str
    meta: str
    value: float
    time: datetime = None  # 자동으로 시간을 설정