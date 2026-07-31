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

Available topic modules include:

- `brazil_soccer` -> `app_brazil_soccer.py`
- `nfl_since_2000` -> `app_nfl_since_2000.py`
- `nba` -> `app_nba.py`
- `metal` -> `app_metal.py`
- `music_theory` -> `app_music_theory.py`
- `boston_sports` -> `app_boston_sports.py`
- `nfl` -> `app_nfl.py`
- `honey_bees` -> `app_honey_bees.py`
- `history` -> `app_history.py`
- `cheesy_movies` -> `app_cheesy_movies.py`

For the cheesy movies game:

```bash
JIPORADY_TOPIC=cheesy_movies python app_loader.py
```

On Windows PowerShell:

```powershell
$env:JIPORADY_TOPIC = "cheesy_movies"
python app_loader.py
```

You can also select the module explicitly:

```bash
JIPORADY_APP_MODULE=app_cheesy_movies python app_loader.py
```

Or run the module directly:

```bash
python app_cheesy_movies.py
```

Then open `http://127.0.0.1:5000`.

If port 5000 is already busy, set a different port first:

```powershell
$env:PORT = "5007"
$env:JIPORADY_TOPIC = "cheesy_movies"
python app_loader.py
```

## Deploy on Render

The branch includes `render-cheesy-movies.yaml`, a dedicated Render Blueprint.

Manual Render settings:

- Branch: `agent/cheesy-movies-1977-1994`
- Root Directory: `promptardy`
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app_loader:app`
- Health Check Path: `/health`
- Environment variable: `JIPORADY_TOPIC=cheesy_movies`
- Environment variable: `PYTHON_VERSION=3.11.9`
- Environment variable: `SECRET_KEY=<generate a random secret>`

## Files
- `app_loader.py` - topic-aware Flask entrypoint
- `app_cheesy_movies.py` - cheesy action, sports, sci-fi, and cult movie game covering 1977-1994
- `app_brazil_soccer.py` - Brazilian international soccer question bank and Flask routes
- `app_nfl_since_2000.py` - NFL since 2000 question bank and Flask routes
- `app_nba.py` - NBA question bank and Flask routes
- `app_metal.py` - Metal question bank and Flask routes
- `app_music_theory.py` - Music theory question bank and Flask routes
- `app_boston_sports.py` - Boston pro sports question bank and Flask routes
- `app_nfl.py` - NFL question bank and Flask routes
- `app_honey_bees.py` - Honey Bees question bank and Flask routes
- `app_history.py` - History question bank with an American Civil War Double Jiporady round
- `app_*.py` - other topic-specific game modules
- `templates/index.html` - main UI
- `static/js/game.js` - gameplay logic and scorekeeping
- `static/css/styles.css` - styling
- `render.yaml` - default Render blueprint
- `render-cheesy-movies.yaml` - dedicated cheesy movies Render blueprint
- `Procfile` - fallback process declaration
