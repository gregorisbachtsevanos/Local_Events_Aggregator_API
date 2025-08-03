from fastapi import FastAPI, Query
from typing import List, Optional
from aggregator import get_all_events
from models import Event
from datetime import datetime

app = FastAPI(title="Local Events Aggregator API")

@app.get("/events", response_model=List[Event])
def list_events(
    category: Optional[str] = None,
    after: Optional[datetime] = None,
    before: Optional[datetime] = None
):
    events = get_all_events()

    if category:
        events = [e for e in events if e.category and e.category.lower() == category.lower()]
    if after:
        events = [e for e in events if e.start_time >= after]
    if before:
        events = [e for e in events if e.start_time <= before]

    return events
