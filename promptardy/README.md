# Jiporady Render Edition

A beefed-up Flask version of the Jeopardy-style game, ready to deploy on Render.

## Features
- Round 1 and Double Jiporady boards
- Running score with negative score support
- Browser-persisted progress via localStorage
- Pop culture, movies/TV, games, sports, history, science, tech, and wordplay categories
- Final Jiporady section
- `/health` endpoint for simple health checks

## Local run
```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000`.

## Deploy on Render
1. Push these files to the repo root.
2. Create a new Web Service in Render from the GitHub repo.
3. Render should detect `render.yaml`, or you can use:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
4. Deploy.

## Files
- `app.py` - Flask app and question bank
- `templates/index.html` - main UI
- `static/style.css` - styling
- `static/app.js` - gameplay logic and scorekeeping
- `render.yaml` - Render blueprint
- `Procfile` - fallback process declaration
