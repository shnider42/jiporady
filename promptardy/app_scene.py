from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Scene Jiporady",
    "subtitle": "What is... the breakdown at the end?",
    "rounds": {
        "round_1": {
            "name": "Round 1",
            "categories": [
                {
                    "title": "Lead Singers",
                    "clues": [
                        {
                            "value": 100,
                            "question": "This vocalist fronted A Day to Remember through albums like Homesick and What Separates Me from You.",
                            "answer": "Who is Jeremy McKinnon?"
                        },
                        {
                            "value": 200,
                            "question": "The unmistakably high voice on Sleeping With Sirens songs like 'If You Can't Hang' belongs to this singer.",
                            "answer": "Who is Kellin Quinn?"
                        },
                        {
                            "value": 300,
                            "question": "This frontman led My Chemical Romance through The Black Parade era.",
                            "answer": "Who is Gerard Way?"
                        },
                        {
                            "value": 400,
                            "question": "This vocalist was the clean-voice star of Underoath during Define the Great Line and Lost in the Sound of Separation.",
                            "answer": "Who is Aaron Gillespie?"
                        },
                        {
                            "value": 500,
                            "question": "Before becoming Skrillex, this singer handled vocals for From First to Last.",
                            "answer": "Who is Sonny Moore?"
                        },
                    ],
                },
                {
                    "title": "Metalcore",
                    "clues": [
                        {
                            "value": 100,
                            "question": "This style is best known for combining metal riffing with hardcore breakdowns.",
                            "answer": "What is metalcore?"
                        },
                        {
                            "value": 200,
                            "question": "This Massachusetts band gave the genre one of its biggest anthems with 'My Last Serenade.'",
                            "answer": "Who are Killswitch Engage?"
                        },
                        {
                            "value": 300,
                            "question": "This Australian group released scene staples like 'Carrion' and 'Sleepwalker.'",
                            "answer": "Who are Parkway Drive?"
                        },
                        {
                            "value": 400,
                            "question": "Known for matching fashion jokes with crushing riffs, this band named itself after a devil in a movie wardrobe gag.",
                            "answer": "Who are The Devil Wears Prada?"
                        },
                        {
                            "value": 500,
                            "question": "This Pennsylvania act was fronted by Jake Luhrs on songs like 'Composure' and 'White Washed.'",
                            "answer": "Who are August Burns Red?"
                        },
                    ],
                },
                {
                    "title": "Easycore... means.... what?",
                    "clues": [
                        {
                            "value": 100,
                            "question": "This hybrid style usually means pop-punk energy mixed with mosh-friendly parts.",
                            "answer": "What is easycore?"
                        },
                        {
                            "value": 200,
                            "question": "This Florida band became the style's best-known crossover success with sing-alongs and breakdowns on the same record.",
                            "answer": "Who are A Day to Remember?"
                        },
                        {
                            "value": 300,
                            "question": "This Massachusetts quartet shouted 'Who cares?' and helped define the faster, more technical end of the style.",
                            "answer": "Who are Four Year Strong?"
                        },
                        {
                            "value": 400,
                            "question": "This goofy but beloved band put exclamation points in their name and opened many listeners to the style through 'In Friends We Trust.'",
                            "answer": "Who are Chunk! No, Captain Chunk!?"
                        },
                        {
                            "value": 500,
                            "question": "Compared with straight pop-punk, this ingredient usually hits harder in the mosh sections of the hybrid style.",
                            "answer": "What is hardcore?"
                        },
                    ],
                },
                {
                    "title": "A Day to Remember",
                    "clues": [
                        {
                            "value": 100,
                            "question": "The band from Ocala broke out to a huge audience with this 2009 album featuring 'The Downfall of Us All.'",
                            "answer": "What is Homesick?"
                        },
                        {
                            "value": 200,
                            "question": "Before Homesick, the group released this album with 'The Plot to Bomb the Panhandle.'",
                            "answer": "What is For Those Who Have Heart?"
                        },
                        {
                            "value": 300,
                            "question": "On a fan-favorite single, the crowd sings about disrespect from 'all my friends' in this broad location.",
                            "answer": "What is the coast?"
                        },
                        {
                            "value": 400,
                            "question": "This song title tells a doubter to wait until the music industry proves otherwise.",
                            "answer": "What is 'I'm Made of Wax, Larry, What Are You Made Of?'"
                        },
                        {
                            "value": 500,
                            "question": "This 2010 single took a blunt, plainspoken title that fit the song's huge sing-along chorus.",
                            "answer": "What is 'All I Want'?"
                        },
                    ],
                },
                {
                    "title": "'Screamo'",
                    "clues": [
                        {
                            "value": 100,
                            "question": "Parents and local news often used this catch-all Ohio band's title when talking about eyeliner, dramatic hooks, and 'Ohio Is for Lovers.'",
                            "answer": "Who are Hawthorne Heights?"
                        },
                        {
                            "value": 200,
                            "question": "This Canadian group blurred post-hardcore and melody on scene staples like 'Smile in Your Sleep.'",
                            "answer": "Who are Silverstein?"
                        },
                        {
                            "value": 300,
                            "question": "This New Jersey act fronted by Bert McCracken became famous for songs like 'The Taste of Ink.'",
                            "answer": "Who are The Used?"
                        },
                        {
                            "value": 400,
                            "question": "This Long Island band gave Warped Tour kids 'Cute Without the E' and endless shout-alongs.",
                            "answer": "Who are Taking Back Sunday?"
                        },
                        {
                            "value": 500,
                            "question": "This Las Vegas group fronted by Ronnie Radke on its debut delivered 'Situations' and huge Myspace-era drama.",
                            "answer": "Who are Escape the Fate?"
                        },
                    ],
                },
                {
                    "title": "Lyrics That Start With This",
                    "clues": [
                        {
                            "value": 100,
                            "question": "This opening shout launches the best-known opener from the 2009 breakout album.",
                            "answer": "What is 'The Downfall of Us All'?"
                        },
                        {
                            "value": 200,
                            "question": "Finish this opening: 'So cut my wrists and black my eyes...'",
                            "answer": "What is '...so I can fall asleep tonight or die'?"
                        },
                        {
                            "value": 300,
                            "question": "Finish this opening: 'How does it feel to know you'll never have to be alone...'",
                            "answer": "What is '...when you get home'?"
                        },
                        {
                            "value": 400,
                            "question": "Finish this opening: 'I got your picture, I'm coming with you...'",
                            "answer": "What is '...dear Maria, count me in'?"
                        },
                        {
                            "value": 500,
                            "question": "Finish this opening: 'This is the end of the world...'",
                            "answer": "What is '...news that we have heard'?"
                        },
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady",
            "categories": [
                {
                    "title": "It's Not a Phase Mom",
                    "clues": [
                        {
                            "value": 200,
                            "question": "This annual traveling summer package tour was basically the parking-lot kingdom for scene kids across the 2000s.",
                            "answer": "What is Warped Tour?"
                        },
                        {
                            "value": 400,
                            "question": "This social platform let bands rack up plays, custom profiles, and top-friend politics before streaming took over.",
                            "answer": "What is MySpace?"
                        },
                        {
                            "value": 600,
                            "question": "This mall chain became visually tied to black skinny jeans, band tees, and scene-kid allowance spending.",
                            "answer": "What is Hot Topic?"
                        },
                        {
                            "value": 800,
                            "question": "This hair-straightening tool was basically a backstage co-headliner for the era.",
                            "answer": "What is a flat iron?"
                        },
                        {
                            "value": 1000,
                            "question": "This face-framing hairstyle was practically an unofficial membership card for the era's look.",
                            "answer": "What are side-swept bangs?"
                        },
                    ],
                },
                {
                    "title": "Songs We Regret We Know the First Lines To",
                    "clues": [
                        {
                            "value": 200,
                            "question": "Name the song that opens with: 'Do you feel like a man...'",
                            "answer": "What is 'If You Can't Hang'?"
                        },
                        {
                            "value": 400,
                            "question": "Name the song that opens with: 'I've got a secret...'",
                            "answer": "What is 'Situations'?"
                        },
                        {
                            "value": 600,
                            "question": "Name the song that opens with: 'One day, you'll see your pretty face...'",
                            "answer": "What is 'King for a Day'?"
                        },
                        {
                            "value": 800,
                            "question": "Name the song whose opening begins, 'My heart is in your...'",
                            "answer": "What is 'Hands Down'?"
                        },
                        {
                            "value": 1000,
                            "question": "Name the song that opens with: 'Beware! Beware! Beware!...'",
                            "answer": "What is 'Danger: Wildman'?"
                        },
                    ],
                },
                {
                    "title": "Band Lineups",
                    "clues": [
                        {
                            "value": 200,
                            "question": "Jeremy McKinnon, Neil Westfall, Kevin Skaff, Josh Woodard, and Alex Shelnutt.",
                            "answer": "Who are A Day to Remember?"
                        },
                        {
                            "value": 400,
                            "question": "Vic Fuentes, Mike Fuentes, Jaime Preciado, and Tony Perry.",
                            "answer": "Who are Pierce the Veil?"
                        },
                        {
                            "value": 600,
                            "question": "Spencer Chamberlain, Aaron Gillespie, Tim McTague, Chris Dudley, James Smith, and Grant Brandell.",
                            "answer": "Who are Underoath?"
                        },
                        {
                            "value": 800,
                            "question": "Oli Sykes, Lee Malia, Matt Kean, and Matt Nicholls, plus Jona Weinhofen during part of the era.",
                            "answer": "Who are Bring Me the Horizon?"
                        },
                        {
                            "value": 1000,
                            "question": "Shane Told, Paul Koehler, Billy Hamilton, Josh Bradford, and Neil Boshart made up this post-hardcore group during much of the era.",
                            "answer": "Who are Silverstein?"
                        },
                    ],
                },
                {
                    "title": "They Went On to Do What?",
                    "clues": [
                        {
                            "value": 200,
                            "question": "After his early post-hardcore band days, Sonny Moore went on to become this electronic superstar alias.",
                            "answer": "Who is Skrillex?"
                        },
                        {
                            "value": 400,
                            "question": "After helping define Alexisonfire, Dallas Green launched this softer, singer-songwriter project.",
                            "answer": "What is City and Colour?"
                        },
                        {
                            "value": 600,
                            "question": "After Chiodos and other stops, Craig Owens fronted this supergroup whose initials were everywhere in 2010.",
                            "answer": "What is D.R.U.G.S.?"
                        },
                        {
                            "value": 800,
                            "question": "After Attack Attack!, Austin Carlile became the frontman of this band whose full name begins with a small rodent.",
                            "answer": "Who are Of Mice & Men?"
                        },
                        {
                            "value": 1000,
                            "question": "Before stepping in for one huge Florida easycore group on tour, Jason Lancaster had already co-founded this piano-laced pop-punk band.",
                            "answer": "Who are Mayday Parade?"
                        },
                    ],
                },
                {
                    "title": "Homesick Deep Cuts",
                    "clues": [
                        {
                            "value": 200,
                            "question": "The first full track on the 2009 breakout opens with a gang-vocal launch and became the album's signature opener.",
                            "answer": "What is 'The Downfall of Us All'?"
                        },
                        {
                            "value": 400,
                            "question": "This title from the same record sounds like an emotional plea where the speaker is still asking for proof.",
                            "answer": "What is 'If It Means a Lot to You'?"
                        },
                        {
                            "value": 600,
                            "question": "This one pairs cold dessert with a place-name abbreviation in a title that every fan of the record remembers.",
                            "answer": "What is 'NJ Legion Iced Tea'?"
                        },
                        {
                            "value": 800,
                            "question": "This title sounds like the sarcastic speech you might hear while being initiated into chaos.",
                            "answer": "What is 'Welcome to the Family'?"
                        },
                        {
                            "value": 1000,
                            "question": "This title sounds like a vow to keep the scene alive for those outside the mainstream.",
                            "answer": "What is 'Holdin' It Down for the Underground'?"
                        },
                    ],
                },
                {
                    "title": "Scene DNA",
                    "clues": [
                        {
                            "value": 200,
                            "question": "This style sits between punk-rooted intensity and melody for bands like Silverstein, Saosin, and early Chiodos.",
                            "answer": "What is post-hardcore?"
                        },
                        {
                            "value": 400,
                            "question": "This subgenre term was often applied to melodic confession-heavy bands like Dashboard Confessional and early Taking Back Sunday.",
                            "answer": "What is emo?"
                        },
                        {
                            "value": 600,
                            "question": "This branch of heavy music leans more toward chugs, panic chords, and dissonance than radio-sized choruses.",
                            "answer": "What is hardcore?"
                        },
                        {
                            "value": 800,
                            "question": "This label name signed many key bands of the era, including A Day to Remember for a stretch and chunks of the Warped ecosystem.",
                            "answer": "What is Victory Records?"
                        },
                        {
                            "value": 1000,
                            "question": "This phrase describes the clean-sung payoff section that often arrives after screaming in many scene staples.",
                            "answer": "What is the chorus?"
                        },
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: Scene Crossover",
        "question": "This Florida band bridged pop-punk hooks and breakdowns so effectively that fans of both Warped Tour sing-alongs and mosh parts could claim them as their own.",
        "answer": "Who are A Day to Remember?"
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
    return {"ok": True, "app": "jiporady_scene"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
