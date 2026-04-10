import os
import random
import secrets
from flask import Flask, render_template, session, jsonify
from question_bank import get_master_bank

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", secrets.token_hex(32))

BOARD_CATEGORY_COUNT = 6
CLUE_VALUES = [200, 400, 600, 800, 1000]


def build_random_board():
    """
    Select 6 random categories.
    For each dollar value, randomly choose one clue from that category's pool.
    """
    bank = get_master_bank()
    all_categories = list(bank.keys())
    selected_categories = random.sample(all_categories, k=BOARD_CATEGORY_COUNT)

    board = []
    for category_name in selected_categories:
        category_data = bank[category_name]
        clues = []

        for value in CLUE_VALUES:
            pool = category_data[value]
            chosen = random.choice(pool)
            clues.append({
                "value": value,
                "question": chosen["question"],
                "answer": chosen["answer"],
            })

        board.append({
            "category": category_name,
            "clues": clues,
        })

    return board


def ensure_board():
    if "board_id" not in session or "board" not in session:
        session["board_id"] = secrets.token_hex(8)
        session["board"] = build_random_board()


@app.route("/")
def index():
    ensure_board()
    return render_template(
        "index.html",
        board=session["board"],
        board_id=session["board_id"]
    )


@app.route("/api/new-game", methods=["POST"])
def new_game():
    session["board_id"] = secrets.token_hex(8)
    session["board"] = build_random_board()
    return jsonify({
        "ok": True,
        "board_id": session["board_id"],
        "board": session["board"]
    })


if __name__ == "__main__":
    app.run(debug=True)