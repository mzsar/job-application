import requests
import json
import hmac
import hashlib
from datetime import datetime

payload ={
    "timestamp": datetime.now().isoformat(timespec="milliseconds").replace("+00:00", "Z"),
    "name": "Marta Sanchez Martin",
    "email": "martasanchez2628@gmail.com",
    "resume_link": "https://www.linkedin.com/in/marta-sanchez-m/",
    # if you're watching this, here's my other repo -> https://github.com/MkS2244 
    # this one contains one of my personal projects :)
    "repository_link": "https://github.com/mzsar/job-application",
    "action_run_link": "https://github.com/mzsar/job-application/actions/runs/ID"
}

body = json.dumps(payload, separators=(",",":"), sort_keys=True).encode("utf-8")
signature = hmac.new(
    b"Hello-you-all",
    body,
    hashlib.sha256
).hexdigest()

response = requests.post(
    "https://b12.io/apply/submission",
    data=body,
    headers = {
        "X-Signature-256": f"sha256={signature}",
        "Content-Type": "application/json"
    }
)

response.raise_for_status()
print(response.json()["receipt"])