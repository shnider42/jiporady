from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Jiporady: Polish History",
    "subtitle": "Round 1 in English, Double Jiporady po polsku — made to be fair but not patronizing for a Polish player",
    "rounds": {
        "round_1": {
            "name": "Round 1",
            "categories": [
                {
                    "title": "Early Poland",
                    "clues": [
                        {"value": 100, "question": "This Piast ruler's baptism in 966 is often treated as the symbolic beginning of the Polish state.", "answer": "Who is Mieszko I?"},
                        {"value": 200, "question": "Mieszko I and Bolesław the Brave belonged to this first historic ruling dynasty of Poland.", "answer": "What is the Piast dynasty?"},
                        {"value": 300, "question": "This son of Mieszko I became Poland's first crowned king in 1025.", "answer": "Who is Bolesław I the Brave, or Bolesław Chrobry?"},
                        {"value": 400, "question": "This city, associated with St. Adalbert and the early archbishopric, was a major symbolic capital of early Poland.", "answer": "What is Gniezno?"},
                        {"value": 500, "question": "This king, remembered as 'the Great,' founded the Kraków Academy and is linked to the saying that he found Poland wooden and left it made of stone.", "answer": "Who is Casimir III the Great, or Kazimierz Wielki?"},
                    ],
                },
                {
                    "title": "Commonwealth Basics",
                    "clues": [
                        {"value": 100, "question": "The 1569 Union of Lublin created the Polish-Lithuanian version of this political entity.", "answer": "What is the Polish-Lithuanian Commonwealth?"},
                        {"value": 200, "question": "This grand duchy was Poland's partner in the Commonwealth formed by the Union of Lublin.", "answer": "What is the Grand Duchy of Lithuania?"},
                        {"value": 300, "question": "This noble estate dominated Commonwealth politics and guarded its privileges fiercely.", "answer": "What is the szlachta?"},
                        {"value": 400, "question": "Because monarchs were chosen rather than simply inherited, Commonwealth kings came to the throne through this process.", "answer": "What is a royal election, or free election?"},
                        {"value": 500, "question": "This parliamentary privilege allowed one deputy to block legislation and became a symbol of the Commonwealth's political dysfunction.", "answer": "What is the liberum veto?"},
                    ],
                },
                {
                    "title": "Kings & Battles",
                    "clues": [
                        {"value": 100, "question": "This queen of Poland married Jogaila, helping connect Poland and Lithuania under the Jagiellonian dynasty.", "answer": "Who is Jadwiga?"},
                        {"value": 200, "question": "At this 1410 battle, Polish-Lithuanian forces defeated the Teutonic Knights.", "answer": "What is the Battle of Grunwald, or Tannenberg?"},
                        {"value": 300, "question": "This king led the relief of Vienna in 1683 against the Ottoman army.", "answer": "Who is Jan III Sobieski?"},
                        {"value": 400, "question": "These famous Polish heavy cavalrymen are strongly associated with spectacular charges and feathered back frames.", "answer": "Who are the Winged Hussars, or husaria?"},
                        {"value": 500, "question": "This Transylvanian-born elected king strengthened the army and fought Muscovy in the Livonian War.", "answer": "Who is Stefan Batory?"},
                    ],
                },
                {
                    "title": "Partitions & Uprisings",
                    "clues": [
                        {"value": 100, "question": "The three partitioning powers of Poland were Russia, Prussia, and this Habsburg monarchy.", "answer": "What is Austria?"},
                        {"value": 200, "question": "The First Partition of Poland took place in this year.", "answer": "What is 1772?"},
                        {"value": 300, "question": "Adopted in 1791, this reform document is celebrated on a major Polish holiday every May 3.", "answer": "What is the Constitution of 3 May?"},
                        {"value": 400, "question": "This 1794 national uprising is named for a Polish and American revolutionary hero.", "answer": "What is the Kościuszko Uprising?"},
                        {"value": 500, "question": "This 1863 uprising against Russian rule became the longest-lasting major Polish insurrection of the partition era.", "answer": "What is the January Uprising?"},
                    ],
                },
                {
                    "title": "World War II Poland",
                    "clues": [
                        {"value": 100, "question": "This small Polish military transit depot near Gdańsk became a symbol of resistance in September 1939.", "answer": "What is Westerplatte?"},
                        {"value": 200, "question": "This underground military organization, abbreviated AK in Polish, was the main armed force of the Polish Underground State.", "answer": "What is the Home Army, or Armia Krajowa?"},
                        {"value": 300, "question": "This 1943 uprising was a Jewish resistance action against the German liquidation of the Warsaw Ghetto.", "answer": "What is the Warsaw Ghetto Uprising?"},
                        {"value": 400, "question": "This 1944 battle was launched by the Home Army in an attempt to liberate Poland's capital before the Red Army arrived.", "answer": "What is the Warsaw Uprising?"},
                        {"value": 500, "question": "This Polish officer deliberately entered Auschwitz, organized intelligence there, escaped, and later wrote reports about the camp.", "answer": "Who is Witold Pilecki?"},
                    ],
                },
                {
                    "title": "Communism & Freedom",
                    "clues": [
                        {"value": 100, "question": "This city gave its name to the June 1956 workers' protests that shook communist Poland.", "answer": "What is Poznań?"},
                        {"value": 200, "question": "Born Karol Wojtyła, this Polish pope became a major spiritual symbol for many Poles under communism.", "answer": "Who is Pope John Paul II?"},
                        {"value": 300, "question": "This independent trade union emerged from the 1980 strikes in Gdańsk.", "answer": "What is Solidarność, or Solidarity?"},
                        {"value": 400, "question": "On December 13, 1981, General Wojciech Jaruzelski imposed this emergency system to crush Solidarity.", "answer": "What is martial law?"},
                        {"value": 500, "question": "These 1989 negotiations between the communist government and the opposition helped open the way to semi-free elections.", "answer": "What are the Round Table Talks?"},
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Double Jiporady",
            "categories": [
                {
                    "title": "Piastowie bez rozgrzewki",
                    "clues": [
                        {"value": 200, "question": "Ten władca przyjął chrzest w 966 roku.", "answer": "Kim był Mieszko I?"},
                        {"value": 400, "question": "Ta czeska księżniczka, żona Mieszka I, jest tradycyjnie łączona z chrystianizacją jego państwa.", "answer": "Kim była Dobrawa?"},
                        {"value": 600, "question": "Ten pierwszy koronowany król Polski nosił przydomek Chrobry.", "answer": "Kim był Bolesław I Chrobry?"},
                        {"value": 800, "question": "Ten dokument z 1138 roku podzielił państwo między synów Bolesława Krzywoustego.", "answer": "Czym był testament Bolesława Krzywoustego?"},
                        {"value": 1000, "question": "Ten ostatni król z dynastii Piastów założył Akademię Krakowską w 1364 roku.", "answer": "Kim był Kazimierz Wielki?"},
                    ],
                },
                {
                    "title": "Rzeczpospolita Obojga Narodów",
                    "clues": [
                        {"value": 200, "question": "Ta unia z 1569 roku połączyła Koronę i Wielkie Księstwo Litewskie w Rzeczpospolitą Obojga Narodów.", "answer": "Czym była unia lubelska?"},
                        {"value": 400, "question": "Tym słowem określa się uprzywilejowany stan szlachecki w dawnej Polsce.", "answer": "Czym była szlachta?"},
                        {"value": 600, "question": "Ten mechanizm wyboru monarchy sprawiał, że po śmierci Zygmunta Augusta królowie byli wybierani przez szlachtę.", "answer": "Czym była wolna elekcja?"},
                        {"value": 800, "question": "Ta zasada sejmowa pozwalała jednemu posłowi zerwać obrady i unieważnić uchwały.", "answer": "Czym było liberum veto?"},
                        {"value": 1000, "question": "Ten król, wybrany w 1576 roku, prowadził skuteczne wojny z Moskwą o Inflanty.", "answer": "Kim był Stefan Batory?"},
                    ],
                },
                {
                    "title": "Rozbiory i opór",
                    "clues": [
                        {"value": 200, "question": "Tak nazywa się konfederacja magnacka z 1792 roku, która sprzeciwiła się reformom Konstytucji 3 maja.", "answer": "Czym była konfederacja targowicka?"},
                        {"value": 400, "question": "Te trzy państwa dokonały rozbiorów Rzeczypospolitej.", "answer": "Czym były Rosja, Prusy i Austria?"},
                        {"value": 600, "question": "Ten naczelnik insurekcji z 1794 roku wcześniej walczył także w wojnie o niepodległość Stanów Zjednoczonych.", "answer": "Kim był Tadeusz Kościuszko?"},
                        {"value": 800, "question": "To powstanie przeciw Rosji wybuchło w nocy z 29 na 30 listopada 1830 roku.", "answer": "Czym było powstanie listopadowe?"},
                        {"value": 1000, "question": "To powstanie z 1863 roku rozpoczęło się między innymi jako reakcja na brankę do armii rosyjskiej.", "answer": "Czym było powstanie styczniowe?"},
                    ],
                },
                {
                    "title": "Dwudziestolecie",
                    "clues": [
                        {"value": 200, "question": "Ten polityk i wojskowy jest szczególnie kojarzony z odzyskaniem niepodległości 11 listopada 1918 roku.", "answer": "Kim był Józef Piłsudski?"},
                        {"value": 400, "question": "Ta bitwa z 1920 roku bywa nazywana Cudem nad Wisłą.", "answer": "Czym była Bitwa Warszawska?"},
                        {"value": 600, "question": "To miasto portowe stało się jednym z największych symboli gospodarczej ambicji II RP.", "answer": "Czym była Gdynia?"},
                        {"value": 800, "question": "Ten skrót oznacza wielki projekt industrializacyjny II RP w południowo-centralnej Polsce.", "answer": "Czym był COP, czyli Centralny Okręg Przemysłowy?"},
                        {"value": 1000, "question": "Ta konstytucja z 1935 roku wzmocniła pozycję prezydenta w systemie politycznym II RP.", "answer": "Czym była konstytucja kwietniowa?"},
                    ],
                },
                {
                    "title": "Wojna i okupacja",
                    "clues": [
                        {"value": 200, "question": "Ten punkt oporu w Wolnym Mieście Gdańsku bronił się na początku września 1939 roku.", "answer": "Czym było Westerplatte?"},
                        {"value": 400, "question": "Tak nazywała się konspiracyjna organizacja harcerska działająca podczas okupacji.", "answer": "Czym były Szare Szeregi?"},
                        {"value": 600, "question": "Ta tajna organizacja Rady Pomocy Żydom działała pod kryptonimem na literę Ż.", "answer": "Czym była Żegota?"},
                        {"value": 800, "question": "To powstanie w 1944 roku trwało 63 dni.", "answer": "Czym było powstanie warszawskie?"},
                        {"value": 1000, "question": "Ta zbrodnia z 1940 roku obejmowała masowe mordy polskich oficerów i przedstawicieli elit przez NKWD.", "answer": "Czym była zbrodnia katyńska?"},
                    ],
                },
                {
                    "title": "PRL i Solidarność",
                    "clues": [
                        {"value": 200, "question": "Ten robotniczy protest z 1956 roku wybuchł w stolicy Wielkopolski.", "answer": "Czym był Poznański Czerwiec?"},
                        {"value": 400, "question": "Ten miesiąc 1968 roku kojarzy się w PRL z protestami studenckimi i kampanią antysemicką.", "answer": "Czym był Marzec 1968?"},
                        {"value": 600, "question": "Te protesty na Wybrzeżu w 1970 roku zostały krwawo stłumione po podwyżkach cen żywności.", "answer": "Czym był Grudzień 1970?"},
                        {"value": 800, "question": "Ten Komitet, założony w 1976 roku, pomagał represjonowanym robotnikom po protestach w Radomiu i Ursusie.", "answer": "Czym był KOR, czyli Komitet Obrony Robotników?"},
                        {"value": 1000, "question": "Te rozmowy z 1989 roku między władzą a opozycją poprzedziły częściowo wolne wybory czerwcowe.", "answer": "Czym były obrady Okrągłego Stołu?"},
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Finał Jiporady: Konstytucja",
        "question": "Ten akt uchwalony przez Sejm Wielki w 1791 roku jest świętowany w Polsce 3 maja.",
        "answer": "Czym była Konstytucja 3 maja?",
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
    return {"ok": True, "app": "jiporady-polish-history"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
