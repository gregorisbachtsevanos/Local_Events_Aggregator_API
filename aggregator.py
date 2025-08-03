from sources import mock_source
from models import Event
from typing import List

def get_all_events() -> List[Event]:
    events = []
    events.extend(mock_source.get_mock_events())
    # more sources should added here in future
    return events
