from fastapi import FastAPI, Header, HTTPException
from app.services.logging_service import log_event
from app.utils.auth import verify_token

app = FastAPI()

@app.post("/log")
def log_endpoint(event: dict, authorization: str = Header(None)):
    if not verify_token(authorization):
        raise HTTPException(status_code=403, detail="Unauthorized")
    return log_event(event)
