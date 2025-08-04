# Local Events Aggregator API

A FastAPI-powered backend service that aggregates local events from real-world sources like Eventbrite and PredictHQ. Designed for location-based queries, date filtering, and easy extension — no UI required.

---

## Features

-  Search for events by location (lat/lon) and radius
-  Filter events by start/end time
-  Integrated with real event sources:
  - [Eventbrite API](https://www.eventbrite.com/developer/v3/)
  - [PredictHQ API](https://developer.predicthq.com/)
-  Geolocation-aware queries
-  FastAPI backend, easily extendable and lightweight

---

##  Project Structure

local_events_api/
│
├── main.py # FastAPI app
├── models.py # Pydantic models
├── aggregator.py # Core event combiner
├── sources/
│ ├── eventbrite_source.py # Eventbrite adapter
│ └── predicthq_source.py # PredictHQ adapter


---

## Requirements

- Python 3.9+
- [FastAPI](https://fastapi.tiangolo.com/)
- `uvicorn`, `requests`, `pydantic`
- Valid API keys for:
  - [Eventbrite](https://www.eventbrite.com/platform/api-keys)
  - [PredictHQ](https://www.predicthq.com/)

---

## Setup

1. **Clone the repo**
```
git clone https://github.com/your-username/local-events-api.git
cd local-events-api
```

2. Install dependencies
```
pip install -r requirements.txt
```

4. Set your API keys
```
export EVENTBRITE_API_KEY="your_eventbrite_token"
export PREDICTHQ_TOKEN="your_predicthq_token"
```

4.Run the app
```
uvicorn main:app --reload
```

 API Usage
GET /events
Search for events based on location, radius, and optional filters.

Query Parameters:
Name	Type	Required	Description
lat	float	✅	Latitude of the search location
lon	float	✅	Longitude of the search location
radius_km	float	❌	Search radius in kilometers (default: 10)
start	string	❌	ISO date string (e.g., 2025-08-01T00:00:00Z)
end	string	❌	ISO date string
phq_category	list of strings	❌	PredictHQ categories to filter by

*example*
```
GET /events?lat=40.64&lon=22.94&radius_km=15&start=2025-08-01T00:00:00Z&end=2025-08-07T23:59:59Z
```

*response*
```
[
  {
    "id": "123456",
    "title": "Live Music Festival",
    "description": "A night of local bands and food trucks.",
    "start_time": "2025-08-03T18:00:00Z",
    "end_time": "2025-08-03T23:00:00Z",
    "location": {
      "address": "Central Park",
      "latitude": 40.645,
      "longitude": 22.945
    },
    "category": "music",
    "source": "eventbrite"
  },
  ...
]
```

 🙋 FAQ
```
Q: Why doesn't it show events in my area?
  Some APIs (like Eventbrite) may limit results by popularity or time. Try expanding the date range or location radius.
Q: Do I need to pay for PredictHQ?
  They offer a free developer tier that works well for prototyping.
Q: Is this production-ready?
  It’s a great base, but would benefit from rate-limiting, retries, error handling, and persistence before production use.
```


<!--
-Rate limiting & caching: store recent responses to reduce API calls.
-Deduplication: avoid overlapping events between sources.
-More filters: text search, free vs paid, category tags.
-Exposing metadata: let users retrieve full details or venue info.
- Add support for more APIs (Meetup)
-->
