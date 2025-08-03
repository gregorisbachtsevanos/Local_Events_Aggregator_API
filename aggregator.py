from sources.eventbrite_source import search_events as eb_search
from sources.predicthq_source import search_events as phq_search
from models import Event
from typing import List

def get_all_events(
    lat: float, lon: float, radius_km: float,
    start: str=None, end: str=None, phq_categories=None
) -> List[Event]:
    events = []
    events += eb_search(lat, lon, f"{radius_km}km", start, end)
    events += phq_search(lat, lon, radius_km, categories=phq_categories, start=start, end=end)
    return events
