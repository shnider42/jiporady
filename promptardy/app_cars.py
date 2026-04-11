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
                    "title": "Car Brands",
                    "clues": [
                        {"value": 100, "question": "This Japanese brand's logo is made of three overlapping ovals.", "answer": "What is Toyota?"},
                        {"value": 200, "question": "This German luxury automaker uses a four-ring logo.", "answer": "What is Audi?"},
                        {"value": 300, "question": "This American brand is famous for the Mustang.", "answer": "What is Ford?"},
                        {"value": 400, "question": "This Italian automaker's road cars often wear a prancing horse badge.", "answer": "What is Ferrari?"},
                        {"value": 500, "question": "This South Korean automaker owns the Genesis luxury brand.", "answer": "What is Hyundai?"},
                    ],
                },
                {
                    "title": "Parts of a Car",
                    "clues": [
                        {"value": 100, "question": "This rubber part is mounted on a wheel and touches the road.", "answer": "What is a tire?"},
                        {"value": 200, "question": "This pedal, found between the brake and accelerator in many manual cars, is used to change gears.", "answer": "What is the clutch?"},
                        {"value": 300, "question": "These front lights are used to help drivers see at night.", "answer": "What are headlights?"},
                        {"value": 400, "question": "This device recharges the battery while the engine is running.", "answer": "What is the alternator?"},
                        {"value": 500, "question": "This engine component opens and closes to let fuel-air mixture in and exhaust out.", "answer": "What is a valve?"},
                    ],
                },
                {
                    "title": "Classic Models",
                    "clues": [
                        {"value": 100, "question": "Volkswagen's famous small rounded people car is commonly known by this insect nickname.", "answer": "What is the Beetle?"},
                        {"value": 200, "question": "Chevrolet's long-running sports car is often called 'America's sports car.'", "answer": "What is the Corvette?"},
                        {"value": 300, "question": "This Ford pony car debuted for the 1965 model year and launched a whole vehicle segment.", "answer": "What is the Mustang?"},
                        {"value": 400, "question": "The Porsche 911 is best known as this type of vehicle.", "answer": "What is a sports car?"},
                        {"value": 500, "question": "The Model T was built by this company.", "answer": "What is Ford?"},
                    ],
                },
                {
                    "title": "On the Dashboard",
                    "clues": [
                        {"value": 100, "question": "This gauge shows how fast the car is moving.", "answer": "What is the speedometer?"},
                        {"value": 200, "question": "This warning light often looks like an old-fashioned oil can.", "answer": "What is the oil pressure light?"},
                        {"value": 300, "question": "This gauge measures how fast the engine is spinning, usually in RPM.", "answer": "What is the tachometer?"},
                        {"value": 400, "question": "This warning light tells you the charging system may have a problem.", "answer": "What is the battery light?"},
                        {"value": 500, "question": "ABS stands for this braking system.", "answer": "What is Anti-lock Braking System?"},
                    ],
                },
                {
                    "title": "Motorsport Basics",
                    "clues": [
                        {"value": 100, "question": "In racing, this flag means the session or race is over.", "answer": "What is the checkered flag?"},
                        {"value": 200, "question": "NASCAR is best known for racing these body styles.", "answer": "What are stock cars?"},
                        {"value": 300, "question": "F1 is short for this top international open-wheel series.", "answer": "What is Formula 1?"},
                        {"value": 400, "question": "At Indianapolis, drivers compete in this famous 500-mile race.", "answer": "What is the Indianapolis 500?"},
                        {"value": 500, "question": "A race team's stop for tires and fuel happens in this lane.", "answer": "What is pit lane?"},
                    ],
                },
                {
                    "title": "Road Trip Stuff",
                    "clues": [
                        {"value": 100, "question": "This device or app commonly gives turn-by-turn directions.", "answer": "What is GPS?"},
                        {"value": 200, "question": "This area at the back of many sedans stores luggage.", "answer": "What is the trunk?"},
                        {"value": 300, "question": "This simple maintenance task means adding air when your tires are low.", "answer": "What is inflating the tires?"},
                        {"value": 400, "question": "Cruise control is mainly used to keep the car at a steady this.", "answer": "What is speed?"},
                        {"value": 500, "question": "This emergency item can be used to raise a car when changing a flat tire.", "answer": "What is a jack?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady",
            "categories": [
                {
                    "title": "Automotive History",
                    "clues": [
                        {"value": 200, "question": "This Ford vehicle made the moving assembly line famous in early mass production.", "answer": "What is the Model T?"},
                        {"value": 400, "question": "This Detroit automaker was founded by Walter Chrysler in 1925.", "answer": "What is Chrysler?"},
                        {"value": 600, "question": "This 1955 Mercedes-Benz gullwing model is known by the internal name 300SL.", "answer": "What is the Mercedes-Benz 300SL?"},
                        {"value": 800, "question": "This oil crisis decade pushed many buyers toward smaller, more fuel-efficient cars.", "answer": "What are the 1970s?"},
                        {"value": 1000, "question": "This Japanese brand's early U.S. luxury success was driven by models like the LS 400.", "answer": "What is Lexus?"},
                    ],
                },
                {
                    "title": "Engines & Drivetrains",
                    "clues": [
                        {"value": 200, "question": "EV stands for this type of vehicle.", "answer": "What is an electric vehicle?"},
                        {"value": 400, "question": "AWD is the abbreviation for this drivetrain layout.", "answer": "What is all-wheel drive?"},
                        {"value": 600, "question": "A turbocharger forces more of this into the engine to help make extra power.", "answer": "What is air?"},
                        {"value": 800, "question": "In a front-engine rear-wheel-drive car, engine power is commonly sent to the rear axle through this long rotating shaft.", "answer": "What is the driveshaft?"},
                        {"value": 1000, "question": "This engine layout has cylinders arranged in two banks forming a V, like a V8.", "answer": "What is a V engine?"},
                    ],
                },
                {
                    "title": "Luxury & Exotic",
                    "clues": [
                        {"value": 200, "question": "This British brand is closely associated with James Bond and makes the DB series.", "answer": "What is Aston Martin?"},
                        {"value": 400, "question": "This Italian maker builds the Huracán and Revuelto.", "answer": "What is Lamborghini?"},
                        {"value": 600, "question": "This ultra-luxury British marque makes the Phantom and Ghost.", "answer": "What is Rolls-Royce?"},
                        {"value": 800, "question": "This French hypercar brand, revived under Volkswagen Group, builds the Chiron.", "answer": "What is Bugatti?"},
                        {"value": 1000, "question": "This Mercedes-Benz high-performance division takes its initials from Aufrecht, Melcher, and Großaspach.", "answer": "What is AMG?"},
                    ],
                },
                {
                    "title": "Famous Race Tracks",
                    "clues": [
                        {"value": 200, "question": "This Florida oval hosts the Daytona 500.", "answer": "What is Daytona International Speedway?"},
                        {"value": 400, "question": "This famous 24-hour endurance race is held in a city in northwestern France.", "answer": "What is Le Mans?"},
                        {"value": 600, "question": "Monaco's Formula 1 race is run on streets in this tiny principality.", "answer": "What is Monaco?"},
                        {"value": 800, "question": "This Indiana speedway is nicknamed 'The Brickyard.'", "answer": "What is Indianapolis Motor Speedway?"},
                        {"value": 1000, "question": "Germany's Nürburgring Nordschleife is often called this two-word nickname meaning 'green hell.'", "answer": "What is the Green Hell?"},
                    ],
                },
                {
                    "title": "Pickups, SUVs & 4x4",
                    "clues": [
                        {"value": 200, "question": "This long-running Ford pickup line has been America's best-selling truck series for decades.", "answer": "What is the F-Series?"},
                        {"value": 400, "question": "Jeep's iconic off-roader with removable doors and roof is this model.", "answer": "What is the Wrangler?"},
                        {"value": 600, "question": "This Toyota SUV shares its name with a geographic term meaning a journey over land.", "answer": "What is the Land Cruiser?"},
                        {"value": 800, "question": "4WD stands for this.", "answer": "What is four-wheel drive?"},
                        {"value": 1000, "question": "This body-on-frame American SUV, reintroduced by Ford for 2021, revived a famous off-road nameplate.", "answer": "What is the Bronco?"},
                    ],
                },
                {
                    "title": "Car Culture",
                    "clues": [
                        {"value": 200, "question": "A car with three pedals usually has this type of transmission.", "answer": "What is a manual transmission?"},
                        {"value": 400, "question": "The initials JDM stand for this national car market and style scene.", "answer": "What is Japanese Domestic Market?"},
                        {"value": 600, "question": "This muscle car term usually refers to the cubic-inch-displacement V8 era of the 1960s and early 1970s in the U.S.", "answer": "What is the muscle car era?"},
                        {"value": 800, "question": "A car's horsepower is a measure of this.", "answer": "What is power?"},
                        {"value": 1000, "question": "In enthusiast slang, a 'sleeper' is a car that looks ordinary but is secretly this.", "answer": "What is very fast?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: Automotive History",
        "question": "Introduced for the 1965 model year, this Ford launched the original 'pony car' craze in the United States.",
        "answer": "What is the Ford Mustang?"
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
