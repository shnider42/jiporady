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
                    "title": "Crates, Keys & Legacy",
                    "clues": [
                        {"value": 100, "question": "Before Credits existed, players used these to open crates.", "answer": "What are Keys?"},
                        {"value": 200, "question": "These free, untradeable crate-openers let players unlock crates without spending Keys.", "answer": "What are Decryptors?"},
                        {"value": 300, "question": "When crates were retired, unopened ones were converted into this reveal-first item system.", "answer": "What are Blueprints?"},
                        {"value": 400, "question": "Owners who had Rocket League before the free-to-play change received this status on select old items.", "answer": "What is Legacy?"},
                        {"value": 500, "question": "Introduced in 2018, this tier-based free and premium reward track became a seasonal staple.", "answer": "What is Rocket Pass?"},
                    ],
                },
                {
                    "title": "Numbers That Matter",
                    "clues": [
                        {"value": 100, "question": "A single small boost pad gives exactly this much boost.", "answer": "What is 12?"},
                        {"value": 200, "question": "A fully filled boost tank contains this much boost.", "answer": "What is 100?"},
                        {"value": 300, "question": "After the first jump, a player's dodge remains available for about this many seconds before expiring.", "answer": "What is 1.5 seconds?"},
                        {"value": 400, "question": "After a demolition, a player respawns after this many seconds.", "answer": "What is 3 seconds?"},
                        {"value": 500, "question": "The Rocket League ball is capped at roughly this top speed in Unreal units per second.", "answer": "What is 6000 uu/s?"},
                    ],
                },
                {
                    "title": "Training Culture",
                    "clues": [
                        {"value": 100, "question": "This built-in mode lets players enter shareable codes for custom shot packs.", "answer": "What is Custom Training?"},
                        {"value": 200, "question": "This community-made PC mod is famous for advanced free play controls, plugins, and training tools.", "answer": "What is BakkesMod?"},
                        {"value": 300, "question": "These custom maps are best known for threading players through floating aerial checkpoints.", "answer": "What are Rings maps?"},
                        {"value": 400, "question": "This famous map series focuses on controlled ground possession through obstacle courses.", "answer": "What is Dribble Challenge?"},
                        {"value": 500, "question": "This creator is strongly associated with bringing custom maps into the mainstream Rocket League content scene.", "answer": "Who is Lethamyr?"},
                    ],
                },
                {
                    "title": "Early Rocket League History",
                    "clues": [
                        {"value": 100, "question": "Rocket League originally released in this year.", "answer": "What is 2015?"},
                        {"value": 200, "question": "Rocket League's predecessor, SARPBC, was released on this console.", "answer": "What is the PlayStation 3?"},
                        {"value": 300, "question": "This studio developed both SARPBC and Rocket League.", "answer": "What is Psyonix?"},
                        {"value": 400, "question": "This executive is the founder and longtime leader most associated with Psyonix.", "answer": "Who is Dave Hagewood?"},
                        {"value": 500, "question": "Give the full title of Rocket League's predecessor, often shortened to SARPBC.", "answer": "What is Supersonic Acrobatic Rocket-Powered Battle-Cars?"},
                    ],
                },
                {
                    "title": "Modes Beyond Soccar",
                    "clues": [
                        {"value": 100, "question": "This extra mode swaps the ball for a puck.", "answer": "What is Snow Day?"},
                        {"value": 200, "question": "This mode trades soccer goals for basketball hoops.", "answer": "What is Hoops?"},
                        {"value": 300, "question": "This chaotic extra mode gives players power-ups like plunger, spikes, and boot.", "answer": "What is Rumble?"},
                        {"value": 400, "question": "This extra mode revolves around breaking hexagonal floor tiles by slamming a special ball downward.", "answer": "What is Dropshot?"},
                        {"value": 500, "question": "This limited-time mode turned Rocket League into a version of American football.", "answer": "What is Gridiron?"},
                    ],
                },
                {
                    "title": "Recovery Tech",
                    "clues": [
                        {"value": 100, "question": "This turnaround mechanic uses a flip cancel and air roll to reverse direction quickly.", "answer": "What is a half-flip?"},
                        {"value": 200, "question": "This landing technique preserves momentum by jumping right as the wheels touch down.", "answer": "What is a wavedash?"},
                        {"value": 300, "question": "This kickoff and movement technique relies on a very fast diagonal flip cancel.", "answer": "What is a speed flip?"},
                        {"value": 400, "question": "Freestylers use this move to kill rotation midair and set up cleaner touches or resets.", "answer": "What is a stall?"},
                        {"value": 500, "question": "This modern landing burst uses an awkward one-wheel style touch to gain speed instantly.", "answer": "What is a zap dash?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady",
            "categories": [
                {
                    "title": "Patch Notes Graveyard",
                    "clues": [
                        {"value": 200, "question": "Rocket League officially made this business-model change in 2020.", "answer": "What is going free-to-play?"},
                        {"value": 400, "question": "After the Epic transition, new buyers could no longer purchase Rocket League on this PC storefront.", "answer": "What is Steam?"},
                        {"value": 600, "question": "This company acquired Psyonix in 2019.", "answer": "What is Epic Games?"},
                        {"value": 800, "question": "This system replaced randomized paid crates with reveal-first purchasing.", "answer": "What are Blueprints?"},
                        {"value": 1000, "question": "This player-to-player feature was removed in late 2023, to the outrage of a huge portion of the community.", "answer": "What is trading?"},
                    ],
                },
                {
                    "title": "Item Taxonomy",
                    "clues": [
                        {"value": 200, "question": "Labels like Striker, Tactician, Sweeper, and Scorer belong to this item property.", "answer": "What are Certifications?"},
                        {"value": 400, "question": "Titanium White, Crimson, and Black are examples of this cosmetic item variant type.", "answer": "What are painted items?"},
                        {"value": 600, "question": "This special currency is used in the esports item shop.", "answer": "What are Esports Tokens?"},
                        {"value": 800, "question": "This inventory feature lets multiple lower-rarity core items become one item of a higher rarity.", "answer": "What is the trade-in system?"},
                        {"value": 1000, "question": "This currency replaced Keys as the main premium spendable in Rocket League.", "answer": "What are Credits?"},
                    ],
                },
                {
                    "title": "Hitbox Arcana",
                    "clues": [
                        {"value": 200, "question": "Rocket League's standardized car system is divided into this many main hitbox classes.", "answer": "What is 6?"},
                        {"value": 400, "question": "Despite its different visual shape, the Fennec shares this hitbox class with the Octane.", "answer": "What is the Octane hitbox?"},
                        {"value": 600, "question": "The Dominus GT shares this hitbox class with the Dominus.", "answer": "What is the Dominus hitbox?"},
                        {"value": 800, "question": "The 2016 Batmobile is most closely associated with this hitbox class.", "answer": "What is the Plank hitbox?"},
                        {"value": 1000, "question": "This hitbox class is the tallest standardized one in Rocket League.", "answer": "What is the Merc hitbox?"},
                    ],
                },
                {
                    "title": "RLCS Matchups & Mythology",
                    "clues": [
                        {"value": 200, "question": "This player is famously known as 'The Four-Time.'", "answer": "Who is Turbopolsa?"},
                        {"value": 400, "question": "NRG defeated this team in the RLCS Season 8 World Championship final.", "answer": "What is Renault Vitality?"},
                        {"value": 600, "question": "jstn.'s zero-second goal in Season 5 tied the series against this team.", "answer": "What is Dignitas?"},
                        {"value": 800, "question": "This org fielded the Kaydop, Fairy Peak!, and Scrub Killa roster that won RLCS Season 7 Worlds.", "answer": "What is Renault Vitality?"},
                        {"value": 1000, "question": "This org won RLCS Season 8 with GarrettG, Fireburner, and jstn.", "answer": "What is NRG Esports?"},
                    ],
                },
                {
                    "title": "Pressure, 50s & Positioning",
                    "clues": [
                        {"value": 200, "question": "On kickoff, creeping forward behind the taker in anticipation of a favorable ball is called this.", "answer": "What is cheating up?"},
                        {"value": 400, "question": "This kind of challenge is taken mainly to deaden the ball and keep it close.", "answer": "What is a low 50?"},
                        {"value": 600, "question": "This challenge is thrown to force a rushed touch without a full commitment.", "answer": "What is a fake challenge?"},
                        {"value": 800, "question": "Repeatedly stealing pads and big boosts to deny the other team resources is called this.", "answer": "What is boost starving?"},
                        {"value": 1000, "question": "This style of defense means staying goal side and mirroring the attacker instead of diving in early.", "answer": "What is shadow defense?"},
                    ],
                },
                {
                    "title": "Arenas by Vibe",
                    "clues": [
                        {"value": 200, "question": "This arena places players under the sea inside a giant glass dome.", "answer": "What is AquaDome?"},
                        {"value": 400, "question": "This arena is the classic neon-lit city map associated with downtown nighttime play.", "answer": "What is Urban Central?"},
                        {"value": 600, "question": "This arena brings a barn-and-fields rural theme to the standard field.", "answer": "What is Farmstead?"},
                        {"value": 800, "question": "This arena has a castle-and-coliseum aesthetic and is one of Rocket League's classic stadiums.", "answer": "What is Utopia Coliseum?"},
                        {"value": 1000, "question": "This arena name is most associated with big-match atmosphere and a world-championship feel.", "answer": "What is Champions Field?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: Rocket League History",
        "question": "Before Rocket League, Psyonix released this PlayStation 3 predecessor whose title veterans usually shorten to just five letters.",
        "answer": "What is Supersonic Acrobatic Rocket-Powered Battle-Cars?"
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