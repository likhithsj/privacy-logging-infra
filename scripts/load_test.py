import requests
import json

headers = {"Authorization": "Bearer securetoken123"}
payload = {"message": "File accessed", "user_id": "101"}

for i in range(10):
    response = requests.post("http://localhost:8000/log", headers=headers, json=payload)
    print(response.json())
