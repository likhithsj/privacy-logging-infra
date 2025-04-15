from app.services.logging_service import log_event

def test_log_event():
    result = log_event({"message": "Access granted", "user_id": "42"})
    assert result["status"] == "logged"
