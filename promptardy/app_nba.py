from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Jiporady: NBA",
    "subtitle": "From easy buckets and superstar nicknames to ABA ghosts, old Finals lore, weird box scores, and historian-level hardwood chaos",
    "rounds": {
        "round_1": {
            "name": "Round 1",
            "categories": [
                {
                    "title": "Teams & Cities",
                    "clues": [
                        {"value": 100, "question": "This Boston team is famous for green jerseys, parquet history, and a lot of championship banners.", "answer": "Who are the Boston Celtics?"},
                        {"value": 200, "question": "This Los Angeles team wears purple and gold and shares a famous rivalry with Boston.", "answer": "Who are the Los Angeles Lakers?"},
                        {"value": 300, "question": "This Chicago team won six championships in the 1990s behind Michael Jordan.", "answer": "Who are the Chicago Bulls?"},
                        {"value": 400, "question": "This Texas team won five championships with Tim Duncan as its franchise cornerstone.", "answer": "Who are the San Antonio Spurs?"},
                        {"value": 500, "question": "This Bay Area team built a modern dynasty around Stephen Curry, Klay Thompson, and Draymond Green.", "answer": "Who are the Golden State Warriors?"},
                    ],
                },
                {
                    "title": "Superstar 101",
                    "clues": [
                        {"value": 100, "question": "This Bulls legend is widely known by the initials MJ.", "answer": "Who is Michael Jordan?"},
                        {"value": 200, "question": "This Lakers and Cavaliers star is often called King James.", "answer": "Who is LeBron James?"},
                        {"value": 300, "question": "This Warriors guard changed modern basketball with deep three-point shooting.", "answer": "Who is Stephen Curry?"},
                        {"value": 400, "question": "This Lakers center was nicknamed Shaq.", "answer": "Who is Shaquille O'Neal?"},
                        {"value": 500, "question": "This Lakers guard scored 81 points in a 2006 game against Toronto.", "answer": "Who is Kobe Bryant?"},
                    ],
                },
                {
                    "title": "NBA Basics",
                    "clues": [
                        {"value": 100, "question": "A normal NBA field goal from inside the arc is worth this many points.", "answer": "What is two?"},
                        {"value": 200, "question": "A made shot from behind the arc is worth this many points.", "answer": "What is three?"},
                        {"value": 300, "question": "A team has this many players on the court at one time.", "answer": "What is five?"},
                        {"value": 400, "question": "This violation is called when a player takes too many steps without dribbling.", "answer": "What is traveling?"},
                        {"value": 500, "question": "The NBA shot clock is this many seconds long.", "answer": "What is 24 seconds?"},
                    ],
                },
                {
                    "title": "Famous Finals",
                    "clues": [
                        {"value": 100, "question": "The Larry O'Brien Trophy is awarded to the winner of this league's Finals.", "answer": "What is the NBA?"},
                        {"value": 200, "question": "The 2016 Cavaliers came back from a 3-1 Finals deficit against this team.", "answer": "Who are the Golden State Warriors?"},
                        {"value": 300, "question": "The 2008 Celtics beat this historic rival in the NBA Finals.", "answer": "Who are the Los Angeles Lakers?"},
                        {"value": 400, "question": "Dirk Nowitzki led this team to the 2011 NBA championship.", "answer": "Who are the Dallas Mavericks?"},
                        {"value": 500, "question": "Kawhi Leonard won Finals MVP with this Canadian team in 2019.", "answer": "Who are the Toronto Raptors?"},
                    ],
                },
                {
                    "title": "Positions & Plays",
                    "clues": [
                        {"value": 100, "question": "This guard position usually runs the offense and brings the ball up the floor.", "answer": "What is point guard?"},
                        {"value": 200, "question": "This tallest traditional position often protects the rim and rebounds.", "answer": "What is center?"},
                        {"value": 300, "question": "A pass that directly leads to a made basket is called this.", "answer": "What is an assist?"},
                        {"value": 400, "question": "A missed shot recovered by a player is called this.", "answer": "What is a rebound?"},
                        {"value": 500, "question": "A hard screen and roll to the basket is part of this two-player action.", "answer": "What is pick-and-roll?"},
                    ],
                },
                {
                    "title": "Nicknames & Awards",
                    "clues": [
                        {"value": 100, "question": "The regular season's top individual award is abbreviated this way.", "answer": "What is MVP?"},
                        {"value": 200, "question": "Earvin Johnson is far better known by this magical nickname.", "answer": "Who is Magic Johnson?"},
                        {"value": 300, "question": "Hakeem Olajuwon was nicknamed this dreamlike title.", "answer": "What is The Dream?"},
                        {"value": 400, "question": "Giannis Antetokounmpo is often called this nationality-based nickname.", "answer": "What is the Greek Freak?"},
                        {"value": 500, "question": "The NBA's Defensive Player of the Year award honors excellence on this side of the ball.", "answer": "What is defense?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady",
            "categories": [
                {
                    "title": "Pre-Merger Hardwood",
                    "clues": [
                        {"value": 200, "question": "The NBA traces part of its origin to this three-letter league founded in 1946, before its merger with the NBL.", "answer": "What is the BAA, or Basketball Association of America?"},
                        {"value": 400, "question": "Before Los Angeles, the Lakers became a dynasty in this Minnesota city.", "answer": "What is Minneapolis?"},
                        {"value": 600, "question": "The current Sacramento Kings franchise won the 1951 NBA title under this upstate New York name.", "answer": "Who are the Rochester Royals?"},
                        {"value": 800, "question": "The 1955 NBA champion Syracuse Nationals later became this current franchise.", "answer": "Who are the Philadelphia 76ers?"},
                        {"value": 1000, "question": "Before Milwaukee, St. Louis, and Atlanta, the Hawks franchise began with this hyphenated Illinois-Iowa name.", "answer": "Who are the Tri-Cities Blackhawks?"},
                    ],
                },
                {
                    "title": "ABA Ghost Stories",
                    "clues": [
                        {"value": 200, "question": "The ABA was famous for using a basketball with these three colors.", "answer": "What are red, white, and blue?"},
                        {"value": 400, "question": "Julius Erving won two ABA titles with this Nets franchise before the NBA merger.", "answer": "Who are the New York Nets?"},
                        {"value": 600, "question": "Before adopting their current name, the Denver Nuggets played in the ABA under this explosive nickname.", "answer": "Who are the Denver Rockets?"},
                        {"value": 800, "question": "The Spurs, Nets, Nuggets, and Pacers were the four ABA teams absorbed into the NBA in this year.", "answer": "What is 1976?"},
                        {"value": 1000, "question": "Artis Gilmore led this ABA team to the 1975 championship before the franchise folded a year later.", "answer": "Who are the Kentucky Colonels?"},
                    ],
                },
                {
                    "title": "Finals Footnotes",
                    "clues": [
                        {"value": 200, "question": "John Havlicek's famous steal in 1965 came against this Philadelphia team.", "answer": "Who are the 76ers?"},
                        {"value": 400, "question": "In the 1970 Finals, this injured Knicks center limped onto the floor for Game 7 and became instant theater.", "answer": "Who is Willis Reed?"},
                        {"value": 600, "question": "Magic Johnson famously started Game 6 of the 1980 Finals at this position in place of Kareem Abdul-Jabbar.", "answer": "What is center?"},
                        {"value": 800, "question": "The Rockets beat this Eastern Conference team in the 1994 NBA Finals, a series that overlapped the O. J. Simpson chase.", "answer": "Who are the New York Knicks?"},
                        {"value": 1000, "question": "This Suns guard hit the triple-overtime Game 5 shot in the 1976 Finals often called the greatest game ever played.", "answer": "Who is Gar Heard?"},
                    ],
                },
                {
                    "title": "Dynasty Fine Print",
                    "clues": [
                        {"value": 200, "question": "The Celtics won this many consecutive NBA championships from 1959 through 1966.", "answer": "What is eight?"},
                        {"value": 400, "question": "This coach led Showtime Lakers teams to four championships in the 1980s.", "answer": "Who is Pat Riley?"},
                        {"value": 600, "question": "Dennis Rodman joined the Bulls before this season, helping launch the second three-peat.", "answer": "What is 1995-96?"},
                        {"value": 800, "question": "The Bad Boys Pistons won back-to-back titles in these two years.", "answer": "What are 1989 and 1990?"},
                        {"value": 1000, "question": "This Spurs role player won rings with Tim Duncan in 1999, 2003, 2005, and 2007, then returned as a respected assistant coach.", "answer": "Who is Avery Johnson?"},
                    ],
                },
                {
                    "title": "Box Score Goblins",
                    "clues": [
                        {"value": 200, "question": "Wilt Chamberlain's 100-point game was played in this Pennsylvania city, not Philadelphia.", "answer": "What is Hershey?"},
                        {"value": 400, "question": "This Orlando Magic guard set the single-game assist record with 30 in 1990.", "answer": "Who is Scott Skiles?"},
                        {"value": 600, "question": "This Laker set the NBA single-game blocked shots record with 17 in 1973.", "answer": "Who is Elmore Smith?"},
                        {"value": 800, "question": "In 1961-62, Wilt Chamberlain averaged this impossible-looking number of minutes per game.", "answer": "What is 48.5 minutes per game?"},
                        {"value": 1000, "question": "This Detroit Piston scored 13 points in the final 33 seconds of a 2004 game against New Jersey.", "answer": "Who is Tayshaun Prince?"},
                    ],
                },
                {
                    "title": "Draft & Trade Wormholes",
                    "clues": [
                        {"value": 200, "question": "The Trail Blazers selected Sam Bowie one pick before this Bulls legend in the 1984 NBA Draft.", "answer": "Who is Michael Jordan?"},
                        {"value": 400, "question": "The 1980 trade that gave Boston Robert Parish also gave the Celtics the pick used on this Hall of Fame forward.", "answer": "Who is Kevin McHale?"},
                        {"value": 600, "question": "The Hornets drafted Kobe Bryant in 1996 before trading him to this team.", "answer": "Who are the Los Angeles Lakers?"},
                        {"value": 800, "question": "Dirk Nowitzki was drafted by the Milwaukee Bucks in 1998 and immediately traded to this team.", "answer": "Who are the Dallas Mavericks?"},
                        {"value": 1000, "question": "The Hawks drafted Luka Doncic in 2018 and traded him for Trae Young and a future pick from this team.", "answer": "Who are the Dallas Mavericks?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: NBA Historian Mode",
        "question": "This franchise, now in Sacramento, won the 1951 NBA championship while playing in Rochester.",
        "answer": "Who are the Royals, or the Rochester Royals?",
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
    return {"ok": True, "app": "jiporady-nba"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
