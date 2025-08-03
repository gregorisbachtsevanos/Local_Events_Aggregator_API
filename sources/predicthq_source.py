import os
import predictHQ
from models import Event
from datetime import datetime
from typing import List

phq = predictHQ.Client(access_token=os.getenv("PREDICTHQ_TOKEN"))

def search_events(lat: float, lon: float, within: float, categories: List[str]=None, start=None, end=None) -> List[Event]:
    resp = phq.events.search(
        within=f"{within}km@{lat},{lon}",
        category=categories,
        start=start,
        end=end
    )
    events = []
    for ev in resp:
        events.append(Event(
            id=ev.id,
            title=ev.title,
            description=ev.description,
            start_time=ev.start,
            end_time=ev.end,
            location={"latitude": ev.location[1], "longitude": ev.location[0]},
            category=ev.category,
            source="predicthq"
        ))
    return events
