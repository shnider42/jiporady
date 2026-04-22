from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {'title': 'Block Jiporady',
 'subtitle': 'What is... punch the tree first?',
 'rounds': {'round_1': {'name': 'Round 1',
                        'categories': [{'title': 'Alpha to 1.0',
                                        'clues': [{'value': 100,
                                                   'question': "Markus Persson's 2009 prototype was first released to the public under this blunt two-word title.",
                                                   'answer': 'What is Cave Game?'},
                                                  {'value': 200,
                                                   'question': 'The Halloween Update added this fiery dimension built around fortresses, soul sand, and travel shortcuts.',
                                                   'answer': 'What is the Nether?'},
                                                  {'value': 300,
                                                   'question': 'In 2014, Mojang was purchased by this technology giant.',
                                                   'answer': 'What is Microsoft?'},
                                                  {'value': 400,
                                                   'question': 'Players gave this nickname to the 1.13 backend overhaul that replaced old numeric block IDs with namespaced ones.',
                                                   'answer': 'What is The Flattening?'},
                                                  {'value': 500,
                                                   'question': 'The 1.13 content wave featuring coral, drowned, and shipwrecks was marketed under this title.',
                                                   'answer': 'What is Update Aquatic?'}]},
                                       {'title': 'Read the Terrain',
                                        'clues': [{'value': 100,
                                                   'question': 'This fungus-covered biome is the only overworld one where most hostile nighttime spawns never naturally appear.',
                                                   'answer': 'What are Mushroom Fields?'},
                                                  {'value': 200,
                                                   'question': 'Formerly called mesa, this striped landscape is notable for terracotta layers and unusually common gold ore.',
                                                   'answer': 'What are the Badlands?'},
                                                  {'value': 300,
                                                   'question': 'This conifer biome variant naturally generates podzol and giant 2x2 pines instead of spruces.',
                                                   'answer': 'What is Old Growth Pine Taiga?'},
                                                  {'value': 400,
                                                   'question': 'Blue orchids occur naturally only in this damp biome filled with vines, murky water, and frequent slime spawns under the right moon phase.',
                                                   'answer': 'What is the Swamp?'},
                                                  {'value': 500,
                                                   'question': 'Towering packed frozen formations define this rare biome variant.',
                                                   'answer': 'What is Ice Spikes?'}]},
                                       {'title': 'Things That Want You Dead',
                                        'clues': [{'value': 100,
                                                   'question': 'This tall teleporting attacker can be provoked simply by making direct eye contact.',
                                                   'answer': 'What is an Enderman?'},
                                                  {'value': 200,
                                                   'question': 'This smaller venomous arachnid is found naturally in abandoned mineshaft spawners.',
                                                   'answer': 'What is a Cave Spider?'},
                                                  {'value': 300,
                                                   'question': 'This axe-carrying illager appears in raids and famously shouts through woodland mansions.',
                                                   'answer': 'What is a Vindicator?'},
                                                  {'value': 400,
                                                   'question': 'This ocean-monument ruler inflicts Mining Fatigue from a distance before you even reach its room.',
                                                   'answer': 'What is an Elder Guardian?'},
                                                  {'value': 500,
                                                   'question': 'Arrange soul sand or soul soil in a T-shape, add three black skulls, and you create this boss.',
                                                   'answer': 'What is the Wither?'}]},
                                       {'title': 'Bookish Violence',
                                        'clues': [{'value': 100,
                                                   'question': 'This bow enchantment sets projectiles ablaze.',
                                                   'answer': 'What is Flame?'},
                                                  {'value': 200,
                                                   'question': 'This fishing-rod enchantment improves treasure odds while reducing junk catches.',
                                                   'answer': 'What is Luck of the Sea?'},
                                                  {'value': 300,
                                                   'question': 'This crossbow-only option fires three projectiles at once.',
                                                   'answer': 'What is Multishot?'},
                                                  {'value': 400,
                                                   'question': 'This enchantment lets you collect certain ores, glasslike blocks, or grass-covered blocks intact instead of receiving their usual drops.',
                                                   'answer': 'What is Silk Touch?'},
                                                  {'value': 500,
                                                   'question': 'This trident enchantment turns rainstorms, rivers, and shorelines into launch opportunities.',
                                                   'answer': 'What is Riptide?'}]},
                                       {'title': 'Where It Spawned',
                                        'clues': [{'value': 100,
                                                   'question': 'This underground strongpoint contains the only naturally generated frame that leads to the dragon fight.',
                                                   'answer': 'What is a Stronghold?'},
                                                  {'value': 200,
                                                   'question': 'Tripwire traps, puzzle levers, and mossy stone define this overgrown ruin.',
                                                   'answer': 'What is a Jungle Temple?'},
                                                  {'value': 300,
                                                   'question': 'Cartographers can sell maps leading to this enormous illager-filled building.',
                                                   'answer': 'What is a Woodland Mansion?'},
                                                  {'value': 400,
                                                   'question': 'Suspicious sand and a TNT floor trap are classic features of this sandstone monument.',
                                                   'answer': 'What is a Desert Pyramid?'},
                                                  {'value': 500,
                                                   'question': "This vast deepslate ruin is home to the game's blind apex predator and large concentrations of sculk.",
                                                   'answer': 'What is an Ancient City?'}]},
                                       {'title': 'Benchmade',
                                        'clues': [{'value': 100,
                                                   'question': 'One blaze rod plus three cobblestone crafts this potion workstation.',
                                                   'answer': 'What is a Brewing Stand?'},
                                                  {'value': 200,
                                                   'question': 'Nether quartz, stone, and redstone torches combine into this signal-measuring device.',
                                                   'answer': 'What is a Comparator?'},
                                                  {'value': 300,
                                                   'question': 'Four obsidian, two diamonds, and a book produce this block used for magical gear upgrades.',
                                                   'answer': 'What is an Enchanting Table?'},
                                                  {'value': 400,
                                                   'question': 'Upgrade templates and bullion-based armor improvements require this workstation made from planks and iron.',
                                                   'answer': 'What is a Smithing Table?'},
                                                  {'value': 500,
                                                   'question': 'A heart from the sea surrounded by eight nautilus shells creates this underwater support block.',
                                                   'answer': 'What is a Conduit?'}]}]},
            'round_2': {'name': 'Double Jiporady',
                        'categories': [{'title': 'Redstone Jargon',
                                        'clues': [{'value': 200,
                                                   'question': 'A circuit with two stable states that changes output each time it receives a pulse is called this.',
                                                   'answer': 'What is a T Flip-Flop?'},
                                                  {'value': 400,
                                                   'question': 'This Java-specific quirk lets pistons, droppers, and similar components respond as though power were reaching them from one block higher.',
                                                   'answer': 'What is Quasi-Connectivity?'},
                                                  {'value': 600,
                                                   'question': 'A self-propelled contraption made with slime or honey that carries itself across gaps is known by this term.',
                                                   'answer': 'What is a Flying Machine?'},
                                                  {'value': 800,
                                                   'question': 'Builders use this general term for any setup that emits regular pulses over time.',
                                                   'answer': 'What is a Redstone Clock?'},
                                                  {'value': 1000,
                                                   'question': 'A redstone arrangement that converts a sustained input into one brief output pulse is called this.',
                                                   'answer': 'What is a Monostable Circuit?'}]},
                                       {'title': 'Bottle Logic',
                                        'clues': [{'value': 200,
                                                   'question': 'Nearly every standard potion line starts with this warted fortress crop.',
                                                   'answer': 'What is Nether Wart?'},
                                                  {'value': 400,
                                                   'question': 'Corrupt a Night Vision base with this item and you get a brew that hides the drinker.',
                                                   'answer': 'What is a Fermented Spider Eye?'},
                                                  {'value': 600,
                                                   'question': 'This red mineral usually extends potion duration rather than increasing potency.',
                                                   'answer': 'What is Redstone Dust?'},
                                                  {'value': 800,
                                                   'question': 'Fire Resistance comes from brewing with this ingredient made from a blaze drop and loot from small lava cubes.',
                                                   'answer': 'What is Magma Cream?'},
                                                  {'value': 1000,
                                                   'question': 'Slow Falling comes from this drop harvested from the nocturnal swooping nuisance tied to insomnia mechanics.',
                                                   'answer': 'What is Phantom Membrane?'}]},
                                       {'title': 'Village People',
                                        'clues': [{'value': 200,
                                                   'question': 'An unemployed resident who claims this paper-based workstation becomes a map seller.',
                                                   'answer': 'What is a Cartography Table?'},
                                                  {'value': 400,
                                                   'question': 'Repeatedly applying this rescue method to formerly infected residents once allowed extreme price reductions before balance changes.',
                                                   'answer': 'What is Curing Zombie Villagers?'},
                                                  {'value': 600,
                                                   'question': 'A barrel creates this profession, the one most associated with cod, salmon, and campfires.',
                                                   'answer': 'What is a Fisherman?'},
                                                  {'value': 800,
                                                   'question': 'Beyond enough food, breeding residents requires at least this kind of unclaimed household item for each new arrival.',
                                                   'answer': 'What is a Bed?'},
                                                  {'value': 1000,
                                                   'question': 'Successfully repelling waves after entering a settlement with Bad Omen awards this reputation-boosting status effect.',
                                                   'answer': 'What is Hero of the Village?'}]},
                                       {'title': 'The Nether, Obviously',
                                        'clues': [{'value': 200,
                                                   'question': 'This gold-loving crimson-forest inhabitant can trade with the player but hates careless mining nearby.',
                                                   'answer': 'What is a Piglin?'},
                                                  {'value': 400,
                                                   'question': 'This fortress-dwelling skeletal swordsman is farmed mainly for black skulls.',
                                                   'answer': 'What is a Wither Skeleton?'},
                                                  {'value': 600,
                                                   'question': 'Ancient debris must be smelted into this intermediary material before being combined with gold.',
                                                   'answer': 'What is Netherite Scrap?'},
                                                  {'value': 800,
                                                   'question': 'This saddle-compatible traveler glides over lava and dislikes standing on cold ground.',
                                                   'answer': 'What is a Strider?'},
                                                  {'value': 1000,
                                                   'question': 'Charged with glowstone, this crafted block sets the return point in a dimension where beds explode.',
                                                   'answer': 'What is a Respawn Anchor?'}]},
                                       {'title': 'Patch Notes Memory',
                                        'clues': [{'value': 200,
                                                   'question': 'The release that brought hunger, sprinting, and villages is remembered by this exploratory subtitle.',
                                                   'answer': 'What is the Adventure Update?'},
                                                  {'value': 400,
                                                   'question': "Official horse support arrived in this numbered release after strong influence from Mo' Creatures.",
                                                   'answer': 'What is 1.6?'},
                                                  {'value': 600,
                                                   'question': 'Honey bottles, nests, and sticky honey blocks arrived in this sweetly named release.',
                                                   'answer': 'What is Buzzy Bees?'},
                                                  {'value': 800,
                                                   'question': 'World-height expansion and the new mountain-and-cave terrain generator landed in this second half of the split overhaul.',
                                                   'answer': 'What is 1.18?'},
                                                  {'value': 1000,
                                                   'question': 'Archaeology, camels, bamboo wood sets, and armor trims were bundled under this storytelling-themed title.',
                                                   'answer': 'What is Trails & Tales?'}]},
                                       {'title': 'The Endgame',
                                        'clues': [{'value': 200,
                                                   'question': 'The glass objects atop obsidian pillars serve this function during the first boss battle.',
                                                   'answer': "What is Regenerating the Dragon's Health?"},
                                                  {'value': 400,
                                                   'question': 'Throwing one of these pearl-derived items lets players trace the route to the underground gateway structure.',
                                                   'answer': 'What is an Eye of Ender?'},
                                                  {'value': 600,
                                                   'question': 'Looted from a vessel attached to a distant city, this chest-slot item enables gliding.',
                                                   'answer': 'What is an Elytra?'},
                                                  {'value': 800,
                                                   'question': 'This boxy sentry found around outer-city towers inflicts levitation.',
                                                   'answer': 'What is a Shulker?'},
                                                  {'value': 1000,
                                                   'question': 'To summon the dragon again, four crafted glass-and-ghast items must be placed around the exit fountain.',
                                                   'answer': 'What are End Crystals?'}]}]}},
 'final': {'category': 'Final Jiporady: Technical Oddities',
           'question': "In Java Edition, using this developer's handle on a name tag flips many mobs upside down as an easter egg.",
           'answer': 'What is Dinnerbone?'}}


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
    return {"ok": True, "app": "jiporady_minecraft"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
