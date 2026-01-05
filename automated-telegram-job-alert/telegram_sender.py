import requests
from config import BOT_TOKEN, CHAT_ID
from job_fetcher import fetch_jobs

print("Fetching jobs...")  # debug

message = fetch_jobs()
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

if not message:
    print("No jobs found in the last 24 hours ")
    # send this message to Telegram as well
    payload = {
        "chat_id": CHAT_ID,
        "text": "No jobs found in the last 24 hours ",
        "disable_web_page_preview": True
    }
    response = requests.post(url, data=payload)
    print(response.text)
else:
    print(f"Jobs found:\n{message[:500]}...")  # show first 500 chars for debug

    MAX_LENGTH = 4000  # Telegram message limit
    chunks = [message[i:i+MAX_LENGTH] for i in range(0, len(message), MAX_LENGTH)]

    for chunk in chunks:
        payload = {
            "chat_id": CHAT_ID,
            "text": chunk,
            "disable_web_page_preview": True
        }
        response = requests.post(url, data=payload)
        print(response.text)
