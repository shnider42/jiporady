import os
import random
import secrets

from flask import Flask, jsonify, render_template, request, session

from question_bank import (
    APP_SUBTITLE,
    APP_TITLE,
    CATEGORY_COUNT,
    FINAL_BANK,
    ROUND_DEFS,
)

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")


def build_stats():
    total_categories = sum(len(round_def["bank"]) for round_def in ROUND_DEFS.values())
    total_clue_variants = 0

    for round_def in ROUND_DEFS.values():
        for category_bank in round_def["bank"].values():
            for clue_options in category_bank.values():
                total_clue_variants += len(clue_options)

    return {
        "total_categories": total_categories,
        "total_clue_variants": total_clue_variants,
        "board_slots_per_game": CATEGORY_COUNT * sum(
            len(round_def["values"]) for round_def in ROUND_DEFS.values()
        ),
    }


def build_round(round_key, rng):
    round_def = ROUND_DEFS[round_key]
    category_titles = list(round_def["bank"].keys())
    selected_titles = rng.sample(
        category_titles,
        k=min(CATEGORY_COUNT, len(category_titles)),
    )

    categories = []
    for title in selected_titles:
        category_bank = round_def["bank"][title]
        clues = []

        for value in round_def["values"]:
            clue_choice = rng.choice(category_bank[value])
            clues.append(
                {
                    "value": value,
                    "question": clue_choice["question"],
                    "answer": clue_choice["answer"],
                }
            )

        categories.append(
            {
                "title": title,
                "clues": clues,
            }
        )

    return {
        "name": round_def["name"],
        "categories": categories,
    }


def build_game_data(seed, board_id):
    rng = random.Random(seed)

    rounds = {}
    for round_key in ROUND_DEFS:
        rounds[round_key] = build_round(round_key, rng)

    final_pick = rng.choice(FINAL_BANK)

    return {
        "board_id": board_id,
        "title": APP_TITLE,
        "subtitle": APP_SUBTITLE,
        "rounds": rounds,
        "final": final_pick,
    }


def reset_session_game():
    session["game_seed"] = secrets.token_hex(16)
    session["board_id"] = secrets.token_hex(8)


def ensure_session_game():
    if "game_seed" not in session or "board_id" not in session:
        reset_session_game()


@app.route("/")
def index():
    ensure_session_game()
    return render_template(
        "index.html",
        title=APP_TITLE,
        subtitle=APP_SUBTITLE,
        stats=build_stats(),
    )


@app.route("/api/game")
def api_game():
    ensure_session_game()
    return jsonify(build_game_data(session["game_seed"], session["board_id"]))


@app.route("/api/new-game", methods=["POST"])
def api_new_game():
    reset_session_game()
    return jsonify(build_game_data(session["game_seed"], session["board_id"]))


@app.route("/api/board")
def api_board():
    """
    Compatibility endpoint in case older scripts still call /api/board.
    Returns the categories for a specific round from the current session's board.
    """
    ensure_session_game()
    round_key = request.args.get("round", "round_1")

    if round_key not in ROUND_DEFS:
        round_key = "round_1"

    game_data = build_game_data(session["game_seed"], session["board_id"])
    return jsonify(
        {
            "board_id": game_data["board_id"],
            "round": round_key,
            "board": game_data["rounds"][round_key]["categories"],
        }
    )


@app.route("/health")
def health_check():
    return {"ok": True, "app": "jiporady"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)