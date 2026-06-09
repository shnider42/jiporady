from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {'title': 'Jiporady: Fibre Optics',
 'subtitle': 'From glowing glass and cable colours to dispersion, multiplexing, testing, and network design',
 'rounds': {'round_1': {'name': 'Round 1',
                        'categories': [{'title': 'Light Work',
                                        'clues': [{'value': 100,
                                                   'question': 'The visible beam in many classroom demonstrations is produced by this focused source.',
                                                   'answer': 'Laser'},
                                                  {'value': 200,
                                                   'question': 'A ray changing direction as it enters a different material demonstrates this optical effect.',
                                                   'answer': 'Refraction'},
                                                  {'value': 300,
                                                   'question': 'When illumination bounces from a surface instead of passing through, this phenomenon occurs.',
                                                   'answer': 'Reflection'},
                                                  {'value': 400,
                                                   'question': 'The distance between matching points on successive waves is called this.',
                                                   'answer': 'Wavelength'},
                                                  {'value': 500,
                                                   'question': 'A packet-like unit carrying electromagnetic energy bears this particle name.',
                                                   'answer': 'Photon'}]},
                                       {'title': 'Inside the Cable',
                                        'clues': [{'value': 100,
                                                   'question': 'Signals travel through the central glass region of an optical strand.',
                                                   'answer': 'Core'},
                                                  {'value': 200,
                                                   'question': 'A surrounding layer with lower refractive index keeps rays confined.',
                                                   'answer': 'Cladding'},
                                                  {'value': 300,
                                                   'question': 'The coloured protective coating immediately outside the glass helps prevent scratches and moisture damage.',
                                                   'answer': 'Buffer'},
                                                  {'value': 400,
                                                   'question': 'Aramid yarn often provides tensile strength under this familiar brand name.',
                                                   'answer': 'Kevlar'},
                                                  {'value': 500,
                                                   'question': 'The outermost protective covering around many assemblies has this clothing-inspired name.',
                                                   'answer': 'Jacket'}]},
                                       {'title': 'Connect the Dots',
                                        'clues': [{'value': 100,
                                                   'question': 'This small-form-factor plug uses a latch resembling the one found on Ethernet patch cords.',
                                                   'answer': 'LC'},
                                                  {'value': 200,
                                                   'question': 'A square push-pull plug common in older enterprise installations uses these two letters.',
                                                   'answer': 'SC'},
                                                  {'value': 300,
                                                   'question': 'A round bayonet-style plug frequently seen on test gear carries this abbreviation.',
                                                   'answer': 'ST'},
                                                  {'value': 400,
                                                   'question': 'A multi-fibre push-on interface can carry many strands in one rectangular ferrule.',
                                                   'answer': 'MPO'},
                                                  {'value': 500,
                                                   'question': 'An angled polish reduces back-reflected energy and is identified by these three letters.',
                                                   'answer': 'APC'}]},
                                       {'title': 'Fibre in the Wild',
                                        'clues': [{'value': 100,
                                                   'question': 'A broadband service delivering glass all the way to a residence is shortened to this four-letter term.',
                                                   'answer': 'FTTH'},
                                                  {'value': 200,
                                                   'question': 'Long-distance cables laid across ocean floors form this global communications infrastructure.',
                                                   'answer': 'Submarine network'},
                                                  {'value': 300,
                                                   'question': 'Hospitals use flexible illuminated instruments to examine internal organs through this medical procedure.',
                                                   'answer': 'Endoscopy'},
                                                  {'value': 400,
                                                   'question': 'Decorative lamps with glowing strands became a retro household novelty under this name.',
                                                   'answer': 'Fibre optic lamp'},
                                                  {'value': 500,
                                                   'question': 'Aircraft and industrial systems can measure strain or temperature through this sensing technology.',
                                                   'answer': 'Fibre Bragg grating'}]},
                                       {'title': 'Colourful Signals',
                                        'clues': [{'value': 100,
                                                   'question': 'This familiar hue has a shorter visible wavelength than red.',
                                                   'answer': 'Blue'},
                                                  {'value': 200,
                                                   'question': 'An approximately 850-nanometre source commonly used with multimode links lies in this invisible region.',
                                                   'answer': 'Near infrared'},
                                                  {'value': 300,
                                                   'question': 'Telecommunications often favour roughly 1310 or 1550 nanometres because glass loss is relatively low there.',
                                                   'answer': 'Transmission windows'},
                                                  {'value': 400,
                                                   'question': 'A device separating combined channels by colour performs this function.',
                                                   'answer': 'Demultiplexing'},
                                                  {'value': 500,
                                                   'question': 'Combining multiple optical colours onto one strand is known by this three-letter abbreviation.',
                                                   'answer': 'WDM'}]},
                                       {'title': 'History Through Glass',
                                        'clues': [{'value': 100,
                                                   'question': 'Alexander Graham Bell sent speech on a beam of sunlight with this 1880 invention.',
                                                   'answer': 'Photophone'},
                                                  {'value': 200,
                                                   'question': 'This physicist demonstrated guiding water-borne illumination during a nineteenth-century lecture.',
                                                   'answer': 'John Tyndall'},
                                                  {'value': 300,
                                                   'question': 'The scientist credited with identifying how ultra-pure glass could support long-distance communications later received a Nobel Prize.',
                                                   'answer': 'Charles Kao'},
                                                  {'value': 400,
                                                   'question': 'Corning researchers produced a landmark low-loss strand in 1970 using this material.',
                                                   'answer': 'Fused silica'},
                                                  {'value': 500,
                                                   'question': 'A transparent strand carrying images was first developed for medical viewing and helped lead toward this instrument.',
                                                   'answer': 'Gastroscope'}]}]},
            'round_2': {'name': 'Double Jiporady',
                        'categories': [{'title': 'Modes & Motion',
                                        'clues': [{'value': 200,
                                                   'question': 'A narrow core permits only one propagation path in this cable class.',
                                                   'answer': 'Single mode'},
                                                  {'value': 400,
                                                   'question': 'A larger central region supports many ray paths and is widely used for shorter premises links.',
                                                   'answer': 'Multimode'},
                                                  {'value': 600,
                                                   'question': 'Different routes arriving at different times create this pulse-spreading impairment.',
                                                   'answer': 'Modal dispersion'},
                                                  {'value': 800,
                                                   'question': 'Varying wavelengths travel at slightly different velocities, producing this form of broadening.',
                                                   'answer': 'Chromatic dispersion'},
                                                  {'value': 1000,
                                                   'question': 'Random birefringence causes two orthogonal states to arrive separately, abbreviated PMD.',
                                                   'answer': 'Polarization mode dispersion'}]},
                                       {'title': 'Loss Budget',
                                        'clues': [{'value': 200,
                                                   'question': 'Power reduction per kilometre is typically expressed in this logarithmic unit.',
                                                   'answer': 'Decibels'},
                                                  {'value': 400,
                                                   'question': 'Microscopic density fluctuations scatter shorter wavelengths through this named mechanism.',
                                                   'answer': 'Rayleigh scattering'},
                                                  {'value': 600,
                                                   'question': 'A bend large enough to let energy escape from the guiding region creates this type of loss.',
                                                   'answer': 'Macrobending'},
                                                  {'value': 800,
                                                   'question': 'Tiny local deformations caused by pressure or imperfect cabling produce this related impairment.',
                                                   'answer': 'Microbending'},
                                                  {'value': 1000,
                                                   'question': 'The sum of launch power, receiver sensitivity, component penalties, and engineering margin forms this design calculation.',
                                                   'answer': 'Link budget'}]},
                                       {'title': 'Clean, Inspect, Connect',
                                        'clues': [{'value': 200,
                                                   'question': 'The first recommended action before mating two ferrules is usually this housekeeping step.',
                                                   'answer': 'Inspection'},
                                                  {'value': 400,
                                                   'question': 'A dry reel or lint-free swab removes contamination through this maintenance process.',
                                                   'answer': 'Cleaning'},
                                                  {'value': 600,
                                                   'question': 'A precision ceramic sleeve aligns two connector tips inside this passive component.',
                                                   'answer': 'Adapter'},
                                                  {'value': 800,
                                                   'question': 'Joining bare strands by melting their ends together uses this permanent technique.',
                                                   'answer': 'Fusion splicing'},
                                                  {'value': 1000,
                                                   'question': 'A poor termination can send energy backward toward the transmitter, quantified by this measurement.',
                                                   'answer': 'Return loss'}]},
                                       {'title': 'Test Bench',
                                        'clues': [{'value': 200,
                                                   'question': 'A simple visible red source helps locate breaks, sharp bends, and incorrect routing.',
                                                   'answer': 'Visual fault locator'},
                                                  {'value': 400,
                                                   'question': 'A calibrated source paired with a meter measures end-to-end attenuation through this method.',
                                                   'answer': 'Optical loss test set'},
                                                  {'value': 600,
                                                   'question': 'An instrument sends pulses and plots reflections versus distance to find events along a span.',
                                                   'answer': 'OTDR'},
                                                  {'value': 800,
                                                   'question': 'A reference spool placed before the link allows the near-end connector to be characterized outside the dead zone.',
                                                   'answer': 'Launch cable'},
                                                  {'value': 1000,
                                                   'question': 'The minimum separation needed for an instrument to distinguish two nearby reflections defines this specification.',
                                                   'answer': 'Event resolution'}]},
                                       {'title': 'Network Architecture',
                                        'clues': [{'value': 200,
                                                   'question': 'A passive access design shares one feeder among many customers using splitters.',
                                                   'answer': 'PON'},
                                                  {'value': 400,
                                                   'question': 'In a central office, this device serves as the provider-side endpoint for many subscribers.',
                                                   'answer': 'OLT'},
                                                  {'value': 600,
                                                   'question': 'At the customer premises, this unit converts incoming light into usable data interfaces.',
                                                   'answer': 'ONT'},
                                                  {'value': 800,
                                                   'question': 'A topology sending traffic both clockwise and counterclockwise can survive a single cut.',
                                                   'answer': 'Resilient ring'},
                                                  {'value': 1000,
                                                   'question': 'Intermediate nodes add or remove selected wavelengths without converting every channel to electronics.',
                                                   'answer': 'ROADM'}]},
                                       {'title': 'Deep Light',
                                        'clues': [{'value': 200,
                                                   'question': 'Guidance occurs when rays strike the boundary beyond a threshold angle and remain trapped.',
                                                   'answer': 'Total internal reflection'},
                                                  {'value': 400,
                                                   'question': 'The sine of the acceptance angle multiplied by the surrounding refractive index defines this quantity.',
                                                   'answer': 'Numerical aperture'},
                                                  {'value': 600,
                                                   'question': 'A dimensionless parameter combining radius, wavelength, and refractive indices predicts how many paths can propagate.',
                                                   'answer': 'V number'},
                                                  {'value': 800,
                                                   'question': "At very high intensity, a channel can alter its own phase because the medium's index depends on power.",
                                                   'answer': 'Kerr effect'},
                                                  {'value': 1000,
                                                   'question': 'Three carriers interact in a nonlinear medium so that two channels generate new frequencies under this process.',
                                                   'answer': 'Four wave mixing'}]}]}},
 'final': {'category': 'Final Jiporady: Long-Haul Breakthroughs',
           'question': 'A device using a rare-earth element near 1550 nanometres boosts many wavelengths directly, avoiding repeated conversion into electronics.',
           'answer': 'Erbium-doped fibre amplifier'}}


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
    return {"ok": True, "app": "jiporady-fibre-optics"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
