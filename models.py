from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Event(BaseModel):
    id: str
    title: str
    description: Optional[str]
    start_time: datetime
    end_time: Optional[datetime]
    location: dict  # e.g. {"address": ... , "latitude": ..., "longitude": ...}
    category: Optional[str]
    source: str
