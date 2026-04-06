# Promptardy!

A Jeopardy-style trivia board built with Flask for easy local testing and quick deployment to Render.

## What's included
- Randomized board generator
- 30 categories
- 150 total clues
- Clickable clue tiles
- Modal-based question and answer reveal
- "New Board" button for fresh category sets
- "Reset Used Clues" button for repeat demos

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Then open `http://127.0.0.1:5000`

## Deploy to Render
### Option 1: Quick manual setup
1. Push this folder to GitHub.
2. In Render, create a new **Web Service**.
3. Point it at your repo.
4. Use:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

### Option 2: Blueprint
If you use the included `render.yaml`, Render can auto-detect the service settings.

## Edit the question bank
All categories and clues live in `question_bank.py`.

Each category follows this shape:
```python
{
    "category": "Science Basics",
    "clues": [
        {"value": 200, "question": "...", "answer": "What is ...?"},
        ...
    ],
}
```

## Presentation tip
For a live demo, set the board to 6 categories for a classic look, and click **New Board** between rounds to show that the site can keep generating fresh boards from the larger clue bank.
