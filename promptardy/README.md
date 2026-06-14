# Jiporady Render Edition

A beefed-up Flask version of the Jeopardy-style game, ready to deploy on Render.

## Features
- Round 1 and Double Jiporady boards
- Running score with negative score support
- Browser-persisted progress via localStorage
- Topic-specific game modules selected by environment variable
- Final Jiporady section
- `/health` endpoint for simple health checks

## Topic modules
Topic modules follow the `app_<topic>.py` filename pattern and are loaded by `app_loader.py`.

For the Honey Bees game added here:

```bash
JIPORADY_TOPIC=honey_bees python app_loader.py
```

On Windows PowerShell:

```powershell
$env:JIPORADY_TOPIC = "honey_bees"
python app_loader.py
```

You can also select the module explicitly:

```bash
JIPORADY_APP_MODULE=app_honey_bees python app_loader.py
```

Then open `http://127.0.0.1:5000`.

## Deploy on Render
1. Push these files to the repo.
2. Create a new Web Service in Render from the GitHub repo.
3. Render should detect `render.yaml`, or you can use:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app_loader:app`
   - Environment variable: `JIPORADY_TOPIC=honey_bees`
4. Deploy.

## Files
- `app_loader.py` - topic-aware Flask entrypoint
- `app_honey_bees.py` - Honey Bees question bank and Flask routes
- `app_*.py` - other topic-specific game modules
- `templates/index.html` - main UI
- `static/js/game.js` - gameplay logic and scorekeeping
- `static/css/styles.css` - styling
- `render.yaml` - Render blueprint
- `render-topic-example.yaml` - topic deployment example
- `Procfile` - fallback process declaration
