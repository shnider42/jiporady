from __future__ import annotations

from flask import Flask, jsonify, render_template, request

from question_bank import build_board, get_bank_stats

app = Flask(__name__)


def sanitize_category_count(raw_value: str | None) -> int:
    try:
        parsed = int(raw_value or 6)
    except (TypeError, ValueError):
        parsed = 6
    return max(4, min(parsed, 10))


@app.route("/")
def index():
    category_count = sanitize_category_count(request.args.get("categories"))
    initial_board = build_board(category_count)
    stats = get_bank_stats()
    return render_template(
        "index.html",
        initial_board=initial_board,
        category_count=category_count,
        stats=stats,
    )


@app.route("/api/board")
def api_board():
    category_count = sanitize_category_count(request.args.get("categories"))
    board = build_board(category_count)
    stats = get_bank_stats()
    return jsonify(
        {
            "board": board,
            "category_count": category_count,
            "stats": stats,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
