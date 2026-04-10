def qa(question, answer):
    return {"question": question, "answer": answer}


APP_TITLE = "Jiporady"
APP_SUBTITLE = "A bigger, louder, random-per-session Jeopardy-style party board"
CATEGORY_COUNT = 6

ROUND_DEFS = {
    "round_1": {
        "name": "Round 1",
        "values": [100, 200, 300, 400, 500],
        "bank": {
            "Science & Space": {
                100: [
                    qa("This ringed planet is the second largest in our solar system.", "What is Saturn?"),
                    qa("This planet is known as the Red Planet.", "What is Mars?"),
                ],
                200: [
                    qa("This force keeps planets in orbit and keeps your feet on the ground.", "What is gravity?"),
                    qa("Plants use sunlight to perform this process.", "What is photosynthesis?"),
                ],
                300: [
                    qa("Most of a cell's DNA is found here.", "What is the nucleus?"),
                    qa("This is the nearest star to Earth.", "What is the Sun?"),
                ],
                400: [
                    qa("This instrument is used to look at stars and distant galaxies.", "What is a telescope?"),
                    qa("Water freezes at this temperature on the Celsius scale.", "What is 0 degrees Celsius?"),
                ],
                500: [
                    qa("Named for an Italian physicist, this paradox asks why we have not clearly detected alien civilizations.", "What is the Fermi paradox?"),
                    qa("This layer of Earth's atmosphere contains the ozone layer.", "What is the stratosphere?"),
                ],
            },
            "Movies & TV": {
                100: [
                    qa("This blue alien experiment is the title character in a Disney film with Lilo.", "Who is Stitch?"),
                    qa("This sitcom is set in the Scranton branch of Dunder Mifflin.", "What is The Office?"),
                ],
                200: [
                    qa("In Breaking Bad, Walter White teaches this subject before becoming a drug kingpin.", "What is chemistry?"),
                    qa("This 1999 film stars Neo, Morpheus, and Trinity.", "What is The Matrix?"),
                ],
                300: [
                    qa("The Stark family appears in this HBO fantasy series.", "What is Game of Thrones?"),
                    qa("This movie features a theme park filled with cloned dinosaurs.", "What is Jurassic Park?"),
                ],
                400: [
                    qa("Bong Joon-ho directed this Best Picture winner about two very different families.", "What is Parasite?"),
                    qa("This sitcom follows six friends living in New York City.", "What is Friends?"),
                ],
                500: [
                    qa("This filmmaker directed Jaws, E.T., and Jurassic Park.", "Who is Steven Spielberg?"),
                    qa("In Star Wars, this smuggler pilots the Millennium Falcon.", "Who is Han Solo?"),
                ],
            },
            "Music & Pop Culture": {
                100: [
                    qa("Taylor Swift first broke out mainly in this genre before becoming a pop superstar.", "What is country?"),
                    qa("This singer is known as the King of Pop.", "Who is Michael Jackson?"),
                ],
                200: [
                    qa("This artist released the album Renaissance.", "Who is Beyoncé?"),
                    qa("This K-pop group includes RM, Jin, Suga, j-hope, Jimin, V, and Jung Kook.", "Who are BTS?"),
                ],
                300: [
                    qa("The Beatles came from this English city.", "What is Liverpool?"),
                    qa("This rapper was born Aubrey Graham.", "Who is Drake?"),
                ],
                400: [
                    qa("This singer's 2024 album was The Tortured Poets Department.", "Who is Taylor Swift?"),
                    qa("This singer is nicknamed The Boss.", "Who is Bruce Springsteen?"),
                ],
                500: [
                    qa("This music term means gradually getting louder.", "What is crescendo?"),
                    qa("This Detroit-based label is associated with artists like Stevie Wonder and The Supremes.", "What is Motown?"),
                ],
            },
            "Internet & Tech": {
                100: [
                    qa("The 'www' in a web address stands for this.", "What is World Wide Web?"),
                    qa("This company created the iPhone.", "What is Apple?"),
                ],
                200: [
                    qa("Linus Torvalds created this open-source operating system kernel.", "What is Linux?"),
                    qa("This version-control platform is now owned by Microsoft.", "What is GitHub?"),
                ],
                300: [
                    qa("HTTP stands for this.", "What is Hypertext Transfer Protocol?"),
                    qa("RAM stands for this.", "What is Random Access Memory?"),
                ],
                400: [
                    qa("This language is primarily used to style web pages.", "What is CSS?"),
                    qa("An API stands for this.", "What is an Application Programming Interface?"),
                ],
                500: [
                    qa("DNS translates domain names into these.", "What are IP addresses?"),
                    qa("In Git, this command copies a remote repository to your local machine.", "What is git clone?"),
                ],
            },
            "Wordplay": {
                100: [
                    qa("A word with the opposite meaning of another word.", "What is an antonym?"),
                    qa("A word that sounds like another but has a different meaning, like sea and see.", "What is a homophone?"),
                ],
                200: [
                    qa("A comparison using 'like' or 'as.'", "What is a simile?"),
                    qa("A figure of speech in which a thing is described as being something else.", "What is a metaphor?"),
                ],
                300: [
                    qa("A word made from the first letters of a phrase, like NASA.", "What is an acronym?"),
                    qa("This punctuation mark can create contractions like can't.", "What is an apostrophe?"),
                ],
                400: [
                    qa("A word or phrase that reads the same backward and forward.", "What is a palindrome?"),
                    qa("The repeated consonant sound at the beginning of nearby words is called this.", "What is alliteration?"),
                ],
                500: [
                    qa("This literary device gives human traits to nonhuman things.", "What is personification?"),
                    qa("A pun usually depends on this kind of double meaning.", "What is wordplay?"),
                ],
            },
            "Odds & Ends": {
                100: [
                    qa("The largest ocean on Earth.", "What is the Pacific Ocean?"),
                    qa("A standard die has this many sides.", "What is 6?"),
                ],
                200: [
                    qa("This board game tells you to pass Go and collect $200.", "What is Monopoly?"),
                    qa("The chess piece that moves in an L-shape.", "What is the knight?"),
                ],
                300: [
                    qa("In Roman numerals, this letter stands for 500.", "What is D?"),
                    qa("This is the common name for a baby kangaroo.", "What is a joey?"),
                ],
                400: [
                    qa("This mythical creature is the national animal of Scotland.", "What is the unicorn?"),
                    qa("A six-sided polygon is called this.", "What is a hexagon?"),
                ],
                500: [
                    qa("This field of study focuses on flags.", "What is vexillology?"),
                    qa("The only letter not used in the modern periodic table is this.", "What is J?"),
                ],
            },
            "Geography": {
                100: [
                    qa("This is the capital of Japan.", "What is Tokyo?"),
                    qa("This river runs through Egypt.", "What is the Nile?"),
                ],
                200: [
                    qa("This desert stretches across much of northern Africa.", "What is the Sahara?"),
                    qa("This country lies directly north of the United States.", "What is Canada?"),
                ],
                300: [
                    qa("Mount Everest is part of this mountain range.", "What are the Himalayas?"),
                    qa("This country contains the city of Barcelona.", "What is Spain?"),
                ],
                400: [
                    qa("This is the capital of Australia.", "What is Canberra?"),
                    qa("Greenland is the world's largest island that is not this.", "What is a continent?"),
                ],
                500: [
                    qa("This strait separates Asia from North America.", "What is the Bering Strait?"),
                    qa("Astana is the capital of this country.", "What is Kazakhstan?"),
                ],
            },
            "Food & Drink": {
                100: [
                    qa("This fruit is mashed to make guacamole.", "What is an avocado?"),
                    qa("Sushi is strongly associated with this country.", "What is Japan?"),
                ],
                200: [
                    qa("Risotto is usually made from this grain.", "What is rice?"),
                    qa("Citrus fruits are especially associated with this vitamin.", "What is Vitamin C?"),
                ],
                300: [
                    qa("This yellow spice is common in many curries.", "What is turmeric?"),
                    qa("This Italian dish is layered with pasta, cheese, and sauce.", "What is lasagna?"),
                ],
                400: [
                    qa("This cheese is commonly found in a Greek salad.", "What is feta?"),
                    qa("Soybeans are used to make this protein-rich food.", "What is tofu?"),
                ],
                500: [
                    qa("The French culinary phrase meaning 'everything in its place.'", "What is mise en place?"),
                    qa("This process turns grape juice into wine.", "What is fermentation?"),
                ],
            },
            "Comics & Superheroes": {
                100: [
                    qa("Bruce Wayne is better known by this superhero name.", "Who is Batman?"),
                    qa("Peter Parker becomes this superhero.", "Who is Spider-Man?"),
                ],
                200: [
                    qa("Wakanda is home to this Marvel hero.", "Who is Black Panther?"),
                    qa("Clark Kent is the alter ego of this hero.", "Who is Superman?"),
                ],
                300: [
                    qa("This metal shield belongs to Captain America.", "What is vibranium?"),
                    qa("Diana Prince is better known as this hero.", "Who is Wonder Woman?"),
                ],
                400: [
                    qa("Tony Stark builds this powered suit identity.", "Who is Iron Man?"),
                    qa("This villain is obsessed with chaos in The Dark Knight.", "Who is the Joker?"),
                ],
                500: [
                    qa("The Infinity Gauntlet is most associated with this Marvel villain.", "Who is Thanos?"),
                    qa("This team includes Cyclops, Storm, and Wolverine.", "Who are the X-Men?"),
                ],
            },
        },
    },
    "round_2": {
        "name": "Double Jiporady",
        "values": [200, 400, 600, 800, 1000],
        "bank": {
            "World History": {
                200: [
                    qa("This wall fell in 1989, becoming a symbol of the end of Soviet control in Eastern Europe.", "What is the Berlin Wall?"),
                    qa("This ship carried the Pilgrims across the Atlantic in 1620.", "What is the Mayflower?"),
                ],
                400: [
                    qa("This French leader crowned himself emperor in 1804.", "Who is Napoleon Bonaparte?"),
                    qa("This English document from 1215 is often cited as limiting royal power.", "What is the Magna Carta?"),
                ],
                600: [
                    qa("The Great War is now better known by this name.", "What is World War I?"),
                    qa("This empire was ruled at one point by Augustus, Rome's first emperor.", "What is the Roman Empire?"),
                ],
                800: [
                    qa("This peace treaty formally ended World War I.", "What is the Treaty of Versailles?"),
                    qa("Joan of Arc is associated with this country.", "What is France?"),
                ],
                1000: [
                    qa("This dynasty built much of the Great Wall of China as commonly seen today.", "What is the Ming Dynasty?"),
                    qa("The French Revolution began in this year.", "What is 1789?"),
                ],
            },
            "Video Games": {
                200: [
                    qa("Nintendo's mustachioed mascot who often rescues Princess Peach.", "Who is Mario?"),
                    qa("This Mojang sandbox game lets players build with blocks and fight the Ender Dragon.", "What is Minecraft?"),
                ],
                400: [
                    qa("Link often wields this legendary blade in The Legend of Zelda.", "What is the Master Sword?"),
                    qa("The company behind the PlayStation brand.", "What is Sony?"),
                ],
                600: [
                    qa("This 2023 RPG by Larian Studios won many Game of the Year awards.", "What is Baldur's Gate 3?"),
                    qa("Master Chief is the iconic hero of this Xbox franchise.", "What is Halo?"),
                ],
                800: [
                    qa("This battle royale game from Epic Games is known for building mechanics and seasonal events.", "What is Fortnite?"),
                    qa("The companion cube appears in this puzzle game series by Valve.", "What is Portal?"),
                ],
                1000: [
                    qa("This company created the Pokémon franchise alongside Game Freak and Creatures.", "What is Nintendo?"),
                    qa("In Pac-Man, these colored enemies chase the player through a maze.", "What are ghosts?"),
                ],
            },
            "Books & Authors": {
                200: [
                    qa("She wrote Pride and Prejudice.", "Who is Jane Austen?"),
                    qa("This author created Middle-earth and wrote The Hobbit.", "Who is J.R.R. Tolkien?"),
                ],
                400: [
                    qa("In Animal Farm, this pig becomes a dictator-like figure.", "Who is Napoleon?"),
                    qa("Herman Melville wrote this whaling novel.", "What is Moby-Dick?"),
                ],
                600: [
                    qa("George Orwell also wrote this dystopian novel.", "What is 1984?"),
                    qa("Odysseus is the hero of this epic poem.", "What is The Odyssey?"),
                ],
                800: [
                    qa("Atticus Finch appears in this Harper Lee novel.", "What is To Kill a Mockingbird?"),
                    qa("This poet wrote The Raven.", "Who is Edgar Allan Poe?"),
                ],
                1000: [
                    qa("Gabriel García Márquez wrote this novel about the Buendía family.", "What is One Hundred Years of Solitude?"),
                    qa("Fyodor Dostoevsky wrote this novel featuring Raskolnikov.", "What is Crime and Punishment?"),
                ],
            },
            "Sports": {
                200: [
                    qa("This sport uses terms like birdie, eagle, and bogey.", "What is golf?"),
                    qa("A soccer team has this many players on the field at one time, including the goalkeeper.", "What is 11?"),
                ],
                400: [
                    qa("Michael Jordan played most famously for this NBA team.", "What are the Chicago Bulls?"),
                    qa("The Stanley Cup is awarded in this sport.", "What is hockey?"),
                ],
                600: [
                    qa("RBI in baseball stands for this.", "What is runs batted in?"),
                    qa("Wimbledon is associated with this sport.", "What is tennis?"),
                ],
                800: [
                    qa("Muhammad Ali was known by this self-chosen nickname.", "What is The Greatest?"),
                    qa("Fenway Park is home to this MLB team.", "Who are the Boston Red Sox?"),
                ],
                1000: [
                    qa("A green jacket is awarded to the winner of this tournament.", "What is The Masters?"),
                    qa("The Tour de France is contested in this sport.", "What is cycling?"),
                ],
            },
            "Hard Science": {
                200: [
                    qa("H2O is the chemical formula for this substance.", "What is water?"),
                    qa("A substance with a pH below 7 is this.", "What is acidic?"),
                ],
                400: [
                    qa("This branch of physics studies heat, work, temperature, and energy transfer.", "What is thermodynamics?"),
                    qa("This subatomic particle has a negative electric charge.", "What is an electron?"),
                ],
                600: [
                    qa("This scientist proposed the uncertainty principle.", "Who is Werner Heisenberg?"),
                    qa("This organelle is often called the powerhouse of the cell.", "What is the mitochondrion?"),
                ],
                800: [
                    qa("Sodium's chemical symbol is this.", "What is Na?"),
                    qa("This blood cell type helps fight infection.", "What are white blood cells?"),
                ],
                1000: [
                    qa("This scale measures acidity and basicity.", "What is the pH scale?"),
                    qa("Isaac Newton is associated with these three famous laws.", "What are the laws of motion?"),
                ],
            },
            "2000s-2020s Pop Culture": {
                200: [
                    qa("This HBO fantasy series ended in 2019 after eight seasons.", "What is Game of Thrones?"),
                    qa("Many Marvel heroes reunited in this blockbuster after Infinity War.", "What is Avengers: Endgame?"),
                ],
                400: [
                    qa("This short-form video app exploded globally in the late 2010s and early 2020s.", "What is TikTok?"),
                    qa("Greta Gerwig directed this 2023 movie based on a famous Mattel doll.", "What is Barbie?"),
                ],
                600: [
                    qa("Kendrick Lamar won a Pulitzer Prize for this album.", "What is DAMN.?"),
                    qa("This singer's Eras Tour became a huge global phenomenon.", "Who is Taylor Swift?"),
                ],
                800: [
                    qa("Pedro Pascal starred as Joel in this HBO adaptation of a hit video game.", "What is The Last of Us?"),
                    qa("This sci-fi series on Netflix helped revive Kate Bush's Running Up That Hill.", "What is Stranger Things?"),
                ],
                1000: [
                    qa("This South Korean series about deadly games became a global hit in 2021.", "What is Squid Game?"),
                    qa("This pop star's album Sour featured songs like drivers license and good 4 u.", "Who is Olivia Rodrigo?"),
                ],
            },
            "Myth & Legend": {
                200: [
                    qa("In Greek myth, this hero slew the Minotaur.", "Who is Theseus?"),
                    qa("This Norse god wields the hammer Mjolnir.", "Who is Thor?"),
                ],
                400: [
                    qa("This Greek king's touch turned things to gold.", "Who is Midas?"),
                    qa("The winged horse of Greek myth is this.", "Who is Pegasus?"),
                ],
                600: [
                    qa("This river in Greek mythology was crossed by Charon.", "What is the Styx?"),
                    qa("In Arthurian legend, this sword was drawn from the stone.", "What is Excalibur?"),
                ],
                800: [
                    qa("This creature guards treasure and breathes fire in many legends.", "What is a dragon?"),
                    qa("Odin belongs to this mythology.", "What is Norse mythology?"),
                ],
                1000: [
                    qa("This city was said to be destroyed after Greek warriors emerged from a wooden horse.", "What is Troy?"),
                    qa("The Labyrinth was built on this island.", "What is Crete?"),
                ],
            },
            "Animals": {
                200: [
                    qa("The largest land animal.", "What is the African elephant?"),
                    qa("This mammal is the only one capable of powered flight.", "What is a bat?"),
                ],
                400: [
                    qa("A group of lions is called this.", "What is a pride?"),
                    qa("This animal is famous for building dams.", "What is a beaver?"),
                ],
                600: [
                    qa("The fastest land animal.", "What is the cheetah?"),
                    qa("A baby sheep is called this.", "What is a lamb?"),
                ],
                800: [
                    qa("The largest species of penguin.", "What is the emperor penguin?"),
                    qa("This Australian animal has fingerprints so close to humans they can confuse investigators.", "What is a koala?"),
                ],
                1000: [
                    qa("This intelligent marine mammal is known for echolocation.", "What is a dolphin?"),
                    qa("This bird can rotate its head dramatically and usually hunts at night.", "What is an owl?"),
                ],
            },
            "Math & Logic": {
                200: [
                    qa("A triangle with all three sides equal is called this.", "What is an equilateral triangle?"),
                    qa("This Roman numeral represents 50.", "What is L?"),
                ],
                400: [
                    qa("A data structure that uses FIFO order.", "What is a queue?"),
                    qa("The result of 12 times 12.", "What is 144?"),
                ],
                600: [
                    qa("In algebra, a value that makes an equation true is often called this.", "What is a solution?"),
                    qa("A number divisible only by 1 and itself is called this.", "What is a prime number?"),
                ],
                800: [
                    qa("This branch of math studies points, lines, angles, and shapes.", "What is geometry?"),
                    qa("A statement that is true by definition or assumed as a starting point is often called this.", "What is an axiom?"),
                ],
                1000: [
                    qa("This famous sequence begins 1, 1, 2, 3, 5, 8.", "What is the Fibonacci sequence?"),
                    qa("In computing and logic, true/false algebra is named for this mathematician.", "Who is George Boole?"),
                ],
            },
        },
    },
}

FINAL_BANK = [
    {
        "category": "Final Jiporady: Pop Culture + Tech",
        "question": "This 1999 sci-fi film shares its title with a mathematical structure used in computer science and linear algebra.",
        "answer": "What is The Matrix?",
    },
    {
        "category": "Final Jiporady: World History",
        "question": "This 1215 document is often described as an early limitation on the power of the English king.",
        "answer": "What is the Magna Carta?",
    },
    {
        "category": "Final Jiporady: Literature",
        "question": "This author created Middle-earth and wrote The Hobbit and The Lord of the Rings.",
        "answer": "Who is J.R.R. Tolkien?",
    },
    {
        "category": "Final Jiporady: Science",
        "question": "This planet is famous for its prominent ring system and is the second largest in our solar system.",
        "answer": "What is Saturn?",
    },
    {
        "category": "Final Jiporady: Geography",
        "question": "This African river flows north and is strongly associated with Egypt.",
        "answer": "What is the Nile?",
    },
    {
        "category": "Final Jiporady: Computing",
        "question": "This system translates domain names like example.com into numeric network addresses.",
        "answer": "What is DNS?",
    },
]