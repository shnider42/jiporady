from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Jiporady: Honey Bees",
    "subtitle": "From hive jobs and waggle dances to wax, queens, swarms, and pollination power",
    "rounds": {
        "round_1": {
            "name": "Round 1",
            "categories": [
                {
                    "title": "Hive Jobs",
                    "clues": [
                        {"value": 100, "question": "This egg-laying female is usually the mother of nearly every bee in the colony.", "answer": "What is the queen bee?"},
                        {"value": 200, "question": "These female bees clean cells, feed larvae, build comb, guard entrances, and eventually forage.", "answer": "What are worker bees?"},
                        {"value": 300, "question": "These male bees do not gather nectar or pollen; their main role is mating with queens.", "answer": "What are drones?"},
                        {"value": 400, "question": "Young workers that feed developing larvae are commonly called this kind of bee.", "answer": "What are nurse bees?"},
                        {"value": 500, "question": "Older workers that leave the hive to collect nectar, pollen, water, or resin are known by this job title.", "answer": "What are forager bees?"},
                    ],
                },
                {
                    "title": "Bee Bodies",
                    "clues": [
                        {"value": 100, "question": "Honey bees have this many main body sections: head, thorax, and abdomen.", "answer": "What is three?"},
                        {"value": 200, "question": "This straw-like mouthpart helps a honey bee drink nectar.", "answer": "What is a proboscis?"},
                        {"value": 300, "question": "These two feelers detect odors, touch, humidity, and other chemical cues.", "answer": "What are antennae?"},
                        {"value": 400, "question": "Worker bees carry pollen on these basket-like structures on their hind legs.", "answer": "What are pollen baskets, or corbiculae?"},
                        {"value": 500, "question": "Honey bees have two large compound eyes plus this many small simple eyes called ocelli.", "answer": "What is three?"},
                    ],
                },
                {
                    "title": "Honey & Wax",
                    "clues": [
                        {"value": 100, "question": "Bees collect this sweet liquid from flowers and transform it into honey.", "answer": "What is nectar?"},
                        {"value": 200, "question": "The hexagonal wax structure where bees raise brood and store food is called this.", "answer": "What is honeycomb?"},
                        {"value": 300, "question": "Worker bees fan their wings to reduce this in nectar as it ripens into honey.", "answer": "What is water content?"},
                        {"value": 400, "question": "Bees seal ripe honey cells with this material.", "answer": "What is beeswax?"},
                        {"value": 500, "question": "The stomach-like storage organ used to carry nectar back to the hive is often called this.", "answer": "What is the honey stomach, or crop?"},
                    ],
                },
                {
                    "title": "Pollination Power",
                    "clues": [
                        {"value": 100, "question": "This powder from flowers sticks to bees and can fertilize other flowers.", "answer": "What is pollen?"},
                        {"value": 200, "question": "Moving pollen from the male part of a flower to the female part is called this.", "answer": "What is pollination?"},
                        {"value": 300, "question": "This sweet floral reward attracts bees and becomes the starting ingredient for honey.", "answer": "What is nectar?"},
                        {"value": 400, "question": "When pollen moves between different plants of the same species, it is this kind of pollination.", "answer": "What is cross-pollination?"},
                        {"value": 500, "question": "Many beekeepers rent hives to farms so bees can pollinate these tree-nut blossoms in early spring.", "answer": "What are almond blossoms?"},
                    ],
                },
                {
                    "title": "Bee Behavior",
                    "clues": [
                        {"value": 100, "question": "This famous figure-eight movement tells nestmates about the direction and distance of food.", "answer": "What is the waggle dance?"},
                        {"value": 200, "question": "A colony reproduces at the group level when a queen leaves with many workers in one of these.", "answer": "What is a swarm?"},
                        {"value": 300, "question": "Bees share food mouth-to-mouth in this social feeding behavior.", "answer": "What is trophallaxis?"},
                        {"value": 400, "question": "Chemical signals used by queens, workers, and brood to coordinate hive life are called these.", "answer": "What are pheromones?"},
                        {"value": 500, "question": "In cold weather, honey bees huddle into this moving ball to conserve heat.", "answer": "What is a winter cluster?"},
                    ],
                },
                {
                    "title": "Beekeeper Gear",
                    "clues": [
                        {"value": 100, "question": "A human-managed honey bee home is commonly called this.", "answer": "What is a hive?"},
                        {"value": 200, "question": "Beekeepers use this tool to puff cool smoke and help calm a colony during inspections.", "answer": "What is a smoker?"},
                        {"value": 300, "question": "This mesh face covering helps protect a beekeeper's head from stings.", "answer": "What is a veil?"},
                        {"value": 400, "question": "Removable rectangular pieces that hold comb inside many modern hives are called these.", "answer": "What are frames?"},
                        {"value": 500, "question": "This grid-like barrier can keep the queen out of honey supers while workers pass through.", "answer": "What is a queen excluder?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady",
            "categories": [
                {
                    "title": "Life Cycle",
                    "clues": [
                        {"value": 200, "question": "The first stage of a honey bee's life is this tiny object laid by the queen.", "answer": "What is an egg?"},
                        {"value": 400, "question": "After hatching, a young bee spends time as this grub-like feeding stage.", "answer": "What is a larva?"},
                        {"value": 600, "question": "During this stage, the bee transforms inside a capped cell.", "answer": "What is the pupa stage?"},
                        {"value": 800, "question": "A fertilized egg can develop into this female caste when fed and raised in a special queen cell.", "answer": "What is a queen?"},
                        {"value": 1000, "question": "A worker honey bee typically emerges from its egg after about this many days.", "answer": "What is 21 days?"},
                    ],
                },
                {
                    "title": "Hive Threats",
                    "clues": [
                        {"value": 200, "question": "This parasitic mite is one of the most serious pests of managed honey bee colonies.", "answer": "What is Varroa destructor, or the varroa mite?"},
                        {"value": 400, "question": "This mysterious-sounding term describes a pattern of worker disappearance and colony failure.", "answer": "What is colony collapse disorder?"},
                        {"value": 600, "question": "These crop-protection chemicals can harm bees when exposure is high or poorly managed.", "answer": "What are pesticides?"},
                        {"value": 800, "question": "This invader can slime stored comb and is especially troublesome in weak colonies.", "answer": "What is the small hive beetle?"},
                        {"value": 1000, "question": "This spore-forming gut parasite group can weaken adult honey bees.", "answer": "What is Nosema?"},
                    ],
                },
                {
                    "title": "Bee Relatives",
                    "clues": [
                        {"value": 200, "question": "This fuzzy bee type often nests in small colonies and can buzz-pollinate tomatoes.", "answer": "What is a bumblebee?"},
                        {"value": 400, "question": "This large solitary bee can tunnel into wood, giving it a construction-related name.", "answer": "What is a carpenter bee?"},
                        {"value": 600, "question": "Honey bees belong to this genus name, also Latin for bee.", "answer": "What is Apis?"},
                        {"value": 800, "question": "Honey bees and wasps are both in this insect order that also includes ants.", "answer": "What is Hymenoptera?"},
                        {"value": 1000, "question": "This species name is commonly used for the western honey bee kept by many beekeepers.", "answer": "What is Apis mellifera?"},
                    ],
                },
                {
                    "title": "Bee Words",
                    "clues": [
                        {"value": 200, "question": "A place where beehives are kept is called this.", "answer": "What is an apiary?"},
                        {"value": 400, "question": "The practice of keeping bees is called this.", "answer": "What is apiculture?"},
                        {"value": 600, "question": "A person who keeps bees can be called this.", "answer": "What is an apiarist?"},
                        {"value": 800, "question": "This term describes honey made mostly from the nectar of one plant species.", "answer": "What is monofloral honey?"},
                        {"value": 1000, "question": "The scientific study of bees is known by this word.", "answer": "What is melittology?"},
                    ],
                },
                {
                    "title": "Products of the Hive",
                    "clues": [
                        {"value": 200, "question": "This resin-like material is collected from plants and used by bees as hive sealant.", "answer": "What is propolis?"},
                        {"value": 400, "question": "This protein-rich food is packed into cells and fed to developing brood.", "answer": "What is bee bread?"},
                        {"value": 600, "question": "This glandular food is famously associated with queen development.", "answer": "What is royal jelly?"},
                        {"value": 800, "question": "Ferment honey with water and you can make this ancient alcoholic drink.", "answer": "What is mead?"},
                        {"value": 1000, "question": "This product of a sting is studied for its defensive proteins and peptides.", "answer": "What is bee venom?"},
                    ],
                },
                {
                    "title": "Deep Hive Science",
                    "clues": [
                        {"value": 200, "question": "Male honey bees develop from unfertilized eggs, a system called this.", "answer": "What is haplodiploidy?"},
                        {"value": 400, "question": "The queen stores sperm for years in this internal organ.", "answer": "What is the spermatheca?"},
                        {"value": 600, "question": "A queen mates in flight at these gathering places used by drones.", "answer": "What are drone congregation areas?"},
                        {"value": 800, "question": "This lemony orientation scent helps workers fan nestmates toward a hive entrance or swarm site.", "answer": "What is Nasonov pheromone?"},
                        {"value": 1000, "question": "This disease-resistance trait involves workers detecting and removing unhealthy brood.", "answer": "What is hygienic behavior?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: Dance of the Bees",
        "question": "This figure-eight communication behavior helps honey bee foragers advertise both direction and distance to a food source.",
        "answer": "What is the waggle dance?",
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
    return {"ok": True, "app": "jiporady-honey-bees"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
