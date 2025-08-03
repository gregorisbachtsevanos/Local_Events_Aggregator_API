from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Event(BaseModel):
    id: str
    title: str
    description: Optional[str]
    start_time: datetime
    end_time: Optional[datetime]
    location: Optional[str]
    category: Optional[str]
    source: str  # Which source this came from
