from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Jiporady: Heavy Metal 1970–1996",
    "subtitle": "From Black Sabbath's first thunderclap to the rise of Gothenburg metal — classic bands, landmark albums, lineups, riffs, mascots, and legendary stages.",
    "rounds": {
        "round_1": {
            "name": "Round 1: Raise the Horns",
            "categories": [
                {
                    "title": "Founding Fathers",
                    "clues": [
                        {"value": 100, "question": "This Birmingham band released its self-titled debut on February 13, 1970, a date often treated as heavy metal's birthday.", "answer": "Who are Black Sabbath?"},
                        {"value": 200, "question": "This Black Sabbath guitarist lost the tips of two fingers in a factory accident but developed a massive, down-tuned sound anyway.", "answer": "Who is Tony Iommi?"},
                        {"value": 300, "question": "Rob Halford is the leather-clad lead singer of this British band.", "answer": "Who are Judas Priest?"},
                        {"value": 400, "question": "After leaving Black Sabbath, Ozzy Osbourne launched a solo career with this 1980 album featuring Randy Rhoads.", "answer": "What is Blizzard of Ozz?"},
                        {"value": 500, "question": "Ronnie James Dio replaced Ozzy in Black Sabbath and debuted with the band on this 1980 album.", "answer": "What is Heaven and Hell?"},
                    ],
                },
                {
                    "title": "Up the Irons",
                    "clues": [
                        {"value": 100, "question": "This undead mascot appears on nearly every Iron Maiden album cover and at the band's concerts.", "answer": "Who is Eddie?"},
                        {"value": 200, "question": "This singer joined Iron Maiden for 1982's 'The Number of the Beast.'", "answer": "Who is Bruce Dickinson?"},
                        {"value": 300, "question": "This bassist founded Iron Maiden and remains the band's primary songwriter.", "answer": "Who is Steve Harris?"},
                        {"value": 400, "question": "This 1984 Iron Maiden album includes 'Aces High,' '2 Minutes to Midnight,' and 'Rime of the Ancient Mariner.'", "answer": "What is Powerslave?"},
                        {"value": 500, "question": "Before Bruce Dickinson, this singer performed on Iron Maiden's first two studio albums.", "answer": "Who is Paul Di'Anno?"},
                    ],
                },
                {
                    "title": "The Big Four",
                    "clues": [
                        {"value": 100, "question": "Metallica, Megadeth, Slayer, and this New York band make up thrash metal's Big Four.", "answer": "Who are Anthrax?"},
                        {"value": 200, "question": "This Metallica frontman sings and plays rhythm guitar on 'Master of Puppets.'", "answer": "Who is James Hetfield?"},
                        {"value": 300, "question": "Dave Mustaine founded this band after leaving Metallica.", "answer": "Who are Megadeth?"},
                        {"value": 400, "question": "This Slayer album opens with 'Angel of Death' and ends with 'Raining Blood.'", "answer": "What is Reign in Blood?"},
                        {"value": 500, "question": "This Anthrax album includes 'Caught in a Mosh' and 'Indians.'", "answer": "What is Among the Living?"},
                    ],
                },
                {
                    "title": "Albums That Built Metal",
                    "clues": [
                        {"value": 100, "question": "This 1970 Black Sabbath album contains 'War Pigs,' 'Iron Man,' and its urgent title track.", "answer": "What is Paranoid?"},
                        {"value": 200, "question": "Judas Priest's 1980 album containing 'Breaking the Law' and 'Living After Midnight' has this industrial title.", "answer": "What is British Steel?"},
                        {"value": 300, "question": "Metallica's 1986 album includes 'Battery,' 'Disposable Heroes,' and its title track.", "answer": "What is Master of Puppets?"},
                        {"value": 400, "question": "Megadeth's 1990 album includes 'Holy Wars... The Punishment Due' and 'Hangar 18.'", "answer": "What is Rust in Peace?"},
                        {"value": 500, "question": "This 1992 Pantera album includes 'Walk,' 'Mouth for War,' and 'This Love.'", "answer": "What is Vulgar Display of Power?"},
                    ],
                },
                {
                    "title": "Faces of Metal",
                    "clues": [
                        {"value": 100, "question": "Megadeth's skeletal mascot, usually shown with metal restraints over his senses, has this name.", "answer": "Who is Vic Rattlehead?"},
                        {"value": 200, "question": "Motörhead's fanged, tusked mascot is commonly known by this one-word name.", "answer": "Who is Snaggletooth, or the War-Pig?"},
                        {"value": 300, "question": "Anthrax's cartoon mascot with a bald head and a grin is known by this negative-sounding name.", "answer": "Who is the Not Man?"},
                        {"value": 400, "question": "This artist created many classic Iron Maiden covers and designed Eddie's best-known 1980s appearances.", "answer": "Who is Derek Riggs?"},
                        {"value": 500, "question": "Dio popularized this two-fingered hand gesture in metal, derived from the Italian 'mano cornuta.'", "answer": "What are the devil horns, or metal horns?"},
                    ],
                },
                {
                    "title": "Live and Loud",
                    "clues": [
                        {"value": 100, "question": "Metallica played a massive 1991 Monsters of Rock concert at Tushino Airfield in this city.", "answer": "What is Moscow?"},
                        {"value": 200, "question": "Iron Maiden's 'Live After Death' was recorded mainly at this California arena.", "answer": "What is Long Beach Arena?"},
                        {"value": 300, "question": "Judas Priest's first live album, 'Unleashed in the East,' was recorded in this country.", "answer": "What is Japan?"},
                        {"value": 400, "question": "The original Black Sabbath lineup briefly reunited at this giant 1985 charity concert.", "answer": "What is Live Aid?"},
                        {"value": 500, "question": "The first Monsters of Rock festival was held in 1980 at Castle Donington in this country.", "answer": "What is England, or the United Kingdom?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady: Deeper Cuts",
            "categories": [
                {
                    "title": "NWOBHM Roll Call",
                    "clues": [
                        {"value": 200, "question": "This acronym names the late-1970s and early-1980s movement that launched Iron Maiden, Saxon, and Diamond Head.", "answer": "What is NWOBHM, or the New Wave of British Heavy Metal?"},
                        {"value": 400, "question": "Metallica later covered 'Am I Evil?' by this NWOBHM band.", "answer": "Who are Diamond Head?"},
                        {"value": 600, "question": "This band's 1980 album 'Wheels of Steel' includes '747 (Strangers in the Night).'", "answer": "Who are Saxon?"},
                        {"value": 800, "question": "Metallica later covered 'The Small Hours' by this Scottish NWOBHM band, whose 1981 album was 'The Nightcomers.'", "answer": "Who are Holocaust?"},
                        {"value": 1000, "question": "This Newcastle band released 'Welcome to Hell' in 1981 and an album called 'Black Metal' in 1982.", "answer": "Who are Venom?"},
                    ],
                },
                {
                    "title": "Thrash Lineup Lab",
                    "clues": [
                        {"value": 200, "question": "This bassist played on Metallica's first three albums before his death in 1986.", "answer": "Who is Cliff Burton?"},
                        {"value": 400, "question": "This guitarist joined Megadeth for 'Rust in Peace' and stayed through 1994's 'Youthanasia.'", "answer": "Who is Marty Friedman?"},
                        {"value": 600, "question": "Anthrax drummer Charlie Benante is the uncle of this longtime Anthrax bassist.", "answer": "Who is Frank Bello?"},
                        {"value": 800, "question": "This drummer's double-bass assault powered Slayer's classic run including 'Reign in Blood.'", "answer": "Who is Dave Lombardo?"},
                        {"value": 1000, "question": "This lead guitarist played on Megadeth's 'Peace Sells... But Who's Buying?' before Marty Friedman joined years later.", "answer": "Who is Chris Poland?"},
                    ],
                },
                {
                    "title": "The Gothenburg Spark",
                    "clues": [
                        {"value": 200, "question": "In Flames formed in 1990 in this Swedish city, which gave its name to a melodic death-metal sound.", "answer": "What is Gothenburg?"},
                        {"value": 400, "question": "This was the title of In Flames' 1994 debut album.", "answer": "What is Lunar Strain?"},
                        {"value": 600, "question": "In Flames released this jester-themed studio album in 1996.", "answer": "What is The Jester Race?"},
                        {"value": 800, "question": "Before becoming In Flames' singer, Anders Fridén fronted this fellow Gothenburg band.", "answer": "Who are Dark Tranquillity?"},
                        {"value": 1000, "question": "This vocalist from Dark Tranquillity sang on In Flames' 'Lunar Strain' before Anders Fridén joined.", "answer": "Who is Mikael Stanne?"},
                    ],
                },
                {
                    "title": "Behind the Boards",
                    "clues": [
                        {"value": 200, "question": "This producer's long Iron Maiden run began with 'Killers' and ended with 'Fear of the Dark.'", "answer": "Who is Martin Birch?"},
                        {"value": 400, "question": "This producer gave Metallica's 1991 self-titled album its fuller, more streamlined sound.", "answer": "Who is Bob Rock?"},
                        {"value": 600, "question": "This producer worked on Pantera's 'Cowboys from Hell,' 'Vulgar Display of Power,' and 'Far Beyond Driven.'", "answer": "Who is Terry Date?"},
                        {"value": 800, "question": "Slayer recorded 'Reign in Blood' with this producer, better known at the time for hip-hop.", "answer": "Who is Rick Rubin?"},
                        {"value": 1000, "question": "This Danish producer engineered and produced Metallica's 'Ride the Lightning,' 'Master of Puppets,' and '...And Justice for All.'", "answer": "Who is Flemming Rasmussen?"},
                    ],
                },
                {
                    "title": "Concert Archaeology",
                    "clues": [
                        {"value": 200, "question": "Rainbow headlined the inaugural 1980 Monsters of Rock festival at this English venue.", "answer": "What is Castle Donington, or Donington Park?"},
                        {"value": 400, "question": "The final side of Iron Maiden's 'Live After Death' was recorded at this London venue.", "answer": "What is Hammersmith Odeon?"},
                        {"value": 600, "question": "Metallica's 1991 Moscow show took place during this touring festival brand.", "answer": "What is Monsters of Rock?"},
                        {"value": 800, "question": "The 1991 North American 'Clash of the Titans' tour united Slayer, Megadeth, Anthrax, and this then-rising Seattle band.", "answer": "Who are Alice in Chains?"},
                        {"value": 1000, "question": "Iron Maiden's year-long 1984–85 tour that produced most of 'Live After Death' had this slavery-themed name.", "answer": "What is the World Slavery Tour?"},
                    ],
                },
                {
                    "title": "Metal Mutates: 1990–96",
                    "clues": [
                        {"value": 200, "question": "Pantera's 1990 major-label breakthrough album introduced the title phrase 'Cowboys from' this fiery place.", "answer": "What is Hell?"},
                        {"value": 400, "question": "Sepultura's 1993 album that mixed thrash, groove, and tribal influence used this abbreviated title.", "answer": "What is Chaos A.D.?"},
                        {"value": 600, "question": "Machine Head's 1994 debut album has this command-like title.", "answer": "What is Burn My Eyes?"},
                        {"value": 800, "question": "Fear Factory's 1995 concept album about conflict between humanity and machines has this manufacturing-themed title.", "answer": "What is Demanufacture?"},
                        {"value": 1000, "question": "Carcass's 1993 melodic death-metal landmark has this cardiac title.", "answer": "What is Heartwork?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: Castle Donington",
        "question": "Led by former Deep Purple guitarist Ritchie Blackmore, this band headlined the inaugural Monsters of Rock festival in 1980 over Judas Priest, Scorpions, and Saxon.",
        "answer": "Who are Rainbow?",
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
    return {"ok": True, "app": "jiporady-heavy-metal-1970-1996"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
