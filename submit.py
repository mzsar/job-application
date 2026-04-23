import requests
import json
import hmac
import hashlib
from datetime import datetime, timezone

payload ={
    "timestamp": datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z"),
    "name": "Marta Sanchez Martin",
    "email": "martasanchez2628@gmail.com",
    "resume_link": "https://www.linkedin.com/in/marta-sanchez-m/",
    "repository_link": "https://github.com/mzsar/job-application",
    "action_run_link": "https://github.com/mzsar/job-application/actions/runs/24856851626"
}

body = json.dumps(payload, separators=(",",":"), sort_keys=True).encode("utf-8")
signature = hmac.new(
    b"hello-there-from-b12",
    body,
    hashlib.sha256
).hexdigest()

print(body.decode("utf-8"))
print(signature)

response = requests.post(
    "https://b12.io/apply/submission",
    data=body,
    headers={
        "Content-Type": "application/json",
        "X-Signature-256": f"sha256={signature}",
    },
    timeout=30,
)

print(response.status_code)
print(response.text)