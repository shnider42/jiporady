from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Jiporady: MLB Since 2000",
    "subtitle": "Modern baseball from 2000 through 2025: AL East wars, awards, iconic moments, scandals, sluggers, gloves, trades, and October pain",
    "rounds": {
        "round_1": {
            "name": "Round 1",
            "categories": [
                {
                    "title": "AL East Since 2000",
                    "clues": [
                        {"value": 100, "question": "This AL East team ended an 86-year World Series championship drought in 2004.", "answer": "Who are the Boston Red Sox?"},
                        {"value": 200, "question": "Before the 2008 season, Tampa Bay dropped this word from its original team name.", "answer": "What is 'Devil'?"},
                        {"value": 300, "question": "This club won the 2014 AL East, its first division title since 1997.", "answer": "Who are the Baltimore Orioles?"},
                        {"value": 400, "question": "This Blue Jays third baseman won the 2015 AL MVP while helping Toronto win the AL East.", "answer": "Who is Josh Donaldson?"},
                        {"value": 500, "question": "This AL East club won the American League pennant in the shortened 2020 season.", "answer": "Who are the Tampa Bay Rays?"},
                    ],
                },
                {
                    "title": "Batting",
                    "clues": [
                        {"value": 100, "question": "This Mariners star set the MLB single-season hits record with 262 in 2004.", "answer": "Who is Ichiro Suzuki?"},
                        {"value": 200, "question": "This Tigers slugger won the 2012 Triple Crown with a .330 average, 44 homers, and 139 RBIs.", "answer": "Who is Miguel Cabrera?"},
                        {"value": 300, "question": "This Twins catcher won his first AL batting title in 2006 and eventually became the first catcher to win three batting titles.", "answer": "Who is Joe Mauer?"},
                        {"value": 400, "question": "This Red Sox star won the 2018 AL batting title at .346 in the same season he won MVP.", "answer": "Who is Mookie Betts?"},
                        {"value": 500, "question": "This Red Sox third baseman won the 2003 AL batting title, the last Boston player to do so before Mookie Betts.", "answer": "Who is Bill Mueller?"},
                    ],
                },
                {
                    "title": "MVP",
                    "clues": [
                        {"value": 100, "question": "This Yankees slugger won AL MVP in 2022, 2024, and 2025.", "answer": "Who is Aaron Judge?"},
                        {"value": 200, "question": "This Red Sox outfielder won the 2018 AL MVP during Boston's 108-win championship season.", "answer": "Who is Mookie Betts?"},
                        {"value": 300, "question": "This Red Sox second baseman won the 2008 AL MVP.", "answer": "Who is Dustin Pedroia?"},
                        {"value": 400, "question": "This Tigers ace became the first starting pitcher since Roger Clemens in 1986 to win AL MVP, doing it in 2011.", "answer": "Who is Justin Verlander?"},
                        {"value": 500, "question": "Nicknamed the 'Bringer of Rain,' this Toronto third baseman won the 2015 AL MVP.", "answer": "Who is Josh Donaldson?"},
                    ],
                },
                {
                    "title": "Cy Young",
                    "clues": [
                        {"value": 100, "question": "This Red Sox ace won the 2000 AL Cy Young Award.", "answer": "Who is Pedro Martinez?"},
                        {"value": 200, "question": "This Boston right-hander edged Justin Verlander for the 2016 AL Cy Young.", "answer": "Who is Rick Porcello?"},
                        {"value": 300, "question": "This Rays left-hander won the 2018 AL Cy Young with a 1.89 ERA.", "answer": "Who is Blake Snell?"},
                        {"value": 400, "question": "This Blue Jays left-hander won the 2021 AL Cy Young after leading the majors with 248 strikeouts.", "answer": "Who is Robbie Ray?"},
                        {"value": 500, "question": "This Yankees ace won his first Cy Young Award in 2023.", "answer": "Who is Gerrit Cole?"},
                    ],
                },
                {
                    "title": "Yankees Fans, Look Away",
                    "clues": [
                        {"value": 100, "question": "In 2004, Boston became the first MLB team ever to erase this series deficit and still win a postseason series.", "answer": "What is 3 games to 0?"},
                        {"value": 200, "question": "This pinch-runner stole second off Mariano Rivera in the ninth inning of 2004 ALCS Game 4.", "answer": "Who is Dave Roberts?"},
                        {"value": 300, "question": "Boston sent New York home 6-2 in this winner-take-all postseason game in 2021.", "answer": "What is the American League Wild Card Game?"},
                        {"value": 400, "question": "This Red Sox utility player hit the first cycle in postseason history during a 16-1 ALDS win at Yankee Stadium in 2018.", "answer": "Who is Brock Holt?"},
                        {"value": 500, "question": "This Red Sox center fielder hit a grand slam and a two-run homer in Game 7 of the 2004 ALCS at Yankee Stadium.", "answer": "Who is Johnny Damon?"},
                    ],
                },
                {
                    "title": "Stadium Names",
                    "clues": [
                        {"value": 100, "question": "Toronto's SkyDome was renamed this in 2005.", "answer": "What is Rogers Centre?"},
                        {"value": 200, "question": "The Giants' former AT&T Park became this in 2019.", "answer": "What is Oracle Park?"},
                        {"value": 300, "question": "Marlins Park took on this lowercase-heavy corporate name in 2021.", "answer": "What is loanDepot park?"},
                        {"value": 400, "question": "Before becoming Guaranteed Rate Field in 2016, the White Sox ballpark had this corporate name.", "answer": "What is U.S. Cellular Field?"},
                        {"value": 500, "question": "Citi Field opened in 2009 as the replacement for this longtime Mets home.", "answer": "What is Shea Stadium?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady",
            "categories": [
                {
                    "title": "Players in Moments",
                    "clues": [
                        {"value": 200, "question": "This Yankee ended the 2003 ALCS with an 11th-inning walk-off homer off Tim Wakefield.", "answer": "Who is Aaron Boone?"},
                        {"value": 400, "question": "After Dave Roberts stole second in 2004 ALCS Game 4, this Red Sox hitter singled off Mariano Rivera to drive him home with the tying run.", "answer": "Who is Bill Mueller?"},
                        {"value": 600, "question": "This Cleveland outfielder tied Game 7 of the 2016 World Series with an eighth-inning homer off Aroldis Chapman.", "answer": "Who is Rajai Davis?"},
                        {"value": 800, "question": "This Astros second baseman ended the 2019 ALCS with a walk-off homer off Aroldis Chapman.", "answer": "Who is Jose Altuve?"},
                        {"value": 1000, "question": "This Rays hitter beat Aroldis Chapman with the decisive homer in Game 5 of the 2020 ALDS.", "answer": "Who is Mike Brosseau?"},
                    ],
                },
                {
                    "title": "Stat Leaders",
                    "clues": [
                        {"value": 200, "question": "This player owns the modern single-season hits record after collecting 262 in 2004.", "answer": "Who is Ichiro Suzuki?"},
                        {"value": 400, "question": "This catcher led the AL with a .365 batting average in 2009.", "answer": "Who is Joe Mauer?"},
                        {"value": 600, "question": "This Oakland slugger led all of MLB with 48 home runs in 2018.", "answer": "Who is Khris Davis?"},
                        {"value": 800, "question": "This Orioles first baseman led MLB with 53 home runs in 2013.", "answer": "Who is Chris Davis?"},
                        {"value": 1000, "question": "This Cubs slugger led the majors with exactly 50 home runs in 2000.", "answer": "Who is Sammy Sosa?"},
                    ],
                },
                {
                    "title": "Controversies",
                    "clues": [
                        {"value": 200, "question": "This Tigers pitcher lost a perfect game in 2010 when umpire Jim Joyce missed the would-be final out at first base.", "answer": "Who is Armando Galarraga?"},
                        {"value": 400, "question": "A controversial infield-fly call in the 2012 NL Wild Card Game was made on a ball hit by this Braves shortstop.", "answer": "Who is Andrelton Simmons?"},
                        {"value": 600, "question": "This Red Sox third baseman was called for obstruction on the walk-off play that ended Game 3 of the 2013 World Series.", "answer": "Who is Will Middlebrooks?"},
                        {"value": 800, "question": "This Cubs left fielder was reaching for the foul ball involved in the infamous Steve Bartman play during the 2003 NLCS.", "answer": "Who is Moises Alou?"},
                        {"value": 1000, "question": "MLB's report on Houston's 2017 sign-stealing scheme identified this later Red Sox manager, then the Astros bench coach, as a major participant in creating the system.", "answer": "Who is Alex Cora?"},
                    ],
                },
                {
                    "title": "Steroid Era",
                    "clues": [
                        {"value": 200, "question": "This Giants slugger set the still-standing MLB single-season home run record with 73 in 2001.", "answer": "Who is Barry Bonds?"},
                        {"value": 400, "question": "This Brewers star accepted a 65-game suspension in 2013 after MLB's Biogenesis investigation.", "answer": "Who is Ryan Braun?"},
                        {"value": 600, "question": "This Yankees third baseman received the harshest punishment from the 2013 Biogenesis case, originally a 211-game suspension.", "answer": "Who is Alex Rodriguez?"},
                        {"value": 800, "question": "At a 2005 congressional hearing on steroids, this former 70-home-run slugger repeatedly said he was 'not here to talk about the past.'", "answer": "Who is Mark McGwire?"},
                        {"value": 1000, "question": "Baseball's 2007 investigation into PED use became known by the surname of this former U.S. senator who led it.", "answer": "Who is George Mitchell?"},
                    ],
                },
                {
                    "title": "Gold Gloves & Homers",
                    "clues": [
                        {"value": 200, "question": "This Yankees slugger broke the American League single-season home run record with 62 in 2022.", "answer": "Who is Aaron Judge?"},
                        {"value": 400, "question": "This Mariners outfielder won 10 straight Gold Gloves from 2001 through 2010.", "answer": "Who is Ichiro Suzuki?"},
                        {"value": 600, "question": "This Cardinals catcher won his ninth Gold Glove in 2018 after winning eight straight from 2008 through 2015.", "answer": "Who is Yadier Molina?"},
                        {"value": 800, "question": "This third baseman won a Gold Glove in each of his first 10 MLB seasons, from 2013 through 2022.", "answer": "Who is Nolan Arenado?"},
                        {"value": 1000, "question": "This 2017 NL MVP led MLB with 59 home runs immediately before being traded to the Yankees.", "answer": "Who is Giancarlo Stanton?"},
                    ],
                },
                {
                    "title": "Trades",
                    "clues": [
                        {"value": 200, "question": "Boston traded this 2018 AL MVP to the Dodgers before the 2020 season in a deal that brought back Alex Verdugo, Jeter Downs, and Connor Wong.", "answer": "Who is Mookie Betts?"},
                        {"value": 400, "question": "Houston acquired this former AL MVP and Cy Young winner from Detroit on Aug. 31, 2017, just in time for postseason eligibility.", "answer": "Who is Justin Verlander?"},
                        {"value": 600, "question": "Milwaukee acquired this reigning Cy Young winner from Cleveland in July 2008; he then went 11-2 down the stretch.", "answer": "Who is CC Sabathia?"},
                        {"value": 800, "question": "Boston acquired this ace from the White Sox in December 2016 for a package headlined by Yoan Moncada and Michael Kopech.", "answer": "Who is Chris Sale?"},
                        {"value": 1000, "question": "In December 2023, the Yankees acquired this superstar outfielder from San Diego in a seven-player trade headlined on the Padres' side by Michael King.", "answer": "Who is Juan Soto?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: Players in Moments",
        "question": "Before Luis Gonzalez's famous walk-off single in Game 7 of the 2001 World Series, this Diamondbacks infielder doubled home the tying run off Mariano Rivera.",
        "answer": "Who is Tony Womack?",
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
    return {"ok": True, "app": "jiporady-mlb-since-2000"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
