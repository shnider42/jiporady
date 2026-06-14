from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Jiporady: Boston Pro Sports",
    "subtitle": "From Fenway and the Garden to parquet legends, Big Papi moments, Bruins lore, and Patriots heartbreak-to-dynasty history",
    "rounds": {
        "round_1": {
            "name": "Round 1",
            "categories": [
                {
                    "title": "Teams & Homes",
                    "clues": [
                        {"value": 100, "question": "This baseball team has played at Fenway Park since 1912.", "answer": "Who are the Boston Red Sox?"},
                        {"value": 200, "question": "Boston's NBA team is known for green uniforms, parquet history, and leprechaun branding.", "answer": "Who are the Boston Celtics?"},
                        {"value": 300, "question": "Boston's NHL team wears black and gold and plays home games at TD Garden.", "answer": "Who are the Boston Bruins?"},
                        {"value": 400, "question": "This NFL team plays in Foxborough and became a 2000s dynasty.", "answer": "Who are the New England Patriots?"},
                        {"value": 500, "question": "This MLS club also calls the Foxborough area home.", "answer": "Who are the New England Revolution?"},
                    ],
                },
                {
                    "title": "Boston Legends",
                    "clues": [
                        {"value": 100, "question": "This quarterback led New England to six Super Bowl wins before leaving for Tampa Bay.", "answer": "Who is Tom Brady?"},
                        {"value": 200, "question": "This Celtics forward from French Lick became the face of 1980s Boston basketball.", "answer": "Who is Larry Bird?"},
                        {"value": 300, "question": "This Red Sox slugger nicknamed Big Papi became a postseason hero in 2004 and 2013.", "answer": "Who is David Ortiz?"},
                        {"value": 400, "question": "This Bruins defenseman is forever linked to a flying Stanley Cup-clinching goal in 1970.", "answer": "Who is Bobby Orr?"},
                        {"value": 500, "question": "This Celtics center became one of the greatest champions in North American pro sports history.", "answer": "Who is Bill Russell?"},
                    ],
                },
                {
                    "title": "Famous Places",
                    "clues": [
                        {"value": 100, "question": "This tall left-field wall at Fenway Park is painted green.", "answer": "What is the Green Monster?"},
                        {"value": 200, "question": "This old arena hosted both the Celtics and Bruins before closing in the 1990s.", "answer": "What is Boston Garden?"},
                        {"value": 300, "question": "This football stadium in Foxborough opened in 2002.", "answer": "What is Gillette Stadium?"},
                        {"value": 400, "question": "This short right-field foul pole at Fenway is named after a Red Sox infielder.", "answer": "What is Pesky's Pole?"},
                        {"value": 500, "question": "This wooden floor pattern became a visual trademark of Celtics home games.", "answer": "What is parquet?"},
                    ],
                },
                {
                    "title": "Rivals, Obviously",
                    "clues": [
                        {"value": 100, "question": "The Red Sox's most famous baseball rival wears pinstripes in the Bronx.", "answer": "Who are the New York Yankees?"},
                        {"value": 200, "question": "The Celtics' classic NBA Finals rival wears purple and gold.", "answer": "Who are the Los Angeles Lakers?"},
                        {"value": 300, "question": "The Bruins' Original Six rivalry with this Montreal team is one of hockey's oldest.", "answer": "Who are the Montreal Canadiens?"},
                        {"value": 400, "question": "The Patriots have long shared the AFC East with this green New York-area rival.", "answer": "Who are the New York Jets?"},
                        {"value": 500, "question": "This New York football team upset the Patriots in two Super Bowls after the 2007 and 2011 seasons.", "answer": "Who are the New York Giants?"},
                    ],
                },
                {
                    "title": "Championship Moments",
                    "clues": [
                        {"value": 100, "question": "The Red Sox ended this supposed title drought in 2004.", "answer": "What is the Curse of the Bambino?"},
                        {"value": 200, "question": "The Patriots' first Super Bowl win came after the 2001 season against this St. Louis team.", "answer": "Who are the Rams?"},
                        {"value": 300, "question": "The Bruins ended a long Cup drought by winning the Stanley Cup in this year against Vancouver.", "answer": "What is 2011?"},
                        {"value": 400, "question": "The Celtics won the 2008 NBA Finals over this historic rival.", "answer": "Who are the Los Angeles Lakers?"},
                        {"value": 500, "question": "This Red Sox closer recorded the final out of the 2004 World Series.", "answer": "Who is Keith Foulke?"},
                    ],
                },
                {
                    "title": "Nicknames & Sayings",
                    "clues": [
                        {"value": 100, "question": "David Ortiz is best known by this two-word nickname.", "answer": "What is Big Papi?"},
                        {"value": 200, "question": "Ted Williams was famously called this superb-sounding kid.", "answer": "What is the Splendid Splinter?"},
                        {"value": 300, "question": "The Patriots' hoodie-wearing head coach was often linked with this phrase: 'Do your ____.'", "answer": "What is job?"},
                        {"value": 400, "question": "Bruins fans often refer to Bobby Orr's 1970 Cup winner as this airborne type of goal.", "answer": "What is the flying goal?"},
                        {"value": 500, "question": "The Celtics' mascot is named this, matching a lucky Irish symbol.", "answer": "Who is Lucky the Leprechaun?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady",
            "categories": [
                {
                    "title": "1970s Boston Sports",
                    "clues": [
                        {"value": 200, "question": "This Bruin scored the flying goal that clinched the 1970 Stanley Cup against St. Louis.", "answer": "Who is Bobby Orr?"},
                        {"value": 400, "question": "This Red Sox catcher waved his 12th-inning Game 6 drive fair in the 1975 World Series.", "answer": "Who is Carlton Fisk?"},
                        {"value": 600, "question": "This Celtics center and 1973 NBA MVP powered Boston's 1974 and 1976 championship teams.", "answer": "Who is Dave Cowens?"},
                        {"value": 800, "question": "In 1971, the Boston Patriots adopted this regional name as they moved into Foxborough.", "answer": "Who are the New England Patriots?"},
                        {"value": 1000, "question": "Before Fisk's famous homer, this Red Sox pinch hitter tied Game 6 of the 1975 World Series with an eighth-inning three-run shot.", "answer": "Who is Bernie Carbo?"},
                    ],
                },
                {
                    "title": "1980s Boston Sports",
                    "clues": [
                        {"value": 200, "question": "A 1980 trade with Golden State brought Robert Parish to Boston and the pick used on this power forward.", "answer": "Who is Kevin McHale?"},
                        {"value": 400, "question": "This Celtic scored 60 points against Atlanta in a 1985 game played in New Orleans.", "answer": "Who is Larry Bird?"},
                        {"value": 600, "question": "The 1985 Patriots won this conference's championship before losing Super Bowl XX to Chicago.", "answer": "What is the AFC?"},
                        {"value": 800, "question": "This player arrived in Boston from Vancouver in a 1986 trade and became a defining Bruins power forward.", "answer": "Who is Cam Neely?"},
                        {"value": 1000, "question": "This Mets outfielder hit the grounder that went through Bill Buckner's legs in Game 6 of the 1986 World Series.", "answer": "Who is Mookie Wilson?"},
                    ],
                },
                {
                    "title": "Fenway Fine Print",
                    "clues": [
                        {"value": 200, "question": "This former Red Sox owner sold Babe Ruth's contract to the Yankees after the 1919 season.", "answer": "Who is Harry Frazee?"},
                        {"value": 400, "question": "The lone red seat in Fenway's right-field bleachers commemorates this hitter's 502-foot home run.", "answer": "Who is Ted Williams?"},
                        {"value": 600, "question": "This Red Sox pitcher won both the 1967 AL Cy Young and AL MVP awards during the Impossible Dream season.", "answer": "Who is Jim Lonborg?"},
                        {"value": 800, "question": "This old left-field incline at Fenway was named after Red Sox outfielder Duffy Lewis.", "answer": "What is Duffy's Cliff?"},
                        {"value": 1000, "question": "This hand-operated feature still lives inside Fenway's left-field wall.", "answer": "What is the manual scoreboard?"},
                    ],
                },
                {
                    "title": "Celtics Deep Cuts",
                    "clues": [
                        {"value": 200, "question": "This forward was Finals MVP in 1981, not Larry Bird, after Boston beat Houston.", "answer": "Who is Cedric Maxwell?"},
                        {"value": 400, "question": "This guard's 'Havlicek stole the ball' pass was intercepted by John Havlicek in 1965.", "answer": "Who is Hal Greer?"},
                        {"value": 600, "question": "This Celtic hit a clutch jumper over Wilt Chamberlain in Game 7 of the 1969 NBA Finals.", "answer": "Who is Don Nelson?"},
                        {"value": 800, "question": "This Celtic won Rookie of the Year in 1957 while Bill Russell joined midseason after the Olympics.", "answer": "Who is Tom Heinsohn?"},
                        {"value": 1000, "question": "This No. 1 overall pick died before playing for Boston after being drafted in 1986.", "answer": "Who is Len Bias?"},
                    ],
                },
                {
                    "title": "Bruins & Garden Lore",
                    "clues": [
                        {"value": 200, "question": "This German-Canadian Bruins line featured Milt Schmidt, Bobby Bauer, and Woody Dumart.", "answer": "What is the Kraut Line?"},
                        {"value": 400, "question": "This Bruins goalie painted stitches on his mask for each puck that would have hit his face.", "answer": "Who is Gerry Cheevers?"},
                        {"value": 600, "question": "This fiery Bruins captain was later nicknamed 'The Tasmanian Devil.'", "answer": "Who is Terry O'Reilly?"},
                        {"value": 800, "question": "This Bruin became the first NHL defenseman to score 100 points in a season.", "answer": "Who is Bobby Orr?"},
                        {"value": 1000, "question": "This Bruins captain wore No. 77 after Phil Esposito's No. 7 was retired.", "answer": "Who is Ray Bourque?"},
                    ],
                },
                {
                    "title": "Patriots Before the Dynasty",
                    "clues": [
                        {"value": 200, "question": "Before becoming New England, the franchise played under this city name in the AFL.", "answer": "Who are the Boston Patriots?"},
                        {"value": 400, "question": "This long-running quarterback bridged the 1970s and 1980s and held many Patriots passing records before the Brady era.", "answer": "Who is Steve Grogan?"},
                        {"value": 600, "question": "This Hall of Fame guard was the Patriots' offensive line icon through the 1970s and early 1980s.", "answer": "Who is John Hannah?"},
                        {"value": 800, "question": "This linebacker was the Patriots' defensive star of the mid-1980s and later reached Canton.", "answer": "Who is Andre Tippett?"},
                        {"value": 1000, "question": "This kicker's snow-clearing field goal against Miami in 1982 became the Snowplow Game's signature moment.", "answer": "Who is John Smith?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: Boston Sports Cathedrals",
        "question": "This arena hosted both the Celtics and Bruins for decades and closed in 1995, but its name still carries mythic weight in Boston sports.",
        "answer": "What is Boston Garden?",
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
    return {"ok": True, "app": "jiporady-boston-sports"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
