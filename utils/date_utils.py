
from datetime import datetime, timezone

def get_current_utc_timestamp() -> datetime:
    return datetime.now(timezone.utc)

def parse_iso_format(date_str: str) -> datetime:
    try:
        return datetime.fromisoformat(date_str)
    except ValueError:
        return None
