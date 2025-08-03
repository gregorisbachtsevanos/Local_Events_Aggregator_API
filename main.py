from fastapi import FastAPI, Query, HTTPException
from typing import List, Optional
from aggregator import get_all_events
from models import Event

app = FastAPI(title="Local Events Aggregator API")

@app.get("/events", response_model=List[Event])
def events(
    lat: float = Query(...),
    lon: float = Query(...),
    radius_km: float = Query(10.0),
    start: Optional[str] = None,
    end: Optional[str] = None,
    phq_category: Optional[List[str]] = Query(None)
):
    try:
        return get_all_events(lat, lon, radius_km, start, end, phq_category)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
