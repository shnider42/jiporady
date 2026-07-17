from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Jiporady: Utah Jazz & Michigan State",
    "subtitle": "Start with approachable Utah Jazz trivia, then step up to tougher Michigan State Spartans history",
    "rounds": {
        "round_1": {
            "name": "Round 1: Utah Jazz",
            "categories": [
                {
                    "title": "Jazz Basics",
                    "clues": [
                        {"value": 100, "question": "This Utah city is home to the Jazz.", "answer": "What is Salt Lake City?"},
                        {"value": 200, "question": "The franchise began in this Louisiana city in 1974.", "answer": "What is New Orleans?"},
                        {"value": 300, "question": "The team kept this musical nickname after moving from Louisiana to Utah.", "answer": "What is the Jazz?"},
                        {"value": 400, "question": "Utah plays in this major professional basketball league.", "answer": "What is the NBA?"},
                        {"value": 500, "question": "The Jazz compete in this NBA conference.", "answer": "What is the Western Conference?"},
                    ],
                },
                {
                    "title": "Stockton & Malone",
                    "clues": [
                        {"value": 100, "question": "This point guard is the NBA's all-time leader in assists.", "answer": "Who is John Stockton?"},
                        {"value": 200, "question": "Karl Malone was better known by this delivery-themed nickname.", "answer": "What is The Mailman?"},
                        {"value": 300, "question": "Stockton wore this jersey number for Utah.", "answer": "What is 12?"},
                        {"value": 400, "question": "Malone wore this jersey number for most of his Jazz career.", "answer": "What is 32?"},
                        {"value": 500, "question": "Stockton and Malone were famous for running this two-man play.", "answer": "What is the pick-and-roll?"},
                    ],
                },
                {
                    "title": "Home Court",
                    "clues": [
                        {"value": 100, "question": "The Jazz's longtime downtown arena is known by this name.", "answer": "What is the Delta Center?"},
                        {"value": 200, "question": "This bear is the team's furry mascot.", "answer": "Who is Jazz Bear?"},
                        {"value": 300, "question": "Salt Lake City hosted this NBA midseason showcase in both 1993 and 2023.", "answer": "What is the NBA All-Star Game?"},
                        {"value": 400, "question": "The Jazz moved to Utah in this year.", "answer": "What is 1979?"},
                        {"value": 500, "question": "This state appears directly in the team's official name.", "answer": "What is Utah?"},
                    ],
                },
                {
                    "title": "Famous Jazzmen",
                    "clues": [
                        {"value": 100, "question": "This coach led the Stockton-and-Malone Jazz for more than two decades.", "answer": "Who is Jerry Sloan?"},
                        {"value": 200, "question": "This sharpshooting guard joined Utah in the 1990s after starring for Philadelphia and Phoenix.", "answer": "Who is Jeff Hornacek?"},
                        {"value": 300, "question": "This Russian forward was nicknamed AK-47.", "answer": "Who is Andrei Kirilenko?"},
                        {"value": 400, "question": "This French center was nicknamed The Stifle Tower.", "answer": "Who is Rudy Gobert?"},
                        {"value": 500, "question": "This high-flying guard, drafted in 2017, was nicknamed Spida.", "answer": "Who is Donovan Mitchell?"},
                    ],
                },
                {
                    "title": "Finals & Rivals",
                    "clues": [
                        {"value": 100, "question": "Utah reached the NBA Finals in 1997 and 1998 against this team.", "answer": "Who are the Chicago Bulls?"},
                        {"value": 200, "question": "This Bulls superstar hit the series-clinching shot in the 1998 Finals.", "answer": "Who is Michael Jordan?"},
                        {"value": 300, "question": "Utah's first NBA Finals appearance came in this year.", "answer": "What is 1997?"},
                        {"value": 400, "question": "John Stockton's famous 1997 buzzer-beater sent Utah past this Texas team.", "answer": "Who are the Houston Rockets?"},
                        {"value": 500, "question": "The 1996-97 Jazz set a franchise record with this many regular-season wins.", "answer": "What is 64?"},
                    ],
                },
                {
                    "title": "Nicknames & Notes",
                    "clues": [
                        {"value": 100, "question": "Pete Maravich was known by this gun-slinging nickname.", "answer": "What is Pistol Pete?"},
                        {"value": 200, "question": "Darrell Griffith was known by this high-flying medical nickname.", "answer": "What is Dr. Dunkenstein?"},
                        {"value": 300, "question": "This Gonzaga product spent his entire NBA career with Utah.", "answer": "Who is John Stockton?"},
                        {"value": 400, "question": "This Louisiana Tech product became the Jazz's all-time leading scorer.", "answer": "Who is Karl Malone?"},
                        {"value": 500, "question": "This former Jazz guard starred at Illinois before becoming Utah's point guard in the mid-2000s.", "answer": "Who is Deron Williams?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady: Michigan State",
            "categories": [
                {
                    "title": "Championship Basketball",
                    "clues": [
                        {"value": 200, "question": "Michigan State defeated this undefeated team to win the 1979 national championship.", "answer": "Who are the Indiana State Sycamores?"},
                        {"value": 400, "question": "This Indiana State star faced Magic Johnson in the 1979 title game.", "answer": "Who is Larry Bird?"},
                        {"value": 600, "question": "This Spartan was named the Final Four's Most Outstanding Player in 1979.", "answer": "Who is Magic Johnson?"},
                        {"value": 800, "question": "Michigan State beat this SEC school 89-76 for the 2000 national title.", "answer": "Who are the Florida Gators?"},
                        {"value": 1000, "question": "This Flint-born point guard was the 2000 Final Four Most Outstanding Player.", "answer": "Who is Mateen Cleaves?"},
                    ],
                },
                {
                    "title": "Izzo Era Deep Cuts",
                    "clues": [
                        {"value": 200, "question": "Tom Izzo succeeded this coach as Michigan State's head coach in 1995.", "answer": "Who is Jud Heathcote?"},
                        {"value": 400, "question": "The core group nicknamed the Flintstones came from this Michigan city.", "answer": "What is Flint?"},
                        {"value": 600, "question": "Michigan State lost the 2009 national title game at Ford Field to this ACC program.", "answer": "Who are the North Carolina Tar Heels?"},
                        {"value": 800, "question": "This guard hit the buzzer-beating three against Maryland in the 2010 NCAA Tournament.", "answer": "Who is Korie Lucious?"},
                        {"value": 1000, "question": "This forward hit the go-ahead three that helped MSU upset Duke in the 2019 Elite Eight.", "answer": "Who is Kenny Goins?"},
                    ],
                },
                {
                    "title": "Golden-Age Football",
                    "clues": [
                        {"value": 200, "question": "This coach, nicknamed Biggie, led Michigan State before Duffy Daugherty.", "answer": "Who is Clarence Munn?"},
                        {"value": 400, "question": "This Hall of Fame coach guided MSU from 1954 through 1972.", "answer": "Who is Duffy Daugherty?"},
                        {"value": 600, "question": "The famous 1966 Game of the Century ended 10-10 against this school.", "answer": "What is Notre Dame?"},
                        {"value": 800, "question": "This towering defensive end wore No. 95 and became the first pick of the 1967 NFL Draft.", "answer": "Who is Bubba Smith?"},
                        {"value": 1000, "question": "This two-time All-American starred at the hybrid roverback position for the 1965-66 teams.", "answer": "Who is George Webster?"},
                    ],
                },
                {
                    "title": "Dantonio Classics",
                    "clues": [
                        {"value": 200, "question": "The 2010 fake field goal that beat Notre Dame in overtime had this two-word play name.", "answer": "What is Little Giants?"},
                        {"value": 400, "question": "On Little Giants, holder Aaron Bates threw the winning touchdown to this tight end.", "answer": "Who is Charlie Gantt?"},
                        {"value": 600, "question": "Kirk Cousins' 2011 Hail Mary against Wisconsin was caught at the goal line by this receiver.", "answer": "Who is Keith Nichol?"},
                        {"value": 800, "question": "Michigan State defeated this Pac-12 team 24-20 in the 2014 Rose Bowl.", "answer": "Who are the Stanford Cardinal?"},
                        {"value": 1000, "question": "This running back's final reach capped a 22-play drive to beat Iowa in the 2015 Big Ten title game.", "answer": "Who is LJ Scott?"},
                    ],
                },
                {
                    "title": "Spartan Legends",
                    "clues": [
                        {"value": 200, "question": "This two-sport Spartan later hit a famous pinch-hit home run for the Dodgers in the 1988 World Series.", "answer": "Who is Kirk Gibson?"},
                        {"value": 400, "question": "This Danish-born Spartan kicker became one of the NFL's all-time leading scorers.", "answer": "Who is Morten Andersen?"},
                        {"value": 600, "question": "This wide receiver set an NCAA record by catching a touchdown in 13 straight regular-season games.", "answer": "Who is Charles Rogers?"},
                        {"value": 800, "question": "This Spartan goalie won the 2001 Hobey Baker Award before starring for the Buffalo Sabres.", "answer": "Who is Ryan Miller?"},
                        {"value": 1000, "question": "This guard scored a career-high 45 points against Minnesota in January 1986.", "answer": "Who is Scott Skiles?"},
                    ],
                },
                {
                    "title": "Venues & Traditions",
                    "clues": [
                        {"value": 200, "question": "Michigan State's basketball arena is named for this former university administrator.", "answer": "Who is Jack Breslin?"},
                        {"value": 400, "question": "The student section at men's basketball games uses this Izzo-inspired name.", "answer": "What is the Izzone?"},
                        {"value": 600, "question": "Spartan Stadium first opened at its current site in this year.", "answer": "What is 1923?"},
                        {"value": 800, "question": "The first football opponent at the new stadium in 1923 was this Illinois college.", "answer": "What is Lake Forest College?"},
                        {"value": 1000, "question": "The 2001 outdoor hockey game at Spartan Stadium against Michigan was known by this chilly two-word name.", "answer": "What is the Cold War?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: Spartan Football History",
        "question": "This 1966 showdown between No. 1 Notre Dame and No. 2 Michigan State ended in a 10-10 tie and became known as the Game of the Century.",
        "answer": "What is Michigan State vs. Notre Dame?",
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
    return {"ok": True, "app": "jiporady-jazz-msu"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
