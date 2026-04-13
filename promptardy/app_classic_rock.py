from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Classic Rock Jiporady",
    "subtitle": "What is... turn it up?",
    "rounds": {
        "round_1": {
            "name": "Round 1",
            "categories": [
                {
                    "title": "British Invasion (No Beatles)",
                    "clues": [
                        {"value": 100, "question": "This London band led by Mick Jagger and Keith Richards was often positioned as the Beatles' rougher counterpart.", "answer": "Who are The Rolling Stones?"},
                        {"value": 200, "question": "Eric Burdon fronted this British Invasion band known for 'House of the Rising Sun.'", "answer": "Who are The Animals?"},
                        {"value": 300, "question": "This Manchester group featuring Graham Nash had a hit with 'Bus Stop.'", "answer": "Who are The Hollies?"},
                        {"value": 400, "question": "Ray and Dave Davies were the songwriting and guitar-driving brothers behind this band.", "answer": "Who are The Kinks?"},
                        {"value": 500, "question": "Featuring Steve Winwood as a teenager, this Birmingham group scored with 'Gimme Some Lovin'' and 'I'm a Man.'", "answer": "Who are The Spencer Davis Group?"},
                    ],
                },
                {
                    "title": "Beatles Lore: Hard Mode",
                    "clues": [
                        {"value": 100, "question": "Before Ringo Starr joined permanently, this drummer appeared on the Beatles' first single release version of 'Love Me Do.'", "answer": "Who is Andy White?"},
                        {"value": 200, "question": "This manager, sometimes called the 'fifth Beatle,' died in 1967 and left a major vacuum in the band's business affairs.", "answer": "Who is Brian Epstein?"},
                        {"value": 300, "question": "Apple Corps was partly conceived as a multimedia empire after the band was inspired by the business vision of this Dutch electronics giant's name.", "answer": "What is Apple?"},
                        {"value": 400, "question": "This working title for 'Yesterday' referenced scrambled eggs before Paul McCartney finalized the lyrics.", "answer": "What is 'Scrambled Eggs'?"},
                        {"value": 500, "question": "This drummer, not Pete Best and not Ringo, briefly sat with the Beatles in Hamburg when one member was unavailable in the early club era.", "answer": "Who is Jimmie Nicol?"},
                    ],
                },
                {
                    "title": "Motown",
                    "clues": [
                        {"value": 100, "question": "This label founder built Motown into a hitmaking empire in Detroit.", "answer": "Who is Berry Gordy?"},
                        {"value": 200, "question": "This vocal group featuring Diana Ross had hits like 'Stop! In the Name of Love.'", "answer": "Who are The Supremes?"},
                        {"value": 300, "question": "This singer of 'What's Going On' was also a former member of The Miracles' touring circle before his solo superstardom.", "answer": "Who is Marvin Gaye?"},
                        {"value": 400, "question": "Smokey Robinson first rose to fame fronting this Motown group.", "answer": "Who are The Miracles?"},
                        {"value": 500, "question": "This songwriting and production trio wrote a huge run of Motown classics including many for The Supremes and Four Tops.", "answer": "Who are Holland-Dozier-Holland?"},
                    ],
                },
                {
                    "title": "Massachusetts Rock Roots",
                    "clues": [
                        {"value": 100, "question": "Steven Tyler and Joe Perry helped found this Boston-area hard rock band.", "answer": "Who are Aerosmith?"},
                        {"value": 200, "question": "This influential proto-punk group featuring Jonathan Richman came out of Massachusetts in the early 1970s.", "answer": "Who are The Modern Lovers?"},
                        {"value": 300, "question": "This Cars frontman was born in Baltimore, but the band itself was formed in Boston.", "answer": "Who is Ric Ocasek?"},
                        {"value": 400, "question": "This blues-rock band fronted by J. Geils became one of Massachusetts' most successful rock exports.", "answer": "Who are The J. Geils Band?"},
                        {"value": 500, "question": "Though often tied to New York punk, this band featuring Joey, Johnny, Dee Dee, and Tommy included this Massachusetts-born original drummer.", "answer": "Who is Tommy Ramone?"},
                    ],
                },
                {
                    "title": "Inspired by the Beatles",
                    "clues": [
                        {"value": 100, "question": "Jeff Lynne's band ELO was consciously built in part as an attempt to continue the melodic and orchestral adventurousness of this band.", "answer": "Who are The Beatles?"},
                        {"value": 200, "question": "The members of this British band openly admired the Beatles and later became huge stars with albums like '(What's the Story) Morning Glory?'.", "answer": "Who are Oasis?"},
                        {"value": 300, "question": "This power-pop band led by Robin Zander and Rick Nielsen often channeled Beatlesque melody under a harder-rock exterior.", "answer": "Who are Cheap Trick?"},
                        {"value": 400, "question": "Todd Rundgren produced this 1970s band whose very name suggested a 'younger than the Beatles' pop spirit.", "answer": "Who are Badfinger?"},
                        {"value": 500, "question": "This band founded by Roy Wood and later led by Jeff Lynne had a name shortened from Electric Light this.", "answer": "What is Orchestra?"},
                    ],
                },
                {
                    "title": "Influential Short-Stint Members",
                    "clues": [
                        {"value": 100, "question": "This Canadian guitarist added a country-rock edge to Crosby, Stills & Nash when the quartet briefly became Crosby, Stills, Nash & this man.", "answer": "Who is Neil Young?"},
                        {"value": 200, "question": "Before becoming a solo icon, this guitarist had a crucial early stint in John Mayall's Bluesbreakers and then in Cream.", "answer": "Who is Eric Clapton?"},
                        {"value": 300, "question": "This guitarist replaced Mick Taylor in the Rolling Stones and, unlike Taylor, stayed for decades.", "answer": "Who is Ron Wood?"},
                        {"value": 400, "question": "This singer and bassist had a relatively brief but hugely important tenure in Fleetwood Mac before launching a massive solo career.", "answer": "Who is Lindsey Buckingham?"},
                        {"value": 500, "question": "Though his time in Buffalo Springfield was short, this future Poco founder helped shape the country-rock lane the band hinted at.", "answer": "Who is Richie Furay?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady",
            "categories": [
                {
                    "title": "Post-Beatles Lives & Legacy",
                    "clues": [
                        {"value": 200, "question": "George Harrison organized this landmark 1971 benefit event for Bangladesh, one of rock's earliest major charity concerts.", "answer": "What is The Concert for Bangladesh?"},
                        {"value": 400, "question": "Paul McCartney formed this band with Linda McCartney and Denny Laine after the Beatles split.", "answer": "What is Wings?"},
                        {"value": 600, "question": "John Lennon spent part of the 1970s separated from Yoko Ono in this so-called period, a phrase borrowed from a Chinese horoscope.", "answer": "What is the Lost Weekend?"},
                        {"value": 800, "question": "Ringo Starr unexpectedly became a family-TV staple as the original narrator of this PBS children's series.", "answer": "What is Thomas the Tank Engine & Friends?"},
                        {"value": 1000, "question": "This supergroup, formed in the late 1980s, included George Harrison alongside Bob Dylan, Tom Petty, Roy Orbison, and Jeff Lynne.", "answer": "Who are The Traveling Wilburys?"},
                    ],
                },
                {
                    "title": "Classic Rock Albums by Clue",
                    "clues": [
                        {"value": 200, "question": "Hotel California, New Kid in Town, and Life in the Fast Lane all appear on this Eagles album.", "answer": "What is Hotel California?"},
                        {"value": 400, "question": "Baba O'Riley and Won't Get Fooled Again are on this Who album.", "answer": "What is Who's Next?"},
                        {"value": 600, "question": "Money, Time, and Us and Them appear on this Pink Floyd album.", "answer": "What is The Dark Side of the Moon?"},
                        {"value": 800, "question": "Black Dog, Rock and Roll, and Stairway to Heaven appear on this untitled Led Zeppelin album commonly called this numeral.", "answer": "What is Led Zeppelin IV?"},
                        {"value": 1000, "question": "Thunder Road, Born to Run, and Jungleland appear on this Bruce Springsteen album.", "answer": "What is Born to Run?"},
                    ],
                },
                {
                    "title": "Guitar Gods",
                    "clues": [
                        {"value": 200, "question": "This Jimi Hendrix Experience bassist later joined Emerson, Lake & Palmer for a brief spin-off project called Emerson, Lake & this surname.", "answer": "Who is Noel Redding?"},
                        {"value": 400, "question": "This Allman Brothers Band guitarist was killed in a 1971 motorcycle accident but remains central to Southern rock mythology.", "answer": "Who is Duane Allman?"},
                        {"value": 600, "question": "This Irish guitarist led Thin Lizzy through classics like 'The Boys Are Back in Town.'", "answer": "Who is Scott Gorham?"},
                        {"value": 800, "question": "Before forming Dire Straits, this fingerpicking virtuoso worked as a journalist and teacher.", "answer": "Who is Mark Knopfler?"},
                        {"value": 1000, "question": "This session legend, not officially a Yardbird for long, played on 'For Your Love' and later founded Led Zeppelin.", "answer": "Who is Jimmy Page?"},
                    ],
                },
                {
                    "title": "Festivals, Feuds & Famous Moments",
                    "clues": [
                        {"value": 200, "question": "This 1969 festival in upstate New York became the defining counterculture concert event of its era.", "answer": "What is Woodstock?"},
                        {"value": 400, "question": "The Rolling Stones' chaotic 1969 free concert at this California speedway became linked with the death of Meredith Hunter.", "answer": "What is Altamont?"},
                        {"value": 600, "question": "This Fleetwood Mac album is inseparable from the interpersonal turmoil among Buckingham, Nicks, and the McVies.", "answer": "What is Rumours?"},
                        {"value": 800, "question": "Roger Waters and David Gilmour became locked in long-running conflict over the legacy and control of this band.", "answer": "What is Pink Floyd?"},
                        {"value": 1000, "question": "This guitarist's famous Monterey Pop Festival stunt involved setting his instrument on fire.", "answer": "Who is Jimi Hendrix?"},
                    ],
                },
                {
                    "title": "Prog, Art & Odd Time",
                    "clues": [
                        {"value": 200, "question": "This British prog band fronted by Jon Anderson recorded 'Roundabout.'", "answer": "Who are Yes?"},
                        {"value": 400, "question": "Peter Gabriel was the original theatrical frontman of this prog band before Phil Collins took over lead vocals.", "answer": "Who are Genesis?"},
                        {"value": 600, "question": "This King Crimson song title begins with '21st Century' and ends with this profession.", "answer": "What is Schizoid Man?"},
                        {"value": 800, "question": "Emerson, Lake & Palmer often adapted this Russian composer's work, especially 'Pictures at an Exhibition.'", "answer": "Who is Modest Mussorgsky?"},
                        {"value": 1000, "question": "This Rush drummer and lyricist joined after the band's debut album and became one of rock's most revered percussionists.", "answer": "Who is Neil Peart?"},
                    ],
                },
                {
                    "title": "Name the Band by the Lineup",
                    "clues": [
                        {"value": 200, "question": "Robert Plant, Jimmy Page, John Paul Jones, and John Bonham.", "answer": "Who are Led Zeppelin?"},
                        {"value": 400, "question": "Roger Daltrey, Pete Townshend, John Entwistle, and Keith Moon.", "answer": "Who are The Who?"},
                        {"value": 600, "question": "Steven Tyler, Joe Perry, Brad Whitford, Tom Hamilton, and Joey Kramer.", "answer": "Who are Aerosmith?"},
                        {"value": 800, "question": "Mick Fleetwood, John McVie, Christine McVie, Lindsey Buckingham, and Stevie Nicks.", "answer": "Who are Fleetwood Mac?"},
                        {"value": 1000, "question": "David Crosby, Stephen Stills, Graham Nash, and occasionally this fourth man.", "answer": "Who is Neil Young?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: Beatles Legacy",
        "question": "After the Beatles broke up, this member became the first to score a U.S. number-one single with 'My Sweet Lord' and later helped launch a landmark major rock charity concert.",
        "answer": "Who is George Harrison?"
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