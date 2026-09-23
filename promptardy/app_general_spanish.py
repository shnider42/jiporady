"""General trivia: 60 clues, eight in Spanish, plus Final Jiporady."""
from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {'title': 'Jiporady: A Little of Everything',
 'subtitle': 'General trivia with a little español. Answers in either language count.',
 'rounds': {'round_1': {'name': 'Round 1',
                        'categories': [{'title': 'Passport, Please',
                                        'clues': [{'value': 100,
                                                   'question': 'The Eiffel Tower stands in this European '
                                                               'capital.',
                                                   'answer': 'What is Paris?'},
                                                  {'value': 200,
                                                   'question': '¿En qué país están las ciudades de Madrid y '
                                                               'Barcelona?',
                                                   'answer': 'España / Spain — English clue: In which '
                                                             'country are Madrid and Barcelona?'},
                                                  {'value': 300,
                                                   'question': 'The pyramids of Giza stand in this country.',
                                                   'answer': 'What is Egypt?'},
                                                  {'value': 400,
                                                   'question': 'This Italian city is famous for canals and '
                                                               'gondolas.',
                                                   'answer': 'What is Venice?'},
                                                  {'value': 500,
                                                   'question': 'This mountain range forms much of the border '
                                                               'between France and Spain.',
                                                   'answer': 'What are the Pyrenees?'}]},
                                       {'title': 'Snack Attack',
                                        'clues': [{'value': 100,
                                                   'question': 'Guacamole gets its green color from this '
                                                               'main ingredient.',
                                                   'answer': 'What is avocado?'},
                                                  {'value': 200,
                                                   'question': 'This Japanese dish pairs vinegared rice with '
                                                               'ingredients that can include fish or '
                                                               'vegetables.',
                                                   'answer': 'What is sushi?'},
                                                  {'value': 300,
                                                   'question': '¿Qué fruta se usa para hacer el vino '
                                                               'tradicional?',
                                                   'answer': 'La uva / Grapes — English clue: Which fruit is '
                                                             'used to make traditional wine?'},
                                                  {'value': 400,
                                                   'question': 'Chickpeas and tahini are the main '
                                                               'ingredients in this Middle Eastern dip.',
                                                   'answer': 'What is hummus?'},
                                                  {'value': 500,
                                                   'question': 'This spice, made from flower stigmas, gives '
                                                               'many paellas their golden color.',
                                                   'answer': 'What is saffron?'}]},
                                       {'title': 'Animal House',
                                        'clues': [{'value': 100,
                                                   'question': 'This black-and-white bear is famous for '
                                                               'eating bamboo.',
                                                   'answer': 'What is the giant panda?'},
                                                  {'value': 200,
                                                   'question': 'A caterpillar becomes a butterfly through '
                                                               'this transformation process.',
                                                   'answer': 'What is metamorphosis?'},
                                                  {'value': 300,
                                                   'question': 'A group of these big cats is called a pride.',
                                                   'answer': 'What are lions?'},
                                                  {'value': 400,
                                                   'question': '¿Qué mamífero pone huevos y tiene un pico '
                                                               'parecido al de un pato?',
                                                   'answer': 'El ornitorrinco / The platypus — English clue: '
                                                             'Which mammal lays eggs and has a duck-like '
                                                             'bill?'},
                                                  {'value': 500,
                                                   'question': 'Sharks have skeletons made primarily of this '
                                                               'flexible material instead of bone.',
                                                   'answer': 'What is cartilage?'}]},
                                       {'title': 'Movie Night',
                                        'clues': [{'value': 100,
                                                   'question': 'In Toy Story, this cowboy toy is best '
                                                               'friends with Buzz Lightyear.',
                                                   'answer': 'Who is Woody?'},
                                                  {'value': 200,
                                                   'question': 'This 1993 dinosaur movie introduced '
                                                               'audiences to a theme park with some very '
                                                               'serious fencing problems.',
                                                   'answer': 'What is Jurassic Park?'},
                                                  {'value': 300,
                                                   'question': 'In The Wizard of Oz, Dorothy follows a road '
                                                               'made of bricks of this color.',
                                                   'answer': 'What is yellow?'},
                                                  {'value': 400,
                                                   'question': 'This actor played both Indiana Jones and Han '
                                                               'Solo.',
                                                   'answer': 'Who is Harrison Ford?'},
                                                  {'value': 500,
                                                   'question': 'In Back to the Future, the DeLorean must '
                                                               'reach this speed in miles per hour to time '
                                                               'travel.',
                                                   'answer': 'What is 88?'}]},
                                       {'title': 'Everyday Science',
                                        'clues': [{'value': 100,
                                                   'question': '¿Qué planeta es conocido como el planeta '
                                                               'rojo?',
                                                   'answer': 'Marte / Mars — English clue: Which planet is '
                                                             'known as the red planet?'},
                                                  {'value': 200,
                                                   'question': 'This gas in the air is essential for human '
                                                               'breathing.',
                                                   'answer': 'What is oxygen?'},
                                                  {'value': 300,
                                                   'question': 'Water changing from a liquid to a gas at its '
                                                               'surface is called this.',
                                                   'answer': 'What is evaporation?'},
                                                  {'value': 400,
                                                   'question': 'This pigment helps plants absorb light and '
                                                               'gives leaves their green color.',
                                                   'answer': 'What is chlorophyll?'},
                                                  {'value': 500,
                                                   'question': 'This effect makes an ambulance siren seem to '
                                                               'change pitch as it passes you.',
                                                   'answer': 'What is the Doppler effect?'}]},
                                       {'title': 'Game Drawer',
                                        'clues': [{'value': 100,
                                                   'question': 'In this game, players shout its name when '
                                                               'they have only one card left.',
                                                   'answer': 'What is Uno?'},
                                                  {'value': 200,
                                                   'question': 'In chess, this piece moves diagonally any '
                                                               'number of unobstructed squares.',
                                                   'answer': 'What is the bishop?'},
                                                  {'value': 300,
                                                   'question': 'A standard deck of playing cards has this '
                                                               'many cards, excluding jokers.',
                                                   'answer': 'What is 52?'},
                                                  {'value': 400,
                                                   'question': 'In Scrabble, Q and this other letter are '
                                                               'each worth 10 points in the standard English '
                                                               'edition.',
                                                   'answer': 'What is Z?'},
                                                  {'value': 500,
                                                   'question': 'In Clue, the solution combines a suspect, a '
                                                               'weapon, and one of these locations.',
                                                   'answer': 'What is a room?'}]}]},
            'round_2': {'name': 'Double Jiporady',
                        'categories': [{'title': 'Map Without Labels',
                                        'clues': [{'value': 200,
                                                   'question': 'This imaginary line divides Earth into the '
                                                               'Northern and Southern Hemispheres.',
                                                   'answer': 'What is the equator?'},
                                                  {'value': 400,
                                                   'question': 'This river flows through London.',
                                                   'answer': 'What is the Thames?'},
                                                  {'value': 600,
                                                   'question': '¿Qué país tiene la forma de una bota en el '
                                                               'mapa de Europa?',
                                                   'answer': 'Italia / Italy — English clue: Which country '
                                                             'is shaped like a boot on the map of Europe?'},
                                                  {'value': 800,
                                                   'question': 'This narrow strait separates Spain from '
                                                               'Morocco.',
                                                   'answer': 'What is the Strait of Gibraltar?'},
                                                  {'value': 1000,
                                                   'question': 'This landlocked country lies between France '
                                                               'and Spain in the Pyrenees.',
                                                   'answer': 'What is Andorra?'}]},
                                       {'title': 'Who Made That?',
                                        'clues': [{'value': 200,
                                                   'question': 'This artist painted the Mona Lisa.',
                                                   'answer': 'Who is Leonardo da Vinci?'},
                                                  {'value': 400,
                                                   'question': 'Alexander Fleming discovered this antibiotic '
                                                               'in 1928.',
                                                   'answer': 'What is penicillin?'},
                                                  {'value': 600,
                                                   'question': 'This inventor is associated with the '
                                                               'movable-type printing press in 15th-century '
                                                               'Europe.',
                                                   'answer': 'Who is Johannes Gutenberg?'},
                                                  {'value': 800,
                                                   'question': 'This scientist was awarded Nobel Prizes in '
                                                               'both physics and chemistry.',
                                                   'answer': 'Who is Marie Curie?'},
                                                  {'value': 1000,
                                                   'question': 'This mathematician wrote the 1843 notes on '
                                                               'the Analytical Engine that included an '
                                                               'algorithm for Bernoulli numbers.',
                                                   'answer': 'Who is Ada Lovelace?'}]},
                                       {'title': 'Turn It Up',
                                        'clues': [{'value': 200,
                                                   'question': 'Freddie Mercury was the lead singer of this '
                                                               'British rock band.',
                                                   'answer': 'Who are Queen?'},
                                                  {'value': 400,
                                                   'question': '¿Qué instrumento musical tiene teclas '
                                                               'blancas y negras y cuerdas que se golpean '
                                                               'con martillos?',
                                                   'answer': 'El piano / The piano — English clue: Which '
                                                             'musical instrument has black and white keys '
                                                             'and strings struck by hammers?'},
                                                  {'value': 600,
                                                   'question': 'This band recorded the album Abbey Road.',
                                                   'answer': 'Who are the Beatles?'},
                                                  {'value': 800,
                                                   'question': 'This Italian musical direction tells '
                                                               'performers to gradually get louder.',
                                                   'answer': 'What is crescendo?'},
                                                  {'value': 1000,
                                                   'question': 'In standard guitar tuning, the lowest and '
                                                               'highest strings share this note name.',
                                                   'answer': 'What is E?'}]},
                                       {'title': 'Time Machine',
                                        'clues': [{'value': 200,
                                                   'question': 'In 1969, this Apollo mission first landed '
                                                               'humans on the Moon.',
                                                   'answer': 'What is Apollo 11?'},
                                                  {'value': 400,
                                                   'question': 'The ancient Olympic Games originated in this '
                                                               'country.',
                                                   'answer': 'What is Greece?'},
                                                  {'value': 600,
                                                   'question': 'This ancient city near Naples was buried by '
                                                               'Mount Vesuvius in AD 79.',
                                                   'answer': 'What is Pompeii?'},
                                                  {'value': 800,
                                                   'question': '¿Qué civilización construyó Machu Picchu en '
                                                               'los Andes?',
                                                   'answer': 'Los incas / The Inca civilization — English '
                                                             'clue: Which civilization built Machu Picchu in '
                                                             'the Andes?'},
                                                  {'value': 1000,
                                                   'question': 'The Rosetta Stone helped scholars decipher '
                                                               'this ancient Egyptian writing system.',
                                                   'answer': 'What are hieroglyphs?'}]},
                                       {'title': 'Between the Covers',
                                        'clues': [{'value': 200,
                                                   'question': 'In this fairy tale, a girl loses a glass '
                                                               'slipper at a royal ball.',
                                                   'answer': 'What is Cinderella?'},
                                                  {'value': 400,
                                                   'question': 'This detective, created by Arthur Conan '
                                                               'Doyle, lives at 221B Baker Street.',
                                                   'answer': 'Who is Sherlock Holmes?'},
                                                  {'value': 600,
                                                   'question': '¿Quién escribió Don Quijote de la Mancha?',
                                                   'answer': 'Miguel de Cervantes — English clue: Who wrote '
                                                             'Don Quixote?'},
                                                  {'value': 800,
                                                   'question': 'Mary Shelley wrote this novel about a '
                                                               'scientist who brings a creature to life.',
                                                   'answer': 'What is Frankenstein?'},
                                                  {'value': 1000,
                                                   'question': 'In Greek mythology, this musician travels to '
                                                               'the underworld to retrieve Eurydice.',
                                                   'answer': 'Who is Orpheus?'}]},
                                       {'title': 'Wait, Really?',
                                        'clues': [{'value': 200,
                                                   'question': 'An octopus has this many arms.',
                                                   'answer': 'What is eight?'},
                                                  {'value': 400,
                                                   'question': 'This is the only even prime number.',
                                                   'answer': 'What is two?'},
                                                  {'value': 600,
                                                   'question': 'This lightweight metal is used to make '
                                                               'kitchen foil and many beverage cans.',
                                                   'answer': 'What is aluminum (aluminium)?'},
                                                  {'value': 800,
                                                   'question': 'This word describes a word or phrase that '
                                                               'reads the same backward and forward, '
                                                               'ignoring spaces and punctuation.',
                                                   'answer': 'What is a palindrome?'},
                                                  {'value': 1000,
                                                   'question': 'This geometric surface can be made by giving '
                                                               'a strip of paper a half twist and joining '
                                                               'its ends; it has only one side.',
                                                   'answer': 'What is a Möbius strip?'}]}]}},
 'final': {'category': 'Final Jiporady: One Word, Three Worlds',
           'question': 'This name belongs to a planet, a Roman messenger god, and a chemical element with '
                       'the symbol Hg.',
           'answer': 'What is Mercury?'}}


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
    return {"ok": True, "app": "jiporady-general-spanish"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
