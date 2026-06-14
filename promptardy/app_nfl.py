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
                    "title": "Pre-Merger Fossils",
                    "clues": [
                        {"value": 200, "question": "The franchise now known as the Bears began APFA play under this Decatur company-team name.", "answer": "Who are the Decatur Staleys?"},
                        {"value": 400, "question": "This undefeated Ohio club was awarded the first APFA championship in 1920.", "answer": "Who are the Akron Pros?"},
                        {"value": 600, "question": "This Pennsylvania club sits at the center of the disputed 1925 NFL championship controversy.", "answer": "Who are the Pottsville Maroons?"},
                        {"value": 800, "question": "This Hall of Famer co-coached Akron in 1921 and is recognized as the NFL's first Black head coach.", "answer": "Who is Fritz Pollard?"},
                        {"value": 1000, "question": "Before the league adopted the NFL name in 1922, it used this four-word association name.", "answer": "What is the American Professional Football Association?"},
                    ],
                },
                {
                    "title": "Old Playoff Ghosts",
                    "clues": [
                        {"value": 200, "question": "NBC cut away from Jets-Raiders to a TV movie, hiding Oakland's late comeback; this nickname stuck.", "answer": "What is the Heidi Game?"},
                        {"value": 400, "question": "Bart Starr's quarterback sneak won this frigid 1967 NFL Championship Game nickname.", "answer": "What is the Ice Bowl?"},
                        {"value": 600, "question": "Clarence Davis' catch through a swarm of Dolphins defenders gave a 1974 Raiders-Dolphins playoff classic this nickname.", "answer": "What is Sea of Hands?"},
                        {"value": 800, "question": "A Ken Stabler-to-Dave Casper deep completion set up Oakland's double-overtime win over Baltimore in this 1977 playoff game nickname.", "answer": "What is Ghost to the Post?"},
                        {"value": 1000, "question": "Stabler's forward fumble and Casper's end-zone recovery against San Diego gave this 1978 Raiders play its nickname.", "answer": "What is the Holy Roller?"},
                    ],
                },
                {
                    "title": "Coaching Tree Stumps",
                    "clues": [
                        {"value": 200, "question": "This Washington coach won Super Bowls with Joe Theismann, Doug Williams, and Mark Rypien as starting quarterbacks.", "answer": "Who is Joe Gibbs?"},
                        {"value": 400, "question": "This defensive mastermind created the 46 defense and coordinated the 1985 Bears before head-coaching the Eagles and Cardinals.", "answer": "Who is Buddy Ryan?"},
                        {"value": 600, "question": "The vertical passing system called Air Coryell takes its name from this Chargers and Cardinals coach.", "answer": "Who is Don Coryell?"},
                        {"value": 800, "question": "This Bengals coach pushed tempo with the no-huddle and once roasted Cleveland fans over the stadium PA.", "answer": "Who is Sam Wyche?"},
                        {"value": 1000, "question": "This Giants defensive coordinator's Super Bowl XXV game plan against Buffalo is famous enough to have landed in Canton.", "answer": "Who is Bill Belichick?"},
                    ],
                },
                {
                    "title": "AFL Merger Archaeology",
                    "clues": [
                        {"value": 200, "question": "Before moving to Kansas City, the Chiefs played in the AFL under this Dallas name.", "answer": "Who are the Dallas Texans?"},
                        {"value": 400, "question": "The Jets began AFL life under this original New York team name.", "answer": "Who are the Titans of New York?"},
                        {"value": 600, "question": "The first Super Bowl was originally billed under this clunky championship-game name.", "answer": "What is the AFL-NFL World Championship Game?"},
                        {"value": 800, "question": "This team was the final AFL champion before the merger fully took effect.", "answer": "Who are the Kansas City Chiefs?"},
                        {"value": 1000, "question": "For a brief moment after moving from Boston, the Patriots tried this state-themed name before becoming New England.", "answer": "Who are the Bay State Patriots?"},
                    ],
                },
                {
                    "title": "Record Book Footnotes",
                    "clues": [
                        {"value": 200, "question": "This Rams back set the single-season rushing record with 2,105 yards in 1984.", "answer": "Who is Eric Dickerson?"},
                        {"value": 400, "question": "This Bills running back was the first to rush for 2,000 yards in a season, doing it in a 14-game schedule.", "answer": "Who is O. J. Simpson?"},
                        {"value": 600, "question": "This Rams quarterback's 554-yard game in 1951 remains the NFL single-game passing yardage record.", "answer": "Who is Norm Van Brocklin?"},
                        {"value": 800, "question": "This Chicago rookie scored six touchdowns in one game against San Francisco in 1965.", "answer": "Who is Gale Sayers?"},
                        {"value": 1000, "question": "This Raiders defensive back owns the single-season interception record with 14 in 1980.", "answer": "Who is Lester Hayes?"},
                    ],
                },
                {
                    "title": "Defense Nickname Museum",
                    "clues": [
                        {"value": 200, "question": "Pittsburgh's dominant 1970s defensive front was known by this industrial nickname.", "answer": "What is the Steel Curtain?"},
                        {"value": 400, "question": "Minnesota's late-1960s and 1970s defensive line wore this royal, people-eating nickname.", "answer": "What are the Purple People Eaters?"},
                        {"value": 600, "question": "The Rams' Deacon Jones-era defensive line shared this intimidating four-man nickname.", "answer": "What is the Fearsome Foursome?"},
                        {"value": 800, "question": "Denver's 1977 Super Bowl defense became known by this citrus-colored nickname.", "answer": "What is the Orange Crush?"},
                        {"value": 1000, "question": "The Jets' late-1960s defensive line of Verlon Biggs, Gerry Philbin, Paul Rochester, and John Elliott used this exchange-themed nickname.", "answer": "What is the New York Sack Exchange?"},
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
