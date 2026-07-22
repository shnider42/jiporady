"""Boston Red Sox history topic module for Jiporady."""

from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Jiporady: Boston Red Sox History",
    "subtitle": "Fenway lore, franchise icons, pennant heartbreak, championship comebacks, and more than a century of Red Sox history",
    "rounds": {
        "round_1": {
            "name": "Round 1",
            "categories": [
                {
                    "title": "Fenway Park Lore",
                    "clues": [
                        {"value": 100, "question": "Fenway Park's first official game in 1912 was an extra-inning win over this New York club, later renamed the Yankees.", "answer": "Who were the New York Highlanders?"},
                        {"value": 200, "question": "The lone red seat in Fenway's right-field bleachers marks a 502-foot home run hit by this Red Sox legend.", "answer": "Who is Ted Williams?"},
                        {"value": 300, "question": "Fenway's short right-field foul pole is named for this longtime player, coach, manager, and 'Mr. Red Sox.'", "answer": "Who is Johnny Pesky?"},
                        {"value": 400, "question": "Before Fenway's left field was rebuilt in the 1930s, this sloped embankment was named for an outfielder.", "answer": "What was Duffy's Cliff?"},
                        {"value": 500, "question": "Fenway Park hosted its first night game in this year, with Boston defeating the White Sox.", "answer": "What is 1947?"},
                    ],
                },
                {
                    "title": "Sox Icons",
                    "clues": [
                        {"value": 100, "question": "This 'Splendid Splinter' remains the last AL or NL player to bat .400, finishing at .406 in 1941.", "answer": "Who is Ted Williams?"},
                        {"value": 200, "question": "This left fielder won the 1967 Triple Crown and led the 'Impossible Dream' Red Sox to the pennant.", "answer": "Who is Carl Yastrzemski?"},
                        {"value": 300, "question": "At Fenway's 1999 All-Star Game, this ace struck out five of the six batters he faced and won MVP honors.", "answer": "Who is Pedro Martinez?"},
                        {"value": 400, "question": "In 1975, this center fielder became the first player to win Rookie of the Year and MVP in the same season.", "answer": "Who is Fred Lynn?"},
                        {"value": 500, "question": "This slugger totaled 400 bases in 1978, the first American Leaguer to reach that mark since Joe DiMaggio.", "answer": "Who is Jim Rice?"},
                    ],
                },
                {
                    "title": "Pennant Drama",
                    "clues": [
                        {"value": 100, "question": "Boston's surprising 1967 pennant-winning season is remembered by this dreamlike nickname.", "answer": "What is the Impossible Dream?"},
                        {"value": 200, "question": "This catcher famously waved his 12th-inning home run fair in Game 6 of the 1975 World Series.", "answer": "Who is Carlton Fisk?"},
                        {"value": 300, "question": "This Mets outfielder hit the ground ball that rolled through Bill Buckner's legs in Game 6 of the 1986 World Series.", "answer": "Who is Mookie Wilson?"},
                        {"value": 400, "question": "This Cardinals outfielder made the 'Mad Dash' from first base to score the winning run in Game 7 of the 1946 World Series.", "answer": "Who is Enos Slaughter?"},
                        {"value": 500, "question": "This Yankees shortstop hit the famous three-run homer in the 1978 AL East tiebreaker at Fenway.", "answer": "Who is Bucky Dent?"},
                    ],
                },
                {
                    "title": "The Yankees Rivalry",
                    "clues": [
                        {"value": 100, "question": "This Red Sox owner sold Babe Ruth's contract to the Yankees after the 1919 season.", "answer": "Who is Harry Frazee?"},
                        {"value": 200, "question": "This Yankee ended the 2003 ALCS with an 11th-inning home run in Game 7.", "answer": "Who is Aaron Boone?"},
                        {"value": 300, "question": "This pinch-runner stole second in the ninth inning of 2004 ALCS Game 4, beginning Boston's historic comeback.", "answer": "Who is Dave Roberts?"},
                        {"value": 400, "question": "This third baseman singled up the middle to score Roberts and tie Game 4 against Mariano Rivera.", "answer": "Who is Bill Mueller?"},
                        {"value": 500, "question": "This former Yankee hit a grand slam for Boston in Game 7 of the 2004 ALCS.", "answer": "Who is Johnny Damon?"},
                    ],
                },
                {
                    "title": "Championship Returns",
                    "clues": [
                        {"value": 100, "question": "Boston swept this National League club to win the 2004 World Series and end an 86-year title drought.", "answer": "Who are the St. Louis Cardinals?"},
                        {"value": 200, "question": "This closer fielded the final ground ball of the 2004 World Series and threw to first for the championship.", "answer": "Who is Keith Foulke?"},
                        {"value": 300, "question": "The Red Sox swept this expansion club to win the 2007 World Series.", "answer": "Who are the Colorado Rockies?"},
                        {"value": 400, "question": "This closer struck out Matt Carpenter for the final out of the 2013 World Series.", "answer": "Who is Koji Uehara?"},
                        {"value": 500, "question": "This first baseman was named World Series MVP after Boston beat the Dodgers in 2018.", "answer": "Who is Steve Pearce?"},
                    ],
                },
                {
                    "title": "Nicknames & Numbers",
                    "clues": [
                        {"value": 100, "question": "David Ortiz is best known by this two-word nickname.", "answer": "What is Big Papi?"},
                        {"value": 200, "question": "Ted Williams carried this nickname inspired by his thin frame and elite hitting.", "answer": "What is the Splendid Splinter?"},
                        {"value": 300, "question": "Carl Yastrzemski is almost universally known by this three-letter nickname.", "answer": "What is Yaz?"},
                        {"value": 400, "question": "Luis Tiant's twisting delivery and Cuban heritage helped make this his famous nickname.", "answer": "What is El Tiante?"},
                        {"value": 500, "question": "This player associated with retired No. 6 was affectionately known as 'Mr. Red Sox.'", "answer": "Who is Johnny Pesky?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady",
            "categories": [
                {
                    "title": "Origins & Early Titles",
                    "clues": [
                        {"value": 200, "question": "When the American League began play in 1901, the franchise was commonly known by this pre-Red Sox name.", "answer": "Who were the Boston Americans?"},
                        {"value": 400, "question": "Boston defeated this National League club in the first modern World Series in 1903.", "answer": "Who are the Pittsburgh Pirates?"},
                        {"value": 600, "question": "Before Fenway Park, the franchise played at this grounds near today's Northeastern University.", "answer": "What was the Huntington Avenue Grounds?"},
                        {"value": 800, "question": "Because it held more fans, Boston played its home World Series games in 1915 and 1916 at this National League ballpark.", "answer": "What was Braves Field?"},
                        {"value": 1000, "question": "This first baseman hit the first major-league home run at Fenway Park in April 1912; it was the last homer of his career.", "answer": "Who is Hugh Bradley?"},
                    ],
                },
                {
                    "title": "Teddy Ballgame Era",
                    "clues": [
                        {"value": 200, "question": "Ted Williams finished with a .406 batting average in this season.", "answer": "What is 1941?"},
                        {"value": 400, "question": "Williams homered in the final at-bat of his career off this Orioles pitcher.", "answer": "Who is Jack Fisher?"},
                        {"value": 600, "question": "Rather than protect his average on the final day of 1941, Williams played both games of a doubleheader and went this many hits for this many at-bats.", "answer": "What is 6-for-8?"},
                        {"value": 800, "question": "This Hall of Fame second baseman hit .409 for Boston in the 1946 World Series.", "answer": "Who is Bobby Doerr?"},
                        {"value": 1000, "question": "Williams lost major-league time while serving as a military pilot during these two wars.", "answer": "What are World War II and the Korean War?"},
                    ],
                },
                {
                    "title": "1967 to 1986",
                    "clues": [
                        {"value": 200, "question": "This pitcher won the 1967 AL Cy Young Award during Boston's Impossible Dream season.", "answer": "Who is Jim Lonborg?"},
                        {"value": 400, "question": "In his 1967 major-league debut, Billy Rohr lost a no-hitter with two outs in the ninth on a single by this Yankee.", "answer": "Who is Elston Howard?"},
                        {"value": 600, "question": "This pinch hitter tied Game 6 of the 1975 World Series with an eighth-inning three-run homer.", "answer": "Who is Bernie Carbo?"},
                        {"value": 800, "question": "In the 11th inning of that Game 6, Dwight Evans robbed this Reds star and doubled Ken Griffey off first.", "answer": "Who is Joe Morgan?"},
                        {"value": 1000, "question": "This outfielder homered with Boston one strike from elimination in Game 5 of the 1986 ALCS.", "answer": "Who is Dave Henderson?"},
                    ],
                },
                {
                    "title": "2004 Deep Cuts",
                    "clues": [
                        {"value": 200, "question": "This batter drew the leadoff walk from Mariano Rivera before Dave Roberts entered Game 4 as a pinch-runner.", "answer": "Who is Kevin Millar?"},
                        {"value": 400, "question": "David Ortiz's Game 4 walk-off home run came against this Yankees reliever.", "answer": "Who is Paul Quantrill?"},
                        {"value": 600, "question": "This second baseman hit a disputed three-run home run in the 'Bloody Sock' Game 6.", "answer": "Who is Mark Bellhorn?"},
                        {"value": 800, "question": "This pitcher started and won ALCS Game 7 on two days' rest.", "answer": "Who is Derek Lowe?"},
                        {"value": 1000, "question": "This Cardinals shortstop grounded to Foulke for the final out of the 2004 World Series.", "answer": "Who is Edgar Renteria?"},
                    ],
                },
                {
                    "title": "Modern Champions",
                    "clues": [
                        {"value": 200, "question": "This third baseman was named MVP of the 2007 World Series.", "answer": "Who is Mike Lowell?"},
                        {"value": 400, "question": "This outfielder hit a first-inning grand slam in Game 6 of the 2007 ALCS to help force Game 7.", "answer": "Who is J.D. Drew?"},
                        {"value": 600, "question": "This 'Flyin' Hawaiian' hit the go-ahead grand slam that clinched the 2013 AL pennant.", "answer": "Who is Shane Victorino?"},
                        {"value": 800, "question": "This Cardinals hitter struck out against Koji Uehara for the final out of the 2013 World Series.", "answer": "Who is Matt Carpenter?"},
                        {"value": 1000, "question": "This left fielder made a game-ending diving catch with the bases loaded in 2018 ALCS Game 4.", "answer": "Who is Andrew Benintendi?"},
                    ],
                },
                {
                    "title": "Deals That Changed Boston",
                    "clues": [
                        {"value": 200, "question": "Before joining Boston in 2003, David Ortiz had been released by this American League club.", "answer": "Who are the Minnesota Twins?"},
                        {"value": 400, "question": "Boston acquired Pedro Martinez from this Canadian franchise in November 1997.", "answer": "Who are the Montreal Expos?"},
                        {"value": 600, "question": "These two pitching prospects went to Montreal in the Pedro Martinez trade.", "answer": "Who are Carl Pavano and Tony Armas Jr.?"},
                        {"value": 800, "question": "Boston's 2004 Nomar Garciaparra trade brought back these two eventual championship infielders.", "answer": "Who are Orlando Cabrera and Doug Mientkiewicz?"},
                        {"value": 1000, "question": "In 1990, Boston traded future Hall of Fame first baseman Jeff Bagwell to Houston for this relief pitcher.", "answer": "Who is Larry Andersen?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: A Season for the Ages",
        "question": "In 1967, this Red Sox star won the Triple Crown, AL MVP, and a Gold Glove while leading Boston to its first pennant since 1946.",
        "answer": "Who is Carl Yastrzemski?",
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
    return {"ok": True, "app": "jiporady-red-sox-history"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
