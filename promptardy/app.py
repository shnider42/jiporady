from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Jiporady",
    "subtitle": "A bigger, louder, score-tracking Jeopardy-style party board",
    "rounds": {
        "round_1": {
            "name": "Round 1",
            "categories": [
                {
                    "title": "Recoveries & Movement",
                    "clues": [
                        {"value": 100, "question": "This recovery mechanic uses a backflip cancel plus air roll to reverse direction much faster than turning around normally.", "answer": "What is a half-flip?"},
                        {"value": 200, "question": "This momentum-saving move is performed by jumping right as your wheels touch down, often after an aerial or wall play.", "answer": "What is a wavedash?"},
                        {"value": 300, "question": "This advanced kickoff and movement technique relies on a very fast diagonal flip cancel to reach the ball sooner.", "answer": "What is a speed flip?"},
                        {"value": 400, "question": "This wall movement technique chains rapid dash-like touches to gain speed along the side surface.", "answer": "What is a wall dash?"},
                        {"value": 500, "question": "Freestylers use this midair input technique to kill or interrupt rotation and set up cleaner follow-up touches or resets.", "answer": "What is a stall?"},
                    ],
                },
                {
                    "title": "Kickoffs, 50s & Defense",
                    "clues": [
                        {"value": 100, "question": "On kickoff, this term refers to the teammate who creeps forward behind the taker to capitalize on a favorable ball.", "answer": "What is cheating up?"},
                        {"value": 200, "question": "This defensive technique means mirroring the attacker between ball and net instead of diving in immediately.", "answer": "What is shadow defense?"},
                        {"value": 300, "question": "This kind of challenge intentionally keeps the ball close and deadens it rather than booming it away.", "answer": "What is a low 50?"},
                        {"value": 400, "question": "This pressure move means pretending to challenge in order to force a rushed touch without fully committing.", "answer": "What is a fake challenge?"},
                        {"value": 500, "question": "Veteran defenders usually rotate through this side of the net because it preserves better angles and coverage.", "answer": "What is the back post?"},
                    ],
                },
                {
                    "title": "Boost Math & Physics",
                    "clues": [
                        {"value": 100, "question": "A single small boost pad gives exactly this amount of boost.", "answer": "What is 12?"},
                        {"value": 200, "question": "A full large boost pad gives this amount.", "answer": "What is 100?"},
                        {"value": 300, "question": "After your first jump, your second jump or dodge remains available for about this long before expiring.", "answer": "What is 1.5 seconds?"},
                        {"value": 400, "question": "This name/term for a layout that are deemed 'identical in size, shape, and boost placement to ensure competitive fairness'", "answer": "What is standard?"},
                        {"value": 500, "question": "This number was the boost amount shown at the bottom right when spawning when the game first released", "answer": "What is 33?"},
                    ],
                },
                {
                    "title": "Freestyle Lexicon",
                    "clues": [
                        {"value": 100, "question": "This shot starts from the ceiling so the player can fall off with a saved dodge and fire later.", "answer": "What is a ceiling shot?"},
                        {"value": 200, "question": "This mechanic restores a dodge by getting all four wheels onto the ball midair.", "answer": "What is a flip reset?"},
                        {"value": 300, "question": "Named after a player, this flick uses a backflip-cancel-style motion from a dribble to launch the ball upward and forward.", "answer": "What is a musty flick?"},
                        {"value": 400, "question": "This notoriously flashy shot redirects the ball from behind or near the opponent's backboard area back into the front of the net.", "answer": "What is a psycho?"},
                        {"value": 500, "question": "This advanced flick, named after a freestyler, uses a dramatic air-roll-heavy wrap around the ball before release.", "answer": "What is a breezi flick?"},
                    ],
                },
                {
                    "title": "RLCS Deep Cuts",
                    "clues": [
                        {"value": 100, "question": "RLCS stands for this.", "answer": "What is Rocket League Championship Series?"},
                        {"value": 200, "question": "Before the current open-circuit style, RLCS primarily used this older seasonal structure.", "answer": "What is league play?"},
                        {"value": 300, "question": "When Northern Gaming won the Season 3 World Championship, this legendary substitute played in place of Maestro.", "answer": "Who is Turbopolsa?"},
                        {"value": 400, "question": "This original world champion team won RLCS Season 1.", "answer": "What is iBUYPOWER Cosmic?"},
                        {"value": 500, "question": "Rocket League's PS3 predecessor had this famously long full title.", "answer": "What is Supersonic Acrobatic Rocket-Powered Battle-Cars?"},
                    ],
                },
                {
                    "title": "High-Level Game Sense",
                    "clues": [
                        {"value": 100, "question": "In 3v3, this player is the safety valve and usually cannot afford the riskiest challenge.", "answer": "Who is the third man?"},
                        {"value": 200, "question": "Repeatedly stealing the opponent's corner and midfield pads to limit their options is called this.", "answer": "What is boost starving?"},
                        {"value": 300, "question": "A pass played across the middle of the field toward a teammate instead of dumped into the corner is called this.", "answer": "What is an infield pass?"},
                        {"value": 400, "question": "When two or more teammates commit to the same ball and expose the net, veterans call it this.", "answer": "What is an overcommit?"},
                        {"value": 500, "question": "In 2s especially, taking a touch mainly to make the defender jump early so your teammate gets the next ball is called this.", "answer": "What is forcing a challenge?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady",
            "categories": [
                {
                    "title": "Arena Archaeology",
                    "clues": [
                        {"value": 200, "question": "This throwback arena recreates the recessed side-wall goal style of Rocket League's predecessor.", "answer": "What is Throwback Stadium?"},
                        {"value": 400, "question": "This oddball arena is best known for the giant pillars sitting on the field.", "answer": "What is Pillars?"},
                        {"value": 600, "question": "This Rocket Labs arena featured an opening in the floor beneath the field, making reads and recoveries especially cursed.", "answer": "What is Underpass?"},
                        {"value": 800, "question": "Before standardization, this desert-themed arena had a famously non-standard shape and weird bounces.", "answer": "What is Wasteland?"},
                        {"value": 1000, "question": "Before it was rebuilt to standard dimensions, this futuristic arena had elevated side platforms and a far stranger layout.", "answer": "What is Neo Tokyo?"},
                    ],
                },
                {
                    "title": "Esports Lore",
                    "clues": [
                        {"value": 200, "question": "This caster delivered the immortal call, 'THIS IS ROCKET LEAGUE!' after jstn's zero-second equalizer.", "answer": "Who is Shogun?"},
                        {"value": 400, "question": "Before becoming the Dignitas dynasty, the Kaydop-Turbo-ViolentPanda roster played under this org name.", "answer": "What is Gale Force eSports?"},
                        {"value": 600, "question": "This player substituted for Northern Gaming at the Season 3 World Championship and won the title.", "answer": "Who is Turbopolsa?"},
                        {"value": 800, "question": "This org won RLCS Season 1 with the roster of Kronovi, Lachinio, and 0ver Zer0.", "answer": "What is iBUYPOWER Cosmic?"},
                        {"value": 1000, "question": "After their breakout run as Team Queso, Rise, Joyo, and Vatira were signed by this org.", "answer": "What is Moist Esports?"},
                    ],
                },
                {
                    "title": "Named Mechanics",
                    "clues": [
                        {"value": 200, "question": "This flick, named after a content creator and pro, uses a backflip-style pop from a dribble.", "answer": "What is a musty flick?"},
                        {"value": 400, "question": "This mechanic, named after a freestyler, involves a dramatic air-roll-heavy wrap before releasing the ball.", "answer": "What is a breezi flick?"},
                        {"value": 600, "question": "This pinch, named after an early pro, is usually generated off the wall or wall-floor seam for absurd speed.", "answer": "What is a Kuxir pinch?"},
                        {"value": 800, "question": "This ultra-fast landing acceleration trick usually starts by touching down with one wheel before dashing forward.", "answer": "What is a zap dash?"},
                        {"value": 1000, "question": "This recovery mechanic chains repeated dash-like bursts along a vertical surface to maintain or gain speed.", "answer": "What is a wall dash?"},
                    ],
                },
                {
                    "title": "Hitboxes & Car Meta",
                    "clues": [
                        {"value": 200, "question": "Despite its different look, the Fennec shares this hitbox class with the Octane.", "answer": "What is the Octane hitbox?"},
                        {"value": 400, "question": "The 2016 Batmobile is most closely associated with this long, flat hitbox class.", "answer": "What is the Plank hitbox?"},
                        {"value": 600, "question": "This hitbox class is shared by the Dominus, Dominus GT, and several muscle-car-style bodies.", "answer": "What is the Dominus hitbox?"},
                        {"value": 800, "question": "This standardized hitbox class is the tallest of the group and is named after the body most associated with it.", "answer": "What is the Merc hitbox?"},
                        {"value": 1000, "question": "Many pros swapped to this car body because it felt visually cleaner than the Octane while keeping the same hitbox.", "answer": "What is the Fennec?"},
                    ],
                },
                {
                    "title": "Dead Modes & Ranked Relics",
                    "clues": [
                        {"value": 200, "question": "This retired ranked playlist was 3v3, but every player had to queue alone.", "answer": "What is Solo Standard?"},
                        {"value": 400, "question": "This experimental playlist name was used for unusual arenas before some ideas were standardized or retired.", "answer": "What is Rocket Labs?"},
                        {"value": 600, "question": "This extra mode swaps the ball for a puck and rewards wall reads and awkward pinches.", "answer": "What is Snow Day?"},
                        {"value": 800, "question": "This extra mode gives players randomized power-ups like plunger, spikes, and boxing glove.", "answer": "What is Rumble?"},
                        {"value": 1000, "question": "This predecessor title, often shortened to an acronym by veterans, came before Rocket League on PlayStation 3.", "answer": "What is Supersonic Acrobatic Rocket-Powered Battle-Cars?"},
                    ],
                },
                {
                    "title": "SSL Brain",
                    "clues": [
                        {"value": 200, "question": "This form of defense means staying goal side, matching the attacker's path, and delaying rather than diving.", "answer": "What is shadow defense?"},
                        {"value": 400, "question": "This pressure concept means moving up behind a kickoff teammate, expecting a favorable 50.", "answer": "What is cheating up?"},
                        {"value": 600, "question": "This type of challenge is thrown without full commitment mainly to force a rushed touch or flick.", "answer": "What is a fake challenge?"},
                        {"value": 800, "question": "High-level rotations usually route through this side of the goal because it preserves better coverage and angles.", "answer": "What is the back post?"},
                        {"value": 1000, "question": "This suffocating pressure style revolves around stealing the opponent's corner and midfield pads so they cannot fully reset.", "answer": "What is boost starving?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: Pop Culture + Tech",
        "question": "This 1999 sci-fi film shares its title with a mathematical structure used in computer science and linear algebra; the movie's title was borrowed from a William Gibson term.",
        "answer": "What is 'The Matrix'?"
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