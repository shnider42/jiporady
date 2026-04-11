"""Topic-aware entrypoint for Jiporady deployments.

Default behavior keeps the current app.py flow working.
Set either of these environment variables on Render to select a different app file:

- JIPORADY_APP_MODULE=app_cars
- JIPORADY_TOPIC=cars   -> loads app_cars.py

Example start command:
    gunicorn app_loader:app
"""

from __future__ import annotations

import importlib
import os
import re

DEFAULT_MODULE = "app"
MODULE_ENV_VAR = "JIPORADY_APP_MODULE"
TOPIC_ENV_VAR = "JIPORADY_TOPIC"


def _normalize_topic(value: str) -> str:
    normalized = re.sub(r"[^0-9a-zA-Z_]+", "_", value.strip()).strip("_").lower()
    return normalized


def _resolve_module_name() -> str:
    explicit_module = os.environ.get(MODULE_ENV_VAR, "").strip()
    if explicit_module:
        return explicit_module

    topic = _normalize_topic(os.environ.get(TOPIC_ENV_VAR, ""))
    if topic:
        return f"app_{topic}"

    return DEFAULT_MODULE


MODULE_NAME = _resolve_module_name()

try:
    loaded_module = importlib.import_module(MODULE_NAME)
except ModuleNotFoundError as exc:
    raise RuntimeError(
        f"Could not import module '{MODULE_NAME}'. "
        f"Set {MODULE_ENV_VAR}=app_<topic> or {TOPIC_ENV_VAR}=<topic>, "
        "and make sure the corresponding file exists."
    ) from exc

app = getattr(loaded_module, "app", None)
if app is None:
    raise RuntimeError(f"Module '{MODULE_NAME}' does not expose a Flask 'app' object.")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
