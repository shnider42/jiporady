from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Jiporady: Music Theory",
    "subtitle": "From notes, rhythm, and chords to modes, cadences, counterpoint, chromatic harmony, and analysis brain-benders",
    "rounds": {
        "round_1": {
            "name": "Round 1",
            "categories": [
                {
                    "title": "Name That Note",
                    "clues": [
                        {"value": 100, "question": "In standard Western music, the musical alphabet uses these seven letter names.", "answer": "What are A, B, C, D, E, F, and G?"},
                        {"value": 200, "question": "This symbol raises a note by one half step.", "answer": "What is a sharp?"},
                        {"value": 300, "question": "This symbol lowers a note by one half step.", "answer": "What is a flat?"},
                        {"value": 400, "question": "This sign cancels a previous sharp or flat.", "answer": "What is a natural?"},
                        {"value": 500, "question": "The note one half step above E on a piano is usually spelled as this white-key note.", "answer": "What is F?"},
                    ],
                },
                {
                    "title": "Rhythm Basics",
                    "clues": [
                        {"value": 100, "question": "In 4/4 time, this note value usually gets one beat.", "answer": "What is a quarter note?"},
                        {"value": 200, "question": "This time signature is often called common time.", "answer": "What is 4/4?"},
                        {"value": 300, "question": "A dot after a note increases its duration by this fraction of its original value.", "answer": "What is one half?"},
                        {"value": 400, "question": "Three notes played in the time normally given to two are called this.", "answer": "What is a triplet?"},
                        {"value": 500, "question": "The emphasis of weak beats or offbeats is called this.", "answer": "What is syncopation?"},
                    ],
                },
                {
                    "title": "Intervals 101",
                    "clues": [
                        {"value": 100, "question": "Two notes with the same pitch name and pitch level form this interval.", "answer": "What is a unison?"},
                        {"value": 200, "question": "The interval from C up to G is this perfect interval.", "answer": "What is a perfect fifth?"},
                        {"value": 300, "question": "The interval from C up to E is this kind of third.", "answer": "What is a major third?"},
                        {"value": 400, "question": "The interval from C up to Eb is this kind of third.", "answer": "What is a minor third?"},
                        {"value": 500, "question": "An octave spans this many half steps.", "answer": "What is twelve?"},
                    ],
                },
                {
                    "title": "Chord Building",
                    "clues": [
                        {"value": 100, "question": "A basic three-note chord built in thirds is called this.", "answer": "What is a triad?"},
                        {"value": 200, "question": "A major triad contains a root, major third, and this perfect interval above the root.", "answer": "What is a perfect fifth?"},
                        {"value": 300, "question": "A minor triad differs from a major triad mainly by having this kind of third.", "answer": "What is a minor third?"},
                        {"value": 400, "question": "Adding the seventh scale degree above a triad creates this type of four-note chord.", "answer": "What is a seventh chord?"},
                        {"value": 500, "question": "A C major triad contains these three notes.", "answer": "What are C, E, and G?"},
                    ],
                },
                {
                    "title": "Keys & Scales",
                    "clues": [
                        {"value": 100, "question": "The C major scale has this many sharps or flats.", "answer": "What is zero?"},
                        {"value": 200, "question": "This pattern describes a major scale: whole, whole, half, whole, whole, whole, half.", "answer": "What is W-W-H-W-W-W-H?"},
                        {"value": 300, "question": "The first note of a scale, often felt as home base, is called this.", "answer": "What is the tonic?"},
                        {"value": 400, "question": "The key signature with one sharp is this major key.", "answer": "What is G major?"},
                        {"value": 500, "question": "The relative minor of C major is this key.", "answer": "What is A minor?"},
                    ],
                },
                {
                    "title": "Staff & Symbols",
                    "clues": [
                        {"value": 100, "question": "The treble clef is also commonly called this letter-name clef.", "answer": "What is the G clef?"},
                        {"value": 200, "question": "The bass clef is also commonly called this letter-name clef.", "answer": "What is the F clef?"},
                        {"value": 300, "question": "This mark tells a performer to hold a note longer than its written value.", "answer": "What is a fermata?"},
                        {"value": 400, "question": "This Italian dynamic marking means to play softly.", "answer": "What is piano?"},
                        {"value": 500, "question": "This Italian tempo marking generally means walking pace.", "answer": "What is andante?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady",
            "categories": [
                {
                    "title": "Roman Numeral Gauntlet",
                    "clues": [
                        {"value": 200, "question": "In C major, the chord G-B-D-F is analyzed with this Roman numeral.", "answer": "What is V7?"},
                        {"value": 400, "question": "In a major key, a borrowed minor iv chord most often comes from this parallel mode.", "answer": "What is the parallel minor, or Aeolian mode?"},
                        {"value": 600, "question": "In first inversion, a triad is labeled with this figured-bass number.", "answer": "What is 6, or 6/3?"},
                        {"value": 800, "question": "A cadential six-four normally functions as an embellishment of this dominant harmony.", "answer": "What is V?"},
                        {"value": 1000, "question": "In C major, the chord D-F#-A-C is best analyzed as this secondary dominant.", "answer": "What is V7/V?"},
                    ],
                },
                {
                    "title": "Modes With Receipts",
                    "clues": [
                        {"value": 200, "question": "This mode is like a natural minor scale with a raised sixth degree.", "answer": "What is Dorian?"},
                        {"value": 400, "question": "This mode is like a major scale with a raised fourth degree.", "answer": "What is Lydian?"},
                        {"value": 600, "question": "This mode is like a major scale with a lowered seventh degree and is common in blues and rock.", "answer": "What is Mixolydian?"},
                        {"value": 800, "question": "This mode has both a lowered second and lowered fifth degree, making it the most unstable diatonic mode.", "answer": "What is Locrian?"},
                        {"value": 1000, "question": "Starting on E and using only the white keys produces this mode.", "answer": "What is Phrygian?"},
                    ],
                },
                {
                    "title": "Cadences & Voice Leading",
                    "clues": [
                        {"value": 200, "question": "A V-to-I motion at the end of a phrase is this strong cadence type.", "answer": "What is an authentic cadence?"},
                        {"value": 400, "question": "A cadence ending on V is commonly called this, because it sounds unfinished.", "answer": "What is a half cadence?"},
                        {"value": 600, "question": "The deceptive cadence V to vi in major avoids resolving to this expected tonic chord.", "answer": "What is I?"},
                        {"value": 800, "question": "In strict four-part writing, leading tones generally resolve by step in this direction.", "answer": "What is upward?"},
                        {"value": 1000, "question": "Moving from one perfect fifth or octave to another perfect fifth or octave in the same two voices creates this forbidden parallel motion.", "answer": "What are parallel perfect fifths or octaves?"},
                    ],
                },
                {
                    "title": "Chromatic Harmony",
                    "clues": [
                        {"value": 200, "question": "This predominant chord is a major chord built on lowered scale degree 2 and is usually heard in first inversion before V.", "answer": "What is a Neapolitan sixth chord?"},
                        {"value": 400, "question": "Italian, French, and German varieties of this chord family usually contain scale degrees flat 6 and sharp 4.", "answer": "What are augmented sixth chords?"},
                        {"value": 600, "question": "A fully diminished seventh chord built on the raised fourth scale degree can function as this secondary leading-tone chord to V.", "answer": "What is vii°7/V?"},
                        {"value": 800, "question": "In common-practice harmony, a German augmented sixth can resemble this dominant seventh chord by enharmonic spelling.", "answer": "What is V7?"},
                        {"value": 1000, "question": "A modulation by reinterpretation of the same diminished seventh sonority under a new spelling is called this kind of modulation.", "answer": "What is enharmonic modulation?"},
                    ],
                },
                {
                    "title": "Jazz Theory Trapdoors",
                    "clues": [
                        {"value": 200, "question": "In jazz, the progression Dm7-G7-Cmaj7 in C is commonly called this three-chord sequence.", "answer": "What is a ii-V-I?"},
                        {"value": 400, "question": "A tritone substitution for G7 usually uses this dominant seventh chord.", "answer": "What is Db7?"},
                        {"value": 600, "question": "The altered scale is the seventh mode of this melodic minor scale, a half step above the altered dominant root.", "answer": "What is melodic minor?"},
                        {"value": 800, "question": "A dominant seventh chord with both a sharp 9 and flat 13 is often described with this broad chord-quality term.", "answer": "What is altered dominant?"},
                        {"value": 1000, "question": "John Coltrane's rapid major-third key cycle, heard in 'Giant Steps,' is often nicknamed this.", "answer": "What are Coltrane changes?"},
                    ],
                },
                {
                    "title": "Counterpoint & Form",
                    "clues": [
                        {"value": 200, "question": "In species counterpoint, one note against one note is called this species.", "answer": "What is first species?"},
                        {"value": 400, "question": "A melody that accompanies the subject consistently in a fugue is called this.", "answer": "What is a countersubject?"},
                        {"value": 600, "question": "A fugue answer transposed exactly to the dominant without interval changes is called this kind of answer.", "answer": "What is a real answer?"},
                        {"value": 800, "question": "In sonata form, the section that destabilizes and travels through keys after the exposition is called this.", "answer": "What is the development?"},
                        {"value": 1000, "question": "A Baroque bass line repeated throughout a piece while upper voices vary above it is called this.", "answer": "What is a ground bass, or basso ostinato?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: Functional Harmony",
        "question": "In C major, the chord D-F#-A-C most directly tonicizes G and is analyzed with this Roman numeral.",
        "answer": "What is V7/V?",
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
    return {"ok": True, "app": "jiporady-music-theory"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
