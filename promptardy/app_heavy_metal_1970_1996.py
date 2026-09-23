from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Jiporady: Bass, Books, America & Transportation",
    "subtitle": "Bassists and bass lines, 19th-century American literature, American history, and the machines and systems that moved the world.",
    "rounds": {
        "round_1": {
            "name": "Round 1: The Warm-Up",
            "categories": [
                {
                    "title": "Bassists 101",
                    "clues": [
                        {"value": 100, "question": "This left-handed Beatle played bass on songs including 'Come Together' and 'Something.'", "answer": "Who is Paul McCartney?"},
                        {"value": 200, "question": "John Paul Jones played bass and keyboards in this band fronted by Robert Plant.", "answer": "Who are Led Zeppelin?"},
                        {"value": 300, "question": "Flea is the energetic bassist for this California band.", "answer": "Who are the Red Hot Chili Peppers?"},
                        {"value": 400, "question": "This Rush member handled bass, lead vocals, and keyboards.", "answer": "Who is Geddy Lee?"},
                        {"value": 500, "question": "This Metallica bassist played on 'Ride the Lightning' and 'Master of Puppets' before his death in 1986.", "answer": "Who is Cliff Burton?"},
                    ],
                },
                {
                    "title": "Bass Lines & Bands",
                    "clues": [
                        {"value": 100, "question": "John Deacon played the famous bass line on 'Another One Bites the Dust' for this band.", "answer": "Who are Queen?"},
                        {"value": 200, "question": "Roger Waters was the longtime bassist and a principal songwriter for this British band.", "answer": "Who are Pink Floyd?"},
                        {"value": 300, "question": "This bassist and singer formed The Police with Stewart Copeland and Andy Summers.", "answer": "Who is Sting?"},
                        {"value": 400, "question": "Steve Harris founded and plays bass for this British heavy-metal band.", "answer": "Who are Iron Maiden?"},
                        {"value": 500, "question": "Chris Squire's bright, aggressive bass sound was a defining part of this progressive-rock band.", "answer": "Who are Yes?"},
                    ],
                },
                {
                    "title": "19th-Century American Lit",
                    "clues": [
                        {"value": 100, "question": "Herman Melville wrote this novel about Captain Ahab's pursuit of a white whale.", "answer": "What is Moby-Dick?"},
                        {"value": 200, "question": "Nathaniel Hawthorne wrote this novel about Hester Prynne and the letter she is forced to wear.", "answer": "What is The Scarlet Letter?"},
                        {"value": 300, "question": "Walt Whitman's great poetry collection, first published in 1855, has this grassy title.", "answer": "What is Leaves of Grass?"},
                        {"value": 400, "question": "Louisa May Alcott wrote this novel about the March sisters.", "answer": "What is Little Women?"},
                        {"value": 500, "question": "Mark Twain's novel about Huck and Jim traveling down the Mississippi has this title.", "answer": "What is Adventures of Huckleberry Finn?"},
                    ],
                },
                {
                    "title": "American History 101",
                    "clues": [
                        {"value": 100, "question": "The Declaration of Independence was adopted in this year.", "answer": "What is 1776?"},
                        {"value": 200, "question": "This president completed the Louisiana Purchase from France in 1803.", "answer": "Who is Thomas Jefferson?"},
                        {"value": 300, "question": "Abraham Lincoln delivered this brief 1863 speech at a Pennsylvania battlefield cemetery.", "answer": "What is the Gettysburg Address?"},
                        {"value": 400, "question": "This constitutional amendment abolished slavery in the United States.", "answer": "What is the Thirteenth Amendment?"},
                        {"value": 500, "question": "This post-Civil War era attempted to rebuild the South and redefine citizenship and federal power.", "answer": "What is Reconstruction?"},
                    ],
                },
                {
                    "title": "Transportation 101",
                    "clues": [
                        {"value": 100, "question": "Orville and Wilbur of this family made the first successful powered airplane flight in 1903.", "answer": "Who are the Wright brothers?"},
                        {"value": 200, "question": "This vehicle follows rails and may pull passenger or freight cars.", "answer": "What is a locomotive, or train?"},
                        {"value": 300, "question": "Ford introduced this enormously influential automobile in 1908.", "answer": "What is the Model T?"},
                        {"value": 400, "question": "Completed in 1825, this canal linked the Hudson River with the Great Lakes.", "answer": "What is the Erie Canal?"},
                        {"value": 500, "question": "The Union Pacific and Central Pacific railroads met in 1869 at this Utah site.", "answer": "What is Promontory Summit?"},
                    ],
                },
                {
                    "title": "Moving America",
                    "clues": [
                        {"value": 100, "question": "This president signed the 1956 law that launched the modern Interstate Highway System.", "answer": "Who is Dwight D. Eisenhower?"},
                        {"value": 200, "question": "Robert Fulton's commercially successful steamboat, commonly called the Clermont, traveled on this New York river.", "answer": "What is the Hudson River?"},
                        {"value": 300, "question": "Opened in 1883, this famous bridge connected Manhattan and Brooklyn.", "answer": "What is the Brooklyn Bridge?"},
                        {"value": 400, "question": "Completed in 1914, this canal dramatically shortened sea travel between the Atlantic and Pacific.", "answer": "What is the Panama Canal?"},
                        {"value": 500, "question": "Boston opened the first subway tunnel in the United States in 1897 under this street.", "answer": "What is Tremont Street?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady: Deeper Cuts",
            "categories": [
                {
                    "title": "Bassist Deep Cuts",
                    "clues": [
                        {"value": 200, "question": "This Motown session bassist played on scores of hits and was a central member of the Funk Brothers.", "answer": "Who is James Jamerson?"},
                        {"value": 400, "question": "This Los Angeles session bassist, associated with the Wrecking Crew, played on records by artists including the Beach Boys and Nancy Sinatra.", "answer": "Who is Carol Kaye?"},
                        {"value": 600, "question": "This fretless-bass virtuoso joined Weather Report in the 1970s and recorded the composition 'Portrait of Tracy.'", "answer": "Who is Jaco Pastorius?"},
                        {"value": 800, "question": "This Black Sabbath bassist also wrote many of the band's classic lyrics.", "answer": "Who is Geezer Butler?"},
                        {"value": 1000, "question": "Donald 'Duck' Dunn anchored the rhythm section of Booker T. & the M.G.'s and played on many Stax recordings.", "answer": "Who is Donald 'Duck' Dunn?"},
                    ],
                },
                {
                    "title": "American Lit Deep Cuts",
                    "clues": [
                        {"value": 200, "question": "Nathaniel Hawthorne set this 1851 novel in a gloomy ancestral home haunted by an old family curse.", "answer": "What is The House of the Seven Gables?"},
                        {"value": 400, "question": "This formerly enslaved author published his first autobiography, 'Narrative of the Life of...' in 1845.", "answer": "Who is Frederick Douglass?"},
                        {"value": 600, "question": "Kate Chopin's 1899 novel about Edna Pontellier has this title.", "answer": "What is The Awakening?"},
                        {"value": 800, "question": "Stephen Crane wrote this 1895 Civil War novel about young soldier Henry Fleming.", "answer": "What is The Red Badge of Courage?"},
                        {"value": 1000, "question": "Herman Melville created this scrivener who repeatedly says he would 'prefer not to.'", "answer": "Who is Bartleby?"},
                    ],
                },
                {
                    "title": "Authors & Works",
                    "clues": [
                        {"value": 200, "question": "Ralph Waldo Emerson published this 1836 essay that became a foundational text of American Transcendentalism.", "answer": "What is Nature?"},
                        {"value": 400, "question": "Henry David Thoreau described his experiment in simple living in this 1854 book.", "answer": "What is Walden?"},
                        {"value": 600, "question": "This reclusive Amherst poet wrote nearly 1,800 poems, most unpublished during her lifetime.", "answer": "Who is Emily Dickinson?"},
                        {"value": 800, "question": "Harriet Beecher Stowe wrote this enormously influential antislavery novel published in 1852.", "answer": "What is Uncle Tom's Cabin?"},
                        {"value": 1000, "question": "Henry James published this 1881 novel about the independent American Isabel Archer.", "answer": "What is The Portrait of a Lady?"},
                    ],
                },
                {
                    "title": "American History Deep Cuts",
                    "clues": [
                        {"value": 200, "question": "This 1820 agreement admitted Missouri as a slave state and Maine as a free state while restricting slavery north of latitude 36°30′ in the Louisiana Purchase territory.", "answer": "What is the Missouri Compromise?"},
                        {"value": 400, "question": "This 1854 law created the Kansas and Nebraska territories and allowed settlers to decide the slavery question by popular sovereignty.", "answer": "What is the Kansas-Nebraska Act?"},
                        {"value": 600, "question": "This disputed political bargain following the 1876 election is commonly associated with the withdrawal of federal troops from the South.", "answer": "What is the Compromise of 1877?"},
                        {"value": 800, "question": "This 1887 federal law divided many tribal lands into individual allotments in an effort to force assimilation.", "answer": "What is the Dawes Act?"},
                        {"value": 1000, "question": "This 1894 labor conflict began at a railroad-car company town near Chicago and disrupted rail traffic across the country.", "answer": "What is the Pullman Strike?"},
                    ],
                },
                {
                    "title": "Turning Points",
                    "clues": [
                        {"value": 200, "question": "This 1803 Supreme Court case established the principle of judicial review.", "answer": "What is Marbury v. Madison?"},
                        {"value": 400, "question": "This 1823 foreign-policy statement warned European powers against new colonization in the Western Hemisphere.", "answer": "What is the Monroe Doctrine?"},
                        {"value": 600, "question": "The 1848 women's-rights convention that issued the Declaration of Sentiments met in this New York town.", "answer": "What is Seneca Falls?"},
                        {"value": 800, "question": "This 1862 law offered western public land to settlers who lived on and improved it.", "answer": "What is the Homestead Act?"},
                        {"value": 1000, "question": "This 1886 Chicago labor rally became infamous after a bomb was thrown and violence erupted.", "answer": "What is the Haymarket affair?"},
                    ],
                },
                {
                    "title": "Transportation Deep Cuts",
                    "clues": [
                        {"value": 200, "question": "George Stephenson's famous 1829 locomotive, winner of the Rainhill Trials, had this speedy name.", "answer": "What is Rocket?"},
                        {"value": 400, "question": "Chartered in 1827, this railroad became the first major common-carrier railroad in the United States.", "answer": "What is the Baltimore and Ohio Railroad, or B&O?"},
                        {"value": 600, "question": "John Kemp Starley's 1885 Rover helped establish this bicycle design with similarly sized wheels and chain drive to the rear wheel.", "answer": "What is the safety bicycle?"},
                        {"value": 800, "question": "This German engineer developed the compression-ignition engine that bears his name in the 1890s.", "answer": "Who is Rudolf Diesel?"},
                        {"value": 1000, "question": "Opened in 1897, this Boston tunnel was the first subway tunnel in the United States.", "answer": "What is the Tremont Street Subway?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: Transportation History",
        "question": "Opened in 1825, this English railway is widely recognized as the first public railway to use steam locomotives to carry both freight and passengers.",
        "answer": "What is the Stockton and Darlington Railway?",
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
    return {"ok": True, "app": "jiporady-heavy-metal-1970-1996"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
