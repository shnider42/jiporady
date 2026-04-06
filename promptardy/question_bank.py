from __future__ import annotations

import random
from typing import Any

QUESTION_BANK = [
    {
        "category": "Science Basics",
        "clues": [
            {"value": 200, "question": "This planet is known as the Red Planet.", "answer": "What is Mars?"},
            {"value": 400, "question": "Water is made of hydrogen and this other element.", "answer": "What is oxygen?"},
            {"value": 600, "question": "The force that pulls objects toward Earth is called this.", "answer": "What is gravity?"},
            {"value": 800, "question": "Plants take in this gas from the air during photosynthesis.", "answer": "What is carbon dioxide?"},
            {"value": 1000, "question": "On the pH scale, a value below 7 describes a substance with this property.", "answer": "What is acidic?"},
        ],
    },
    {
        "category": "Space",
        "clues": [
            {"value": 200, "question": "This is the star at the center of our solar system.", "answer": "What is the Sun?"},
            {"value": 400, "question": "Earth's natural satellite is this.", "answer": "What is the Moon?"},
            {"value": 600, "question": "This planet has the most famous ring system in our solar system.", "answer": "What is Saturn?"},
            {"value": 800, "question": "The Milky Way is a type of this large star system.", "answer": "What is a galaxy?"},
            {"value": 1000, "question": "Neil Armstrong became the first person to do this on July 20, 1969.", "answer": "What is walk on the Moon?"},
        ],
    },
    {
        "category": "World Geography",
        "clues": [
            {"value": 200, "question": "This is the largest ocean on Earth.", "answer": "What is the Pacific Ocean?"},
            {"value": 400, "question": "This desert stretches across much of North Africa.", "answer": "What is the Sahara Desert?"},
            {"value": 600, "question": "Mount Everest lies in the Himalayas on the border of Nepal and this country.", "answer": "What is China?"},
            {"value": 800, "question": "This river flows through Egypt and empties into the Mediterranean Sea.", "answer": "What is the Nile River?"},
            {"value": 1000, "question": "This country is both a continent and a nation.", "answer": "What is Australia?"},
        ],
    },
    {
        "category": "U.S. Geography",
        "clues": [
            {"value": 200, "question": "This state is known as the Sunshine State.", "answer": "What is Florida?"},
            {"value": 400, "question": "The Grand Canyon is found in this state.", "answer": "What is Arizona?"},
            {"value": 600, "question": "This is the longest river in the United States.", "answer": "What is the Missouri River?"},
            {"value": 800, "question": "This U.S. state has the most people.", "answer": "What is California?"},
            {"value": 1000, "question": "This mountain range runs along much of the eastern United States.", "answer": "What are the Appalachian Mountains?"},
        ],
    },
    {
        "category": "World History",
        "clues": [
            {"value": 200, "question": "This wall was built in northern China over many dynasties.", "answer": "What is the Great Wall of China?"},
            {"value": 400, "question": "This empire was ruled by Julius Caesar and Augustus.", "answer": "What is the Roman Empire?"},
            {"value": 600, "question": "The French Revolution began in this year-famous decade.", "answer": "What are the 1780s?"},
            {"value": 800, "question": "This ship sank on its maiden voyage in 1912.", "answer": "What is the Titanic?"},
            {"value": 1000, "question": "This conflict from 1939 to 1945 involved the Allies and Axis powers.", "answer": "What is World War II?"},
        ],
    },
    {
        "category": "U.S. History",
        "clues": [
            {"value": 200, "question": "He was the first president of the United States.", "answer": "Who is George Washington?"},
            {"value": 400, "question": "This document begins with the words 'We the People.'", "answer": "What is the U.S. Constitution?"},
            {"value": 600, "question": "The purchase of this territory from France doubled the size of the United States in 1803.", "answer": "What is the Louisiana Purchase?"},
            {"value": 800, "question": "This civil rights leader gave the 'I Have a Dream' speech in 1963.", "answer": "Who is Martin Luther King Jr.?"},
            {"value": 1000, "question": "This scandal led to President Richard Nixon's resignation in 1974.", "answer": "What is Watergate?"},
        ],
    },
    {
        "category": "Literature",
        "clues": [
            {"value": 200, "question": "This young wizard attends Hogwarts.", "answer": "Who is Harry Potter?"},
            {"value": 400, "question": "This novel opens with the line 'Call me Ishmael.'", "answer": "What is Moby-Dick?"},
            {"value": 600, "question": "George Orwell wrote this dystopian novel set in Airstrip One.", "answer": "What is 1984?"},
            {"value": 800, "question": "Odysseus is the hero of this ancient Greek epic.", "answer": "What is The Odyssey?"},
            {"value": 1000, "question": "This Jane Austen novel centers on Elizabeth Bennet and Mr. Darcy.", "answer": "What is Pride and Prejudice?"},
        ],
    },
    {
        "category": "Famous Authors",
        "clues": [
            {"value": 200, "question": "He wrote many plays including Hamlet and Macbeth.", "answer": "Who is William Shakespeare?"},
            {"value": 400, "question": "She wrote Little Women.", "answer": "Who is Louisa May Alcott?"},
            {"value": 600, "question": "This horror writer created Dracula.", "answer": "Who is Bram Stoker?"},
            {"value": 800, "question": "He wrote The Old Man and the Sea and won the Nobel Prize in Literature.", "answer": "Who is Ernest Hemingway?"},
            {"value": 1000, "question": "This author created Middle-earth.", "answer": "Who is J.R.R. Tolkien?"},
        ],
    },
    {
        "category": "Movies",
        "clues": [
            {"value": 200, "question": "This 1997 blockbuster is about a famous doomed ocean liner.", "answer": "What is Titanic?"},
            {"value": 400, "question": "In The Wizard of Oz, Dorothy travels to this magical land.", "answer": "What is Oz?"},
            {"value": 600, "question": "This film franchise features Luke Skywalker and Darth Vader.", "answer": "What is Star Wars?"},
            {"value": 800, "question": "Pixar's first feature film was this story about living toys.", "answer": "What is Toy Story?"},
            {"value": 1000, "question": "In Back to the Future, Doc Brown's time machine is built from this car brand.", "answer": "What is a DeLorean?"},
        ],
    },
    {
        "category": "Television",
        "clues": [
            {"value": 200, "question": "This animated family lives in Springfield.", "answer": "Who are the Simpsons?"},
            {"value": 400, "question": "Ross, Rachel, Monica, Chandler, Joey, and Phoebe star on this sitcom.", "answer": "What is Friends?"},
            {"value": 600, "question": "The phrase 'Winter is coming' comes from this fantasy series.", "answer": "What is Game of Thrones?"},
            {"value": 800, "question": "This long-running British sci-fi show features the TARDIS.", "answer": "What is Doctor Who?"},
            {"value": 1000, "question": "Walter White teaches chemistry before turning to crime in this series.", "answer": "What is Breaking Bad?"},
        ],
    },
    {
        "category": "Music",
        "clues": [
            {"value": 200, "question": "This instrument has 88 keys on a standard model.", "answer": "What is the piano?"},
            {"value": 400, "question": "The Beatles were formed in this English city.", "answer": "What is Liverpool?"},
            {"value": 600, "question": "This singer is known as the 'King of Pop.'", "answer": "Who is Michael Jackson?"},
            {"value": 800, "question": "A group of three musicians is called this.", "answer": "What is a trio?"},
            {"value": 1000, "question": "Beethoven's Ninth Symphony includes this famous choral movement.", "answer": "What is 'Ode to Joy'?"},
        ],
    },
    {
        "category": "Technology",
        "clues": [
            {"value": 200, "question": "CPU stands for Central Processing this.", "answer": "What is Unit?"},
            {"value": 400, "question": "This company created the Windows operating system.", "answer": "What is Microsoft?"},
            {"value": 600, "question": "A small picture used to launch an app is commonly called this.", "answer": "What is an icon?"},
            {"value": 800, "question": "This piece of hardware stores data long-term in many computers.", "answer": "What is a hard drive?"},
            {"value": 1000, "question": "HTML is mainly used to structure this kind of document.", "answer": "What is a web page?"},
        ],
    },
    {
        "category": "Internet & Computing",
        "clues": [
            {"value": 200, "question": "The 'www' in a web address stands for World Wide this.", "answer": "What is Web?"},
            {"value": 400, "question": "This symbol appears in every email address.", "answer": "What is the @ symbol?"},
            {"value": 600, "question": "A malicious program that spreads between computers can be called this.", "answer": "What is a virus?"},
            {"value": 800, "question": "This popular version-control system is used by many software developers.", "answer": "What is Git?"},
            {"value": 1000, "question": "RAM is prized because it allows this kind of access to data.", "answer": "What is fast temporary access?"},
        ],
    },
    {
        "category": "Sports",
        "clues": [
            {"value": 200, "question": "This sport is played at Wimbledon.", "answer": "What is tennis?"},
            {"value": 400, "question": "A baseball game typically lasts this many innings.", "answer": "What is nine?"},
            {"value": 600, "question": "The Olympics are held every this many years.", "answer": "What is four?"},
            {"value": 800, "question": "In soccer, players try to score in this part of the field setup.", "answer": "What is the goal?"},
            {"value": 1000, "question": "This sport uses terms like birdie, eagle, and bogey.", "answer": "What is golf?"},
        ],
    },
    {
        "category": "Food & Drink",
        "clues": [
            {"value": 200, "question": "Sushi is most closely associated with this country.", "answer": "What is Japan?"},
            {"value": 400, "question": "Guacamole is made primarily from this fruit.", "answer": "What is avocado?"},
            {"value": 600, "question": "Espresso is a concentrated form of this beverage.", "answer": "What is coffee?"},
            {"value": 800, "question": "Mozzarella is a cheese often paired with tomato and basil in this salad.", "answer": "What is caprese salad?"},
            {"value": 1000, "question": "This French pastry is famous for its crescent shape.", "answer": "What is a croissant?"},
        ],
    },
    {
        "category": "Nature & Animals",
        "clues": [
            {"value": 200, "question": "This mammal is known for its black-and-white stripes.", "answer": "What is a zebra?"},
            {"value": 400, "question": "A baby frog begins life in this form.", "answer": "What is a tadpole?"},
            {"value": 600, "question": "This is the fastest land animal.", "answer": "What is a cheetah?"},
            {"value": 800, "question": "A group of wolves is called this.", "answer": "What is a pack?"},
            {"value": 1000, "question": "These huge trees are famous for growing in California's Sierra Nevada.", "answer": "What are giant sequoias?"},
        ],
    },
    {
        "category": "Art & Architecture",
        "clues": [
            {"value": 200, "question": "Leonardo da Vinci painted this famous smiling woman.", "answer": "What is the Mona Lisa?"},
            {"value": 400, "question": "The Eiffel Tower stands in this city.", "answer": "What is Paris?"},
            {"value": 600, "question": "This artist cut off part of his ear.", "answer": "Who is Vincent van Gogh?"},
            {"value": 800, "question": "A building's detailed drawing made before construction is called this.", "answer": "What is a blueprint?"},
            {"value": 1000, "question": "This famous domed basilica overlooks Vatican City.", "answer": "What is St. Peter's Basilica?"},
        ],
    },
    {
        "category": "Mythology",
        "clues": [
            {"value": 200, "question": "In Greek myth, this king of the gods wields thunderbolts.", "answer": "Who is Zeus?"},
            {"value": 400, "question": "This winged horse sprang from Medusa's blood.", "answer": "Who is Pegasus?"},
            {"value": 600, "question": "In Norse mythology, this god carries the hammer Mjolnir.", "answer": "Who is Thor?"},
            {"value": 800, "question": "This Greek hero completed twelve famous labors.", "answer": "Who is Heracles?"},
            {"value": 1000, "question": "In Egyptian mythology, this god of the dead is often depicted with a jackal head.", "answer": "Who is Anubis?"},
        ],
    },
    {
        "category": "Word Origins",
        "clues": [
            {"value": 200, "question": "A word with the opposite meaning of another word is called this.", "answer": "What is an antonym?"},
            {"value": 400, "question": "A word that sounds like what it describes, like 'buzz,' is this.", "answer": "What is onomatopoeia?"},
            {"value": 600, "question": "A dictionary is organized alphabetically by these units of language.", "answer": "What are words?"},
            {"value": 800, "question": "The root 'bio-' relates to this.", "answer": "What is life?"},
            {"value": 1000, "question": "When a brand name becomes a generic term in everyday speech, that's commonly called this kind of shift.", "answer": "What is genericization?"},
        ],
    },
    {
        "category": "Math & Logic",
        "clues": [
            {"value": 200, "question": "This is the result of 9 times 9.", "answer": "What is 81?"},
            {"value": 400, "question": "A triangle with all three sides equal is called this.", "answer": "What is an equilateral triangle?"},
            {"value": 600, "question": "The Roman numeral X represents this number.", "answer": "What is 10?"},
            {"value": 800, "question": "A six-sided polygon is called this.", "answer": "What is a hexagon?"},
            {"value": 1000, "question": "In a standard deck of cards, the probability of drawing a king from a full shuffled deck is this fraction.", "answer": "What is 1/13?"},
        ],
    },
    {
        "category": "Inventions",
        "clues": [
            {"value": 200, "question": "This invention tells time using hands or digits.", "answer": "What is a clock?"},
            {"value": 400, "question": "The brothers Orville and Wilbur Wright are associated with this invention.", "answer": "What is the airplane?"},
            {"value": 600, "question": "Johannes Gutenberg is famous for improving this machine.", "answer": "What is the printing press?"},
            {"value": 800, "question": "This inventor is strongly associated with the practical incandescent light bulb.", "answer": "Who is Thomas Edison?"},
            {"value": 1000, "question": "The World Wide Web was invented by this British computer scientist.", "answer": "Who is Tim Berners-Lee?"},
        ],
    },
    {
        "category": "Famous People",
        "clues": [
            {"value": 200, "question": "He developed the theory of relativity.", "answer": "Who is Albert Einstein?"},
            {"value": 400, "question": "She was the first woman to win a Nobel Prize.", "answer": "Who is Marie Curie?"},
            {"value": 600, "question": "He was a South African leader imprisoned for 27 years before becoming president.", "answer": "Who is Nelson Mandela?"},
            {"value": 800, "question": "This aviation pioneer disappeared over the Pacific in 1937.", "answer": "Who is Amelia Earhart?"},
            {"value": 1000, "question": "This naturalist wrote On the Origin of Species.", "answer": "Who is Charles Darwin?"},
        ],
    },
    {
        "category": "Business & Brands",
        "clues": [
            {"value": 200, "question": "This company is famous for its golden arches.", "answer": "What is McDonald's?"},
            {"value": 400, "question": "This online retailer started as an internet bookstore.", "answer": "What is Amazon?"},
            {"value": 600, "question": "This athletic brand uses the slogan 'Just Do It.'", "answer": "What is Nike?"},
            {"value": 800, "question": "This soft drink brand shares its name with a major cola company.", "answer": "What is Coca-Cola?"},
            {"value": 1000, "question": "This electric-car company was co-founded by Martin Eberhard and Marc Tarpenning.", "answer": "What is Tesla?"},
        ],
    },
    {
        "category": "Ireland",
        "clues": [
            {"value": 200, "question": "This is the capital city of Ireland.", "answer": "What is Dublin?"},
            {"value": 400, "question": "The Irish tricolor includes green, white, and this third color.", "answer": "What is orange?"},
            {"value": 600, "question": "This Irish holiday is celebrated worldwide on March 17.", "answer": "What is St. Patrick's Day?"},
            {"value": 800, "question": "This famous stone at Blarney Castle is said to grant the gift of eloquence.", "answer": "What is the Blarney Stone?"},
            {"value": 1000, "question": "This river flows through Dublin and into Dublin Bay.", "answer": "What is the River Liffey?"},
        ],
    },
    {
        "category": "Capitals",
        "clues": [
            {"value": 200, "question": "The capital of France is this city.", "answer": "What is Paris?"},
            {"value": 400, "question": "The capital of Japan is this city.", "answer": "What is Tokyo?"},
            {"value": 600, "question": "The capital of Canada is this city.", "answer": "What is Ottawa?"},
            {"value": 800, "question": "The capital of Brazil is this planned city.", "answer": "What is Brasília?"},
            {"value": 1000, "question": "The capital of South Korea is this city.", "answer": "What is Seoul?"},
        ],
    },
    {
        "category": "Human Body",
        "clues": [
            {"value": 200, "question": "This organ pumps blood through the body.", "answer": "What is the heart?"},
            {"value": 400, "question": "Humans normally have this many lungs.", "answer": "What is two?"},
            {"value": 600, "question": "The femur is a bone found in this part of the body.", "answer": "What is the leg?"},
            {"value": 800, "question": "This organ helps filter blood and produce urine.", "answer": "What are the kidneys?"},
            {"value": 1000, "question": "The smallest bones in the body are found in this sensory organ.", "answer": "What is the ear?"},
        ],
    },
    {
        "category": "Oceans & Earth",
        "clues": [
            {"value": 200, "question": "This layer of Earth is the one we live on.", "answer": "What is the crust?"},
            {"value": 400, "question": "Molten rock below Earth's surface is called this.", "answer": "What is magma?"},
            {"value": 600, "question": "This imaginary line circles Earth halfway between the poles.", "answer": "What is the equator?"},
            {"value": 800, "question": "The Atlantic Ocean lies between the Americas and these two continents.", "answer": "What are Europe and Africa?"},
            {"value": 1000, "question": "This instrument is used to measure atmospheric pressure.", "answer": "What is a barometer?"},
        ],
    },
    {
        "category": "Everyday Objects",
        "clues": [
            {"value": 200, "question": "You use this object to unlock many doors.", "answer": "What is a key?"},
            {"value": 400, "question": "This household item is used to illuminate a room by hanging from or standing in it.", "answer": "What is a lamp?"},
            {"value": 600, "question": "This tool has teeth and is used to style hair.", "answer": "What is a comb?"},
            {"value": 800, "question": "You might mail a letter in this paper container.", "answer": "What is an envelope?"},
            {"value": 1000, "question": "This kitchen item measures ingredients and often comes in sets.", "answer": "What are measuring cups?"},
        ],
    },
    {
        "category": "Games & Toys",
        "clues": [
            {"value": 200, "question": "This board game asks players to buy properties like Boardwalk.", "answer": "What is Monopoly?"},
            {"value": 400, "question": "In chess, this piece moves in an L-shape.", "answer": "What is the knight?"},
            {"value": 600, "question": "This colorful puzzle cube was invented by Ernő Rubik.", "answer": "What is the Rubik's Cube?"},
            {"value": 800, "question": "Nintendo's plumber hero is this character.", "answer": "Who is Mario?"},
            {"value": 1000, "question": "In playing cards, these are the four suits.", "answer": "What are hearts, diamonds, clubs, and spades?"},
        ],
    },
    {
        "category": "Potpourri",
        "clues": [
            {"value": 200, "question": "This weekday comes right before Saturday.", "answer": "What is Friday?"},
            {"value": 400, "question": "A century contains this many years.", "answer": "What is 100?"},
            {"value": 600, "question": "This colorful arc can appear in the sky after rain.", "answer": "What is a rainbow?"},
            {"value": 800, "question": "This is the freezing point of water in degrees Celsius.", "answer": "What is 0?"},
            {"value": 1000, "question": "This famous detective created by Arthur Conan Doyle lives at 221B Baker Street.", "answer": "Who is Sherlock Holmes?"},
        ],
    },
]


def build_board(category_count: int = 6) -> list[dict[str, Any]]:
    """Return a randomized set of categories for the board."""
    category_count = max(4, min(category_count, len(QUESTION_BANK)))
    selected = random.sample(QUESTION_BANK, k=category_count)
    board = []
    for item in selected:
        clues = sorted(item["clues"], key=lambda clue: clue["value"])
        board.append({"category": item["category"], "clues": clues})
    return board


def get_bank_stats() -> dict[str, int]:
    total_categories = len(QUESTION_BANK)
    total_clues = sum(len(item["clues"]) for item in QUESTION_BANK)
    return {"total_categories": total_categories, "total_clues": total_clues}
