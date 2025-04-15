def tag_event_with_purpose(event: dict, purpose: str) -> dict:
    event["purpose"] = purpose
    return event
