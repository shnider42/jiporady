from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Beverage Jiporady",
    "subtitle": "What is... something to drink?",
    "rounds": {
        "round_1": {
            "name": "Round 1",
            "categories": [
                {
                    "title": "Coffee Basics",
                    "clues": [
                        {"value": 100, "question": "This hot drink is commonly made by brewing ground roasted beans.", "answer": "What is coffee?"},
                        {"value": 200, "question": "A shot of this concentrated coffee is the base for many café drinks.", "answer": "What is espresso?"},
                        {"value": 300, "question": "This drink is typically espresso topped with steamed milk and a layer of foam.", "answer": "What is a latte?"},
                        {"value": 400, "question": "This Italian coffee dessert drink is flavored with cocoa and often means 'pick me up.'", "answer": "What is tiramisu coffee's cousin, cappuccino?"},
                        {"value": 500, "question": "Beans for this style of coffee are roasted longer, giving a bolder and less acidic flavor.", "answer": "What is dark roast?"},
                    ],
                },
                {
                    "title": "Tea Time",
                    "clues": [
                        {"value": 100, "question": "This common tea variety shares its name with a color.", "answer": "What is black tea?"},
                        {"value": 200, "question": "This tea is known for its minimal oxidation and fresh grassy flavor.", "answer": "What is green tea?"},
                        {"value": 300, "question": "A blend of black tea, milk, spices, and sweetener is often called this.", "answer": "What is chai?"},
                        {"value": 400, "question": "This tea is naturally caffeine-free and is often made from flowers rather than tea leaves.", "answer": "What is herbal tea?"},
                        {"value": 500, "question": "This British tea tradition is named for a meal between lunch and dinner.", "answer": "What is afternoon tea?"},
                    ],
                },
                {
                    "title": "Bubbles & Fizz",
                    "clues": [
                        {"value": 100, "question": "This generic term describes a sweet carbonated soft drink.", "answer": "What is soda?"},
                        {"value": 200, "question": "This cola brand shares its name with a drug once used medicinally.", "answer": "What is Coca-Cola?"},
                        {"value": 300, "question": "This lemon-lime soda brand is often called clear instead of dark.", "answer": "What is Sprite?"},
                        {"value": 400, "question": "These tiny gas pockets give sparkling water its fizz.", "answer": "What are bubbles?"},
                        {"value": 500, "question": "This gas is added to many soft drinks to make them carbonated.", "answer": "What is carbon dioxide?"},
                    ],
                },
                {
                    "title": "Juicy Details",
                    "clues": [
                        {"value": 100, "question": "This citrus juice is most associated with breakfast tables.", "answer": "What is orange juice?"},
                        {"value": 200, "question": "This tart red juice is commonly linked with cranberries.", "answer": "What is cranberry juice?"},
                        {"value": 300, "question": "Juice made from this fruit is often cloudy and can be sweet or tart depending on the variety.", "answer": "What is apple juice?"},
                        {"value": 400, "question": "This tropical juice comes from a fruit with a spiky exterior and sweet yellow flesh.", "answer": "What is pineapple juice?"},
                        {"value": 500, "question": "This ruby-colored juice comes from a fruit also associated with the myth of Persephone.", "answer": "What is pomegranate juice?"},
                    ],
                },
                {
                    "title": "Milk Matters",
                    "clues": [
                        {"value": 100, "question": "This dairy beverage comes most commonly from cows.", "answer": "What is milk?"},
                        {"value": 200, "question": "This chocolate-flavored version of milk is popular in school cafeterias.", "answer": "What is chocolate milk?"},
                        {"value": 300, "question": "This milk alternative is made from oats and has become popular in coffee shops.", "answer": "What is oat milk?"},
                        {"value": 400, "question": "This nut-based milk alternative is one of the most common non-dairy options.", "answer": "What is almond milk?"},
                        {"value": 500, "question": "Milk heated just below boiling and treated to kill harmful microbes is called this.", "answer": "What is pasteurized milk?"},
                    ],
                },
                {
                    "title": "Smooth Operators",
                    "clues": [
                        {"value": 100, "question": "This blended drink often combines fruit, ice, and yogurt or milk.", "answer": "What is a smoothie?"},
                        {"value": 200, "question": "A banana and strawberry version of this drink is a common café favorite.", "answer": "What is a smoothie?"},
                        {"value": 300, "question": "This green smoothie ingredient is also the title of a leafy comic-strip vegetable in some jokes.", "answer": "What is spinach?"},
                        {"value": 400, "question": "This thick tropical smoothie ingredient has a large pit in the center.", "answer": "What is mango?"},
                        {"value": 500, "question": "This ingredient is often added to smoothies for protein and probiotic benefits.", "answer": "What is yogurt?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady",
            "categories": [
                {
                    "title": "Mocktails & More",
                    "clues": [
                        {"value": 200, "question": "This word describes a mixed drink without alcohol.", "answer": "What is a mocktail?"},
                        {"value": 400, "question": "A Shirley Temple is traditionally made with ginger ale or lemon-lime soda and this bright red garnish fruit.", "answer": "What is a cherry?"},
                        {"value": 600, "question": "This sour citrus juice is commonly used to brighten mocktails and cocktails alike.", "answer": "What is lime juice?"},
                        {"value": 800, "question": "This sparkling nonalcoholic beverage is simply water with carbonation.", "answer": "What is sparkling water?"},
                        {"value": 1000, "question": "This sweetener, made by dissolving sugar in water, is a bar staple.", "answer": "What is simple syrup?"},
                    ],
                },
                {
                    "title": "Around the World",
                    "clues": [
                        {"value": 200, "question": "This tea ceremony beverage is famously associated with Japan.", "answer": "What is matcha?"},
                        {"value": 400, "question": "This yogurt-based salty drink is popular in parts of the Middle East and South Asia.", "answer": "What is lassi?"},
                        {"value": 600, "question": "This South American herbal drink is sipped from a gourd through a metal straw.", "answer": "What is yerba mate?"},
                        {"value": 800, "question": "This thick Mexican drink made from masa can be served hot or cold.", "answer": "What is atole?"},
                        {"value": 1000, "question": "This fermented milk drink is popular in Eastern Europe and the Caucasus region.", "answer": "What is kefir?"},
                    ],
                },
                {
                    "title": "Café Menu",
                    "clues": [
                        {"value": 200, "question": "Espresso with a larger amount of hot water added becomes this drink.", "answer": "What is an Americano?"},
                        {"value": 400, "question": "A cappuccino is typically made of espresso, steamed milk, and this top layer.", "answer": "What is foam?"},
                        {"value": 600, "question": "This coffee drink is usually stronger and smaller than a latte, with less milk.", "answer": "What is a macchiato?"},
                        {"value": 800, "question": "Coffee chilled and poured over cubes of frozen water is described with this one word.", "answer": "What is iced?"},
                        {"value": 1000, "question": "This method of making coffee involves water slowly dripping through grounds held in a paper or metal cone.", "answer": "What is pour-over coffee?"},
                    ],
                },
                {
                    "title": "Famous Ingredients",
                    "clues": [
                        {"value": 200, "question": "This stimulant is found naturally in coffee and many teas.", "answer": "What is caffeine?"},
                        {"value": 400, "question": "This yellow citrus fruit is often sliced into tea.", "answer": "What is lemon?"},
                        {"value": 600, "question": "This spice, common in chai and autumn drinks, comes from tree bark.", "answer": "What is cinnamon?"},
                        {"value": 800, "question": "This dark sweetener made from sugarcane is often associated with rum and ginger drinks.", "answer": "What is molasses?"},
                        {"value": 1000, "question": "This bean gives vanilla extract its flavor and shares its name with a pale off-white color.", "answer": "What is vanilla?"},
                    ],
                },
                {
                    "title": "Breakfast in a Glass",
                    "clues": [
                        {"value": 200, "question": "This pink juice is most commonly made from grapefruit.", "answer": "What is grapefruit juice?"},
                        {"value": 400, "question": "A drink made by blending milk, ice cream, and flavoring is called this.", "answer": "What is a milkshake?"},
                        {"value": 600, "question": "This cultured dairy drink is thinner than yogurt and often sold in probiotic bottles.", "answer": "What is kefir?"},
                        {"value": 800, "question": "This beverage made from soaked grains is often marketed as a breakfast replacement.", "answer": "What is a meal shake?"},
                        {"value": 1000, "question": "This hot breakfast drink is made by simmering cocoa powder or chocolate with milk or water.", "answer": "What is hot chocolate?"},
                    ],
                },
                {
                    "title": "Name That Beverage",
                    "clues": [
                        {"value": 200, "question": "Mint leaves, lime, sugar, and soda water are key parts of this classic Cuban-style drink.", "answer": "What is a mojito?"},
                        {"value": 400, "question": "Espresso poured over cold milk and ice usually makes this café staple.", "answer": "What is an iced latte?"},
                        {"value": 600, "question": "This drink mixes tea, lemonade, and usually ice for a refreshing combo.", "answer": "What is an Arnold Palmer?"},
                        {"value": 800, "question": "This spicy soft drink is flavored with ginger.", "answer": "What is ginger ale?"},
                        {"value": 1000, "question": "This frothy Indian café drink is made by whipping instant coffee with sugar and hot water, then adding milk.", "answer": "What is dalgona coffee?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: Beverage Basics",
        "question": "This gas is responsible for the fizz in sparkling water and many soft drinks.",
        "answer": "What is carbon dioxide?"
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