from flask import Flask, jsonify, render_template, request
import os
import random

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-secret-key")

GAME_DATA = {
    "title": "Cultura Hispana Jiporady",
    "subtitle": "¿Qué es... puro orgullo y buena vibra?",
    "rounds": {
        "round_1": {
            "name": "Round 1",
            "categories": [
                {
                    "title": "Dichos y Refranes",
                    "clues": [
                        {
                            "value": 100,
                            "question": "This proverb says it is wiser to hold onto something certain than to chase many uncertain possibilities.",
                            "answer": "¿Qué es 'Más vale pájaro en mano que cien volando'?"
                        },
                        {
                            "value": 200,
                            "question": "This saying warns that drifting through life half-awake can make opportunity pass you by.",
                            "answer": "¿Qué es 'Camarón que se duerme se lo lleva la corriente'?"
                        },
                        {
                            "value": 300,
                            "question": "This popular line praises persistence and says that steady effort eventually gets results.",
                            "answer": "¿Qué es 'El que persevera alcanza'?"
                        },
                        {
                            "value": 400,
                            "question": "This proverb reminds us that no matter how polished the outside looks, true nature still shows through.",
                            "answer": "¿Qué es 'Aunque la mona se vista de seda, mona se queda'?"
                        },
                        {
                            "value": 500,
                            "question": "This saying reminds you that forcing the clock does not make life unfold any faster.",
                            "answer": "¿Qué es 'No por mucho madrugar amanece más temprano'?"
                        },
                    ],
                },
                {
                    "title": "El Salvador",
                    "clues": [
                        {
                            "value": 100,
                            "question": "This stuffed griddled favorite, often served with curtido, is one of the country's best-known foods.",
                            "answer": "¿Qué es la pupusa?"
                        },
                        {
                            "value": 200,
                            "question": "This capital city sits near El Boquerón and begins with the same saintly title found in the country's name.",
                            "answer": "¿Qué es San Salvador?"
                        },
                        {
                            "value": 300,
                            "question": "This ocean borders the nation's southern edge.",
                            "answer": "¿Qué es el Océano Pacífico?"
                        },
                        {
                            "value": 400,
                            "question": "At the center of the flag appears this three-sided shape, shared with imagery from regional history.",
                            "answer": "¿Qué es un triángulo?"
                        },
                        {
                            "value": 500,
                            "question": "This archbishop, later canonized, became an enduring symbol of faith and justice after his assassination in 1980.",
                            "answer": "¿Quién es Óscar Romero?"
                        },
                    ],
                },
                {
                    "title": "Memes y Nostalgia",
                    "clues": [
                        {
                            "value": 100,
                            "question": "In many family jokes, this flying household item arrives faster than an apology.",
                            "answer": "¿Qué es la chancla?"
                        },
                        {
                            "value": 200,
                            "question": "This simple question about whether you have eaten often really means 'I care about you.'",
                            "answer": "¿Qué es '¿Ya comiste?'?"
                        },
                        {
                            "value": 300,
                            "question": "When someone says 'ponte un suéter,' the invisible enemy they fear is often this evening chill.",
                            "answer": "¿Qué es el sereno?"
                        },
                        {
                            "value": 400,
                            "question": "This giant weekend variety program, hosted for decades by Don Francisco, was background soundtrack in many homes.",
                            "answer": "¿Qué es Sábado Gigante?"
                        },
                        {
                            "value": 500,
                            "question": "This sweet holiday bread often hides a tiny figurine and turns dessert into a January surprise.",
                            "answer": "¿Qué es la rosca de reyes?"
                        },
                    ],
                },
                {
                    "title": "Música Latina",
                    "clues": [
                        {
                            "value": 100,
                            "question": "This Cuban-born legend is forever linked with the joyful shout '¡Azúcar!'",
                            "answer": "¿Quién es Celia Cruz?"
                        },
                        {
                            "value": 200,
                            "question": "This Puerto Rican star broke globally into crossover pop with 'Livin' la Vida Loca.'",
                            "answer": "¿Quién es Ricky Martin?"
                        },
                        {
                            "value": 300,
                            "question": "This Colombian singer behind 'Hips Don't Lie' became known for mixing pop with global rhythms.",
                            "answer": "¿Quién es Shakira?"
                        },
                        {
                            "value": 400,
                            "question": "Nicknamed El Charro de Huentitán, this beloved performer became one of ranchera's biggest icons.",
                            "answer": "¿Quién es Vicente Fernández?"
                        },
                        {
                            "value": 500,
                            "question": "This fast, danceable Dominican genre became a worldwide calling card for Juan Luis Guerra.",
                            "answer": "¿Qué es el merengue?"
                        },
                    ],
                },
                {
                    "title": "Español Fácil",
                    "clues": [
                        {
                            "value": 100,
                            "question": "If someone says 'Tengo hambre,' they are saying this in English.",
                            "answer": "What is 'I am hungry'?"
                        },
                        {
                            "value": 200,
                            "question": "In many places, 'qué chévere' means something close to this English adjective.",
                            "answer": "What is 'cool'?"
                        },
                        {
                            "value": 300,
                            "question": "The phrase 'buen provecho' is commonly said around this moment of the day.",
                            "answer": "What is mealtime?"
                        },
                        {
                            "value": 400,
                            "question": "Depending on the speaker, 'ahorita' can mean right now, very soon, or this frustratingly vague alternative.",
                            "answer": "What is 'later... maybe'?"
                        },
                        {
                            "value": 500,
                            "question": "When someone says '¡Qué pena!', they may be expressing sympathy, embarrassment, or this softer English reaction.",
                            "answer": "What is 'what a shame'?"
                        },
                    ],
                },
                {
                    "title": "Comida con Cariño",
                    "clues": [
                        {
                            "value": 100,
                            "question": "This famous rice dish from Spain is often cooked in a wide shallow pan and may include seafood, meat, or vegetables.",
                            "answer": "¿Qué es la paella?"
                        },
                        {
                            "value": 200,
                            "question": "This rich shredded specialty, popular at celebrations, is often tucked into tortillas after a long simmer.",
                            "answer": "¿Qué es la birria?"
                        },
                        {
                            "value": 300,
                            "question": "This twice-pressed green plantain favorite is loved across the Caribbean and Central America.",
                            "answer": "¿Qué son los tostones?"
                        },
                        {
                            "value": 400,
                            "question": "This chilled purple-corn drink is strongly associated with Peru.",
                            "answer": "¿Qué es la chicha morada?"
                        },
                        {
                            "value": 500,
                            "question": "This silky caramel-topped dessert appears across much of the Spanish-speaking world.",
                            "answer": "¿Qué es el flan?"
                        },
                    ],
                },
            ],
        },
        "round_2": {
            "name": "Doble Jiporady",
            "categories": [
                {
                    "title": "Dichos: Nivel Difícil",
                    "clues": [
                        {
                            "value": 200,
                            "question": "Este refrán da esperanza al recordar que incluso las épocas malas no duran para siempre.",
                            "answer": "¿Qué es 'No hay mal que dure cien años'?"
                        },
                        {
                            "value": 400,
                            "question": "Este consejo advierte que no se debe examinar demasiado un acto generoso.",
                            "answer": "¿Qué es 'A caballo regalado no se le mira el diente'?"
                        },
                        {
                            "value": 600,
                            "question": "Este dicho enseña que cada persona carga con su propia fortuna o destino.",
                            "answer": "¿Qué es 'Cada quien tiene su suerte'?"
                        },
                        {
                            "value": 800,
                            "question": "Esta frase celebra a quien sigue intentando hasta ver resultados.",
                            "answer": "¿Qué es 'El que persevera alcanza'?"
                        },
                        {
                            "value": 1000,
                            "question": "Este refrán promete que después de un revés puede aparecer una nueva oportunidad.",
                            "answer": "¿Qué es 'Cuando una puerta se cierra, otra se abre'?"
                        },
                    ],
                },
                {
                    "title": "Centroamérica en Español",
                    "clues": [
                        {
                            "value": 200,
                            "question": "Este país es famoso por una vía interoceánica que cambió el comercio mundial.",
                            "answer": "¿Qué es Panamá?"
                        },
                        {
                            "value": 400,
                            "question": "Este lugar es conocido por su biodiversidad y por la expresión 'Pura vida'.",
                            "answer": "¿Qué es Costa Rica?"
                        },
                        {
                            "value": 600,
                            "question": "En este país nació Rubén Darío, figura clave del modernismo.",
                            "answer": "¿Qué es Nicaragua?"
                        },
                        {
                            "value": 800,
                            "question": "Este territorio caribeño comparte isla con Haití y usa mayormente el español.",
                            "answer": "¿Qué es la República Dominicana?"
                        },
                        {
                            "value": 1000,
                            "question": "En esta nación, el quetzal es tanto ave simbólica como moneda.",
                            "answer": "¿Qué es Guatemala?"
                        },
                    ],
                },
                {
                    "title": "Arte y Letras",
                    "clues": [
                        {
                            "value": 200,
                            "question": "This Colombian novelist wrote 'Cien años de soledad.'",
                            "answer": "¿Quién es Gabriel García Márquez?"
                        },
                        {
                            "value": 400,
                            "question": "Known for striking self-portraits and flower crowns, this Mexican artist became a global cultural icon.",
                            "answer": "¿Quién es Frida Kahlo?"
                        },
                        {
                            "value": 600,
                            "question": "This Chilean Nobel laureate wrote 'Veinte poemas de amor y una canción desesperada.'",
                            "answer": "¿Quién es Pablo Neruda?"
                        },
                        {
                            "value": 800,
                            "question": "This Dominican-American author won wide acclaim for 'The Brief Wondrous Life of Oscar Wao.'",
                            "answer": "¿Quién es Junot Díaz?"
                        },
                        {
                            "value": 1000,
                            "question": "This Argentine master gave readers labyrinths, mirrors, and books within books in works like 'Ficciones.'",
                            "answer": "¿Quién es Jorge Luis Borges?"
                        },
                    ],
                },
                {
                    "title": "PTSD (pero con cariño)",
                    "clues": [
                        {
                            "value": 200,
                            "question": "The sound of a neighborhood loudspeaker selling frozen treats can instantly unlock childhood summer memories of this rolling attraction.",
                            "answer": "¿Qué es el carrito de paletas?"
                        },
                        {
                            "value": 400,
                            "question": "Being told not to touch the decorated room often brings flashbacks to this guest-only part of the house.",
                            "answer": "¿Qué es la sala buena?"
                        },
                        {
                            "value": 600,
                            "question": "Before entering a family party, the phrase 'saluda bien' often meant you were about to perform this social ritual.",
                            "answer": "¿Qué es dar beso y abrazo a todos?"
                        },
                        {
                            "value": 800,
                            "question": "One glance at a giant ice-cream tub in the freezer can trigger the classic surprise that it actually contains this.",
                            "answer": "¿Qué son los frijoles?"
                        },
                        {
                            "value": 1000,
                            "question": "At many gatherings, a relative asking about your future can instantly revive memories of this unofficial family sport.",
                            "answer": "¿Qué es el interrogatorio cariñoso?"
                        },
                    ],
                },
                {
                    "title": "Baile y Ritmo",
                    "clues": [
                        {
                            "value": 200,
                            "question": "Este estilo urbano, impulsado por artistas como Daddy Yankee, dominó clubes y playlists globales.",
                            "answer": "¿Qué es el reguetón?"
                        },
                        {
                            "value": 400,
                            "question": "Este baile del Río de la Plata se reconoce por su abrazo cerrado y su drama elegante.",
                            "answer": "¿Qué es el tango?"
                        },
                        {
                            "value": 600,
                            "question": "Este género afrocaribeño nacido en Cuba viajó al mundo con clave, metales y mucho sabor.",
                            "answer": "¿Qué es la salsa?"
                        },
                        {
                            "value": 800,
                            "question": "Nacida en el Bronx, esta estrella brilló en cine, televisión y éxitos como 'On the Floor.'",
                            "answer": "¿Quién es Jennifer Lopez?"
                        },
                        {
                            "value": 1000,
                            "question": "Con temas como 'Baila Esta Cumbia' y 'Como la Flor,' esta artista tejana sigue siendo querida décadas después.",
                            "answer": "¿Quién es Selena?"
                        },
                    ],
                },
                {
                    "title": "Palabras Viajeras",
                    "clues": [
                        {
                            "value": 200,
                            "question": "This Spanish word for a small savory bite became a common English menu word.",
                            "answer": "What is tapas?"
                        },
                        {
                            "value": 400,
                            "question": "This everyday Spanish term for a party gave English one of its most common celebration words.",
                            "answer": "What is fiesta?"
                        },
                        {
                            "value": 600,
                            "question": "This ranch word traveled north and became the English term for a skilled rider.",
                            "answer": "What is vaquero?"
                        },
                        {
                            "value": 800,
                            "question": "English borrowed this musical term for a fast, spicy sauce-style rhythm from Spanish.",
                            "answer": "What is salsa?"
                        },
                        {
                            "value": 1000,
                            "question": "This Spanish word for a cattle rope eventually gave English the term for a looping tool used by cowhands.",
                            "answer": "What is lazo?"
                        },
                    ],
                },
            ],
        },
    },
    "final": {
        "category": "Final Jiporady: Rocket League x Cultura",
        "question": "In a Rocket League lobby with soccer energy, this Spanish exclamation would be perfect after an overtime screamer into the top corner.",
        "answer": "¿Qué es '¡Golazo!'?"
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
    return {"ok": True, "app": "jiporady_hispanic"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)