from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Ricket Log Jiporady",
    "subtitle": "What is.....I miss trading?",
    "rounds": {
        "round_1": {
            "name": "Round 1",
            "categories": [
                {
                    "title": "Arena Archaeology",
                    "clues": [
                        {"value": 100, "question": "This throwback arena recreates the recessed side-wall goal style of Rocket League's predecessor.", "answer": "What is Throwback Stadium?"},
                        {"value": 200, "question": "This oddball arena is best known for the giant pillars sitting on the field.", "answer": "What is Pillars?"},
                        {"value": 300, "question": "This Rocket Labs arena featured an opening in the floor beneath the field, making reads and recoveries especially cursed.", "answer": "What is Underpass?"},
                        {"value": 400, "question": "Before standardization, this desert-themed arena had a famously non-standard shape and weird bounces.", "answer": "What is Wasteland?"},
                        {"value": 500, "question": "Before it was rebuilt to standard dimensions, this futuristic arena had elevated side platforms and a far stranger layout.", "answer": "What is Neo Tokyo?"},
                    ],
                },
                {
                    "title": "Esports Lore",
                    "clues": [
                        {"value": 100, "question": "This caster delivered the immortal call, 'THIS IS ROCKET LEAGUE!' after jstn's zero-second equalizer.", "answer": "Who is Shogun?"},
                        {"value": 200, "question": "Before becoming the Dignitas dynasty, the Kaydop-Turbo-ViolentPanda roster played under this org name.", "answer": "What is Gale Force eSports?"},
                        {"value": 300, "question": "This player substituted for Northern Gaming at the Season 3 World Championship and won the title.", "answer": "Who is Turbopolsa?"},
                        {"value": 400, "question": "This org won RLCS Season 1 with the roster of Kronovi, Lachinio, and 0ver Zer0.", "answer": "What is iBUYPOWER Cosmic?"},
                        {"value": 500, "question": "After their breakout run as Team Queso, Rise, Joyo, and Vatira were signed by this org.", "answer": "What is Moist Esports?"},
                    ],
                },
                {
                    "title": "Named Mechanics",
                    "clues": [
                        {"value": 100, "question": "This flick, named after a content creator and pro, uses a backflip-style pop from a dribble.", "answer": "What is a musty flick?"},
                        {"value": 200, "question": "This mechanic, named after a freestyler, involves a dramatic air-roll-heavy wrap before releasing the ball.", "answer": "What is a breezi flick?"},
                        {"value": 300, "question": "This pinch, named after an early pro, is usually generated off the wall or wall-floor seam for absurd speed.", "answer": "What is a Kuxir pinch?"},
                        {"value": 400, "question": "This ultra-fast landing acceleration trick usually starts by touching down with one wheel before dashing forward.", "answer": "What is a zap dash?"},
                        {"value": 500, "question": "This recovery mechanic chains repeated dash-like bursts along a vertical surface to maintain or gain speed.", "answer": "What is a wall dash?"},
                    ],
                },
                {
                    "title": "F9 Rumble (in spirit)",
                    "clues": [
                        {"value": 100, "question": "Despite his thorny exterior, he's actually a softie on the inside, and kind of a good dude. Don't chirp him though", "answer": "Who is Data?"},
                        {"value": 200, "question": "This person made the F9 logo", "answer": "Who is Jeter?"},
                        {"value": 300, "question": "This phrase is uttered by shnider often enough he has been scolded for it", "answer": "What is 'I'm sorry'?  ('For a brick, he flew pretty good', also counts)"},
                        {"value": 400, "question": "This person is most often hanging around the f9 chat", "answer": "Whoever you think it is ;)"},
                        {"value": 500, "question": "This F9 member was the first (and so far only) champion of an F9 hosted tournament", "answer": "Who is Zetch?"},
                    ],
                },
                {
                    "title": "Dead Modes & Ranked Relics",
                    "clues": [
                        {"value": 100, "question": "This retired ranked playlist was 3v3, but every player had to queue alone.", "answer": "What is Solo Standard?"},
                        {"value": 200, "question": "This experimental playlist name was used for unusual arenas before some ideas were standardized or retired.", "answer": "What is Rocket Labs?"},
                        {"value": 300, "question": "This extra mode swaps the ball for a puck and rewards wall reads and awkward pinches.", "answer": "What is Snow Day?"},
                        {"value": 400, "question": "This extra mode gives players randomized power-ups like plunger, spikes, and boxing glove.", "answer": "What is Rumble?"},
                        {"value": 500, "question": "This predecessor title, often shortened to an acronym by veterans, came before Rocket League on PlayStation 3.", "answer": "What is Supersonic Acrobatic Rocket-Powered Battle-Cars?"},
                    ],
                },
                {
                    "title": "SSL Brain",
                    "clues": [
                        {"value": 100, "question": "This form of defense means staying goal side, matching the attacker's path, and delaying rather than diving.", "answer": "What is shadow defense?"},
                        {"value": 200, "question": "This pressure concept means moving up behind a kickoff teammate, expecting a favorable 50.", "answer": "What is cheating up?"},
                        {"value": 300, "question": "This type of challenge is thrown without full commitment mainly to force a rushed touch or flick.", "answer": "What is a fake challenge?"},
                        {"value": 400, "question": "High-level rotations usually route through this side of the goal because it preserves better coverage and angles.", "answer": "What is the back post?"},
                        {"value": 500, "question": "This suffocating pressure style revolves around stealing the opponent's corner and midfield pads so they cannot fully reset.", "answer": "What is boost starving?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady",
            "categories": [
                {
                    "title": "Patch History & Platform Shifts",
                    "clues": [
                        {"value": 200, "question": "Rocket League officially went free-to-play in this year.", "answer": "What is 2020?"},
                        {"value": 400, "question": "Before it was delisted for new buyers on PC, Rocket League was mainly sold on this storefront.", "answer": "What is Steam?"},
                        {"value": 600, "question": "In 2019, Psyonix was acquired by this company.", "answer": "What is Epic Games?"},
                        {"value": 800, "question": "Randomized paid crates were replaced by this item-reveal system.", "answer": "What are Blueprints?"},
                        {"value": 1000, "question": "This player-to-player feature was removed from Rocket League in late 2023.", "answer": "What is trading?"},
                    ],
                },
                {
                    "title": "Numbers Only Sickos Know",
                    "clues": [
                        {"value": 200, "question": "A single small boost pad gives exactly this amount of boost.", "answer": "What is 12?"},
                        {"value": 400, "question": "After the first jump, your dodge remains available for about this many seconds before it expires.", "answer": "What is 1.5 seconds?"},
                        {"value": 600, "question": "After a demolition, a player respawns after this many seconds.", "answer": "What is 3 seconds?"},
                        {"value": 800, "question": "A Rocket League car's maximum speed is roughly this many Unreal units per second.", "answer": "What is 2300 uu/s?"},
                        {"value": 1000, "question": "This number, at the game's release, was the amount of boost shown on the bottom right when you first spawn", "answer": "What is 33?"},
                    ],
                },
                {
                    "title": "Training, Workshop & Tools",
                    "clues": [
                        {"value": 200, "question": "This built-in mode lets players share codes for custom shot sequences.", "answer": "What is Custom Training?"},
                        {"value": 400, "question": "This community-made PC mod is famous for adding advanced free play and training features.", "answer": "What is BakkesMod?"},
                        {"value": 600, "question": "On PC, many custom rings and dribble maps became popular through this platform feature.", "answer": "What is the Steam Workshop?"},
                        {"value": 800, "question": "These custom maps are especially associated with aerial pathing through floating checkpoints.", "answer": "What are rings maps?"},
                        {"value": 1000, "question": "This custom map series is built around controlled ground possession through obstacle courses.", "answer": "What is Dribble Challenge?"},
                    ],
                },
                {
                    "title": "Inventory, Items & Cosmetics",
                    "clues": [
                        {"value": 200, "question": "Before Credits became the main premium currency, players used these to open crates.", "answer": "What are Keys?"},
                        {"value": 400, "question": "Item labels like Striker, Scorer, and Sweeper belong to this stat-tracking system.", "answer": "What are Certifications?"},
                        {"value": 600, "question": "Titanium White, Black, and Crimson are examples of this type of item variant.", "answer": "What are painted items?"},
                        {"value": 800, "question": "Items in the esports shop are purchased with this special currency.", "answer": "What are Esports Tokens?"},
                        {"value": 1000, "question": "This inventory system lets players exchange multiple lower-rarity items for one higher-rarity item.", "answer": "What is the trade-in system?"},
                    ],
                },
                {
                    "title": "Competitive Systems & Rank History",
                    "clues": [
                        {"value": 200, "question": "This hidden number is the rating system most players refer to when talking about matchmaking progress.", "answer": "What is MMR?"},
                        {"value": 400, "question": "Before Supersonic Legend was introduced, this was Rocket League's highest rank.", "answer": "What is Grand Champion?"},
                        {"value": 600, "question": "This rank tier sits above Champion and below Supersonic Legend in the modern ladder.", "answer": "What is Grand Champion?"},
                        {"value": 800, "question": "In the RLCS open era, teams often have to survive these events before reaching a regional main event.", "answer": "What are open qualifiers?"},
                        {"value": 1000, "question": "This tournament format advances or eliminates teams after a set number of wins or losses, and is common in RLCS events.", "answer": "What is a Swiss stage?"},
                    ],
                },
                {
                    "title": "Shot Types & Offensive Concepts",
                    "clues": [
                        {"value": 200, "question": "A goal scored by playing the ball off the backboard and then hitting it again is called this.", "answer": "What is a double tap?"},
                        {"value": 400, "question": "This offensive read involves jumping before the pass or clear actually arrives.", "answer": "What is a prejump?"},
                        {"value": 600, "question": "This dribble move uses a sharp change of direction across the ball to beat a defender.", "answer": "What is a cut?"},
                        {"value": 800, "question": "This ground shot wraps around the outside of the ball from the side for a powerful finish.", "answer": "What is a hook shot?"},
                        {"value": 1000, "question": "This controlled first touch is taken mainly to keep possession rather than to boom the ball away.", "answer": "What is a catch?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: Rocket League Esports Lore",
        "question": "In one of RLCS's most famous moments, jstn.'s zero-second goal in the Season 5 World Championship forced overtime against this eventual world champion team.",
        "answer": "What is Dignitas?"
    },
}


def all_categories():
    categories = []
    for round_data in GAME_DATA["rounds"].values():
        for category in round_data["categories"]:
            categories.append(
                {
                    "category": category["title"],
                    "clues": category["clues"],
                }
            )
    return categories


def build_board(category_count=6):
    categories = all_categories()
    category_count = max(4, min(category_count, len(categories)))
    board = random.sample(categories, category_count)
    return board


def build_stats():
    categories = all_categories()
    total_categories = len(categories)
    total_clues = sum(len(category["clues"]) for category in categories)
    return {
        "total_categories": total_categories,
        "total_clues": total_clues,
    }


@app.route("/")
def index():
    category_count = request.args.get("categories", default=6, type=int) or 6
    initial_board = build_board(category_count)
    return render_template(
        "index.html",
        title=GAME_DATA["title"],
        subtitle=GAME_DATA["subtitle"],
        stats=build_stats(),
        category_count=category_count,
        initial_board=initial_board,
    )


@app.route("/api/board")
def api_board():
    category_count = request.args.get("categories", default=6, type=int) or 6
    return jsonify({"board": build_board(category_count)})


@app.route("/api/game")
def game_data():
    return jsonify(GAME_DATA)


@app.route("/health")
def health_check():
    return {"ok": True, "app": "jiporady"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)