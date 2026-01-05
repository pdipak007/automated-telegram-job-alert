#  Automated Telegram Job Alert Bot (Cloud & DevOps Roles)

This Python-based Telegram bot automatically sends Cloud & DevOps job links to Telegram every day at 9:00 PM. It fetches only jobs posted in the last 24 hours, so even if your PC was off for 2–3 days, it will send only fresh links when it runs.

## Features
- Daily automated job alerts at 9 PM
- Sends only last 24 hours job links
- Works even if PC was off earlier
- Secure token handling (no secrets pushed to GitHub)
- Easy Windows Task Scheduler automation
- Beginner-friendly Python project

## Tech Stack:
- Python 3.10+ (Tested on Python 3.13)
- Telegram Bot API  
- Requests  
- BeautifulSoup  
- Windows Task Scheduler  

## Step 1: Create Telegram Bot:
1. Open Telegram
2. Search **@BotFather**
3. Type `/start`
4. Type `/newbot`
5. Give bot name & username
6. Copy **BOT TOKEN** (keep it secret)

## Step 2: Get Chat ID:
1. Send any message to your bot
2. Open browser and visit:
             https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates
3. Copy the number from:
            "chat":{"id":123456789}
            
## Project Structure:
```
automated-telegram-job-alert/
│
├── telegram_sender.py
├── job_fetcher.py
├── config_example.py
├── requirements.txt
└── README.md
```

## Step 3: Configuration (IMPORTANT):
- Create a file `config.py`  
- Copy content from `config_example.py` and add your details

```python
BOT_TOKEN = "ENTER_YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "ENTER_YOUR_CHAT_ID"

ROLES = [
    "Junior Cloud Engineer",
    "Cloud Engineer Trainee",
    "DevOps Intern",
    "Junior DevOps Engineer",
    "Cloud Support Engineer",
    "AWS Support Engineer",
    "SRE Intern"
]

SITES = ["linkedin", "naukri", "unstop", "wellfound"] 
```
## Step 4: Install Dependencies:
```pip install -r requirements.txt```

## Step 5: Test Manually:
```python telegram_sender.py```

## Step 6: Windows Task Scheduler Automation:
- This project can be automated using Windows Task Scheduler to run daily at 9:00 PM.

Steps:
1.Open Task Scheduler
2.Click Create Task
3.Go to Triggers
     - Set trigger to Daily
     - Time: 9:00 PM
4.Go to Actions
     - Action: Start a program

## Action Configuration (IMPORTANT):
- Program/script:
         Use the full path to your Python executable.

## Example:
```C:\Path\To\Your\Python\python.exe```

-You can find this path by running:
 ``` where python```

## Add arguments:
```telegram_sender.py```

## Start in:
```<Path to project folder>```

## Example:
```C:\Users\<your-username>\Desktop\telegram-job-alert```

## Recommended Settings:
- Enable the following options:
 1. Run whether user is logged on or not
 2. Run with highest privileges
 3. Run task as soon as possible after a scheduled start is missed
 4. Do not start a new instance

## Troubleshooting:
- If no jobs are found, bot will notify: "No jobs found in last 24 hours"
- If Telegram message fails, recheck BOT_TOKEN and CHAT_ID


Author

Dipak Purane
Cloud | DevOps | Automation

