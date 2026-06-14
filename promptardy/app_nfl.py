from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Jiporady: NFL",
    "subtitle": "From gridiron basics and legendary players to rivalries, trophies, records, and Sunday chaos",
    "rounds": {
        "round_1": {
            "name": "Round 1",
            "categories": [
                {
                    "title": "Team Nicknames",
                    "clues": [
                        {"value": 100, "question": "Green Bay's NFL team is known by this meat-packing nickname.", "answer": "Who are the Packers?"},
                        {"value": 200, "question": "Dallas uses this western nickname and a star on its helmet.", "answer": "Who are the Cowboys?"},
                        {"value": 300, "question": "Pittsburgh's team name honors the city's historic steel industry.", "answer": "Who are the Steelers?"},
                        {"value": 400, "question": "Miami's NFL team is named for this intelligent marine mammal.", "answer": "Who are the Dolphins?"},
                        {"value": 500, "question": "Baltimore's team name comes from an Edgar Allan Poe poem.", "answer": "Who are the Ravens?"},
                    ],
                },
                {
                    "title": "Positions & Jobs",
                    "clues": [
                        {"value": 100, "question": "This offensive leader usually takes the snap and throws passes.", "answer": "What is the quarterback?"},
                        {"value": 200, "question": "This player snaps the ball to start most offensive plays.", "answer": "What is the center?"},
                        {"value": 300, "question": "These wide-aligned offensive players run routes and catch passes.", "answer": "What are wide receivers?"},
                        {"value": 400, "question": "This defensive back often lines up across from a wide receiver.", "answer": "What is a cornerback?"},
                        {"value": 500, "question": "This hybrid offensive position may block like a lineman or catch passes like a receiver.", "answer": "What is a tight end?"},
                    ],
                },
                {
                    "title": "Scoring Plays",
                    "clues": [
                        {"value": 100, "question": "Crossing the goal line with the ball or catching it in the end zone scores this six-point play.", "answer": "What is a touchdown?"},
                        {"value": 200, "question": "This kick after a touchdown is usually worth one point.", "answer": "What is an extra point?"},
                        {"value": 300, "question": "Kicking the ball through the uprights during a normal play scores this three-point play.", "answer": "What is a field goal?"},
                        {"value": 400, "question": "Tackling the offense in its own end zone creates this two-point defensive score.", "answer": "What is a safety?"},
                        {"value": 500, "question": "After a touchdown, a team can try this play from scrimmage for two points instead of kicking.", "answer": "What is a two-point conversion?"},
                    ],
                },
                {
                    "title": "The Big Game",
                    "clues": [
                        {"value": 100, "question": "This is the NFL's championship game, usually written with Roman numerals.", "answer": "What is the Super Bowl?"},
                        {"value": 200, "question": "The Super Bowl winner receives this trophy named for a famous Packers coach.", "answer": "What is the Vince Lombardi Trophy?"},
                        {"value": 300, "question": "The first Super Bowl was played after the 1966 season between the NFL champion Packers and this AFL team.", "answer": "Who are the Kansas City Chiefs?"},
                        {"value": 400, "question": "This Roman numeral represented the 50th Super Bowl and was replaced by Arabic numeral 50 for branding.", "answer": "What is L?"},
                        {"value": 500, "question": "This perfect-season team won Super Bowl VII and remains famous for finishing 17-0.", "answer": "Who are the 1972 Miami Dolphins?"},
                    ],
                },
                {
                    "title": "Rules & Penalties",
                    "clues": [
                        {"value": 100, "question": "A team normally gets this many downs to gain ten yards.", "answer": "What is four?"},
                        {"value": 200, "question": "Moving before the snap by an offensive player can draw this penalty.", "answer": "What is a false start?"},
                        {"value": 300, "question": "Grabbing an opponent illegally, especially to restrict movement, is this common penalty.", "answer": "What is holding?"},
                        {"value": 400, "question": "A defender crossing the neutral zone and contacting an offensive player before the snap is commonly this penalty.", "answer": "What is encroachment?"},
                        {"value": 500, "question": "When the offense snaps the ball after the play clock hits zero, officials call this penalty.", "answer": "What is delay of game?"},
                    ],
                },
                {
                    "title": "Football Words",
                    "clues": [
                        {"value": 100, "question": "The line where the ball is spotted before a play is the line of this.", "answer": "What is scrimmage?"},
                        {"value": 200, "question": "A pass caught by the defense is called this.", "answer": "What is an interception?"},
                        {"value": 300, "question": "Losing possession after dropping or having the ball knocked loose is called this.", "answer": "What is a fumble?"},
                        {"value": 400, "question": "Throwing the ball away or downfield to avoid a sack without an eligible receiver nearby may be this penalty.", "answer": "What is intentional grounding?"},
                        {"value": 500, "question": "A quarterback changing the play at the line of scrimmage is said to call this.", "answer": "What is an audible?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady",
            "categories": [
                {
                    "title": "Legendary Quarterbacks",
                    "clues": [
                        {"value": 200, "question": "This Patriots and Buccaneers quarterback is widely associated with seven Super Bowl rings.", "answer": "Who is Tom Brady?"},
                        {"value": 400, "question": "This 49ers legend won four Super Bowls and was known for calm precision in big moments.", "answer": "Who is Joe Montana?"},
                        {"value": 600, "question": "This Colts and Broncos quarterback was famous for line-of-scrimmage adjustments and the phrase Omaha.", "answer": "Who is Peyton Manning?"},
                        {"value": 800, "question": "This Packers quarterback won three straight MVP awards in the 1990s and later played for the Jets and Vikings.", "answer": "Who is Brett Favre?"},
                        {"value": 1000, "question": "This Chargers Hall of Famer helped define the Air Coryell passing attack.", "answer": "Who is Dan Fouts?"},
                    ],
                },
                {
                    "title": "Dynasties & Dominance",
                    "clues": [
                        {"value": 200, "question": "This franchise won four Super Bowls in the 1970s with the Steel Curtain defense.", "answer": "Who are the Pittsburgh Steelers?"},
                        {"value": 400, "question": "This team won three Super Bowls in four seasons during the 1990s behind Troy Aikman, Emmitt Smith, and Michael Irvin.", "answer": "Who are the Dallas Cowboys?"},
                        {"value": 600, "question": "Bill Walsh's West Coast offense helped turn this team into an 1980s dynasty.", "answer": "Who are the San Francisco 49ers?"},
                        {"value": 800, "question": "This franchise reached four straight Super Bowls after the 1990 through 1993 seasons but lost them all.", "answer": "Who are the Buffalo Bills?"},
                        {"value": 1000, "question": "Under Bill Belichick and Tom Brady, this team won six Super Bowls from the 2001 through 2018 seasons.", "answer": "Who are the New England Patriots?"},
                    ],
                },
                {
                    "title": "Rivalries & Divisions",
                    "clues": [
                        {"value": 200, "question": "Packers versus Bears is a classic rivalry from this NFC division.", "answer": "What is the NFC North?"},
                        {"value": 400, "question": "Cowboys, Eagles, Giants, and Washington's franchise make up this division.", "answer": "What is the NFC East?"},
                        {"value": 600, "question": "Chiefs, Raiders, Broncos, and Chargers make up this division.", "answer": "What is the AFC West?"},
                        {"value": 800, "question": "The Ravens and Steelers are hard-hitting rivals in this division.", "answer": "What is the AFC North?"},
                        {"value": 1000, "question": "The Saints and Falcons rivalry belongs to this NFC division.", "answer": "What is the NFC South?"},
                    ],
                },
                {
                    "title": "Awards & Honors",
                    "clues": [
                        {"value": 200, "question": "This award names the league's most valuable player for a season.", "answer": "What is NFL MVP?"},
                        {"value": 400, "question": "The NFL's annual all-star showcase is called this.", "answer": "What is the Pro Bowl?"},
                        {"value": 600, "question": "The league's official all-star recognition team is commonly called this, especially when paired with first-team or second-team.", "answer": "What is All-Pro?"},
                        {"value": 800, "question": "The Walter Payton NFL Man of the Year Award honors excellence on the field and this off-field quality.", "answer": "What is community service, or charitable impact?"},
                        {"value": 1000, "question": "The Pro Football Hall of Fame is located in this Ohio city.", "answer": "What is Canton?"},
                    ],
                },
                {
                    "title": "Record Book",
                    "clues": [
                        {"value": 200, "question": "This Cowboys running back holds the NFL career rushing yards record.", "answer": "Who is Emmitt Smith?"},
                        {"value": 400, "question": "This 49ers receiver holds the NFL career receiving yards and receiving touchdowns records.", "answer": "Who is Jerry Rice?"},
                        {"value": 600, "question": "This Rams running back set the single-season rushing yards record in 1984.", "answer": "Who is Eric Dickerson?"},
                        {"value": 800, "question": "This quarterback threw for 5,477 yards in 2013, setting the single-season passing yards record.", "answer": "Who is Peyton Manning?"},
                        {"value": 1000, "question": "This Chargers running back scored 31 touchdowns in 2006, setting the single-season touchdown record.", "answer": "Who is LaDainian Tomlinson?"},
                    ],
                },
                {
                    "title": "Deep Cut Playbook",
                    "clues": [
                        {"value": 200, "question": "This defensive formation uses three down linemen and four linebackers.", "answer": "What is a 3-4 defense?"},
                        {"value": 400, "question": "This defensive formation uses four down linemen and three linebackers.", "answer": "What is a 4-3 defense?"},
                        {"value": 600, "question": "A defense using five defensive backs is commonly called this package.", "answer": "What is nickel?"},
                        {"value": 800, "question": "A quick handoff option paired with a quarterback reading a defender is called this three-letter concept.", "answer": "What is RPO, or run-pass option?"},
                        {"value": 1000, "question": "This offensive style spreads the field and emphasizes short, timing-based passes; Bill Walsh made it famous in San Francisco.", "answer": "What is the West Coast offense?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: NFL History",
        "question": "This coach's name is on the trophy awarded to the winner of the Super Bowl.",
        "answer": "Who is Vince Lombardi?",
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
    return random.sample(categories, category_count)


def build_stats():
    categories = all_categories()
    return {
        "total_categories": len(categories),
        "total_clues": sum(len(category["clues"]) for category in categories),
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
    return {"ok": True, "app": "jiporady-nfl"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
