from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Jiporady: Brazilian International Soccer",
    "subtitle": "Seleção magic, World Cup heartbreak, samba-football legends, and an entire Double Jiporady round on David Luiz",
    "rounds": {
        "round_1": {
            "name": "Round 1",
            "categories": [
                {
                    "title": "A Seleção",
                    "clues": [
                        {"value": 100, "question": "Brazil's national soccer team is commonly known by this Portuguese nickname meaning 'the selection.'", "answer": "What is A Seleção?"},
                        {"value": 200, "question": "Brazil usually wears this bright shirt color as its most famous home look.", "answer": "What is yellow?"},
                        {"value": 300, "question": "This bird-inspired nickname, Canarinho, refers to Brazil's yellow-shirted national team.", "answer": "What is the little canary?"},
                        {"value": 400, "question": "Brazil's main soccer federation is commonly abbreviated with these three letters.", "answer": "What is CBF?"},
                        {"value": 500, "question": "Brazil's national team is associated with this Portuguese phrase for beautiful or joyful soccer.", "answer": "What is jogo bonito?"},
                    ],
                },
                {
                    "title": "Copas do Mundo",
                    "clues": [
                        {"value": 100, "question": "Brazil has won this men's tournament more times than any other nation.", "answer": "What is the FIFA World Cup?"},
                        {"value": 200, "question": "Brazil won its first World Cup in 1958 in this Scandinavian country.", "answer": "What is Sweden?"},
                        {"value": 300, "question": "Brazil won the 1970 World Cup in this country, with Pelé, Jairzinho, Tostão, Gérson, and Carlos Alberto starring.", "answer": "What is Mexico?"},
                        {"value": 400, "question": "Brazil's 2002 World Cup win came against this European opponent in the final.", "answer": "Who are Germany?"},
                        {"value": 500, "question": "Brazil hosted the World Cup in 1950 and again in this year.", "answer": "What is 2014?"},
                    ],
                },
                {
                    "title": "Brazilian Icons",
                    "clues": [
                        {"value": 100, "question": "This three-time World Cup winner is often called the King of Football.", "answer": "Who is Pelé?"},
                        {"value": 200, "question": "This striker scored both Brazil goals in the 2002 World Cup final.", "answer": "Who is Ronaldo?"},
                        {"value": 300, "question": "This free-smiling Barcelona star won the 2002 World Cup and the 2005 Ballon d'Or.", "answer": "Who is Ronaldinho?"},
                        {"value": 400, "question": "This left back was famous for rocket free kicks and wore No. 6 for Brazil.", "answer": "Who is Roberto Carlos?"},
                        {"value": 500, "question": "This modern Brazil star wears No. 10 and became the country's all-time leading men's scorer by official count.", "answer": "Who is Neymar?"},
                    ],
                },
                {
                    "title": "Gols e Momentos",
                    "clues": [
                        {"value": 100, "question": "This captain scored Brazil's famous sweeping team goal to seal the 1970 World Cup final.", "answer": "Who is Carlos Alberto?"},
                        {"value": 200, "question": "This goalkeeper's saves helped Brazil win the 1994 World Cup final shootout against Italy.", "answer": "Who is Cláudio Taffarel?"},
                        {"value": 300, "question": "This Italian striker sent the decisive 1994 World Cup final penalty over the bar.", "answer": "Who is Roberto Baggio?"},
                        {"value": 400, "question": "Ronaldo's redemption World Cup came in this year after the mystery and disappointment of 1998.", "answer": "What is 2002?"},
                        {"value": 500, "question": "Brazil's 2014 World Cup semifinal loss to Germany is remembered by this shocking scoreline.", "answer": "What is 7-1?"},
                    ],
                },
                {
                    "title": "Rivals & Villains",
                    "clues": [
                        {"value": 100, "question": "Brazil's fiercest South American soccer rival wears sky blue and white stripes.", "answer": "Who are Argentina?"},
                        {"value": 200, "question": "Uruguay's 1950 upset of Brazil at the Maracanã is remembered by this one-word nickname.", "answer": "What is the Maracanazo?"},
                        {"value": 300, "question": "This European nation beat Brazil in the 1998 World Cup final.", "answer": "Who are France?"},
                        {"value": 400, "question": "This Dutch team eliminated Brazil from the 2010 World Cup.", "answer": "Who are the Netherlands?"},
                        {"value": 500, "question": "This Belgian team knocked Brazil out of the 2018 World Cup quarterfinals.", "answer": "Who are Belgium?"},
                    ],
                },
                {
                    "title": "Positions in Portuguese",
                    "clues": [
                        {"value": 100, "question": "In Portuguese, 'goleiro' is this position.", "answer": "What is goalkeeper?"},
                        {"value": 200, "question": "In Portuguese, 'zagueiro' is this defensive position.", "answer": "What is center back?"},
                        {"value": 300, "question": "In Portuguese, 'lateral' is usually this wide defensive role.", "answer": "What is fullback?"},
                        {"value": 400, "question": "In Portuguese, 'meia' is usually this midfield role.", "answer": "What is midfielder?"},
                        {"value": 500, "question": "In Portuguese, 'atacante' is this attacking role.", "answer": "What is forward or striker?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady",
            "categories": [
                {
                    "title": "David Luiz: Seleção",
                    "clues": [
                        {"value": 200, "question": "David Luiz played this position for Brazil, usually in the middle of the back line.", "answer": "What is center back?"},
                        {"value": 400, "question": "David Luiz was part of Brazil's squad that won this 2013 FIFA tournament on home soil.", "answer": "What is the FIFA Confederations Cup?"},
                        {"value": 600, "question": "In the 2014 World Cup quarterfinal against Colombia, David Luiz scored with this kind of set-piece strike.", "answer": "What is a free kick?"},
                        {"value": 800, "question": "With Thiago Silva suspended, David Luiz captained Brazil in this infamous 2014 World Cup semifinal.", "answer": "What is Brazil's 7-1 loss to Germany?"},
                        {"value": 1000, "question": "David Luiz and this PSG teammate were Brazil's first-choice center-back pairing for much of the 2014 World Cup.", "answer": "Who is Thiago Silva?"},
                    ],
                },
                {
                    "title": "David Luiz: Club Trail",
                    "clues": [
                        {"value": 200, "question": "David Luiz developed professionally in Brazil with this Salvador-based club before moving to Europe.", "answer": "What is Vitória?"},
                        {"value": 400, "question": "This Portuguese club brought David Luiz to Europe before his first Chelsea move.", "answer": "What is Benfica?"},
                        {"value": 600, "question": "David Luiz won the 2011-12 Champions League with this English club.", "answer": "What is Chelsea?"},
                        {"value": 800, "question": "David Luiz moved from Chelsea to this Paris club in 2014 for a huge defender transfer fee.", "answer": "What is Paris Saint-Germain?"},
                        {"value": 1000, "question": "After returning to England with Chelsea, David Luiz later crossed London to this club in 2019.", "answer": "What is Arsenal?"},
                    ],
                },
                {
                    "title": "David Luiz: Hair & Chaos",
                    "clues": [
                        {"value": 200, "question": "David Luiz is instantly recognizable for this big, curly feature.", "answer": "What is his hair?"},
                        {"value": 400, "question": "Because of his hair and position, fans often compared David Luiz to this Simpsons character.", "answer": "Who is Sideshow Bob?"},
                        {"value": 600, "question": "David Luiz's adventurous style made him famous for stepping out of defense into this phase of play.", "answer": "What is the attack, or midfield build-up?"},
                        {"value": 800, "question": "David Luiz's long-range shooting and set pieces made him unusually dangerous for this position.", "answer": "What is center back?"},
                        {"value": 1000, "question": "His highlight reel swings between brilliant diagonals, free kicks, and this less flattering defensive meme category.", "answer": "What are mistakes, errors, or chaos defending?"},
                    ],
                },
                {
                    "title": "David Luiz: London Nights",
                    "clues": [
                        {"value": 200, "question": "David Luiz's first Chelsea spell included a Champions League final win over this German club in its own stadium.", "answer": "Who are Bayern Munich?"},
                        {"value": 400, "question": "Chelsea beat this Portuguese club in the 2013 Europa League final with David Luiz in the squad.", "answer": "Who are Benfica?"},
                        {"value": 600, "question": "David Luiz returned to Chelsea in 2016 under this Italian manager.", "answer": "Who is Antonio Conte?"},
                        {"value": 800, "question": "During Chelsea's 2016-17 title season, David Luiz often played in the center of this back-line shape.", "answer": "What is a back three, or three-at-the-back?"},
                        {"value": 1000, "question": "David Luiz won the 2018-19 Europa League final with Chelsea against this London rival he would soon join.", "answer": "Who are Arsenal?"},
                    ],
                },
                {
                    "title": "David Luiz: PSG Chapter",
                    "clues": [
                        {"value": 200, "question": "At PSG, David Luiz played alongside this Swedish superstar striker.", "answer": "Who is Zlatan Ibrahimović?"},
                        {"value": 400, "question": "At PSG, David Luiz often reunited with this Brazil center-back partner from the national team.", "answer": "Who is Thiago Silva?"},
                        {"value": 600, "question": "In 2015, David Luiz scored a Champions League knockout goal for PSG against this former club.", "answer": "Who are Chelsea?"},
                        {"value": 800, "question": "Barcelona's Luis Suárez famously nutmegged David Luiz during this European competition.", "answer": "What is the UEFA Champions League?"},
                        {"value": 1000, "question": "David Luiz's PSG years placed him in this French top-flight league.", "answer": "What is Ligue 1?"},
                    ],
                },
                {
                    "title": "David Luiz: Receipts",
                    "clues": [
                        {"value": 200, "question": "David Luiz shares this first name with a Biblical king, though his surname is spelled Luiz.", "answer": "What is David?"},
                        {"value": 400, "question": "David Luiz was born in this country.", "answer": "What is Brazil?"},
                        {"value": 600, "question": "David Luiz was born in this São Paulo state city, also known as a large industrial suburb.", "answer": "What is Diadema?"},
                        {"value": 800, "question": "David Luiz returned to Brazilian club football with this Rio de Janeiro giant in 2021.", "answer": "What is Flamengo?"},
                        {"value": 1000, "question": "Although famous as David Luiz, his full name includes these two surnames after David Luiz.", "answer": "What is Moreira Marinho?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: David Luiz at the World Cup",
        "question": "David Luiz scored a memorable long-range free kick for Brazil against this opponent in the 2014 World Cup quarterfinal.",
        "answer": "Who are Colombia?",
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
    return {"ok": True, "app": "jiporady-brazil-soccer"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
