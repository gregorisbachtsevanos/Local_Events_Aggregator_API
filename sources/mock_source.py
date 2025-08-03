from models import Event
from datetime import datetime, timedelta
import uuid

def get_mock_events():
    now = datetime.utcnow()
    return [
        Event(
            id=str(uuid.uuid4()),
            title="Downtown Farmers Market",
            description="Local produce and goods.",
            start_time=now + timedelta(days=1),
            end_time=now + timedelta(days=1, hours=3),
            location="Main Street Plaza",
            category="Market",
            source="mock"
        ),
        Event(
            id=str(uuid.uuid4()),
            title="Live Jazz Concert",
            description="Enjoy an evening of jazz.",
            start_time=now + timedelta(days=2, hours=5),
            end_time=now + timedelta(days=2, hours=7),
            location="City Park Amphitheater",
            category="Music",
            source="mock"
        )
    ]
