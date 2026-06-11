from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Jiporady: JDM Cars",
    "subtitle": "From tuner icons and drifting to chassis codes, engines, homologation specials, and import lore",
    "rounds": {
        "round_1": {
            "name": "Round 1",
            "categories": [
                {
                    "title": "Nameplate Legends",
                    "clues": [
                        {"value": 100, "question": "A80 coupe fame exploded after big-screen quarter-mile glory and a famously stout 2JZ heart.", "answer": "Toyota Supra"},
                        {"value": 200, "question": "Hiroshima sports machine with sequential twin turbos and a spinning-triangle personality.", "answer": "Mazda RX-7"},
                        {"value": 300, "question": "Turbo all-wheel-drive hero nicknamed Godzilla came from the R32 through R34 family.", "answer": "Nissan Skyline GT-R"},
                        {"value": 400, "question": "Mid-engine aluminum supercar development included input from Ayrton Senna.", "answer": "Honda NSX"},
                        {"value": 500, "question": "Rally-bred sedan lineage is usually shortened to Evo by fans.", "answer": "Mitsubishi Lancer Evolution"},
                    ],
                },
                {
                    "title": "Brands & Badges",
                    "clues": [
                        {"value": 100, "question": "A red oval badge fronts many Corolla, Celica, and Chaser builds.", "answer": "Toyota"},
                        {"value": 200, "question": "A winged M once appeared on old Familia and Cosmo models.", "answer": "Mazda"},
                        {"value": 300, "question": "A red central wordmark sits on many Z, Silvia, and Laurel grilles.", "answer": "Nissan"},
                        {"value": 400, "question": "Boxer engines and symmetrical all-wheel drive define much of this brand's enthusiast identity.", "answer": "Subaru"},
                        {"value": 500, "question": "Three diamonds mark machines such as Starion, Pajero, and GTO.", "answer": "Mitsubishi"},
                    ],
                },
                {
                    "title": "Pop Culture Garage",
                    "clues": [
                        {"value": 100, "question": "Tofu delivery, downhill battles, and eurobeat define this manga-and-anime racing series.", "answer": "Initial D"},
                        {"value": 200, "question": "The orange hero car driven by Han in Tokyo Drift wore this wild body-kit line.", "answer": "VeilSide Fortune"},
                        {"value": 300, "question": "License tests, endurance events, and huge Japanese vehicle lists helped make this PlayStation series famous.", "answer": "Gran Turismo"},
                        {"value": 400, "question": "A green S15 in Tokyo Drift receives this art-world nickname.", "answer": "Mona Lisa"},
                        {"value": 500, "question": "The 2001 street-racing film introduced many Americans to tuner culture and a bright orange Mk IV.", "answer": "Fast & Furious"},
                    ],
                },
                {
                    "title": "Drift & Track Talk",
                    "clues": [
                        {"value": 100, "question": "Sending the rear sideways under control is this motorsport style.", "answer": "Drifting"},
                        {"value": 200, "question": "Mountain-pass runs in Japan are known by this term.", "answer": "Touge"},
                        {"value": 300, "question": "A lap battle against the stopwatch rather than wheel-to-wheel opponents.", "answer": "Time attack"},
                        {"value": 400, "question": "Maintaining traction and clean racing line instead of intentional slides is called this.", "answer": "Grip driving"},
                        {"value": 500, "question": "A quick pedal stab can break rear traction during a slide.", "answer": "Clutch kick"},
                    ],
                },
                {
                    "title": "Little Cars, Big Personality",
                    "clues": [
                        {"value": 100, "question": "Tiny tax-friendly Japanese vehicles obey strict size and displacement limits.", "answer": "Kei car"},
                        {"value": 200, "question": "A small roadster with coffee-themed naming came from the company behind the Jimny.", "answer": "Suzuki Cappuccino"},
                        {"value": 300, "question": "Gullwing micro-sports machine sold through a short-lived youth-oriented dealership channel.", "answer": "Autozam AZ-1"},
                        {"value": 400, "question": "Pininfarina-styled mid-engine roadster shared its badge with a musical pulse.", "answer": "Honda Beat"},
                        {"value": 500, "question": "Retractable-hardtop micro roadster came from the company known for Mira and Move.", "answer": "Daihatsu Copen"},
                    ],
                },
                {
                    "title": "Parts People Argue About",
                    "clues": [
                        {"value": 100, "question": "This device uses exhaust energy to force extra air into cylinders.", "answer": "Turbocharger"},
                        {"value": 200, "question": "A traction-aiding rear unit helps both drive wheels share torque instead of one freely spinning.", "answer": "Limited-slip differential"},
                        {"value": 300, "question": "Adjustable spring-and-damper assemblies lower ride height and tune handling.", "answer": "Coilovers"},
                        {"value": 400, "question": "A heat exchanger cools compressed intake charge before combustion.", "answer": "Intercooler"},
                        {"value": 500, "question": "The loud whoosh between shifts often comes from this pressure-release component.", "answer": "Blow-off valve"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady",
            "categories": [
                {
                    "title": "Chassis Code Challenge",
                    "clues": [
                        {"value": 200, "question": "Hachi-roku refers to this Corolla generation loved for lightweight rear-drive balance.", "answer": "AE86"},
                        {"value": 400, "question": "Early Silvia and 180SX builds from the late eighties and early nineties share this platform label.", "answer": "S13"},
                        {"value": 600, "question": "The first modern Godzilla generation dominated Group A touring-car racing.", "answer": "R32"},
                        {"value": 800, "question": "The fourth-generation Supra's internal label uses these five characters.", "answer": "JZA80"},
                        {"value": 1000, "question": "The final RX-7 generation is known by this four-character identifier.", "answer": "FD3S"},
                    ],
                },
                {
                    "title": "Engine Bay Alphabet Soup",
                    "clues": [
                        {"value": 200, "question": "Twin-turbo straight-six powering the fourth-generation Supra Turbo.", "answer": "2JZ-GTE"},
                        {"value": 400, "question": "The legendary Skyline GT-R inline-six uses individual throttle bodies and twin snails.", "answer": "RB26DETT"},
                        {"value": 600, "question": "Turbo four-cylinder commonly swapped into 240SX drift builds.", "answer": "SR20DET"},
                        {"value": 800, "question": "Iron-block four-cylinder powering many Evolution generations and DSM relatives.", "answer": "4G63T"},
                        {"value": 1000, "question": "High-revving 1.6-liter Type R motor from the EK9 Civic.", "answer": "B16B"},
                    ],
                },
                {
                    "title": "Homologation & Rally Royalty",
                    "clues": [
                        {"value": 200, "question": "Touring-car rules helped create R32's racing monster; name this classification.", "answer": "Group A"},
                        {"value": 400, "question": "Top international rally series crowned many Impreza and Lancer legends.", "answer": "WRC"},
                        {"value": 600, "question": "Wide-bodied limited Impreza coupe celebrated a famous rally era.", "answer": "22B STI"},
                        {"value": 800, "question": "Toyota's turbo all-wheel-drive rally weapon carried this hyphenated model name.", "answer": "Celica GT-Four"},
                        {"value": 1000, "question": "Mitsubishi built this Dakar-ready road-going special with swollen fenders and unusual suspension.", "answer": "Pajero Evolution"},
                    ],
                },
                {
                    "title": "Auction Sheet & Import Lore",
                    "clues": [
                        {"value": 200, "question": "U.S. enthusiasts often wait a quarter century before importing vehicles under this exemption.", "answer": "25-year rule"},
                        {"value": 400, "question": "Japan's periodic roadworthiness inspection can make older ownership expensive.", "answer": "Shaken"},
                        {"value": 600, "question": "On many auction sheets, this single-letter rating can indicate repaired history.", "answer": "Grade R"},
                        {"value": 800, "question": "Mileage fraud involving a lower displayed reading is called this.", "answer": "Odometer rollback"},
                        {"value": 1000, "question": "Export paperwork proving a vehicle was removed from Japanese registration is this document.", "answer": "Deregistration certificate"},
                    ],
                },
                {
                    "title": "Tuning Houses & Shops",
                    "clues": [
                        {"value": 200, "question": "This three-letter firm is famous for purple-and-green branding, turbos, and exhaust systems.", "answer": "HKS"},
                        {"value": 400, "question": "A gold high-speed Supra from this shop became legend in highway-run folklore.", "answer": "Top Secret"},
                        {"value": 600, "question": "Circuit-focused Honda builds with blue-and-yellow livery come from this company.", "answer": "Spoon Sports"},
                        {"value": 800, "question": "Rotary specialists from Chiba created many famous RX-7 demo cars.", "answer": "RE Amemiya"},
                        {"value": 1000, "question": "A white Skyline tuned by this shop appeared in Best Motoring battles as a response-focused benchmark.", "answer": "Mine's"},
                    ],
                },
                {
                    "title": "Deep Cut Tech",
                    "clues": [
                        {"value": 200, "question": "Honda's cam-profile switching system became a meme when high-rpm lobes engaged.", "answer": "VTEC"},
                        {"value": 400, "question": "Skyline GT-R torque distribution system sends power forward when sensors demand it.", "answer": "ATTESA E-TS"},
                        {"value": 600, "question": "Nissan's rear-steering setup was fitted to several performance chassis.", "answer": "Super HICAS"},
                        {"value": 800, "question": "Driver-controlled center differential in many rally-bred Subarus uses this four-letter abbreviation.", "answer": "DCCD"},
                        {"value": 1000, "question": "Mitsubishi's yaw-managing rear differential technology wore these three letters.", "answer": "AYC"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: Deep JDM Lore",
        "question": "This R33-based road car used the RBX-GT2 motor and advertised roughly 400 horsepower.",
        "answer": "Nismo 400R",
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
    return {"ok": True, "app": "jiporady-jdm-cars"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
