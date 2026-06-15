from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Jiporady: NFL Since 2000",
    "subtitle": "Modern NFL chaos: Brady, Mahomes, memes, miracle plays, draft receipts, replay drama, and playoff heartbreak",
    "rounds": {
        "round_1": {
            "name": "Round 1",
            "categories": [
                {
                    "title": "Modern QB Icons",
                    "clues": [
                        {"value": 100, "question": "This quarterback won six Super Bowls with New England and one more with Tampa Bay.", "answer": "Who is Tom Brady?"},
                        {"value": 200, "question": "This Colts and Broncos quarterback made 'Omaha' a line-of-scrimmage catchphrase.", "answer": "Who is Peyton Manning?"},
                        {"value": 300, "question": "This Packers quarterback won four NFL MVP awards and later joined the Jets.", "answer": "Who is Aaron Rodgers?"},
                        {"value": 400, "question": "This Chiefs quarterback became famous for off-platform throws, no-look passes, and playoff comebacks.", "answer": "Who is Patrick Mahomes?"},
                        {"value": 500, "question": "This Saints quarterback retired as one of the most productive passers ever after years with Sean Payton.", "answer": "Who is Drew Brees?"},
                    ],
                },
                {
                    "title": "Super Bowl Snapshots",
                    "clues": [
                        {"value": 100, "question": "The Patriots' first Super Bowl win after the 2001 season came against this St. Louis team.", "answer": "Who are the Rams?"},
                        {"value": 200, "question": "This Giants receiver made the Helmet Catch in Super Bowl XLII.", "answer": "Who is David Tyree?"},
                        {"value": 300, "question": "Seattle's late interception at the goal line in Super Bowl XLIX was made by this Patriots cornerback.", "answer": "Who is Malcolm Butler?"},
                        {"value": 400, "question": "The Eagles trick play in Super Bowl LII, thrown to Nick Foles, is known by this two-word nickname.", "answer": "What is the Philly Special?"},
                        {"value": 500, "question": "The Chiefs beat this Bay Area team in Super Bowl LIV to win Patrick Mahomes' first title.", "answer": "Who are the San Francisco 49ers?"},
                    ],
                },
                {
                    "title": "Meme Games",
                    "clues": [
                        {"value": 100, "question": "The Falcons led this many points to 3 before New England's Super Bowl LI comeback became a meme forever.", "answer": "What is 28?"},
                        {"value": 200, "question": "Marshawn Lynch's earthquake-causing 2010 playoff run is known by this animal nickname.", "answer": "What is Beast Quake?"},
                        {"value": 300, "question": "Stefon Diggs' walk-off touchdown against the Saints after the 2017 season is called this regional miracle.", "answer": "What is the Minneapolis Miracle?"},
                        {"value": 400, "question": "The 2018 Bears-Eagles playoff miss by Cody Parkey is remembered by this two-impact nickname.", "answer": "What is the Double Doink?"},
                        {"value": 500, "question": "A Thanksgiving 2012 collision with a teammate's backside gave Mark Sanchez this infamous nickname play.", "answer": "What is the Butt Fumble?"},
                    ],
                },
                {
                    "title": "Team Eras",
                    "clues": [
                        {"value": 100, "question": "The early-2000s Patriots dynasty was led by Tom Brady and this hoodie-famous head coach.", "answer": "Who is Bill Belichick?"},
                        {"value": 200, "question": "The Legion of Boom was the nickname for this team's hard-hitting defensive backfield.", "answer": "Who are the Seattle Seahawks?"},
                        {"value": 300, "question": "The Greatest Show on Turf belonged to this franchise at the start of the 2000s.", "answer": "Who are the St. Louis Rams?"},
                        {"value": 400, "question": "The Killer B's nickname in Pittsburgh often referred to Ben Roethlisberger, Antonio Brown, and this running back.", "answer": "Who is Le'Veon Bell?"},
                        {"value": 500, "question": "This franchise used the name Washington Football Team for two seasons before becoming the Commanders.", "answer": "Who are Washington?"},
                    ],
                },
                {
                    "title": "Fantasy Football Faces",
                    "clues": [
                        {"value": 100, "question": "This Chargers running back scored 31 touchdowns in 2006.", "answer": "Who is LaDainian Tomlinson?"},
                        {"value": 200, "question": "This Vikings running back rushed for 2,097 yards in 2012 after returning from a major knee injury.", "answer": "Who is Adrian Peterson?"},
                        {"value": 300, "question": "This Lions receiver nicknamed Megatron was a fantasy monster in the early 2010s.", "answer": "Who is Calvin Johnson?"},
                        {"value": 400, "question": "This Panthers quarterback's 2015 MVP season made dabbing part of NFL highlight culture.", "answer": "Who is Cam Newton?"},
                        {"value": 500, "question": "This Chiefs tight end became Patrick Mahomes' favorite middle-of-the-field target.", "answer": "Who is Travis Kelce?"},
                    ],
                },
                {
                    "title": "Sideline Main Characters",
                    "clues": [
                        {"value": 100, "question": "This Chiefs coach, famous for mustaches and red gear, won Super Bowls with Patrick Mahomes.", "answer": "Who is Andy Reid?"},
                        {"value": 200, "question": "This Seahawks coach's 'always compete' era included a Super Bowl XLVIII blowout win.", "answer": "Who is Pete Carroll?"},
                        {"value": 300, "question": "This Saints coach worked with Drew Brees and later became Broncos head coach.", "answer": "Who is Sean Payton?"},
                        {"value": 400, "question": "This Steelers coach has led Pittsburgh since 2007 and won Super Bowl XLIII.", "answer": "Who is Mike Tomlin?"},
                        {"value": 500, "question": "This Rams coach became one of the youngest head coaches to win a Super Bowl.", "answer": "Who is Sean McVay?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady",
            "categories": [
                {
                    "title": "Playoff Chaos Since 2000",
                    "clues": [
                        {"value": 200, "question": "The 2006 AFC Championship saw this Colts quarterback finally beat Brady's Patriots on the way to his first Super Bowl win.", "answer": "Who is Peyton Manning?"},
                        {"value": 400, "question": "In the 2011 playoffs, Vernon Davis caught a late touchdown from Alex Smith in a 49ers-Saints classic known by this nickname.", "answer": "What is The Catch III?"},
                        {"value": 600, "question": "This Cardinals receiver sprinted across the field for a shovel-pass touchdown in Super Bowl XLIII before Pittsburgh's final drive.", "answer": "Who is Larry Fitzgerald?"},
                        {"value": 800, "question": "This Jaguars quarterback led a 45-point upset of Pittsburgh in the 2017 divisional round before nearly beating New England.", "answer": "Who is Blake Bortles?"},
                        {"value": 1000, "question": "The 2021 AFC Divisional '13 seconds' comeback was forced by Mahomes and this Bills quarterback trading impossible late drives.", "answer": "Who is Josh Allen?"},
                    ],
                },
                {
                    "title": "Draft Receipts",
                    "clues": [
                        {"value": 200, "question": "Tom Brady was drafted with pick 199 in this year.", "answer": "What is 2000?"},
                        {"value": 400, "question": "The Chargers drafted Eli Manning first overall in 2004, then traded him to this team.", "answer": "Who are the New York Giants?"},
                        {"value": 600, "question": "In 2017, the Bears traded up one spot to draft this quarterback second overall.", "answer": "Who is Mitchell Trubisky?"},
                        {"value": 800, "question": "Patrick Mahomes was picked 10th overall in 2017 after Kansas City traded up with this AFC East team.", "answer": "Who are the Buffalo Bills?"},
                        {"value": 1000, "question": "The 2012 draft opened with Andrew Luck first and this Heisman-winning quarterback second.", "answer": "Who is Robert Griffin III?"},
                    ],
                },
                {
                    "title": "Rulebook Drama",
                    "clues": [
                        {"value": 200, "question": "The 2001 Raiders-Patriots playoff controversy centered on this now-retired rule.", "answer": "What is the tuck rule?"},
                        {"value": 400, "question": "This Lions receiver's apparent 2010 game-winning catch helped fuel years of 'process of the catch' debate.", "answer": "Who is Calvin Johnson?"},
                        {"value": 600, "question": "Dez Bryant's overturned 2014 playoff catch came against this team at Lambeau Field.", "answer": "Who are the Green Bay Packers?"},
                        {"value": 800, "question": "A missed pass interference call against the Saints after the 2018 season helped push expanded review of this penalty.", "answer": "What is pass interference?"},
                        {"value": 1000, "question": "The 2021 postseason changed overtime discourse after Buffalo never touched the ball in overtime against this team.", "answer": "Who are the Kansas City Chiefs?"},
                    ],
                },
                {
                    "title": "Not Quite Dynasties",
                    "clues": [
                        {"value": 200, "question": "This team went 15-1 in 2011 behind Aaron Rodgers but lost its first playoff game to the Giants.", "answer": "Who are the Green Bay Packers?"},
                        {"value": 400, "question": "The 2006 Chargers went 14-2 with LaDainian Tomlinson but lost their first playoff game to this team.", "answer": "Who are the New England Patriots?"},
                        {"value": 600, "question": "This team started 13-0 in 2009 under Sean Payton and Drew Brees before winning the Super Bowl.", "answer": "Who are the New Orleans Saints?"},
                        {"value": 800, "question": "This 2015 team went 15-1, dabbed a lot, and lost Super Bowl 50 to Denver.", "answer": "Who are the Carolina Panthers?"},
                        {"value": 1000, "question": "This 2019 team went 14-2 behind Lamar Jackson but lost at home to Derrick Henry's Titans.", "answer": "Who are the Baltimore Ravens?"},
                    ],
                },
                {
                    "title": "Modern Defensive Menaces",
                    "clues": [
                        {"value": 200, "question": "This Ravens linebacker won Super Bowl MVP in the 2000 season and again led Baltimore to a title after the 2012 season.", "answer": "Who is Ray Lewis?"},
                        {"value": 400, "question": "This Steelers safety's flowing hair and instinctive play made him one of the 2000s' most recognizable defenders.", "answer": "Who is Troy Polamalu?"},
                        {"value": 600, "question": "This Texans and Cardinals pass rusher won three Defensive Player of the Year awards in the 2010s.", "answer": "Who is J. J. Watt?"},
                        {"value": 800, "question": "This Rams defensive tackle became the centerpiece of Aaron Donald Appreciation Sundays.", "answer": "Who is Aaron Donald?"},
                        {"value": 1000, "question": "This Broncos linebacker strip-sacked Cam Newton in Super Bowl 50 and was named the game's MVP.", "answer": "Who is Von Miller?"},
                    ],
                },
                {
                    "title": "Modern NFL Grab Bag",
                    "clues": [
                        {"value": 200, "question": "This Bills quarterback jumped over defenders and eventually became one half of the Mahomes-Allen playoff rivalry.", "answer": "Who is Josh Allen?"},
                        {"value": 400, "question": "This Titans running back's stiff-arm highlights and 2,000-yard season made him a modern power-back throwback.", "answer": "Who is Derrick Henry?"},
                        {"value": 600, "question": "This Bengals quarterback helped Cincinnati reach Super Bowl LVI after being drafted first overall in 2020.", "answer": "Who is Joe Burrow?"},
                        {"value": 800, "question": "This Raiders kicker made three game-winning kicks in the 2021 season finale to send Las Vegas to the playoffs.", "answer": "Who is Daniel Carlson?"},
                        {"value": 1000, "question": "This 2008 Dolphins formation briefly turned Ronnie Brown into a left-handed touchdown machine and revived an old-school concept.", "answer": "What is the Wildcat?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: Modern NFL Memes",
        "question": "This number became permanent NFL internet shorthand after New England's Super Bowl LI comeback against Atlanta.",
        "answer": "What is 28-3?",
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
    return {"ok": True, "app": "jiporady-nfl-since-2000"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
