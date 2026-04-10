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
                    "title": "Champions by Season",
                    "clues": [
                        {"value": 100, "question": "This org won the very first RLCS World Championship.", "answer": "What is iBUYPOWER Cosmic?"},
                        {"value": 200, "question": "Kuxir97, Markydooda, and Greazymeister won Season 2 Worlds under this org name.", "answer": "What is Flipsid3 Tactics?"},
                        {"value": 300, "question": "The Season 3 World Championship was won by this org, with Turbopolsa subbing into the LAN lineup.", "answer": "What is Northern Gaming?"},
                        {"value": 400, "question": "SquishyMuffinz, Gimmick, and Torment won Season 6 Worlds for this org.", "answer": "What is Cloud9?"},
                        {"value": 500, "question": "The first RLCS World Championship held after RLCS X was won by this org.", "answer": "What is Team BDS?"},
                    ],
                },
                {
                    "title": "Who Signed That Roster?",
                    "clues": [
                        {"value": 100, "question": "After winning Worlds as Gale Force eSports, Kaydop, Turbopolsa, and ViolentPanda were signed by this org.", "answer": "What is Dignitas?"},
                        {"value": 200, "question": "After their breakout run as Team Queso, Rise, Joyo, and Vatira were signed by this org.", "answer": "What is Moist Esports?"},
                        {"value": 300, "question": "Kaydop, Fairy Peak!, and Scrub Killa won Season 7 Worlds for this org.", "answer": "What is Renault Vitality?"},
                        {"value": 400, "question": "M0nkey M00n, Extra, and Marc_by_8 became synonymous with this org during the RLCS X era.", "answer": "What is Team BDS?"},
                        {"value": 500, "question": "ApparentlyJack, Noly, and Chronic won the 2022-23 Fall Major for this org.", "answer": "What is Gen.G Mobil1 Racing?"},
                    ],
                },
                {
                    "title": "Worlds by City",
                    "clues": [
                        {"value": 100, "question": "The Season 2 World Championship LAN was held in this Dutch capital.", "answer": "What is Amsterdam?"},
                        {"value": 200, "question": "The Season 5 World Championship, site of the 'THIS IS ROCKET LEAGUE!' call, was held in this city.", "answer": "What is London?"},
                        {"value": 300, "question": "The Season 7 World Championship LAN was held in this New Jersey city.", "answer": "What is Newark?"},
                        {"value": 400, "question": "The Season 8 World Championship LAN was held in this Spanish capital.", "answer": "What is Madrid?"},
                        {"value": 500, "question": "The 2021-22 World Championship main event was held in this Texas city.", "answer": "What is Fort Worth?"},
                    ],
                },
                {
                    "title": "Name the Missing Third",
                    "clues": [
                        {"value": 100, "question": "Kronovi and Lachinio won Season 1 Worlds alongside this third teammate.", "answer": "Who is 0ver Zer0?"},
                        {"value": 200, "question": "Kuxir97 and Markydooda won Season 2 Worlds alongside this teammate.", "answer": "Who is Greazymeister?"},
                        {"value": 300, "question": "GarrettG and jstn. won Season 8 Worlds alongside this veteran third.", "answer": "Who is Fireburner?"},
                        {"value": 400, "question": "Kaydop and Fairy Peak! won Season 7 Worlds alongside this Scottish prodigy.", "answer": "Who is Scrub Killa?"},
                        {"value": 500, "question": "M0nkey M00n and Seikoo won the 2021-22 World Championship alongside this teammate.", "answer": "Who is Extra?"},
                    ],
                },
                {
                    "title": "Regions on the Rise",
                    "clues": [
                        {"value": 100, "question": "Chiefs, Renegades, and Pioneers are all orgs strongly associated with this RLCS region.", "answer": "What is OCE?"},
                        {"value": 200, "question": "FURIA's international breakthrough helped define this RLCS region.", "answer": "What is SAM?"},
                        {"value": 300, "question": "Sandrock Gaming and Team Falcons put this region on the RLCS map.", "answer": "What is MENA?"},
                        {"value": 400, "question": "Tokyo Verdy and DeToNator competed under this RLCS region label.", "answer": "What is APAC?"},
                        {"value": 500, "question": "Limitless became one of the most visible orgs from this RLCS region.", "answer": "What is SSA?"},
                    ],
                },
                {
                    "title": "Legends & Lore",
                    "clues": [
                        {"value": 100, "question": "This player is famously known as 'The Four-Time.'", "answer": "Who is Turbopolsa?"},
                        {"value": 200, "question": "This player reached six straight RLCS World Championship grand finals from Seasons 3 through 8.", "answer": "Who is Kaydop?"},
                        {"value": 300, "question": "This season never had a World Championship because of the pandemic.", "answer": "What is RLCS X?"},
                        {"value": 400, "question": "This player scored the zero-second equalizer in the Season 5 World Championship final.", "answer": "Who is jstn.?"},
                        {"value": 500, "question": "This caster delivered the call, 'THIS IS ROCKET LEAGUE!'", "answer": "Who is Shogun?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady",
            "categories": [
                {
                    "title": "Grand Final Losers Club",
                    "clues": [
                        {"value": 200, "question": "iBUYPOWER Cosmic beat this team in the Season 1 World Championship final.", "answer": "What is Flipsid3 Tactics?"},
                        {"value": 400, "question": "Northern Gaming beat this all-French squad in the Season 3 World Championship final.", "answer": "What is Mock-It Esports?"},
                        {"value": 600, "question": "Dignitas beat this North American team in the Season 5 World Championship final.", "answer": "What is NRG Esports?"},
                        {"value": 800, "question": "Renault Vitality beat this North American team in the Season 7 World Championship final.", "answer": "What is G2 Esports?"},
                        {"value": 1000, "question": "NRG beat this European superteam in the Season 8 World Championship final.", "answer": "What is Renault Vitality?"},
                    ],
                },
                {
                    "title": "Worlds Venues",
                    "clues": [
                        {"value": 200, "question": "The Season 5 World Championship was held at this London venue.", "answer": "What is the Copper Box Arena?"},
                        {"value": 400, "question": "The Season 3 World Championship was held at this Los Angeles venue.", "answer": "What is the Wiltern Theatre?"},
                        {"value": 600, "question": "The Season 7 World Championship was held at this New Jersey venue.", "answer": "What is the Prudential Center?"},
                        {"value": 800, "question": "The Season 8 World Championship was held at this Madrid venue.", "answer": "What is the Palacio Vistalegre?"},
                        {"value": 1000, "question": "The 2021-22 World Championship main event was held at this Fort Worth venue.", "answer": "What is Dickies Arena?"},
                    ],
                },
                {
                    "title": "Open-Era RLCS",
                    "clues": [
                        {"value": 200, "question": "This season name replaced the old numbered-season structure and ran through Fall, Winter, and Spring splits during the pandemic era.", "answer": "What is RLCS X?"},
                        {"value": 400, "question": "This weekly RLCS X competition ran alongside the main regional circuit.", "answer": "What is The Grid?"},
                        {"value": 600, "question": "This term describes one third of a modern RLCS season: Fall, Winter, or Spring.", "answer": "What is a split?"},
                        {"value": 800, "question": "This stage was introduced at the 2021-22 World Championship to filter teams into the main event.", "answer": "What is the Wildcard?"},
                        {"value": 1000, "question": "This format, common in modern RLCS events, advances or eliminates teams after they hit win or loss thresholds.", "answer": "What is a Swiss stage?"},
                    ],
                },
                {
                    "title": "Majors, Not Worlds",
                    "clues": [
                        {"value": 200, "question": "This team won the 2021-22 Fall Major in Stockholm.", "answer": "What is Team BDS?"},
                        {"value": 400, "question": "This North American org won the 2021-22 Winter Major in Los Angeles.", "answer": "What is G2 Esports?"},
                        {"value": 600, "question": "Rise, Joyo, and Vatira won the 2021-22 Spring Major for this org.", "answer": "What is Moist Esports?"},
                        {"value": 800, "question": "ApparentlyJack, Noly, and Chronic won the 2022-23 Fall Major for this org.", "answer": "What is Gen.G Mobil1 Racing?"},
                        {"value": 1000, "question": "This org won the 2022-23 Winter Major in San Diego.", "answer": "What is Karmine Corp?"},
                    ],
                },
                {
                    "title": "Season 3 Stand-In Saga",
                    "clues": [
                        {"value": 200, "question": "This Northern Gaming player was absent from the Season 3 Worlds LAN lineup, prompting a substitute.", "answer": "Who is Maestro?"},
                        {"value": 400, "question": "This substitute stepped in for Northern Gaming and won the World Championship.", "answer": "Who is Turbopolsa?"},
                        {"value": 600, "question": "This Northern Gaming striker was central to their Season 3 title run.", "answer": "Who is Deevo?"},
                        {"value": 800, "question": "Northern Gaming beat this team in the Season 3 World Championship final.", "answer": "What is Mock-It Esports?"},
                        {"value": 1000, "question": "This numbered RLCS season featured the Northern Gaming substitute title run.", "answer": "What is Season 3?"},
                    ],
                },
                {
                    "title": "Records & Streaks",
                    "clues": [
                        {"value": 200, "question": "This many World Championships were won by Turbopolsa.", "answer": "What is 4?"},
                        {"value": 400, "question": "This many straight World Championship grand finals were reached by Kaydop from Seasons 3 through 8.", "answer": "What is 6?"},
                        {"value": 600, "question": "This team ended Dignitas' World Championship reign by sweeping them in the Season 6 grand final.", "answer": "What is Cloud9?"},
                        {"value": 800, "question": "This veteran finally got his RLCS world title with NRG in Season 8 after years of near-misses.", "answer": "Who is GarrettG?"},
                        {"value": 1000, "question": "This organization won back-to-back World Championships in Seasons 4 and 5, though under two different names if you count the original roster org.", "answer": "What is Dignitas?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: RLCS Streaks",
        "question": "This player reached six straight RLCS World Championship grand finals across Mock-It, Gale Force/Dignitas, and Renault Vitality.",
        "answer": "Who is Kaydop?"
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