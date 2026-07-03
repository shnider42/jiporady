from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Jiporady: History",
    "subtitle": "Round 1 covers intermediate world history; Double Jiporady narrows in on the American Civil War.",
    "rounds": {
        "round_1": {
            "name": "Round 1",
            "categories": [
                {
                    "title": "Ancient & Classical",
                    "clues": [
                        {"value": 100, "question": "This city-state defeated Persia at Marathon before becoming the leading naval power of the Delian League.", "answer": "What is Athens?"},
                        {"value": 200, "question": "This Macedonian king built an empire from Greece to Egypt and India before dying in Babylon in 323 BCE.", "answer": "Who is Alexander the Great?"},
                        {"value": 300, "question": "This Roman general crossed the Rubicon in 49 BCE, helping trigger the end of the Roman Republic.", "answer": "Who is Julius Caesar?"},
                        {"value": 400, "question": "This Mauryan emperor promoted Buddhism after the bloody conquest of Kalinga.", "answer": "Who is Ashoka?"},
                        {"value": 500, "question": "This late antique emperor issued the Edict of Milan with Licinius and later presided over the Council of Nicaea.", "answer": "Who is Constantine the Great?"},
                    ],
                },
                {
                    "title": "Empires & States",
                    "clues": [
                        {"value": 100, "question": "This empire ruled from Constantinople and preserved many Roman institutions long after the western empire fell.", "answer": "What is the Byzantine Empire?"},
                        {"value": 200, "question": "This West African empire became famous for gold, salt trade, and the wealthy pilgrimage of Mansa Musa.", "answer": "What is the Mali Empire?"},
                        {"value": 300, "question": "This empire founded by Osman eventually captured Constantinople in 1453.", "answer": "What is the Ottoman Empire?"},
                        {"value": 400, "question": "This Chinese dynasty founded by Kublai Khan linked China to the wider Mongol world.", "answer": "What is the Yuan dynasty?"},
                        {"value": 500, "question": "This Persian empire, founded by Cyrus the Great, was organized into satrapies and challenged the Greek city-states.", "answer": "What is the Achaemenid Empire?"},
                    ],
                },
                {
                    "title": "Revolutions & Republics",
                    "clues": [
                        {"value": 100, "question": "This 1789 event at a Paris fortress became a symbol of the French Revolution.", "answer": "What is the storming of the Bastille?"},
                        {"value": 200, "question": "This 1776 document declared the thirteen colonies independent from Great Britain.", "answer": "What is the Declaration of Independence?"},
                        {"value": 300, "question": "This Caribbean revolution led by enslaved and formerly enslaved people created an independent Haiti.", "answer": "What is the Haitian Revolution?"},
                        {"value": 400, "question": "This 1917 revolution brought the Bolsheviks to power in Russia.", "answer": "What is the October Revolution?"},
                        {"value": 500, "question": "This 1848 manifesto by Marx and Engels called on workers of the world to unite.", "answer": "What is The Communist Manifesto?"},
                    ],
                },
                {
                    "title": "Trade & Encounters",
                    "clues": [
                        {"value": 100, "question": "This network of routes linked China, Central Asia, the Middle East, and Europe through trade in goods and ideas.", "answer": "What is the Silk Road?"},
                        {"value": 200, "question": "This Portuguese explorer's crew completed the first circumnavigation of the globe after his death in the Philippines.", "answer": "Who is Ferdinand Magellan?"},
                        {"value": 300, "question": "This exchange after 1492 moved crops, animals, people, diseases, and ideas between the Americas and Afro-Eurasia.", "answer": "What is the Columbian Exchange?"},
                        {"value": 400, "question": "This Chinese Muslim admiral led massive Ming treasure voyages across the Indian Ocean in the early 1400s.", "answer": "Who is Zheng He?"},
                        {"value": 500, "question": "This 1494 treaty divided newly claimed lands outside Europe between Spain and Portugal.", "answer": "What is the Treaty of Tordesillas?"},
                    ],
                },
                {
                    "title": "Ideas & Reformers",
                    "clues": [
                        {"value": 100, "question": "This German monk's Ninety-five Theses helped launch the Protestant Reformation.", "answer": "Who is Martin Luther?"},
                        {"value": 200, "question": "This Enlightenment thinker argued for separation of powers in The Spirit of the Laws.", "answer": "Who is Montesquieu?"},
                        {"value": 300, "question": "This abolitionist escaped slavery and became a major writer, speaker, and newspaper publisher.", "answer": "Who is Frederick Douglass?"},
                        {"value": 400, "question": "This English philosopher described life in the state of nature as 'solitary, poor, nasty, brutish, and short.'", "answer": "Who is Thomas Hobbes?"},
                        {"value": 500, "question": "This Indian leader used satyagraha and nonviolent resistance against British colonial rule.", "answer": "Who is Mohandas Gandhi?"},
                    ],
                },
                {
                    "title": "Modern Turning Points",
                    "clues": [
                        {"value": 100, "question": "This 1914 assassination in Sarajevo helped trigger World War I.", "answer": "What is the assassination of Archduke Franz Ferdinand?"},
                        {"value": 200, "question": "This 1919 treaty formally ended World War I with Germany and imposed major penalties on it.", "answer": "What is the Treaty of Versailles?"},
                        {"value": 300, "question": "This 1944 Allied landing in Normandy opened a major western front against Nazi Germany.", "answer": "What is D-Day, or Operation Overlord?"},
                        {"value": 400, "question": "This 1947 plan offered U.S. economic aid to help rebuild Western Europe after World War II.", "answer": "What is the Marshall Plan?"},
                        {"value": 500, "question": "This 1989 event became the clearest symbol of the end of Cold War division in Europe.", "answer": "What is the fall of the Berlin Wall?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady: The American Civil War",
            "categories": [
                {
                    "title": "Road to War",
                    "clues": [
                        {"value": 200, "question": "This 1854 law opened Kansas and Nebraska to popular sovereignty and helped destroy the old party system.", "answer": "What is the Kansas-Nebraska Act?"},
                        {"value": 400, "question": "This Supreme Court decision said Congress could not ban slavery in the territories and denied citizenship to Dred Scott.", "answer": "What is Dred Scott v. Sandford?"},
                        {"value": 600, "question": "This abolitionist's 1859 raid on Harpers Ferry intensified Southern fears of slave rebellion.", "answer": "Who is John Brown?"},
                        {"value": 800, "question": "This state was the first to secede after Abraham Lincoln's election in 1860.", "answer": "What is South Carolina?"},
                        {"value": 1000, "question": "This April 1861 attack in Charleston Harbor marked the beginning of open war between Union and Confederate forces.", "answer": "What is Fort Sumter?"},
                    ],
                },
                {
                    "title": "Commanders & Leaders",
                    "clues": [
                        {"value": 200, "question": "This Union general won victories in the West before becoming general-in-chief and later president.", "answer": "Who is Ulysses S. Grant?"},
                        {"value": 400, "question": "This Confederate general commanded the Army of Northern Virginia after earlier service in the U.S. Army.", "answer": "Who is Robert E. Lee?"},
                        {"value": 600, "question": "This Confederate president had earlier served as a U.S. senator and secretary of war.", "answer": "Who is Jefferson Davis?"},
                        {"value": 800, "question": "This Union general captured Atlanta and then led a destructive march across Georgia to the sea.", "answer": "Who is William Tecumseh Sherman?"},
                        {"value": 1000, "question": "This Confederate general earned his famous nickname at First Bull Run and was mortally wounded by friendly fire at Chancellorsville.", "answer": "Who is Stonewall Jackson?"},
                    ],
                },
                {
                    "title": "Battles & Campaigns",
                    "clues": [
                        {"value": 200, "question": "This first major battle of the war near Manassas showed both sides that the conflict would not end quickly.", "answer": "What is the First Battle of Bull Run, or First Manassas?"},
                        {"value": 400, "question": "This September 1862 Maryland battle remains the bloodiest single day in American military history.", "answer": "What is Antietam, or Sharpsburg?"},
                        {"value": 600, "question": "This July 1863 Pennsylvania battle ended Lee's second invasion of the North.", "answer": "What is Gettysburg?"},
                        {"value": 800, "question": "This Mississippi River fortress city surrendered to Grant on July 4, 1863, splitting the Confederacy.", "answer": "What is Vicksburg?"},
                        {"value": 1000, "question": "This 1864 campaign featured weeks of brutal fighting as Grant pushed toward Richmond and Petersburg despite heavy losses.", "answer": "What is the Overland Campaign?"},
                    ],
                },
                {
                    "title": "Emancipation & Politics",
                    "clues": [
                        {"value": 200, "question": "This 1863 presidential order declared enslaved people in rebelling areas to be free.", "answer": "What is the Emancipation Proclamation?"},
                        {"value": 400, "question": "This constitutional amendment, ratified after the war, abolished slavery in the United States.", "answer": "What is the Thirteenth Amendment?"},
                        {"value": 600, "question": "This term was used for enslaved people who escaped to Union lines and were treated as property seized from the enemy.", "answer": "What are contraband?"},
                        {"value": 800, "question": "This 1864 election tested Northern commitment to the war and ended with Lincoln defeating George McClellan.", "answer": "What is the presidential election of 1864?"},
                        {"value": 1000, "question": "This group in Congress pushed for a harder line against the Confederacy and stronger protections for formerly enslaved people.", "answer": "Who are the Radical Republicans?"},
                    ],
                },
                {
                    "title": "Soldiers & Home Front",
                    "clues": [
                        {"value": 200, "question": "This nurse and relief organizer later founded the American Red Cross.", "answer": "Who is Clara Barton?"},
                        {"value": 400, "question": "This African American regiment from the North became famous for its assault on Fort Wagner.", "answer": "What is the 54th Massachusetts Infantry Regiment?"},
                        {"value": 600, "question": "These Northern Democrats opposed the war or Lincoln's policies and were named after a venomous snake.", "answer": "Who are Copperheads?"},
                        {"value": 800, "question": "These 1863 disturbances erupted partly over conscription and racial tensions in the Union's largest city.", "answer": "What are the New York City draft riots?"},
                        {"value": 1000, "question": "This paper currency, not backed by gold or silver at first, helped the Union finance the war.", "answer": "What are greenbacks?"},
                    ],
                },
                {
                    "title": "War's End & Legacy",
                    "clues": [
                        {"value": 200, "question": "Lee surrendered the Army of Northern Virginia to Grant at this Virginia courthouse village in April 1865.", "answer": "What is Appomattox Court House?"},
                        {"value": 400, "question": "This vice president became president after Lincoln was assassinated.", "answer": "Who is Andrew Johnson?"},
                        {"value": 600, "question": "This postwar federal agency assisted formerly enslaved people and poor white Southerners with food, labor contracts, and schools.", "answer": "What is the Freedmen's Bureau?"},
                        {"value": 800, "question": "This constitutional amendment defined national citizenship and promised equal protection of the laws.", "answer": "What is the Fourteenth Amendment?"},
                        {"value": 1000, "question": "This period after the Civil War tried to rebuild the South and define freedom, citizenship, and federal power.", "answer": "What is Reconstruction?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: The War Reframed",
        "question": "Lincoln delivered this brief 1863 address at a battlefield cemetery dedication, arguing that the war tested whether a nation 'conceived in Liberty' could endure.",
        "answer": "What is the Gettysburg Address?",
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
    return {"ok": True, "app": "jiporady-history"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
