"""
Event log schema for content automation.
All pipeline steps must emit events here.
"""

from datetime import datetime
from typing import Dict, Any

def emit_event(event_type: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "event_type": event_type,
        "timestamp": datetime.utcnow().isoformat(),
        "payload": payload,
    }
