from copy import deepcopy

QUESTION_BANK = {
    "Science": {
        200: [
            {"question": "What planet is known as the Red Planet?", "answer": "Mars"},
            {"question": "What gas do plants absorb from the atmosphere?", "answer": "Carbon dioxide"},
            {"question": "What force keeps us on the ground?", "answer": "Gravity"},
        ],
        400: [
            {"question": "What part of the cell contains genetic material?", "answer": "The nucleus"},
            {"question": "What is H2O more commonly known as?", "answer": "Water"},
            {"question": "What organ pumps blood through the human body?", "answer": "The heart"},
        ],
        600: [
            {"question": "What is the speed of light commonly rounded to in miles per second?", "answer": "186,000 miles per second"},
            {"question": "What is the chemical symbol for sodium?", "answer": "Na"},
            {"question": "What process converts sugar into energy inside cells?", "answer": "Cellular respiration"},
        ],
        800: [
            {"question": "What branch of physics studies heat and energy transfer?", "answer": "Thermodynamics"},
            {"question": "What is the powerhouse of the cell?", "answer": "The mitochondrion"},
            {"question": "What type of blood cells help fight infection?", "answer": "White blood cells"},
        ],
        1000: [
            {"question": "What is the second most abundant gas in Earth’s atmosphere?", "answer": "Oxygen"},
            {"question": "What scientist proposed the three laws of motion?", "answer": "Isaac Newton"},
            {"question": "What scale measures the acidity or basicity of a substance?", "answer": "The pH scale"},
        ],
    },

    "History": {
        200: [
            {"question": "What ancient civilization built the pyramids?", "answer": "The Egyptians"},
            {"question": "Who was the first president of the United States?", "answer": "George Washington"},
            {"question": "What wall famously divided Berlin?", "answer": "The Berlin Wall"},
        ],
        400: [
            {"question": "In what year did World War II end?", "answer": "1945"},
            {"question": "Who was known as the Maid of Orléans?", "answer": "Joan of Arc"},
            {"question": "What ship sank on its maiden voyage in 1912?", "answer": "The Titanic"},
        ],
        600: [
            {"question": "What empire was ruled by Julius Caesar?", "answer": "Rome / the Roman Republic"},
            {"question": "What document begins with 'We the People'?", "answer": "The U.S. Constitution"},
            {"question": "Who purchased Alaska from Russia?", "answer": "The United States"},
        ],
        800: [
            {"question": "What war was fought between the North and South regions of the United States?", "answer": "The Civil War"},
            {"question": "Who was the British prime minister during most of World War II?", "answer": "Winston Churchill"},
            {"question": "What year did the French Revolution begin?", "answer": "1789"},
        ],
        1000: [
            {"question": "What peace treaty ended World War I?", "answer": "The Treaty of Versailles"},
            {"question": "Who was the first emperor of Rome?", "answer": "Augustus"},
            {"question": "What dynasty built much of the Great Wall of China as seen today?", "answer": "The Ming Dynasty"},
        ],
    },

    "Geography": {
        200: [
            {"question": "What is the largest ocean on Earth?", "answer": "The Pacific Ocean"},
            {"question": "What river runs through Egypt?", "answer": "The Nile"},
            {"question": "What country is directly north of the United States?", "answer": "Canada"},
        ],
        400: [
            {"question": "What is the capital of Japan?", "answer": "Tokyo"},
            {"question": "What desert covers much of northern Africa?", "answer": "The Sahara"},
            {"question": "What mountain range includes Mount Everest?", "answer": "The Himalayas"},
        ],
        600: [
            {"question": "What is the smallest U.S. state by area?", "answer": "Rhode Island"},
            {"question": "What country has the city of Barcelona?", "answer": "Spain"},
            {"question": "What is the longest river in South America?", "answer": "The Amazon River"},
        ],
        800: [
            {"question": "What is the capital of Australia?", "answer": "Canberra"},
            {"question": "What strait separates Asia from North America?", "answer": "The Bering Strait"},
            {"question": "What African lake is the source of the White Nile?", "answer": "Lake Victoria"},
        ],
        1000: [
            {"question": "What is the world’s largest island that is not a continent?", "answer": "Greenland"},
            {"question": "What is the capital of Kazakhstan?", "answer": "Astana"},
            {"question": "What sea lies between Europe and Africa?", "answer": "The Mediterranean Sea"},
        ],
    },

    "Movies": {
        200: [
            {"question": "What film features a shark terrorizing Amity Island?", "answer": "Jaws"},
            {"question": "Who is the wizard headmaster in Harry Potter?", "answer": "Albus Dumbledore"},
            {"question": "What yellow creatures appear in Despicable Me?", "answer": "Minions"},
        ],
        400: [
            {"question": "What movie says 'Life is like a box of chocolates'?", "answer": "Forrest Gump"},
            {"question": "What 1997 film is about a doomed ocean liner romance?", "answer": "Titanic"},
            {"question": "What film introduced audiences to Wakanda?", "answer": "Black Panther"},
        ],
        600: [
            {"question": "Who directed E.T. the Extra-Terrestrial?", "answer": "Steven Spielberg"},
            {"question": "What movie features the song 'Let It Go'?", "answer": "Frozen"},
            {"question": "What is the name of Han Solo’s ship?", "answer": "The Millennium Falcon"},
        ],
        800: [
            {"question": "What film won Best Picture at the Oscars for 2020 ceremony?", "answer": "Parasite"},
            {"question": "Who played the Joker in The Dark Knight?", "answer": "Heath Ledger"},
            {"question": "What trilogy includes the character Aragorn?", "answer": "The Lord of the Rings"},
        ],
        1000: [
            {"question": "What Akira Kurosawa film inspired many later westerns and ensemble stories?", "answer": "Seven Samurai"},
            {"question": "What 1942 classic is set largely in Morocco?", "answer": "Casablanca"},
            {"question": "What film follows Cobb through layered dreams?", "answer": "Inception"},
        ],
    },

    "Music": {
        200: [
            {"question": "How many keys are on a standard piano?", "answer": "88"},
            {"question": "What instrument has six strings and is often electric or acoustic?", "answer": "The guitar"},
            {"question": "What clef is commonly used for higher-pitched notes?", "answer": "Treble clef"},
        ],
        400: [
            {"question": "What family of instruments includes trumpet and trombone?", "answer": "Brass"},
            {"question": "Who is known as the King of Pop?", "answer": "Michael Jackson"},
            {"question": "What band recorded 'Hey Jude'?", "answer": "The Beatles"},
        ],
        600: [
            {"question": "What is the musical term for gradually getting louder?", "answer": "Crescendo"},
            {"question": "What composer wrote The Four Seasons?", "answer": "Vivaldi"},
            {"question": "What singer is nicknamed 'The Boss'?", "answer": "Bruce Springsteen"},
        ],
        800: [
            {"question": "What genre originated in Jamaica and influenced ska and dub?", "answer": "Reggae"},
            {"question": "What singer released the album 21?", "answer": "Adele"},
            {"question": "What instrument does Yo-Yo Ma play?", "answer": "The cello"},
        ],
        1000: [
            {"question": "Who composed the Moonlight Sonata?", "answer": "Beethoven"},
            {"question": "What singer-songwriter wrote 'Like a Rolling Stone'?", "answer": "Bob Dylan"},
            {"question": "What city is strongly associated with Motown?", "answer": "Detroit"},
        ],
    },

    "Sports": {
        200: [
            {"question": "How many points is a touchdown worth in American football?", "answer": "6"},
            {"question": "What sport uses a puck?", "answer": "Hockey"},
            {"question": "In baseball, how many strikes make an out?", "answer": "3"},
        ],
        400: [
            {"question": "What country hosted the 2016 Summer Olympics?", "answer": "Brazil"},
            {"question": "What sport is Wimbledon associated with?", "answer": "Tennis"},
            {"question": "How many players are on the court for one basketball team at a time?", "answer": "5"},
        ],
        600: [
            {"question": "What golfer is nicknamed Tiger?", "answer": "Tiger Woods"},
            {"question": "What race is known as 'The Fastest Two Minutes in Sports'?", "answer": "The Kentucky Derby"},
            {"question": "What sport features the Tour de France?", "answer": "Cycling"},
        ],
        800: [
            {"question": "What country invented judo?", "answer": "Japan"},
            {"question": "What is the maximum score with one dart in standard darts?", "answer": "60"},
            {"question": "What MLB team is associated with Fenway Park?", "answer": "The Boston Red Sox"},
        ],
        1000: [
            {"question": "What boxer was known as 'The Greatest'?", "answer": "Muhammad Ali"},
            {"question": "What sport awards a green jacket to its champion?", "answer": "Golf / The Masters"},
            {"question": "In soccer, what is a score of 0-0 often called?", "answer": "A nil-nil draw"},
        ],
    },

    "Literature": {
        200: [
            {"question": "Who wrote Charlotte’s Web?", "answer": "E. B. White"},
            {"question": "Who created Sherlock Holmes?", "answer": "Arthur Conan Doyle"},
            {"question": "What is the last name of Tom Sawyer’s creator, Mark?", "answer": "Twain"},
        ],
        400: [
            {"question": "Who wrote Pride and Prejudice?", "answer": "Jane Austen"},
            {"question": "What novel begins with Ishmael narrating a whaling voyage?", "answer": "Moby-Dick"},
            {"question": "Who wrote The Great Gatsby?", "answer": "F. Scott Fitzgerald"},
        ],
        600: [
            {"question": "Who wrote 1984?", "answer": "George Orwell"},
            {"question": "What epic poem features Odysseus returning home?", "answer": "The Odyssey"},
            {"question": "Who wrote The Raven?", "answer": "Edgar Allan Poe"},
        ],
        800: [
            {"question": "What Shakespeare play features Rosencrantz and Guildenstern?", "answer": "Hamlet"},
            {"question": "Who wrote Beloved?", "answer": "Toni Morrison"},
            {"question": "What novel features Atticus Finch?", "answer": "To Kill a Mockingbird"},
        ],
        1000: [
            {"question": "Who wrote One Hundred Years of Solitude?", "answer": "Gabriel García Márquez"},
            {"question": "What Russian author wrote Crime and Punishment?", "answer": "Fyodor Dostoevsky"},
            {"question": "Who wrote The Sound and the Fury?", "answer": "William Faulkner"},
        ],
    },

    "Technology": {
        200: [
            {"question": "What does CPU stand for?", "answer": "Central Processing Unit"},
            {"question": "What company created Windows?", "answer": "Microsoft"},
            {"question": "What does URL stand for?", "answer": "Uniform Resource Locator"},
        ],
        400: [
            {"question": "What language is primarily used to style web pages?", "answer": "CSS"},
            {"question": "What does RAM stand for?", "answer": "Random Access Memory"},
            {"question": "What open-source operating system kernel powers many servers?", "answer": "Linux"},
        ],
        600: [
            {"question": "What protocol commonly secures web traffic with encryption?", "answer": "HTTPS"},
            {"question": "In Git, what command copies a repository to your local machine?", "answer": "git clone"},
            {"question": "What company created the iPhone?", "answer": "Apple"},
        ],
        800: [
            {"question": "What database language uses SELECT statements?", "answer": "SQL"},
            {"question": "What does API stand for?", "answer": "Application Programming Interface"},
            {"question": "What tag usually contains JavaScript in an HTML page?", "answer": "<script>"},
        ],
        1000: [
            {"question": "What data structure uses FIFO order?", "answer": "A queue"},
            {"question": "What does DNS translate domain names into?", "answer": "IP addresses"},
            {"question": "What version control system is widely used with GitHub?", "answer": "Git"},
        ],
    },

    "Random Trivia": {
        200: [
            {"question": "What color do you get when you mix blue and yellow?", "answer": "Green"},
            {"question": "How many sides does a hexagon have?", "answer": "6"},
            {"question": "What day comes after Friday?", "answer": "Saturday"},
        ],
        400: [
            {"question": "What is the largest mammal?", "answer": "The blue whale"},
            {"question": "What is the common name for a baby kangaroo?", "answer": "A joey"},
            {"question": "What board game features Park Place and Boardwalk?", "answer": "Monopoly"},
        ],
        600: [
            {"question": "What is the only letter not used in the periodic table?", "answer": "J"},
            {"question": "What is the tallest breed of dog?", "answer": "The Great Dane"},
            {"question": "What planet has the most moons currently recognized in common trivia?", "answer": "Saturn"},
        ],
        800: [
            {"question": "What is the fear of spiders called?", "answer": "Arachnophobia"},
            {"question": "What does a vexillologist study?", "answer": "Flags"},
            {"question": "What is the national animal of Scotland in mythology?", "answer": "The unicorn"},
        ],
        1000: [
            {"question": "What chess piece can move in an L-shape?", "answer": "The knight"},
            {"question": "What is the world’s most spoken native language?", "answer": "Mandarin Chinese"},
            {"question": "What does the 'D' in D-Day stand for?", "answer": "It does not stand for anything specific / Day"},
        ],
    },

    "Food & Drink": {
        200: [
            {"question": "What fruit is used to make guacamole?", "answer": "Avocado"},
            {"question": "What dairy product is commonly added to coffee?", "answer": "Milk / cream"},
            {"question": "Sushi is most associated with what country?", "answer": "Japan"},
        ],
        400: [
            {"question": "What grain is risotto usually made from?", "answer": "Rice"},
            {"question": "What vitamin is especially associated with citrus fruits?", "answer": "Vitamin C"},
            {"question": "What Italian dish is layered with pasta, sauce, and cheese?", "answer": "Lasagna"},
        ],
        600: [
            {"question": "What spice is most associated with yellow curry color?", "answer": "Turmeric"},
            {"question": "What French term means 'everything in its place' in professional kitchens?", "answer": "Mise en place"},
            {"question": "What cut of pork is used for pulled pork barbecue?", "answer": "Pork shoulder / Boston butt"},
        ],
        800: [
            {"question": "What cheese is traditionally used in a Greek salad?", "answer": "Feta"},
            {"question": "What is the primary spirit in a traditional martini?", "answer": "Gin"},
            {"question": "What bean is used to make tofu?", "answer": "Soybean"},
        ],
        1000: [
            {"question": "What Japanese dish consists of vinegared rice with toppings or fillings?", "answer": "Sushi"},
            {"question": "What process turns grape juice into wine?", "answer": "Fermentation"},
            {"question": "What is the French mother sauce made from milk thickened with a white roux?", "answer": "Béchamel"},
        ],
    },

    "Animals": {
        200: [
            {"question": "What is the largest land animal?", "answer": "The African elephant"},
            {"question": "What animal is known for changing color to blend in?", "answer": "The chameleon"},
            {"question": "What bird is the symbol of peace?", "answer": "The dove"},
        ],
        400: [
            {"question": "What mammal can truly fly?", "answer": "The bat"},
            {"question": "What is a group of lions called?", "answer": "A pride"},
            {"question": "What animal is famous for building dams?", "answer": "The beaver"},
        ],
        600: [
            {"question": "What is the fastest land animal?", "answer": "The cheetah"},
            {"question": "What marine mammal is known for echolocation and high intelligence?", "answer": "The dolphin"},
            {"question": "What is a baby sheep called?", "answer": "A lamb"},
        ],
        800: [
            {"question": "What is the largest species of penguin?", "answer": "The emperor penguin"},
            {"question": "What animal’s fingerprints are so close to humans they can confuse crime scenes?", "answer": "The koala"},
            {"question": "What reptile has no legs and sheds its skin?", "answer": "A snake"},
        ],
        1000: [
            {"question": "What bird can rotate its head dramatically and hunts mostly at night?", "answer": "An owl"},
            {"question": "What horned African herbivore is often confused with the Asian water buffalo?", "answer": "The wildebeest / gnu"},
            {"question": "What is the only mammal capable of powered flight?", "answer": "The bat"},
        ],
    },
}


def get_master_bank():
    return deepcopy(QUESTION_BANK)