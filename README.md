# Workout Tracker — Natural Language Exercise Logger

A Python automation that understands plain English exercise descriptions and automatically logs your workout data — calories, duration, exercise name — to a Google Sheet.

Just type "ran 5km and did 30 pushups" and it handles the rest.

## How It Works

1. You enter your exercise in plain English via terminal input
2. Nutritionix NLP API interprets the exercise, calculates calories burned and duration based on your personal stats (weight, height, age, gender)
3. Data is automatically logged to a Google Sheet via Sheety API with today's date and time

## Example

**Input:**
```
Tell me which exercises you did? ran 4km and did 20 pushups
```

**Logged to Google Sheet:**

| Date | Time | Exercise | Duration (min) | Calories |
|---|---|---|---|---|
| 30/05/2026 | 08:45:00 | Running | 24 | 214 |
| 30/05/2026 | 08:45:00 | Pushups | 5 | 30 |

## Features

- **Natural language input** — no dropdowns or forms, just type freely
- **Personal stats** — calories calculated based on your weight, height, age, gender
- **Auto date/time** — timestamp added automatically on every log
- **Google Sheets storage** — persistent, viewable, shareable workout history
- **Fully secure** — all API keys in environment variables

## Setup

### 1. Get API Keys

| Service | Where to get it |
|---|---|
| Nutritionix | [developer.nutritionix.com](https://developer.nutritionix.com) — free tier |
| Sheety | [sheety.co](https://sheety.co) — connects Google Sheets to API |

### 2. Set Up Google Sheet

Create a Google Sheet with these columns:
```
date | time | exercise | duration | calories
```
Connect it to Sheety and copy the endpoint URL.

### 3. Set Environment Variables

```bash
export X_APP_ID="your_nutritionix_app_id"
export X_APP_KEY="your_nutritionix_app_key"
export SHEETY_TOKEN="your_sheety_bearer_token"
export NUTRITION_ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"
export SHEETY_ENDPOINT="your_sheety_sheet_endpoint"
```

### 4. Update Personal Stats

Edit `main.py`:
```python
WEIGHT_KG = 58
HEIGHT_CM = 175
AGE = 18
GENDER = "male"
```

### 5. Run

```bash
pip install requests
python main.py
```

## Requirements

- Python 3.x
- requests (`pip install requests`)

## What I Learned

- Natural language processing via third-party API (Nutritionix NLP)
- POST requests with custom headers and JSON body
- Chaining multiple APIs in a single script
- Google Sheets as a database via Sheety
- Bearer token authentication
- datetime formatting for structured data logging
