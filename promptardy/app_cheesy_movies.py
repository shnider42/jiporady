from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Jiporady: Glorious Cheese (1977-1994)",
    "subtitle": "Round 1 is approachable cult-movie fun. Double Jiporady is for people who own an Over the Top hat and have opinions about tournament brackets.",
    "rounds": {
        "round_1": {
            "name": "Round 1: Rental-Store Royalty",
            "categories": [
                {
                    "title": "Rocky Balboa",
                    "clues": [
                        {"value": 100, "question": "In Rocky III, this wrestler-turned-actor plays Clubber Lang.", "answer": "Who is Mr. T?"},
                        {"value": 200, "question": "Rocky trains in the Soviet winter before fighting this towering opponent in Rocky IV.", "answer": "Who is Ivan Drago?"},
                        {"value": 300, "question": "This song from Rocky III became Survivor's signature anthem.", "answer": "What is Eye of the Tiger?"},
                        {"value": 400, "question": "In Rocky II, this unusual farm animal becomes part of Rocky's speed training.", "answer": "What is a chicken?"},
                        {"value": 500, "question": "Rocky V introduces this young boxer whom Rocky trains before the relationship turns sour.", "answer": "Who is Tommy Gunn?"},
                    ],
                },
                {
                    "title": "Jean-Claude Van Damme",
                    "clues": [
                        {"value": 100, "question": "Van Damme plays Frank Dux in this 1988 underground-fighting favorite.", "answer": "What is Bloodsport?"},
                        {"value": 200, "question": "In Kickboxer, Van Damme's Kurt Sloane seeks revenge against this fearsome Thai champion.", "answer": "Who is Tong Po?"},
                        {"value": 300, "question": "Van Damme plays twin brothers Alex and Chad Wagner in this 1991 action film.", "answer": "What is Double Impact?"},
                        {"value": 400, "question": "This 1993 film casts Van Damme as a fugitive protecting a widow and her children.", "answer": "What is Nowhere to Run?"},
                        {"value": 500, "question": "In Hard Target, Van Damme's character Chance Boudreaux uncovers humans being hunted for sport in this Louisiana city.", "answer": "What is New Orleans?"},
                    ],
                },
                {
                    "title": "Training Montage Department",
                    "clues": [
                        {"value": 100, "question": "Daniel learns balance by standing on one leg in this 1984 martial-arts hit.", "answer": "What is The Karate Kid?"},
                        {"value": 200, "question": "Kevin Bacon dances out his frustration in an abandoned warehouse in this 1984 movie.", "answer": "What is Footloose?"},
                        {"value": 300, "question": "Tom Cruise trains to become an elite naval aviator in this 1986 blockbuster.", "answer": "What is Top Gun?"},
                        {"value": 400, "question": "In Vision Quest, Louden Swain drops weight to wrestle this feared opponent.", "answer": "Who is Brian Shute?"},
                        {"value": 500, "question": "This 1985 gymnastics movie starring Kurt Thomas gave the world the pommel-horse fighting style known as 'gymkata.'", "answer": "What is Gymkata?"},
                    ],
                },
                {
                    "title": "Vehicles With Personalities",
                    "clues": [
                        {"value": 100, "question": "This talking black Pontiac helps Michael Knight fight crime on television and became an icon of the era.", "answer": "What is KITT?"},
                        {"value": 200, "question": "A DeLorean reaches 88 mph in this 1985 time-travel comedy.", "answer": "What is Back to the Future?"},
                        {"value": 300, "question": "This 1977 road comedy sends the Bandit eastbound and down in a black Pontiac Trans Am.", "answer": "What is Smokey and the Bandit?"},
                        {"value": 400, "question": "In The Wraith, a mysterious driver returns in this supernatural black sports car to punish a gang of racers.", "answer": "What is the Dodge M4S Turbo Interceptor?"},
                        {"value": 500, "question": "This 1986 cult film follows a sentient red-and-black motorcycle that possesses its riders.", "answer": "What is I Bought a Vampire Motorcycle?"},
                    ],
                },
                {
                    "title": "Future, Neon & Questionable Science",
                    "clues": [
                        {"value": 100, "question": "Arnold Schwarzenegger says he'll be back in this 1984 sci-fi action movie.", "answer": "What is The Terminator?"},
                        {"value": 200, "question": "This 1982 film sends a video-game programmer inside a glowing computer world.", "answer": "What is Tron?"},
                        {"value": 300, "question": "In The Running Man, Schwarzenegger competes on a deadly television show hosted by this character.", "answer": "Who is Damon Killian?"},
                        {"value": 400, "question": "This 1988 alien-invasion satire features special sunglasses that expose hidden messages and disguised aliens.", "answer": "What is They Live?"},
                        {"value": 500, "question": "In Cherry 2000, a man hires Melanie Griffith's tracker to cross a dangerous wasteland in search of this.", "answer": "What is a replacement robot companion?"},
                    ],
                },
                {
                    "title": "One-Liners & Excess",
                    "clues": [
                        {"value": 100, "question": "Arnold's 'Get to the choppa!' comes from this 1987 jungle action film.", "answer": "What is Predator?"},
                        {"value": 200, "question": "This 1989 Patrick Swayze movie teaches that a good bouncer should 'be nice' until it is time not to be nice.", "answer": "What is Road House?"},
                        {"value": 300, "question": "In Commando, Schwarzenegger's John Matrix promises to kill Sully last, then delivers this correction.", "answer": "What is 'I lied'?"},
                        {"value": 400, "question": "This 1986 Sylvester Stallone cop movie features the slogan 'Crime is a disease. Meet the cure.'", "answer": "What is Cobra?"},
                        {"value": 500, "question": "This 1991 Bruce Willis action comedy involves a master thief, Leonardo da Vinci machines, and villains named Darwin and Minerva Mayflower.", "answer": "What is Hudson Hawk?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady: The Over the Top Hat Society",
            "categories": [
                {
                    "title": "Over the Top Deep Cuts",
                    "clues": [
                        {"value": 200, "question": "Stallone's truck-driving arm wrestler is named this.", "answer": "Who is Lincoln Hawk?"},
                        {"value": 400, "question": "Lincoln is trying to reconnect with this son, played by David Mendenhall.", "answer": "Who is Michael Cutler?"},
                        {"value": 600, "question": "The climactic arm-wrestling championship takes place in this Nevada city.", "answer": "What is Las Vegas?"},
                        {"value": 800, "question": "Lincoln's wealthy and hostile father-in-law is played by this actor, also known for Patton.", "answer": "Who is Robert Loggia?"},
                        {"value": 1000, "question": "Lincoln repeatedly explains that turning this item backward is like flipping a switch before a match.", "answer": "What is his baseball cap?"},
                    ],
                },
                {
                    "title": "Cannon Films University",
                    "clues": [
                        {"value": 200, "question": "This Israeli producing duo, cousins Menahem and Yoram, became synonymous with Cannon Films.", "answer": "Who are Menahem Golan and Yoram Globus?"},
                        {"value": 400, "question": "Chuck Norris leads an American rescue mission in this 1984 Cannon action film.", "answer": "What is Missing in Action?"},
                        {"value": 600, "question": "This 1985 Cannon sequel sends Charles Bronson's vigilante Paul Kersey back into action in New York.", "answer": "What is Death Wish 3?"},
                        {"value": 800, "question": "In Masters of the Universe, Dolph Lundgren plays this sword-wielding hero from Eternia.", "answer": "Who is He-Man?"},
                        {"value": 1000, "question": "This expensive 1987 Cannon production starring Christopher Reeve dramatized a famous American aviator and contributed to the studio's financial strain.", "answer": "What is The Aviator?"},
                    ],
                },
                {
                    "title": "Tournament Brackets",
                    "clues": [
                        {"value": 200, "question": "Bloodsport's secret full-contact tournament is called this.", "answer": "What is the Kumite?"},
                        {"value": 400, "question": "In The Karate Kid Part III, Daniel enters this tournament despite Mr. Miyagi's objections.", "answer": "What is the All Valley Karate Tournament?"},
                        {"value": 600, "question": "Best of the Best follows a U.S. team competing against this country in taekwondo.", "answer": "What is South Korea?"},
                        {"value": 800, "question": "In No Retreat, No Surrender, this actor plays the ruthless Russian fighter Ivan Kraschinsky.", "answer": "Who is Jean-Claude Van Damme?"},
                        {"value": 1000, "question": "The climactic contest in Sidekicks is this multi-event martial-arts competition where Barry imagines teaming with Chuck Norris.", "answer": "What is the Battle of the Champions?"},
                    ],
                },
                {
                    "title": "Villains You Respect",
                    "clues": [
                        {"value": 200, "question": "Alan Rickman made his film debut as this Die Hard villain.", "answer": "Who is Hans Gruber?"},
                        {"value": 400, "question": "In Road House, Brad Wesley controls the town of Jasper and is played by this actor.", "answer": "Who is Ben Gazzara?"},
                        {"value": 600, "question": "Bennett, the chainmail-shirted villain of Commando, is played by this Australian actor.", "answer": "Who is Vernon Wells?"},
                        {"value": 800, "question": "This actor plays the scenery-devouring General M. Bison in 1994's Street Fighter.", "answer": "Who is Raul Julia?"},
                        {"value": 1000, "question": "In Ricochet, this actor plays psychotic criminal Earl Talbot Blake opposite Denzel Washington.", "answer": "Who is John Lithgow?"},
                    ],
                },
                {
                    "title": "Direct-to-Video Adjacent",
                    "clues": [
                        {"value": 200, "question": "This 1992 film pairs Dolph Lundgren and Brandon Lee as cops fighting the Yakuza in Los Angeles.", "answer": "What is Showdown in Little Tokyo?"},
                        {"value": 400, "question": "Stone Cold stars former NFL linebacker Brian Bosworth as a cop infiltrating this kind of gang.", "answer": "What is an outlaw motorcycle gang?"},
                        {"value": 600, "question": "In 1993's Only the Strong, Mark Dacascos teaches students this Brazilian martial art.", "answer": "What is capoeira?"},
                        {"value": 800, "question": "This 1990 action film stars Brian Thompson as an alien drug dealer pursued by Dolph Lundgren.", "answer": "What is I Come in Peace, also known as Dark Angel?"},
                        {"value": 1000, "question": "This 1991 action film stars Jeff Speakman as a kenpo expert battling organized crime after his mentor is killed.", "answer": "What is The Perfect Weapon?"},
                    ],
                },
                {
                    "title": "Soundtrack Cassette Permanently Stuck",
                    "clues": [
                        {"value": 200, "question": "Kenny Loggins performs this Top Gun song used during the opening carrier-deck sequence.", "answer": "What is Danger Zone?"},
                        {"value": 400, "question": "Joe Esposito sings this Karate Kid tournament anthem.", "answer": "What is You're the Best?"},
                        {"value": 600, "question": "Sammy Hagar's title song opens this 1987 Sylvester Stallone arm-wrestling movie.", "answer": "What is Winner Takes It All?"},
                        {"value": 800, "question": "This Stan Bush song accompanies the Autobots' darkest hour in The Transformers: The Movie.", "answer": "What is The Touch?"},
                        {"value": 1000, "question": "John Farnham performs this triumphant montage song heard in Rad and later embraced as an eighties cult anthem.", "answer": "What is Break the Ice?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: Maximum Commitment",
        "question": "This 1989 film stars Jean-Claude Van Damme as a former soldier who enters a brutal kickboxing contest to avenge his paralyzed brother.",
        "answer": "What is Kickboxer?",
    },
}


def all_categories():
    categories = []
    for round_data in GAME_DATA["rounds"].values():
        for category in round_data["categories"]:
            categories.append({"category": category["title"], "clues": category["clues"]})
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
    return {"ok": True, "app": "jiporady-cheesy-movies-1977-1994"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
