import os, requests
from models import Event
from datetime import datetime
from typing import List

EB_TOKEN = os.getenv("EVENTBRITE_API_KEY")
BASE = "https://www.eventbriteapi.com/v3/"
HEADERS = {"Authorization": f"Bearer {EB_TOKEN}"}

def search_events(lat: float, lon: float, within: str, start: str=None, end: str=None) -> List[Event]:
    params = {
        "location.latitude": lat,
        "location.longitude": lon,
        "location.within": within,
        "expand": "venue"
    }
    if start: params["start_date.range_start"] = start
    if end: params["start_date.range_end"] = end

    resp = requests.get(BASE + "events/search/", params=params, headers=HEADERS)
    resp.raise_for_status()
    data = resp.json().get("events", [])
    events = []
    for ev in data:
        venue = ev.get("venue", {})
        if not venue.get("latitude") or not venue.get("longitude"):
            continue
        events.append(Event(
            id=ev["id"],
            title=ev["name"]["text"],
            description=ev["description"]["text"] if ev.get("description") else None,
            start_time=datetime.fromisoformat(ev["start"]["utc"].replace("Z", "+00:00")),
            end_time=datetime.fromisoformat(ev["end"]["utc"].replace("Z", "+00:00")) if ev.get("end") else None,
            location={
                "address": venue.get("address", {}).get("localized_address_display"),
                "latitude": float(venue["latitude"]),
                "longitude": float(venue["longitude"])
            },
            category=None,
            source="eventbrite"
        ))
    return events
s
