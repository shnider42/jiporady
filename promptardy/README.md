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

For the Brazilian international soccer game:

```bash
JIPORADY_TOPIC=brazil_soccer python app_loader.py
```

On Windows PowerShell:

```powershell
$env:JIPORADY_TOPIC = "brazil_soccer"
python app_loader.py
```

You can also select the module explicitly:

```bash
JIPORADY_APP_MODULE=app_brazil_soccer python app_loader.py
```

Or run the module directly:

```bash
python app_brazil_soccer.py
```

Then open `http://127.0.0.1:5000`.

If port 5000 is already busy, set a different port first:

```powershell
$env:PORT = "5007"
$env:JIPORADY_TOPIC = "brazil_soccer"
python app_loader.py
```

## Deploy on Render
1. Push these files to the repo.
2. Create a new Web Service in Render from the GitHub repo.
3. Render should detect `render.yaml`, or you can use:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app_loader:app`
   - Environment variable: `JIPORADY_TOPIC=brazil_soccer`
4. Deploy.

## Files
- `app_loader.py` - topic-aware Flask entrypoint
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
- `render.yaml` - Render blueprint
- `render-topic-example.yaml` - topic deployment example
- `Procfile` - fallback process declaration

## General trivia with a little Spanish

`general_spanish` -> `app_general_spanish.py`: 60 new clues across 12 categories,
plus Final Jiporady. Eight Spanish clues are scattered across both rounds.
Their answer reveals include an English translation; accept answers in either
language. Round 1 is approachable, with a more challenging Double Jiporady.

- Round 1: Passport, Please; Snack Attack; Animal House; Movie Night;
  Everyday Science; Game Drawer.
- Double Jiporady: Map Without Labels; Who Made That?; Turn It Up;
  Time Machine; Between the Covers; Wait, Really?

Run locally from `promptardy`:

```bash
JIPORADY_TOPIC=general_spanish python app_loader.py
```

Render settings for this version:

- Branch: `feature/general-trivia-spanish` (until merged)
- Root directory: `promptardy`
- Build: `pip install -r requirements.txt`
- Start: `gunicorn app_loader:app`
- Health check: `/health`
- Set `JIPORADY_TOPIC=general_spanish`.
- Remove any old `JIPORADY_APP_MODULE` setting, or change it to
  `app_general_spanish`: that variable overrides `JIPORADY_TOPIC`.

When switching an existing deployment from another topic, click **New Game**
to clear the shared browser score and used-clue progress.
