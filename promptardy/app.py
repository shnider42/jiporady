from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Jiporady",
    "subtitle": "A bigger, louder, score-tracking Jeopardy-style party board",
    "rounds": {
        "round_1": {
            "name": "Round 1",
            "categories": [
                {
                    "title": "Science & Space",
                    "clues": [
                        {"value": 100, "question": "This planet is famous for its rings.", "answer": "What is Saturn?"},
                        {"value": 200, "question": "The force that keeps planets orbiting stars and keeps your feet on the ground.", "answer": "What is gravity?"},
                        {"value": 300, "question": "This part of the cell contains most of its DNA.", "answer": "What is the nucleus?"},
                        {"value": 400, "question": "The speed of light in a vacuum is about 186,000 of these per second.", "answer": "What are miles?"},
                        {"value": 500, "question": "Named after an Italian physicist, this paradox involves why we have not yet clearly detected extraterrestrial civilizations.", "answer": "What is the Fermi paradox?"},
                    ],
                },
                {
                    "title": "Movies & TV",
                    "clues": [
                        {"value": 100, "question": "This blue-skinned group lives on Pandora in James Cameron's blockbuster franchise.", "answer": "Who are the Na'vi?"},
                        {"value": 200, "question": "The sitcom 'The Office' is set mainly in this Pennsylvania city.", "answer": "What is Scranton?"},
                        {"value": 300, "question": "In 'Breaking Bad,' Walter White starts out teaching this high school subject.", "answer": "What is chemistry?"},
                        {"value": 400, "question": "The 1999 sci-fi film in which Neo learns reality is simulated.", "answer": "What is 'The Matrix'?"},
                        {"value": 500, "question": "This Korean filmmaker directed the Best Picture winner 'Parasite.'", "answer": "Who is Bong Joon-ho?"},
                    ],
                },
                {
                    "title": "Music & Pop Culture",
                    "clues": [
                        {"value": 100, "question": "Taylor Swift started out mainly in this music genre before becoming a pop powerhouse.", "answer": "What is country?"},
                        {"value": 200, "question": "This artist released the album 'Renaissance' in 2022.", "answer": "Who is Beyoncé?"},
                        {"value": 300, "question": "The K-pop group featuring RM, Jin, Suga, j-hope, Jimin, V, and Jung Kook.", "answer": "Who are BTS?"},
                        {"value": 400, "question": "In 2024, this pop star's album 'The Tortured Poets Department' broke major streaming records.", "answer": "Who is Taylor Swift?"},
                        {"value": 500, "question": "The rapper born Aubrey Graham is better known by this stage name.", "answer": "Who is Drake?"},
                    ],
                },
                {
                    "title": "Internet & Tech",
                    "clues": [
                        {"value": 100, "question": "The 'www' in a website stands for this three-word phrase.", "answer": "What is World Wide Web?"},
                        {"value": 200, "question": "This company created the iPhone.", "answer": "What is Apple?"},
                        {"value": 300, "question": "This open-source operating system kernel was created by Linus Torvalds.", "answer": "What is Linux?"},
                        {"value": 400, "question": "In networking, 'HTTP' stands for this.", "answer": "What is Hypertext Transfer Protocol?"},
                        {"value": 500, "question": "This version-control platform, now owned by Microsoft, is where countless developers host repositories.", "answer": "What is GitHub?"},
                    ],
                },
                {
                    "title": "Wordplay",
                    "clues": [
                        {"value": 100, "question": "A word that means the opposite of another word.", "answer": "What is an antonym?"},
                        {"value": 200, "question": "A figure of speech comparing two unlike things using 'like' or 'as.'", "answer": "What is a simile?"},
                        {"value": 300, "question": "A word formed from the first letters of a phrase, like NASA.", "answer": "What is an acronym?"},
                        {"value": 400, "question": "This punctuation mark can show possession or create a contraction.", "answer": "What is an apostrophe?"},
                        {"value": 500, "question": "This 5-letter word can mean either to guide a horse or to reduce spending; spelling stays the same, pronunciation changes.", "answer": "What is rein / reign?"},
                    ],
                },
                {
                    "title": "Odds & Ends",
                    "clues": [
                        {"value": 100, "question": "The largest ocean on Earth.", "answer": "What is the Pacific Ocean?"},
                        {"value": 200, "question": "A standard die has this many total sides.", "answer": "What is 6?"},
                        {"value": 300, "question": "This board game asks you to pass Go and collect $200.", "answer": "What is Monopoly?"},
                        {"value": 400, "question": "The chess piece that can move in an L-shape.", "answer": "What is the knight?"},
                        {"value": 500, "question": "In Roman numerals, this letter represents 500.", "answer": "What is D?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady",
            "categories": [
                {
                    "title": "World History",
                    "clues": [
                        {"value": 200, "question": "This wall came down in 1989, symbolizing the decline of Soviet control in Eastern Europe.", "answer": "What is the Berlin Wall?"},
                        {"value": 400, "question": "This French military leader crowned himself emperor in 1804.", "answer": "Who is Napoleon Bonaparte?"},
                        {"value": 600, "question": "The ship on which the Pilgrims crossed the Atlantic in 1620.", "answer": "What is the Mayflower?"},
                        {"value": 800, "question": "The conflict from 1914 to 1918 that was once called the Great War.", "answer": "What is World War I?"},
                        {"value": 1000, "question": "The 1215 English document often cited as limiting the king's power.", "answer": "What is the Magna Carta?"},
                    ],
                },
                {
                    "title": "Video Games",
                    "clues": [
                        {"value": 200, "question": "Nintendo's mustachioed mascot who often rescues Princess Peach.", "answer": "Who is Mario?"},
                        {"value": 400, "question": "This sandbox game by Mojang lets players build with blocks and fight the Ender Dragon.", "answer": "What is Minecraft?"},
                        {"value": 600, "question": "The legendary sword often wielded by Link in 'The Legend of Zelda.'", "answer": "What is the Master Sword?"},
                        {"value": 800, "question": "This 2023 game by Larian Studios swept many Game of the Year awards and is based on Dungeons & Dragons.", "answer": "What is Baldur's Gate 3?"},
                        {"value": 1000, "question": "The company behind the PlayStation console brand.", "answer": "What is Sony?"},
                    ],
                },
                {
                    "title": "Books & Authors",
                    "clues": [
                        {"value": 200, "question": "She wrote 'Pride and Prejudice.'", "answer": "Who is Jane Austen?"},
                        {"value": 400, "question": "This author created Middle-earth and wrote 'The Hobbit.'", "answer": "Who is J.R.R. Tolkien?"},
                        {"value": 600, "question": "In George Orwell's 'Animal Farm,' this farm animal becomes a dictator-like figure.", "answer": "Who is Napoleon the pig?"},
                        {"value": 800, "question": "This American writer created Captain Ahab and wrote 'Moby-Dick.'", "answer": "Who is Herman Melville?"},
                        {"value": 1000, "question": "The literary term for a story's underlying moral or central idea.", "answer": "What is a theme?"},
                    ],
                },
                {
                    "title": "Sports",
                    "clues": [
                        {"value": 200, "question": "This sport uses terms like birdie, eagle, and bogey.", "answer": "What is golf?"},
                        {"value": 400, "question": "The number of players on the field for one soccer team at a time, including the goalkeeper.", "answer": "What is 11?"},
                        {"value": 600, "question": "This NBA legend was nicknamed 'His Airness.'", "answer": "Who is Michael Jordan?"},
                        {"value": 800, "question": "The trophy awarded to the NHL playoff champion.", "answer": "What is the Stanley Cup?"},
                        {"value": 1000, "question": "In baseball statistics, this abbreviation measures runs batted in.", "answer": "What is RBI?"},
                    ],
                },
                {
                    "title": "Hard Science",
                    "clues": [
                        {"value": 200, "question": "H2O is the chemical formula for this substance.", "answer": "What is water?"},
                        {"value": 400, "question": "This branch of physics studies heat, work, temperature, and energy transfer.", "answer": "What is thermodynamics?"},
                        {"value": 600, "question": "On the pH scale, values below 7 describe substances that are this.", "answer": "What is acidic?"},
                        {"value": 800, "question": "This subatomic particle has a negative electric charge.", "answer": "What is an electron?"},
                        {"value": 1000, "question": "This scientist proposed the uncertainty principle.", "answer": "Who is Werner Heisenberg?"},
                    ],
                },
                {
                    "title": "2000s-2020s Pop Culture",
                    "clues": [
                        {"value": 200, "question": "This HBO fantasy series ended in 2019 after eight seasons.", "answer": "What is 'Game of Thrones'?"},
                        {"value": 400, "question": "The Marvel film event in which many heroes reunite after 'Infinity War.'", "answer": "What is 'Avengers: Endgame'?"},
                        {"value": 600, "question": "This social media app, centered on short-form vertical video, exploded globally in the late 2010s and early 2020s.", "answer": "What is TikTok?"},
                        {"value": 800, "question": "This 2023 film directed by Greta Gerwig turned a Mattel doll into a box office phenomenon.", "answer": "What is 'Barbie'?"},
                        {"value": 1000, "question": "This rapper, born Kendrick Lamar Duckworth, won a Pulitzer Prize for Music for 'DAMN.'", "answer": "Who is Kendrick Lamar?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: Pop Culture + Tech",
        "question": "This 1999 sci-fi film shares its title with a mathematical structure used in computer science and linear algebra; the movie's title was borrowed from a William Gibson term.",
        "answer": "What is 'The Matrix'?"
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