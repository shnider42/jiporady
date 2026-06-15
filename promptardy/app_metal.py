from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Jiporady: Metal — Pantera to Avenged Sevenfold",
    "subtitle": "From groove-metal anthems and 2000s metalcore to stage names, riffs, albums, lineups, and deep-cut pit trivia",
    "rounds": {
        "round_1": {
            "name": "Round 1",
            "categories": [
                {
                    "title": "Pantera 101",
                    "clues": [
                        {"value": 100, "question": "This guitarist, born Darrell Abbott, became Pantera's most iconic riff machine.", "answer": "Who is Dimebag Darrell?"},
                        {"value": 200, "question": "This Pantera vocalist fronted the band during its classic groove-metal era.", "answer": "Who is Phil Anselmo?"},
                        {"value": 300, "question": "This 1990 album helped launch Pantera's groove-metal identity with a title track about hostile riders.", "answer": "What is Cowboys from Hell?"},
                        {"value": 400, "question": "This one-word Pantera anthem tells listeners to be themselves, by command.", "answer": "What is Walk?"},
                        {"value": 500, "question": "Dimebag Darrell and drummer Vinnie Paul shared this family relationship.", "answer": "What are brothers?"},
                    ],
                },
                {
                    "title": "Avenged 101",
                    "clues": [
                        {"value": 100, "question": "Avenged Sevenfold is often abbreviated with this three-character nickname.", "answer": "What is A7X?"},
                        {"value": 200, "question": "This singer, born Matthew Sanders, is Avenged Sevenfold's lead vocalist.", "answer": "Who is M. Shadows?"},
                        {"value": 300, "question": "This lead guitarist, born Brian Haner Jr., is known for fast solos and a villainous stage name.", "answer": "Who is Synyster Gates?"},
                        {"value": 400, "question": "This 2005 Avenged Sevenfold album includes 'Bat Country' and helped push the band into the mainstream.", "answer": "What is City of Evil?"},
                        {"value": 500, "question": "This drummer, born Jimmy Sullivan, was a founding member of Avenged Sevenfold.", "answer": "Who is The Rev?"},
                    ],
                },
                {
                    "title": "Albums Everyone Knows",
                    "clues": [
                        {"value": 100, "question": "Pantera's 1992 album with a punched-face cover is this display of power.", "answer": "What is Vulgar Display of Power?"},
                        {"value": 200, "question": "This 1994 Pantera album reached No. 1 and pushed the band even heavier.", "answer": "What is Far Beyond Driven?"},
                        {"value": 300, "question": "Avenged Sevenfold's 2010 album, completed after The Rev's death, has this dark dream-themed title.", "answer": "What is Nightmare?"},
                        {"value": 400, "question": "This 2013 Avenged Sevenfold album shares its title with a royal command.", "answer": "What is Hail to the King?"},
                        {"value": 500, "question": "This Machine Head debut album from 1994 helped define post-thrash/groove metal's decade.", "answer": "What is Burn My Eyes?"},
                    ],
                },
                {
                    "title": "Song Pit",
                    "clues": [
                        {"value": 100, "question": "The opening Pantera track 'Mouth for War' appears on this 1992 album.", "answer": "What is Vulgar Display of Power?"},
                        {"value": 200, "question": "This Pantera ballad begins with clean guitar and a cemetery-referencing title.", "answer": "What is Cemetery Gates?"},
                        {"value": 300, "question": "Avenged Sevenfold's breakthrough single about bats shares imagery with Hunter S. Thompson territory.", "answer": "What is Bat Country?"},
                        {"value": 400, "question": "This A7X song from 'City of Evil' names a Biblical-sounding city but opens with a huge dual-guitar attack.", "answer": "What is Beast and the Harlot?"},
                        {"value": 500, "question": "This Pantera song from 'Far Beyond Driven' bluntly declares damage in its two-word title.", "answer": "What is I'm Broken?"},
                    ],
                },
                {
                    "title": "Metal Styles",
                    "clues": [
                        {"value": 100, "question": "Pantera is strongly associated with this riff-heavy, rhythm-driven style of metal.", "answer": "What is groove metal?"},
                        {"value": 200, "question": "Early Avenged Sevenfold is often tied to this style blending extreme metal with hardcore punk breakdowns.", "answer": "What is metalcore?"},
                        {"value": 300, "question": "This 1980s metal style includes Metallica, Slayer, Megadeth, and Anthrax.", "answer": "What is thrash metal?"},
                        {"value": 400, "question": "This metal subgenre uses down-tuned riffs and emotional, hardcore-influenced breakdowns; Killswitch Engage is a major example.", "answer": "What is metalcore?"},
                        {"value": 500, "question": "A guitar part built around a repeated catchy pattern is commonly called this.", "answer": "What is a riff?"},
                    ],
                },
                {
                    "title": "People in the Band",
                    "clues": [
                        {"value": 100, "question": "Rex Brown played this instrument in Pantera's classic lineup.", "answer": "What is bass?"},
                        {"value": 200, "question": "Vinnie Paul played this instrument in Pantera.", "answer": "What are drums?"},
                        {"value": 300, "question": "Zacky Vengeance is primarily this kind of guitarist in Avenged Sevenfold.", "answer": "What is rhythm guitarist?"},
                        {"value": 400, "question": "Johnny Christ plays this low-end instrument in Avenged Sevenfold.", "answer": "What is bass?"},
                        {"value": 500, "question": "This Dream Theater drummer helped Avenged Sevenfold finish and tour behind 'Nightmare.'", "answer": "Who is Mike Portnoy?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady",
            "categories": [
                {
                    "title": "Pantera Deep Cuts",
                    "clues": [
                        {"value": 200, "question": "Before Phil Anselmo, this singer fronted Pantera on several glam-era releases.", "answer": "Who is Terry Glaze?"},
                        {"value": 400, "question": "This 1988 Pantera album was the first to feature Phil Anselmo on lead vocals.", "answer": "What is Power Metal?"},
                        {"value": 600, "question": "This producer worked on major Pantera albums including 'Cowboys from Hell' and 'Vulgar Display of Power.'", "answer": "Who is Terry Date?"},
                        {"value": 800, "question": "This 1996 Pantera album contains 'Drag the Waters' and a harsher, darker production style.", "answer": "What is The Great Southern Trendkill?"},
                        {"value": 1000, "question": "This post-Pantera band formed by Dimebag Darrell and Vinnie Paul released 'New Found Power.'", "answer": "What is Damageplan?"},
                    ],
                },
                {
                    "title": "A7X Deep Cuts",
                    "clues": [
                        {"value": 200, "question": "This 2001 Avenged Sevenfold debut album took its title from a trumpet-heavy image in Revelation.", "answer": "What is Sounding the Seventh Trumpet?"},
                        {"value": 400, "question": "This 2003 A7X album includes 'Unholy Confessions' and became a core metalcore-era release.", "answer": "What is Waking the Fallen?"},
                        {"value": 600, "question": "This drummer joined Avenged Sevenfold in 2015 after playing with Bad Religion.", "answer": "Who is Brooks Wackerman?"},
                        {"value": 800, "question": "This 2016 Avenged Sevenfold album was released with a surprise rollout and a space/science-fiction concept.", "answer": "What is The Stage?"},
                        {"value": 1000, "question": "The song 'A Little Piece of Heaven' was largely written by this late Avenged Sevenfold drummer.", "answer": "Who is The Rev?"},
                    ],
                },
                {
                    "title": "Groove Metal Family Tree",
                    "clues": [
                        {"value": 200, "question": "This Brazilian band moved toward groove and tribal rhythms on 'Chaos A.D.' and 'Roots.'", "answer": "Who are Sepultura?"},
                        {"value": 400, "question": "Before becoming Lamb of God, this Richmond band used this more sacrificial name.", "answer": "What is Burn the Priest?"},
                        {"value": 600, "question": "This Machine Head frontman previously played guitar in Bay Area thrash band Vio-lence.", "answer": "Who is Robb Flynn?"},
                        {"value": 800, "question": "This 1992 White Zombie album title combines a devilish music machine with a hot-rod image.", "answer": "What is La Sexorcisto: Devil Music Volume One?"},
                        {"value": 1000, "question": "This Prong album with 'Snap Your Fingers, Snap Your Neck' became a major industrial/groove-metal crossover point.", "answer": "What is Cleansing?"},
                    ],
                },
                {
                    "title": "Metalcore to Arena Metal",
                    "clues": [
                        {"value": 200, "question": "This Massachusetts band released 'The End of Heartache' in 2004 with vocalist Howard Jones.", "answer": "Who are Killswitch Engage?"},
                        {"value": 400, "question": "This Orange County band released 'The Curse' in 2004 and helped define mid-2000s melodic metalcore.", "answer": "Who are Atreyu?"},
                        {"value": 600, "question": "This Welsh band released 'The Poison' and crossed metalcore into mainstream hard rock radio.", "answer": "Who are Bullet for My Valentine?"},
                        {"value": 800, "question": "This Trivium album from 2005 contains 'Pull Harder on the Strings of Your Martyr.'", "answer": "What is Ascendancy?"},
                        {"value": 1000, "question": "Avenged Sevenfold's shift away from metalcore screaming toward a more classic-metal vocal approach is most obvious on this 2005 album.", "answer": "What is City of Evil?"},
                    ],
                },
                {
                    "title": "Names Behind the Names",
                    "clues": [
                        {"value": 200, "question": "M. Shadows' legal first name is this.", "answer": "What is Matthew?"},
                        {"value": 400, "question": "Synyster Gates' father, Brian Haner Sr., is a guitarist and comedian who performs under this nickname.", "answer": "Who is Papa Gates?"},
                        {"value": 600, "question": "Dimebag Darrell previously used this diamond-themed stage name.", "answer": "What is Diamond Darrell?"},
                        {"value": 800, "question": "The Rev's legal surname was this.", "answer": "What is Sullivan?"},
                        {"value": 1000, "question": "Johnny Christ's legal surname is this.", "answer": "What is Seward?"},
                    ],
                },
                {
                    "title": "Release-Year Pit Trap",
                    "clues": [
                        {"value": 200, "question": "Pantera released 'Cowboys from Hell' in this year.", "answer": "What is 1990?"},
                        {"value": 400, "question": "'Vulgar Display of Power' and Megadeth's 'Countdown to Extinction' both arrived in this year.", "answer": "What is 1992?"},
                        {"value": 600, "question": "Avenged Sevenfold released 'Waking the Fallen' in this year.", "answer": "What is 2003?"},
                        {"value": 800, "question": "The self-titled Avenged Sevenfold album with 'Afterlife' and 'Almost Easy' arrived in this year.", "answer": "What is 2007?"},
                        {"value": 1000, "question": "Pantera's final studio album, 'Reinventing the Steel,' was released in this year.", "answer": "What is 2000?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: Groove to A7X",
        "question": "This Dream Theater drummer recorded drum parts for Avenged Sevenfold's 'Nightmare' after the death of The Rev.",
        "answer": "Who is Mike Portnoy?",
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
    return {"ok": True, "app": "jiporady-metal"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
