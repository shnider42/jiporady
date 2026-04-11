from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Avenged Sevenfold Jiporady",
    "subtitle": "What is... a little piece of trivia?",
    "rounds": {
        "round_1": {
            "name": "Round 1",
            "categories": [
                {
                    "title": "Band Members",
                    "clues": [
                        {"value": 100, "question": "This frontman of Avenged Sevenfold is known by the stage name M. Shadows.", "answer": "Who is Matt Sanders?"},
                        {"value": 200, "question": "This lead guitarist is known for his flashy solos and the stage name Synyster Gates.", "answer": "Who is Brian Haner Jr.?"},
                        {"value": 300, "question": "This rhythm guitarist and backing vocalist goes by the name Zacky Vengeance.", "answer": "Who is Zachary Baker?"},
                        {"value": 400, "question": "This bassist, one of the longest-running members of the band, uses the stage name Johnny Christ.", "answer": "Who is Jonathan Seward?"},
                        {"value": 500, "question": "This original drummer, whose death in 2009 deeply affected the band, was nicknamed The Rev.", "answer": "Who is Jimmy Sullivan?"},
                    ],
                },
                {
                    "title": "Albums",
                    "clues": [
                        {"value": 100, "question": "This 2005 album helped launch the band into the mainstream with songs like 'Bat Country.'", "answer": "What is City of Evil?"},
                        {"value": 200, "question": "This self-titled 2007 album includes 'Almost Easy' and 'Afterlife.'", "answer": "What is Avenged Sevenfold?"},
                        {"value": 300, "question": "Released in 2010, this album featured Mike Portnoy on drums after The Rev's death.", "answer": "What is Nightmare?"},
                        {"value": 400, "question": "This 2013 album shares its title with one of the band's biggest arena-ready singles.", "answer": "What is Hail to the King?"},
                        {"value": 500, "question": "This 2023 album shortened to LIBAD pushed the band into more experimental territory.", "answer": "What is Life Is But a Dream...?"},
                    ],
                },
                {
                    "title": "Song Titles",
                    "clues": [
                        {"value": 100, "question": "This breakthrough single from City of Evil shares its title with a place associated with Hunter S. Thompson-inspired chaos.", "answer": "What is Bat Country?"},
                        {"value": 200, "question": "This fan-favorite song from the self-titled album deals with death and the afterlife.", "answer": "What is Afterlife?"},
                        {"value": 300, "question": "This dramatic title track opens the 2010 album of the same name.", "answer": "What is Nightmare?"},
                        {"value": 400, "question": "This song begins with the words 'He who makes a beast out of himself' in concert intros and on record.", "answer": "What is Bat Country?"},
                        {"value": 500, "question": "This song title asks a question about moral decay and appears on Waking the Fallen.", "answer": "What is Unholy Confessions?"},
                    ],
                },
                {
                    "title": "Stage Names",
                    "clues": [
                        {"value": 100, "question": "Matt Sanders performs under this stage name.", "answer": "Who is M. Shadows?"},
                        {"value": 200, "question": "Brian Haner Jr. performs under this stage name.", "answer": "Who is Synyster Gates?"},
                        {"value": 300, "question": "Zachary Baker performs under this stage name.", "answer": "Who is Zacky Vengeance?"},
                        {"value": 400, "question": "Jonathan Seward performs under this stage name.", "answer": "Who is Johnny Christ?"},
                        {"value": 500, "question": "Jimmy Sullivan performed under this stage name.", "answer": "Who is The Rev?"},
                    ],
                },
                {
                    "title": "Early Era A7X",
                    "clues": [
                        {"value": 100, "question": "This 2001 debut album showed the band's more metalcore-influenced early sound.", "answer": "What is Sounding the Seventh Trumpet?"},
                        {"value": 200, "question": "This 2003 album is often considered a major early classic and features 'Unholy Confessions.'", "answer": "What is Waking the Fallen?"},
                        {"value": 300, "question": "Before the polished hard rock of later years, the band was more closely associated with this heavy subgenre.", "answer": "What is metalcore?"},
                        {"value": 400, "question": "The band's name Avenged Sevenfold was inspired by a story from this book of the Bible.", "answer": "What is Genesis?"},
                        {"value": 500, "question": "The title of their debut album references this trumpet-heavy, apocalyptic book of the Bible.", "answer": "What is Revelation?"},
                    ],
                },
                {
                    "title": "Big Songs",
                    "clues": [
                        {"value": 100, "question": "This 2013 title track became one of the band's signature modern songs.", "answer": "What is Hail to the King?"},
                        {"value": 200, "question": "This song from the self-titled album is known for its orchestral touches and guitar duel feel.", "answer": "What is Afterlife?"},
                        {"value": 300, "question": "This energetic single from the self-titled album begins with a pounding drum groove.", "answer": "What is Almost Easy?"},
                        {"value": 400, "question": "This emotional 2010 single became one of the band's best-known songs after The Rev's passing.", "answer": "What is So Far Away?"},
                        {"value": 500, "question": "This song from City of Evil tells a dark story involving a violent showdown and a doomed narrator.", "answer": "What is M.I.A.?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady",
            "categories": [
                {
                    "title": "Nightmare Era",
                    "clues": [
                        {"value": 200, "question": "This drummer from Dream Theater played on Nightmare as a tribute after The Rev's death.", "answer": "Who is Mike Portnoy?"},
                        {"value": 400, "question": "This ballad from Nightmare was written in memory of The Rev.", "answer": "What is So Far Away?"},
                        {"value": 600, "question": "This title track from Nightmare became one of the band's heaviest and most recognizable singles.", "answer": "What is Nightmare?"},
                        {"value": 800, "question": "This Nightmare song title sounds like a heavenly phrase but is paired with dark, pounding riffs.", "answer": "What is Welcome to the Family?"},
                        {"value": 1000, "question": "This member of Avenged Sevenfold's family, not a permanent band member, handled drums for Nightmare in the studio and touring era immediately after.", "answer": "Who is Mike Portnoy?"},
                    ],
                },
                {
                    "title": "Album by Clue",
                    "clues": [
                        {"value": 200, "question": "Bat Country, Beast and the Harlot, and Seize the Day all appear on this album.", "answer": "What is City of Evil?"},
                        {"value": 400, "question": "Almost Easy, Critical Acclaim, and Dear God appear on this album.", "answer": "What is Avenged Sevenfold?"},
                        {"value": 600, "question": "The Stage, Paradigm, and Exist appear on this album.", "answer": "What is The Stage?"},
                        {"value": 800, "question": "Shepherd of Fire, This Means War, and Coming Home appear on this album.", "answer": "What is Hail to the King?"},
                        {"value": 1000, "question": "Game Over, Nobody, and Cosmic appear on this album.", "answer": "What is Life Is But a Dream...?"},
                    ],
                },
                {
                    "title": "Drummers",
                    "clues": [
                        {"value": 200, "question": "This original Avenged Sevenfold drummer was known for his songwriting contributions as well as his drumming.", "answer": "Who is The Rev?"},
                        {"value": 400, "question": "This famous progressive metal drummer helped the band complete Nightmare.", "answer": "Who is Mike Portnoy?"},
                        {"value": 600, "question": "This drummer became the band's longer-term live and studio drummer beginning in the 2010s.", "answer": "Who is Brooks Wackerman?"},
                        {"value": 800, "question": "Before joining Avenged Sevenfold, Brooks Wackerman had been associated with punk and rock acts like this band fronted by Dexter Holland.", "answer": "What is The Offspring?"},
                        {"value": 1000, "question": "The death of this drummer in 2009 was a turning point in the band's history.", "answer": "Who is Jimmy 'The Rev' Sullivan?"},
                    ],
                },
                {
                    "title": "The Stage & Beyond",
                    "clues": [
                        {"value": 200, "question": "This 2016 album took the band's sound in a more progressive and science-focused direction.", "answer": "What is The Stage?"},
                        {"value": 400, "question": "This nearly 16-minute closing track on The Stage is one of the band's longest songs.", "answer": "What is Exist?"},
                        {"value": 600, "question": "This album arrived unexpectedly in late 2016 with very little traditional rollout.", "answer": "What is The Stage?"},
                        {"value": 800, "question": "This 2023 single from Life Is But a Dream...? was notable for its surreal video and Grammy attention.", "answer": "What is Nobody?"},
                        {"value": 1000, "question": "This word best describes the sonic leap from straightforward Hail to the King riffs to the more adventurous sound of The Stage and LIBAD.", "answer": "What is experimental?"},
                    ],
                },
                {
                    "title": "Tangential but Fair",
                    "clues": [
                        {"value": 200, "question": "This video game franchise famously featured Avenged Sevenfold songs and even band-related content in Zombies mode.", "answer": "What is Call of Duty?"},
                        {"value": 400, "question": "This sport's video-game style, over-the-top anthem energy fits songs like 'Hail to the King' and 'Nightmare' especially well.", "answer": "What is football?"},
                        {"value": 600, "question": "This holiday, often associated with skulls and darker aesthetics, feels especially on-brand for many Avenged Sevenfold visuals.", "answer": "What is Halloween?"},
                        {"value": 800, "question": "This classic literary and philosophical topic, dealing with mortality and meaning, became especially central on Life Is But a Dream... .", "answer": "What is existentialism?"},
                        {"value": 1000, "question": "This one-word symbol, a winged skull, is perhaps the most recognizable visual icon associated with the band.", "answer": "What is the Deathbat?"},
                    ],
                },
                {
                    "title": "Lyrics? No, Titles",
                    "clues": [
                        {"value": 200, "question": "This song title sounds like the opposite of a sacred admission and became one of the band's early calling cards.", "answer": "What is Unholy Confessions?"},
                        {"value": 400, "question": "This title track invites the listener into a dark dreamscape on the 2010 album.", "answer": "What is Nightmare?"},
                        {"value": 600, "question": "This song title from Hail to the King sounds like a medieval military role.", "answer": "What is Shepherd of Fire?"},
                        {"value": 800, "question": "This title from The Stage refers both to performance and to a place where cosmic questions unfold.", "answer": "What is The Stage?"},
                        {"value": 1000, "question": "This 2023 song title suggests a vast emotional or astronomical scale and became a standout fan favorite.", "answer": "What is Cosmic?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: Avenged Sevenfold History",
        "question": "This drummer, known as The Rev, was an original member of Avenged Sevenfold and remained a defining creative force until his death in 2009.",
        "answer": "Who is Jimmy Sullivan?"
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