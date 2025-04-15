import base64
import json

def encrypt_data(data: dict) -> dict:
    encoded = base64.b64encode(json.dumps(data).encode("utf-8")).decode("utf-8")
    return {"data": encoded}
