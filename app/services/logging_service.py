import json
from datetime import datetime
from app.utils.encryption import encrypt_data
from app.utils.governance import tag_event_with_purpose

def log_event(event: dict) -> dict:
    event["timestamp"] = datetime.utcnow().isoformat()
    event = tag_event_with_purpose(event, "security_audit")
    encrypted_event = encrypt_data(event)
    with open("logs.txt", "a") as f:
        f.write(json.dumps(encrypted_event) + "\n")
    return {"status": "logged", "event_id": event["timestamp"]}
