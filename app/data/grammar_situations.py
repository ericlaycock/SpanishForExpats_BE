"""Grammar situation configuration — single source of truth.

Each entry defines the grammar situation's word workload, drill type,
phase availability, and conversation config for phases 2/3.
"""

GRAMMAR_WORD_TRANSLATIONS = {
    # Pronouns
    "yo": "I (subject pronoun)",
    "tú": "you (informal)",
    "tu": "your (informal)",
    "él": "he/him",
    "ella": "she/her",
    "usted": "you (formal)",
    "nosotros": "we (masc./mixed)",
    "nosotras": "we (all fem.)",
    "ellos": "they (masc./mixed)",
    "ellas": "they (all fem.)",
    "ustedes": "you all (formal plural)",
    "su": "his/her/your/their",
    # Articles
    "el": "the (masculine)",
    "los": "the (masc. plural)",
    "la": "the (feminine)",
    "las": "the (fem. plural)",
    "un": "a (masc.)",
    "unos": "some (masc.)",
    "una": "a (fem.)",
    "unas": "some (fem.)",
    # Verbs
    "hablar": "to speak",
    "escuchar": "to listen",
    "beber": "to drink",
    "comer": "to eat",
    "vivir": "to live",
    "escribir": "to write",
    "ser": "to be (permanent)",
    "estar": "to be (temporary)",
    "ir": "to go",
    "dar": "to give",
    "tener": "to have",
    "venir": "to come",
    "caer": "to fall",
    "traer": "to bring",
    "hacer": "to do/make",
    "poner": "to put",
    "salir": "to leave/go out",
    "valer": "to be worth",
    "decir": "to say/tell",
    "oír": "to hear",
    "conseguir": "to get/obtain",
    "recoger": "to pick up",
    "dirigir": "to direct",
    "convencer": "to convince",
    "conocer": "to know (person/place)",
    "producir": "to produce",
    "construir": "to build",
    "continuar": "to continue",
    "mover": "to move",
    "almorzar": "to have lunch",
    "morir": "to die",
    "cerrar": "to close",
    "entender": "to understand",
    "pedir": "to ask for",
    "repetir": "to repeat",
    "encontrar": "to find",
    "unir": "to join/unite",
    "ver": "to see",
    "dormir": "to sleep",
    "caminar": "to walk",
    "charlar": "to chat",
    "inhibir": "to inhibit",
    "prohibir": "to prohibit",
    "gusta": "is pleasing (sing.)",
    "gustan": "are pleasing (pl.)",
    # New verbs added for multi-lesson grammar
    "cantar": "to sing",
    "leer": "to read",
    "abrir": "to open",
    "poder": "to be able",
    "dormir": "to sleep",
    "volver": "to return",
    "pensar": "to think",
    "querer": "to want",
    "preferir": "to prefer",
    "empezar": "to begin",
    "seguir": "to follow/continue",
    "servir": "to serve",
    "vestir": "to dress",
    "elegir": "to choose",
    "estudiar": "to study",    # Added by build_grammar_lessons.py
    'lavarse': 'to wash oneself',
    'llamarse': 'to be called',
    'levantarse': 'to get up',
    'ducharse': 'to shower',
    'despertarse': 'to wake up',
    'acostarse': 'to go to bed',
    'vestirse': 'to get dressed',
    'sentarse': 'to sit down',
    'pagar': 'to pay',
    'jugar': 'to play',
    'buscar': 'to look for',
    'tocar': 'to touch/play (instrument)',
    'creer': 'to believe',
    'fluir': 'to flow',
    'andar': 'to walk/wander',
    'haber': 'to have (auxiliary)',
    'caber': 'to fit',
    'mantener': 'to maintain',
    'obtener': 'to obtain',
    'traducir': 'to translate',
    'conducir': 'to drive',
    'introducir': 'to introduce',
    'sentir': 'to feel',
    'lo': 'him/it (direct, masc.)',
    'le': 'to him/her/you (indirect)',
    'les': 'to them (indirect)',
    'se': 'to him/her/them (used before lo/la/los/las)',
    'me': 'to/for me',
    'te': 'to/for you',
    'nos': 'to/for us',
    'preterite': 'preterite (completed past)',
    'imperfect': 'imperfect (ongoing past)',
}

PRONOUNS = ["yo", "tú", "él", "ella", "usted", "nosotros", "nosotras", "ellos", "ellas", "ustedes"]

# Grammar Level → Vocab Level threshold mapping.
# A user is "overmatched" (and gated) when their VL >= the threshold for the next GL.
GL_VL_THRESHOLDS: dict[float, int] = {
    1: 10, 1.5: 10, 2: 15, 3: 100, 4: 200, 4.1: 200, 4.2: 200, 4.3: 200, 4.4: 200,
    4.5: 240, 5: 260, 5.5: 260,
    6: 300, 7: 330, 8: 400, 9: 500, 10: 510, 10.3: 515,
    10.6: 520, 11: 550, 12: 600, 13: 700, 13.5: 700, 14: 750, 15: 800,
    16: 900, 17: 1000, 17.1: 1010, 17.2: 1020, 17.3: 1030,
    17.4: 1050, 17.5: 1060, 18: 1300, 18.5: 1350, 19: 1400, 20: 1500,
}

# Titles for ALL grammar levels (including those without content yet).
GL_TITLES: dict[float, str] = {
    1: "Pronouns", 1.5: "Possessive Adjectives", 2: "Grammatical Gender", 3: "Regular Present",
    4: "Irregular Present", 4.1: "Ser vs. Estar", 4.2: "Por vs. Para",
    4.3: "Demonstratives", 4.4: "Possessive Pronouns",
    4.5: "Irregular Present II",
    5: "Spelling Changes", 5.5: "Saber vs. Conocer",
    6: "Present O→UE", 7: "Present E→IE",
    8: "Present E→I", 9: "Ir A + Infinitive",
    10: "Gustar Part 1", 10.3: "Gustar Part 2", 10.6: "Gustar Part 3",
    11: "Tengo que / Me toca / Necesito", 12: "Imperfect",
    13: "Reflexive", 13.5: "Imperatives", 14: "Future Simple", 15: "Conditional",
    16: "Preterite vs Imperfect", 17: "Preterite Regular",
    17.1: "Preterite Highly Irregular", 17.2: "Preterite Weird Spelling Changes",
    17.3: "Preterite Stem Changers", 17.4: "Preterite DUCIR",
    17.5: "Preterite e-to-i Irregular", 18: "Gerund",
    18.5: "Perfect Tenses",
    19: "Direct + Indirect Object Pronouns", 20: "Subjunctive",
}

# Sorted list of all grammar levels for iteration.
GL_SORTED = sorted(GL_VL_THRESHOLDS.keys())

GRAMMAR_SITUATIONS = {
    "grammar_pronouns": {
        "title": "Pronouns (singular)",
        "grammar_level": 1,
        "lesson_number": 1,
        "lesson_type": "rule",
        "word_workload": ["yo", "tú", "él", "ella", "usted"],
        "video_embed_id": "bLZk006G5ge",
        "drill_type": "rule",
        "tense": "pronouns",
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "rule_chart": {'kind': 'table', 'title': 'Subject pronouns (singular)', 'headers': ['Person', 'Pronoun', 'English', 'Note'], 'rows': [['1st sg', 'yo', 'I', ''], ['2nd sg informal', 'tú', 'you', 'casual / friends / family'], ['3rd sg masc', 'él', 'he', ''], ['3rd sg fem', 'ella', 'she', ''], ['2nd sg formal', 'usted', 'you', 'polite / strangers / older / authority']], 'footnote': "Latin America uses 'tú' and 'usted' for the singular 'you'. The choice is about register, not number."},
        "drill_sentences": [
            {"en": "I am tall", "es": "Yo soy alto", "noun_id": None, "type": "written"},
            {"en": "You are a tourist", "es": "Tú eres turista", "noun_id": None, "type": "auditory"},
            {"en": "He is important", "es": "Él es importante", "noun_id": None, "type": "written"},
            {"en": "She is elegant", "es": "Ella es elegante", "noun_id": None, "type": "auditory"},
            {"en": "You are professional", "es": "Usted es profesional", "noun_id": None, "type": "written"},
            {"en": "I am sociable", "es": "Yo soy social", "noun_id": None, "type": "auditory"},
            {"en": "You are international", "es": "Tú eres internacional", "noun_id": None, "type": "written"},
            {"en": "He is sociable", "es": "Él es social", "noun_id": None, "type": "auditory"},
            {"en": "She is important", "es": "Ella es importante", "noun_id": None, "type": "written"},
            {"en": "You are likeable", "es": "Usted es simpático", "noun_id": None, "type": "auditory"},
        ],
    },
    # --- GL 1: Pronouns (plural drill) ---
    "grammar_pronouns_plural": {
        "title": "Pronouns (plural)",
        "grammar_level": 1,
        "lesson_number": 2,
        "lesson_type": "rule",
        "word_workload": ["nosotros", "nosotras", "ellos", "ellas", "ustedes"],
        "video_embed_id": None,
        "drill_type": "rule",
        "tense": "pronouns",
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "rule_chart": {'kind': 'table', 'title': 'Subject pronouns (plural)', 'headers': ['Person', 'Pronoun', 'English', 'Note'], 'rows': [['1st pl masc/mixed', 'nosotros', 'we', ''], ['1st pl all-fem', 'nosotras', 'we', 'all-female group'], ['3rd pl masc/mixed', 'ellos', 'they', ''], ['3rd pl all-fem', 'ellas', 'they', 'all-female group'], ['2nd pl', 'ustedes', 'you all', "Latin America uses 'ustedes' for both formal and informal plural."]]},
        "drill_sentences": [
            {"en": "We are Colombian", "es": "Nosotros somos colombianos", "noun_id": None, "type": "written"},
            {"en": "We (f) are Latin", "es": "Nosotras somos latinas", "noun_id": None, "type": "auditory"},
            {"en": "They are sociable", "es": "Ellos son sociales", "noun_id": None, "type": "written"},
            {"en": "They (f) are professional", "es": "Ellas son profesionales", "noun_id": None, "type": "auditory"},
            {"en": "You all are tourists", "es": "Ustedes son turistas", "noun_id": None, "type": "written"},
            {"en": "We are important", "es": "Nosotros somos importantes", "noun_id": None, "type": "auditory"},
            {"en": "We (f) are international", "es": "Nosotras somos internacionales", "noun_id": None, "type": "written"},
            {"en": "They are likeable", "es": "Ellos son simpáticos", "noun_id": None, "type": "auditory"},
            {"en": "They (f) are elegant", "es": "Ellas son elegantes", "noun_id": None, "type": "written"},
            {"en": "You all are tall", "es": "Ustedes son altos", "noun_id": None, "type": "auditory"},
        ],
    },
    # --- GL 1: Pronouns (chat) ---
    "grammar_pronouns_chat": {
        "title": "Pronouns — Chat",
        "grammar_level": 1,
        "lesson_number": 3,
        "lesson_type": "rule",
        "word_workload": ["yo", "tú", "él", "ella", "usted", "nosotros", "nosotras", "ellos", "ellas", "ustedes"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "pronouns",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {
            "description": "All 10 pronouns in conversation",
            "targets": [{"word": p} for p in ["yo", "tú", "él", "ella", "usted", "nosotros", "nosotras", "ellos", "ellas", "ustedes"]],
        },
    },
    # --- GL 1.5: Possessive Adjectives ---
    "grammar_possessive_adj": {
        "title": "Possessive Adjectives (singular)",
        "grammar_level": 1.5,
        "lesson_number": 1,
        "lesson_type": "rule",
        "word_workload": ["mi", "tu", "su", "nuestro", "nuestra"],
        "video_embed_id": None,
        "drill_type": "rule",
        "tense": "possessive",
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "rule_chart": {'kind': 'table', 'title': 'Possessive adjectives — singular', 'headers': ['Form', 'Used for', 'Example'], 'rows': [['mi', 'my', 'mi casa'], ['tu', 'your (informal)', 'tu amigo'], ['su', 'his / her / your (formal) / their', 'su carro'], ['nuestro', 'our (masculine noun)', 'nuestro perro'], ['nuestra', 'our (feminine noun)', 'nuestra familia']], 'footnote': "'nuestro' / 'nuestra' agrees with the noun's gender. The others don't change with gender — only with number (mi → mis, tu → tus, su → sus)."},
        "drill_sentences": [
            {"en": "my house", "es": "mi casa", "noun_id": "casa", "type": "written"},
            {"en": "your friend", "es": "tu amigo", "noun_id": "amigo", "type": "auditory"},
            {"en": "his car", "es": "su carro", "noun_id": "carro", "type": "written"},
            {"en": "our (f) family", "es": "nuestra familia", "noun_id": "familia", "type": "auditory"},
            {"en": "our (m) dog", "es": "nuestro perro", "noun_id": "perro", "type": "written"},
            {"en": "my book", "es": "mi libro", "noun_id": "libro", "type": "auditory"},
            {"en": "your name", "es": "tu nombre", "noun_id": "nombre", "type": "written"},
            {"en": "her work", "es": "su trabajo", "noun_id": "trabajo", "type": "auditory"},
            {"en": "our (f) city", "es": "nuestra ciudad", "noun_id": "ciudad", "type": "written"},
            {"en": "our (m) plan", "es": "nuestro plan", "noun_id": "plan", "type": "auditory"},
        ],
    },
    # --- GL 1.5: Possessive Adjectives (plural drill) ---
    "grammar_possessive_adj_plural": {
        "title": "Possessive Adjectives (plural)",
        "grammar_level": 1.5,
        "lesson_number": 2,
        "lesson_type": "rule",
        "word_workload": ["mis", "tus", "sus", "nuestros", "nuestras"],
        "video_embed_id": None,
        "drill_type": "rule",
        "tense": "possessive",
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "rule_chart": {'kind': 'table', 'title': 'Possessive adjectives — plural', 'headers': ['Form', 'Used for', 'Example'], 'rows': [['mis', 'my (plural)', 'mis libros'], ['tus', 'your (plural)', 'tus amigos'], ['sus', 'his/her/your(formal)/their (plural)', 'sus carros'], ['nuestros', 'our (masc. plural)', 'nuestros perros'], ['nuestras', 'our (fem. plural)', 'nuestras familias']]},
        "drill_sentences": [
            {"en": "my books", "es": "mis libros", "noun_id": "libro", "type": "written"},
            {"en": "your friends", "es": "tus amigos", "noun_id": "amigo", "type": "auditory"},
            {"en": "their cars", "es": "sus carros", "noun_id": "carro", "type": "written"},
            {"en": "our (f) families", "es": "nuestras familias", "noun_id": "familia", "type": "auditory"},
            {"en": "our (m) dogs", "es": "nuestros perros", "noun_id": "perro", "type": "written"},
            {"en": "my houses", "es": "mis casas", "noun_id": "casa", "type": "auditory"},
            {"en": "your works", "es": "tus trabajos", "noun_id": "trabajo", "type": "written"},
            {"en": "their plans", "es": "sus planes", "noun_id": "plan", "type": "auditory"},
            {"en": "our (f) cities", "es": "nuestras ciudades", "noun_id": "ciudad", "type": "written"},
            {"en": "our (m) names", "es": "nuestros nombres", "noun_id": "nombre", "type": "auditory"},
        ],
    },
    # --- GL 1.5: Possessive Adjectives (chat) ---
    "grammar_possessive_adj_chat": {
        "title": "Possessive Adjectives — Chat",
        "grammar_level": 1.5,
        "lesson_number": 3,
        "lesson_type": "rule",
        "word_workload": ["mi", "mis", "tu", "tus", "su", "sus", "nuestro", "nuestros", "nuestra", "nuestras"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "possessive",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {
            "description": "All possessive adjectives in conversation",
            "targets": [{"word": w} for w in ["mi", "mis", "tu", "tus", "su", "sus", "nuestro", "nuestros", "nuestra", "nuestras"]],
        },
    },
    "grammar_gender": {
        "title": "Grammatical Gender (definite)",
        "grammar_level": 2,
        "lesson_number": 1,
        "lesson_type": "rule",
        "word_workload": ["el", "la", "los", "las"],
        "video_embed_id": "aJguo8cBgm7",
        "drill_type": "rule",
        "tense": "gender",
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "rule_chart": {'kind': 'rule_pack', 'title': 'Spanish noun gender — endings', 'sections': [{'heading': 'MAJE LONERS — masculine endings', 'items': ['-ma  →  el problema, el sistema', '-je  →  el viaje, el pasaje', '-l  →  el animal, el papel', '-o  →  el libro, el caso', '-n  →  el limón, el examen', '-e  →  el café, el coche', '-r  →  el doctor, el actor', '-s  →  el atlas, el lunes']}, {'heading': 'DIONZA — feminine endings', 'items': ['-d  →  la libertad, la verdad', '-ion  →  la nación, la opción', '-z  →  la vez, la luz', '-a  →  la casa, la mesa']}], 'footnote': 'Definite articles: el / la (singular), los / las (plural). These rules cover most nouns; learn exceptions case-by-case.'},
        "drill_sentences": [
            {"en": "the problem", "es": "el problema", "noun_id": "problema", "type": "written"},
            {"en": "the trip", "es": "el viaje", "noun_id": "viaje", "type": "auditory"},
            {"en": "the animal", "es": "el animal", "noun_id": "animal", "type": "written"},
            {"en": "the book", "es": "el libro", "noun_id": "libro", "type": "auditory"},
            {"en": "the lemon", "es": "el limón", "noun_id": "limón", "type": "written"},
            {"en": "the coffee", "es": "el café", "noun_id": "café", "type": "auditory"},
            {"en": "the freedom", "es": "la libertad", "noun_id": "libertad", "type": "written"},
            {"en": "the nation", "es": "la nación", "noun_id": "nación", "type": "auditory"},
            {"en": "the time", "es": "la vez", "noun_id": "vez", "type": "written"},
            {"en": "the house", "es": "la casa", "noun_id": "casa", "type": "auditory"},
        ],
        "drill_config": {
            "curated_nouns": [
                {"spanish": "libro", "english": "book", "gender": "m", "ending_rule": "LONERS_o"},
                {"spanish": "papel", "english": "paper", "gender": "m", "ending_rule": "LONERS_l"},
                {"spanish": "pan", "english": "bread", "gender": "m", "ending_rule": "LONERS_n"},
                {"spanish": "café", "english": "coffee", "gender": "m", "ending_rule": "LONERS_e"},
                {"spanish": "amor", "english": "love", "gender": "m", "ending_rule": "LONERS_r"},
                {"spanish": "lunes", "english": "Monday", "gender": "m", "ending_rule": "LONERS_s"},
                {"spanish": "problema", "english": "problem", "gender": "m", "ending_rule": "MAJE_ma"},
                {"spanish": "viaje", "english": "trip", "gender": "m", "ending_rule": "MAJE_je"},
                {"spanish": "ciudad", "english": "city", "gender": "f", "ending_rule": "DIONZA_d"},
                {"spanish": "televisión", "english": "televisión", "gender": "f", "ending_rule": "DIONZA_ion"},
                {"spanish": "voz", "english": "voice", "gender": "f", "ending_rule": "DIONZA_z"},
                {"spanish": "casa", "english": "house", "gender": "f", "ending_rule": "DIONZA_a"},
                {"spanish": "mesa", "english": "table", "gender": "f", "ending_rule": "DIONZA_a"},
                {"spanish": "nación", "english": "nation", "gender": "f", "ending_rule": "DIONZA_ion"},
                {"spanish": "libertad", "english": "freedom", "gender": "f", "ending_rule": "DIONZA_d"},
                {"spanish": "luz", "english": "light", "gender": "f", "ending_rule": "DIONZA_z"},
                {"spanish": "gato", "english": "cat", "gender": "m", "ending_rule": "LONERS_o"},
                {"spanish": "sistema", "english": "system", "gender": "m", "ending_rule": "MAJE_ma"},
                {"spanish": "carne", "english": "meat", "gender": "f", "ending_rule": "exception_e"},
                {"spanish": "leche", "english": "milk", "gender": "f", "ending_rule": "exception_e"},
            ],
        },
        "phase_2_config": None,
    },
    # --- GL 2: Grammatical Gender (indefinite drill) ---
    "grammar_gender_indef": {
        "title": "Grammatical Gender (indefinite)",
        "grammar_level": 2,
        "lesson_number": 2,
        "lesson_type": "rule",
        "word_workload": ["un", "una", "unos", "unas"],
        "video_embed_id": None,
        "drill_type": "rule",
        "tense": "gender",
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "rule_chart": {'kind': 'rule_pack', 'title': 'Indefinite articles — un / una / unos / unas', 'sections': [{'heading': 'Singular', 'items': ['un + masculine noun  →  un libro, un actor', 'una + feminine noun  →  una verdad, una luz']}, {'heading': 'Plural', 'items': ['unos + masculine plural  →  unos libros', 'unas + feminine plural  →  unas verdades']}], 'footnote': "MAJE LONERS / DIONZA still apply: pick the article from the noun's ending."},
        "drill_sentences": [
            {"en": "a system", "es": "un sistema", "noun_id": "sistema", "type": "written"},
            {"en": "a passage", "es": "un pasaje", "noun_id": "pasaje", "type": "auditory"},
            {"en": "a paper", "es": "un papel", "noun_id": "papel", "type": "written"},
            {"en": "a case", "es": "un caso", "noun_id": "caso", "type": "auditory"},
            {"en": "an exam", "es": "un examen", "noun_id": "examen", "type": "written"},
            {"en": "an actor", "es": "un actor", "noun_id": "actor", "type": "auditory"},
            {"en": "an atlas", "es": "un atlas", "noun_id": "atlas", "type": "written"},
            {"en": "a truth", "es": "una verdad", "noun_id": "verdad", "type": "auditory"},
            {"en": "an option", "es": "una opción", "noun_id": "opción", "type": "written"},
            {"en": "a light", "es": "una luz", "noun_id": "luz", "type": "auditory"},
        ],
        "phase_2_config": None,
    },
    # --- GL 2: Grammatical Gender (chat) ---
    "grammar_gender_chat": {
        "title": "Grammatical Gender — Chat",
        "grammar_level": 2,
        "lesson_number": 3,
        "lesson_type": "rule",
        "word_workload": ["el", "la", "los", "las", "un", "una", "unos", "unas"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "gender",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {
            "description": "Articles + gendered nouns in conversation",
            "targets": [{"word": w} for w in ["el", "la", "los", "las", "un", "una", "unos", "unas"]],
        },
    },
    # --- GL 3: Regular Present — 3 lessons (1 -ar + 1 -er + 1 -ir each) ---
    "grammar_regular_present_1": {
        "title": "Regular Present (1/3)",
        "grammar_level": 3,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "beber", "vivir"],
        "video_embed_id": "6jpCj97AHMN",
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {
            "answers": {
                "hablar": {
                    "yo": "hablo", "tú": "hablas", "él": "habla", "ella": "habla",
                    "usted": "habla", "nosotros": "hablamos", "nosotras": "hablamos",
                    "ellos": "hablan", "ellas": "hablan", "ustedes": "hablan",
                },
                "beber": {
                    "yo": "bebo", "tú": "bebes", "él": "bebe", "ella": "bebe",
                    "usted": "bebe", "nosotros": "bebemos", "nosotras": "bebemos",
                    "ellos": "beben", "ellas": "beben", "ustedes": "beben",
                },
                "vivir": {
                    "yo": "vivo", "tú": "vives", "él": "vive", "ella": "vive",
                    "usted": "vive", "nosotros": "vivimos", "nosotras": "vivimos",
                    "ellos": "viven", "ellas": "viven", "ustedes": "viven",
                },
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I speak Spanish at home", "es": "Yo hablo español en casa", "noun_id": "casa", "type": "written"},
            {"en": "She speaks English", "es": "Ella habla inglés", "noun_id": None, "type": "auditory"},
            {"en": "You all speak well", "es": "Ustedes hablan bien", "noun_id": None, "type": "written"},
            {"en": "You drink coffee every day", "es": "Tú bebes café todos los días", "noun_id": "café", "type": "auditory"},
            {"en": "We (f) drink water", "es": "Nosotras bebemos agua", "noun_id": "agua", "type": "written"},
            {"en": "He drinks juice in the morning", "es": "Él bebe jugo por la mañana", "noun_id": "jugo", "type": "auditory"},
            {"en": "You live in the city", "es": "Usted vive en la ciudad", "noun_id": "ciudad", "type": "written"},
            {"en": "We live in a house", "es": "Nosotros vivimos en una casa", "noun_id": "casa", "type": "auditory"},
            {"en": "They (f) live here", "es": "Ellas viven aquí", "noun_id": None, "type": "written"},
            {"en": "They live in Colombia", "es": "Ellos viven en Colombia", "noun_id": None, "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "ella"},
            {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "beber", "pronoun": "tú"},
            {"verb": "beber", "pronoun": "nosotras"}, {"verb": "beber", "pronoun": "él"},
            {"verb": "vivir", "pronoun": "usted"}, {"verb": "vivir", "pronoun": "nosotros"},
            {"verb": "vivir", "pronoun": "ellas"}, {"verb": "vivir", "pronoun": "ellos"},
        ],
        "phase_2_config": {
            "description": "Regular Present lesson 1: hablar (-ar), beber (-er), vivir (-ir)",
            "targets": [
                {"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "ella"},
                {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "beber", "pronoun": "tú"},
                {"verb": "beber", "pronoun": "nosotras"}, {"verb": "beber", "pronoun": "él"},
                {"verb": "vivir", "pronoun": "usted"}, {"verb": "vivir", "pronoun": "nosotros"},
                {"verb": "vivir", "pronoun": "ellas"}, {"verb": "vivir", "pronoun": "ellos"},
            ],
        },
        "opener_en": "Do you speak English?",
        "opener_es": "¿Hablas inglés?",
    },
    # --- GL 3: chat companion of `grammar_regular_present_1` ---
    "grammar_regular_present_1_chat": {
        "title": "Regular Present (1/3) — Chat",
        "grammar_level": 3,
        "lesson_number": 1.1,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "beber", "vivir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Regular Present lesson 1: hablar (-ar), beber (-er), vivir (-ir)', 'targets': [{'verb': 'hablar', 'pronoun': 'yo'}, {'verb': 'hablar', 'pronoun': 'ella'}, {'verb': 'hablar', 'pronoun': 'ustedes'}, {'verb': 'beber', 'pronoun': 'tú'}, {'verb': 'beber', 'pronoun': 'nosotras'}, {'verb': 'beber', 'pronoun': 'él'}, {'verb': 'vivir', 'pronoun': 'usted'}, {'verb': 'vivir', 'pronoun': 'nosotros'}, {'verb': 'vivir', 'pronoun': 'ellas'}, {'verb': 'vivir', 'pronoun': 'ellos'}]},
    },
    "grammar_regular_present_2": {
        "title": "Regular Present (2/3)",
        "grammar_level": 3,
        "lesson_number": 2,
        "lesson_type": "conjugation",
        "word_workload": ["escuchar", "comer", "escribir"],
        "video_embed_id": "6jpCj97AHMN",
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {
            "answers": {
                "escuchar": {
                    "yo": "escucho", "tú": "escuchas", "él": "escucha", "ella": "escucha",
                    "usted": "escucha", "nosotros": "escuchamos", "nosotras": "escuchamos",
                    "ellos": "escuchan", "ellas": "escuchan", "ustedes": "escuchan",
                },
                "comer": {
                    "yo": "como", "tú": "comes", "él": "come", "ella": "come",
                    "usted": "come", "nosotros": "comemos", "nosotras": "comemos",
                    "ellos": "comen", "ellas": "comen", "ustedes": "comen",
                },
                "escribir": {
                    "yo": "escribo", "tú": "escribes", "él": "escribe", "ella": "escribe",
                    "usted": "escribe", "nosotros": "escribimos", "nosotras": "escribimos",
                    "ellos": "escriben", "ellas": "escriben", "ustedes": "escriben",
                },
            },
        },
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I listen to music every day", "es": "Yo escucho música todos los días", "noun_id": "música", "type": "written"},
            {"en": "You listen to the radio", "es": "Usted escucha la radio", "noun_id": None, "type": "auditory"},
            {"en": "They (f) listen at home", "es": "Ellas escuchan en casa", "noun_id": "casa", "type": "written"},
            {"en": "You eat meat at lunch", "es": "Tú comes carne al almuerzo", "noun_id": "carne", "type": "auditory"},
            {"en": "We eat bread every morning", "es": "Nosotros comemos pan cada mañana", "noun_id": "pan", "type": "written"},
            {"en": "She eats at the restaurant", "es": "Ella come en el restaurante", "noun_id": "restaurante", "type": "auditory"},
            {"en": "He writes a letter", "es": "Él escribe una carta", "noun_id": "carta", "type": "written"},
            {"en": "We (f) write in Spanish", "es": "Nosotras escribimos en español", "noun_id": None, "type": "auditory"},
            {"en": "You all write your names", "es": "Ustedes escriben sus nombres", "noun_id": None, "type": "written"},
            {"en": "They write books", "es": "Ellos escriben libros", "noun_id": "libro", "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "escuchar", "pronoun": "yo"}, {"verb": "escuchar", "pronoun": "usted"},
            {"verb": "escuchar", "pronoun": "ellas"}, {"verb": "comer", "pronoun": "tú"},
            {"verb": "comer", "pronoun": "nosotros"}, {"verb": "comer", "pronoun": "ella"},
            {"verb": "escribir", "pronoun": "él"}, {"verb": "escribir", "pronoun": "nosotras"},
            {"verb": "escribir", "pronoun": "ustedes"}, {"verb": "escribir", "pronoun": "ellos"},
        ],
        "phase_2_config": {
            "description": "Regular Present lesson 2: escuchar (-ar), comer (-er), escribir (-ir)",
            "targets": [
                {"verb": "escuchar", "pronoun": "yo"}, {"verb": "escuchar", "pronoun": "usted"},
                {"verb": "escuchar", "pronoun": "ellas"}, {"verb": "comer", "pronoun": "tú"},
                {"verb": "comer", "pronoun": "nosotros"}, {"verb": "comer", "pronoun": "ella"},
                {"verb": "escribir", "pronoun": "él"}, {"verb": "escribir", "pronoun": "nosotras"},
                {"verb": "escribir", "pronoun": "ustedes"}, {"verb": "escribir", "pronoun": "ellos"},
            ],
        },
        "opener_en": "What do you eat for lunch?",
        "opener_es": "¿Qué comes para el almuerzo?",
    },
    # --- GL 3: chat companion of `grammar_regular_present_2` ---
    "grammar_regular_present_2_chat": {
        "title": "Regular Present (2/3) — Chat",
        "grammar_level": 3,
        "lesson_number": 2.1,
        "lesson_type": "conjugation",
        "word_workload": ["escuchar", "comer", "escribir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Regular Present lesson 2: escuchar (-ar), comer (-er), escribir (-ir)', 'targets': [{'verb': 'escuchar', 'pronoun': 'yo'}, {'verb': 'escuchar', 'pronoun': 'usted'}, {'verb': 'escuchar', 'pronoun': 'ellas'}, {'verb': 'comer', 'pronoun': 'tú'}, {'verb': 'comer', 'pronoun': 'nosotros'}, {'verb': 'comer', 'pronoun': 'ella'}, {'verb': 'escribir', 'pronoun': 'él'}, {'verb': 'escribir', 'pronoun': 'nosotras'}, {'verb': 'escribir', 'pronoun': 'ustedes'}, {'verb': 'escribir', 'pronoun': 'ellos'}]},
    },
    "grammar_regular_present_3": {
        "title": "Regular Present (3/3)",
        "grammar_level": 3,
        "lesson_number": 3,
        "lesson_type": "conjugation",
        "word_workload": ["cantar", "leer", "abrir"],
        "video_embed_id": "6jpCj97AHMN",
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {
            "answers": {
                "cantar": {
                    "yo": "canto", "tú": "cantas", "él": "canta", "ella": "canta",
                    "usted": "canta", "nosotros": "cantamos", "nosotras": "cantamos",
                    "ellos": "cantan", "ellas": "cantan", "ustedes": "cantan",
                },
                "leer": {
                    "yo": "leo", "tú": "lees", "él": "lee", "ella": "lee",
                    "usted": "lee", "nosotros": "leemos", "nosotras": "leemos",
                    "ellos": "leen", "ellas": "leen", "ustedes": "leen",
                },
                "abrir": {
                    "yo": "abro", "tú": "abres", "él": "abre", "ella": "abre",
                    "usted": "abre", "nosotros": "abrimos", "nosotras": "abrimos",
                    "ellos": "abren", "ellas": "abren", "ustedes": "abren",
                },
            },
        },
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I sing at home", "es": "Yo canto en casa", "noun_id": "casa", "type": "written"},
            {"en": "We (f) sing in Spanish", "es": "Nosotras cantamos en español", "noun_id": None, "type": "auditory"},
            {"en": "You all sing well", "es": "Ustedes cantan bien", "noun_id": None, "type": "written"},
            {"en": "You read a book every day", "es": "Tú lees un libro cada día", "noun_id": "libro", "type": "auditory"},
            {"en": "She reads a book", "es": "Ella lee un libro", "noun_id": "libro", "type": "written"},
            {"en": "They read Spanish books", "es": "Ellos leen libros en español", "noun_id": "libro", "type": "auditory"},
            {"en": "He opens the door", "es": "Él abre la puerta", "noun_id": "puerta", "type": "written"},
            {"en": "You open the window", "es": "Usted abre la ventana", "noun_id": "ventana", "type": "auditory"},
            {"en": "We open the store", "es": "Nosotros abrimos la tienda", "noun_id": "tienda", "type": "written"},
            {"en": "They (f) open their books", "es": "Ellas abren sus libros", "noun_id": "libro", "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "cantar", "pronoun": "yo"}, {"verb": "cantar", "pronoun": "nosotras"},
            {"verb": "cantar", "pronoun": "ustedes"}, {"verb": "leer", "pronoun": "tú"},
            {"verb": "leer", "pronoun": "ella"}, {"verb": "leer", "pronoun": "ellos"},
            {"verb": "abrir", "pronoun": "él"}, {"verb": "abrir", "pronoun": "usted"},
            {"verb": "abrir", "pronoun": "nosotros"}, {"verb": "abrir", "pronoun": "ellas"},
        ],
        "phase_2_config": {
            "description": "Regular Present lesson 3: cantar (-ar), leer (-er), abrir (-ir)",
            "targets": [
                {"verb": "cantar", "pronoun": "yo"}, {"verb": "cantar", "pronoun": "nosotras"},
                {"verb": "cantar", "pronoun": "ustedes"}, {"verb": "leer", "pronoun": "tú"},
                {"verb": "leer", "pronoun": "ella"}, {"verb": "leer", "pronoun": "ellos"},
                {"verb": "abrir", "pronoun": "él"}, {"verb": "abrir", "pronoun": "usted"},
                {"verb": "abrir", "pronoun": "nosotros"}, {"verb": "abrir", "pronoun": "ellas"},
            ],
        },
        "opener_en": "Do you read in Spanish?",
        "opener_es": "¿Lees en español?",
    },
    # --- GL 3: chat companion of `grammar_regular_present_3` ---
    "grammar_regular_present_3_chat": {
        "title": "Regular Present (3/3) — Chat",
        "grammar_level": 3,
        "lesson_number": 3.1,
        "lesson_type": "conjugation",
        "word_workload": ["cantar", "leer", "abrir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Regular Present lesson 3: cantar (-ar), leer (-er), abrir (-ir)', 'targets': [{'verb': 'cantar', 'pronoun': 'yo'}, {'verb': 'cantar', 'pronoun': 'nosotras'}, {'verb': 'cantar', 'pronoun': 'ustedes'}, {'verb': 'leer', 'pronoun': 'tú'}, {'verb': 'leer', 'pronoun': 'ella'}, {'verb': 'leer', 'pronoun': 'ellos'}, {'verb': 'abrir', 'pronoun': 'él'}, {'verb': 'abrir', 'pronoun': 'usted'}, {'verb': 'abrir', 'pronoun': 'nosotros'}, {'verb': 'abrir', 'pronoun': 'ellas'}]},
    },
    # --- GL 4: Irregular Present — 3 lessons (all 6 verbs, pronouns distributed) ---
    "grammar_irregular_present_1": {
        "title": "Irregular Present (1/3)",
        "grammar_level": 4,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ["ser", "estar", "ir", "dar", "tener", "venir"],
        "video_embed_id": "sD2tovQc7pB",
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {"answers": {
            "ser": {"yo": "soy", "tú": "eres", "él": "es", "ella": "es", "usted": "es", "nosotros": "somos", "nosotras": "somos", "ellos": "son", "ellas": "son", "ustedes": "son"},
            "estar": {"yo": "estoy", "tú": "estás", "él": "está", "ella": "está", "usted": "está", "nosotros": "estamos", "nosotras": "estamos", "ellos": "están", "ellas": "están", "ustedes": "están"},
            "ir": {"yo": "voy", "tú": "vas", "él": "va", "ella": "va", "usted": "va", "nosotros": "vamos", "nosotras": "vamos", "ellos": "van", "ellas": "van", "ustedes": "van"},
            "dar": {"yo": "doy", "tú": "das", "él": "da", "ella": "da", "usted": "da", "nosotros": "damos", "nosotras": "damos", "ellos": "dan", "ellas": "dan", "ustedes": "dan"},
            "tener": {"yo": "tengo", "tú": "tienes", "él": "tiene", "ella": "tiene", "usted": "tiene", "nosotros": "tenemos", "nosotras": "tenemos", "ellos": "tienen", "ellas": "tienen", "ustedes": "tienen"},
            "venir": {"yo": "vengo", "tú": "vienes", "él": "viene", "ella": "viene", "usted": "viene", "nosotros": "venimos", "nosotras": "venimos", "ellos": "vienen", "ellas": "vienen", "ustedes": "vienen"},
        }},
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I am from Colombia", "es": "Yo soy de Colombia", "noun_id": None, "type": "written"},
            {"en": "She is at the bank", "es": "Ella está en el banco", "noun_id": "banco", "type": "auditory"},
            {"en": "You go to the market", "es": "Usted va al mercado", "noun_id": "mercado", "type": "written"},
            {"en": "You (f) are at home", "es": "Tú estás en casa", "noun_id": "casa", "type": "auditory"},
            {"en": "They (f) go to the store", "es": "Ellas van a la tienda", "noun_id": "tienda", "type": "written"},
            {"en": "We (f) are from the city", "es": "Nosotras somos de la ciudad", "noun_id": "ciudad", "type": "auditory"},
            {"en": "You all give money", "es": "Ustedes dan dinero", "noun_id": "dinero", "type": "written"},
            {"en": "He has a dog", "es": "Él tiene un perro", "noun_id": "perro", "type": "auditory"},
            {"en": "We have the book", "es": "Nosotros tenemos el libro", "noun_id": "libro", "type": "written"},
            {"en": "They come from the house", "es": "Ellos vienen de la casa", "noun_id": "casa", "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "ser", "pronoun": "yo"}, {"verb": "ser", "pronoun": "ella"},
            {"verb": "estar", "pronoun": "tú"}, {"verb": "estar", "pronoun": "nosotras"},
            {"verb": "ir", "pronoun": "usted"}, {"verb": "ir", "pronoun": "ellas"},
            {"verb": "dar", "pronoun": "ustedes"}, {"verb": "tener", "pronoun": "él"},
            {"verb": "tener", "pronoun": "nosotros"}, {"verb": "venir", "pronoun": "ellos"},
        ],
        "phase_2_config": {
            "description": "Irregular Present lesson 1: ser, estar, ir, dar, tener, venir",
            "targets": [
                {"verb": "ser", "pronoun": "yo"}, {"verb": "ser", "pronoun": "ella"},
                {"verb": "estar", "pronoun": "tú"}, {"verb": "estar", "pronoun": "nosotras"},
                {"verb": "ir", "pronoun": "usted"}, {"verb": "ir", "pronoun": "ellas"},
                {"verb": "dar", "pronoun": "ustedes"}, {"verb": "tener", "pronoun": "él"},
                {"verb": "tener", "pronoun": "nosotros"}, {"verb": "venir", "pronoun": "ellos"},
            ],
        },
        "opener_en": "Are you from here?",
        "opener_es": "¿Eres de aquí?",
    },
    # --- GL 4: chat companion of `grammar_irregular_present_1` ---
    "grammar_irregular_present_1_chat": {
        "title": "Irregular Present (1/3) — Chat",
        "grammar_level": 4,
        "lesson_number": 1.1,
        "lesson_type": "conjugation",
        "word_workload": ["ser", "estar", "ir", "dar", "tener", "venir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Irregular Present lesson 1: ser, estar, ir, dar, tener, venir', 'targets': [{'verb': 'ser', 'pronoun': 'yo'}, {'verb': 'ser', 'pronoun': 'ella'}, {'verb': 'estar', 'pronoun': 'tú'}, {'verb': 'estar', 'pronoun': 'nosotras'}, {'verb': 'ir', 'pronoun': 'usted'}, {'verb': 'ir', 'pronoun': 'ellas'}, {'verb': 'dar', 'pronoun': 'ustedes'}, {'verb': 'tener', 'pronoun': 'él'}, {'verb': 'tener', 'pronoun': 'nosotros'}, {'verb': 'venir', 'pronoun': 'ellos'}]},
    },
    "grammar_irregular_present_2": {
        "title": "Irregular Present (2/3)",
        "grammar_level": 4,
        "lesson_number": 2,
        "lesson_type": "conjugation",
        "word_workload": ["ser", "estar", "ir", "dar", "tener", "venir"],
        "video_embed_id": "sD2tovQc7pB",
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {"answers": {
            "ser": {"yo": "soy", "tú": "eres", "él": "es", "ella": "es", "usted": "es", "nosotros": "somos", "nosotras": "somos", "ellos": "son", "ellas": "son", "ustedes": "son"},
            "estar": {"yo": "estoy", "tú": "estás", "él": "está", "ella": "está", "usted": "está", "nosotros": "estamos", "nosotras": "estamos", "ellos": "están", "ellas": "están", "ustedes": "están"},
            "ir": {"yo": "voy", "tú": "vas", "él": "va", "ella": "va", "usted": "va", "nosotros": "vamos", "nosotras": "vamos", "ellos": "van", "ellas": "van", "ustedes": "van"},
            "dar": {"yo": "doy", "tú": "das", "él": "da", "ella": "da", "usted": "da", "nosotros": "damos", "nosotras": "damos", "ellos": "dan", "ellas": "dan", "ustedes": "dan"},
            "tener": {"yo": "tengo", "tú": "tienes", "él": "tiene", "ella": "tiene", "usted": "tiene", "nosotros": "tenemos", "nosotras": "tenemos", "ellos": "tienen", "ellas": "tienen", "ustedes": "tienen"},
            "venir": {"yo": "vengo", "tú": "vienes", "él": "viene", "ella": "viene", "usted": "viene", "nosotros": "venimos", "nosotras": "venimos", "ellos": "vienen", "ellas": "vienen", "ustedes": "vienen"},
        }},
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You are from Mexico", "es": "Tú eres de México", "noun_id": None, "type": "written"},
            {"en": "We are from here", "es": "Nosotros somos de aquí", "noun_id": None, "type": "auditory"},
            {"en": "He is at the office", "es": "Él está en la oficina", "noun_id": "oficina", "type": "written"},
            {"en": "You all are in the city", "es": "Ustedes están en la ciudad", "noun_id": "ciudad", "type": "auditory"},
            {"en": "She goes to the market", "es": "Ella va al mercado", "noun_id": "mercado", "type": "written"},
            {"en": "We (f) go to the store", "es": "Nosotras vamos a la tienda", "noun_id": "tienda", "type": "auditory"},
            {"en": "I give the book to her", "es": "Yo doy el libro", "noun_id": "libro", "type": "written"},
            {"en": "They give money", "es": "Ellos dan dinero", "noun_id": "dinero", "type": "auditory"},
            {"en": "You have a car", "es": "Usted tiene un carro", "noun_id": "carro", "type": "written"},
            {"en": "They (f) come from the house", "es": "Ellas vienen de la casa", "noun_id": "casa", "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "ser", "pronoun": "tú"}, {"verb": "ser", "pronoun": "nosotros"},
            {"verb": "estar", "pronoun": "él"}, {"verb": "estar", "pronoun": "ustedes"},
            {"verb": "ir", "pronoun": "ella"}, {"verb": "ir", "pronoun": "nosotras"},
            {"verb": "dar", "pronoun": "yo"}, {"verb": "dar", "pronoun": "ellos"},
            {"verb": "tener", "pronoun": "usted"}, {"verb": "venir", "pronoun": "ellas"},
        ],
        "phase_2_config": {
            "description": "Irregular Present lesson 2: ser, estar, ir, dar, tener, venir",
            "targets": [
                {"verb": "ser", "pronoun": "tú"}, {"verb": "ser", "pronoun": "nosotros"},
                {"verb": "estar", "pronoun": "él"}, {"verb": "estar", "pronoun": "ustedes"},
                {"verb": "ir", "pronoun": "ella"}, {"verb": "ir", "pronoun": "nosotras"},
                {"verb": "dar", "pronoun": "yo"}, {"verb": "dar", "pronoun": "ellos"},
                {"verb": "tener", "pronoun": "usted"}, {"verb": "venir", "pronoun": "ellas"},
            ],
        },
        "opener_en": "Where is your family from?",
        "opener_es": "¿De dónde es tu familia?",
    },
    # --- GL 4: chat companion of `grammar_irregular_present_2` ---
    "grammar_irregular_present_2_chat": {
        "title": "Irregular Present (2/3) — Chat",
        "grammar_level": 4,
        "lesson_number": 2.1,
        "lesson_type": "conjugation",
        "word_workload": ["ser", "estar", "ir", "dar", "tener", "venir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Irregular Present lesson 2: ser, estar, ir, dar, tener, venir', 'targets': [{'verb': 'ser', 'pronoun': 'tú'}, {'verb': 'ser', 'pronoun': 'nosotros'}, {'verb': 'estar', 'pronoun': 'él'}, {'verb': 'estar', 'pronoun': 'ustedes'}, {'verb': 'ir', 'pronoun': 'ella'}, {'verb': 'ir', 'pronoun': 'nosotras'}, {'verb': 'dar', 'pronoun': 'yo'}, {'verb': 'dar', 'pronoun': 'ellos'}, {'verb': 'tener', 'pronoun': 'usted'}, {'verb': 'venir', 'pronoun': 'ellas'}]},
    },
    "grammar_irregular_present_3": {
        "title": "Irregular Present (3/3)",
        "grammar_level": 4,
        "lesson_number": 3,
        "lesson_type": "conjugation",
        "word_workload": ["ser", "estar", "ir", "dar", "tener", "venir"],
        "video_embed_id": "sD2tovQc7pB",
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {"answers": {
            "ser": {"yo": "soy", "tú": "eres", "él": "es", "ella": "es", "usted": "es", "nosotros": "somos", "nosotras": "somos", "ellos": "son", "ellas": "son", "ustedes": "son"},
            "estar": {"yo": "estoy", "tú": "estás", "él": "está", "ella": "está", "usted": "está", "nosotros": "estamos", "nosotras": "estamos", "ellos": "están", "ellas": "están", "ustedes": "están"},
            "ir": {"yo": "voy", "tú": "vas", "él": "va", "ella": "va", "usted": "va", "nosotros": "vamos", "nosotras": "vamos", "ellos": "van", "ellas": "van", "ustedes": "van"},
            "dar": {"yo": "doy", "tú": "das", "él": "da", "ella": "da", "usted": "da", "nosotros": "damos", "nosotras": "damos", "ellos": "dan", "ellas": "dan", "ustedes": "dan"},
            "tener": {"yo": "tengo", "tú": "tienes", "él": "tiene", "ella": "tiene", "usted": "tiene", "nosotros": "tenemos", "nosotras": "tenemos", "ellos": "tienen", "ellas": "tienen", "ustedes": "tienen"},
            "venir": {"yo": "vengo", "tú": "vienes", "él": "viene", "ella": "viene", "usted": "viene", "nosotros": "venimos", "nosotras": "venimos", "ellos": "vienen", "ellas": "vienen", "ustedes": "vienen"},
        }},
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You are a good person", "es": "Usted es una buena persona", "noun_id": None, "type": "written"},
            {"en": "They are at the restaurant", "es": "Ellos están en el restaurante", "noun_id": "restaurante", "type": "auditory"},
            {"en": "I am at the store", "es": "Yo estoy en la tienda", "noun_id": "tienda", "type": "written"},
            {"en": "They (f) are in the city", "es": "Ellas están en la ciudad", "noun_id": "ciudad", "type": "auditory"},
            {"en": "You go to the office", "es": "Tú vas a la oficina", "noun_id": "oficina", "type": "written"},
            {"en": "We go to the park", "es": "Nosotros vamos al parque", "noun_id": "parque", "type": "auditory"},
            {"en": "She gives bread to them", "es": "Ella da pan", "noun_id": "pan", "type": "written"},
            {"en": "We (f) give water", "es": "Nosotras damos agua", "noun_id": "agua", "type": "auditory"},
            {"en": "You all have a dog", "es": "Ustedes tienen un perro", "noun_id": "perro", "type": "written"},
            {"en": "He comes from the park", "es": "Él viene del parque", "noun_id": "parque", "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "ser", "pronoun": "usted"}, {"verb": "ser", "pronoun": "ellos"},
            {"verb": "estar", "pronoun": "yo"}, {"verb": "estar", "pronoun": "ellas"},
            {"verb": "ir", "pronoun": "tú"}, {"verb": "ir", "pronoun": "nosotros"},
            {"verb": "dar", "pronoun": "ella"}, {"verb": "dar", "pronoun": "nosotras"},
            {"verb": "tener", "pronoun": "ustedes"}, {"verb": "venir", "pronoun": "él"},
        ],
        "phase_2_config": {
            "description": "Irregular Present lesson 3: ser, estar, ir, dar, tener, venir",
            "targets": [
                {"verb": "ser", "pronoun": "usted"}, {"verb": "ser", "pronoun": "ellos"},
                {"verb": "estar", "pronoun": "yo"}, {"verb": "estar", "pronoun": "ellas"},
                {"verb": "ir", "pronoun": "tú"}, {"verb": "ir", "pronoun": "nosotros"},
                {"verb": "dar", "pronoun": "ella"}, {"verb": "dar", "pronoun": "nosotras"},
                {"verb": "tener", "pronoun": "ustedes"}, {"verb": "venir", "pronoun": "él"},
            ],
        },
        "opener_en": "Do your neighbors have pets?",
        "opener_es": "¿Tus vecinas tienen mascotas?",
    },
    # --- GL 4: chat companion of `grammar_irregular_present_3` ---
    "grammar_irregular_present_3_chat": {
        "title": "Irregular Present (3/3) — Chat",
        "grammar_level": 4,
        "lesson_number": 3.1,
        "lesson_type": "conjugation",
        "word_workload": ["ser", "estar", "ir", "dar", "tener", "venir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Irregular Present lesson 3: ser, estar, ir, dar, tener, venir', 'targets': [{'verb': 'ser', 'pronoun': 'usted'}, {'verb': 'ser', 'pronoun': 'ellos'}, {'verb': 'estar', 'pronoun': 'yo'}, {'verb': 'estar', 'pronoun': 'ellas'}, {'verb': 'ir', 'pronoun': 'tú'}, {'verb': 'ir', 'pronoun': 'nosotros'}, {'verb': 'dar', 'pronoun': 'ella'}, {'verb': 'dar', 'pronoun': 'nosotras'}, {'verb': 'tener', 'pronoun': 'ustedes'}, {'verb': 'venir', 'pronoun': 'él'}]},
    },
    # --- GL 4.1: Ser vs. Estar ---
    "grammar_ser_estar_rules": {
        "title": "Ser vs. Estar",
        "grammar_level": 4.1,
        "lesson_number": 1,
        "lesson_type": "rule",
        "word_workload": ["ser", "estar"],
        "video_embed_id": None,
        "drill_type": "rule",
        "tense": "present",
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "rule_chart": {'kind': 'comparison', 'title': 'Ser vs. Estar', 'left': {'heading': 'ser', 'items': ['Identity / profession  →  Yo soy profesora', 'Origin / nationality  →  Ella es de Colombia', 'Permanent traits  →  La casa es grande', 'Time / dates  →  Son las tres']}, 'right': {'heading': 'estar', 'items': ['Location  →  Estoy en el mercado', 'Temporary states  →  Él está cansado', 'Conditions / feelings  →  La puerta está abierta', 'Ongoing actions  →  Estoy hablando']}, 'footnote': "Rule of thumb: ser = essence, estar = state. If it'll change in an hour, use estar."},
        "drill_sentences": [
            {"en": "I am a teacher", "es": "Yo soy profesora", "noun_id": None, "type": "written"},
            {"en": "The coffee is hot", "es": "El café está caliente", "noun_id": "café", "type": "auditory"},
            {"en": "She is from Colombia", "es": "Ella es de Colombia", "noun_id": None, "type": "written"},
            {"en": "He is tired", "es": "Él está cansado", "noun_id": None, "type": "auditory"},
            {"en": "The house is big", "es": "La casa es grande", "noun_id": "casa", "type": "written"},
            {"en": "The door is open", "es": "La puerta está abierta", "noun_id": "puerta", "type": "auditory"},
            {"en": "We are at the market", "es": "Nosotros estamos en el mercado", "noun_id": "mercado", "type": "written"},
            {"en": "The water is cold", "es": "El agua está fría", "noun_id": "agua", "type": "auditory"},
            {"en": "You all are students", "es": "Ustedes son estudiantes", "noun_id": None, "type": "written"},
            {"en": "The restaurant is closed", "es": "El restaurante está cerrado", "noun_id": "restaurante", "type": "auditory"},
        ],
        "phase_2_config": {
            "description": "Ser vs. Estar rules: permanent vs. temporary states",
            "targets": [{"word": "ser"}, {"word": "estar"}],
        },
    },
    # --- GL 4.1: chat companion of `grammar_ser_estar_rules` ---
    "grammar_ser_estar_rules_chat": {
        "title": "Ser vs. Estar — Chat",
        "grammar_level": 4.1,
        "lesson_number": 1.1,
        "lesson_type": "rule",
        "word_workload": ["ser", "estar"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Ser vs. Estar rules: permanent vs. temporary states', 'targets': [{'word': 'ser'}, {'word': 'estar'}]},
    },
    # --- GL 4.2: Por vs. Para ---
    "grammar_por_para": {
        "title": "Por vs. Para",
        "grammar_level": 4.2,
        "lesson_number": 1,
        "lesson_type": "rule",
        "word_workload": ["por", "para"],
        "video_embed_id": None,
        "drill_type": "rule",
        "tense": "present",
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "rule_chart": {'kind': 'comparison', 'title': 'Por vs. Para', 'left': {'heading': 'por', 'items': ['Movement through  →  Voy por el parque', 'Cause / reason  →  Trabaja por dinero', "Means / 'by'  →  Viajo por avión", 'Duration  →  Estudié por dos horas', 'Exchange  →  Gracias por el libro']}, 'right': {'heading': 'para', 'items': ['Recipient  →  Esto es para ti', 'Purpose / goal  →  Estudiamos para aprender', 'Deadline  →  Lo necesito para mañana', 'Destination  →  Salgo para Bogotá']}, 'footnote': 'para = forward (purpose, recipient, deadline); por = around / through / because.'},
        "drill_sentences": [
            {"en": "I go by the park", "es": "Yo voy por el parque", "noun_id": "parque", "type": "written"},
            {"en": "This is for you", "es": "Esto es para ti", "noun_id": None, "type": "auditory"},
            {"en": "She works for money", "es": "Ella trabaja por dinero", "noun_id": "dinero", "type": "written"},
            {"en": "We study in order to learn", "es": "Nosotros estudiamos para aprender", "noun_id": None, "type": "auditory"},
            {"en": "He comes by the house", "es": "Él pasa por la casa", "noun_id": "casa", "type": "written"},
            {"en": "The book is for the class", "es": "El libro es para la clase", "noun_id": "libro", "type": "auditory"},
            {"en": "She travels by car", "es": "Ella viaja en carro", "noun_id": "carro", "type": "written"},
            {"en": "I need it for tomorrow", "es": "Lo necesito para mañana", "noun_id": None, "type": "auditory"},
            {"en": "Thank you for the water", "es": "Gracias por el agua", "noun_id": "agua", "type": "written"},
            {"en": "We work to live", "es": "Nosotras trabajamos para vivir", "noun_id": None, "type": "auditory"},
        ],
        "phase_2_config": {
            "description": "Por vs. Para: different uses of each preposition",
            "targets": [{"word": "por"}, {"word": "para"}],
        },
    },
    # --- GL 4.2: chat companion of `grammar_por_para` ---
    "grammar_por_para_chat": {
        "title": "Por vs. Para — Chat",
        "grammar_level": 4.2,
        "lesson_number": 1.1,
        "lesson_type": "rule",
        "word_workload": ["por", "para"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Por vs. Para: different uses of each preposition', 'targets': [{'word': 'por'}, {'word': 'para'}]},
    },
    # --- GL 4.3: Demonstratives ---
    "grammar_demonstratives": {
        "title": "Demonstratives",
        "grammar_level": 4.3,
        "lesson_number": 1,
        "lesson_type": "rule",
        "word_workload": ["este", "esta", "ese", "esa", "aquel", "aquella"],
        "video_embed_id": None,
        "drill_type": "rule",
        "tense": "demonstratives",
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "rule_chart": {'kind': 'table', 'title': 'Demonstratives — this / that / that-yonder', 'headers': ['Distance', 'Masc. sg', 'Fem. sg', 'Masc. pl', 'Fem. pl'], 'rows': [['near (this)', 'este', 'esta', 'estos', 'estas'], ['far from speaker (that)', 'ese', 'esa', 'esos', 'esas'], ['far from both (that yonder)', 'aquel', 'aquella', 'aquellos', 'aquellas']], 'footnote': "Match gender + number with the noun. Use 'aquel' for things visibly distant from both speaker and listener."},
        "drill_sentences": [
            {"en": "This house is big", "es": "Esta casa es grande", "noun_id": "casa", "type": "written"},
            {"en": "That book is interesting", "es": "Ese libro es interesante", "noun_id": "libro", "type": "auditory"},
            {"en": "That city over there is beautiful", "es": "Aquella ciudad es bonita", "noun_id": "ciudad", "type": "written"},
            {"en": "This coffee is hot", "es": "Este café está caliente", "noun_id": "café", "type": "auditory"},
            {"en": "That door is open", "es": "Esa puerta está abierta", "noun_id": "puerta", "type": "written"},
            {"en": "That park over there is nice", "es": "Aquel parque es bonito", "noun_id": "parque", "type": "auditory"},
            {"en": "This water is cold", "es": "Esta agua está fría", "noun_id": "agua", "type": "written"},
            {"en": "That car is expensive", "es": "Ese carro es caro", "noun_id": "carro", "type": "auditory"},
            {"en": "That restaurant over there is good", "es": "Aquel restaurante es bueno", "noun_id": "restaurante", "type": "written"},
            {"en": "This music is great", "es": "Esta música es genial", "noun_id": "música", "type": "auditory"},
        ],
        "phase_2_config": {
            "description": "Demonstratives: este/esta (near), ese/esa (near listener), aquel/aquella (far)",
            "targets": [{"word": w} for w in ["este", "esta", "ese", "esa", "aquel", "aquella"]],
        },
    },
    # --- GL 4.3: chat companion of `grammar_demonstratives` ---
    "grammar_demonstratives_chat": {
        "title": "Demonstratives — Chat",
        "grammar_level": 4.3,
        "lesson_number": 1.1,
        "lesson_type": "rule",
        "word_workload": ["este", "esta", "ese", "esa", "aquel", "aquella"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "demonstratives",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Demonstratives: este/esta (near), ese/esa (near listener), aquel/aquella (far)', 'targets': [{'word': 'este'}, {'word': 'esta'}, {'word': 'ese'}, {'word': 'esa'}, {'word': 'aquel'}, {'word': 'aquella'}]},
    },
    # --- GL 4.4: Possessive Pronouns ---
    "grammar_possessive_pronouns": {
        "title": "Possessive Pronouns",
        "grammar_level": 4.4,
        "lesson_number": 1,
        "lesson_type": "rule",
        "word_workload": ["el mío", "el tuyo", "el suyo", "el nuestro"],
        "video_embed_id": None,
        "drill_type": "rule",
        "tense": "possessive_pronouns",
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "rule_chart": {'kind': 'table', 'title': "Possessive pronouns — 'mine / yours / his …'", 'headers': ['Form', 'Used for'], 'rows': [['el mío / la mía', 'mine'], ['el tuyo / la tuya', 'yours (informal)'], ['el suyo / la suya', 'his / hers / yours (formal) / theirs'], ['el nuestro / la nuestra', 'ours']], 'footnote': 'Stand-alone — replaces the noun. Agree in gender and number with the thing owned. Plural forms add -s (los míos, las nuestras).'},
        "drill_sentences": [
            {"en": "The book is mine", "es": "El libro es mío", "noun_id": "libro", "type": "written"},
            {"en": "The house is yours", "es": "La casa es tuya", "noun_id": "casa", "type": "auditory"},
            {"en": "The car is his", "es": "El carro es suyo", "noun_id": "carro", "type": "written"},
            {"en": "The money is ours", "es": "El dinero es nuestro", "noun_id": "dinero", "type": "auditory"},
            {"en": "The bag is mine", "es": "La bolsa es mía", "noun_id": None, "type": "written"},
            {"en": "The coffee is yours", "es": "El café es tuyo", "noun_id": "café", "type": "auditory"},
            {"en": "The dog is hers", "es": "El perro es suyo", "noun_id": "perro", "type": "written"},
            {"en": "The house is ours", "es": "La casa es nuestra", "noun_id": "casa", "type": "auditory"},
            {"en": "The water is mine", "es": "El agua es mía", "noun_id": "agua", "type": "written"},
            {"en": "The book is theirs", "es": "El libro es suyo", "noun_id": "libro", "type": "auditory"},
        ],
        "phase_2_config": {
            "description": "Possessive pronouns: mío/mía, tuyo/tuya, suyo/suya, nuestro/nuestra",
            "targets": [{"word": w} for w in ["mío", "mía", "tuyo", "tuya", "suyo", "suya", "nuestro", "nuestra"]],
        },
    },
    # --- GL 4.4: chat companion of `grammar_possessive_pronouns` ---
    "grammar_possessive_pronouns_chat": {
        "title": "Possessive Pronouns — Chat",
        "grammar_level": 4.4,
        "lesson_number": 1.1,
        "lesson_type": "rule",
        "word_workload": ["el mío", "el tuyo", "el suyo", "el nuestro"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "possessive_pronouns",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Possessive pronouns: mío/mía, tuyo/tuya, suyo/suya, nuestro/nuestra', 'targets': [{'word': 'mío'}, {'word': 'mía'}, {'word': 'tuyo'}, {'word': 'tuya'}, {'word': 'suyo'}, {'word': 'suya'}, {'word': 'nuestro'}, {'word': 'nuestra'}]},
    },
    # --- GL 4.5: Irregular Present II — 4 lessons (L1&3: hacer,poner,salir,decir / L2&4: oír,caer,traer,valer) ---
    "grammar_irregular_present_ii_1": {
        "title": "Irregular Present II (1/4)",
        "grammar_level": 4.5,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ["hacer", "poner", "salir", "decir"],
        "video_embed_id": "tPXOw1Rz82y",
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {
            "answers": {
                "hacer": {
                    "yo": "hago", "tú": "haces", "él": "hace", "ella": "hace",
                    "usted": "hace", "nosotros": "hacemos", "nosotras": "hacemos",
                    "ellos": "hacen", "ellas": "hacen", "ustedes": "hacen",
                },
                "poner": {
                    "yo": "pongo", "tú": "pones", "él": "pone", "ella": "pone",
                    "usted": "pone", "nosotros": "ponemos", "nosotras": "ponemos",
                    "ellos": "ponen", "ellas": "ponen", "ustedes": "ponen",
                },
                "salir": {
                    "yo": "salgo", "tú": "sales", "él": "sale", "ella": "sale",
                    "usted": "sale", "nosotros": "salimos", "nosotras": "salimos",
                    "ellos": "salen", "ellas": "salen", "ustedes": "salen",
                },
                "decir": {
                    "yo": "digo", "tú": "dices", "él": "dice", "ella": "dice",
                    "usted": "dice", "nosotros": "decimos", "nosotras": "decimos",
                    "ellos": "dicen", "ellas": "dicen", "ustedes": "dicen",
                },
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I make the food at home", "es": "Yo hago la comida en casa", "noun_id": "comida", "type": "written"},
            {"en": "She makes the coffee", "es": "Ella hace el café", "noun_id": "café", "type": "auditory"},
            {"en": "You all do the work", "es": "Ustedes hacen el trabajo", "noun_id": "trabajo", "type": "written"},
            {"en": "You put the book here", "es": "Tú pones el libro aquí", "noun_id": "libro", "type": "auditory"},
            {"en": "We (f) put the water here", "es": "Nosotras ponemos el agua aquí", "noun_id": "agua", "type": "written"},
            {"en": "He leaves the house", "es": "Él sale de la casa", "noun_id": "casa", "type": "auditory"},
            {"en": "They leave the office", "es": "Ellos salen de la oficina", "noun_id": "oficina", "type": "written"},
            {"en": "You say the truth", "es": "Usted dice la verdad", "noun_id": None, "type": "auditory"},
            {"en": "We say hello every day", "es": "Nosotros decimos hola cada día", "noun_id": None, "type": "written"},
            {"en": "They (f) say the name", "es": "Ellas dicen el nombre", "noun_id": None, "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "hacer", "pronoun": "yo"}, {"verb": "hacer", "pronoun": "ella"},
            {"verb": "hacer", "pronoun": "ustedes"}, {"verb": "poner", "pronoun": "tú"},
            {"verb": "poner", "pronoun": "nosotras"}, {"verb": "salir", "pronoun": "él"},
            {"verb": "salir", "pronoun": "ellos"}, {"verb": "decir", "pronoun": "usted"},
            {"verb": "decir", "pronoun": "nosotros"}, {"verb": "decir", "pronoun": "ellas"},
        ],
        "phase_2_config": {
            "description": "Irregular Present II lesson 1: hacer, poner, salir, decir",
            "targets": [
                {"verb": "hacer", "pronoun": "yo"}, {"verb": "hacer", "pronoun": "ella"},
                {"verb": "hacer", "pronoun": "ustedes"}, {"verb": "poner", "pronoun": "tú"},
                {"verb": "poner", "pronoun": "nosotras"}, {"verb": "salir", "pronoun": "él"},
                {"verb": "salir", "pronoun": "ellos"}, {"verb": "decir", "pronoun": "usted"},
                {"verb": "decir", "pronoun": "nosotros"}, {"verb": "decir", "pronoun": "ellas"},
            ],
        },
        "opener_en": "What do you do on weekends?",
        "opener_es": "¿Qué haces los fines de semana?",
    },
    # --- GL 4.5: chat companion of `grammar_irregular_present_ii_1` ---
    "grammar_irregular_present_ii_1_chat": {
        "title": "Irregular Present II (1/4) — Chat",
        "grammar_level": 4.5,
        "lesson_number": 1.1,
        "lesson_type": "conjugation",
        "word_workload": ["hacer", "poner", "salir", "decir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Irregular Present II lesson 1: hacer, poner, salir, decir', 'targets': [{'verb': 'hacer', 'pronoun': 'yo'}, {'verb': 'hacer', 'pronoun': 'ella'}, {'verb': 'hacer', 'pronoun': 'ustedes'}, {'verb': 'poner', 'pronoun': 'tú'}, {'verb': 'poner', 'pronoun': 'nosotras'}, {'verb': 'salir', 'pronoun': 'él'}, {'verb': 'salir', 'pronoun': 'ellos'}, {'verb': 'decir', 'pronoun': 'usted'}, {'verb': 'decir', 'pronoun': 'nosotros'}, {'verb': 'decir', 'pronoun': 'ellas'}]},
    },
    "grammar_irregular_present_ii_2": {
        "title": "Irregular Present II (2/4)",
        "grammar_level": 4.5,
        "lesson_number": 2,
        "lesson_type": "conjugation",
        "word_workload": ["oír", "caer", "traer", "valer"],
        "video_embed_id": "tPXOw1Rz82y",
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {
            "answers": {
                "oír": {
                    "yo": "oigo", "tú": "oyes", "él": "oye", "ella": "oye",
                    "usted": "oye", "nosotros": "oímos", "nosotras": "oímos",
                    "ellos": "oyen", "ellas": "oyen", "ustedes": "oyen",
                },
                "caer": {
                    "yo": "caigo", "tú": "caes", "él": "cae", "ella": "cae",
                    "usted": "cae", "nosotros": "caemos", "nosotras": "caemos",
                    "ellos": "caen", "ellas": "caen", "ustedes": "caen",
                },
                "traer": {
                    "yo": "traigo", "tú": "traes", "él": "trae", "ella": "trae",
                    "usted": "trae", "nosotros": "traemos", "nosotras": "traemos",
                    "ellos": "traen", "ellas": "traen", "ustedes": "traen",
                },
                "valer": {
                    "yo": "valgo", "tú": "vales", "él": "vale", "ella": "vale",
                    "usted": "vale", "nosotros": "valemos", "nosotras": "valemos",
                    "ellos": "valen", "ellas": "valen", "ustedes": "valen",
                },
            },
        },
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I hear the music", "es": "Yo oigo la música", "noun_id": None, "type": "written"},
            {"en": "We hear the dog at night", "es": "Nosotros oímos el perro de noche", "noun_id": "perro", "type": "auditory"},
            {"en": "They (f) hear the door", "es": "Ellas oyen la puerta", "noun_id": "puerta", "type": "written"},
            {"en": "You fall in the park", "es": "Tú caes en el parque", "noun_id": "parque", "type": "auditory"},
            {"en": "She falls in the house", "es": "Ella cae en la casa", "noun_id": "casa", "type": "written"},
            {"en": "He brings the food", "es": "Él trae la comida", "noun_id": "comida", "type": "auditory"},
            {"en": "You all bring water", "es": "Ustedes traen agua", "noun_id": "agua", "type": "written"},
            {"en": "It is worth the money", "es": "Usted vale el dinero", "noun_id": "dinero", "type": "auditory"},
            {"en": "We (f) are worth a lot", "es": "Nosotras valemos mucho", "noun_id": None, "type": "written"},
            {"en": "They cost a lot", "es": "Ellos valen mucho", "noun_id": None, "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "oír", "pronoun": "yo"}, {"verb": "oír", "pronoun": "nosotros"},
            {"verb": "oír", "pronoun": "ellas"}, {"verb": "caer", "pronoun": "tú"},
            {"verb": "caer", "pronoun": "ella"}, {"verb": "traer", "pronoun": "él"},
            {"verb": "traer", "pronoun": "ustedes"}, {"verb": "valer", "pronoun": "usted"},
            {"verb": "valer", "pronoun": "nosotras"}, {"verb": "valer", "pronoun": "ellos"},
        ],
        "phase_2_config": {
            "description": "Irregular Present II lesson 2: oír, caer, traer, valer",
            "targets": [
                {"verb": "oír", "pronoun": "yo"}, {"verb": "oír", "pronoun": "nosotros"},
                {"verb": "oír", "pronoun": "ellas"}, {"verb": "caer", "pronoun": "tú"},
                {"verb": "caer", "pronoun": "ella"}, {"verb": "traer", "pronoun": "él"},
                {"verb": "traer", "pronoun": "ustedes"}, {"verb": "valer", "pronoun": "usted"},
                {"verb": "valer", "pronoun": "nosotras"}, {"verb": "valer", "pronoun": "ellos"},
            ],
        },
        "opener_en": "Do you hear the noise outside?",
        "opener_es": "¿Oyes el ruido afuera?",
    },
    # --- GL 4.5: chat companion of `grammar_irregular_present_ii_2` ---
    "grammar_irregular_present_ii_2_chat": {
        "title": "Irregular Present II (2/4) — Chat",
        "grammar_level": 4.5,
        "lesson_number": 2.1,
        "lesson_type": "conjugation",
        "word_workload": ["oír", "caer", "traer", "valer"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Irregular Present II lesson 2: oír, caer, traer, valer', 'targets': [{'verb': 'oír', 'pronoun': 'yo'}, {'verb': 'oír', 'pronoun': 'nosotros'}, {'verb': 'oír', 'pronoun': 'ellas'}, {'verb': 'caer', 'pronoun': 'tú'}, {'verb': 'caer', 'pronoun': 'ella'}, {'verb': 'traer', 'pronoun': 'él'}, {'verb': 'traer', 'pronoun': 'ustedes'}, {'verb': 'valer', 'pronoun': 'usted'}, {'verb': 'valer', 'pronoun': 'nosotras'}, {'verb': 'valer', 'pronoun': 'ellos'}]},
    },
    "grammar_irregular_present_ii_3": {
        "title": "Irregular Present II (3/4)",
        "grammar_level": 4.5,
        "lesson_number": 3,
        "lesson_type": "conjugation",
        "word_workload": ["hacer", "poner", "salir", "decir"],
        "video_embed_id": "tPXOw1Rz82y",
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {
            "answers": {
                "hacer": {
                    "yo": "hago", "tú": "haces", "él": "hace", "ella": "hace",
                    "usted": "hace", "nosotros": "hacemos", "nosotras": "hacemos",
                    "ellos": "hacen", "ellas": "hacen", "ustedes": "hacen",
                },
                "poner": {
                    "yo": "pongo", "tú": "pones", "él": "pone", "ella": "pone",
                    "usted": "pone", "nosotros": "ponemos", "nosotras": "ponemos",
                    "ellos": "ponen", "ellas": "ponen", "ustedes": "ponen",
                },
                "salir": {
                    "yo": "salgo", "tú": "sales", "él": "sale", "ella": "sale",
                    "usted": "sale", "nosotros": "salimos", "nosotras": "salimos",
                    "ellos": "salen", "ellas": "salen", "ustedes": "salen",
                },
                "decir": {
                    "yo": "digo", "tú": "dices", "él": "dice", "ella": "dice",
                    "usted": "dice", "nosotros": "decimos", "nosotras": "decimos",
                    "ellos": "dicen", "ellas": "dicen", "ustedes": "dicen",
                },
            },
        },
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You make breakfast every day", "es": "Tú haces el desayuno cada día", "noun_id": None, "type": "written"},
            {"en": "We do the work together", "es": "Nosotros hacemos el trabajo juntos", "noun_id": "trabajo", "type": "auditory"},
            {"en": "You put the book here", "es": "Usted pone el libro aquí", "noun_id": "libro", "type": "written"},
            {"en": "They (f) put the water here", "es": "Ellas ponen el agua aquí", "noun_id": "agua", "type": "auditory"},
            {"en": "I leave the house", "es": "Yo salgo de la casa", "noun_id": "casa", "type": "written"},
            {"en": "We (f) leave early", "es": "Nosotras salimos temprano", "noun_id": None, "type": "auditory"},
            {"en": "You all leave the office", "es": "Ustedes salen de la oficina", "noun_id": "oficina", "type": "written"},
            {"en": "He says hello in Spanish", "es": "Él dice hola en español", "noun_id": None, "type": "auditory"},
            {"en": "She says the truth", "es": "Ella dice la verdad", "noun_id": None, "type": "written"},
            {"en": "They say the name", "es": "Ellos dicen el nombre", "noun_id": None, "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "hacer", "pronoun": "tú"}, {"verb": "hacer", "pronoun": "nosotros"},
            {"verb": "poner", "pronoun": "usted"}, {"verb": "poner", "pronoun": "ellas"},
            {"verb": "salir", "pronoun": "yo"}, {"verb": "salir", "pronoun": "nosotras"},
            {"verb": "salir", "pronoun": "ustedes"}, {"verb": "decir", "pronoun": "él"},
            {"verb": "decir", "pronoun": "ella"}, {"verb": "decir", "pronoun": "ellos"},
        ],
        "phase_2_config": {
            "description": "Irregular Present II lesson 3: hacer, poner, salir, decir",
            "targets": [
                {"verb": "hacer", "pronoun": "tú"}, {"verb": "hacer", "pronoun": "nosotros"},
                {"verb": "poner", "pronoun": "usted"}, {"verb": "poner", "pronoun": "ellas"},
                {"verb": "salir", "pronoun": "yo"}, {"verb": "salir", "pronoun": "nosotras"},
                {"verb": "salir", "pronoun": "ustedes"}, {"verb": "decir", "pronoun": "él"},
                {"verb": "decir", "pronoun": "ella"}, {"verb": "decir", "pronoun": "ellos"},
            ],
        },
        "opener_en": "What does your friend do for work?",
        "opener_es": "¿Qué hace tu amiga?",
    },
    # --- GL 4.5: chat companion of `grammar_irregular_present_ii_3` ---
    "grammar_irregular_present_ii_3_chat": {
        "title": "Irregular Present II (3/4) — Chat",
        "grammar_level": 4.5,
        "lesson_number": 3.1,
        "lesson_type": "conjugation",
        "word_workload": ["hacer", "poner", "salir", "decir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Irregular Present II lesson 3: hacer, poner, salir, decir', 'targets': [{'verb': 'hacer', 'pronoun': 'tú'}, {'verb': 'hacer', 'pronoun': 'nosotros'}, {'verb': 'poner', 'pronoun': 'usted'}, {'verb': 'poner', 'pronoun': 'ellas'}, {'verb': 'salir', 'pronoun': 'yo'}, {'verb': 'salir', 'pronoun': 'nosotras'}, {'verb': 'salir', 'pronoun': 'ustedes'}, {'verb': 'decir', 'pronoun': 'él'}, {'verb': 'decir', 'pronoun': 'ella'}, {'verb': 'decir', 'pronoun': 'ellos'}]},
    },
    "grammar_irregular_present_ii_4": {
        "title": "Irregular Present II (4/4)",
        "grammar_level": 4.5,
        "lesson_number": 4,
        "lesson_type": "conjugation",
        "word_workload": ["oír", "caer", "traer", "valer"],
        "video_embed_id": "tPXOw1Rz82y",
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {
            "answers": {
                "oír": {
                    "yo": "oigo", "tú": "oyes", "él": "oye", "ella": "oye",
                    "usted": "oye", "nosotros": "oímos", "nosotras": "oímos",
                    "ellos": "oyen", "ellas": "oyen", "ustedes": "oyen",
                },
                "caer": {
                    "yo": "caigo", "tú": "caes", "él": "cae", "ella": "cae",
                    "usted": "cae", "nosotros": "caemos", "nosotras": "caemos",
                    "ellos": "caen", "ellas": "caen", "ustedes": "caen",
                },
                "traer": {
                    "yo": "traigo", "tú": "traes", "él": "trae", "ella": "trae",
                    "usted": "trae", "nosotros": "traemos", "nosotras": "traemos",
                    "ellos": "traen", "ellas": "traen", "ustedes": "traen",
                },
                "valer": {
                    "yo": "valgo", "tú": "vales", "él": "vale", "ella": "vale",
                    "usted": "vale", "nosotros": "valemos", "nosotras": "valemos",
                    "ellos": "valen", "ellas": "valen", "ustedes": "valen",
                },
            },
        },
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You hear the music", "es": "Tú oyes la música", "noun_id": "música", "type": "written"},
            {"en": "You hear the dog", "es": "Usted oye el perro", "noun_id": "perro", "type": "auditory"},
            {"en": "I fall near the door", "es": "Yo caigo cerca de la puerta", "noun_id": "puerta", "type": "written"},
            {"en": "We (f) fall in the street", "es": "Nosotras caemos en la calle", "noun_id": None, "type": "auditory"},
            {"en": "They fall at the park", "es": "Ellos caen en el parque", "noun_id": "parque", "type": "written"},
            {"en": "She brings the food from the market", "es": "Ella trae la comida del mercado", "noun_id": "comida", "type": "auditory"},
            {"en": "We bring water", "es": "Nosotros traemos agua", "noun_id": "agua", "type": "written"},
            {"en": "It is worth the price", "es": "Él vale el precio", "noun_id": None, "type": "auditory"},
            {"en": "They (f) are worth a lot", "es": "Ellas valen mucho", "noun_id": None, "type": "written"},
            {"en": "You all are worth the effort", "es": "Ustedes valen el esfuerzo", "noun_id": None, "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "oír", "pronoun": "tú"}, {"verb": "oír", "pronoun": "usted"},
            {"verb": "caer", "pronoun": "yo"}, {"verb": "caer", "pronoun": "nosotras"},
            {"verb": "caer", "pronoun": "ellos"}, {"verb": "traer", "pronoun": "ella"},
            {"verb": "traer", "pronoun": "nosotros"}, {"verb": "valer", "pronoun": "él"},
            {"verb": "valer", "pronoun": "ellas"}, {"verb": "valer", "pronoun": "ustedes"},
        ],
        "phase_2_config": {
            "description": "Irregular Present II lesson 4: oír, caer, traer, valer",
            "targets": [
                {"verb": "oír", "pronoun": "tú"}, {"verb": "oír", "pronoun": "usted"},
                {"verb": "caer", "pronoun": "yo"}, {"verb": "caer", "pronoun": "nosotras"},
                {"verb": "caer", "pronoun": "ellos"}, {"verb": "traer", "pronoun": "ella"},
                {"verb": "traer", "pronoun": "nosotros"}, {"verb": "valer", "pronoun": "él"},
                {"verb": "valer", "pronoun": "ellas"}, {"verb": "valer", "pronoun": "ustedes"},
            ],
        },
        "opener_en": "Does your neighbor hear the dog?",
        "opener_es": "¿Tu vecina oye al perro?",
    },
    # --- GL 4.5: chat companion of `grammar_irregular_present_ii_4` ---
    "grammar_irregular_present_ii_4_chat": {
        "title": "Irregular Present II (4/4) — Chat",
        "grammar_level": 4.5,
        "lesson_number": 4.1,
        "lesson_type": "conjugation",
        "word_workload": ["oír", "caer", "traer", "valer"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Irregular Present II lesson 4: oír, caer, traer, valer', 'targets': [{'verb': 'oír', 'pronoun': 'tú'}, {'verb': 'oír', 'pronoun': 'usted'}, {'verb': 'caer', 'pronoun': 'yo'}, {'verb': 'caer', 'pronoun': 'nosotras'}, {'verb': 'caer', 'pronoun': 'ellos'}, {'verb': 'traer', 'pronoun': 'ella'}, {'verb': 'traer', 'pronoun': 'nosotros'}, {'verb': 'valer', 'pronoun': 'él'}, {'verb': 'valer', 'pronoun': 'ellas'}, {'verb': 'valer', 'pronoun': 'ustedes'}]},
    },
    # --- GL 5: Spelling Changes — 4 lessons (L1&3: conocer,producir,construir,conseguir / L2&4: recoger,dirigir,convencer,continuar) ---
    "grammar_spelling_changes_1": {
        "title": "Spelling Changes (1/4)",
        "grammar_level": 5,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ["conocer", "producir", "construir", "conseguir"],
        "video_embed_id": "dYyywu1hOVp",
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {
            "answers": {
                "conocer": {
                    "yo": "conozco", "tú": "conoces", "él": "conoce", "ella": "conoce",
                    "usted": "conoce", "nosotros": "conocemos", "nosotras": "conocemos",
                    "ellos": "conocen", "ellas": "conocen", "ustedes": "conocen",
                },
                "producir": {
                    "yo": "produzco", "tú": "produces", "él": "produce", "ella": "produce",
                    "usted": "produce", "nosotros": "producimos", "nosotras": "producimos",
                    "ellos": "producen", "ellas": "producen", "ustedes": "producen",
                },
                "construir": {
                    "yo": "construyo", "tú": "construyes", "él": "construye", "ella": "construye",
                    "usted": "construye", "nosotros": "construimos", "nosotras": "construimos",
                    "ellos": "construyen", "ellas": "construyen", "ustedes": "construyen",
                },
                "conseguir": {
                    "yo": "consigo", "tú": "consigues", "él": "consigue", "ella": "consigue",
                    "usted": "consigue", "nosotros": "conseguimos", "nosotras": "conseguimos",
                    "ellos": "consiguen", "ellas": "consiguen", "ustedes": "consiguen",
                },
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I know a good restaurant", "es": "Yo conozco un buen restaurante", "noun_id": "restaurante", "type": "written"},
            {"en": "She knows the city well", "es": "Ella conoce la ciudad bien", "noun_id": "ciudad", "type": "auditory"},
            {"en": "You all know the area", "es": "Ustedes conocen la zona", "noun_id": None, "type": "written"},
            {"en": "You produce food every day", "es": "Tú produces comida cada día", "noun_id": "comida", "type": "auditory"},
            {"en": "We (f) produce good work", "es": "Nosotras producimos buen trabajo", "noun_id": "trabajo", "type": "written"},
            {"en": "He builds a house", "es": "Él construye una casa", "noun_id": "casa", "type": "auditory"},
            {"en": "They build in the city", "es": "Ellos construyen en la ciudad", "noun_id": "ciudad", "type": "written"},
            {"en": "You get the book", "es": "Usted consigue el libro", "noun_id": "libro", "type": "auditory"},
            {"en": "We get the money", "es": "Nosotros conseguimos el dinero", "noun_id": "dinero", "type": "written"},
            {"en": "They (f) get a good job", "es": "Ellas consiguen un buen trabajo", "noun_id": "trabajo", "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "conocer", "pronoun": "yo"}, {"verb": "conocer", "pronoun": "ella"},
            {"verb": "conocer", "pronoun": "ustedes"}, {"verb": "producir", "pronoun": "tú"},
            {"verb": "producir", "pronoun": "nosotras"}, {"verb": "construir", "pronoun": "él"},
            {"verb": "construir", "pronoun": "ellos"}, {"verb": "conseguir", "pronoun": "usted"},
            {"verb": "conseguir", "pronoun": "nosotros"}, {"verb": "conseguir", "pronoun": "ellas"},
        ],
        "phase_2_config": {
            "description": "Spelling Changes lesson 1: conocer, producir, construir, conseguir",
            "targets": [
                {"verb": "conocer", "pronoun": "yo"}, {"verb": "conocer", "pronoun": "ella"},
                {"verb": "conocer", "pronoun": "ustedes"}, {"verb": "producir", "pronoun": "tú"},
                {"verb": "producir", "pronoun": "nosotras"}, {"verb": "construir", "pronoun": "él"},
                {"verb": "construir", "pronoun": "ellos"}, {"verb": "conseguir", "pronoun": "usted"},
                {"verb": "conseguir", "pronoun": "nosotros"}, {"verb": "conseguir", "pronoun": "ellas"},
            ],
        },
        "opener_en": "Do you know a good restaurant?",
        "opener_es": "¿Conoces un buen restaurante?",
    },
    # --- GL 5: chat companion of `grammar_spelling_changes_1` ---
    "grammar_spelling_changes_1_chat": {
        "title": "Spelling Changes (1/4) — Chat",
        "grammar_level": 5,
        "lesson_number": 1.1,
        "lesson_type": "conjugation",
        "word_workload": ["conocer", "producir", "construir", "conseguir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Spelling Changes lesson 1: conocer, producir, construir, conseguir', 'targets': [{'verb': 'conocer', 'pronoun': 'yo'}, {'verb': 'conocer', 'pronoun': 'ella'}, {'verb': 'conocer', 'pronoun': 'ustedes'}, {'verb': 'producir', 'pronoun': 'tú'}, {'verb': 'producir', 'pronoun': 'nosotras'}, {'verb': 'construir', 'pronoun': 'él'}, {'verb': 'construir', 'pronoun': 'ellos'}, {'verb': 'conseguir', 'pronoun': 'usted'}, {'verb': 'conseguir', 'pronoun': 'nosotros'}, {'verb': 'conseguir', 'pronoun': 'ellas'}]},
    },
    "grammar_spelling_changes_2": {
        "title": "Spelling Changes (2/4)",
        "grammar_level": 5,
        "lesson_number": 2,
        "lesson_type": "conjugation",
        "word_workload": ["recoger", "dirigir", "convencer", "continuar"],
        "video_embed_id": "dYyywu1hOVp",
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {
            "answers": {
                "recoger": {
                    "yo": "recojo", "tú": "recoges", "él": "recoge", "ella": "recoge",
                    "usted": "recoge", "nosotros": "recogemos", "nosotras": "recogemos",
                    "ellos": "recogen", "ellas": "recogen", "ustedes": "recogen",
                },
                "dirigir": {
                    "yo": "dirijo", "tú": "diriges", "él": "dirige", "ella": "dirige",
                    "usted": "dirige", "nosotros": "dirigimos", "nosotras": "dirigimos",
                    "ellos": "dirigen", "ellas": "dirigen", "ustedes": "dirigen",
                },
                "convencer": {
                    "yo": "convenzo", "tú": "convences", "él": "convence", "ella": "convence",
                    "usted": "convence", "nosotros": "convencemos", "nosotras": "convencemos",
                    "ellos": "convencen", "ellas": "convencen", "ustedes": "convencen",
                },
                "continuar": {
                    "yo": "continúo", "tú": "continúas", "él": "continúa", "ella": "continúa",
                    "usted": "continúa", "nosotros": "continuamos", "nosotras": "continuamos",
                    "ellos": "continúan", "ellas": "continúan", "ustedes": "continúan",
                },
            },
        },
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I pick up the food", "es": "Yo recojo la comida", "noun_id": "comida", "type": "written"},
            {"en": "We pick up the bags", "es": "Nosotros recogemos las bolsas", "noun_id": "bolsa", "type": "auditory"},
            {"en": "They (f) pick up the books", "es": "Ellas recogen los libros", "noun_id": "libro", "type": "written"},
            {"en": "You direct the work", "es": "Tú diriges el trabajo", "noun_id": "trabajo", "type": "auditory"},
            {"en": "She directs the team", "es": "Ella dirige el equipo", "noun_id": None, "type": "written"},
            {"en": "He convinces the client", "es": "Él convence al cliente", "noun_id": None, "type": "auditory"},
            {"en": "You all convince the family", "es": "Ustedes convencen a la familia", "noun_id": None, "type": "written"},
            {"en": "You continue working every day", "es": "Usted continúa trabajando cada día", "noun_id": None, "type": "auditory"},
            {"en": "We (f) continue with the plan", "es": "Nosotras continuamos con el plan", "noun_id": None, "type": "written"},
            {"en": "They continue in the city", "es": "Ellos continúan en la ciudad", "noun_id": "ciudad", "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "recoger", "pronoun": "yo"}, {"verb": "recoger", "pronoun": "nosotros"},
            {"verb": "recoger", "pronoun": "ellas"}, {"verb": "dirigir", "pronoun": "tú"},
            {"verb": "dirigir", "pronoun": "ella"}, {"verb": "convencer", "pronoun": "él"},
            {"verb": "convencer", "pronoun": "ustedes"}, {"verb": "continuar", "pronoun": "usted"},
            {"verb": "continuar", "pronoun": "nosotras"}, {"verb": "continuar", "pronoun": "ellos"},
        ],
        "phase_2_config": {
            "description": "Spelling Changes lesson 2: recoger, dirigir, convencer, continuar",
            "targets": [
                {"verb": "recoger", "pronoun": "yo"}, {"verb": "recoger", "pronoun": "nosotros"},
                {"verb": "recoger", "pronoun": "ellas"}, {"verb": "dirigir", "pronoun": "tú"},
                {"verb": "dirigir", "pronoun": "ella"}, {"verb": "convencer", "pronoun": "él"},
                {"verb": "convencer", "pronoun": "ustedes"}, {"verb": "continuar", "pronoun": "usted"},
                {"verb": "continuar", "pronoun": "nosotras"}, {"verb": "continuar", "pronoun": "ellos"},
            ],
        },
        "opener_en": "Where do you pick up your kids?",
        "opener_es": "¿Dónde recoges a tus hijos?",
    },
    # --- GL 5: chat companion of `grammar_spelling_changes_2` ---
    "grammar_spelling_changes_2_chat": {
        "title": "Spelling Changes (2/4) — Chat",
        "grammar_level": 5,
        "lesson_number": 2.1,
        "lesson_type": "conjugation",
        "word_workload": ["recoger", "dirigir", "convencer", "continuar"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Spelling Changes lesson 2: recoger, dirigir, convencer, continuar', 'targets': [{'verb': 'recoger', 'pronoun': 'yo'}, {'verb': 'recoger', 'pronoun': 'nosotros'}, {'verb': 'recoger', 'pronoun': 'ellas'}, {'verb': 'dirigir', 'pronoun': 'tú'}, {'verb': 'dirigir', 'pronoun': 'ella'}, {'verb': 'convencer', 'pronoun': 'él'}, {'verb': 'convencer', 'pronoun': 'ustedes'}, {'verb': 'continuar', 'pronoun': 'usted'}, {'verb': 'continuar', 'pronoun': 'nosotras'}, {'verb': 'continuar', 'pronoun': 'ellos'}]},
    },
    "grammar_spelling_changes_3": {
        "title": "Spelling Changes (3/4)",
        "grammar_level": 5,
        "lesson_number": 3,
        "lesson_type": "conjugation",
        "word_workload": ["conocer", "producir", "construir", "conseguir"],
        "video_embed_id": "dYyywu1hOVp",
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {
            "answers": {
                "conocer": {
                    "yo": "conozco", "tú": "conoces", "él": "conoce", "ella": "conoce",
                    "usted": "conoce", "nosotros": "conocemos", "nosotras": "conocemos",
                    "ellos": "conocen", "ellas": "conocen", "ustedes": "conocen",
                },
                "producir": {
                    "yo": "produzco", "tú": "produces", "él": "produce", "ella": "produce",
                    "usted": "produce", "nosotros": "producimos", "nosotras": "producimos",
                    "ellos": "producen", "ellas": "producen", "ustedes": "producen",
                },
                "construir": {
                    "yo": "construyo", "tú": "construyes", "él": "construye", "ella": "construye",
                    "usted": "construye", "nosotros": "construimos", "nosotras": "construimos",
                    "ellos": "construyen", "ellas": "construyen", "ustedes": "construyen",
                },
                "conseguir": {
                    "yo": "consigo", "tú": "consigues", "él": "consigue", "ella": "consigue",
                    "usted": "consigue", "nosotros": "conseguimos", "nosotras": "conseguimos",
                    "ellos": "consiguen", "ellas": "consiguen", "ustedes": "consiguen",
                },
            },
        },
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You know a good park", "es": "Tú conoces un buen parque", "noun_id": "parque", "type": "written"},
            {"en": "We know this neighborhood", "es": "Nosotros conocemos este barrio", "noun_id": None, "type": "auditory"},
            {"en": "You produce good results", "es": "Usted produce buenos resultados", "noun_id": None, "type": "written"},
            {"en": "They (f) produce the best food", "es": "Ellas producen la mejor comida", "noun_id": "comida", "type": "auditory"},
            {"en": "I build a house", "es": "Yo construyo una casa", "noun_id": "casa", "type": "written"},
            {"en": "We (f) build near the market", "es": "Nosotras construimos cerca del mercado", "noun_id": "mercado", "type": "auditory"},
            {"en": "You all build the office", "es": "Ustedes construyen la oficina", "noun_id": "oficina", "type": "written"},
            {"en": "He gets the job", "es": "Él consigue el trabajo", "noun_id": "trabajo", "type": "auditory"},
            {"en": "She gets the book", "es": "Ella consigue el libro", "noun_id": "libro", "type": "written"},
            {"en": "They get the money", "es": "Ellos consiguen el dinero", "noun_id": "dinero", "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "conocer", "pronoun": "tú"}, {"verb": "conocer", "pronoun": "nosotros"},
            {"verb": "producir", "pronoun": "usted"}, {"verb": "producir", "pronoun": "ellas"},
            {"verb": "construir", "pronoun": "yo"}, {"verb": "construir", "pronoun": "nosotras"},
            {"verb": "construir", "pronoun": "ustedes"}, {"verb": "conseguir", "pronoun": "él"},
            {"verb": "conseguir", "pronoun": "ella"}, {"verb": "conseguir", "pronoun": "ellos"},
        ],
        "phase_2_config": {
            "description": "Spelling Changes lesson 3: conocer, producir, construir, conseguir",
            "targets": [
                {"verb": "conocer", "pronoun": "tú"}, {"verb": "conocer", "pronoun": "nosotros"},
                {"verb": "producir", "pronoun": "usted"}, {"verb": "producir", "pronoun": "ellas"},
                {"verb": "construir", "pronoun": "yo"}, {"verb": "construir", "pronoun": "nosotras"},
                {"verb": "construir", "pronoun": "ustedes"}, {"verb": "conseguir", "pronoun": "él"},
                {"verb": "conseguir", "pronoun": "ella"}, {"verb": "conseguir", "pronoun": "ellos"},
            ],
        },
        "opener_en": "Does your neighbor know the area?",
        "opener_es": "¿Tu vecina conoce la zona?",
    },
    # --- GL 5: chat companion of `grammar_spelling_changes_3` ---
    "grammar_spelling_changes_3_chat": {
        "title": "Spelling Changes (3/4) — Chat",
        "grammar_level": 5,
        "lesson_number": 3.1,
        "lesson_type": "conjugation",
        "word_workload": ["conocer", "producir", "construir", "conseguir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Spelling Changes lesson 3: conocer, producir, construir, conseguir', 'targets': [{'verb': 'conocer', 'pronoun': 'tú'}, {'verb': 'conocer', 'pronoun': 'nosotros'}, {'verb': 'producir', 'pronoun': 'usted'}, {'verb': 'producir', 'pronoun': 'ellas'}, {'verb': 'construir', 'pronoun': 'yo'}, {'verb': 'construir', 'pronoun': 'nosotras'}, {'verb': 'construir', 'pronoun': 'ustedes'}, {'verb': 'conseguir', 'pronoun': 'él'}, {'verb': 'conseguir', 'pronoun': 'ella'}, {'verb': 'conseguir', 'pronoun': 'ellos'}]},
    },
    "grammar_spelling_changes_4": {
        "title": "Spelling Changes (4/4)",
        "grammar_level": 5,
        "lesson_number": 4,
        "lesson_type": "conjugation",
        "word_workload": ["recoger", "dirigir", "convencer", "continuar"],
        "video_embed_id": "dYyywu1hOVp",
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {
            "answers": {
                "recoger": {
                    "yo": "recojo", "tú": "recoges", "él": "recoge", "ella": "recoge",
                    "usted": "recoge", "nosotros": "recogemos", "nosotras": "recogemos",
                    "ellos": "recogen", "ellas": "recogen", "ustedes": "recogen",
                },
                "dirigir": {
                    "yo": "dirijo", "tú": "diriges", "él": "dirige", "ella": "dirige",
                    "usted": "dirige", "nosotros": "dirigimos", "nosotras": "dirigimos",
                    "ellos": "dirigen", "ellas": "dirigen", "ustedes": "dirigen",
                },
                "convencer": {
                    "yo": "convenzo", "tú": "convences", "él": "convence", "ella": "convence",
                    "usted": "convence", "nosotros": "convencemos", "nosotras": "convencemos",
                    "ellos": "convencen", "ellas": "convencen", "ustedes": "convencen",
                },
                "continuar": {
                    "yo": "continúo", "tú": "continúas", "él": "continúa", "ella": "continúa",
                    "usted": "continúa", "nosotros": "continuamos", "nosotras": "continuamos",
                    "ellos": "continúan", "ellas": "continúan", "ustedes": "continúan",
                },
            },
        },
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You pick up the food", "es": "Tú recoges la comida", "noun_id": "comida", "type": "written"},
            {"en": "You pick up the book", "es": "Usted recoge el libro", "noun_id": "libro", "type": "auditory"},
            {"en": "I direct the work", "es": "Yo dirijo el trabajo", "noun_id": "trabajo", "type": "written"},
            {"en": "We (f) direct the project", "es": "Nosotras dirigimos el proyecto", "noun_id": None, "type": "auditory"},
            {"en": "They direct from the office", "es": "Ellos dirigen desde la oficina", "noun_id": "oficina", "type": "written"},
            {"en": "She convinces the neighbor", "es": "Ella convence a la vecina", "noun_id": None, "type": "auditory"},
            {"en": "We convince with the truth", "es": "Nosotros convencemos con la verdad", "noun_id": None, "type": "written"},
            {"en": "He continues with the plan", "es": "Él continúa con el plan", "noun_id": None, "type": "auditory"},
            {"en": "They (f) continue in the city", "es": "Ellas continúan en la ciudad", "noun_id": "ciudad", "type": "written"},
            {"en": "You all continue working", "es": "Ustedes continúan trabajando", "noun_id": None, "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "recoger", "pronoun": "tú"}, {"verb": "recoger", "pronoun": "usted"},
            {"verb": "dirigir", "pronoun": "yo"}, {"verb": "dirigir", "pronoun": "nosotras"},
            {"verb": "dirigir", "pronoun": "ellos"}, {"verb": "convencer", "pronoun": "ella"},
            {"verb": "convencer", "pronoun": "nosotros"}, {"verb": "continuar", "pronoun": "él"},
            {"verb": "continuar", "pronoun": "ellas"}, {"verb": "continuar", "pronoun": "ustedes"},
        ],
        "phase_2_config": {
            "description": "Spelling Changes lesson 4: recoger, dirigir, convencer, continuar",
            "targets": [
                {"verb": "recoger", "pronoun": "tú"}, {"verb": "recoger", "pronoun": "usted"},
                {"verb": "dirigir", "pronoun": "yo"}, {"verb": "dirigir", "pronoun": "nosotras"},
                {"verb": "dirigir", "pronoun": "ellos"}, {"verb": "convencer", "pronoun": "ella"},
                {"verb": "convencer", "pronoun": "nosotros"}, {"verb": "continuar", "pronoun": "él"},
                {"verb": "continuar", "pronoun": "ellas"}, {"verb": "continuar", "pronoun": "ustedes"},
            ],
        },
        "opener_en": "Does your boss keep working late?",
        "opener_es": "¿Tu jefa continúa trabajando tarde?",
    },
    # --- GL 5: chat companion of `grammar_spelling_changes_4` ---
    "grammar_spelling_changes_4_chat": {
        "title": "Spelling Changes (4/4) — Chat",
        "grammar_level": 5,
        "lesson_number": 4.1,
        "lesson_type": "conjugation",
        "word_workload": ["recoger", "dirigir", "convencer", "continuar"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Spelling Changes lesson 4: recoger, dirigir, convencer, continuar', 'targets': [{'verb': 'recoger', 'pronoun': 'tú'}, {'verb': 'recoger', 'pronoun': 'usted'}, {'verb': 'dirigir', 'pronoun': 'yo'}, {'verb': 'dirigir', 'pronoun': 'nosotras'}, {'verb': 'dirigir', 'pronoun': 'ellos'}, {'verb': 'convencer', 'pronoun': 'ella'}, {'verb': 'convencer', 'pronoun': 'nosotros'}, {'verb': 'continuar', 'pronoun': 'él'}, {'verb': 'continuar', 'pronoun': 'ellas'}, {'verb': 'continuar', 'pronoun': 'ustedes'}]},
    },
    # --- GL 5.5: Saber vs. Conocer ---
    "grammar_saber_conocer": {
        "title": "Saber vs. Conocer",
        "grammar_level": 5.5,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ["saber", "conocer"],
        "video_embed_id": None,
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {
            "answers": {
                "saber": {
                    "yo": "sé", "tú": "sabes", "él": "sabe", "ella": "sabe",
                    "usted": "sabe", "nosotros": "sabemos", "nosotras": "sabemos",
                    "ellos": "saben", "ellas": "saben", "ustedes": "saben",
                },
                "conocer": {
                    "yo": "conozco", "tú": "conoces", "él": "conoce", "ella": "conoce",
                    "usted": "conoce", "nosotros": "conocemos", "nosotras": "conocemos",
                    "ellos": "conocen", "ellas": "conocen", "ustedes": "conocen",
                },
            },
        },
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "rule_chart": {'kind': 'comparison', 'title': 'Saber vs. Conocer', 'left': {'heading': 'saber', 'items': ['Facts  →  Yo sé la respuesta', 'Skills (saber + infinitive)  →  Sé hablar español', 'Information  →  Sabes qué hora es']}, 'right': {'heading': 'conocer', 'items': ['People  →  Conozco a María', 'Places  →  Conozco la ciudad', 'Familiarity  →  Conoces el restaurante']}, 'footnote': 'saber = knowledge / how-to; conocer = acquaintance / familiarity.'},
        "drill_sentences": [
            {"en": "I know how to speak Spanish", "es": "Yo sé hablar español", "noun_id": None, "type": "written"},
            {"en": "You know the city", "es": "Tú conoces la ciudad", "noun_id": "ciudad", "type": "auditory"},
            {"en": "She knows the answer", "es": "Ella sabe la respuesta", "noun_id": "respuesta", "type": "written"},
            {"en": "He knows the restaurant", "es": "Él conoce el restaurante", "noun_id": "restaurante", "type": "auditory"},
            {"en": "We know how to cook", "es": "Nosotros sabemos cocinar", "noun_id": "cocinar", "type": "written"},
            {"en": "We know the market", "es": "Nosotras conocemos el mercado", "noun_id": "mercado", "type": "auditory"},
            {"en": "They know the way", "es": "Ellos saben el camino", "noun_id": "camino", "type": "written"},
            {"en": "They know the park", "es": "Ellas conocen el parque", "noun_id": "parque", "type": "auditory"},
            {"en": "You know what time it is", "es": "Usted sabe qué hora es", "noun_id": "hora", "type": "written"},
            {"en": "You all know the neighbors", "es": "Ustedes conocen a los vecinos", "noun_id": "vecino", "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "saber", "pronoun": "yo"}, {"verb": "conocer", "pronoun": "tú"},
            {"verb": "saber", "pronoun": "ella"}, {"verb": "conocer", "pronoun": "él"},
            {"verb": "saber", "pronoun": "nosotros"}, {"verb": "conocer", "pronoun": "nosotras"},
            {"verb": "saber", "pronoun": "ellos"}, {"verb": "conocer", "pronoun": "ellas"},
            {"verb": "saber", "pronoun": "usted"}, {"verb": "conocer", "pronoun": "ustedes"},
        ],
        "phase_2_config": {
            "description": "Saber vs. Conocer: saber (facts/skills) vs. conocer (people/places)",
            "targets": [
                {"verb": "saber", "pronoun": "yo"}, {"verb": "conocer", "pronoun": "tú"},
                {"verb": "saber", "pronoun": "ella"}, {"verb": "conocer", "pronoun": "él"},
                {"verb": "saber", "pronoun": "nosotros"}, {"verb": "conocer", "pronoun": "nosotras"},
                {"verb": "saber", "pronoun": "ellos"}, {"verb": "conocer", "pronoun": "ellas"},
            ],
        },
        "opener_en": "Do you know this area?",
        "opener_es": "¿Conoces esta zona?",
    },
    # --- GL 5.5: chat companion of `grammar_saber_conocer` ---
    "grammar_saber_conocer_chat": {
        "title": "Saber vs. Conocer — Chat",
        "grammar_level": 5.5,
        "lesson_number": 1.1,
        "lesson_type": "conjugation",
        "word_workload": ["saber", "conocer"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Saber vs. Conocer: saber (facts/skills) vs. conocer (people/places)', 'targets': [{'verb': 'saber', 'pronoun': 'yo'}, {'verb': 'conocer', 'pronoun': 'tú'}, {'verb': 'saber', 'pronoun': 'ella'}, {'verb': 'conocer', 'pronoun': 'él'}, {'verb': 'saber', 'pronoun': 'nosotros'}, {'verb': 'conocer', 'pronoun': 'nosotras'}, {'verb': 'saber', 'pronoun': 'ellos'}, {'verb': 'conocer', 'pronoun': 'ellas'}]},
    },
    # --- GL 6: Present O→UE — 3 lessons ---
    "grammar_present_o_ue_1": {
        "title": "Present O→UE (1/3)",
        "grammar_level": 6,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ['mover', 'almorzar', 'morir', 'poder', 'dormir', 'volver'],
        "video_embed_id": "My2TaOGsmet",
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {"answers": {
            "mover": {"yo": "muevo", "tú": "mueves", "él": "mueve", "ella": "mueve", "usted": "mueve", "nosotros": "movemos", "nosotras": "movemos", "ellos": "mueven", "ellas": "mueven", "ustedes": "mueven"},
            "almorzar": {"yo": "almuerzo", "tú": "almuerzas", "él": "almuerza", "ella": "almuerza", "usted": "almuerza", "nosotros": "almorzamos", "nosotras": "almorzamos", "ellos": "almuerzan", "ellas": "almuerzan", "ustedes": "almuerzan"},
            "morir": {"yo": "muero", "tú": "mueres", "él": "muere", "ella": "muere", "usted": "muere", "nosotros": "morimos", "nosotras": "morimos", "ellos": "mueren", "ellas": "mueren", "ustedes": "mueren"},
            "poder": {"yo": "puedo", "tú": "puedes", "él": "puede", "ella": "puede", "usted": "puede", "nosotros": "podemos", "nosotras": "podemos", "ellos": "pueden", "ellas": "pueden", "ustedes": "pueden"},
            "dormir": {"yo": "duermo", "tú": "duermes", "él": "duerme", "ella": "duerme", "usted": "duerme", "nosotros": "dormimos", "nosotras": "dormimos", "ellos": "duermen", "ellas": "duermen", "ustedes": "duermen"},
            "volver": {"yo": "vuelvo", "tú": "vuelves", "él": "vuelve", "ella": "vuelve", "usted": "vuelve", "nosotros": "volvemos", "nosotras": "volvemos", "ellos": "vuelven", "ellas": "vuelven", "ustedes": "vuelven"},
        }},
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I move the table", "es": "Yo muevo la mesa", "noun_id": None, "type": "written"},
            {"en": "You have lunch at the restaurant", "es": "Tú almuerzas en el restaurante", "noun_id": "restaurante", "type": "auditory"},
            {"en": "He is dying of hunger", "es": "Él muere de hambre", "noun_id": None, "type": "written"},
            {"en": "She can help at the office", "es": "Ella puede ayudar en la oficina", "noun_id": "oficina", "type": "auditory"},
            {"en": "You sleep eight hours", "es": "Usted duerme ocho horas", "noun_id": None, "type": "written"},
            {"en": "We return home", "es": "Nosotros volvemos a casa", "noun_id": "casa", "type": "auditory"},
            {"en": "We (f) move the chairs", "es": "Nosotras movemos las sillas", "noun_id": None, "type": "written"},
            {"en": "They have lunch in the city", "es": "Ellos almuerzan en la ciudad", "noun_id": "ciudad", "type": "auditory"},
            {"en": "They (f) die laughing", "es": "Ellas mueren de risa", "noun_id": None, "type": "written"},
            {"en": "You all can speak Spanish", "es": "Ustedes pueden hablar español", "noun_id": None, "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "mover", "pronoun": "yo"},
            {"verb": "almorzar", "pronoun": "tú"},
            {"verb": "morir", "pronoun": "él"},
            {"verb": "poder", "pronoun": "ella"},
            {"verb": "dormir", "pronoun": "usted"},
            {"verb": "volver", "pronoun": "nosotros"},
            {"verb": "mover", "pronoun": "nosotras"},
            {"verb": "almorzar", "pronoun": "ellos"},
            {"verb": "morir", "pronoun": "ellas"},
            {"verb": "poder", "pronoun": "ustedes"},
        ],
        "phase_2_config": {
            "description": "Present O→UE lesson 1",
            "targets": [
            {"verb": "mover", "pronoun": "yo"},
            {"verb": "almorzar", "pronoun": "tú"},
            {"verb": "morir", "pronoun": "él"},
            {"verb": "poder", "pronoun": "ella"},
            {"verb": "dormir", "pronoun": "usted"},
            {"verb": "volver", "pronoun": "nosotros"},
            {"verb": "mover", "pronoun": "nosotras"},
            {"verb": "almorzar", "pronoun": "ellos"},
            {"verb": "morir", "pronoun": "ellas"},
            {"verb": "poder", "pronoun": "ustedes"},
            ],
        },
        "opener_en": "Can you move your car?",
        "opener_es": "¿Puedes mover tu carro?",
    },
    # --- GL 6: chat companion of `grammar_present_o_ue_1` ---
    "grammar_present_o_ue_1_chat": {
        "title": "Present O→UE (1/3) — Chat",
        "grammar_level": 6,
        "lesson_number": 1.1,
        "lesson_type": "conjugation",
        "word_workload": ["mover", "almorzar", "morir", "poder", "dormir", "volver"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Present O→UE lesson 1', 'targets': [{'verb': 'mover', 'pronoun': 'yo'}, {'verb': 'almorzar', 'pronoun': 'tú'}, {'verb': 'morir', 'pronoun': 'él'}, {'verb': 'poder', 'pronoun': 'ella'}, {'verb': 'dormir', 'pronoun': 'usted'}, {'verb': 'volver', 'pronoun': 'nosotros'}, {'verb': 'mover', 'pronoun': 'nosotras'}, {'verb': 'almorzar', 'pronoun': 'ellos'}, {'verb': 'morir', 'pronoun': 'ellas'}, {'verb': 'poder', 'pronoun': 'ustedes'}]},
    },
    "grammar_present_o_ue_2": {
        "title": "Present O→UE (2/3)",
        "grammar_level": 6,
        "lesson_number": 2,
        "lesson_type": "conjugation",
        "word_workload": ['mover', 'almorzar', 'morir', 'poder', 'dormir', 'volver'],
        "video_embed_id": "My2TaOGsmet",
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {"answers": {
            "mover": {"yo": "muevo", "tú": "mueves", "él": "mueve", "ella": "mueve", "usted": "mueve", "nosotros": "movemos", "nosotras": "movemos", "ellos": "mueven", "ellas": "mueven", "ustedes": "mueven"},
            "almorzar": {"yo": "almuerzo", "tú": "almuerzas", "él": "almuerza", "ella": "almuerza", "usted": "almuerza", "nosotros": "almorzamos", "nosotras": "almorzamos", "ellos": "almuerzan", "ellas": "almuerzan", "ustedes": "almuerzan"},
            "morir": {"yo": "muero", "tú": "mueres", "él": "muere", "ella": "muere", "usted": "muere", "nosotros": "morimos", "nosotras": "morimos", "ellos": "mueren", "ellas": "mueren", "ustedes": "mueren"},
            "poder": {"yo": "puedo", "tú": "puedes", "él": "puede", "ella": "puede", "usted": "puede", "nosotros": "podemos", "nosotras": "podemos", "ellos": "pueden", "ellas": "pueden", "ustedes": "pueden"},
            "dormir": {"yo": "duermo", "tú": "duermes", "él": "duerme", "ella": "duerme", "usted": "duerme", "nosotros": "dormimos", "nosotras": "dormimos", "ellos": "duermen", "ellas": "duermen", "ustedes": "duermen"},
            "volver": {"yo": "vuelvo", "tú": "vuelves", "él": "vuelve", "ella": "vuelve", "usted": "vuelve", "nosotros": "volvemos", "nosotras": "volvemos", "ellos": "vuelven", "ellas": "vuelven", "ustedes": "vuelven"},
        }},
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You move the chair", "es": "Tú mueves la silla", "noun_id": "silla", "type": "written"},
            {"en": "I have lunch at the market", "es": "Yo almuerzo en el mercado", "noun_id": "mercado", "type": "auditory"},
            {"en": "She is dying of tiredness", "es": "Ella muere de cansancio", "noun_id": None, "type": "written"},
            {"en": "He can come to the house", "es": "Él puede venir a la casa", "noun_id": "casa", "type": "auditory"},
            {"en": "We sleep in the bedroom", "es": "Nosotros dormimos en la habitación", "noun_id": None, "type": "written"},
            {"en": "You return to the city", "es": "Usted vuelve a la ciudad", "noun_id": "ciudad", "type": "auditory"},
            {"en": "They move to the park", "es": "Ellos mueven al parque", "noun_id": "parque", "type": "written"},
            {"en": "We (f) have lunch near the store", "es": "Nosotras almorzamos cerca de la tienda", "noun_id": "tienda", "type": "auditory"},
            {"en": "You all are dying of laughter", "es": "Ustedes mueren de risa", "noun_id": None, "type": "written"},
            {"en": "They (f) can speak Spanish", "es": "Ellas pueden hablar español", "noun_id": None, "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "mover", "pronoun": "tú"},
            {"verb": "almorzar", "pronoun": "yo"},
            {"verb": "morir", "pronoun": "ella"},
            {"verb": "poder", "pronoun": "él"},
            {"verb": "dormir", "pronoun": "nosotros"},
            {"verb": "volver", "pronoun": "usted"},
            {"verb": "mover", "pronoun": "ellos"},
            {"verb": "almorzar", "pronoun": "nosotras"},
            {"verb": "morir", "pronoun": "ustedes"},
            {"verb": "poder", "pronoun": "ellas"},
        ],
        "phase_2_config": {
            "description": "Present O→UE lesson 2",
            "targets": [
            {"verb": "mover", "pronoun": "tú"},
            {"verb": "almorzar", "pronoun": "yo"},
            {"verb": "morir", "pronoun": "ella"},
            {"verb": "poder", "pronoun": "él"},
            {"verb": "dormir", "pronoun": "nosotros"},
            {"verb": "volver", "pronoun": "usted"},
            {"verb": "mover", "pronoun": "ellos"},
            {"verb": "almorzar", "pronoun": "nosotras"},
            {"verb": "morir", "pronoun": "ustedes"},
            {"verb": "poder", "pronoun": "ellas"},
            ],
        },
        "opener_en": "Where does your sister eat lunch?",
        "opener_es": "¿Dónde almuerza tu hermana?",
    },
    # --- GL 6: chat companion of `grammar_present_o_ue_2` ---
    "grammar_present_o_ue_2_chat": {
        "title": "Present O→UE (2/3) — Chat",
        "grammar_level": 6,
        "lesson_number": 2.1,
        "lesson_type": "conjugation",
        "word_workload": ["mover", "almorzar", "morir", "poder", "dormir", "volver"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Present O→UE lesson 2', 'targets': [{'verb': 'mover', 'pronoun': 'tú'}, {'verb': 'almorzar', 'pronoun': 'yo'}, {'verb': 'morir', 'pronoun': 'ella'}, {'verb': 'poder', 'pronoun': 'él'}, {'verb': 'dormir', 'pronoun': 'nosotros'}, {'verb': 'volver', 'pronoun': 'usted'}, {'verb': 'mover', 'pronoun': 'ellos'}, {'verb': 'almorzar', 'pronoun': 'nosotras'}, {'verb': 'morir', 'pronoun': 'ustedes'}, {'verb': 'poder', 'pronoun': 'ellas'}]},
    },
    "grammar_present_o_ue_3": {
        "title": "Present O→UE (3/3)",
        "grammar_level": 6,
        "lesson_number": 3,
        "lesson_type": "conjugation",
        "word_workload": ['mover', 'almorzar', 'morir', 'poder', 'dormir', 'volver'],
        "video_embed_id": "My2TaOGsmet",
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {"answers": {
            "mover": {"yo": "muevo", "tú": "mueves", "él": "mueve", "ella": "mueve", "usted": "mueve", "nosotros": "movemos", "nosotras": "movemos", "ellos": "mueven", "ellas": "mueven", "ustedes": "mueven"},
            "almorzar": {"yo": "almuerzo", "tú": "almuerzas", "él": "almuerza", "ella": "almuerza", "usted": "almuerza", "nosotros": "almorzamos", "nosotras": "almorzamos", "ellos": "almuerzan", "ellas": "almuerzan", "ustedes": "almuerzan"},
            "morir": {"yo": "muero", "tú": "mueres", "él": "muere", "ella": "muere", "usted": "muere", "nosotros": "morimos", "nosotras": "morimos", "ellos": "mueren", "ellas": "mueren", "ustedes": "mueren"},
            "poder": {"yo": "puedo", "tú": "puedes", "él": "puede", "ella": "puede", "usted": "puede", "nosotros": "podemos", "nosotras": "podemos", "ellos": "pueden", "ellas": "pueden", "ustedes": "pueden"},
            "dormir": {"yo": "duermo", "tú": "duermes", "él": "duerme", "ella": "duerme", "usted": "duerme", "nosotros": "dormimos", "nosotras": "dormimos", "ellos": "duermen", "ellas": "duermen", "ustedes": "duermen"},
            "volver": {"yo": "vuelvo", "tú": "vuelves", "él": "vuelve", "ella": "vuelve", "usted": "vuelve", "nosotros": "volvemos", "nosotras": "volvemos", "ellos": "vuelven", "ellas": "vuelven", "ustedes": "vuelven"},
        }},
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "He moves the car", "es": "Él mueve el carro", "noun_id": "carro", "type": "written"},
            {"en": "She has lunch at home", "es": "Ella almuerza en casa", "noun_id": "casa", "type": "auditory"},
            {"en": "I am dying of thirst", "es": "Yo muero de sed", "noun_id": None, "type": "written"},
            {"en": "You can go to the market", "es": "Tú puedes ir al mercado", "noun_id": "mercado", "type": "auditory"},
            {"en": "We (f) sleep eight hours at night", "es": "Nosotras dormimos ocho horas de noche", "noun_id": None, "type": "written"},
            {"en": "They return to the restaurant", "es": "Ellos vuelven al restaurante", "noun_id": "restaurante", "type": "auditory"},
            {"en": "You move to a new house", "es": "Usted se mueve a una nueva casa", "noun_id": "casa", "type": "written"},
            {"en": "We have lunch near the office", "es": "Nosotros almorzamos cerca de la oficina", "noun_id": "oficina", "type": "auditory"},
            {"en": "They (f) sleep in the house", "es": "Ellas duermen en la casa", "noun_id": "casa", "type": "written"},
            {"en": "You all return to the city", "es": "Ustedes vuelven a la ciudad", "noun_id": "ciudad", "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "mover", "pronoun": "él"},
            {"verb": "almorzar", "pronoun": "ella"},
            {"verb": "morir", "pronoun": "yo"},
            {"verb": "poder", "pronoun": "tú"},
            {"verb": "dormir", "pronoun": "nosotras"},
            {"verb": "volver", "pronoun": "ellos"},
            {"verb": "mover", "pronoun": "usted"},
            {"verb": "almorzar", "pronoun": "nosotros"},
            {"verb": "dormir", "pronoun": "ellas"},
            {"verb": "volver", "pronoun": "ustedes"},
        ],
        "phase_2_config": {
            "description": "Present O→UE lesson 3",
            "targets": [
            {"verb": "mover", "pronoun": "él"},
            {"verb": "almorzar", "pronoun": "ella"},
            {"verb": "morir", "pronoun": "yo"},
            {"verb": "poder", "pronoun": "tú"},
            {"verb": "dormir", "pronoun": "nosotras"},
            {"verb": "volver", "pronoun": "ellos"},
            {"verb": "mover", "pronoun": "usted"},
            {"verb": "almorzar", "pronoun": "nosotros"},
            {"verb": "dormir", "pronoun": "ellas"},
            {"verb": "volver", "pronoun": "ustedes"},
            ],
        },
        "opener_en": "What time do your kids sleep?",
        "opener_es": "¿A qué hora duermen tus hijas?",
    },
    # --- GL 6: chat companion of `grammar_present_o_ue_3` ---
    "grammar_present_o_ue_3_chat": {
        "title": "Present O→UE (3/3) — Chat",
        "grammar_level": 6,
        "lesson_number": 3.1,
        "lesson_type": "conjugation",
        "word_workload": ["mover", "almorzar", "morir", "poder", "dormir", "volver"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Present O→UE lesson 3', 'targets': [{'verb': 'mover', 'pronoun': 'él'}, {'verb': 'almorzar', 'pronoun': 'ella'}, {'verb': 'morir', 'pronoun': 'yo'}, {'verb': 'poder', 'pronoun': 'tú'}, {'verb': 'dormir', 'pronoun': 'nosotras'}, {'verb': 'volver', 'pronoun': 'ellos'}, {'verb': 'mover', 'pronoun': 'usted'}, {'verb': 'almorzar', 'pronoun': 'nosotros'}, {'verb': 'dormir', 'pronoun': 'ellas'}, {'verb': 'volver', 'pronoun': 'ustedes'}]},
    },
    # --- GL 7: Present E→IE — 3 lessons ---
    "grammar_present_e_ie_1": {
        "title": "Present E→IE (1/3)",
        "grammar_level": 7,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ['cerrar', 'entender', 'pensar', 'querer', 'preferir', 'empezar'],
        "video_embed_id": "BwvOV8xReZZ",
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {"answers": {
            "cerrar": {"yo": "cierro", "tú": "cierras", "él": "cierra", "ella": "cierra", "usted": "cierra", "nosotros": "cerramos", "nosotras": "cerramos", "ellos": "cierran", "ellas": "cierran", "ustedes": "cierran"},
            "entender": {"yo": "entiendo", "tú": "entiendes", "él": "entiende", "ella": "entiende", "usted": "entiende", "nosotros": "entendemos", "nosotras": "entendemos", "ellos": "entienden", "ellas": "entienden", "ustedes": "entienden"},
            "pensar": {"yo": "pienso", "tú": "piensas", "él": "piensa", "ella": "piensa", "usted": "piensa", "nosotros": "pensamos", "nosotras": "pensamos", "ellos": "piensan", "ellas": "piensan", "ustedes": "piensan"},
            "querer": {"yo": "quiero", "tú": "quieres", "él": "quiere", "ella": "quiere", "usted": "quiere", "nosotros": "queremos", "nosotras": "queremos", "ellos": "quieren", "ellas": "quieren", "ustedes": "quieren"},
            "preferir": {"yo": "prefiero", "tú": "prefieres", "él": "prefiere", "ella": "prefiere", "usted": "prefiere", "nosotros": "preferimos", "nosotras": "preferimos", "ellos": "prefieren", "ellas": "prefieren", "ustedes": "prefieren"},
            "empezar": {"yo": "empiezo", "tú": "empiezas", "él": "empieza", "ella": "empieza", "usted": "empieza", "nosotros": "empezamos", "nosotras": "empezamos", "ellos": "empiezan", "ellas": "empiezan", "ustedes": "empiezan"},
        }},
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I close the door", "es": "Yo cierro la puerta", "noun_id": "puerta", "type": "written"},
            {"en": "You understand Spanish well", "es": "Tú entiendes bien el español", "noun_id": None, "type": "auditory"},
            {"en": "He thinks about the plan", "es": "Él piensa en el plan", "noun_id": None, "type": "written"},
            {"en": "She wants water", "es": "Ella quiere agua", "noun_id": "agua", "type": "auditory"},
            {"en": "You prefer coffee", "es": "Usted prefiere el café", "noun_id": "café", "type": "written"},
            {"en": "We start early", "es": "Nosotros empezamos temprano", "noun_id": None, "type": "auditory"},
            {"en": "We (f) close the store", "es": "Nosotras cerramos la tienda", "noun_id": "tienda", "type": "written"},
            {"en": "They understand the situation", "es": "Ellos entienden la situación", "noun_id": None, "type": "auditory"},
            {"en": "They (f) think about the house", "es": "Ellas piensan en la casa", "noun_id": "casa", "type": "written"},
            {"en": "You all want to eat", "es": "Ustedes quieren comer", "noun_id": None, "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "cerrar", "pronoun": "yo"},
            {"verb": "entender", "pronoun": "tú"},
            {"verb": "pensar", "pronoun": "él"},
            {"verb": "querer", "pronoun": "ella"},
            {"verb": "preferir", "pronoun": "usted"},
            {"verb": "empezar", "pronoun": "nosotros"},
            {"verb": "cerrar", "pronoun": "nosotras"},
            {"verb": "entender", "pronoun": "ellos"},
            {"verb": "pensar", "pronoun": "ellas"},
            {"verb": "querer", "pronoun": "ustedes"},
        ],
        "phase_2_config": {
            "description": "Present E→IE lesson 1",
            "targets": [
            {"verb": "cerrar", "pronoun": "yo"},
            {"verb": "entender", "pronoun": "tú"},
            {"verb": "pensar", "pronoun": "él"},
            {"verb": "querer", "pronoun": "ella"},
            {"verb": "preferir", "pronoun": "usted"},
            {"verb": "empezar", "pronoun": "nosotros"},
            {"verb": "cerrar", "pronoun": "nosotras"},
            {"verb": "entender", "pronoun": "ellos"},
            {"verb": "pensar", "pronoun": "ellas"},
            {"verb": "querer", "pronoun": "ustedes"},
            ],
        },
        "opener_en": "What time do they close?",
        "opener_es": "¿A qué hora cierran aquí?",
    },
    # --- GL 7: chat companion of `grammar_present_e_ie_1` ---
    "grammar_present_e_ie_1_chat": {
        "title": "Present E→IE (1/3) — Chat",
        "grammar_level": 7,
        "lesson_number": 1.1,
        "lesson_type": "conjugation",
        "word_workload": ["cerrar", "entender", "pensar", "querer", "preferir", "empezar"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Present E→IE lesson 1', 'targets': [{'verb': 'cerrar', 'pronoun': 'yo'}, {'verb': 'entender', 'pronoun': 'tú'}, {'verb': 'pensar', 'pronoun': 'él'}, {'verb': 'querer', 'pronoun': 'ella'}, {'verb': 'preferir', 'pronoun': 'usted'}, {'verb': 'empezar', 'pronoun': 'nosotros'}, {'verb': 'cerrar', 'pronoun': 'nosotras'}, {'verb': 'entender', 'pronoun': 'ellos'}, {'verb': 'pensar', 'pronoun': 'ellas'}, {'verb': 'querer', 'pronoun': 'ustedes'}]},
    },
    "grammar_present_e_ie_2": {
        "title": "Present E→IE (2/3)",
        "grammar_level": 7,
        "lesson_number": 2,
        "lesson_type": "conjugation",
        "word_workload": ['cerrar', 'entender', 'pensar', 'querer', 'preferir', 'empezar'],
        "video_embed_id": "BwvOV8xReZZ",
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {"answers": {
            "cerrar": {"yo": "cierro", "tú": "cierras", "él": "cierra", "ella": "cierra", "usted": "cierra", "nosotros": "cerramos", "nosotras": "cerramos", "ellos": "cierran", "ellas": "cierran", "ustedes": "cierran"},
            "entender": {"yo": "entiendo", "tú": "entiendes", "él": "entiende", "ella": "entiende", "usted": "entiende", "nosotros": "entendemos", "nosotras": "entendemos", "ellos": "entienden", "ellas": "entienden", "ustedes": "entienden"},
            "pensar": {"yo": "pienso", "tú": "piensas", "él": "piensa", "ella": "piensa", "usted": "piensa", "nosotros": "pensamos", "nosotras": "pensamos", "ellos": "piensan", "ellas": "piensan", "ustedes": "piensan"},
            "querer": {"yo": "quiero", "tú": "quieres", "él": "quiere", "ella": "quiere", "usted": "quiere", "nosotros": "queremos", "nosotras": "queremos", "ellos": "quieren", "ellas": "quieren", "ustedes": "quieren"},
            "preferir": {"yo": "prefiero", "tú": "prefieres", "él": "prefiere", "ella": "prefiere", "usted": "prefiere", "nosotros": "preferimos", "nosotras": "preferimos", "ellos": "prefieren", "ellas": "prefieren", "ustedes": "prefieren"},
            "empezar": {"yo": "empiezo", "tú": "empiezas", "él": "empieza", "ella": "empieza", "usted": "empieza", "nosotros": "empezamos", "nosotras": "empezamos", "ellos": "empiezan", "ellas": "empiezan", "ustedes": "empiezan"},
        }},
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You close the window", "es": "Tú cierras la ventana", "noun_id": "ventana", "type": "written"},
            {"en": "I understand the problem", "es": "Yo entiendo el problema", "noun_id": None, "type": "auditory"},
            {"en": "She thinks about work", "es": "Ella piensa en el trabajo", "noun_id": "trabajo", "type": "written"},
            {"en": "He wants a coffee", "es": "Él quiere un café", "noun_id": "café", "type": "auditory"},
            {"en": "We prefer the park", "es": "Nosotros preferimos el parque", "noun_id": "parque", "type": "written"},
            {"en": "You start the day early", "es": "Usted empieza el día temprano", "noun_id": None, "type": "auditory"},
            {"en": "They close the door", "es": "Ellos cierran la puerta", "noun_id": "puerta", "type": "written"},
            {"en": "We (f) understand the situation", "es": "Nosotras entendemos la situación", "noun_id": None, "type": "auditory"},
            {"en": "You all think about it", "es": "Ustedes piensan en eso", "noun_id": None, "type": "written"},
            {"en": "They (f) want to go home", "es": "Ellas quieren ir a casa", "noun_id": "casa", "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "cerrar", "pronoun": "tú"},
            {"verb": "entender", "pronoun": "yo"},
            {"verb": "pensar", "pronoun": "ella"},
            {"verb": "querer", "pronoun": "él"},
            {"verb": "preferir", "pronoun": "nosotros"},
            {"verb": "empezar", "pronoun": "usted"},
            {"verb": "cerrar", "pronoun": "ellos"},
            {"verb": "entender", "pronoun": "nosotras"},
            {"verb": "pensar", "pronoun": "ustedes"},
            {"verb": "querer", "pronoun": "ellas"},
        ],
        "phase_2_config": {
            "description": "Present E→IE lesson 2",
            "targets": [
            {"verb": "cerrar", "pronoun": "tú"},
            {"verb": "entender", "pronoun": "yo"},
            {"verb": "pensar", "pronoun": "ella"},
            {"verb": "querer", "pronoun": "él"},
            {"verb": "preferir", "pronoun": "nosotros"},
            {"verb": "empezar", "pronoun": "usted"},
            {"verb": "cerrar", "pronoun": "ellos"},
            {"verb": "entender", "pronoun": "nosotras"},
            {"verb": "pensar", "pronoun": "ustedes"},
            {"verb": "querer", "pronoun": "ellas"},
            ],
        },
        "opener_en": "Does your partner prefer the beach?",
        "opener_es": "¿Tu pareja prefiere la playa?",
    },
    # --- GL 7: chat companion of `grammar_present_e_ie_2` ---
    "grammar_present_e_ie_2_chat": {
        "title": "Present E→IE (2/3) — Chat",
        "grammar_level": 7,
        "lesson_number": 2.1,
        "lesson_type": "conjugation",
        "word_workload": ["cerrar", "entender", "pensar", "querer", "preferir", "empezar"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Present E→IE lesson 2', 'targets': [{'verb': 'cerrar', 'pronoun': 'tú'}, {'verb': 'entender', 'pronoun': 'yo'}, {'verb': 'pensar', 'pronoun': 'ella'}, {'verb': 'querer', 'pronoun': 'él'}, {'verb': 'preferir', 'pronoun': 'nosotros'}, {'verb': 'empezar', 'pronoun': 'usted'}, {'verb': 'cerrar', 'pronoun': 'ellos'}, {'verb': 'entender', 'pronoun': 'nosotras'}, {'verb': 'pensar', 'pronoun': 'ustedes'}, {'verb': 'querer', 'pronoun': 'ellas'}]},
    },
    "grammar_present_e_ie_3": {
        "title": "Present E→IE (3/3)",
        "grammar_level": 7,
        "lesson_number": 3,
        "lesson_type": "conjugation",
        "word_workload": ['cerrar', 'entender', 'pensar', 'querer', 'preferir', 'empezar'],
        "video_embed_id": "BwvOV8xReZZ",
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {"answers": {
            "cerrar": {"yo": "cierro", "tú": "cierras", "él": "cierra", "ella": "cierra", "usted": "cierra", "nosotros": "cerramos", "nosotras": "cerramos", "ellos": "cierran", "ellas": "cierran", "ustedes": "cierran"},
            "entender": {"yo": "entiendo", "tú": "entiendes", "él": "entiende", "ella": "entiende", "usted": "entiende", "nosotros": "entendemos", "nosotras": "entendemos", "ellos": "entienden", "ellas": "entienden", "ustedes": "entienden"},
            "pensar": {"yo": "pienso", "tú": "piensas", "él": "piensa", "ella": "piensa", "usted": "piensa", "nosotros": "pensamos", "nosotras": "pensamos", "ellos": "piensan", "ellas": "piensan", "ustedes": "piensan"},
            "querer": {"yo": "quiero", "tú": "quieres", "él": "quiere", "ella": "quiere", "usted": "quiere", "nosotros": "queremos", "nosotras": "queremos", "ellos": "quieren", "ellas": "quieren", "ustedes": "quieren"},
            "preferir": {"yo": "prefiero", "tú": "prefieres", "él": "prefiere", "ella": "prefiere", "usted": "prefiere", "nosotros": "preferimos", "nosotras": "preferimos", "ellos": "prefieren", "ellas": "prefieren", "ustedes": "prefieren"},
            "empezar": {"yo": "empiezo", "tú": "empiezas", "él": "empieza", "ella": "empieza", "usted": "empieza", "nosotros": "empezamos", "nosotras": "empezamos", "ellos": "empiezan", "ellas": "empiezan", "ustedes": "empiezan"},
        }},
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "He closes the shop at night", "es": "Él cierra la tienda de noche", "noun_id": "tienda", "type": "written"},
            {"en": "She understands Spanish", "es": "Ella entiende español", "noun_id": None, "type": "auditory"},
            {"en": "I think about the house", "es": "Yo pienso en la casa", "noun_id": "casa", "type": "written"},
            {"en": "You want a dog", "es": "Tú quieres un perro", "noun_id": "perro", "type": "auditory"},
            {"en": "We (f) prefer water", "es": "Nosotras preferimos agua", "noun_id": "agua", "type": "written"},
            {"en": "They start the work early", "es": "Ellos empiezan el trabajo temprano", "noun_id": "trabajo", "type": "auditory"},
            {"en": "You close the door", "es": "Usted cierra la puerta", "noun_id": "puerta", "type": "written"},
            {"en": "We understand the plan", "es": "Nosotros entendemos el plan", "noun_id": None, "type": "auditory"},
            {"en": "They (f) prefer the city", "es": "Ellas prefieren la ciudad", "noun_id": "ciudad", "type": "written"},
            {"en": "You all start today", "es": "Ustedes empiezan hoy", "noun_id": None, "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "cerrar", "pronoun": "él"},
            {"verb": "entender", "pronoun": "ella"},
            {"verb": "pensar", "pronoun": "yo"},
            {"verb": "querer", "pronoun": "tú"},
            {"verb": "preferir", "pronoun": "nosotras"},
            {"verb": "empezar", "pronoun": "ellos"},
            {"verb": "cerrar", "pronoun": "usted"},
            {"verb": "entender", "pronoun": "nosotros"},
            {"verb": "preferir", "pronoun": "ellas"},
            {"verb": "empezar", "pronoun": "ustedes"},
        ],
        "phase_2_config": {
            "description": "Present E→IE lesson 3",
            "targets": [
            {"verb": "cerrar", "pronoun": "él"},
            {"verb": "entender", "pronoun": "ella"},
            {"verb": "pensar", "pronoun": "yo"},
            {"verb": "querer", "pronoun": "tú"},
            {"verb": "preferir", "pronoun": "nosotras"},
            {"verb": "empezar", "pronoun": "ellos"},
            {"verb": "cerrar", "pronoun": "usted"},
            {"verb": "entender", "pronoun": "nosotros"},
            {"verb": "preferir", "pronoun": "ellas"},
            {"verb": "empezar", "pronoun": "ustedes"},
            ],
        },
        "opener_en": "Do your friends want to come?",
        "opener_es": "¿Tus amigas quieren venir?",
    },
    # --- GL 7: chat companion of `grammar_present_e_ie_3` ---
    "grammar_present_e_ie_3_chat": {
        "title": "Present E→IE (3/3) — Chat",
        "grammar_level": 7,
        "lesson_number": 3.1,
        "lesson_type": "conjugation",
        "word_workload": ["cerrar", "entender", "pensar", "querer", "preferir", "empezar"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Present E→IE lesson 3', 'targets': [{'verb': 'cerrar', 'pronoun': 'él'}, {'verb': 'entender', 'pronoun': 'ella'}, {'verb': 'pensar', 'pronoun': 'yo'}, {'verb': 'querer', 'pronoun': 'tú'}, {'verb': 'preferir', 'pronoun': 'nosotras'}, {'verb': 'empezar', 'pronoun': 'ellos'}, {'verb': 'cerrar', 'pronoun': 'usted'}, {'verb': 'entender', 'pronoun': 'nosotros'}, {'verb': 'preferir', 'pronoun': 'ellas'}, {'verb': 'empezar', 'pronoun': 'ustedes'}]},
    },
    # --- GL 8: Present E→I — 3 lessons ---
    "grammar_present_e_i_1": {
        "title": "Present E→I (1/3)",
        "grammar_level": 8,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ['pedir', 'repetir', 'seguir', 'servir', 'vestir', 'elegir'],
        "video_embed_id": "meS3lef4ubp",
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {"answers": {
            "pedir": {"yo": "pido", "tú": "pides", "él": "pide", "ella": "pide", "usted": "pide", "nosotros": "pedimos", "nosotras": "pedimos", "ellos": "piden", "ellas": "piden", "ustedes": "piden"},
            "repetir": {"yo": "repito", "tú": "repites", "él": "repite", "ella": "repite", "usted": "repite", "nosotros": "repetimos", "nosotras": "repetimos", "ellos": "repiten", "ellas": "repiten", "ustedes": "repiten"},
            "seguir": {"yo": "sigo", "tú": "sigues", "él": "sigue", "ella": "sigue", "usted": "sigue", "nosotros": "seguimos", "nosotras": "seguimos", "ellos": "siguen", "ellas": "siguen", "ustedes": "siguen"},
            "servir": {"yo": "sirvo", "tú": "sirves", "él": "sirve", "ella": "sirve", "usted": "sirve", "nosotros": "servimos", "nosotras": "servimos", "ellos": "sirven", "ellas": "sirven", "ustedes": "sirven"},
            "vestir": {"yo": "visto", "tú": "vistes", "él": "viste", "ella": "viste", "usted": "viste", "nosotros": "vestimos", "nosotras": "vestimos", "ellos": "visten", "ellas": "visten", "ustedes": "visten"},
            "elegir": {"yo": "elijo", "tú": "eliges", "él": "elige", "ella": "elige", "usted": "elige", "nosotros": "elegimos", "nosotras": "elegimos", "ellos": "eligen", "ellas": "eligen", "ustedes": "eligen"},
        }},
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I order coffee at the restaurant", "es": "Yo pido café en el restaurante", "noun_id": "café", "type": "written"},
            {"en": "You repeat the word", "es": "Tú repites la palabra", "noun_id": None, "type": "auditory"},
            {"en": "He continues on the road", "es": "Él sigue en el camino", "noun_id": None, "type": "written"},
            {"en": "She serves the food", "es": "Ella sirve la comida", "noun_id": "comida", "type": "auditory"},
            {"en": "You dress the child", "es": "Usted viste al niño", "noun_id": None, "type": "written"},
            {"en": "We choose the book", "es": "Nosotros elegimos el libro", "noun_id": "libro", "type": "auditory"},
            {"en": "We (f) order water", "es": "Nosotras pedimos agua", "noun_id": "agua", "type": "written"},
            {"en": "They repeat the sentence", "es": "Ellos repiten la frase", "noun_id": None, "type": "auditory"},
            {"en": "They (f) continue working", "es": "Ellas siguen trabajando", "noun_id": None, "type": "written"},
            {"en": "You all serve the coffee", "es": "Ustedes sirven el café", "noun_id": "café", "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "pedir", "pronoun": "yo"},
            {"verb": "repetir", "pronoun": "tú"},
            {"verb": "seguir", "pronoun": "él"},
            {"verb": "servir", "pronoun": "ella"},
            {"verb": "vestir", "pronoun": "usted"},
            {"verb": "elegir", "pronoun": "nosotros"},
            {"verb": "pedir", "pronoun": "nosotras"},
            {"verb": "repetir", "pronoun": "ellos"},
            {"verb": "seguir", "pronoun": "ellas"},
            {"verb": "servir", "pronoun": "ustedes"},
        ],
        "phase_2_config": {
            "description": "Present E→I lesson 1",
            "targets": [
            {"verb": "pedir", "pronoun": "yo"},
            {"verb": "repetir", "pronoun": "tú"},
            {"verb": "seguir", "pronoun": "él"},
            {"verb": "servir", "pronoun": "ella"},
            {"verb": "vestir", "pronoun": "usted"},
            {"verb": "elegir", "pronoun": "nosotros"},
            {"verb": "pedir", "pronoun": "nosotras"},
            {"verb": "repetir", "pronoun": "ellos"},
            {"verb": "seguir", "pronoun": "ellas"},
            {"verb": "servir", "pronoun": "ustedes"},
            ],
        },
        "opener_en": "What do you order at a restaurant?",
        "opener_es": "¿Qué pides en un restaurante?",
    },
    # --- GL 8: chat companion of `grammar_present_e_i_1` ---
    "grammar_present_e_i_1_chat": {
        "title": "Present E→I (1/3) — Chat",
        "grammar_level": 8,
        "lesson_number": 1.1,
        "lesson_type": "conjugation",
        "word_workload": ["pedir", "repetir", "seguir", "servir", "vestir", "elegir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Present E→I lesson 1', 'targets': [{'verb': 'pedir', 'pronoun': 'yo'}, {'verb': 'repetir', 'pronoun': 'tú'}, {'verb': 'seguir', 'pronoun': 'él'}, {'verb': 'servir', 'pronoun': 'ella'}, {'verb': 'vestir', 'pronoun': 'usted'}, {'verb': 'elegir', 'pronoun': 'nosotros'}, {'verb': 'pedir', 'pronoun': 'nosotras'}, {'verb': 'repetir', 'pronoun': 'ellos'}, {'verb': 'seguir', 'pronoun': 'ellas'}, {'verb': 'servir', 'pronoun': 'ustedes'}]},
    },
    "grammar_present_e_i_2": {
        "title": "Present E→I (2/3)",
        "grammar_level": 8,
        "lesson_number": 2,
        "lesson_type": "conjugation",
        "word_workload": ['pedir', 'repetir', 'seguir', 'servir', 'vestir', 'elegir'],
        "video_embed_id": "meS3lef4ubp",
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {"answers": {
            "pedir": {"yo": "pido", "tú": "pides", "él": "pide", "ella": "pide", "usted": "pide", "nosotros": "pedimos", "nosotras": "pedimos", "ellos": "piden", "ellas": "piden", "ustedes": "piden"},
            "repetir": {"yo": "repito", "tú": "repites", "él": "repite", "ella": "repite", "usted": "repite", "nosotros": "repetimos", "nosotras": "repetimos", "ellos": "repiten", "ellas": "repiten", "ustedes": "repiten"},
            "seguir": {"yo": "sigo", "tú": "sigues", "él": "sigue", "ella": "sigue", "usted": "sigue", "nosotros": "seguimos", "nosotras": "seguimos", "ellos": "siguen", "ellas": "siguen", "ustedes": "siguen"},
            "servir": {"yo": "sirvo", "tú": "sirves", "él": "sirve", "ella": "sirve", "usted": "sirve", "nosotros": "servimos", "nosotras": "servimos", "ellos": "sirven", "ellas": "sirven", "ustedes": "sirven"},
            "vestir": {"yo": "visto", "tú": "vistes", "él": "viste", "ella": "viste", "usted": "viste", "nosotros": "vestimos", "nosotras": "vestimos", "ellos": "visten", "ellas": "visten", "ustedes": "visten"},
            "elegir": {"yo": "elijo", "tú": "eliges", "él": "elige", "ella": "elige", "usted": "elige", "nosotros": "elegimos", "nosotras": "elegimos", "ellos": "eligen", "ellas": "eligen", "ustedes": "eligen"},
        }},
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You order the food", "es": "Tú pides la comida", "noun_id": "comida", "type": "written"},
            {"en": "I repeat the name", "es": "Yo repito el nombre", "noun_id": None, "type": "auditory"},
            {"en": "She follows the plan", "es": "Ella sigue el plan", "noun_id": None, "type": "written"},
            {"en": "He serves the water", "es": "Él sirve el agua", "noun_id": "agua", "type": "auditory"},
            {"en": "We dress for work", "es": "Nosotros vestimos para el trabajo", "noun_id": "trabajo", "type": "written"},
            {"en": "You choose the restaurant", "es": "Usted elige el restaurante", "noun_id": "restaurante", "type": "auditory"},
            {"en": "They order at the restaurant", "es": "Ellos piden en el restaurante", "noun_id": "restaurante", "type": "written"},
            {"en": "We (f) repeat every day", "es": "Nosotras repetimos cada día", "noun_id": None, "type": "auditory"},
            {"en": "You all continue on the road", "es": "Ustedes siguen en el camino", "noun_id": None, "type": "written"},
            {"en": "They (f) serve the food", "es": "Ellas sirven la comida", "noun_id": "comida", "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "pedir", "pronoun": "tú"},
            {"verb": "repetir", "pronoun": "yo"},
            {"verb": "seguir", "pronoun": "ella"},
            {"verb": "servir", "pronoun": "él"},
            {"verb": "vestir", "pronoun": "nosotros"},
            {"verb": "elegir", "pronoun": "usted"},
            {"verb": "pedir", "pronoun": "ellos"},
            {"verb": "repetir", "pronoun": "nosotras"},
            {"verb": "seguir", "pronoun": "ustedes"},
            {"verb": "servir", "pronoun": "ellas"},
        ],
        "phase_2_config": {
            "description": "Present E→I lesson 2",
            "targets": [
            {"verb": "pedir", "pronoun": "tú"},
            {"verb": "repetir", "pronoun": "yo"},
            {"verb": "seguir", "pronoun": "ella"},
            {"verb": "servir", "pronoun": "él"},
            {"verb": "vestir", "pronoun": "nosotros"},
            {"verb": "elegir", "pronoun": "usted"},
            {"verb": "pedir", "pronoun": "ellos"},
            {"verb": "repetir", "pronoun": "nosotras"},
            {"verb": "seguir", "pronoun": "ustedes"},
            {"verb": "servir", "pronoun": "ellas"},
            ],
        },
        "opener_en": "What does your friend usually order?",
        "opener_es": "¿Qué pide tu amiga normalmente?",
    },
    # --- GL 8: chat companion of `grammar_present_e_i_2` ---
    "grammar_present_e_i_2_chat": {
        "title": "Present E→I (2/3) — Chat",
        "grammar_level": 8,
        "lesson_number": 2.1,
        "lesson_type": "conjugation",
        "word_workload": ["pedir", "repetir", "seguir", "servir", "vestir", "elegir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Present E→I lesson 2', 'targets': [{'verb': 'pedir', 'pronoun': 'tú'}, {'verb': 'repetir', 'pronoun': 'yo'}, {'verb': 'seguir', 'pronoun': 'ella'}, {'verb': 'servir', 'pronoun': 'él'}, {'verb': 'vestir', 'pronoun': 'nosotros'}, {'verb': 'elegir', 'pronoun': 'usted'}, {'verb': 'pedir', 'pronoun': 'ellos'}, {'verb': 'repetir', 'pronoun': 'nosotras'}, {'verb': 'seguir', 'pronoun': 'ustedes'}, {'verb': 'servir', 'pronoun': 'ellas'}]},
    },
    "grammar_present_e_i_3": {
        "title": "Present E→I (3/3)",
        "grammar_level": 8,
        "lesson_number": 3,
        "lesson_type": "conjugation",
        "word_workload": ['pedir', 'repetir', 'seguir', 'servir', 'vestir', 'elegir'],
        "video_embed_id": "meS3lef4ubp",
        "drill_type": "conjugation",
        "tense": "present",
        "drill_config": {"answers": {
            "pedir": {"yo": "pido", "tú": "pides", "él": "pide", "ella": "pide", "usted": "pide", "nosotros": "pedimos", "nosotras": "pedimos", "ellos": "piden", "ellas": "piden", "ustedes": "piden"},
            "repetir": {"yo": "repito", "tú": "repites", "él": "repite", "ella": "repite", "usted": "repite", "nosotros": "repetimos", "nosotras": "repetimos", "ellos": "repiten", "ellas": "repiten", "ustedes": "repiten"},
            "seguir": {"yo": "sigo", "tú": "sigues", "él": "sigue", "ella": "sigue", "usted": "sigue", "nosotros": "seguimos", "nosotras": "seguimos", "ellos": "siguen", "ellas": "siguen", "ustedes": "siguen"},
            "servir": {"yo": "sirvo", "tú": "sirves", "él": "sirve", "ella": "sirve", "usted": "sirve", "nosotros": "servimos", "nosotras": "servimos", "ellos": "sirven", "ellas": "sirven", "ustedes": "sirven"},
            "vestir": {"yo": "visto", "tú": "vistes", "él": "viste", "ella": "viste", "usted": "viste", "nosotros": "vestimos", "nosotras": "vestimos", "ellos": "visten", "ellas": "visten", "ustedes": "visten"},
            "elegir": {"yo": "elijo", "tú": "eliges", "él": "elige", "ella": "elige", "usted": "elige", "nosotros": "elegimos", "nosotras": "elegimos", "ellos": "eligen", "ellas": "eligen", "ustedes": "eligen"},
        }},
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "He orders a coffee", "es": "Él pide un café", "noun_id": "café", "type": "written"},
            {"en": "She repeats the word", "es": "Ella repite la palabra", "noun_id": None, "type": "auditory"},
            {"en": "I continue working at home", "es": "Yo sigo trabajando en casa", "noun_id": "casa", "type": "written"},
            {"en": "You serve the customers", "es": "Tú sirves a los clientes", "noun_id": None, "type": "auditory"},
            {"en": "We (f) dress well for work", "es": "Nosotras vestimos bien para el trabajo", "noun_id": "trabajo", "type": "written"},
            {"en": "They choose the best restaurant", "es": "Ellos eligen el mejor restaurante", "noun_id": "restaurante", "type": "auditory"},
            {"en": "You ask for the book", "es": "Usted pide el libro", "noun_id": "libro", "type": "written"},
            {"en": "We repeat the Spanish words", "es": "Nosotros repetimos las palabras en español", "noun_id": None, "type": "auditory"},
            {"en": "They (f) dress the children", "es": "Ellas visten a los niños", "noun_id": None, "type": "written"},
            {"en": "You all choose the city", "es": "Ustedes eligen la ciudad", "noun_id": "ciudad", "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "pedir", "pronoun": "él"},
            {"verb": "repetir", "pronoun": "ella"},
            {"verb": "seguir", "pronoun": "yo"},
            {"verb": "servir", "pronoun": "tú"},
            {"verb": "vestir", "pronoun": "nosotras"},
            {"verb": "elegir", "pronoun": "ellos"},
            {"verb": "pedir", "pronoun": "usted"},
            {"verb": "repetir", "pronoun": "nosotros"},
            {"verb": "vestir", "pronoun": "ellas"},
            {"verb": "elegir", "pronoun": "ustedes"},
        ],
        "phase_2_config": {
            "description": "Present E→I lesson 3",
            "targets": [
            {"verb": "pedir", "pronoun": "él"},
            {"verb": "repetir", "pronoun": "ella"},
            {"verb": "seguir", "pronoun": "yo"},
            {"verb": "servir", "pronoun": "tú"},
            {"verb": "vestir", "pronoun": "nosotras"},
            {"verb": "elegir", "pronoun": "ellos"},
            {"verb": "pedir", "pronoun": "usted"},
            {"verb": "repetir", "pronoun": "nosotros"},
            {"verb": "vestir", "pronoun": "ellas"},
            {"verb": "elegir", "pronoun": "ustedes"},
            ],
        },
        "opener_en": "Do your kids choose their own clothes?",
        "opener_es": "¿Tus hijas eligen su ropa?",
    },
    # --- GL 8: chat companion of `grammar_present_e_i_3` ---
    "grammar_present_e_i_3_chat": {
        "title": "Present E→I (3/3) — Chat",
        "grammar_level": 8,
        "lesson_number": 3.1,
        "lesson_type": "conjugation",
        "word_workload": ["pedir", "repetir", "seguir", "servir", "vestir", "elegir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Present E→I lesson 3', 'targets': [{'verb': 'pedir', 'pronoun': 'él'}, {'verb': 'repetir', 'pronoun': 'ella'}, {'verb': 'seguir', 'pronoun': 'yo'}, {'verb': 'servir', 'pronoun': 'tú'}, {'verb': 'vestir', 'pronoun': 'nosotras'}, {'verb': 'elegir', 'pronoun': 'ellos'}, {'verb': 'pedir', 'pronoun': 'usted'}, {'verb': 'repetir', 'pronoun': 'nosotros'}, {'verb': 'vestir', 'pronoun': 'ellas'}, {'verb': 'elegir', 'pronoun': 'ustedes'}]},
    },
    # --- GL 9: Ir A + Infinitive — 3 lessons ---
    "grammar_ir_a_inf_1": {
        "title": "Ir A + Infinitive (1/3)",
        "grammar_level": 9,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ['hablar', 'comer', 'dormir', 'vivir', 'escribir', 'estudiar'],
        "video_embed_id": "geHPDI9tMdH",
        "drill_type": "ir_a_inf",
        "tense": "ir_a_infinitive",
        "drill_config": {"answers": {
            "hablar": {"yo": "voy a hablar", "tú": "vas a hablar", "él": "va a hablar", "ella": "va a hablar", "usted": "va a hablar", "nosotros": "vamos a hablar", "nosotras": "vamos a hablar", "ellos": "van a hablar", "ellas": "van a hablar", "ustedes": "van a hablar"},
            "comer": {"yo": "voy a comer", "tú": "vas a comer", "él": "va a comer", "ella": "va a comer", "usted": "va a comer", "nosotros": "vamos a comer", "nosotras": "vamos a comer", "ellos": "van a comer", "ellas": "van a comer", "ustedes": "van a comer"},
            "dormir": {"yo": "voy a dormir", "tú": "vas a dormir", "él": "va a dormir", "ella": "va a dormir", "usted": "va a dormir", "nosotros": "vamos a dormir", "nosotras": "vamos a dormir", "ellos": "van a dormir", "ellas": "van a dormir", "ustedes": "van a dormir"},
            "vivir": {"yo": "voy a vivir", "tú": "vas a vivir", "él": "va a vivir", "ella": "va a vivir", "usted": "va a vivir", "nosotros": "vamos a vivir", "nosotras": "vamos a vivir", "ellos": "van a vivir", "ellas": "van a vivir", "ustedes": "van a vivir"},
            "escribir": {"yo": "voy a escribir", "tú": "vas a escribir", "él": "va a escribir", "ella": "va a escribir", "usted": "va a escribir", "nosotros": "vamos a escribir", "nosotras": "vamos a escribir", "ellos": "van a escribir", "ellas": "van a escribir", "ustedes": "van a escribir"},
            "estudiar": {"yo": "voy a estudiar", "tú": "vas a estudiar", "él": "va a estudiar", "ella": "va a estudiar", "usted": "va a estudiar", "nosotros": "vamos a estudiar", "nosotras": "vamos a estudiar", "ellos": "van a estudiar", "ellas": "van a estudiar", "ustedes": "van a estudiar"},
        }},
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I am going to speak Spanish", "es": "Voy a hablar español", "noun_id": None, "type": "written"},
            {"en": "You are going to eat", "es": "Vas a comer", "noun_id": None, "type": "auditory"},
            {"en": "He is going to sleep", "es": "Él va a dormir", "noun_id": None, "type": "written"},
            {"en": "She is going to live here", "es": "Ella va a vivir aquí", "noun_id": None, "type": "auditory"},
            {"en": "You are going to write a letter", "es": "Usted va a escribir una carta", "noun_id": "carta", "type": "written"},
            {"en": "We are going to study", "es": "Nosotros vamos a estudiar", "noun_id": None, "type": "auditory"},
            {"en": "We (f) are going to speak Spanish", "es": "Nosotras vamos a hablar español", "noun_id": None, "type": "written"},
            {"en": "They are going to eat", "es": "Ellos van a comer", "noun_id": None, "type": "auditory"},
            {"en": "They (f) are going to sleep", "es": "Ellas van a dormir", "noun_id": None, "type": "written"},
            {"en": "You all are going to live here", "es": "Ustedes van a vivir aquí", "noun_id": None, "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "hablar", "pronoun": "yo"},
            {"verb": "comer", "pronoun": "tú"},
            {"verb": "dormir", "pronoun": "él"},
            {"verb": "vivir", "pronoun": "ella"},
            {"verb": "escribir", "pronoun": "usted"},
            {"verb": "estudiar", "pronoun": "nosotros"},
            {"verb": "hablar", "pronoun": "nosotras"},
            {"verb": "comer", "pronoun": "ellos"},
            {"verb": "dormir", "pronoun": "ellas"},
            {"verb": "vivir", "pronoun": "ustedes"},
        ],
        "phase_2_config": {
            "description": "Ir A + Infinitive lesson 1",
            "targets": [
            {"verb": "hablar", "pronoun": "yo"},
            {"verb": "comer", "pronoun": "tú"},
            {"verb": "dormir", "pronoun": "él"},
            {"verb": "vivir", "pronoun": "ella"},
            {"verb": "escribir", "pronoun": "usted"},
            {"verb": "estudiar", "pronoun": "nosotros"},
            {"verb": "hablar", "pronoun": "nosotras"},
            {"verb": "comer", "pronoun": "ellos"},
            {"verb": "dormir", "pronoun": "ellas"},
            {"verb": "vivir", "pronoun": "ustedes"},
            ],
        },
        "opener_en": "What are you going to eat today?",
        "opener_es": "¿Qué vas a comer hoy?",
    },
    # --- GL 9: chat companion of `grammar_ir_a_inf_1` ---
    "grammar_ir_a_inf_1_chat": {
        "title": "Ir A + Infinitive (1/3) — Chat",
        "grammar_level": 9,
        "lesson_number": 1.1,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "comer", "dormir", "vivir", "escribir", "estudiar"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "ir_a_infinitive",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Ir A + Infinitive lesson 1', 'targets': [{'verb': 'hablar', 'pronoun': 'yo'}, {'verb': 'comer', 'pronoun': 'tú'}, {'verb': 'dormir', 'pronoun': 'él'}, {'verb': 'vivir', 'pronoun': 'ella'}, {'verb': 'escribir', 'pronoun': 'usted'}, {'verb': 'estudiar', 'pronoun': 'nosotros'}, {'verb': 'hablar', 'pronoun': 'nosotras'}, {'verb': 'comer', 'pronoun': 'ellos'}, {'verb': 'dormir', 'pronoun': 'ellas'}, {'verb': 'vivir', 'pronoun': 'ustedes'}]},
    },
    "grammar_ir_a_inf_2": {
        "title": "Ir A + Infinitive (2/3)",
        "grammar_level": 9,
        "lesson_number": 2,
        "lesson_type": "conjugation",
        "word_workload": ['hablar', 'comer', 'dormir', 'vivir', 'escribir', 'estudiar'],
        "video_embed_id": "geHPDI9tMdH",
        "drill_type": "ir_a_inf",
        "tense": "ir_a_infinitive",
        "drill_config": {"answers": {
            "hablar": {"yo": "voy a hablar", "tú": "vas a hablar", "él": "va a hablar", "ella": "va a hablar", "usted": "va a hablar", "nosotros": "vamos a hablar", "nosotras": "vamos a hablar", "ellos": "van a hablar", "ellas": "van a hablar", "ustedes": "van a hablar"},
            "comer": {"yo": "voy a comer", "tú": "vas a comer", "él": "va a comer", "ella": "va a comer", "usted": "va a comer", "nosotros": "vamos a comer", "nosotras": "vamos a comer", "ellos": "van a comer", "ellas": "van a comer", "ustedes": "van a comer"},
            "dormir": {"yo": "voy a dormir", "tú": "vas a dormir", "él": "va a dormir", "ella": "va a dormir", "usted": "va a dormir", "nosotros": "vamos a dormir", "nosotras": "vamos a dormir", "ellos": "van a dormir", "ellas": "van a dormir", "ustedes": "van a dormir"},
            "vivir": {"yo": "voy a vivir", "tú": "vas a vivir", "él": "va a vivir", "ella": "va a vivir", "usted": "va a vivir", "nosotros": "vamos a vivir", "nosotras": "vamos a vivir", "ellos": "van a vivir", "ellas": "van a vivir", "ustedes": "van a vivir"},
            "escribir": {"yo": "voy a escribir", "tú": "vas a escribir", "él": "va a escribir", "ella": "va a escribir", "usted": "va a escribir", "nosotros": "vamos a escribir", "nosotras": "vamos a escribir", "ellos": "van a escribir", "ellas": "van a escribir", "ustedes": "van a escribir"},
            "estudiar": {"yo": "voy a estudiar", "tú": "vas a estudiar", "él": "va a estudiar", "ella": "va a estudiar", "usted": "va a estudiar", "nosotros": "vamos a estudiar", "nosotras": "vamos a estudiar", "ellos": "van a estudiar", "ellas": "van a estudiar", "ustedes": "van a estudiar"},
        }},
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You are going to speak Spanish", "es": "Tú vas a hablar español", "noun_id": None, "type": "written"},
            {"en": "I am going to eat lunch", "es": "Yo voy a comer", "noun_id": None, "type": "auditory"},
            {"en": "She is going to sleep", "es": "Ella va a dormir", "noun_id": None, "type": "written"},
            {"en": "He is going to live here", "es": "Él va a vivir aquí", "noun_id": None, "type": "auditory"},
            {"en": "We are going to write a letter", "es": "Nosotros vamos a escribir una carta", "noun_id": "carta", "type": "written"},
            {"en": "You are going to study", "es": "Usted va a estudiar", "noun_id": None, "type": "auditory"},
            {"en": "They are going to speak Spanish", "es": "Ellos van a hablar español", "noun_id": None, "type": "written"},
            {"en": "We (f) are going to eat", "es": "Nosotras vamos a comer", "noun_id": None, "type": "auditory"},
            {"en": "You all are going to sleep", "es": "Ustedes van a dormir", "noun_id": None, "type": "written"},
            {"en": "They (f) are going to live here", "es": "Ellas van a vivir aquí", "noun_id": None, "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "hablar", "pronoun": "tú"},
            {"verb": "comer", "pronoun": "yo"},
            {"verb": "dormir", "pronoun": "ella"},
            {"verb": "vivir", "pronoun": "él"},
            {"verb": "escribir", "pronoun": "nosotros"},
            {"verb": "estudiar", "pronoun": "usted"},
            {"verb": "hablar", "pronoun": "ellos"},
            {"verb": "comer", "pronoun": "nosotras"},
            {"verb": "dormir", "pronoun": "ustedes"},
            {"verb": "vivir", "pronoun": "ellas"},
        ],
        "phase_2_config": {
            "description": "Ir A + Infinitive lesson 2",
            "targets": [
            {"verb": "hablar", "pronoun": "tú"},
            {"verb": "comer", "pronoun": "yo"},
            {"verb": "dormir", "pronoun": "ella"},
            {"verb": "vivir", "pronoun": "él"},
            {"verb": "escribir", "pronoun": "nosotros"},
            {"verb": "estudiar", "pronoun": "usted"},
            {"verb": "hablar", "pronoun": "ellos"},
            {"verb": "comer", "pronoun": "nosotras"},
            {"verb": "dormir", "pronoun": "ustedes"},
            {"verb": "vivir", "pronoun": "ellas"},
            ],
        },
        "opener_en": "Where is your family going to live?",
        "opener_es": "¿Dónde va a vivir tu familia?",
    },
    # --- GL 9: chat companion of `grammar_ir_a_inf_2` ---
    "grammar_ir_a_inf_2_chat": {
        "title": "Ir A + Infinitive (2/3) — Chat",
        "grammar_level": 9,
        "lesson_number": 2.1,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "comer", "dormir", "vivir", "escribir", "estudiar"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "ir_a_infinitive",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Ir A + Infinitive lesson 2', 'targets': [{'verb': 'hablar', 'pronoun': 'tú'}, {'verb': 'comer', 'pronoun': 'yo'}, {'verb': 'dormir', 'pronoun': 'ella'}, {'verb': 'vivir', 'pronoun': 'él'}, {'verb': 'escribir', 'pronoun': 'nosotros'}, {'verb': 'estudiar', 'pronoun': 'usted'}, {'verb': 'hablar', 'pronoun': 'ellos'}, {'verb': 'comer', 'pronoun': 'nosotras'}, {'verb': 'dormir', 'pronoun': 'ustedes'}, {'verb': 'vivir', 'pronoun': 'ellas'}]},
    },
    "grammar_ir_a_inf_3": {
        "title": "Ir A + Infinitive (3/3)",
        "grammar_level": 9,
        "lesson_number": 3,
        "lesson_type": "conjugation",
        "word_workload": ['hablar', 'comer', 'dormir', 'vivir', 'escribir', 'estudiar'],
        "video_embed_id": "geHPDI9tMdH",
        "drill_type": "ir_a_inf",
        "tense": "ir_a_infinitive",
        "drill_config": {"answers": {
            "hablar": {"yo": "voy a hablar", "tú": "vas a hablar", "él": "va a hablar", "ella": "va a hablar", "usted": "va a hablar", "nosotros": "vamos a hablar", "nosotras": "vamos a hablar", "ellos": "van a hablar", "ellas": "van a hablar", "ustedes": "van a hablar"},
            "comer": {"yo": "voy a comer", "tú": "vas a comer", "él": "va a comer", "ella": "va a comer", "usted": "va a comer", "nosotros": "vamos a comer", "nosotras": "vamos a comer", "ellos": "van a comer", "ellas": "van a comer", "ustedes": "van a comer"},
            "dormir": {"yo": "voy a dormir", "tú": "vas a dormir", "él": "va a dormir", "ella": "va a dormir", "usted": "va a dormir", "nosotros": "vamos a dormir", "nosotras": "vamos a dormir", "ellos": "van a dormir", "ellas": "van a dormir", "ustedes": "van a dormir"},
            "vivir": {"yo": "voy a vivir", "tú": "vas a vivir", "él": "va a vivir", "ella": "va a vivir", "usted": "va a vivir", "nosotros": "vamos a vivir", "nosotras": "vamos a vivir", "ellos": "van a vivir", "ellas": "van a vivir", "ustedes": "van a vivir"},
            "escribir": {"yo": "voy a escribir", "tú": "vas a escribir", "él": "va a escribir", "ella": "va a escribir", "usted": "va a escribir", "nosotros": "vamos a escribir", "nosotras": "vamos a escribir", "ellos": "van a escribir", "ellas": "van a escribir", "ustedes": "van a escribir"},
            "estudiar": {"yo": "voy a estudiar", "tú": "vas a estudiar", "él": "va a estudiar", "ella": "va a estudiar", "usted": "va a estudiar", "nosotros": "vamos a estudiar", "nosotras": "vamos a estudiar", "ellos": "van a estudiar", "ellas": "van a estudiar", "ustedes": "van a estudiar"},
        }},
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "He is going to speak Spanish", "es": "Él va a hablar español", "noun_id": None, "type": "written"},
            {"en": "She is going to eat", "es": "Ella va a comer", "noun_id": None, "type": "auditory"},
            {"en": "I am going to sleep", "es": "Yo voy a dormir", "noun_id": None, "type": "written"},
            {"en": "You are going to live here", "es": "Tú vas a vivir aquí", "noun_id": None, "type": "auditory"},
            {"en": "We (f) are going to write a book", "es": "Nosotras vamos a escribir un libro", "noun_id": "libro", "type": "written"},
            {"en": "They are going to study", "es": "Ellos van a estudiar", "noun_id": None, "type": "auditory"},
            {"en": "You are going to speak Spanish", "es": "Usted va a hablar español", "noun_id": None, "type": "written"},
            {"en": "We are going to eat", "es": "Nosotros vamos a comer", "noun_id": None, "type": "auditory"},
            {"en": "They (f) are going to write", "es": "Ellas van a escribir", "noun_id": None, "type": "written"},
            {"en": "You all are going to study", "es": "Ustedes van a estudiar", "noun_id": None, "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "hablar", "pronoun": "él"},
            {"verb": "comer", "pronoun": "ella"},
            {"verb": "dormir", "pronoun": "yo"},
            {"verb": "vivir", "pronoun": "tú"},
            {"verb": "escribir", "pronoun": "nosotras"},
            {"verb": "estudiar", "pronoun": "ellos"},
            {"verb": "hablar", "pronoun": "usted"},
            {"verb": "comer", "pronoun": "nosotros"},
            {"verb": "escribir", "pronoun": "ellas"},
            {"verb": "estudiar", "pronoun": "ustedes"},
        ],
        "phase_2_config": {
            "description": "Ir A + Infinitive lesson 3",
            "targets": [
            {"verb": "hablar", "pronoun": "él"},
            {"verb": "comer", "pronoun": "ella"},
            {"verb": "dormir", "pronoun": "yo"},
            {"verb": "vivir", "pronoun": "tú"},
            {"verb": "escribir", "pronoun": "nosotras"},
            {"verb": "estudiar", "pronoun": "ellos"},
            {"verb": "hablar", "pronoun": "usted"},
            {"verb": "comer", "pronoun": "nosotros"},
            {"verb": "escribir", "pronoun": "ellas"},
            {"verb": "estudiar", "pronoun": "ustedes"},
            ],
        },
        "opener_en": "Are your friends going to study too?",
        "opener_es": "¿Tus amigas van a estudiar también?",
    },
    # --- GL 9: chat companion of `grammar_ir_a_inf_3` ---
    "grammar_ir_a_inf_3_chat": {
        "title": "Ir A + Infinitive (3/3) — Chat",
        "grammar_level": 9,
        "lesson_number": 3.1,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "comer", "dormir", "vivir", "escribir", "estudiar"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "ir_a_infinitive",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Ir A + Infinitive lesson 3', 'targets': [{'verb': 'hablar', 'pronoun': 'él'}, {'verb': 'comer', 'pronoun': 'ella'}, {'verb': 'dormir', 'pronoun': 'yo'}, {'verb': 'vivir', 'pronoun': 'tú'}, {'verb': 'escribir', 'pronoun': 'nosotras'}, {'verb': 'estudiar', 'pronoun': 'ellos'}, {'verb': 'hablar', 'pronoun': 'usted'}, {'verb': 'comer', 'pronoun': 'nosotros'}, {'verb': 'escribir', 'pronoun': 'ellas'}, {'verb': 'estudiar', 'pronoun': 'ustedes'}]},
    },
    "grammar_gustar_1": {
        "title": "Gustar Part 1",
        "grammar_level": 10,
        "word_workload": ["gusta"],
        "video_embed_id": "rfPPtJI9prc",
        "drill_type": "gustar",
        "tense": "gustar",
        "drill_config": {
        "items": [
                {
                        "prompt": "I like (el café)",
                        "answer": "me gusta",
                        "hint": "me"
                },
                {
                        "prompt": "You like (la música)",
                        "answer": "te gusta",
                        "hint": "te"
                },
                {
                        "prompt": "He likes (el libro)",
                        "answer": "le gusta",
                        "hint": "le"
                },
                {
                        "prompt": "She likes (la película)",
                        "answer": "le gusta",
                        "hint": "le"
                },
                {
                        "prompt": "We like (el chocolate)",
                        "answer": "nos gusta",
                        "hint": "nos"
                },
                {
                        "prompt": "We like (la playa)",
                        "answer": "nos gusta",
                        "hint": "nos"
                },
                {
                        "prompt": "They like (el fútbol)",
                        "answer": "les gusta",
                        "hint": "les"
                },
                {
                        "prompt": "They like (la comida)",
                        "answer": "les gusta",
                        "hint": "les"
                },
                {
                        "prompt": "You (formal) like (el té)",
                        "answer": "le gusta",
                        "hint": "le"
                },
                {
                        "prompt": "I like (la fruta)",
                        "answer": "me gusta",
                        "hint": "me"
                },
                {
                        "prompt": "You like (el cine)",
                        "answer": "te gusta",
                        "hint": "te"
                },
                {
                        "prompt": "They like (la ciudad)",
                        "answer": "les gusta",
                        "hint": "les"
                }
        ]
},
        "lesson_type": "rule",
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "gustar_singular"},
        "drill_sentences": [
            {"en": "I like the coffee", "es": "Me gusta el café", "noun_id": "café", "type": "written"},
            {"en": "You like the music", "es": "Te gusta la música", "noun_id": None, "type": "auditory"},
            {"en": "She likes the book", "es": "Le gusta el libro", "noun_id": "libro", "type": "written"},
            {"en": "He likes the water", "es": "Le gusta el agua", "noun_id": "agua", "type": "auditory"},
            {"en": "You (formal) like the food", "es": "Le gusta la comida", "noun_id": "comida", "type": "written"},
            {"en": "We like the plan", "es": "Nos gusta el plan", "noun_id": None, "type": "auditory"},
            {"en": "They like the park", "es": "Les gusta el parque", "noun_id": "parque", "type": "written"},
            {"en": "I like the dog", "es": "Me gusta el perro", "noun_id": "perro", "type": "auditory"},
            {"en": "You like the city", "es": "Te gusta la ciudad", "noun_id": "ciudad", "type": "written"},
            {"en": "She likes the house", "es": "Le gusta la casa", "noun_id": "casa", "type": "auditory"},
        ],
        "phase_2_config": {
            "description": "5 pronoun+gusta+noun combos",
            "targets": 5,
            "pattern": "pronoun_gusta_singular",
        },
    },
    # --- GL 10: chat companion of `grammar_gustar_1` ---
    "grammar_gustar_1_chat": {
        "title": "Gustar Part 1 — Chat",
        "grammar_level": 10,
        "lesson_number": 1.1,
        "lesson_type": "rule",
        "word_workload": ["gusta"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "gustar",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': '5 pronoun+gusta+noun combos', 'targets': 5, 'pattern': 'pronoun_gusta_singular'},
    },
    "grammar_gustar_2": {
        "title": "Gustar Part 2",
        "grammar_level": 10.3,
        "word_workload": ["gustan"],
        "video_embed_id": "WjOxPPu1uQo",
        "drill_type": "gustar",
        "tense": "gustar",
        "drill_config": {
        "items": [
                {
                        "prompt": "I like (los gatos)",
                        "answer": "me gustan",
                        "hint": "me"
                },
                {
                        "prompt": "I like (las manzanas)",
                        "answer": "me gustan",
                        "hint": "me"
                },
                {
                        "prompt": "You like (los libros)",
                        "answer": "te gustan",
                        "hint": "te"
                },
                {
                        "prompt": "You like (las flores)",
                        "answer": "te gustan",
                        "hint": "te"
                },
                {
                        "prompt": "He/She likes (los perros)",
                        "answer": "le gustan",
                        "hint": "le"
                },
                {
                        "prompt": "He/She likes (las películas)",
                        "answer": "le gustan",
                        "hint": "le"
                },
                {
                        "prompt": "We like (los coches)",
                        "answer": "nos gustan",
                        "hint": "nos"
                },
                {
                        "prompt": "We like (las canciones)",
                        "answer": "nos gustan",
                        "hint": "nos"
                },
                {
                        "prompt": "They like (los deportes)",
                        "answer": "les gustan",
                        "hint": "les"
                },
                {
                        "prompt": "They like (las frutas)",
                        "answer": "les gustan",
                        "hint": "les"
                },
                {
                        "prompt": "You all like (los árboles)",
                        "answer": "les gustan",
                        "hint": "les"
                },
                {
                        "prompt": "You all like (las montañas)",
                        "answer": "les gustan",
                        "hint": "les"
                }
        ]
},
        "lesson_type": "rule",
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "gustar_plural"},
        "drill_sentences": [
            {"en": "I like the cats", "es": "Me gustan los gatos", "noun_id": "gato", "type": "written"},
            {"en": "You like the books", "es": "Te gustan los libros", "noun_id": "libro", "type": "auditory"},
            {"en": "She likes the dogs", "es": "Le gustan los perros", "noun_id": "perro", "type": "written"},
            {"en": "He likes the cars", "es": "Le gustan los carros", "noun_id": "carro", "type": "auditory"},
            {"en": "We like the movies", "es": "Nos gustan las películas", "noun_id": None, "type": "written"},
            {"en": "They like the parks", "es": "Les gustan los parques", "noun_id": "parque", "type": "auditory"},
            {"en": "You all like the beaches", "es": "Les gustan las playas", "noun_id": "playa", "type": "written"},
            {"en": "I like the cities", "es": "Me gustan las ciudades", "noun_id": "ciudad", "type": "auditory"},
            {"en": "You like the colors", "es": "Te gustan los colores", "noun_id": "color", "type": "written"},
            {"en": "She likes the houses", "es": "Le gustan las casas", "noun_id": "casa", "type": "auditory"},
        ],
        "phase_2_config": {
            "description": "5 pronoun+gustan+noun combos",
            "targets": 5,
            "pattern": "pronoun_gustan_plural",
        },
    },
    # --- GL 10.3: chat companion of `grammar_gustar_2` ---
    "grammar_gustar_2_chat": {
        "title": "Gustar Part 2 — Chat",
        "grammar_level": 10.3,
        "lesson_number": 1.1,
        "lesson_type": "rule",
        "word_workload": ["gustan"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "gustar",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': '5 pronoun+gustan+noun combos', 'targets': 5, 'pattern': 'pronoun_gustan_plural'},
    },
    "grammar_gustar_3": {
        "title": "Gustar Part 3",
        "grammar_level": 10.6,
        "word_workload": ["gusta", "gustan"],
        "video_embed_id": "lIAdqI5fpun",
        "drill_type": "gustar_prefix",
        "tense": "gustar",
        "drill_config": {
        "items": [
                {
                        "prompt": "me gusta el gato",
                        "answer": "a mí",
                        "hint": "a mí"
                },
                {
                        "prompt": "te gusta la música",
                        "answer": "a ti",
                        "hint": "a ti"
                },
                {
                        "prompt": "le gusta el fútbol",
                        "answer": "a él",
                        "hint": "a él"
                },
                {
                        "prompt": "le gusta la playa",
                        "answer": "a ella",
                        "hint": "a ella"
                },
                {
                        "prompt": "le gusta el libro",
                        "answer": "a usted",
                        "hint": "a usted"
                },
                {
                        "prompt": "nos gusta la pizza",
                        "answer": "a nosotros",
                        "hint": "a nosotros"
                },
                {
                        "prompt": "les gusta el cine",
                        "answer": "a ellos",
                        "hint": "a ellos"
                },
                {
                        "prompt": "les gusta la clase",
                        "answer": "a ustedes",
                        "hint": "a ustedes"
                },
                {
                        "prompt": "me gusta bailar",
                        "answer": "a mí",
                        "hint": "a mí"
                },
                {
                        "prompt": "te gusta correr",
                        "answer": "a ti",
                        "hint": "a ti"
                },
                {
                        "prompt": "le gusta viajar",
                        "answer": "a ella",
                        "hint": "a ella"
                },
                {
                        "prompt": "les gusta estudiar",
                        "answer": "a ellos",
                        "hint": "a ellos"
                }
        ]
},
        "lesson_type": "rule",
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "gustar_prefix"},
        "drill_sentences": [
            {"en": "I like the coffee (emphatic)", "es": "A mí me gusta el café", "noun_id": "café", "type": "written"},
            {"en": "You like the music (emphatic)", "es": "A ti te gusta la música", "noun_id": None, "type": "auditory"},
            {"en": "He likes the book (emphatic)", "es": "A él le gusta el libro", "noun_id": "libro", "type": "written"},
            {"en": "She likes the water (emphatic)", "es": "A ella le gusta el agua", "noun_id": "agua", "type": "auditory"},
            {"en": "You (formal) like the food (emphatic)", "es": "A usted le gusta la comida", "noun_id": "comida", "type": "written"},
            {"en": "We like the park (emphatic)", "es": "A nosotros nos gusta el parque", "noun_id": "parque", "type": "auditory"},
            {"en": "They like the dog (emphatic)", "es": "A ellos les gusta el perro", "noun_id": "perro", "type": "written"},
            {"en": "You all like the city (emphatic)", "es": "A ustedes les gusta la ciudad", "noun_id": "ciudad", "type": "auditory"},
            {"en": "I like the house (emphatic)", "es": "A mí me gusta la casa", "noun_id": "casa", "type": "written"},
            {"en": "She likes the car (emphatic)", "es": "A ella le gusta el carro", "noun_id": "carro", "type": "auditory"},
        ],
        "phase_2_config": {
            "description": "1 per pronoun type (10 total)",
            "targets": 10,
            "pattern": "a_prefix",
        },
    },
    # --- GL 10.6: chat companion of `grammar_gustar_3` ---
    "grammar_gustar_3_chat": {
        "title": "Gustar Part 3 — Chat",
        "grammar_level": 10.6,
        "lesson_number": 1.1,
        "lesson_type": "rule",
        "word_workload": ["gusta", "gustan"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "gustar",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': '1 per pronoun type (10 total)', 'targets': 10, 'pattern': 'a_prefix'},
    },
    # --- GL 13.5: Imperatives — 2 lessons ---
    "grammar_imperatives_1": {
        "title": "Imperatives (1/2)",
        "grammar_level": 13.5,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "comer", "vivir"],
        "video_embed_id": None,
        "drill_type": "conjugation",
        "tense": "imperative",
        "drill_config": {"answers": {
            "hablar": {"tú": "habla", "usted": "hable", "nosotros": "hablemos", "vosotros": "hablad", "ustedes": "hablen"},
            "comer": {"tú": "come", "usted": "coma", "nosotros": "comamos", "vosotros": "comed", "ustedes": "coman"},
            "vivir": {"tú": "vive", "usted": "viva", "nosotros": "vivamos", "vosotros": "vivid", "ustedes": "vivan"},
        }},
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "Speak slowly (tú)", "es": "Habla despacio", "noun_id": None, "type": "written"},
            {"en": "Speak here (usted)", "es": "Hable aquí", "noun_id": None, "type": "auditory"},
            {"en": "Let's speak now (nosotros)", "es": "Hablemos ahora", "noun_id": None, "type": "written"},
            {"en": "Eat the bread (tú)", "es": "Come el pan", "noun_id": "pan", "type": "auditory"},
            {"en": "Eat the food (usted)", "es": "Coma la comida", "noun_id": "comida", "type": "written"},
            {"en": "Let's eat together (nosotros)", "es": "Comamos juntos", "noun_id": None, "type": "auditory"},
            {"en": "You all eat now (ustedes)", "es": "Coman ahora", "noun_id": None, "type": "written"},
            {"en": "Live well (tú)", "es": "Vive bien", "noun_id": None, "type": "auditory"},
            {"en": "Live here (usted)", "es": "Viva aquí", "noun_id": None, "type": "written"},
            {"en": "Let's live well (nosotros)", "es": "Vivamos bien", "noun_id": None, "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "hablar", "pronoun": "tú"},
            {"verb": "hablar", "pronoun": "usted"},
            {"verb": "hablar", "pronoun": "nosotros"},
            {"verb": "comer", "pronoun": "tú"},
            {"verb": "comer", "pronoun": "usted"},
            {"verb": "comer", "pronoun": "nosotros"},
            {"verb": "comer", "pronoun": "ustedes"},
            {"verb": "vivir", "pronoun": "tú"},
            {"verb": "vivir", "pronoun": "usted"},
            {"verb": "vivir", "pronoun": "nosotros"},
        ],
        "phase_2_config": {
            "description": "Imperatives lesson 1: hablar, comer, vivir (tú/usted/nosotros commands)",
            "targets": [
                {"verb": "hablar", "pronoun": "tú"},
                {"verb": "hablar", "pronoun": "usted"},
                {"verb": "comer", "pronoun": "tú"},
                {"verb": "comer", "pronoun": "usted"},
                {"verb": "vivir", "pronoun": "tú"},
                {"verb": "vivir", "pronoun": "usted"},
            ],
        },
        "opener_en": "Can you tell me where to go?",
        "opener_es": "¿Me puedes decir adónde ir?",
    },
    # --- GL 13.5: chat companion of `grammar_imperatives_1` ---
    "grammar_imperatives_1_chat": {
        "title": "Imperatives (1/2) — Chat",
        "grammar_level": 13.5,
        "lesson_number": 1.1,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "comer", "vivir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "imperative",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Imperatives lesson 1: hablar, comer, vivir (tú/usted/nosotros commands)', 'targets': [{'verb': 'hablar', 'pronoun': 'tú'}, {'verb': 'hablar', 'pronoun': 'usted'}, {'verb': 'comer', 'pronoun': 'tú'}, {'verb': 'comer', 'pronoun': 'usted'}, {'verb': 'vivir', 'pronoun': 'tú'}, {'verb': 'vivir', 'pronoun': 'usted'}]},
    },
    "grammar_imperatives_2": {
        "title": "Imperatives (2/2)",
        "grammar_level": 13.5,
        "lesson_number": 2,
        "lesson_type": "conjugation",
        "word_workload": ["ir", "ser", "tener"],
        "video_embed_id": None,
        "drill_type": "conjugation",
        "tense": "imperative",
        "drill_config": {"answers": {
            "ir": {"tú": "ve", "usted": "vaya", "nosotros": "vamos", "ustedes": "vayan"},
            "ser": {"tú": "sé", "usted": "sea", "nosotros": "seamos", "ustedes": "sean"},
            "tener": {"tú": "ten", "usted": "tenga", "nosotros": "tengamos", "ustedes": "tengan"},
        }},
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "Go now (tú)", "es": "Ve ahora", "noun_id": None, "type": "written"},
            {"en": "Go to the park (usted)", "es": "Vaya al parque", "noun_id": "parque", "type": "auditory"},
            {"en": "Let's go (nosotros)", "es": "Vamos", "noun_id": None, "type": "written"},
            {"en": "You all go now (ustedes)", "es": "Vayan ahora", "noun_id": None, "type": "auditory"},
            {"en": "Be calm (tú)", "es": "Sé tranquilo", "noun_id": None, "type": "written"},
            {"en": "Be here (usted)", "es": "Sea aquí", "noun_id": None, "type": "auditory"},
            {"en": "Let's be calm (nosotros)", "es": "Seamos tranquilos", "noun_id": None, "type": "written"},
            {"en": "Have the book (tú)", "es": "Ten el libro", "noun_id": "libro", "type": "auditory"},
            {"en": "Have patience (usted)", "es": "Tenga paciencia", "noun_id": None, "type": "written"},
            {"en": "You all have the plan (ustedes)", "es": "Tengan el plan", "noun_id": None, "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "ir", "pronoun": "tú"},
            {"verb": "ir", "pronoun": "usted"},
            {"verb": "ir", "pronoun": "nosotros"},
            {"verb": "ir", "pronoun": "ustedes"},
            {"verb": "ser", "pronoun": "tú"},
            {"verb": "ser", "pronoun": "usted"},
            {"verb": "ser", "pronoun": "nosotros"},
            {"verb": "tener", "pronoun": "tú"},
            {"verb": "tener", "pronoun": "usted"},
            {"verb": "tener", "pronoun": "ustedes"},
        ],
        "phase_2_config": {
            "description": "Imperatives lesson 2: ir, ser, tener (tú/usted/ustedes commands)",
            "targets": [
                {"verb": "ir", "pronoun": "tú"},
                {"verb": "ir", "pronoun": "usted"},
                {"verb": "ser", "pronoun": "tú"},
                {"verb": "ser", "pronoun": "usted"},
                {"verb": "tener", "pronoun": "tú"},
                {"verb": "tener", "pronoun": "usted"},
            ],
        },
        "opener_en": "Go ahead, tell me what you need.",
        "opener_es": "Ve, dime lo que necesitas.",
    },
    # --- GL 13.5: chat companion of `grammar_imperatives_2` ---
    "grammar_imperatives_2_chat": {
        "title": "Imperatives (2/2) — Chat",
        "grammar_level": 13.5,
        "lesson_number": 2.1,
        "lesson_type": "conjugation",
        "word_workload": ["ir", "ser", "tener"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "imperative",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Imperatives lesson 2: ir, ser, tener (tú/usted/ustedes commands)', 'targets': [{'verb': 'ir', 'pronoun': 'tú'}, {'verb': 'ir', 'pronoun': 'usted'}, {'verb': 'ser', 'pronoun': 'tú'}, {'verb': 'ser', 'pronoun': 'usted'}, {'verb': 'tener', 'pronoun': 'tú'}, {'verb': 'tener', 'pronoun': 'usted'}]},
    },
    # --- GL 17: Preterite Regular — 3 lessons ---
    "grammar_preterite_regular_1": {
        "title": "Preterite Regular (1/3)",
        "grammar_level": 17,
        "lesson_number": 1,
        "word_workload": ['hablar', 'encontrar', 'comer', 'unir', 'beber', 'salir'],
        "video_embed_id": "uBOH6A3vO0U",
        "drill_type": "conjugation",
        "tense": "preterite",
        "drill_config": {"answers": {
            "hablar": {"yo": "hablé", "tú": "hablaste", "él": "habló", "ella": "habló", "usted": "habló", "nosotros": "hablamos", "nosotras": "hablamos", "ellos": "hablaron", "ellas": "hablaron", "ustedes": "hablaron"},
            "encontrar": {"yo": "encontré", "tú": "encontraste", "él": "encontró", "ella": "encontró", "usted": "encontró", "nosotros": "encontramos", "nosotras": "encontramos", "ellos": "encontraron", "ellas": "encontraron", "ustedes": "encontraron"},
            "comer": {"yo": "comí", "tú": "comiste", "él": "comió", "ella": "comió", "usted": "comió", "nosotros": "comimos", "nosotras": "comimos", "ellos": "comieron", "ellas": "comieron", "ustedes": "comieron"},
            "unir": {"yo": "uní", "tú": "uniste", "él": "unió", "ella": "unió", "usted": "unió", "nosotros": "unimos", "nosotras": "unimos", "ellos": "unieron", "ellas": "unieron", "ustedes": "unieron"},
            "beber": {"yo": "bebí", "tú": "bebiste", "él": "bebió", "ella": "bebió", "usted": "bebió", "nosotros": "bebimos", "nosotras": "bebimos", "ellos": "bebieron", "ellas": "bebieron", "ustedes": "bebieron"},
            "salir": {"yo": "salí", "tú": "saliste", "él": "salió", "ella": "salió", "usted": "salió", "nosotros": "salimos", "nosotras": "salimos", "ellos": "salieron", "ellas": "salieron", "ustedes": "salieron"},
        }},
        "lesson_type": "conjugation",
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I spoke Spanish", "es": "Yo hablé español", "noun_id": None, "type": "written"},
            {"en": "You found the book", "es": "Tú encontraste el libro", "noun_id": "libro", "type": "auditory"},
            {"en": "He ate the food", "es": "Él comió la comida", "noun_id": "comida", "type": "written"},
            {"en": "She united the group", "es": "Ella unió al grupo", "noun_id": None, "type": "auditory"},
            {"en": "You (formal) drank the water", "es": "Usted bebió el agua", "noun_id": "agua", "type": "written"},
            {"en": "We left the house", "es": "Nosotros salimos de la casa", "noun_id": "casa", "type": "auditory"},
            {"en": "We (f) spoke a lot", "es": "Nosotras hablamos mucho", "noun_id": None, "type": "written"},
            {"en": "They found the dog", "es": "Ellos encontraron el perro", "noun_id": "perro", "type": "auditory"},
            {"en": "They (f) ate the bread", "es": "Ellas comieron el pan", "noun_id": "pan", "type": "written"},
            {"en": "You all united here", "es": "Ustedes unieron aquí", "noun_id": None, "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "hablar", "pronoun": "yo"},
            {"verb": "encontrar", "pronoun": "tú"},
            {"verb": "comer", "pronoun": "él"},
            {"verb": "unir", "pronoun": "ella"},
            {"verb": "beber", "pronoun": "usted"},
            {"verb": "salir", "pronoun": "nosotros"},
            {"verb": "hablar", "pronoun": "nosotras"},
            {"verb": "encontrar", "pronoun": "ellos"},
            {"verb": "comer", "pronoun": "ellas"},
            {"verb": "unir", "pronoun": "ustedes"},
        ],
        "phase_2_config": {
            "description": "Preterite Regular lesson 1",
            "targets": [
            {"verb": "hablar", "pronoun": "yo"},
            {"verb": "encontrar", "pronoun": "tú"},
            {"verb": "comer", "pronoun": "él"},
            {"verb": "unir", "pronoun": "ella"},
            {"verb": "beber", "pronoun": "usted"},
            {"verb": "salir", "pronoun": "nosotros"},
            {"verb": "hablar", "pronoun": "nosotras"},
            {"verb": "encontrar", "pronoun": "ellos"},
            {"verb": "comer", "pronoun": "ellas"},
            {"verb": "unir", "pronoun": "ustedes"},
            ],
        },
        "opener_en": "Did you talk to anyone today?",
        "opener_es": "¿Hablaste con alguien hoy?",
    },
    # --- GL 17: chat companion of `grammar_preterite_regular_1` ---
    "grammar_preterite_regular_1_chat": {
        "title": "Preterite Regular (1/3) — Chat",
        "grammar_level": 17,
        "lesson_number": 1.1,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "encontrar", "comer", "unir", "beber", "salir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "preterite",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Preterite Regular lesson 1', 'targets': [{'verb': 'hablar', 'pronoun': 'yo'}, {'verb': 'encontrar', 'pronoun': 'tú'}, {'verb': 'comer', 'pronoun': 'él'}, {'verb': 'unir', 'pronoun': 'ella'}, {'verb': 'beber', 'pronoun': 'usted'}, {'verb': 'salir', 'pronoun': 'nosotros'}, {'verb': 'hablar', 'pronoun': 'nosotras'}, {'verb': 'encontrar', 'pronoun': 'ellos'}, {'verb': 'comer', 'pronoun': 'ellas'}, {'verb': 'unir', 'pronoun': 'ustedes'}]},
    },
    "grammar_preterite_regular_2": {
        "title": "Preterite Regular (2/3)",
        "grammar_level": 17,
        "lesson_number": 2,
        "word_workload": ['hablar', 'encontrar', 'comer', 'unir', 'beber', 'salir'],
        "video_embed_id": "uBOH6A3vO0U",
        "drill_type": "conjugation",
        "tense": "preterite",
        "drill_config": {"answers": {
            "hablar": {"yo": "hablé", "tú": "hablaste", "él": "habló", "ella": "habló", "usted": "habló", "nosotros": "hablamos", "nosotras": "hablamos", "ellos": "hablaron", "ellas": "hablaron", "ustedes": "hablaron"},
            "encontrar": {"yo": "encontré", "tú": "encontraste", "él": "encontró", "ella": "encontró", "usted": "encontró", "nosotros": "encontramos", "nosotras": "encontramos", "ellos": "encontraron", "ellas": "encontraron", "ustedes": "encontraron"},
            "comer": {"yo": "comí", "tú": "comiste", "él": "comió", "ella": "comió", "usted": "comió", "nosotros": "comimos", "nosotras": "comimos", "ellos": "comieron", "ellas": "comieron", "ustedes": "comieron"},
            "unir": {"yo": "uní", "tú": "uniste", "él": "unió", "ella": "unió", "usted": "unió", "nosotros": "unimos", "nosotras": "unimos", "ellos": "unieron", "ellas": "unieron", "ustedes": "unieron"},
            "beber": {"yo": "bebí", "tú": "bebiste", "él": "bebió", "ella": "bebió", "usted": "bebió", "nosotros": "bebimos", "nosotras": "bebimos", "ellos": "bebieron", "ellas": "bebieron", "ustedes": "bebieron"},
            "salir": {"yo": "salí", "tú": "saliste", "él": "salió", "ella": "salió", "usted": "salió", "nosotros": "salimos", "nosotras": "salimos", "ellos": "salieron", "ellas": "salieron", "ustedes": "salieron"},
        }},
        "lesson_type": "conjugation",
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You spoke first", "es": "Tú hablaste primero", "noun_id": None, "type": "written"},
            {"en": "I found the letter", "es": "Yo encontré la carta", "noun_id": "carta", "type": "auditory"},
            {"en": "She ate the bread", "es": "Ella comió el pan", "noun_id": "pan", "type": "written"},
            {"en": "He united the family", "es": "Él unió a la familia", "noun_id": None, "type": "auditory"},
            {"en": "We drank the water", "es": "Nosotros bebimos el agua", "noun_id": "agua", "type": "written"},
            {"en": "You (formal) left the house", "es": "Usted salió de la casa", "noun_id": "casa", "type": "auditory"},
            {"en": "They spoke Spanish", "es": "Ellos hablaron español", "noun_id": None, "type": "written"},
            {"en": "We (f) found the dog", "es": "Nosotras encontramos el perro", "noun_id": "perro", "type": "auditory"},
            {"en": "You all ate the food", "es": "Ustedes comieron la comida", "noun_id": "comida", "type": "written"},
            {"en": "They (f) united here", "es": "Ellas unieron aquí", "noun_id": None, "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "hablar", "pronoun": "tú"},
            {"verb": "encontrar", "pronoun": "yo"},
            {"verb": "comer", "pronoun": "ella"},
            {"verb": "unir", "pronoun": "él"},
            {"verb": "beber", "pronoun": "nosotros"},
            {"verb": "salir", "pronoun": "usted"},
            {"verb": "hablar", "pronoun": "ellos"},
            {"verb": "encontrar", "pronoun": "nosotras"},
            {"verb": "comer", "pronoun": "ustedes"},
            {"verb": "unir", "pronoun": "ellas"},
        ],
        "phase_2_config": {
            "description": "Preterite Regular lesson 2",
            "targets": [
            {"verb": "hablar", "pronoun": "tú"},
            {"verb": "encontrar", "pronoun": "yo"},
            {"verb": "comer", "pronoun": "ella"},
            {"verb": "unir", "pronoun": "él"},
            {"verb": "beber", "pronoun": "nosotros"},
            {"verb": "salir", "pronoun": "usted"},
            {"verb": "hablar", "pronoun": "ellos"},
            {"verb": "encontrar", "pronoun": "nosotras"},
            {"verb": "comer", "pronoun": "ustedes"},
            {"verb": "unir", "pronoun": "ellas"},
            ],
        },
        "opener_en": "What did your friend eat?",
        "opener_es": "¿Qué comió tu amiga ayer?",
    },
    # --- GL 17: chat companion of `grammar_preterite_regular_2` ---
    "grammar_preterite_regular_2_chat": {
        "title": "Preterite Regular (2/3) — Chat",
        "grammar_level": 17,
        "lesson_number": 2.1,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "encontrar", "comer", "unir", "beber", "salir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "preterite",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Preterite Regular lesson 2', 'targets': [{'verb': 'hablar', 'pronoun': 'tú'}, {'verb': 'encontrar', 'pronoun': 'yo'}, {'verb': 'comer', 'pronoun': 'ella'}, {'verb': 'unir', 'pronoun': 'él'}, {'verb': 'beber', 'pronoun': 'nosotros'}, {'verb': 'salir', 'pronoun': 'usted'}, {'verb': 'hablar', 'pronoun': 'ellos'}, {'verb': 'encontrar', 'pronoun': 'nosotras'}, {'verb': 'comer', 'pronoun': 'ustedes'}, {'verb': 'unir', 'pronoun': 'ellas'}]},
    },
    "grammar_preterite_regular_3": {
        "title": "Preterite Regular (3/3)",
        "grammar_level": 17,
        "lesson_number": 3,
        "word_workload": ['hablar', 'encontrar', 'comer', 'unir', 'beber', 'salir'],
        "video_embed_id": "uBOH6A3vO0U",
        "drill_type": "conjugation",
        "tense": "preterite",
        "drill_config": {"answers": {
            "hablar": {"yo": "hablé", "tú": "hablaste", "él": "habló", "ella": "habló", "usted": "habló", "nosotros": "hablamos", "nosotras": "hablamos", "ellos": "hablaron", "ellas": "hablaron", "ustedes": "hablaron"},
            "encontrar": {"yo": "encontré", "tú": "encontraste", "él": "encontró", "ella": "encontró", "usted": "encontró", "nosotros": "encontramos", "nosotras": "encontramos", "ellos": "encontraron", "ellas": "encontraron", "ustedes": "encontraron"},
            "comer": {"yo": "comí", "tú": "comiste", "él": "comió", "ella": "comió", "usted": "comió", "nosotros": "comimos", "nosotras": "comimos", "ellos": "comieron", "ellas": "comieron", "ustedes": "comieron"},
            "unir": {"yo": "uní", "tú": "uniste", "él": "unió", "ella": "unió", "usted": "unió", "nosotros": "unimos", "nosotras": "unimos", "ellos": "unieron", "ellas": "unieron", "ustedes": "unieron"},
            "beber": {"yo": "bebí", "tú": "bebiste", "él": "bebió", "ella": "bebió", "usted": "bebió", "nosotros": "bebimos", "nosotras": "bebimos", "ellos": "bebieron", "ellas": "bebieron", "ustedes": "bebieron"},
            "salir": {"yo": "salí", "tú": "saliste", "él": "salió", "ella": "salió", "usted": "salió", "nosotros": "salimos", "nosotras": "salimos", "ellos": "salieron", "ellas": "salieron", "ustedes": "salieron"},
        }},
        "lesson_type": "conjugation",
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "He spoke the truth", "es": "Él habló la verdad", "noun_id": None, "type": "written"},
            {"en": "She found the book", "es": "Ella encontró el libro", "noun_id": "libro", "type": "auditory"},
            {"en": "I ate the bread", "es": "Yo comí el pan", "noun_id": "pan", "type": "written"},
            {"en": "You united the group", "es": "Tú uniste al grupo", "noun_id": None, "type": "auditory"},
            {"en": "We (f) drank the water", "es": "Nosotras bebimos el agua", "noun_id": "agua", "type": "written"},
            {"en": "They left the house", "es": "Ellos salieron de la casa", "noun_id": "casa", "type": "auditory"},
            {"en": "You (formal) spoke a lot", "es": "Usted habló mucho", "noun_id": None, "type": "written"},
            {"en": "We found the dog", "es": "Nosotros encontramos el perro", "noun_id": "perro", "type": "auditory"},
            {"en": "They (f) drank the coffee", "es": "Ellas bebieron el café", "noun_id": "café", "type": "written"},
            {"en": "You all left the city", "es": "Ustedes salieron de la ciudad", "noun_id": "ciudad", "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "hablar", "pronoun": "él"},
            {"verb": "encontrar", "pronoun": "ella"},
            {"verb": "comer", "pronoun": "yo"},
            {"verb": "unir", "pronoun": "tú"},
            {"verb": "beber", "pronoun": "nosotras"},
            {"verb": "salir", "pronoun": "ellos"},
            {"verb": "hablar", "pronoun": "usted"},
            {"verb": "encontrar", "pronoun": "nosotros"},
            {"verb": "beber", "pronoun": "ellas"},
            {"verb": "salir", "pronoun": "ustedes"},
        ],
        "phase_2_config": {
            "description": "Preterite Regular lesson 3",
            "targets": [
            {"verb": "hablar", "pronoun": "él"},
            {"verb": "encontrar", "pronoun": "ella"},
            {"verb": "comer", "pronoun": "yo"},
            {"verb": "unir", "pronoun": "tú"},
            {"verb": "beber", "pronoun": "nosotras"},
            {"verb": "salir", "pronoun": "ellos"},
            {"verb": "hablar", "pronoun": "usted"},
            {"verb": "encontrar", "pronoun": "nosotros"},
            {"verb": "beber", "pronoun": "ellas"},
            {"verb": "salir", "pronoun": "ustedes"},
            ],
        },
        "opener_en": "Did they go out last weekend?",
        "opener_es": "¿Salieron el fin de semana?",
    },
    # --- GL 17: chat companion of `grammar_preterite_regular_3` ---
    "grammar_preterite_regular_3_chat": {
        "title": "Preterite Regular (3/3) — Chat",
        "grammar_level": 17,
        "lesson_number": 3.1,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "encontrar", "comer", "unir", "beber", "salir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "preterite",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Preterite Regular lesson 3', 'targets': [{'verb': 'hablar', 'pronoun': 'él'}, {'verb': 'encontrar', 'pronoun': 'ella'}, {'verb': 'comer', 'pronoun': 'yo'}, {'verb': 'unir', 'pronoun': 'tú'}, {'verb': 'beber', 'pronoun': 'nosotras'}, {'verb': 'salir', 'pronoun': 'ellos'}, {'verb': 'hablar', 'pronoun': 'usted'}, {'verb': 'encontrar', 'pronoun': 'nosotros'}, {'verb': 'beber', 'pronoun': 'ellas'}, {'verb': 'salir', 'pronoun': 'ustedes'}]},
    },
    # --- GL 17.1: Preterite Highly Irregular — 4 lessons (L1&3: ser/ir,dar,ver,hacer,decir / L2&4: traer,dormir,morir + 2 from first) ---
    "grammar_preterite_irregular_1": {
        "title": "Preterite Highly Irregular (1/4)",
        "grammar_level": 17.1,
        "lesson_number": 1,
        "word_workload": ['ser', 'ir', 'dar', 'ver', 'hacer', 'decir'],
        "video_embed_id": "Ib68zJ3q7i8",
        "drill_type": "conjugation",
        "tense": "preterite",
        "drill_config": {
            "answers": {
            "ser": {"yo": "fui", "tú": "fuiste", "él": "fue", "ella": "fue", "usted": "fue", "nosotros": "fuimos", "nosotras": "fuimos", "ellos": "fueron", "ellas": "fueron", "ustedes": "fueron"},
            "ir": {"yo": "fui", "tú": "fuiste", "él": "fue", "ella": "fue", "usted": "fue", "nosotros": "fuimos", "nosotras": "fuimos", "ellos": "fueron", "ellas": "fueron", "ustedes": "fueron"},
            "dar": {"yo": "di", "tú": "diste", "él": "dio", "ella": "dio", "usted": "dio", "nosotros": "dimos", "nosotras": "dimos", "ellos": "dieron", "ellas": "dieron", "ustedes": "dieron"},
            "ver": {"yo": "vi", "tú": "viste", "él": "vio", "ella": "vio", "usted": "vio", "nosotros": "vimos", "nosotras": "vimos", "ellos": "vieron", "ellas": "vieron", "ustedes": "vieron"},
            "hacer": {"yo": "hice", "tú": "hiciste", "él": "hizo", "ella": "hizo", "usted": "hizo", "nosotros": "hicimos", "nosotras": "hicimos", "ellos": "hicieron", "ellas": "hicieron", "ustedes": "hicieron"},
            "decir": {"yo": "dije", "tú": "dijiste", "él": "dijo", "ella": "dijo", "usted": "dijo", "nosotros": "dijimos", "nosotras": "dijimos", "ellos": "dijeron", "ellas": "dijeron", "ustedes": "dijeron"},
            },
        },
        "lesson_type": "conjugation",
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I was a student", "es": "Yo fui estudiante", "noun_id": None, "type": "written"},
            {"en": "She was at the park", "es": "Ella fue al parque", "noun_id": "parque", "type": "auditory"},
            {"en": "You went to the market", "es": "Tú fuiste al mercado", "noun_id": "mercado", "type": "written"},
            {"en": "We (f) gave the letter", "es": "Nosotras dimos la carta", "noun_id": "carta", "type": "auditory"},
            {"en": "He gave the book", "es": "Él dio el libro", "noun_id": "libro", "type": "written"},
            {"en": "You all saw the dog", "es": "Ustedes vieron el perro", "noun_id": "perro", "type": "auditory"},
            {"en": "You (formal) saw the house", "es": "Usted vio la casa", "noun_id": "casa", "type": "written"},
            {"en": "We made the plan", "es": "Nosotros hicimos el plan", "noun_id": None, "type": "auditory"},
            {"en": "They (f) made the food", "es": "Ellas hicieron la comida", "noun_id": "comida", "type": "written"},
            {"en": "They said the truth", "es": "Ellos dijeron la verdad", "noun_id": None, "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "ser", "pronoun": "yo"},
            {"verb": "ser", "pronoun": "ella"},
            {"verb": "ir", "pronoun": "tú"},
            {"verb": "dar", "pronoun": "nosotras"},
            {"verb": "dar", "pronoun": "él"},
            {"verb": "ver", "pronoun": "ustedes"},
            {"verb": "ver", "pronoun": "usted"},
            {"verb": "hacer", "pronoun": "nosotros"},
            {"verb": "hacer", "pronoun": "ellas"},
            {"verb": "decir", "pronoun": "ellos"},
        ],
        "phase_2_config": {
            "description": "Preterite Highly Irregular lesson 1: ser, ir, dar, ver, hacer, decir",
            "targets": [
                {"verb": "ser", "pronoun": "yo"},
            {"verb": "ser", "pronoun": "ella"},
            {"verb": "ir", "pronoun": "tú"},
            {"verb": "dar", "pronoun": "nosotras"},
            {"verb": "dar", "pronoun": "él"},
            {"verb": "ver", "pronoun": "ustedes"},
            {"verb": "ver", "pronoun": "usted"},
            {"verb": "hacer", "pronoun": "nosotros"},
            {"verb": "hacer", "pronoun": "ellas"},
            {"verb": "decir", "pronoun": "ellos"},
            ],
        },
        "opener_en": "Did you go to the market?",
        "opener_es": "¿Fuiste al mercado?",
    },
    # --- GL 17.1: chat companion of `grammar_preterite_irregular_1` ---
    "grammar_preterite_irregular_1_chat": {
        "title": "Preterite Highly Irregular (1/4) — Chat",
        "grammar_level": 17.1,
        "lesson_number": 1.1,
        "lesson_type": "conjugation",
        "word_workload": ["ser", "ir", "dar", "ver", "hacer", "decir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "preterite",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Preterite Highly Irregular lesson 1: ser, ir, dar, ver, hacer, decir', 'targets': [{'verb': 'ser', 'pronoun': 'yo'}, {'verb': 'ser', 'pronoun': 'ella'}, {'verb': 'ir', 'pronoun': 'tú'}, {'verb': 'dar', 'pronoun': 'nosotras'}, {'verb': 'dar', 'pronoun': 'él'}, {'verb': 'ver', 'pronoun': 'ustedes'}, {'verb': 'ver', 'pronoun': 'usted'}, {'verb': 'hacer', 'pronoun': 'nosotros'}, {'verb': 'hacer', 'pronoun': 'ellas'}, {'verb': 'decir', 'pronoun': 'ellos'}]},
    },
    "grammar_preterite_irregular_2": {
        "title": "Preterite Highly Irregular (2/4)",
        "grammar_level": 17.1,
        "lesson_number": 2,
        "word_workload": ['traer', 'dormir', 'morir', 'ser', 'hacer'],
        "video_embed_id": "Ib68zJ3q7i8",
        "drill_type": "conjugation",
        "tense": "preterite",
        "drill_config": {
            "answers": {
            "traer": {"yo": "traje", "tú": "trajiste", "él": "trajo", "ella": "trajo", "usted": "trajo", "nosotros": "trajimos", "nosotras": "trajimos", "ellos": "trajeron", "ellas": "trajeron", "ustedes": "trajeron"},
            "dormir": {"yo": "dormí", "tú": "dormiste", "él": "durmió", "ella": "durmió", "usted": "durmió", "nosotros": "dormimos", "nosotras": "dormimos", "ellos": "durmieron", "ellas": "durmieron", "ustedes": "durmieron"},
            "morir": {"yo": "morí", "tú": "moriste", "él": "murió", "ella": "murió", "usted": "murió", "nosotros": "morimos", "nosotras": "morimos", "ellos": "murieron", "ellas": "murieron", "ustedes": "murieron"},
            "ser": {"yo": "fui", "tú": "fuiste", "él": "fue", "ella": "fue", "usted": "fue", "nosotros": "fuimos", "nosotras": "fuimos", "ellos": "fueron", "ellas": "fueron", "ustedes": "fueron"},
            "hacer": {"yo": "hice", "tú": "hiciste", "él": "hizo", "ella": "hizo", "usted": "hizo", "nosotros": "hicimos", "nosotras": "hicimos", "ellos": "hicieron", "ellas": "hicieron", "ustedes": "hicieron"},
            },
        },
        "lesson_type": "conjugation",
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I brought the food", "es": "Yo traje la comida", "noun_id": "comida", "type": "written"},
            {"en": "We brought the letter", "es": "Nosotros trajimos la carta", "noun_id": "carta", "type": "auditory"},
            {"en": "They (f) brought the bags", "es": "Ellas trajeron las bolsas", "noun_id": "bolsa", "type": "written"},
            {"en": "You slept well", "es": "Tú dormiste bien", "noun_id": None, "type": "auditory"},
            {"en": "She slept a lot", "es": "Ella durmió mucho", "noun_id": None, "type": "written"},
            {"en": "He died young", "es": "Él murió joven", "noun_id": None, "type": "auditory"},
            {"en": "You all died of fear", "es": "Ustedes murieron de miedo", "noun_id": None, "type": "written"},
            {"en": "You (formal) were a doctor", "es": "Usted fue doctor", "noun_id": None, "type": "auditory"},
            {"en": "We (f) were at the park", "es": "Nosotras fuimos al parque", "noun_id": "parque", "type": "written"},
            {"en": "They made the plan", "es": "Ellos hicieron el plan", "noun_id": None, "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "traer", "pronoun": "yo"},
            {"verb": "traer", "pronoun": "nosotros"},
            {"verb": "traer", "pronoun": "ellas"},
            {"verb": "dormir", "pronoun": "tú"},
            {"verb": "dormir", "pronoun": "ella"},
            {"verb": "morir", "pronoun": "él"},
            {"verb": "morir", "pronoun": "ustedes"},
            {"verb": "ser", "pronoun": "usted"},
            {"verb": "ser", "pronoun": "nosotras"},
            {"verb": "hacer", "pronoun": "ellos"},
        ],
        "phase_2_config": {
            "description": "Preterite Highly Irregular lesson 2: traer, dormir, morir, ser, hacer",
            "targets": [
                {"verb": "traer", "pronoun": "yo"},
            {"verb": "traer", "pronoun": "nosotros"},
            {"verb": "traer", "pronoun": "ellas"},
            {"verb": "dormir", "pronoun": "tú"},
            {"verb": "dormir", "pronoun": "ella"},
            {"verb": "morir", "pronoun": "él"},
            {"verb": "morir", "pronoun": "ustedes"},
            {"verb": "ser", "pronoun": "usted"},
            {"verb": "ser", "pronoun": "nosotras"},
            {"verb": "hacer", "pronoun": "ellos"},
            ],
        },
        "opener_en": "What did you bring?",
        "opener_es": "¿Qué trajiste?",
    },
    # --- GL 17.1: chat companion of `grammar_preterite_irregular_2` ---
    "grammar_preterite_irregular_2_chat": {
        "title": "Preterite Highly Irregular (2/4) — Chat",
        "grammar_level": 17.1,
        "lesson_number": 2.1,
        "lesson_type": "conjugation",
        "word_workload": ["traer", "dormir", "morir", "ser", "hacer"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "preterite",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Preterite Highly Irregular lesson 2: traer, dormir, morir, ser, hacer', 'targets': [{'verb': 'traer', 'pronoun': 'yo'}, {'verb': 'traer', 'pronoun': 'nosotros'}, {'verb': 'traer', 'pronoun': 'ellas'}, {'verb': 'dormir', 'pronoun': 'tú'}, {'verb': 'dormir', 'pronoun': 'ella'}, {'verb': 'morir', 'pronoun': 'él'}, {'verb': 'morir', 'pronoun': 'ustedes'}, {'verb': 'ser', 'pronoun': 'usted'}, {'verb': 'ser', 'pronoun': 'nosotras'}, {'verb': 'hacer', 'pronoun': 'ellos'}]},
    },
    "grammar_preterite_irregular_3": {
        "title": "Preterite Highly Irregular (3/4)",
        "grammar_level": 17.1,
        "lesson_number": 3,
        "word_workload": ['ser', 'ir', 'dar', 'ver', 'hacer', 'decir'],
        "video_embed_id": "Ib68zJ3q7i8",
        "drill_type": "conjugation",
        "tense": "preterite",
        "drill_config": {
            "answers": {
            "ser": {"yo": "fui", "tú": "fuiste", "él": "fue", "ella": "fue", "usted": "fue", "nosotros": "fuimos", "nosotras": "fuimos", "ellos": "fueron", "ellas": "fueron", "ustedes": "fueron"},
            "ir": {"yo": "fui", "tú": "fuiste", "él": "fue", "ella": "fue", "usted": "fue", "nosotros": "fuimos", "nosotras": "fuimos", "ellos": "fueron", "ellas": "fueron", "ustedes": "fueron"},
            "dar": {"yo": "di", "tú": "diste", "él": "dio", "ella": "dio", "usted": "dio", "nosotros": "dimos", "nosotras": "dimos", "ellos": "dieron", "ellas": "dieron", "ustedes": "dieron"},
            "ver": {"yo": "vi", "tú": "viste", "él": "vio", "ella": "vio", "usted": "vio", "nosotros": "vimos", "nosotras": "vimos", "ellos": "vieron", "ellas": "vieron", "ustedes": "vieron"},
            "hacer": {"yo": "hice", "tú": "hiciste", "él": "hizo", "ella": "hizo", "usted": "hizo", "nosotros": "hicimos", "nosotras": "hicimos", "ellos": "hicieron", "ellas": "hicieron", "ustedes": "hicieron"},
            "decir": {"yo": "dije", "tú": "dijiste", "él": "dijo", "ella": "dijo", "usted": "dijo", "nosotros": "dijimos", "nosotras": "dijimos", "ellos": "dijeron", "ellas": "dijeron", "ustedes": "dijeron"},
            },
        },
        "lesson_type": "conjugation",
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You were a teacher", "es": "Tú fuiste profesor", "noun_id": None, "type": "written"},
            {"en": "We went to the park", "es": "Nosotros fuimos al parque", "noun_id": "parque", "type": "auditory"},
            {"en": "They went to the city", "es": "Ellos fueron a la ciudad", "noun_id": "ciudad", "type": "written"},
            {"en": "You (formal) gave the book", "es": "Usted dio el libro", "noun_id": "libro", "type": "auditory"},
            {"en": "I gave the letter", "es": "Yo di la carta", "noun_id": "carta", "type": "written"},
            {"en": "She saw the dog", "es": "Ella vio el perro", "noun_id": "perro", "type": "auditory"},
            {"en": "We (f) saw the house", "es": "Nosotras vimos la casa", "noun_id": "casa", "type": "written"},
            {"en": "He made the plan", "es": "Él hizo el plan", "noun_id": None, "type": "auditory"},
            {"en": "You all made the food", "es": "Ustedes hicieron la comida", "noun_id": "comida", "type": "written"},
            {"en": "They (f) said the truth", "es": "Ellas dijeron la verdad", "noun_id": None, "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "ser", "pronoun": "tú"},
            {"verb": "ir", "pronoun": "nosotros"},
            {"verb": "ir", "pronoun": "ellos"},
            {"verb": "dar", "pronoun": "usted"},
            {"verb": "dar", "pronoun": "yo"},
            {"verb": "ver", "pronoun": "ella"},
            {"verb": "ver", "pronoun": "nosotras"},
            {"verb": "hacer", "pronoun": "él"},
            {"verb": "hacer", "pronoun": "ustedes"},
            {"verb": "decir", "pronoun": "ellas"},
        ],
        "phase_2_config": {
            "description": "Preterite Highly Irregular lesson 3: ser, ir, dar, ver, hacer, decir",
            "targets": [
                {"verb": "ser", "pronoun": "tú"},
            {"verb": "ir", "pronoun": "nosotros"},
            {"verb": "ir", "pronoun": "ellos"},
            {"verb": "dar", "pronoun": "usted"},
            {"verb": "dar", "pronoun": "yo"},
            {"verb": "ver", "pronoun": "ella"},
            {"verb": "ver", "pronoun": "nosotras"},
            {"verb": "hacer", "pronoun": "él"},
            {"verb": "hacer", "pronoun": "ustedes"},
            {"verb": "decir", "pronoun": "ellas"},
            ],
        },
        "opener_en": "What did your friend do?",
        "opener_es": "¿Qué hizo tu amiga?",
    },
    # --- GL 17.1: chat companion of `grammar_preterite_irregular_3` ---
    "grammar_preterite_irregular_3_chat": {
        "title": "Preterite Highly Irregular (3/4) — Chat",
        "grammar_level": 17.1,
        "lesson_number": 3.1,
        "lesson_type": "conjugation",
        "word_workload": ["ser", "ir", "dar", "ver", "hacer", "decir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "preterite",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Preterite Highly Irregular lesson 3: ser, ir, dar, ver, hacer, decir', 'targets': [{'verb': 'ser', 'pronoun': 'tú'}, {'verb': 'ir', 'pronoun': 'nosotros'}, {'verb': 'ir', 'pronoun': 'ellos'}, {'verb': 'dar', 'pronoun': 'usted'}, {'verb': 'dar', 'pronoun': 'yo'}, {'verb': 'ver', 'pronoun': 'ella'}, {'verb': 'ver', 'pronoun': 'nosotras'}, {'verb': 'hacer', 'pronoun': 'él'}, {'verb': 'hacer', 'pronoun': 'ustedes'}, {'verb': 'decir', 'pronoun': 'ellas'}]},
    },
    "grammar_preterite_irregular_4": {
        "title": "Preterite Highly Irregular (4/4)",
        "grammar_level": 17.1,
        "lesson_number": 4,
        "word_workload": ['traer', 'dormir', 'morir', 'ir', 'decir'],
        "video_embed_id": "Ib68zJ3q7i8",
        "drill_type": "conjugation",
        "tense": "preterite",
        "drill_config": {
            "answers": {
            "traer": {"yo": "traje", "tú": "trajiste", "él": "trajo", "ella": "trajo", "usted": "trajo", "nosotros": "trajimos", "nosotras": "trajimos", "ellos": "trajeron", "ellas": "trajeron", "ustedes": "trajeron"},
            "dormir": {"yo": "dormí", "tú": "dormiste", "él": "durmió", "ella": "durmió", "usted": "durmió", "nosotros": "dormimos", "nosotras": "dormimos", "ellos": "durmieron", "ellas": "durmieron", "ustedes": "durmieron"},
            "morir": {"yo": "morí", "tú": "moriste", "él": "murió", "ella": "murió", "usted": "murió", "nosotros": "morimos", "nosotras": "morimos", "ellos": "murieron", "ellas": "murieron", "ustedes": "murieron"},
            "ir": {"yo": "fui", "tú": "fuiste", "él": "fue", "ella": "fue", "usted": "fue", "nosotros": "fuimos", "nosotras": "fuimos", "ellos": "fueron", "ellas": "fueron", "ustedes": "fueron"},
            "decir": {"yo": "dije", "tú": "dijiste", "él": "dijo", "ella": "dijo", "usted": "dijo", "nosotros": "dijimos", "nosotras": "dijimos", "ellos": "dijeron", "ellas": "dijeron", "ustedes": "dijeron"},
            },
        },
        "lesson_type": "conjugation",
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You brought the food", "es": "Tú trajiste la comida", "noun_id": "comida", "type": "written"},
            {"en": "You (formal) brought the letter", "es": "Usted trajo la carta", "noun_id": "carta", "type": "auditory"},
            {"en": "I slept eight hours", "es": "Yo dormí ocho horas", "noun_id": None, "type": "written"},
            {"en": "We (f) slept here", "es": "Nosotras dormimos aquí", "noun_id": None, "type": "auditory"},
            {"en": "They slept in the house", "es": "Ellos durmieron en la casa", "noun_id": "casa", "type": "written"},
            {"en": "She died at home", "es": "Ella murió en casa", "noun_id": None, "type": "auditory"},
            {"en": "We died of laughter", "es": "Nosotros morimos de risa", "noun_id": None, "type": "written"},
            {"en": "He went to the market", "es": "Él fue al mercado", "noun_id": "mercado", "type": "auditory"},
            {"en": "They (f) went to the park", "es": "Ellas fueron al parque", "noun_id": "parque", "type": "written"},
            {"en": "You all said the truth", "es": "Ustedes dijeron la verdad", "noun_id": None, "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "traer", "pronoun": "tú"},
            {"verb": "traer", "pronoun": "usted"},
            {"verb": "dormir", "pronoun": "yo"},
            {"verb": "dormir", "pronoun": "nosotras"},
            {"verb": "dormir", "pronoun": "ellos"},
            {"verb": "morir", "pronoun": "ella"},
            {"verb": "morir", "pronoun": "nosotros"},
            {"verb": "ir", "pronoun": "él"},
            {"verb": "ir", "pronoun": "ellas"},
            {"verb": "decir", "pronoun": "ustedes"},
        ],
        "phase_2_config": {
            "description": "Preterite Highly Irregular lesson 4: traer, dormir, morir, ir, decir",
            "targets": [
                {"verb": "traer", "pronoun": "tú"},
            {"verb": "traer", "pronoun": "usted"},
            {"verb": "dormir", "pronoun": "yo"},
            {"verb": "dormir", "pronoun": "nosotras"},
            {"verb": "dormir", "pronoun": "ellos"},
            {"verb": "morir", "pronoun": "ella"},
            {"verb": "morir", "pronoun": "nosotros"},
            {"verb": "ir", "pronoun": "él"},
            {"verb": "ir", "pronoun": "ellas"},
            {"verb": "decir", "pronoun": "ustedes"},
            ],
        },
        "opener_en": "Did your friends see the game?",
        "opener_es": "¿Tus amigas vieron el partido?",
    },
    # --- GL 17.1: chat companion of `grammar_preterite_irregular_4` ---
    "grammar_preterite_irregular_4_chat": {
        "title": "Preterite Highly Irregular (4/4) — Chat",
        "grammar_level": 17.1,
        "lesson_number": 4.1,
        "lesson_type": "conjugation",
        "word_workload": ["traer", "dormir", "morir", "ir", "decir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "preterite",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Preterite Highly Irregular lesson 4: traer, dormir, morir, ir, decir', 'targets': [{'verb': 'traer', 'pronoun': 'tú'}, {'verb': 'traer', 'pronoun': 'usted'}, {'verb': 'dormir', 'pronoun': 'yo'}, {'verb': 'dormir', 'pronoun': 'nosotras'}, {'verb': 'dormir', 'pronoun': 'ellos'}, {'verb': 'morir', 'pronoun': 'ella'}, {'verb': 'morir', 'pronoun': 'nosotros'}, {'verb': 'ir', 'pronoun': 'él'}, {'verb': 'ir', 'pronoun': 'ellas'}, {'verb': 'decir', 'pronoun': 'ustedes'}]},
    },
    # --- GL 18: Gerund — 4 lessons (L1&3: hablar,caminar,charlar,comer / L2&4: beber,inhibir,prohibir,salir) ---
    "grammar_gerund_1": {
        "title": "Gerund (1/4)",
        "grammar_level": 18,
        "lesson_number": 1,
        "word_workload": ['hablar', 'caminar', 'charlar', 'comer'],
        "video_embed_id": "Xpma6w0jy7m",
        "drill_type": "conjugation",
        "tense": "gerund",
        "drill_config": {
            "answers": {
            "hablar": {"yo": "estoy hablando", "tú": "estás hablando", "él": "está hablando", "ella": "está hablando", "usted": "está hablando", "nosotros": "estamos hablando", "nosotras": "estamos hablando", "ellos": "están hablando", "ellas": "están hablando", "ustedes": "están hablando"},
            "caminar": {"yo": "estoy caminando", "tú": "estás caminando", "él": "está caminando", "ella": "está caminando", "usted": "está caminando", "nosotros": "estamos caminando", "nosotras": "estamos caminando", "ellos": "están caminando", "ellas": "están caminando", "ustedes": "están caminando"},
            "charlar": {"yo": "estoy charlando", "tú": "estás charlando", "él": "está charlando", "ella": "está charlando", "usted": "está charlando", "nosotros": "estamos charlando", "nosotras": "estamos charlando", "ellos": "están charlando", "ellas": "están charlando", "ustedes": "están charlando"},
            "comer": {"yo": "estoy comiendo", "tú": "estás comiendo", "él": "está comiendo", "ella": "está comiendo", "usted": "está comiendo", "nosotros": "estamos comiendo", "nosotras": "estamos comiendo", "ellos": "están comiendo", "ellas": "están comiendo", "ustedes": "están comiendo"},
            },
        },
        "lesson_type": "conjugation",
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I am speaking Spanish", "es": "Yo estoy hablando español", "noun_id": None, "type": "written"},
            {"en": "She is speaking now", "es": "Ella está hablando ahora", "noun_id": None, "type": "auditory"},
            {"en": "You all are speaking", "es": "Ustedes están hablando", "noun_id": None, "type": "written"},
            {"en": "You are walking here", "es": "Tú estás caminando aquí", "noun_id": None, "type": "auditory"},
            {"en": "We (f) are walking a lot", "es": "Nosotras estamos caminando mucho", "noun_id": None, "type": "written"},
            {"en": "He is chatting now", "es": "Él está charlando ahora", "noun_id": None, "type": "auditory"},
            {"en": "They are chatting here", "es": "Ellos están charlando aquí", "noun_id": None, "type": "written"},
            {"en": "You (formal) are eating the food", "es": "Usted está comiendo la comida", "noun_id": "comida", "type": "auditory"},
            {"en": "We are eating the bread", "es": "Nosotros estamos comiendo el pan", "noun_id": "pan", "type": "written"},
            {"en": "They (f) are eating a lot", "es": "Ellas están comiendo mucho", "noun_id": None, "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "hablar", "pronoun": "yo"},
            {"verb": "hablar", "pronoun": "ella"},
            {"verb": "hablar", "pronoun": "ustedes"},
            {"verb": "caminar", "pronoun": "tú"},
            {"verb": "caminar", "pronoun": "nosotras"},
            {"verb": "charlar", "pronoun": "él"},
            {"verb": "charlar", "pronoun": "ellos"},
            {"verb": "comer", "pronoun": "usted"},
            {"verb": "comer", "pronoun": "nosotros"},
            {"verb": "comer", "pronoun": "ellas"},
        ],
        "phase_2_config": {
            "description": "Gerund lesson 1: hablar, caminar, charlar, comer",
            "targets": [
                {"verb": "hablar", "pronoun": "yo"},
            {"verb": "hablar", "pronoun": "ella"},
            {"verb": "hablar", "pronoun": "ustedes"},
            {"verb": "caminar", "pronoun": "tú"},
            {"verb": "caminar", "pronoun": "nosotras"},
            {"verb": "charlar", "pronoun": "él"},
            {"verb": "charlar", "pronoun": "ellos"},
            {"verb": "comer", "pronoun": "usted"},
            {"verb": "comer", "pronoun": "nosotros"},
            {"verb": "comer", "pronoun": "ellas"},
            ],
        },
        "opener_en": "Are you talking on the phone?",
        "opener_es": "¿Estás hablando por teléfono?",
    },
    # --- GL 18: chat companion of `grammar_gerund_1` ---
    "grammar_gerund_1_chat": {
        "title": "Gerund (1/4) — Chat",
        "grammar_level": 18,
        "lesson_number": 1.1,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "caminar", "charlar", "comer"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "gerund",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Gerund lesson 1: hablar, caminar, charlar, comer', 'targets': [{'verb': 'hablar', 'pronoun': 'yo'}, {'verb': 'hablar', 'pronoun': 'ella'}, {'verb': 'hablar', 'pronoun': 'ustedes'}, {'verb': 'caminar', 'pronoun': 'tú'}, {'verb': 'caminar', 'pronoun': 'nosotras'}, {'verb': 'charlar', 'pronoun': 'él'}, {'verb': 'charlar', 'pronoun': 'ellos'}, {'verb': 'comer', 'pronoun': 'usted'}, {'verb': 'comer', 'pronoun': 'nosotros'}, {'verb': 'comer', 'pronoun': 'ellas'}]},
    },
    "grammar_gerund_2": {
        "title": "Gerund (2/4)",
        "grammar_level": 18,
        "lesson_number": 2,
        "word_workload": ['beber', 'inhibir', 'prohibir', 'salir'],
        "video_embed_id": "Xpma6w0jy7m",
        "drill_type": "conjugation",
        "tense": "gerund",
        "drill_config": {
            "answers": {
            "beber": {"yo": "estoy bebiendo", "tú": "estás bebiendo", "él": "está bebiendo", "ella": "está bebiendo", "usted": "está bebiendo", "nosotros": "estamos bebiendo", "nosotras": "estamos bebiendo", "ellos": "están bebiendo", "ellas": "están bebiendo", "ustedes": "están bebiendo"},
            "inhibir": {"yo": "estoy inhibiendo", "tú": "estás inhibiendo", "él": "está inhibiendo", "ella": "está inhibiendo", "usted": "está inhibiendo", "nosotros": "estamos inhibiendo", "nosotras": "estamos inhibiendo", "ellos": "están inhibiendo", "ellas": "están inhibiendo", "ustedes": "están inhibiendo"},
            "prohibir": {"yo": "estoy prohibiendo", "tú": "estás prohibiendo", "él": "está prohibiendo", "ella": "está prohibiendo", "usted": "está prohibiendo", "nosotros": "estamos prohibiendo", "nosotras": "estamos prohibiendo", "ellos": "están prohibiendo", "ellas": "están prohibiendo", "ustedes": "están prohibiendo"},
            "salir": {"yo": "estoy saliendo", "tú": "estás saliendo", "él": "está saliendo", "ella": "está saliendo", "usted": "está saliendo", "nosotros": "estamos saliendo", "nosotras": "estamos saliendo", "ellos": "están saliendo", "ellas": "están saliendo", "ustedes": "están saliendo"},
            },
        },
        "lesson_type": "conjugation",
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I am drinking the water", "es": "Yo estoy bebiendo el agua", "noun_id": "agua", "type": "written"},
            {"en": "We are drinking the coffee", "es": "Nosotros estamos bebiendo el café", "noun_id": "café", "type": "auditory"},
            {"en": "They (f) are drinking a lot", "es": "Ellas están bebiendo mucho", "noun_id": None, "type": "written"},
            {"en": "You are inhibiting me", "es": "Tú estás inhibiendo aquí", "noun_id": None, "type": "auditory"},
            {"en": "She is inhibiting now", "es": "Ella está inhibiendo ahora", "noun_id": None, "type": "written"},
            {"en": "He is prohibiting the entry", "es": "Él está prohibiendo la entrada", "noun_id": None, "type": "auditory"},
            {"en": "You all are prohibiting it", "es": "Ustedes están prohibiendo eso", "noun_id": None, "type": "written"},
            {"en": "You (formal) are leaving now", "es": "Usted está saliendo ahora", "noun_id": None, "type": "auditory"},
            {"en": "We (f) are leaving the house", "es": "Nosotras estamos saliendo de la casa", "noun_id": "casa", "type": "written"},
            {"en": "They are leaving the city", "es": "Ellos están saliendo de la ciudad", "noun_id": "ciudad", "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "beber", "pronoun": "yo"},
            {"verb": "beber", "pronoun": "nosotros"},
            {"verb": "beber", "pronoun": "ellas"},
            {"verb": "inhibir", "pronoun": "tú"},
            {"verb": "inhibir", "pronoun": "ella"},
            {"verb": "prohibir", "pronoun": "él"},
            {"verb": "prohibir", "pronoun": "ustedes"},
            {"verb": "salir", "pronoun": "usted"},
            {"verb": "salir", "pronoun": "nosotras"},
            {"verb": "salir", "pronoun": "ellos"},
        ],
        "phase_2_config": {
            "description": "Gerund lesson 2: beber, inhibir, prohibir, salir",
            "targets": [
                {"verb": "beber", "pronoun": "yo"},
            {"verb": "beber", "pronoun": "nosotros"},
            {"verb": "beber", "pronoun": "ellas"},
            {"verb": "inhibir", "pronoun": "tú"},
            {"verb": "inhibir", "pronoun": "ella"},
            {"verb": "prohibir", "pronoun": "él"},
            {"verb": "prohibir", "pronoun": "ustedes"},
            {"verb": "salir", "pronoun": "usted"},
            {"verb": "salir", "pronoun": "nosotras"},
            {"verb": "salir", "pronoun": "ellos"},
            ],
        },
        "opener_en": "Are you leaving already?",
        "opener_es": "¿Estás saliendo ya?",
    },
    # --- GL 18: chat companion of `grammar_gerund_2` ---
    "grammar_gerund_2_chat": {
        "title": "Gerund (2/4) — Chat",
        "grammar_level": 18,
        "lesson_number": 2.1,
        "lesson_type": "conjugation",
        "word_workload": ["beber", "inhibir", "prohibir", "salir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "gerund",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Gerund lesson 2: beber, inhibir, prohibir, salir', 'targets': [{'verb': 'beber', 'pronoun': 'yo'}, {'verb': 'beber', 'pronoun': 'nosotros'}, {'verb': 'beber', 'pronoun': 'ellas'}, {'verb': 'inhibir', 'pronoun': 'tú'}, {'verb': 'inhibir', 'pronoun': 'ella'}, {'verb': 'prohibir', 'pronoun': 'él'}, {'verb': 'prohibir', 'pronoun': 'ustedes'}, {'verb': 'salir', 'pronoun': 'usted'}, {'verb': 'salir', 'pronoun': 'nosotras'}, {'verb': 'salir', 'pronoun': 'ellos'}]},
    },
    "grammar_gerund_3": {
        "title": "Gerund (3/4)",
        "grammar_level": 18,
        "lesson_number": 3,
        "word_workload": ['hablar', 'caminar', 'charlar', 'comer'],
        "video_embed_id": "Xpma6w0jy7m",
        "drill_type": "conjugation",
        "tense": "gerund",
        "drill_config": {
            "answers": {
            "hablar": {"yo": "estoy hablando", "tú": "estás hablando", "él": "está hablando", "ella": "está hablando", "usted": "está hablando", "nosotros": "estamos hablando", "nosotras": "estamos hablando", "ellos": "están hablando", "ellas": "están hablando", "ustedes": "están hablando"},
            "caminar": {"yo": "estoy caminando", "tú": "estás caminando", "él": "está caminando", "ella": "está caminando", "usted": "está caminando", "nosotros": "estamos caminando", "nosotras": "estamos caminando", "ellos": "están caminando", "ellas": "están caminando", "ustedes": "están caminando"},
            "charlar": {"yo": "estoy charlando", "tú": "estás charlando", "él": "está charlando", "ella": "está charlando", "usted": "está charlando", "nosotros": "estamos charlando", "nosotras": "estamos charlando", "ellos": "están charlando", "ellas": "están charlando", "ustedes": "están charlando"},
            "comer": {"yo": "estoy comiendo", "tú": "estás comiendo", "él": "está comiendo", "ella": "está comiendo", "usted": "está comiendo", "nosotros": "estamos comiendo", "nosotras": "estamos comiendo", "ellos": "están comiendo", "ellas": "están comiendo", "ustedes": "están comiendo"},
            },
        },
        "lesson_type": "conjugation",
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You are speaking now", "es": "Tú estás hablando ahora", "noun_id": None, "type": "written"},
            {"en": "We are speaking Spanish", "es": "Nosotros estamos hablando español", "noun_id": None, "type": "auditory"},
            {"en": "You (formal) are walking here", "es": "Usted está caminando aquí", "noun_id": None, "type": "written"},
            {"en": "They (f) are walking a lot", "es": "Ellas están caminando mucho", "noun_id": None, "type": "auditory"},
            {"en": "I am chatting now", "es": "Yo estoy charlando ahora", "noun_id": None, "type": "written"},
            {"en": "We (f) are chatting here", "es": "Nosotras estamos charlando aquí", "noun_id": None, "type": "auditory"},
            {"en": "You all are chatting a lot", "es": "Ustedes están charlando mucho", "noun_id": None, "type": "written"},
            {"en": "He is eating the food", "es": "Él está comiendo la comida", "noun_id": "comida", "type": "auditory"},
            {"en": "She is eating the bread", "es": "Ella está comiendo el pan", "noun_id": "pan", "type": "written"},
            {"en": "They are eating now", "es": "Ellos están comiendo ahora", "noun_id": None, "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "hablar", "pronoun": "tú"},
            {"verb": "hablar", "pronoun": "nosotros"},
            {"verb": "caminar", "pronoun": "usted"},
            {"verb": "caminar", "pronoun": "ellas"},
            {"verb": "charlar", "pronoun": "yo"},
            {"verb": "charlar", "pronoun": "nosotras"},
            {"verb": "charlar", "pronoun": "ustedes"},
            {"verb": "comer", "pronoun": "él"},
            {"verb": "comer", "pronoun": "ella"},
            {"verb": "comer", "pronoun": "ellos"},
        ],
        "phase_2_config": {
            "description": "Gerund lesson 3: hablar, caminar, charlar, comer",
            "targets": [
                {"verb": "hablar", "pronoun": "tú"},
            {"verb": "hablar", "pronoun": "nosotros"},
            {"verb": "caminar", "pronoun": "usted"},
            {"verb": "caminar", "pronoun": "ellas"},
            {"verb": "charlar", "pronoun": "yo"},
            {"verb": "charlar", "pronoun": "nosotras"},
            {"verb": "charlar", "pronoun": "ustedes"},
            {"verb": "comer", "pronoun": "él"},
            {"verb": "comer", "pronoun": "ella"},
            {"verb": "comer", "pronoun": "ellos"},
            ],
        },
        "opener_en": "Is your friend eating now?",
        "opener_es": "¿Tu amiga está comiendo?",
    },
    # --- GL 18: chat companion of `grammar_gerund_3` ---
    "grammar_gerund_3_chat": {
        "title": "Gerund (3/4) — Chat",
        "grammar_level": 18,
        "lesson_number": 3.1,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "caminar", "charlar", "comer"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "gerund",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Gerund lesson 3: hablar, caminar, charlar, comer', 'targets': [{'verb': 'hablar', 'pronoun': 'tú'}, {'verb': 'hablar', 'pronoun': 'nosotros'}, {'verb': 'caminar', 'pronoun': 'usted'}, {'verb': 'caminar', 'pronoun': 'ellas'}, {'verb': 'charlar', 'pronoun': 'yo'}, {'verb': 'charlar', 'pronoun': 'nosotras'}, {'verb': 'charlar', 'pronoun': 'ustedes'}, {'verb': 'comer', 'pronoun': 'él'}, {'verb': 'comer', 'pronoun': 'ella'}, {'verb': 'comer', 'pronoun': 'ellos'}]},
    },
    "grammar_gerund_4": {
        "title": "Gerund (4/4)",
        "grammar_level": 18,
        "lesson_number": 4,
        "word_workload": ['beber', 'inhibir', 'prohibir', 'salir'],
        "video_embed_id": "Xpma6w0jy7m",
        "drill_type": "conjugation",
        "tense": "gerund",
        "drill_config": {
            "answers": {
            "beber": {"yo": "estoy bebiendo", "tú": "estás bebiendo", "él": "está bebiendo", "ella": "está bebiendo", "usted": "está bebiendo", "nosotros": "estamos bebiendo", "nosotras": "estamos bebiendo", "ellos": "están bebiendo", "ellas": "están bebiendo", "ustedes": "están bebiendo"},
            "inhibir": {"yo": "estoy inhibiendo", "tú": "estás inhibiendo", "él": "está inhibiendo", "ella": "está inhibiendo", "usted": "está inhibiendo", "nosotros": "estamos inhibiendo", "nosotras": "estamos inhibiendo", "ellos": "están inhibiendo", "ellas": "están inhibiendo", "ustedes": "están inhibiendo"},
            "prohibir": {"yo": "estoy prohibiendo", "tú": "estás prohibiendo", "él": "está prohibiendo", "ella": "está prohibiendo", "usted": "está prohibiendo", "nosotros": "estamos prohibiendo", "nosotras": "estamos prohibiendo", "ellos": "están prohibiendo", "ellas": "están prohibiendo", "ustedes": "están prohibiendo"},
            "salir": {"yo": "estoy saliendo", "tú": "estás saliendo", "él": "está saliendo", "ella": "está saliendo", "usted": "está saliendo", "nosotros": "estamos saliendo", "nosotras": "estamos saliendo", "ellos": "están saliendo", "ellas": "están saliendo", "ustedes": "están saliendo"},
            },
        },
        "lesson_type": "conjugation",
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You are drinking the water", "es": "Tú estás bebiendo el agua", "noun_id": "agua", "type": "written"},
            {"en": "You (formal) are drinking the coffee", "es": "Usted está bebiendo el café", "noun_id": "café", "type": "auditory"},
            {"en": "I am inhibiting it", "es": "Yo estoy inhibiendo eso", "noun_id": None, "type": "written"},
            {"en": "We (f) are inhibiting now", "es": "Nosotras estamos inhibiendo ahora", "noun_id": None, "type": "auditory"},
            {"en": "They are inhibiting here", "es": "Ellos están inhibiendo aquí", "noun_id": None, "type": "written"},
            {"en": "She is prohibiting the entry", "es": "Ella está prohibiendo la entrada", "noun_id": None, "type": "auditory"},
            {"en": "We are prohibiting it", "es": "Nosotros estamos prohibiendo eso", "noun_id": None, "type": "written"},
            {"en": "He is leaving now", "es": "Él está saliendo ahora", "noun_id": None, "type": "auditory"},
            {"en": "They (f) are leaving the house", "es": "Ellas están saliendo de la casa", "noun_id": "casa", "type": "written"},
            {"en": "You all are leaving the city", "es": "Ustedes están saliendo de la ciudad", "noun_id": "ciudad", "type": "auditory"},
        ],
        "drill_targets": [
            {"verb": "beber", "pronoun": "tú"},
            {"verb": "beber", "pronoun": "usted"},
            {"verb": "inhibir", "pronoun": "yo"},
            {"verb": "inhibir", "pronoun": "nosotras"},
            {"verb": "inhibir", "pronoun": "ellos"},
            {"verb": "prohibir", "pronoun": "ella"},
            {"verb": "prohibir", "pronoun": "nosotros"},
            {"verb": "salir", "pronoun": "él"},
            {"verb": "salir", "pronoun": "ellas"},
            {"verb": "salir", "pronoun": "ustedes"},
        ],
        "phase_2_config": {
            "description": "Gerund lesson 4: beber, inhibir, prohibir, salir",
            "targets": [
                {"verb": "beber", "pronoun": "tú"},
            {"verb": "beber", "pronoun": "usted"},
            {"verb": "inhibir", "pronoun": "yo"},
            {"verb": "inhibir", "pronoun": "nosotras"},
            {"verb": "inhibir", "pronoun": "ellos"},
            {"verb": "prohibir", "pronoun": "ella"},
            {"verb": "prohibir", "pronoun": "nosotros"},
            {"verb": "salir", "pronoun": "él"},
            {"verb": "salir", "pronoun": "ellas"},
            {"verb": "salir", "pronoun": "ustedes"},
            ],
        },
        "opener_en": "Are they going out tonight?",
        "opener_es": "¿Están saliendo esta noche?",
    },
    # --- GL 18: chat companion of `grammar_gerund_4` ---
    "grammar_gerund_4_chat": {
        "title": "Gerund (4/4) — Chat",
        "grammar_level": 18,
        "lesson_number": 4.1,
        "lesson_type": "conjugation",
        "word_workload": ["beber", "inhibir", "prohibir", "salir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "gerund",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Gerund lesson 4: beber, inhibir, prohibir, salir', 'targets': [{'verb': 'beber', 'pronoun': 'tú'}, {'verb': 'beber', 'pronoun': 'usted'}, {'verb': 'inhibir', 'pronoun': 'yo'}, {'verb': 'inhibir', 'pronoun': 'nosotras'}, {'verb': 'inhibir', 'pronoun': 'ellos'}, {'verb': 'prohibir', 'pronoun': 'ella'}, {'verb': 'prohibir', 'pronoun': 'nosotros'}, {'verb': 'salir', 'pronoun': 'él'}, {'verb': 'salir', 'pronoun': 'ellas'}, {'verb': 'salir', 'pronoun': 'ustedes'}]},
    },

    # --- GL 18.5: Perfect Tenses — placeholder (video content pending) ---
    "grammar_perfect_tenses": {
        "title": "Perfect Tenses",
        "grammar_level": 18.5,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ["haber"],
        "video_embed_id": None,  # placeholder — content not yet produced
        "drill_type": "skip",
        "tense": "perfect",
        "phases": {"0a": False, "0b": False, "1a": True, "1b": True, "1c": False, "2": True, "3": True},
        "phase_2_config": {
            "description": "Perfect tenses: present perfect, pluperfect, future perfect, conditional perfect",
            "targets": [],
        },
        "opener_en": "Have you been to the market?",
        "opener_es": "¿Has ido al mercado?",
    },

    # ─── Generated by scripts/build_grammar_lessons.py ───
    # === GL 11 — Tengo Que / Me Toca / Necesito ===
    'grammar_modal_tengo_que': {
        'title': 'Tengo Que + Inf (1/3)',
        'grammar_level': 11,
        'lesson_number': 1,
        'lesson_type': 'conjugation',
        'word_workload': [
            'hablar',
            'comer'
        ],
        'video_embed_id': None,
        'drill_type': 'ir_a_inf',
        'tense': 'modal_inf',
        'drill_config': {
            'answers': {
                'hablar': {
                    'yo': 'tengo que hablar',
                    'tú': 'tienes que hablar',
                    'él': 'tiene que hablar',
                    'ella': 'tiene que hablar',
                    'usted': 'tiene que hablar',
                    'nosotros': 'tenemos que hablar',
                    'nosotras': 'tenemos que hablar',
                    'ellos': 'tienen que hablar',
                    'ellas': 'tienen que hablar',
                    'ustedes': 'tienen que hablar'
                },
                'comer': {
                    'yo': 'tengo que comer',
                    'tú': 'tienes que comer',
                    'él': 'tiene que comer',
                    'ella': 'tiene que comer',
                    'usted': 'tiene que comer',
                    'nosotros': 'tenemos que comer',
                    'nosotras': 'tenemos que comer',
                    'ellos': 'tienen que comer',
                    'ellas': 'tienen que comer',
                    'ustedes': 'tienen que comer'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'We (f) tengo que + verb the letter',
                'es': 'Nosotras tenemos que comer la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'We (f) tengo que + verb Spanish',
                'es': 'Nosotras tenemos que hablar español',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You tengo que + verb water',
                'es': 'Tú tienes que comer agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'They (f) tengo que + verb the bread',
                'es': 'Ellas tienen que comer el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'You tengo que + verb the coffee',
                'es': 'Tú tienes que hablar el café',
                'noun_id': 'café',
                'type': 'written'
            },
            {
                'en': 'You (formal) tengo que + verb the music',
                'es': 'Usted tiene que hablar la música',
                'noun_id': 'música',
                'type': 'auditory'
            },
            {
                'en': 'I tengo que + verb the letter',
                'es': 'Yo tengo que comer la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You all tengo que + verb the book',
                'es': 'Ustedes tienen que comer el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'She tengo que + verb water',
                'es': 'Ella tiene que comer agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'I tengo que + verb at home',
                'es': 'Yo tengo que hablar en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'comer',
                'pronoun': 'yo'
            },
            {
                'verb': 'comer',
                'pronoun': 'él'
            },
            {
                'verb': 'hablar',
                'pronoun': 'nosotros'
            },
            {
                'verb': 'comer',
                'pronoun': 'ustedes'
            },
            {
                'verb': 'comer',
                'pronoun': 'ella'
            }
        ],
        'phase_2_config': {
            'description': 'Tengo Que + Inf (1/3)',
            'targets': [
                {
                    'verb': 'comer',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'él'
                },
                {
                    'verb': 'hablar',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'ella'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_modal_me_toca': {
        'title': 'Me Toca + Inf (2/3)',
        'grammar_level': 11,
        'lesson_number': 2,
        'lesson_type': 'conjugation',
        'word_workload': [
            'vivir',
            'estudiar'
        ],
        'video_embed_id': None,
        'drill_type': 'ir_a_inf',
        'tense': 'modal_inf',
        'drill_config': {
            'answers': {
                'vivir': {
                    'yo': 'me toca vivir',
                    'tú': 'te toca vivir',
                    'él': 'le toca vivir',
                    'ella': 'le toca vivir',
                    'usted': 'le toca vivir',
                    'nosotros': 'nos toca vivir',
                    'nosotras': 'nos toca vivir',
                    'ellos': 'les toca vivir',
                    'ellas': 'les toca vivir',
                    'ustedes': 'les toca vivir'
                },
                'estudiar': {
                    'yo': 'me toca estudiar',
                    'tú': 'te toca estudiar',
                    'él': 'le toca estudiar',
                    'ella': 'le toca estudiar',
                    'usted': 'le toca estudiar',
                    'nosotros': 'nos toca estudiar',
                    'nosotras': 'nos toca estudiar',
                    'ellos': 'les toca estudiar',
                    'ellas': 'les toca estudiar',
                    'ustedes': 'les toca estudiar'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'You all me toca + verb the letter',
                'es': 'Ustedes les toca vivir la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You all me toca + verb Spanish',
                'es': 'Ustedes les toca estudiar español',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'She me toca + verb water',
                'es': 'Ella le toca vivir agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'We (f) me toca + verb the bread',
                'es': 'Nosotras nos toca vivir el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'You me toca + verb the coffee',
                'es': 'Tú te toca estudiar el café',
                'noun_id': 'café',
                'type': 'written'
            },
            {
                'en': 'You (formal) me toca + verb the truth',
                'es': 'Usted le toca vivir la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'We (f) me toca + verb the song',
                'es': 'Nosotras nos toca estudiar la canción',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'They (f) me toca + verb Spanish',
                'es': 'Ellas les toca estudiar español',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You (formal) me toca + verb English',
                'es': 'Usted le toca estudiar inglés',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'I me toca + verb the bread',
                'es': 'Yo me toca vivir el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'estudiar',
                'pronoun': 'ellas'
            },
            {
                'verb': 'estudiar',
                'pronoun': 'tú'
            },
            {
                'verb': 'estudiar',
                'pronoun': 'ellos'
            },
            {
                'verb': 'vivir',
                'pronoun': 'nosotras'
            },
            {
                'verb': 'vivir',
                'pronoun': 'ustedes'
            }
        ],
        'phase_2_config': {
            'description': 'Me Toca + Inf (2/3)',
            'targets': [
                {
                    'verb': 'estudiar',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'ustedes'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_modal_necesito': {
        'title': 'Necesito + Inf (3/3)',
        'grammar_level': 11,
        'lesson_number': 3,
        'lesson_type': 'conjugation',
        'word_workload': [
            'dormir',
            'escribir'
        ],
        'video_embed_id': None,
        'drill_type': 'ir_a_inf',
        'tense': 'modal_inf',
        'drill_config': {
            'answers': {
                'dormir': {
                    'yo': 'necesito dormir',
                    'tú': 'necesitas dormir',
                    'él': 'necesita dormir',
                    'ella': 'necesita dormir',
                    'usted': 'necesita dormir',
                    'nosotros': 'necesitamos dormir',
                    'nosotras': 'necesitamos dormir',
                    'ellos': 'necesitan dormir',
                    'ellas': 'necesitan dormir',
                    'ustedes': 'necesitan dormir'
                },
                'escribir': {
                    'yo': 'necesito escribir',
                    'tú': 'necesitas escribir',
                    'él': 'necesita escribir',
                    'ella': 'necesita escribir',
                    'usted': 'necesita escribir',
                    'nosotros': 'necesitamos escribir',
                    'nosotras': 'necesitamos escribir',
                    'ellos': 'necesitan escribir',
                    'ellas': 'necesitan escribir',
                    'ustedes': 'necesitan escribir'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'They (f) necesito + verb the letter',
                'es': 'Ellas necesitan escribir la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'I necesito + verb the book',
                'es': 'Yo necesito dormir el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'They (f) necesito + verb water',
                'es': 'Ellas necesitan dormir agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (formal) necesito + verb the bread',
                'es': 'Usted necesita dormir el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'She necesito + verb here',
                'es': 'Ella necesita escribir aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You all necesito + verb the truth',
                'es': 'Ustedes necesitan escribir la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'She necesito + verb the letter',
                'es': 'Ella necesita dormir la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'We (f) necesito + verb the book',
                'es': 'Nosotras necesitamos escribir el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You (formal) necesito + verb water',
                'es': 'Usted necesita escribir agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'I necesito + verb the bread',
                'es': 'Yo necesito escribir el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'escribir',
                'pronoun': 'nosotros'
            },
            {
                'verb': 'dormir',
                'pronoun': 'yo'
            },
            {
                'verb': 'escribir',
                'pronoun': 'tú'
            },
            {
                'verb': 'dormir',
                'pronoun': 'ellas'
            },
            {
                'verb': 'escribir',
                'pronoun': 'él'
            }
        ],
        'phase_2_config': {
            'description': 'Necesito + Inf (3/3)',
            'targets': [
                {
                    'verb': 'escribir',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'dormir',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'escribir',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'dormir',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'escribir',
                    'pronoun': 'él'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_modal_chat_1': {
        'title': 'Tengo Que / Me Toca — Voice Chat',
        'grammar_level': 11,
        'lesson_number': 4,
        'lesson_type': 'conjugation',
        'word_workload': [
            'hablar',
            'comer',
            'vivir',
            'estudiar'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'modal_inf',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Tengo Que / Me Toca — Voice Chat: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'comer',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'él'
                },
                {
                    'verb': 'hablar',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'ustedes'
                }
            ]
        },
        'opener_en': 'What do you have to do today?',
        'opener_es': '¿Qué tienes que hacer hoy?',
    },
    'grammar_modal_chat_2': {
        'title': 'Necesito — Voice Chat',
        'grammar_level': 11,
        'lesson_number': 5,
        'lesson_type': 'conjugation',
        'word_workload': [
            'dormir',
            'escribir'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'modal_inf',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Necesito — Voice Chat: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'escribir',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'dormir',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'escribir',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'dormir',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'escribir',
                    'pronoun': 'él'
                },
                {
                    'verb': 'escribir',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'dormir',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'escribir',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'dormir',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'escribir',
                    'pronoun': 'él'
                }
            ]
        },
        'opener_en': 'What do you need to buy tomorrow?',
        'opener_es': '¿Qué necesitas comprar mañana?',
    },
    # === GL 12 — Imperfect ===
    'grammar_imperfect_1': {
        'title': 'Imperfect (1)',
        'grammar_level': 12,
        'lesson_number': 1,
        'lesson_type': 'conjugation',
        'word_workload': [
            'hablar',
            'escuchar'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'imperfect',
        'drill_config': {
            'answers': {
                'hablar': {
                    'yo': 'hablaba',
                    'tú': 'hablabas',
                    'él': 'hablaba',
                    'ella': 'hablaba',
                    'usted': 'hablaba',
                    'nosotros': 'hablábamos',
                    'nosotras': 'hablábamos',
                    'ellos': 'hablaban',
                    'ellas': 'hablaban',
                    'ustedes': 'hablaban'
                },
                'escuchar': {
                    'yo': 'escuchaba',
                    'tú': 'escuchabas',
                    'él': 'escuchaba',
                    'ella': 'escuchaba',
                    'usted': 'escuchaba',
                    'nosotros': 'escuchábamos',
                    'nosotras': 'escuchábamos',
                    'ellos': 'escuchaban',
                    'ellas': 'escuchaban',
                    'ustedes': 'escuchaban'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'You all used to (imperfect) the song',
                'es': 'Ustedes hablaban la canción',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You (formal) used to (imperfect) Spanish',
                'es': 'Usted hablaba español',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'We (f) used to (imperfect) English',
                'es': 'Nosotras escuchábamos inglés',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'We (f) used to (imperfect) at home',
                'es': 'Nosotras hablábamos en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            },
            {
                'en': 'I used to (imperfect) the coffee',
                'es': 'Yo hablaba el café',
                'noun_id': 'café',
                'type': 'written'
            },
            {
                'en': 'She used to (imperfect) the music',
                'es': 'Ella escuchaba la música',
                'noun_id': 'música',
                'type': 'auditory'
            },
            {
                'en': 'I used to (imperfect) the song',
                'es': 'Yo escuchaba la canción',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'They (f) used to (imperfect) Spanish',
                'es': 'Ellas hablaban español',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You all used to (imperfect) English',
                'es': 'Ustedes escuchaban inglés',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You (formal) used to (imperfect) at home',
                'es': 'Usted escuchaba en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'escuchar',
                'pronoun': 'nosotros'
            },
            {
                'verb': 'hablar',
                'pronoun': 'yo'
            },
            {
                'verb': 'hablar',
                'pronoun': 'ella'
            },
            {
                'verb': 'escuchar',
                'pronoun': 'ustedes'
            },
            {
                'verb': 'escuchar',
                'pronoun': 'ellos'
            }
        ],
        'phase_2_config': {
            'description': 'Imperfect (1)',
            'targets': [
                {
                    'verb': 'escuchar',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'hablar',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'hablar',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'escuchar',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'escuchar',
                    'pronoun': 'ellos'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_imperfect_2': {
        'title': 'Imperfect (2)',
        'grammar_level': 12,
        'lesson_number': 2,
        'lesson_type': 'conjugation',
        'word_workload': [
            'comer',
            'vivir'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'imperfect',
        'drill_config': {
            'answers': {
                'comer': {
                    'yo': 'comía',
                    'tú': 'comías',
                    'él': 'comía',
                    'ella': 'comía',
                    'usted': 'comía',
                    'nosotros': 'comíamos',
                    'nosotras': 'comíamos',
                    'ellos': 'comían',
                    'ellas': 'comían',
                    'ustedes': 'comían'
                },
                'vivir': {
                    'yo': 'vivía',
                    'tú': 'vivías',
                    'él': 'vivía',
                    'ella': 'vivía',
                    'usted': 'vivía',
                    'nosotros': 'vivíamos',
                    'nosotras': 'vivíamos',
                    'ellos': 'vivían',
                    'ellas': 'vivían',
                    'ustedes': 'vivían'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'You used to (imperfect) the letter',
                'es': 'Tú vivías la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You all used to (imperfect) the book',
                'es': 'Ustedes vivían el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'She used to (imperfect) water',
                'es': 'Ella vivía agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'We (f) used to (imperfect) the bread',
                'es': 'Nosotras comíamos el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'She used to (imperfect) here',
                'es': 'Ella comía aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'They (f) used to (imperfect) the truth',
                'es': 'Ellas comían la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'They (f) used to (imperfect) the letter',
                'es': 'Ellas vivían la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You all used to (imperfect) the book',
                'es': 'Ustedes comían el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'We (f) used to (imperfect) water',
                'es': 'Nosotras vivíamos agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You used to (imperfect) the bread',
                'es': 'Tú comías el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'vivir',
                'pronoun': 'tú'
            },
            {
                'verb': 'vivir',
                'pronoun': 'usted'
            },
            {
                'verb': 'vivir',
                'pronoun': 'ella'
            },
            {
                'verb': 'comer',
                'pronoun': 'usted'
            },
            {
                'verb': 'vivir',
                'pronoun': 'yo'
            }
        ],
        'phase_2_config': {
            'description': 'Imperfect (2)',
            'targets': [
                {
                    'verb': 'vivir',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'yo'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_imperfect_3': {
        'title': 'Imperfect — Chat 1',
        'grammar_level': 12,
        'lesson_number': 3,
        'lesson_type': 'conjugation',
        'word_workload': [
            'hablar',
            'escuchar',
            'comer',
            'vivir'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'imperfect',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Imperfect — Chat 1: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'escuchar',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'hablar',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'hablar',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'escuchar',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'escuchar',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'yo'
                }
            ]
        },
        'opener_en': 'What did you used to do as a kid?',
        'opener_es': '¿Qué hacías de niño?',
    },
    'grammar_imperfect_4': {
        'title': 'Imperfect (4)',
        'grammar_level': 12,
        'lesson_number': 4,
        'lesson_type': 'conjugation',
        'word_workload': [
            'ir',
            'ser'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'imperfect',
        'drill_config': {
            'answers': {
                'ir': {
                    'yo': 'iba',
                    'tú': 'ibas',
                    'él': 'iba',
                    'ella': 'iba',
                    'usted': 'iba',
                    'nosotros': 'íbamos',
                    'nosotras': 'íbamos',
                    'ellos': 'iban',
                    'ellas': 'iban',
                    'ustedes': 'iban'
                },
                'ser': {
                    'yo': 'era',
                    'tú': 'eras',
                    'él': 'era',
                    'ella': 'era',
                    'usted': 'era',
                    'nosotros': 'éramos',
                    'nosotras': 'éramos',
                    'ellos': 'eran',
                    'ellas': 'eran',
                    'ustedes': 'eran'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'You used to (imperfect) the letter',
                'es': 'Tú eras la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'I used to (imperfect) the book',
                'es': 'Yo iba el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You (formal) used to (imperfect) water',
                'es': 'Usted era agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (formal) used to (imperfect) the bread',
                'es': 'Usted iba el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'You used to (imperfect) here',
                'es': 'Tú ibas aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'I used to (imperfect) the truth',
                'es': 'Yo era la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You all used to (imperfect) the letter',
                'es': 'Ustedes eran la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'She used to (imperfect) the book',
                'es': 'Ella era el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'She used to (imperfect) water',
                'es': 'Ella iba agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'They (f) used to (imperfect) the bread',
                'es': 'Ellas eran el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'ser',
                'pronoun': 'ustedes'
            },
            {
                'verb': 'ser',
                'pronoun': 'yo'
            },
            {
                'verb': 'ser',
                'pronoun': 'usted'
            },
            {
                'verb': 'ser',
                'pronoun': 'nosotras'
            },
            {
                'verb': 'ir',
                'pronoun': 'ustedes'
            }
        ],
        'phase_2_config': {
            'description': 'Imperfect (4)',
            'targets': [
                {
                    'verb': 'ser',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'ser',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'ser',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'ser',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'ir',
                    'pronoun': 'ustedes'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_imperfect_5': {
        'title': 'Imperfect (5)',
        'grammar_level': 12,
        'lesson_number': 5,
        'lesson_type': 'conjugation',
        'word_workload': [
            'ver',
            'escribir'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'imperfect',
        'drill_config': {
            'answers': {
                'ver': {
                    'yo': 'veía',
                    'tú': 'veías',
                    'él': 'veía',
                    'ella': 'veía',
                    'usted': 'veía',
                    'nosotros': 'veíamos',
                    'nosotras': 'veíamos',
                    'ellos': 'veían',
                    'ellas': 'veían',
                    'ustedes': 'veían'
                },
                'escribir': {
                    'yo': 'escribía',
                    'tú': 'escribías',
                    'él': 'escribía',
                    'ella': 'escribía',
                    'usted': 'escribía',
                    'nosotros': 'escribíamos',
                    'nosotras': 'escribíamos',
                    'ellos': 'escribían',
                    'ellas': 'escribían',
                    'ustedes': 'escribían'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'They (f) used to (imperfect) the letter',
                'es': 'Ellas escribían la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You all used to (imperfect) the book',
                'es': 'Ustedes veían el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You used to (imperfect) water',
                'es': 'Tú escribías agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (formal) used to (imperfect) the bread',
                'es': 'Usted escribía el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'We (f) used to (imperfect) here',
                'es': 'Nosotras veíamos aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You (formal) used to (imperfect) the truth',
                'es': 'Usted veía la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'She used to (imperfect) the letter',
                'es': 'Ella escribía la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'I used to (imperfect) the book',
                'es': 'Yo veía el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'We (f) used to (imperfect) water',
                'es': 'Nosotras escribíamos agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'They (f) used to (imperfect) the bread',
                'es': 'Ellas veían el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'escribir',
                'pronoun': 'ellas'
            },
            {
                'verb': 'ver',
                'pronoun': 'ellos'
            },
            {
                'verb': 'escribir',
                'pronoun': 'ustedes'
            },
            {
                'verb': 'escribir',
                'pronoun': 'ellos'
            },
            {
                'verb': 'ver',
                'pronoun': 'nosotras'
            }
        ],
        'phase_2_config': {
            'description': 'Imperfect (5)',
            'targets': [
                {
                    'verb': 'escribir',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'ver',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'escribir',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'escribir',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'ver',
                    'pronoun': 'nosotras'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_imperfect_6': {
        'title': 'Imperfect — Chat 2',
        'grammar_level': 12,
        'lesson_number': 6,
        'lesson_type': 'conjugation',
        'word_workload': [
            'ir',
            'ser',
            'ver',
            'escribir'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'imperfect',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Imperfect — Chat 2: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'ser',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'ser',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'ser',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'ser',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'ir',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'escribir',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'ver',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'escribir',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'escribir',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'ver',
                    'pronoun': 'nosotras'
                }
            ]
        },
        'opener_en': 'Tell me how things used to be.',
        'opener_es': 'Cuéntame cómo eran las cosas antes.',
    },
    # === GL 13 — Reflexive ===
    'grammar_reflexive_1': {
        'title': 'Reflexive (1)',
        'grammar_level': 13,
        'lesson_number': 1,
        'lesson_type': 'conjugation',
        'word_workload': [
            'lavarse',
            'llamarse'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'reflexive_present',
        'drill_config': {
            'answers': {
                'lavarse': {
                    'yo': 'me lavo',
                    'tú': 'te lavas',
                    'él': 'se lava',
                    'ella': 'se lava',
                    'usted': 'se lava',
                    'nosotros': 'nos lavamos',
                    'nosotras': 'nos lavamos',
                    'ellos': 'se lavan',
                    'ellas': 'se lavan',
                    'ustedes': 'se lavan'
                },
                'llamarse': {
                    'yo': 'me llamo',
                    'tú': 'te llamas',
                    'él': 'se llama',
                    'ella': 'se llama',
                    'usted': 'se llama',
                    'nosotros': 'nos llamamos',
                    'nosotras': 'nos llamamos',
                    'ellos': 'se llaman',
                    'ellas': 'se llaman',
                    'ustedes': 'se llaman'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'We (f) (reflexive present) the letter',
                'es': 'Nosotras nos lavamos la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'We (f) (reflexive present) the book',
                'es': 'Nosotras nos llamamos el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'They (f) (reflexive present) water',
                'es': 'Ellas se llaman agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (reflexive present) the bread',
                'es': 'Tú te llamas el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'You (formal) (reflexive present) here',
                'es': 'Usted se llama aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'I (reflexive present) the truth',
                'es': 'Yo me llamo la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'They (f) (reflexive present) the letter',
                'es': 'Ellas se lavan la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You (reflexive present) the book',
                'es': 'Tú te lavas el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'She (reflexive present) water',
                'es': 'Ella se lava agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (formal) (reflexive present) the bread',
                'es': 'Usted se lava el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'lavarse',
                'pronoun': 'nosotros'
            },
            {
                'verb': 'lavarse',
                'pronoun': 'tú'
            },
            {
                'verb': 'lavarse',
                'pronoun': 'usted'
            },
            {
                'verb': 'lavarse',
                'pronoun': 'yo'
            },
            {
                'verb': 'llamarse',
                'pronoun': 'ellos'
            }
        ],
        'phase_2_config': {
            'description': 'Reflexive (1)',
            'targets': [
                {
                    'verb': 'lavarse',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'lavarse',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'lavarse',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'lavarse',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'llamarse',
                    'pronoun': 'ellos'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_reflexive_2': {
        'title': 'Reflexive (2)',
        'grammar_level': 13,
        'lesson_number': 2,
        'lesson_type': 'conjugation',
        'word_workload': [
            'levantarse',
            'ducharse'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'reflexive_present',
        'drill_config': {
            'answers': {
                'levantarse': {
                    'yo': 'me levanto',
                    'tú': 'te levantas',
                    'él': 'se levanta',
                    'ella': 'se levanta',
                    'usted': 'se levanta',
                    'nosotros': 'nos levantamos',
                    'nosotras': 'nos levantamos',
                    'ellos': 'se levantan',
                    'ellas': 'se levantan',
                    'ustedes': 'se levantan'
                },
                'ducharse': {
                    'yo': 'me ducho',
                    'tú': 'te duchas',
                    'él': 'se ducha',
                    'ella': 'se ducha',
                    'usted': 'se ducha',
                    'nosotros': 'nos duchamos',
                    'nosotras': 'nos duchamos',
                    'ellos': 'se duchan',
                    'ellas': 'se duchan',
                    'ustedes': 'se duchan'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'You (reflexive present) the letter',
                'es': 'Tú te duchas la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'She (reflexive present) the book',
                'es': 'Ella se ducha el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You (formal) (reflexive present) water',
                'es': 'Usted se levanta agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'They (f) (reflexive present) the bread',
                'es': 'Ellas se levantan el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'You all (reflexive present) here',
                'es': 'Ustedes se duchan aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'We (f) (reflexive present) the truth',
                'es': 'Nosotras nos levantamos la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You (reflexive present) the letter',
                'es': 'Tú te levantas la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'She (reflexive present) the book',
                'es': 'Ella se levanta el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'I (reflexive present) water',
                'es': 'Yo me levanto agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (formal) (reflexive present) the bread',
                'es': 'Usted se ducha el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'levantarse',
                'pronoun': 'ellos'
            },
            {
                'verb': 'ducharse',
                'pronoun': 'nosotras'
            },
            {
                'verb': 'levantarse',
                'pronoun': 'nosotros'
            },
            {
                'verb': 'ducharse',
                'pronoun': 'yo'
            },
            {
                'verb': 'levantarse',
                'pronoun': 'usted'
            }
        ],
        'phase_2_config': {
            'description': 'Reflexive (2)',
            'targets': [
                {
                    'verb': 'levantarse',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'ducharse',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'levantarse',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'ducharse',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'levantarse',
                    'pronoun': 'usted'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_reflexive_3': {
        'title': 'Reflexive — Chat 1',
        'grammar_level': 13,
        'lesson_number': 3,
        'lesson_type': 'conjugation',
        'word_workload': [
            'lavarse',
            'llamarse',
            'levantarse',
            'ducharse'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'reflexive_present',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Reflexive — Chat 1: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'lavarse',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'lavarse',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'lavarse',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'lavarse',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'llamarse',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'levantarse',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'ducharse',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'levantarse',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'ducharse',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'levantarse',
                    'pronoun': 'usted'
                }
            ]
        },
        'opener_en': 'Tell me about your morning routine.',
        'opener_es': 'Cuéntame sobre tu rutina de la mañana.',
    },
    'grammar_reflexive_4': {
        'title': 'Reflexive (4)',
        'grammar_level': 13,
        'lesson_number': 4,
        'lesson_type': 'conjugation',
        'word_workload': [
            'despertarse',
            'acostarse'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'reflexive_present',
        'drill_config': {
            'answers': {
                'despertarse': {
                    'yo': 'me despierto',
                    'tú': 'te despiertas',
                    'él': 'se despierta',
                    'ella': 'se despierta',
                    'usted': 'se despierta',
                    'nosotros': 'nos despertamos',
                    'nosotras': 'nos despertamos',
                    'ellos': 'se despiertan',
                    'ellas': 'se despiertan',
                    'ustedes': 'se despiertan'
                },
                'acostarse': {
                    'yo': 'me acuesto',
                    'tú': 'te acuestas',
                    'él': 'se acuesta',
                    'ella': 'se acuesta',
                    'usted': 'se acuesta',
                    'nosotros': 'nos acostamos',
                    'nosotras': 'nos acostamos',
                    'ellos': 'se acuestan',
                    'ellas': 'se acuestan',
                    'ustedes': 'se acuestan'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'They (f) (reflexive present) the letter',
                'es': 'Ellas se despiertan la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You (formal) (reflexive present) the book',
                'es': 'Usted se acuesta el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You (formal) (reflexive present) water',
                'es': 'Usted se despierta agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'They (f) (reflexive present) the bread',
                'es': 'Ellas se acuestan el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'I (reflexive present) here',
                'es': 'Yo me acuesto aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'She (reflexive present) the truth',
                'es': 'Ella se despierta la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'She (reflexive present) the letter',
                'es': 'Ella se acuesta la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You (reflexive present) the book',
                'es': 'Tú te acuestas el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'I (reflexive present) water',
                'es': 'Yo me despierto agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You all (reflexive present) the bread',
                'es': 'Ustedes se despiertan el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'acostarse',
                'pronoun': 'usted'
            },
            {
                'verb': 'despertarse',
                'pronoun': 'ustedes'
            },
            {
                'verb': 'acostarse',
                'pronoun': 'ella'
            },
            {
                'verb': 'acostarse',
                'pronoun': 'yo'
            },
            {
                'verb': 'despertarse',
                'pronoun': 'usted'
            }
        ],
        'phase_2_config': {
            'description': 'Reflexive (4)',
            'targets': [
                {
                    'verb': 'acostarse',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'despertarse',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'acostarse',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'acostarse',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'despertarse',
                    'pronoun': 'usted'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_reflexive_5': {
        'title': 'Reflexive (5)',
        'grammar_level': 13,
        'lesson_number': 5,
        'lesson_type': 'conjugation',
        'word_workload': [
            'vestirse',
            'sentarse'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'reflexive_present',
        'drill_config': {
            'answers': {
                'vestirse': {
                    'yo': 'me visto',
                    'tú': 'te vistes',
                    'él': 'se viste',
                    'ella': 'se viste',
                    'usted': 'se viste',
                    'nosotros': 'nos vestemos',
                    'nosotras': 'nos vestemos',
                    'ellos': 'se visten',
                    'ellas': 'se visten',
                    'ustedes': 'se visten'
                },
                'sentarse': {
                    'yo': 'me siento',
                    'tú': 'te sientas',
                    'él': 'se sienta',
                    'ella': 'se sienta',
                    'usted': 'se sienta',
                    'nosotros': 'nos sentamos',
                    'nosotras': 'nos sentamos',
                    'ellos': 'se sientan',
                    'ellas': 'se sientan',
                    'ustedes': 'se sientan'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'They (f) (reflexive present) the letter',
                'es': 'Ellas se sientan la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'I (reflexive present) the book',
                'es': 'Yo me visto el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You all (reflexive present) water',
                'es': 'Ustedes se sientan agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (reflexive present) the bread',
                'es': 'Tú te vistes el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'You (formal) (reflexive present) here',
                'es': 'Usted se sienta aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'They (f) (reflexive present) the truth',
                'es': 'Ellas se visten la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'We (f) (reflexive present) the letter',
                'es': 'Nosotras nos vestemos la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'I (reflexive present) the book',
                'es': 'Yo me siento el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'She (reflexive present) water',
                'es': 'Ella se sienta agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You all (reflexive present) the bread',
                'es': 'Ustedes se visten el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'vestirse',
                'pronoun': 'tú'
            },
            {
                'verb': 'sentarse',
                'pronoun': 'ella'
            },
            {
                'verb': 'sentarse',
                'pronoun': 'ustedes'
            },
            {
                'verb': 'sentarse',
                'pronoun': 'nosotras'
            },
            {
                'verb': 'vestirse',
                'pronoun': 'ellas'
            }
        ],
        'phase_2_config': {
            'description': 'Reflexive (5)',
            'targets': [
                {
                    'verb': 'vestirse',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'sentarse',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'sentarse',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'sentarse',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'vestirse',
                    'pronoun': 'ellas'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_reflexive_6': {
        'title': 'Reflexive — Chat 2',
        'grammar_level': 13,
        'lesson_number': 6,
        'lesson_type': 'conjugation',
        'word_workload': [
            'despertarse',
            'acostarse',
            'vestirse',
            'sentarse'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'reflexive_present',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Reflexive — Chat 2: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'acostarse',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'despertarse',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'acostarse',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'acostarse',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'despertarse',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'vestirse',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'sentarse',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'sentarse',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'sentarse',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'vestirse',
                    'pronoun': 'ellas'
                }
            ]
        },
        'opener_en': 'How do you get ready in the morning?',
        'opener_es': '¿Cómo te preparas en la mañana?',
    },
    # === GL 14 — Future Simple ===
    'grammar_future_1': {
        'title': 'Future Simple (1)',
        'grammar_level': 14,
        'lesson_number': 1,
        'lesson_type': 'conjugation',
        'word_workload': [
            'hablar',
            'comer'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'future',
        'drill_config': {
            'answers': {
                'hablar': {
                    'yo': 'hablaré',
                    'tú': 'hablarás',
                    'él': 'hablará',
                    'ella': 'hablará',
                    'usted': 'hablará',
                    'nosotros': 'hablaremos',
                    'nosotras': 'hablaremos',
                    'ellos': 'hablarán',
                    'ellas': 'hablarán',
                    'ustedes': 'hablarán'
                },
                'comer': {
                    'yo': 'comeré',
                    'tú': 'comerás',
                    'él': 'comerá',
                    'ella': 'comerá',
                    'usted': 'comerá',
                    'nosotros': 'comeremos',
                    'nosotras': 'comeremos',
                    'ellos': 'comerán',
                    'ellas': 'comerán',
                    'ustedes': 'comerán'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'They (f) will the song',
                'es': 'Ellas hablarán la canción',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You (formal) will the book',
                'es': 'Usted comerá el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'We (f) will water',
                'es': 'Nosotras comeremos agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You all will at home',
                'es': 'Ustedes hablarán en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            },
            {
                'en': 'We (f) will the coffee',
                'es': 'Nosotras hablaremos el café',
                'noun_id': 'café',
                'type': 'written'
            },
            {
                'en': 'You will the truth',
                'es': 'Tú comerás la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You (formal) will the song',
                'es': 'Usted hablará la canción',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'They (f) will the book',
                'es': 'Ellas comerán el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You all will water',
                'es': 'Ustedes comerán agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'I will the bread',
                'es': 'Yo comeré el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'comer',
                'pronoun': 'yo'
            },
            {
                'verb': 'comer',
                'pronoun': 'él'
            },
            {
                'verb': 'hablar',
                'pronoun': 'nosotros'
            },
            {
                'verb': 'comer',
                'pronoun': 'ustedes'
            },
            {
                'verb': 'comer',
                'pronoun': 'ella'
            }
        ],
        'phase_2_config': {
            'description': 'Future Simple (1)',
            'targets': [
                {
                    'verb': 'comer',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'él'
                },
                {
                    'verb': 'hablar',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'ella'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_future_2': {
        'title': 'Future Simple (2)',
        'grammar_level': 14,
        'lesson_number': 2,
        'lesson_type': 'conjugation',
        'word_workload': [
            'vivir',
            'estudiar'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'future',
        'drill_config': {
            'answers': {
                'vivir': {
                    'yo': 'viviré',
                    'tú': 'vivirás',
                    'él': 'vivirá',
                    'ella': 'vivirá',
                    'usted': 'vivirá',
                    'nosotros': 'viviremos',
                    'nosotras': 'viviremos',
                    'ellos': 'vivirán',
                    'ellas': 'vivirán',
                    'ustedes': 'vivirán'
                },
                'estudiar': {
                    'yo': 'estudiaré',
                    'tú': 'estudiarás',
                    'él': 'estudiará',
                    'ella': 'estudiará',
                    'usted': 'estudiará',
                    'nosotros': 'estudiaremos',
                    'nosotras': 'estudiaremos',
                    'ellos': 'estudiarán',
                    'ellas': 'estudiarán',
                    'ustedes': 'estudiarán'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'You (formal) will the letter',
                'es': 'Usted vivirá la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You will Spanish',
                'es': 'Tú estudiarás español',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'She will English',
                'es': 'Ella estudiará inglés',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You will the bread',
                'es': 'Tú vivirás el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'She will here',
                'es': 'Ella vivirá aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'We (f) will the truth',
                'es': 'Nosotras viviremos la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'We (f) will the song',
                'es': 'Nosotras estudiaremos la canción',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You all will the book',
                'es': 'Ustedes vivirán el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You (formal) will English',
                'es': 'Usted estudiará inglés',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You all will at home',
                'es': 'Ustedes estudiarán en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'estudiar',
                'pronoun': 'ellas'
            },
            {
                'verb': 'estudiar',
                'pronoun': 'tú'
            },
            {
                'verb': 'estudiar',
                'pronoun': 'ellos'
            },
            {
                'verb': 'vivir',
                'pronoun': 'nosotras'
            },
            {
                'verb': 'vivir',
                'pronoun': 'ustedes'
            }
        ],
        'phase_2_config': {
            'description': 'Future Simple (2)',
            'targets': [
                {
                    'verb': 'estudiar',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'ustedes'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_future_3': {
        'title': 'Future Simple — Chat 1',
        'grammar_level': 14,
        'lesson_number': 3,
        'lesson_type': 'conjugation',
        'word_workload': [
            'hablar',
            'comer',
            'vivir',
            'estudiar'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'future',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Future Simple — Chat 1: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'comer',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'él'
                },
                {
                    'verb': 'hablar',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'ustedes'
                }
            ]
        },
        'opener_en': 'What will you do tomorrow?',
        'opener_es': '¿Qué harás mañana?',
    },
    'grammar_future_4': {
        'title': 'Future Simple (4)',
        'grammar_level': 14,
        'lesson_number': 4,
        'lesson_type': 'conjugation',
        'word_workload': [
            'tener',
            'hacer'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'future',
        'drill_config': {
            'answers': {
                'tener': {
                    'yo': 'tendré',
                    'tú': 'tendrás',
                    'él': 'tendrá',
                    'ella': 'tendrá',
                    'usted': 'tendrá',
                    'nosotros': 'tendremos',
                    'nosotras': 'tendremos',
                    'ellos': 'tendrán',
                    'ellas': 'tendrán',
                    'ustedes': 'tendrán'
                },
                'hacer': {
                    'yo': 'haré',
                    'tú': 'harás',
                    'él': 'hará',
                    'ella': 'hará',
                    'usted': 'hará',
                    'nosotros': 'haremos',
                    'nosotras': 'haremos',
                    'ellos': 'harán',
                    'ellas': 'harán',
                    'ustedes': 'harán'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'You all will the letter',
                'es': 'Ustedes harán la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'We (f) will the book',
                'es': 'Nosotras haremos el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'They (f) will water',
                'es': 'Ellas tendrán agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (formal) will the bread',
                'es': 'Usted tendrá el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'I will here',
                'es': 'Yo tendré aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You (formal) will the truth',
                'es': 'Usted hará la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'She will the letter',
                'es': 'Ella tendrá la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'They (f) will the book',
                'es': 'Ellas harán el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'I will water',
                'es': 'Yo haré agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You will the bread',
                'es': 'Tú harás el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'tener',
                'pronoun': 'ella'
            },
            {
                'verb': 'hacer',
                'pronoun': 'nosotras'
            },
            {
                'verb': 'tener',
                'pronoun': 'usted'
            },
            {
                'verb': 'tener',
                'pronoun': 'él'
            },
            {
                'verb': 'tener',
                'pronoun': 'nosotros'
            }
        ],
        'phase_2_config': {
            'description': 'Future Simple (4)',
            'targets': [
                {
                    'verb': 'tener',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'hacer',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'tener',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'tener',
                    'pronoun': 'él'
                },
                {
                    'verb': 'tener',
                    'pronoun': 'nosotros'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_future_5': {
        'title': 'Future Simple (5)',
        'grammar_level': 14,
        'lesson_number': 5,
        'lesson_type': 'conjugation',
        'word_workload': [
            'decir',
            'poder'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'future',
        'drill_config': {
            'answers': {
                'decir': {
                    'yo': 'diré',
                    'tú': 'dirás',
                    'él': 'dirá',
                    'ella': 'dirá',
                    'usted': 'dirá',
                    'nosotros': 'diremos',
                    'nosotras': 'diremos',
                    'ellos': 'dirán',
                    'ellas': 'dirán',
                    'ustedes': 'dirán'
                },
                'poder': {
                    'yo': 'podré',
                    'tú': 'podrás',
                    'él': 'podrá',
                    'ella': 'podrá',
                    'usted': 'podrá',
                    'nosotros': 'podremos',
                    'nosotras': 'podremos',
                    'ellos': 'podrán',
                    'ellas': 'podrán',
                    'ustedes': 'podrán'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'I will the letter',
                'es': 'Yo podré la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You will the book',
                'es': 'Tú dirás el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You (formal) will water',
                'es': 'Usted dirá agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (formal) will the bread',
                'es': 'Usted podrá el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'She will here',
                'es': 'Ella dirá aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'They (f) will the truth',
                'es': 'Ellas dirán la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'I will the letter',
                'es': 'Yo diré la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You all will the book',
                'es': 'Ustedes podrán el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'We (f) will water',
                'es': 'Nosotras diremos agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'She will the bread',
                'es': 'Ella podrá el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'poder',
                'pronoun': 'ellos'
            },
            {
                'verb': 'poder',
                'pronoun': 'él'
            },
            {
                'verb': 'poder',
                'pronoun': 'ustedes'
            },
            {
                'verb': 'poder',
                'pronoun': 'ellas'
            },
            {
                'verb': 'poder',
                'pronoun': 'nosotras'
            }
        ],
        'phase_2_config': {
            'description': 'Future Simple (5)',
            'targets': [
                {
                    'verb': 'poder',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'él'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'nosotras'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_future_6': {
        'title': 'Future Simple — Chat 2',
        'grammar_level': 14,
        'lesson_number': 6,
        'lesson_type': 'conjugation',
        'word_workload': [
            'tener',
            'hacer',
            'decir',
            'poder'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'future',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Future Simple — Chat 2: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'tener',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'hacer',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'tener',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'tener',
                    'pronoun': 'él'
                },
                {
                    'verb': 'tener',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'él'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'nosotras'
                }
            ]
        },
        'opener_en': 'Tell me your plans for the weekend.',
        'opener_es': 'Cuéntame tus planes para el fin de semana.',
    },
    'grammar_future_7': {
        'title': 'Future Simple (7)',
        'grammar_level': 14,
        'lesson_number': 7,
        'lesson_type': 'conjugation',
        'word_workload': [
            'saber',
            'querer'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'future',
        'drill_config': {
            'answers': {
                'saber': {
                    'yo': 'sabré',
                    'tú': 'sabrás',
                    'él': 'sabrá',
                    'ella': 'sabrá',
                    'usted': 'sabrá',
                    'nosotros': 'sabremos',
                    'nosotras': 'sabremos',
                    'ellos': 'sabrán',
                    'ellas': 'sabrán',
                    'ustedes': 'sabrán'
                },
                'querer': {
                    'yo': 'querré',
                    'tú': 'querrás',
                    'él': 'querrá',
                    'ella': 'querrá',
                    'usted': 'querrá',
                    'nosotros': 'querremos',
                    'nosotras': 'querremos',
                    'ellos': 'querrán',
                    'ellas': 'querrán',
                    'ustedes': 'querrán'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'You all will the letter',
                'es': 'Ustedes querrán la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'She will the book',
                'es': 'Ella sabrá el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'We (f) will water',
                'es': 'Nosotras querremos agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'They (f) will the bread',
                'es': 'Ellas querrán el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'I will here',
                'es': 'Yo sabré aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'I will the truth',
                'es': 'Yo querré la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'We (f) will the letter',
                'es': 'Nosotras sabremos la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You will the book',
                'es': 'Tú sabrás el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'They (f) will water',
                'es': 'Ellas sabrán agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'She will the bread',
                'es': 'Ella querrá el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'saber',
                'pronoun': 'nosotros'
            },
            {
                'verb': 'querer',
                'pronoun': 'nosotras'
            },
            {
                'verb': 'saber',
                'pronoun': 'nosotras'
            },
            {
                'verb': 'querer',
                'pronoun': 'ellas'
            },
            {
                'verb': 'saber',
                'pronoun': 'él'
            }
        ],
        'phase_2_config': {
            'description': 'Future Simple (7)',
            'targets': [
                {
                    'verb': 'saber',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'querer',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'saber',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'querer',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'saber',
                    'pronoun': 'él'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_future_8': {
        'title': 'Future Simple (8)',
        'grammar_level': 14,
        'lesson_number': 8,
        'lesson_type': 'conjugation',
        'word_workload': [
            'venir',
            'salir'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'future',
        'drill_config': {
            'answers': {
                'venir': {
                    'yo': 'vendré',
                    'tú': 'vendrás',
                    'él': 'vendrá',
                    'ella': 'vendrá',
                    'usted': 'vendrá',
                    'nosotros': 'vendremos',
                    'nosotras': 'vendremos',
                    'ellos': 'vendrán',
                    'ellas': 'vendrán',
                    'ustedes': 'vendrán'
                },
                'salir': {
                    'yo': 'saldré',
                    'tú': 'saldrás',
                    'él': 'saldrá',
                    'ella': 'saldrá',
                    'usted': 'saldrá',
                    'nosotros': 'saldremos',
                    'nosotras': 'saldremos',
                    'ellos': 'saldrán',
                    'ellas': 'saldrán',
                    'ustedes': 'saldrán'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'You will the letter',
                'es': 'Tú saldrás la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'I will the book',
                'es': 'Yo vendré el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'We (f) will water',
                'es': 'Nosotras vendremos agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'She will the bread',
                'es': 'Ella saldrá el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'We (f) will here',
                'es': 'Nosotras saldremos aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You (formal) will the truth',
                'es': 'Usted vendrá la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You (formal) will the letter',
                'es': 'Usted saldrá la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You all will the book',
                'es': 'Ustedes vendrán el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'She will water',
                'es': 'Ella vendrá agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You will the bread',
                'es': 'Tú vendrás el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'venir',
                'pronoun': 'ella'
            },
            {
                'verb': 'salir',
                'pronoun': 'ellas'
            },
            {
                'verb': 'salir',
                'pronoun': 'ustedes'
            },
            {
                'verb': 'salir',
                'pronoun': 'él'
            },
            {
                'verb': 'venir',
                'pronoun': 'yo'
            }
        ],
        'phase_2_config': {
            'description': 'Future Simple (8)',
            'targets': [
                {
                    'verb': 'venir',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'salir',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'salir',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'salir',
                    'pronoun': 'él'
                },
                {
                    'verb': 'venir',
                    'pronoun': 'yo'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_future_9': {
        'title': 'Future Simple — Chat 3',
        'grammar_level': 14,
        'lesson_number': 9,
        'lesson_type': 'conjugation',
        'word_workload': [
            'saber',
            'querer',
            'venir',
            'salir'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'future',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Future Simple — Chat 3: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'saber',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'querer',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'saber',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'querer',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'saber',
                    'pronoun': 'él'
                },
                {
                    'verb': 'venir',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'salir',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'salir',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'salir',
                    'pronoun': 'él'
                },
                {
                    'verb': 'venir',
                    'pronoun': 'yo'
                }
            ]
        },
        'opener_en': 'What will the next year bring?',
        'opener_es': '¿Qué traerá el próximo año?',
    },
    # === GL 15 — Conditional ===
    'grammar_conditional_1': {
        'title': 'Conditional (1)',
        'grammar_level': 15,
        'lesson_number': 1,
        'lesson_type': 'conjugation',
        'word_workload': [
            'hablar',
            'comer'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'conditional',
        'drill_config': {
            'answers': {
                'hablar': {
                    'yo': 'hablaría',
                    'tú': 'hablarías',
                    'él': 'hablaría',
                    'ella': 'hablaría',
                    'usted': 'hablaría',
                    'nosotros': 'hablaríamos',
                    'nosotras': 'hablaríamos',
                    'ellos': 'hablarían',
                    'ellas': 'hablarían',
                    'ustedes': 'hablarían'
                },
                'comer': {
                    'yo': 'comería',
                    'tú': 'comerías',
                    'él': 'comería',
                    'ella': 'comería',
                    'usted': 'comería',
                    'nosotros': 'comeríamos',
                    'nosotras': 'comeríamos',
                    'ellos': 'comerían',
                    'ellas': 'comerían',
                    'ustedes': 'comerían'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'You all would the letter',
                'es': 'Ustedes comerían la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'She would the book',
                'es': 'Ella comería el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'I would English',
                'es': 'Yo hablaría inglés',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'She would at home',
                'es': 'Ella hablaría en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            },
            {
                'en': 'We (f) would here',
                'es': 'Nosotras comeríamos aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You all would the music',
                'es': 'Ustedes hablarían la música',
                'noun_id': 'música',
                'type': 'auditory'
            },
            {
                'en': 'They (f) would the letter',
                'es': 'Ellas comerían la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You (formal) would the book',
                'es': 'Usted comería el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'They (f) would English',
                'es': 'Ellas hablarían inglés',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You would at home',
                'es': 'Tú hablarías en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'comer',
                'pronoun': 'yo'
            },
            {
                'verb': 'comer',
                'pronoun': 'él'
            },
            {
                'verb': 'hablar',
                'pronoun': 'nosotros'
            },
            {
                'verb': 'comer',
                'pronoun': 'ustedes'
            },
            {
                'verb': 'comer',
                'pronoun': 'ella'
            }
        ],
        'phase_2_config': {
            'description': 'Conditional (1)',
            'targets': [
                {
                    'verb': 'comer',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'él'
                },
                {
                    'verb': 'hablar',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'ella'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_conditional_2': {
        'title': 'Conditional (2)',
        'grammar_level': 15,
        'lesson_number': 2,
        'lesson_type': 'conjugation',
        'word_workload': [
            'vivir',
            'estudiar'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'conditional',
        'drill_config': {
            'answers': {
                'vivir': {
                    'yo': 'viviría',
                    'tú': 'vivirías',
                    'él': 'viviría',
                    'ella': 'viviría',
                    'usted': 'viviría',
                    'nosotros': 'viviríamos',
                    'nosotras': 'viviríamos',
                    'ellos': 'vivirían',
                    'ellas': 'vivirían',
                    'ustedes': 'vivirían'
                },
                'estudiar': {
                    'yo': 'estudiaría',
                    'tú': 'estudiarías',
                    'él': 'estudiaría',
                    'ella': 'estudiaría',
                    'usted': 'estudiaría',
                    'nosotros': 'estudiaríamos',
                    'nosotras': 'estudiaríamos',
                    'ellos': 'estudiarían',
                    'ellas': 'estudiarían',
                    'ustedes': 'estudiarían'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'I would the letter',
                'es': 'Yo viviría la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You all would Spanish',
                'es': 'Ustedes estudiarían español',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You would water',
                'es': 'Tú vivirías agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (formal) would at home',
                'es': 'Usted estudiaría en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            },
            {
                'en': 'You would the coffee',
                'es': 'Tú estudiarías el café',
                'noun_id': 'café',
                'type': 'written'
            },
            {
                'en': 'She would the truth',
                'es': 'Ella viviría la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'They (f) would the letter',
                'es': 'Ellas vivirían la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You all would the book',
                'es': 'Ustedes vivirían el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You (formal) would water',
                'es': 'Usted viviría agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'She would at home',
                'es': 'Ella estudiaría en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'estudiar',
                'pronoun': 'ellas'
            },
            {
                'verb': 'estudiar',
                'pronoun': 'tú'
            },
            {
                'verb': 'estudiar',
                'pronoun': 'ellos'
            },
            {
                'verb': 'vivir',
                'pronoun': 'nosotras'
            },
            {
                'verb': 'vivir',
                'pronoun': 'ustedes'
            }
        ],
        'phase_2_config': {
            'description': 'Conditional (2)',
            'targets': [
                {
                    'verb': 'estudiar',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'ustedes'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_conditional_3': {
        'title': 'Conditional — Chat 1',
        'grammar_level': 15,
        'lesson_number': 3,
        'lesson_type': 'conjugation',
        'word_workload': [
            'hablar',
            'comer',
            'vivir',
            'estudiar'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'conditional',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Conditional — Chat 1: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'comer',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'él'
                },
                {
                    'verb': 'hablar',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'ustedes'
                }
            ]
        },
        'opener_en': 'What would you do with a million dollars?',
        'opener_es': '¿Qué harías con un millón de dólares?',
    },
    'grammar_conditional_4': {
        'title': 'Conditional (4)',
        'grammar_level': 15,
        'lesson_number': 4,
        'lesson_type': 'conjugation',
        'word_workload': [
            'tener',
            'hacer'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'conditional',
        'drill_config': {
            'answers': {
                'tener': {
                    'yo': 'tendría',
                    'tú': 'tendrías',
                    'él': 'tendría',
                    'ella': 'tendría',
                    'usted': 'tendría',
                    'nosotros': 'tendríamos',
                    'nosotras': 'tendríamos',
                    'ellos': 'tendrían',
                    'ellas': 'tendrían',
                    'ustedes': 'tendrían'
                },
                'hacer': {
                    'yo': 'haría',
                    'tú': 'harías',
                    'él': 'haría',
                    'ella': 'haría',
                    'usted': 'haría',
                    'nosotros': 'haríamos',
                    'nosotras': 'haríamos',
                    'ellos': 'harían',
                    'ellas': 'harían',
                    'ustedes': 'harían'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'They (f) would the letter',
                'es': 'Ellas tendrían la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You would the book',
                'es': 'Tú tendrías el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'She would water',
                'es': 'Ella haría agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'They (f) would the bread',
                'es': 'Ellas harían el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'You all would here',
                'es': 'Ustedes harían aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'I would the truth',
                'es': 'Yo tendría la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'We (f) would the letter',
                'es': 'Nosotras tendríamos la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You would the book',
                'es': 'Tú harías el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You all would water',
                'es': 'Ustedes tendrían agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'I would the bread',
                'es': 'Yo haría el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'tener',
                'pronoun': 'ella'
            },
            {
                'verb': 'hacer',
                'pronoun': 'nosotras'
            },
            {
                'verb': 'tener',
                'pronoun': 'usted'
            },
            {
                'verb': 'tener',
                'pronoun': 'él'
            },
            {
                'verb': 'tener',
                'pronoun': 'nosotros'
            }
        ],
        'phase_2_config': {
            'description': 'Conditional (4)',
            'targets': [
                {
                    'verb': 'tener',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'hacer',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'tener',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'tener',
                    'pronoun': 'él'
                },
                {
                    'verb': 'tener',
                    'pronoun': 'nosotros'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_conditional_5': {
        'title': 'Conditional (5)',
        'grammar_level': 15,
        'lesson_number': 5,
        'lesson_type': 'conjugation',
        'word_workload': [
            'decir',
            'poder'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'conditional',
        'drill_config': {
            'answers': {
                'decir': {
                    'yo': 'diría',
                    'tú': 'dirías',
                    'él': 'diría',
                    'ella': 'diría',
                    'usted': 'diría',
                    'nosotros': 'diríamos',
                    'nosotras': 'diríamos',
                    'ellos': 'dirían',
                    'ellas': 'dirían',
                    'ustedes': 'dirían'
                },
                'poder': {
                    'yo': 'podría',
                    'tú': 'podrías',
                    'él': 'podría',
                    'ella': 'podría',
                    'usted': 'podría',
                    'nosotros': 'podríamos',
                    'nosotras': 'podríamos',
                    'ellos': 'podrían',
                    'ellas': 'podrían',
                    'ustedes': 'podrían'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'You would the letter',
                'es': 'Tú podrías la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'I would the book',
                'es': 'Yo podría el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'They (f) would water',
                'es': 'Ellas dirían agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You all would the bread',
                'es': 'Ustedes dirían el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'She would here',
                'es': 'Ella diría aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'We (f) would the truth',
                'es': 'Nosotras podríamos la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You all would the letter',
                'es': 'Ustedes podrían la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You would the book',
                'es': 'Tú dirías el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'I would water',
                'es': 'Yo diría agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (formal) would the bread',
                'es': 'Usted podría el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'poder',
                'pronoun': 'ellos'
            },
            {
                'verb': 'poder',
                'pronoun': 'él'
            },
            {
                'verb': 'poder',
                'pronoun': 'ustedes'
            },
            {
                'verb': 'poder',
                'pronoun': 'ellas'
            },
            {
                'verb': 'poder',
                'pronoun': 'nosotras'
            }
        ],
        'phase_2_config': {
            'description': 'Conditional (5)',
            'targets': [
                {
                    'verb': 'poder',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'él'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'nosotras'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_conditional_6': {
        'title': 'Conditional — Chat 2',
        'grammar_level': 15,
        'lesson_number': 6,
        'lesson_type': 'conjugation',
        'word_workload': [
            'tener',
            'hacer',
            'decir',
            'poder'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'conditional',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Conditional — Chat 2: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'tener',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'hacer',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'tener',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'tener',
                    'pronoun': 'él'
                },
                {
                    'verb': 'tener',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'él'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'nosotras'
                }
            ]
        },
        'opener_en': 'Where would you live if you could choose?',
        'opener_es': '¿Dónde vivirías si pudieras elegir?',
    },
    # === GL 16 — Preterite vs Imperfect ===
    'grammar_pret_vs_imperfect': {
        'title': 'Preterite vs. Imperfect',
        'grammar_level': 16,
        'lesson_number': 1,
        'lesson_type': 'rule',
        'word_workload': [
            'preterite',
            'imperfect'
        ],
        'video_embed_id': None,
        'drill_type': 'rule',
        'tense': 'preterite_imperfect',
        'phases': {
            '0a': False,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        "rule_chart": {'kind': 'comparison', 'title': 'Preterite vs. Imperfect', 'left': {'heading': 'preterite', 'items': ['Completed actions with a clear endpoint', 'Specific moment in time', 'Series of finished events', 'Examples: comí ayer, viví allí cinco años']}, 'right': {'heading': 'imperfect', 'items': ['Habitual / repeated past actions', 'Background description / setting', 'Ongoing state of being or feeling', 'Examples: comía todos los días, era niño']}, 'footnote': 'Snapshot vs. movie: preterite is the photo, imperfect is the video.'},
        'drill_sentences': [
            {"en": "I was reading when she arrived", "es": "Yo leía cuando ella llegó", "noun_id": None, "type": "written"},
            {"en": "We used to play every day", "es": "Jugábamos todos los días", "noun_id": None, "type": "auditory"},
            {"en": "He ate the bread", "es": "Él comió el pan", "noun_id": "pan", "type": "written"},
            {"en": "She was eating when I called", "es": "Ella comía cuando yo llamé", "noun_id": None, "type": "auditory"},
            {"en": "It was raining all morning", "es": "Llovía toda la mañana", "noun_id": None, "type": "written"},
            {"en": "It rained yesterday", "es": "Llovió ayer", "noun_id": None, "type": "auditory"},
            {"en": "I was tired", "es": "Yo estaba cansado", "noun_id": None, "type": "written"},
            {"en": "I was tired for an hour", "es": "Estuve cansado por una hora", "noun_id": "hora", "type": "auditory"},
            {"en": "When I was a kid, I used to live in Mexico", "es": "Cuando era niño, vivía en México", "noun_id": None, "type": "written"},
            {"en": "She lived in Mexico for five years", "es": "Ella vivió en México por cinco años", "noun_id": None, "type": "auditory"}
        ],
        'phase_2_config': {
            'description': 'Choosing between preterite (completed) and imperfect (ongoing/habitual)',
            'targets': [
                {
                    'word': 'preterite'
                },
                {
                    'word': 'imperfect'
                }
            ]
        },
        'opener_en': 'Tell me about a memorable day from your childhood.',
        'opener_es': 'Cuéntame de un día memorable de tu niñez.',
    },
    # --- GL 16: chat companion of `grammar_pret_vs_imperfect` ---
    "grammar_pret_vs_imperfect_chat": {
        "title": "Preterite vs. Imperfect — Chat",
        "grammar_level": 16,
        "lesson_number": 1.1,
        "lesson_type": "rule",
        "word_workload": ["preterite", "imperfect"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "preterite_imperfect",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Choosing between preterite (completed) and imperfect (ongoing/habitual)', 'targets': [{'word': 'preterite'}, {'word': 'imperfect'}]},
    },
    # === GL 17.2 — Preterite Spelling Changes ===
    'grammar_pret_spelling_1': {
        'title': 'Preterite Spelling Changes (1)',
        'grammar_level': 17.2,
        'lesson_number': 1,
        'lesson_type': 'conjugation',
        'word_workload': [
            'pagar',
            'jugar'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'preterite',
        'drill_config': {
            'answers': {
                'pagar': {
                    'yo': 'pagué',
                    'tú': 'pagaste',
                    'él': 'pagó',
                    'ella': 'pagó',
                    'usted': 'pagó',
                    'nosotros': 'pagamos',
                    'nosotras': 'pagamos',
                    'ellos': 'pagaron',
                    'ellas': 'pagaron',
                    'ustedes': 'pagaron'
                },
                'jugar': {
                    'yo': 'jugué',
                    'tú': 'jugaste',
                    'él': 'jugó',
                    'ella': 'jugó',
                    'usted': 'jugó',
                    'nosotros': 'jugamos',
                    'nosotras': 'jugamos',
                    'ellos': 'jugaron',
                    'ellas': 'jugaron',
                    'ustedes': 'jugaron'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'We (f) (preterite) the song',
                'es': 'Nosotras jugamos la canción',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You (preterite) Spanish',
                'es': 'Tú pagaste español',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You (preterite) English',
                'es': 'Tú jugaste inglés',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'She (preterite) at home',
                'es': 'Ella pagó en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            },
            {
                'en': 'You (formal) (preterite) the coffee',
                'es': 'Usted jugó el café',
                'noun_id': 'café',
                'type': 'written'
            },
            {
                'en': 'You all (preterite) the music',
                'es': 'Ustedes pagaron la música',
                'noun_id': 'música',
                'type': 'auditory'
            },
            {
                'en': 'They (f) (preterite) the song',
                'es': 'Ellas pagaron la canción',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You (formal) (preterite) Spanish',
                'es': 'Usted pagó español',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'We (f) (preterite) English',
                'es': 'Nosotras pagamos inglés',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'They (f) (preterite) at home',
                'es': 'Ellas jugaron en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'pagar',
                'pronoun': 'nosotros'
            },
            {
                'verb': 'pagar',
                'pronoun': 'usted'
            },
            {
                'verb': 'pagar',
                'pronoun': 'ustedes'
            },
            {
                'verb': 'jugar',
                'pronoun': 'ustedes'
            },
            {
                'verb': 'jugar',
                'pronoun': 'ellas'
            }
        ],
        'phase_2_config': {
            'description': 'Preterite Spelling Changes (1)',
            'targets': [
                {
                    'verb': 'pagar',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'pagar',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'pagar',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'jugar',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'jugar',
                    'pronoun': 'ellas'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_pret_spelling_2': {
        'title': 'Preterite Spelling Changes (2)',
        'grammar_level': 17.2,
        'lesson_number': 2,
        'lesson_type': 'conjugation',
        'word_workload': [
            'buscar',
            'tocar'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'preterite',
        'drill_config': {
            'answers': {
                'buscar': {
                    'yo': 'busqué',
                    'tú': 'buscaste',
                    'él': 'buscó',
                    'ella': 'buscó',
                    'usted': 'buscó',
                    'nosotros': 'buscamos',
                    'nosotras': 'buscamos',
                    'ellos': 'buscaron',
                    'ellas': 'buscaron',
                    'ustedes': 'buscaron'
                },
                'tocar': {
                    'yo': 'toqué',
                    'tú': 'tocaste',
                    'él': 'tocó',
                    'ella': 'tocó',
                    'usted': 'tocó',
                    'nosotros': 'tocamos',
                    'nosotras': 'tocamos',
                    'ellos': 'tocaron',
                    'ellas': 'tocaron',
                    'ustedes': 'tocaron'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'We (f) (preterite) the song',
                'es': 'Nosotras buscamos la canción',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You (preterite) Spanish',
                'es': 'Tú buscaste español',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You (preterite) English',
                'es': 'Tú tocaste inglés',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'I (preterite) at home',
                'es': 'Yo toqué en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            },
            {
                'en': 'They (f) (preterite) the coffee',
                'es': 'Ellas buscaron el café',
                'noun_id': 'café',
                'type': 'written'
            },
            {
                'en': 'They (f) (preterite) the music',
                'es': 'Ellas tocaron la música',
                'noun_id': 'música',
                'type': 'auditory'
            },
            {
                'en': 'You all (preterite) the song',
                'es': 'Ustedes tocaron la canción',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You (formal) (preterite) Spanish',
                'es': 'Usted tocó español',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'She (preterite) English',
                'es': 'Ella tocó inglés',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You all (preterite) at home',
                'es': 'Ustedes buscaron en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'tocar',
                'pronoun': 'él'
            },
            {
                'verb': 'tocar',
                'pronoun': 'ella'
            },
            {
                'verb': 'buscar',
                'pronoun': 'usted'
            },
            {
                'verb': 'tocar',
                'pronoun': 'ellas'
            },
            {
                'verb': 'tocar',
                'pronoun': 'ustedes'
            }
        ],
        'phase_2_config': {
            'description': 'Preterite Spelling Changes (2)',
            'targets': [
                {
                    'verb': 'tocar',
                    'pronoun': 'él'
                },
                {
                    'verb': 'tocar',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'buscar',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'tocar',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'tocar',
                    'pronoun': 'ustedes'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_pret_spelling_3': {
        'title': 'Preterite Spelling Changes — Chat 1',
        'grammar_level': 17.2,
        'lesson_number': 3,
        'lesson_type': 'conjugation',
        'word_workload': [
            'pagar',
            'jugar',
            'buscar',
            'tocar'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'preterite',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Preterite Spelling Changes — Chat 1: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'pagar',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'pagar',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'pagar',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'jugar',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'jugar',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'tocar',
                    'pronoun': 'él'
                },
                {
                    'verb': 'tocar',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'buscar',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'tocar',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'tocar',
                    'pronoun': 'ustedes'
                }
            ]
        },
        'opener_en': 'Tell me what you bought yesterday.',
        'opener_es': 'Cuéntame qué compraste ayer.',
    },
    'grammar_pret_spelling_4': {
        'title': 'Preterite Spelling Changes (4)',
        'grammar_level': 17.2,
        'lesson_number': 4,
        'lesson_type': 'conjugation',
        'word_workload': [
            'empezar',
            'almorzar'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'preterite',
        'drill_config': {
            'answers': {
                'empezar': {
                    'yo': 'empecé',
                    'tú': 'empezaste',
                    'él': 'empezó',
                    'ella': 'empezó',
                    'usted': 'empezó',
                    'nosotros': 'empezamos',
                    'nosotras': 'empezamos',
                    'ellos': 'empezaron',
                    'ellas': 'empezaron',
                    'ustedes': 'empezaron'
                },
                'almorzar': {
                    'yo': 'almorcé',
                    'tú': 'almorzaste',
                    'él': 'almorzó',
                    'ella': 'almorzó',
                    'usted': 'almorzó',
                    'nosotros': 'almorzamos',
                    'nosotras': 'almorzamos',
                    'ellos': 'almorzaron',
                    'ellas': 'almorzaron',
                    'ustedes': 'almorzaron'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'They (f) (preterite) the song',
                'es': 'Ellas empezaron la canción',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You (formal) (preterite) Spanish',
                'es': 'Usted empezó español',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'I (preterite) English',
                'es': 'Yo almorcé inglés',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'She (preterite) at home',
                'es': 'Ella empezó en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            },
            {
                'en': 'I (preterite) the coffee',
                'es': 'Yo empecé el café',
                'noun_id': 'café',
                'type': 'written'
            },
            {
                'en': 'They (f) (preterite) the music',
                'es': 'Ellas almorzaron la música',
                'noun_id': 'música',
                'type': 'auditory'
            },
            {
                'en': 'You (preterite) the song',
                'es': 'Tú almorzaste la canción',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'We (f) (preterite) Spanish',
                'es': 'Nosotras almorzamos español',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You (preterite) English',
                'es': 'Tú empezaste inglés',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'We (f) (preterite) at home',
                'es': 'Nosotras empezamos en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'almorzar',
                'pronoun': 'nosotros'
            },
            {
                'verb': 'empezar',
                'pronoun': 'ellas'
            },
            {
                'verb': 'almorzar',
                'pronoun': 'ella'
            },
            {
                'verb': 'almorzar',
                'pronoun': 'ellos'
            },
            {
                'verb': 'almorzar',
                'pronoun': 'él'
            }
        ],
        'phase_2_config': {
            'description': 'Preterite Spelling Changes (4)',
            'targets': [
                {
                    'verb': 'almorzar',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'empezar',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'almorzar',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'almorzar',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'almorzar',
                    'pronoun': 'él'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_pret_spelling_5': {
        'title': 'Preterite Spelling Changes (5)',
        'grammar_level': 17.2,
        'lesson_number': 5,
        'lesson_type': 'conjugation',
        'word_workload': [
            'creer',
            'leer'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'preterite',
        'drill_config': {
            'answers': {
                'creer': {
                    'yo': 'creí',
                    'tú': 'creíste',
                    'él': 'creyó',
                    'ella': 'creyó',
                    'usted': 'creyó',
                    'nosotros': 'creímos',
                    'nosotras': 'creímos',
                    'ellos': 'creyeron',
                    'ellas': 'creyeron',
                    'ustedes': 'creyeron'
                },
                'leer': {
                    'yo': 'leí',
                    'tú': 'leíste',
                    'él': 'leyó',
                    'ella': 'leyó',
                    'usted': 'leyó',
                    'nosotros': 'leímos',
                    'nosotras': 'leímos',
                    'ellos': 'leyeron',
                    'ellas': 'leyeron',
                    'ustedes': 'leyeron'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'You all (preterite) the letter',
                'es': 'Ustedes leyeron la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You all (preterite) the book',
                'es': 'Ustedes creyeron el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You (formal) (preterite) water',
                'es': 'Usted leyó agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'They (f) (preterite) the bread',
                'es': 'Ellas creyeron el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'We (f) (preterite) here',
                'es': 'Nosotras leímos aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You (preterite) the truth',
                'es': 'Tú leíste la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'She (preterite) the letter',
                'es': 'Ella leyó la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'We (f) (preterite) the book',
                'es': 'Nosotras creímos el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'I (preterite) water',
                'es': 'Yo leí agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'They (f) (preterite) the bread',
                'es': 'Ellas leyeron el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'creer',
                'pronoun': 'ella'
            },
            {
                'verb': 'leer',
                'pronoun': 'ustedes'
            },
            {
                'verb': 'leer',
                'pronoun': 'él'
            },
            {
                'verb': 'creer',
                'pronoun': 'usted'
            },
            {
                'verb': 'leer',
                'pronoun': 'ella'
            }
        ],
        'phase_2_config': {
            'description': 'Preterite Spelling Changes (5)',
            'targets': [
                {
                    'verb': 'creer',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'leer',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'leer',
                    'pronoun': 'él'
                },
                {
                    'verb': 'creer',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'leer',
                    'pronoun': 'ella'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_pret_spelling_6': {
        'title': 'Preterite Spelling Changes — Chat 2',
        'grammar_level': 17.2,
        'lesson_number': 6,
        'lesson_type': 'conjugation',
        'word_workload': [
            'empezar',
            'almorzar',
            'creer',
            'leer'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'preterite',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Preterite Spelling Changes — Chat 2: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'almorzar',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'empezar',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'almorzar',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'almorzar',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'almorzar',
                    'pronoun': 'él'
                },
                {
                    'verb': 'creer',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'leer',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'leer',
                    'pronoun': 'él'
                },
                {
                    'verb': 'creer',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'leer',
                    'pronoun': 'ella'
                }
            ]
        },
        'opener_en': 'What did you read this week?',
        'opener_es': '¿Qué leíste esta semana?',
    },
    'grammar_pret_spelling_7': {
        'title': 'Preterite Spelling Changes (7)',
        'grammar_level': 17.2,
        'lesson_number': 7,
        'lesson_type': 'conjugation',
        'word_workload': [
            'caer',
            'oír'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'preterite',
        'drill_config': {
            'answers': {
                'caer': {
                    'yo': 'caí',
                    'tú': 'caíste',
                    'él': 'cayó',
                    'ella': 'cayó',
                    'usted': 'cayó',
                    'nosotros': 'caímos',
                    'nosotras': 'caímos',
                    'ellos': 'cayeron',
                    'ellas': 'cayeron',
                    'ustedes': 'cayeron'
                },
                'oír': {
                    'yo': 'oí',
                    'tú': 'oíste',
                    'él': 'oyó',
                    'ella': 'oyó',
                    'usted': 'oyó',
                    'nosotros': 'oímos',
                    'nosotras': 'oímos',
                    'ellos': 'oyeron',
                    'ellas': 'oyeron',
                    'ustedes': 'oyeron'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'You (preterite) the letter',
                'es': 'Tú oíste la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'We (f) (preterite) the book',
                'es': 'Nosotras caímos el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'We (f) (preterite) water',
                'es': 'Nosotras oímos agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (preterite) the bread',
                'es': 'Tú caíste el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'You all (preterite) here',
                'es': 'Ustedes oyeron aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You (formal) (preterite) the truth',
                'es': 'Usted cayó la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You (formal) (preterite) the letter',
                'es': 'Usted oyó la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'They (f) (preterite) the book',
                'es': 'Ellas cayeron el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You all (preterite) water',
                'es': 'Ustedes cayeron agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'I (preterite) the bread',
                'es': 'Yo oí el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'caer',
                'pronoun': 'tú'
            },
            {
                'verb': 'oír',
                'pronoun': 'ellos'
            },
            {
                'verb': 'oír',
                'pronoun': 'yo'
            },
            {
                'verb': 'oír',
                'pronoun': 'usted'
            },
            {
                'verb': 'oír',
                'pronoun': 'ustedes'
            }
        ],
        'phase_2_config': {
            'description': 'Preterite Spelling Changes (7)',
            'targets': [
                {
                    'verb': 'caer',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'oír',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'oír',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'oír',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'oír',
                    'pronoun': 'ustedes'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_pret_spelling_8': {
        'title': 'Preterite Spelling Changes (8)',
        'grammar_level': 17.2,
        'lesson_number': 8,
        'lesson_type': 'conjugation',
        'word_workload': [
            'construir',
            'fluir'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'preterite',
        'drill_config': {
            'answers': {
                'construir': {
                    'yo': 'construí',
                    'tú': 'construiste',
                    'él': 'construyó',
                    'ella': 'construyó',
                    'usted': 'construyó',
                    'nosotros': 'construimos',
                    'nosotras': 'construimos',
                    'ellos': 'construyeron',
                    'ellas': 'construyeron',
                    'ustedes': 'construyeron'
                },
                'fluir': {
                    'yo': 'fluí',
                    'tú': 'fluiste',
                    'él': 'fluyó',
                    'ella': 'fluyó',
                    'usted': 'fluyó',
                    'nosotros': 'fluimos',
                    'nosotras': 'fluimos',
                    'ellos': 'fluyeron',
                    'ellas': 'fluyeron',
                    'ustedes': 'fluyeron'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'She (preterite) the letter',
                'es': 'Ella construyó la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You (preterite) the book',
                'es': 'Tú fluiste el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'She (preterite) water',
                'es': 'Ella fluyó agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (formal) (preterite) the bread',
                'es': 'Usted fluyó el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'I (preterite) here',
                'es': 'Yo fluí aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You (preterite) the truth',
                'es': 'Tú construiste la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You all (preterite) the letter',
                'es': 'Ustedes construyeron la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'We (f) (preterite) the book',
                'es': 'Nosotras construimos el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You all (preterite) water',
                'es': 'Ustedes fluyeron agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (formal) (preterite) the bread',
                'es': 'Usted construyó el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'fluir',
                'pronoun': 'yo'
            },
            {
                'verb': 'construir',
                'pronoun': 'tú'
            },
            {
                'verb': 'fluir',
                'pronoun': 'él'
            },
            {
                'verb': 'construir',
                'pronoun': 'ella'
            },
            {
                'verb': 'fluir',
                'pronoun': 'nosotras'
            }
        ],
        'phase_2_config': {
            'description': 'Preterite Spelling Changes (8)',
            'targets': [
                {
                    'verb': 'fluir',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'construir',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'fluir',
                    'pronoun': 'él'
                },
                {
                    'verb': 'construir',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'fluir',
                    'pronoun': 'nosotras'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_pret_spelling_9': {
        'title': 'Preterite Spelling Changes — Chat 3',
        'grammar_level': 17.2,
        'lesson_number': 9,
        'lesson_type': 'conjugation',
        'word_workload': [
            'caer',
            'oír',
            'construir',
            'fluir'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'preterite',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Preterite Spelling Changes — Chat 3: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'caer',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'oír',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'oír',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'oír',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'oír',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'fluir',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'construir',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'fluir',
                    'pronoun': 'él'
                },
                {
                    'verb': 'construir',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'fluir',
                    'pronoun': 'nosotras'
                }
            ]
        },
        'opener_en': 'Did you hear the news?',
        'opener_es': '¿Oíste las noticias?',
    },
    # === GL 17.3 — Preterite Strong-Stem ===
    'grammar_pret_strong_1': {
        'title': 'Preterite Strong-Stem (1)',
        'grammar_level': 17.3,
        'lesson_number': 1,
        'lesson_type': 'conjugation',
        'word_workload': [
            'estar',
            'tener'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'preterite',
        'drill_config': {
            'answers': {
                'estar': {
                    'yo': 'estuve',
                    'tú': 'estuviste',
                    'él': 'estuvo',
                    'ella': 'estuvo',
                    'usted': 'estuvo',
                    'nosotros': 'estuvimos',
                    'nosotras': 'estuvimos',
                    'ellos': 'estuvieron',
                    'ellas': 'estuvieron',
                    'ustedes': 'estuvieron'
                },
                'tener': {
                    'yo': 'tuve',
                    'tú': 'tuviste',
                    'él': 'tuvo',
                    'ella': 'tuvo',
                    'usted': 'tuvo',
                    'nosotros': 'tuvimos',
                    'nosotras': 'tuvimos',
                    'ellos': 'tuvieron',
                    'ellas': 'tuvieron',
                    'ustedes': 'tuvieron'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'You all (preterite) the song',
                'es': 'Ustedes estuvieron la canción',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You (formal) (preterite) the book',
                'es': 'Usted tuvo el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'They (f) (preterite) water',
                'es': 'Ellas tuvieron agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (preterite) the bread',
                'es': 'Tú tuviste el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'We (f) (preterite) here',
                'es': 'Nosotras tuvimos aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'She (preterite) the music',
                'es': 'Ella estuvo la música',
                'noun_id': 'música',
                'type': 'auditory'
            },
            {
                'en': 'I (preterite) the letter',
                'es': 'Yo tuve la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You all (preterite) the book',
                'es': 'Ustedes tuvieron el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'We (f) (preterite) English',
                'es': 'Nosotras estuvimos inglés',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You (preterite) at home',
                'es': 'Tú estuviste en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'estar',
                'pronoun': 'ellos'
            },
            {
                'verb': 'estar',
                'pronoun': 'ella'
            },
            {
                'verb': 'estar',
                'pronoun': 'yo'
            },
            {
                'verb': 'estar',
                'pronoun': 'él'
            },
            {
                'verb': 'tener',
                'pronoun': 'nosotros'
            }
        ],
        'phase_2_config': {
            'description': 'Preterite Strong-Stem (1)',
            'targets': [
                {
                    'verb': 'estar',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'estar',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'estar',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'estar',
                    'pronoun': 'él'
                },
                {
                    'verb': 'tener',
                    'pronoun': 'nosotros'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_pret_strong_2': {
        'title': 'Preterite Strong-Stem (2)',
        'grammar_level': 17.3,
        'lesson_number': 2,
        'lesson_type': 'conjugation',
        'word_workload': [
            'poder',
            'poner'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'preterite',
        'drill_config': {
            'answers': {
                'poder': {
                    'yo': 'pude',
                    'tú': 'pudiste',
                    'él': 'pudo',
                    'ella': 'pudo',
                    'usted': 'pudo',
                    'nosotros': 'pudimos',
                    'nosotras': 'pudimos',
                    'ellos': 'pudieron',
                    'ellas': 'pudieron',
                    'ustedes': 'pudieron'
                },
                'poner': {
                    'yo': 'puse',
                    'tú': 'pusiste',
                    'él': 'puso',
                    'ella': 'puso',
                    'usted': 'puso',
                    'nosotros': 'pusimos',
                    'nosotras': 'pusimos',
                    'ellos': 'pusieron',
                    'ellas': 'pusieron',
                    'ustedes': 'pusieron'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'You all (preterite) the letter',
                'es': 'Ustedes pudieron la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'She (preterite) the book',
                'es': 'Ella puso el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'They (f) (preterite) water',
                'es': 'Ellas pudieron agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You all (preterite) the bread',
                'es': 'Ustedes pusieron el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'They (f) (preterite) here',
                'es': 'Ellas pusieron aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'We (f) (preterite) the truth',
                'es': 'Nosotras pusimos la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'I (preterite) the letter',
                'es': 'Yo pude la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'We (f) (preterite) the book',
                'es': 'Nosotras pudimos el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You (formal) (preterite) water',
                'es': 'Usted pudo agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'I (preterite) the bread',
                'es': 'Yo puse el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'poner',
                'pronoun': 'él'
            },
            {
                'verb': 'poder',
                'pronoun': 'ella'
            },
            {
                'verb': 'poner',
                'pronoun': 'ellas'
            },
            {
                'verb': 'poner',
                'pronoun': 'nosotras'
            },
            {
                'verb': 'poner',
                'pronoun': 'tú'
            }
        ],
        'phase_2_config': {
            'description': 'Preterite Strong-Stem (2)',
            'targets': [
                {
                    'verb': 'poner',
                    'pronoun': 'él'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'poner',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'poner',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'poner',
                    'pronoun': 'tú'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_pret_strong_3': {
        'title': 'Preterite Strong-Stem — Chat 1',
        'grammar_level': 17.3,
        'lesson_number': 3,
        'lesson_type': 'conjugation',
        'word_workload': [
            'estar',
            'tener',
            'poder',
            'poner'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'preterite',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Preterite Strong-Stem — Chat 1: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'estar',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'estar',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'estar',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'estar',
                    'pronoun': 'él'
                },
                {
                    'verb': 'tener',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'poner',
                    'pronoun': 'él'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'poner',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'poner',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'poner',
                    'pronoun': 'tú'
                }
            ]
        },
        'opener_en': 'Where were you yesterday?',
        'opener_es': '¿Dónde estuviste ayer?',
    },
    'grammar_pret_strong_4': {
        'title': 'Preterite Strong-Stem (4)',
        'grammar_level': 17.3,
        'lesson_number': 4,
        'lesson_type': 'conjugation',
        'word_workload': [
            'saber',
            'querer'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'preterite',
        'drill_config': {
            'answers': {
                'saber': {
                    'yo': 'supe',
                    'tú': 'supiste',
                    'él': 'supo',
                    'ella': 'supo',
                    'usted': 'supo',
                    'nosotros': 'supimos',
                    'nosotras': 'supimos',
                    'ellos': 'supieron',
                    'ellas': 'supieron',
                    'ustedes': 'supieron'
                },
                'querer': {
                    'yo': 'quise',
                    'tú': 'quisiste',
                    'él': 'quiso',
                    'ella': 'quiso',
                    'usted': 'quiso',
                    'nosotros': 'quisimos',
                    'nosotras': 'quisimos',
                    'ellos': 'quisieron',
                    'ellas': 'quisieron',
                    'ustedes': 'quisieron'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'You (preterite) the letter',
                'es': 'Tú supiste la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'They (f) (preterite) the book',
                'es': 'Ellas quisieron el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You all (preterite) water',
                'es': 'Ustedes supieron agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'I (preterite) the bread',
                'es': 'Yo supe el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'We (f) (preterite) here',
                'es': 'Nosotras supimos aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'She (preterite) the truth',
                'es': 'Ella quiso la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You (preterite) the letter',
                'es': 'Tú quisiste la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'They (f) (preterite) the book',
                'es': 'Ellas supieron el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You (formal) (preterite) water',
                'es': 'Usted quiso agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'I (preterite) the bread',
                'es': 'Yo quise el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'saber',
                'pronoun': 'nosotros'
            },
            {
                'verb': 'querer',
                'pronoun': 'nosotras'
            },
            {
                'verb': 'saber',
                'pronoun': 'nosotras'
            },
            {
                'verb': 'querer',
                'pronoun': 'ellas'
            },
            {
                'verb': 'saber',
                'pronoun': 'él'
            }
        ],
        'phase_2_config': {
            'description': 'Preterite Strong-Stem (4)',
            'targets': [
                {
                    'verb': 'saber',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'querer',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'saber',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'querer',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'saber',
                    'pronoun': 'él'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_pret_strong_5': {
        'title': 'Preterite Strong-Stem (5)',
        'grammar_level': 17.3,
        'lesson_number': 5,
        'lesson_type': 'conjugation',
        'word_workload': [
            'andar',
            'venir'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'preterite',
        'drill_config': {
            'answers': {
                'andar': {
                    'yo': 'anduve',
                    'tú': 'anduviste',
                    'él': 'anduvo',
                    'ella': 'anduvo',
                    'usted': 'anduvo',
                    'nosotros': 'anduvimos',
                    'nosotras': 'anduvimos',
                    'ellos': 'anduvieron',
                    'ellas': 'anduvieron',
                    'ustedes': 'anduvieron'
                },
                'venir': {
                    'yo': 'vine',
                    'tú': 'viniste',
                    'él': 'vino',
                    'ella': 'vino',
                    'usted': 'vino',
                    'nosotros': 'vinimos',
                    'nosotras': 'vinimos',
                    'ellos': 'vinieron',
                    'ellas': 'vinieron',
                    'ustedes': 'vinieron'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'We (f) (preterite) the song',
                'es': 'Nosotras anduvimos la canción',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'We (f) (preterite) the book',
                'es': 'Nosotras vinimos el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'She (preterite) English',
                'es': 'Ella anduvo inglés',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'They (f) (preterite) the bread',
                'es': 'Ellas vinieron el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'They (f) (preterite) the coffee',
                'es': 'Ellas anduvieron el café',
                'noun_id': 'café',
                'type': 'written'
            },
            {
                'en': 'She (preterite) the truth',
                'es': 'Ella vino la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You (preterite) the letter',
                'es': 'Tú viniste la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'I (preterite) the book',
                'es': 'Yo vine el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You (preterite) English',
                'es': 'Tú anduviste inglés',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You all (preterite) at home',
                'es': 'Ustedes anduvieron en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'andar',
                'pronoun': 'ellos'
            },
            {
                'verb': 'andar',
                'pronoun': 'tú'
            },
            {
                'verb': 'andar',
                'pronoun': 'nosotras'
            },
            {
                'verb': 'venir',
                'pronoun': 'ellas'
            },
            {
                'verb': 'andar',
                'pronoun': 'ellas'
            }
        ],
        'phase_2_config': {
            'description': 'Preterite Strong-Stem (5)',
            'targets': [
                {
                    'verb': 'andar',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'andar',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'andar',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'venir',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'andar',
                    'pronoun': 'ellas'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_pret_strong_6': {
        'title': 'Preterite Strong-Stem — Chat 2',
        'grammar_level': 17.3,
        'lesson_number': 6,
        'lesson_type': 'conjugation',
        'word_workload': [
            'saber',
            'querer',
            'andar',
            'venir'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'preterite',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Preterite Strong-Stem — Chat 2: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'saber',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'querer',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'saber',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'querer',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'saber',
                    'pronoun': 'él'
                },
                {
                    'verb': 'andar',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'andar',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'andar',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'venir',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'andar',
                    'pronoun': 'ellas'
                }
            ]
        },
        'opener_en': 'What did you have to do last week?',
        'opener_es': '¿Qué tuviste que hacer la semana pasada?',
    },
    'grammar_pret_strong_7': {
        'title': 'Preterite Strong-Stem (7)',
        'grammar_level': 17.3,
        'lesson_number': 7,
        'lesson_type': 'conjugation',
        'word_workload': [
            'haber',
            'caber'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'preterite',
        'drill_config': {
            'answers': {
                'haber': {
                    'yo': 'hube',
                    'tú': 'hubiste',
                    'él': 'hubo',
                    'ella': 'hubo',
                    'usted': 'hubo',
                    'nosotros': 'hubimos',
                    'nosotras': 'hubimos',
                    'ellos': 'hubieron',
                    'ellas': 'hubieron',
                    'ustedes': 'hubieron'
                },
                'caber': {
                    'yo': 'cupe',
                    'tú': 'cupiste',
                    'él': 'cupo',
                    'ella': 'cupo',
                    'usted': 'cupo',
                    'nosotros': 'cupimos',
                    'nosotras': 'cupimos',
                    'ellos': 'cupieron',
                    'ellas': 'cupieron',
                    'ustedes': 'cupieron'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'I (preterite) the letter',
                'es': 'Yo hube la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'She (preterite) the book',
                'es': 'Ella cupo el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'We (f) (preterite) water',
                'es': 'Nosotras hubimos agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You all (preterite) the bread',
                'es': 'Ustedes hubieron el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'They (f) (preterite) here',
                'es': 'Ellas hubieron aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'She (preterite) the truth',
                'es': 'Ella hubo la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You (preterite) the letter',
                'es': 'Tú cupiste la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'They (f) (preterite) the book',
                'es': 'Ellas cupieron el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You (formal) (preterite) water',
                'es': 'Usted hubo agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (formal) (preterite) the bread',
                'es': 'Usted cupo el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'caber',
                'pronoun': 'tú'
            },
            {
                'verb': 'caber',
                'pronoun': 'ellas'
            },
            {
                'verb': 'caber',
                'pronoun': 'ellos'
            },
            {
                'verb': 'haber',
                'pronoun': 'nosotras'
            },
            {
                'verb': 'haber',
                'pronoun': 'usted'
            }
        ],
        'phase_2_config': {
            'description': 'Preterite Strong-Stem (7)',
            'targets': [
                {
                    'verb': 'caber',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'caber',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'caber',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'haber',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'haber',
                    'pronoun': 'usted'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_pret_strong_8': {
        'title': 'Preterite Strong-Stem (8)',
        'grammar_level': 17.3,
        'lesson_number': 8,
        'lesson_type': 'conjugation',
        'word_workload': [
            'mantener',
            'obtener'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'preterite',
        'drill_config': {
            'answers': {
                'mantener': {
                    'yo': 'mantuve',
                    'tú': 'mantuviste',
                    'él': 'mantuvo',
                    'ella': 'mantuvo',
                    'usted': 'mantuvo',
                    'nosotros': 'mantuvimos',
                    'nosotras': 'mantuvimos',
                    'ellos': 'mantuvieron',
                    'ellas': 'mantuvieron',
                    'ustedes': 'mantuvieron'
                },
                'obtener': {
                    'yo': 'obtuve',
                    'tú': 'obtuviste',
                    'él': 'obtuvo',
                    'ella': 'obtuvo',
                    'usted': 'obtuvo',
                    'nosotros': 'obtuvimos',
                    'nosotras': 'obtuvimos',
                    'ellos': 'obtuvieron',
                    'ellas': 'obtuvieron',
                    'ustedes': 'obtuvieron'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'They (f) (preterite) the letter',
                'es': 'Ellas mantuvieron la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You all (preterite) the book',
                'es': 'Ustedes obtuvieron el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'We (f) (preterite) water',
                'es': 'Nosotras obtuvimos agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (preterite) the bread',
                'es': 'Tú obtuviste el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'You all (preterite) here',
                'es': 'Ustedes mantuvieron aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You (preterite) the truth',
                'es': 'Tú mantuviste la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You (formal) (preterite) the letter',
                'es': 'Usted mantuvo la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'We (f) (preterite) the book',
                'es': 'Nosotras mantuvimos el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'She (preterite) water',
                'es': 'Ella mantuvo agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'I (preterite) the bread',
                'es': 'Yo mantuve el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'obtener',
                'pronoun': 'ella'
            },
            {
                'verb': 'obtener',
                'pronoun': 'yo'
            },
            {
                'verb': 'obtener',
                'pronoun': 'tú'
            },
            {
                'verb': 'obtener',
                'pronoun': 'ellos'
            },
            {
                'verb': 'mantener',
                'pronoun': 'él'
            }
        ],
        'phase_2_config': {
            'description': 'Preterite Strong-Stem (8)',
            'targets': [
                {
                    'verb': 'obtener',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'obtener',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'obtener',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'obtener',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'mantener',
                    'pronoun': 'él'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_pret_strong_9': {
        'title': 'Preterite Strong-Stem — Chat 3',
        'grammar_level': 17.3,
        'lesson_number': 9,
        'lesson_type': 'conjugation',
        'word_workload': [
            'haber',
            'caber',
            'mantener',
            'obtener'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'preterite',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Preterite Strong-Stem — Chat 3: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'caber',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'caber',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'caber',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'haber',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'haber',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'obtener',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'obtener',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'obtener',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'obtener',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'mantener',
                    'pronoun': 'él'
                }
            ]
        },
        'opener_en': "Tell me about a time you couldn't do something.",
        'opener_es': 'Cuéntame de una vez que no pudiste hacer algo.',
    },
    # === GL 17.4 — Preterite DUCIR ===
    'grammar_pret_ducir_1': {
        'title': 'Preterite DUCIR (1)',
        'grammar_level': 17.4,
        'lesson_number': 1,
        'lesson_type': 'conjugation',
        'word_workload': [
            'traducir',
            'conducir'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'preterite',
        'drill_config': {
            'answers': {
                'traducir': {
                    'yo': 'traduje',
                    'tú': 'tradujiste',
                    'él': 'tradujo',
                    'ella': 'tradujo',
                    'usted': 'tradujo',
                    'nosotros': 'tradujimos',
                    'nosotras': 'tradujimos',
                    'ellos': 'tradujeron',
                    'ellas': 'tradujeron',
                    'ustedes': 'tradujeron'
                },
                'conducir': {
                    'yo': 'conduje',
                    'tú': 'condujiste',
                    'él': 'condujo',
                    'ella': 'condujo',
                    'usted': 'condujo',
                    'nosotros': 'condujimos',
                    'nosotras': 'condujimos',
                    'ellos': 'condujeron',
                    'ellas': 'condujeron',
                    'ustedes': 'condujeron'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'They (f) (preterite) the letter',
                'es': 'Ellas condujeron la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'I (preterite) the book',
                'es': 'Yo traduje el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You (formal) (preterite) water',
                'es': 'Usted tradujo agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (preterite) the bread',
                'es': 'Tú tradujiste el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'You (preterite) here',
                'es': 'Tú condujiste aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You all (preterite) the truth',
                'es': 'Ustedes tradujeron la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'We (f) (preterite) the letter',
                'es': 'Nosotras condujimos la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You all (preterite) the book',
                'es': 'Ustedes condujeron el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You (formal) (preterite) water',
                'es': 'Usted condujo agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'She (preterite) the bread',
                'es': 'Ella condujo el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'conducir',
                'pronoun': 'yo'
            },
            {
                'verb': 'traducir',
                'pronoun': 'nosotras'
            },
            {
                'verb': 'traducir',
                'pronoun': 'ella'
            },
            {
                'verb': 'conducir',
                'pronoun': 'nosotras'
            },
            {
                'verb': 'traducir',
                'pronoun': 'yo'
            }
        ],
        'phase_2_config': {
            'description': 'Preterite DUCIR (1)',
            'targets': [
                {
                    'verb': 'conducir',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'traducir',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'traducir',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'conducir',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'traducir',
                    'pronoun': 'yo'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_pret_ducir_2': {
        'title': 'Preterite DUCIR (2)',
        'grammar_level': 17.4,
        'lesson_number': 2,
        'lesson_type': 'conjugation',
        'word_workload': [
            'producir',
            'introducir'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'preterite',
        'drill_config': {
            'answers': {
                'producir': {
                    'yo': 'produje',
                    'tú': 'produjiste',
                    'él': 'produjo',
                    'ella': 'produjo',
                    'usted': 'produjo',
                    'nosotros': 'produjimos',
                    'nosotras': 'produjimos',
                    'ellos': 'produjeron',
                    'ellas': 'produjeron',
                    'ustedes': 'produjeron'
                },
                'introducir': {
                    'yo': 'introduje',
                    'tú': 'introdujiste',
                    'él': 'introdujo',
                    'ella': 'introdujo',
                    'usted': 'introdujo',
                    'nosotros': 'introdujimos',
                    'nosotras': 'introdujimos',
                    'ellos': 'introdujeron',
                    'ellas': 'introdujeron',
                    'ustedes': 'introdujeron'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'You (preterite) the letter',
                'es': 'Tú produjiste la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You (formal) (preterite) the book',
                'es': 'Usted introdujo el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You all (preterite) water',
                'es': 'Ustedes introdujeron agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (formal) (preterite) the bread',
                'es': 'Usted produjo el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'I (preterite) here',
                'es': 'Yo produje aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'We (f) (preterite) the truth',
                'es': 'Nosotras introdujimos la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'They (f) (preterite) the letter',
                'es': 'Ellas introdujeron la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'She (preterite) the book',
                'es': 'Ella produjo el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'I (preterite) water',
                'es': 'Yo introduje agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'We (f) (preterite) the bread',
                'es': 'Nosotras produjimos el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'introducir',
                'pronoun': 'yo'
            },
            {
                'verb': 'producir',
                'pronoun': 'yo'
            },
            {
                'verb': 'introducir',
                'pronoun': 'usted'
            },
            {
                'verb': 'producir',
                'pronoun': 'usted'
            },
            {
                'verb': 'introducir',
                'pronoun': 'él'
            }
        ],
        'phase_2_config': {
            'description': 'Preterite DUCIR (2)',
            'targets': [
                {
                    'verb': 'introducir',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'producir',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'introducir',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'producir',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'introducir',
                    'pronoun': 'él'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_pret_ducir_3': {
        'title': 'Preterite DUCIR — Chat 1',
        'grammar_level': 17.4,
        'lesson_number': 3,
        'lesson_type': 'conjugation',
        'word_workload': [
            'traducir',
            'conducir',
            'producir',
            'introducir'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'preterite',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Preterite DUCIR — Chat 1: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'conducir',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'traducir',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'traducir',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'conducir',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'traducir',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'introducir',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'producir',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'introducir',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'producir',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'introducir',
                    'pronoun': 'él'
                }
            ]
        },
        'opener_en': 'Did you drive yesterday?',
        'opener_es': '¿Condujiste ayer?',
    },
    # === GL 17.5 — Preterite e→i ===
    'grammar_pret_e_to_i_1': {
        'title': 'Preterite e→i (1)',
        'grammar_level': 17.5,
        'lesson_number': 1,
        'lesson_type': 'conjugation',
        'word_workload': [
            'pedir',
            'sentir'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'preterite',
        'drill_config': {
            'answers': {
                'pedir': {
                    'yo': 'pedí',
                    'tú': 'pediste',
                    'él': 'pidió',
                    'ella': 'pidió',
                    'usted': 'pidió',
                    'nosotros': 'pedimos',
                    'nosotras': 'pedimos',
                    'ellos': 'pidieron',
                    'ellas': 'pidieron',
                    'ustedes': 'pidieron'
                },
                'sentir': {
                    'yo': 'sentí',
                    'tú': 'sentiste',
                    'él': 'sintió',
                    'ella': 'sintió',
                    'usted': 'sintió',
                    'nosotros': 'sentimos',
                    'nosotras': 'sentimos',
                    'ellos': 'sintieron',
                    'ellas': 'sintieron',
                    'ustedes': 'sintieron'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'We (f) (preterite) the letter',
                'es': 'Nosotras pedimos la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'I (preterite) the book',
                'es': 'Yo sentí el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'She (preterite) water',
                'es': 'Ella sintió agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You all (preterite) the bread',
                'es': 'Ustedes sintieron el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'You (preterite) here',
                'es': 'Tú sentiste aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'We (f) (preterite) the truth',
                'es': 'Nosotras sentimos la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You (formal) (preterite) the letter',
                'es': 'Usted pidió la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You (preterite) the book',
                'es': 'Tú pediste el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'I (preterite) water',
                'es': 'Yo pedí agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'They (f) (preterite) the bread',
                'es': 'Ellas pidieron el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'sentir',
                'pronoun': 'ellas'
            },
            {
                'verb': 'sentir',
                'pronoun': 'nosotras'
            },
            {
                'verb': 'pedir',
                'pronoun': 'ellos'
            },
            {
                'verb': 'pedir',
                'pronoun': 'nosotras'
            },
            {
                'verb': 'sentir',
                'pronoun': 'nosotros'
            }
        ],
        'phase_2_config': {
            'description': 'Preterite e→i (1)',
            'targets': [
                {
                    'verb': 'sentir',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'sentir',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'pedir',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'pedir',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'sentir',
                    'pronoun': 'nosotros'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_pret_e_to_i_2': {
        'title': 'Preterite e→i (2)',
        'grammar_level': 17.5,
        'lesson_number': 2,
        'lesson_type': 'conjugation',
        'word_workload': [
            'repetir',
            'servir'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'preterite',
        'drill_config': {
            'answers': {
                'repetir': {
                    'yo': 'repetí',
                    'tú': 'repetiste',
                    'él': 'repitió',
                    'ella': 'repitió',
                    'usted': 'repitió',
                    'nosotros': 'repetimos',
                    'nosotras': 'repetimos',
                    'ellos': 'repitieron',
                    'ellas': 'repitieron',
                    'ustedes': 'repitieron'
                },
                'servir': {
                    'yo': 'serví',
                    'tú': 'serviste',
                    'él': 'sirvió',
                    'ella': 'sirvió',
                    'usted': 'sirvió',
                    'nosotros': 'servimos',
                    'nosotras': 'servimos',
                    'ellos': 'sirvieron',
                    'ellas': 'sirvieron',
                    'ustedes': 'sirvieron'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'I (preterite) the letter',
                'es': 'Yo serví la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You (preterite) the book',
                'es': 'Tú serviste el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'They (f) (preterite) water',
                'es': 'Ellas repitieron agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'They (f) (preterite) the bread',
                'es': 'Ellas sirvieron el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'You all (preterite) here',
                'es': 'Ustedes repitieron aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You (preterite) the truth',
                'es': 'Tú repetiste la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'We (f) (preterite) the letter',
                'es': 'Nosotras servimos la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'I (preterite) the book',
                'es': 'Yo repetí el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You (formal) (preterite) water',
                'es': 'Usted repitió agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'We (f) (preterite) the bread',
                'es': 'Nosotras repetimos el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'repetir',
                'pronoun': 'usted'
            },
            {
                'verb': 'servir',
                'pronoun': 'ustedes'
            },
            {
                'verb': 'repetir',
                'pronoun': 'nosotros'
            },
            {
                'verb': 'servir',
                'pronoun': 'ellas'
            },
            {
                'verb': 'repetir',
                'pronoun': 'él'
            }
        ],
        'phase_2_config': {
            'description': 'Preterite e→i (2)',
            'targets': [
                {
                    'verb': 'repetir',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'servir',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'repetir',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'servir',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'repetir',
                    'pronoun': 'él'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_pret_e_to_i_3': {
        'title': 'Preterite e→i — Chat 1',
        'grammar_level': 17.5,
        'lesson_number': 3,
        'lesson_type': 'conjugation',
        'word_workload': [
            'pedir',
            'sentir',
            'repetir',
            'servir'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'preterite',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Preterite e→i — Chat 1: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'sentir',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'sentir',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'pedir',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'pedir',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'sentir',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'repetir',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'servir',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'repetir',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'servir',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'repetir',
                    'pronoun': 'él'
                }
            ]
        },
        'opener_en': 'What did you order at the restaurant?',
        'opener_es': '¿Qué pediste en el restaurante?',
    },
    # === GL 19 — Direct + Indirect Object Pronouns ===
    'grammar_obj_direct': {
        'title': 'Direct Object Pronouns',
        'grammar_level': 19,
        'lesson_number': 1,
        'lesson_type': 'rule',
        'word_workload': [
            'lo',
            'la',
            'los',
            'las'
        ],
        'video_embed_id': None,
        'drill_type': 'rule',
        'tense': 'object_pronouns',
        'phases': {
            '0a': False,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        "rule_chart": {'kind': 'table', 'title': "Direct object pronouns — 'it / them'", 'headers': ['Pronoun', 'Replaces', 'Example'], 'rows': [['lo', 'masculine singular', 'Lo veo (the book)'], ['la', 'feminine singular', 'La compro (the bag)'], ['los', 'masculine plural / mixed', 'Los oyes (the children)'], ['las', 'feminine plural', 'Las traen (the apples)']], 'footnote': 'Position: directly before a conjugated verb (Lo veo) or attached to an infinitive/gerund (Voy a verlo).'},
        'drill_sentences': [
            {"en": "I see it", "es": "Lo veo", "noun_id": None, "type": "written"},
            {"en": "She buys them", "es": "Las compra", "noun_id": None, "type": "auditory"},
            {"en": "We eat it", "es": "Lo comemos", "noun_id": None, "type": "written"},
            {"en": "They bring her", "es": "La traen", "noun_id": None, "type": "auditory"},
            {"en": "You hear them", "es": "Los oyes", "noun_id": None, "type": "written"},
            {"en": "I read it", "es": "La leo", "noun_id": None, "type": "auditory"},
            {"en": "He drinks it", "es": "Lo bebe", "noun_id": None, "type": "written"},
            {"en": "We see them", "es": "Los vemos", "noun_id": None, "type": "auditory"},
            {"en": "She wants it", "es": "Lo quiere", "noun_id": None, "type": "written"},
            {"en": "I take her", "es": "La llevo", "noun_id": None, "type": "auditory"}
        ],
        'phase_2_config': {
            'description': 'Direct Object Pronouns',
            'targets': [
                {
                    'word': 'lo'
                },
                {
                    'word': 'la'
                },
                {
                    'word': 'los'
                },
                {
                    'word': 'las'
                }
            ]
        },
        'opener_en': 'Tell me what you do for your friends.',
        'opener_es': 'Cuéntame qué haces por tus amigos.',
    },
    # --- GL 19: chat companion of `grammar_obj_direct` ---
    "grammar_obj_direct_chat": {
        "title": "Direct Object Pronouns — Chat",
        "grammar_level": 19,
        "lesson_number": 1.1,
        "lesson_type": "rule",
        "word_workload": ["lo", "la", "los", "las"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "object_pronouns",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Direct Object Pronouns', 'targets': [{'word': 'lo'}, {'word': 'la'}, {'word': 'los'}, {'word': 'las'}]},
    },
    'grammar_obj_indirect': {
        'title': 'Indirect Object Pronouns',
        'grammar_level': 19,
        'lesson_number': 2,
        'lesson_type': 'rule',
        'word_workload': [
            'le',
            'les'
        ],
        'video_embed_id': None,
        'drill_type': 'rule',
        'tense': 'object_pronouns',
        'phases': {
            '0a': False,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        "rule_chart": {'kind': 'table', 'title': "Indirect object pronouns — 'to him / to them'", 'headers': ['Pronoun', 'Used for', 'Example'], 'rows': [['me', 'to me', 'Me da el libro'], ['te', 'to you (informal)', 'Te digo la verdad'], ['le', 'to him / her / you (formal)', 'Le doy el libro'], ['nos', 'to us', 'Nos traen comida'], ['les', 'to them / you all', 'Les pagamos']], 'footnote': 'Indirect = receiver of the action. Same position rules as direct objects.'},
        'drill_sentences': [
            {"en": "I give him the book", "es": "Le doy el libro", "noun_id": "libro", "type": "written"},
            {"en": "She tells them the truth", "es": "Les dice la verdad", "noun_id": "verdad", "type": "auditory"},
            {"en": "We bring her the food", "es": "Le traemos la comida", "noun_id": "comida", "type": "written"},
            {"en": "They send him the letter", "es": "Le mandan la carta", "noun_id": "carta", "type": "auditory"},
            {"en": "I write him a message", "es": "Le escribo un mensaje", "noun_id": "mensaje", "type": "written"},
            {"en": "We pay them the money", "es": "Les pagamos el dinero", "noun_id": "dinero", "type": "auditory"},
            {"en": "You give them the gift", "es": "Les das el regalo", "noun_id": "regalo", "type": "written"},
            {"en": "She buys him the shirt", "es": "Le compra la camisa", "noun_id": "camisa", "type": "auditory"},
            {"en": "I show him the photo", "es": "Le muestro la foto", "noun_id": "foto", "type": "written"},
            {"en": "We tell them everything", "es": "Les decimos todo", "noun_id": None, "type": "auditory"}
        ],
        'phase_2_config': {
            'description': 'Indirect Object Pronouns',
            'targets': [
                {
                    'word': 'le'
                },
                {
                    'word': 'les'
                }
            ]
        },
        'opener_en': 'Tell me what you do for your friends.',
        'opener_es': 'Cuéntame qué haces por tus amigos.',
    },
    # --- GL 19: chat companion of `grammar_obj_indirect` ---
    "grammar_obj_indirect_chat": {
        "title": "Indirect Object Pronouns — Chat",
        "grammar_level": 19,
        "lesson_number": 2.1,
        "lesson_type": "rule",
        "word_workload": ["le", "les"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "object_pronouns",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Indirect Object Pronouns', 'targets': [{'word': 'le'}, {'word': 'les'}]},
    },
    'grammar_obj_chat_1': {
        'title': 'Object Pronouns — Chat 1',
        'grammar_level': 19,
        'lesson_number': 3,
        'lesson_type': 'rule',
        'word_workload': [
            'lo',
            'la',
            'los',
            'las',
            'le',
            'les'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'object_pronouns',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Voice chat: substitute nouns with direct + indirect pronouns',
            'targets': [
                {
                    'word': 'lo'
                },
                {
                    'word': 'la'
                },
                {
                    'word': 'los'
                },
                {
                    'word': 'las'
                },
                {
                    'word': 'le'
                },
                {
                    'word': 'les'
                }
            ]
        },
        'opener_en': "Let's talk about who does what for whom.",
        'opener_es': 'Hablemos de quién hace qué por quién.',
    },
    'grammar_obj_combined_a': {
        'title': 'Combined Object Pronouns (1/2)',
        'grammar_level': 19,
        'lesson_number': 4,
        'lesson_type': 'rule',
        'word_workload': [
            'se',
            'lo',
            'la',
            'me',
            'te'
        ],
        'video_embed_id': None,
        'drill_type': 'rule',
        'tense': 'object_pronouns',
        'phases': {
            '0a': False,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'drill_sentences': [
            {"en": "She gives it to me", "es": "Me lo da", "noun_id": None, "type": "written"},
            {"en": "I give it to you", "es": "Te lo doy", "noun_id": None, "type": "auditory"},
            {"en": "She gives it to him", "es": "Se lo da", "noun_id": None, "type": "written"},
            {"en": "We bring it to her", "es": "Se lo traemos", "noun_id": None, "type": "auditory"},
            {"en": "I tell it to you", "es": "Te lo digo", "noun_id": None, "type": "written"},
            {"en": "He sends it to me", "es": "Me lo manda", "noun_id": None, "type": "auditory"},
            {"en": "She writes it to me", "es": "Me la escribe", "noun_id": None, "type": "written"},
            {"en": "We bring it to you", "es": "Te la traemos", "noun_id": None, "type": "auditory"},
            {"en": "They give it to him", "es": "Se la dan", "noun_id": None, "type": "written"},
            {"en": "I show it to her", "es": "Se la muestro", "noun_id": None, "type": "auditory"}
        ],
        'phase_2_config': {
            'description': 'Combined Object Pronouns (1/2)',
            'targets': [
                {
                    'word': 'se'
                },
                {
                    'word': 'lo'
                },
                {
                    'word': 'la'
                },
                {
                    'word': 'me'
                },
                {
                    'word': 'te'
                }
            ]
        },
        'opener_en': 'Tell me what you do for your friends.',
        'opener_es': 'Cuéntame qué haces por tus amigos.',
    },
    # --- GL 19: chat companion of `grammar_obj_combined_a` ---
    "grammar_obj_combined_a_chat": {
        "title": "Combined Object Pronouns (1/2) — Chat",
        "grammar_level": 19,
        "lesson_number": 4.1,
        "lesson_type": "rule",
        "word_workload": ["se", "lo", "la", "me", "te"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "object_pronouns",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Combined Object Pronouns (1/2)', 'targets': [{'word': 'se'}, {'word': 'lo'}, {'word': 'la'}, {'word': 'me'}, {'word': 'te'}]},
    },
    'grammar_obj_combined_b': {
        'title': 'Combined Object Pronouns (2/2)',
        'grammar_level': 19,
        'lesson_number': 5,
        'lesson_type': 'rule',
        'word_workload': [
            'nos',
            'los',
            'las',
            'se'
        ],
        'video_embed_id': None,
        'drill_type': 'rule',
        'tense': 'object_pronouns',
        'phases': {
            '0a': False,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'drill_sentences': [
            {"en": "They bring them to us", "es": "Nos los traen", "noun_id": None, "type": "written"},
            {"en": "She tells them to us", "es": "Nos los dice", "noun_id": None, "type": "auditory"},
            {"en": "He gives them to them", "es": "Se los da", "noun_id": None, "type": "written"},
            {"en": "We send them to her", "es": "Se las mandamos", "noun_id": None, "type": "auditory"},
            {"en": "They show them to us", "es": "Nos las muestran", "noun_id": None, "type": "written"},
            {"en": "I write them to him", "es": "Se las escribo", "noun_id": None, "type": "auditory"},
            {"en": "We pay them to them", "es": "Se los pagamos", "noun_id": None, "type": "written"},
            {"en": "You give them to us", "es": "Nos los das", "noun_id": None, "type": "auditory"},
            {"en": "She brings them to me", "es": "Me las trae", "noun_id": None, "type": "written"},
            {"en": "I send them to you", "es": "Te las mando", "noun_id": None, "type": "auditory"}
        ],
        'phase_2_config': {
            'description': 'Combined Object Pronouns (2/2)',
            'targets': [
                {
                    'word': 'nos'
                },
                {
                    'word': 'los'
                },
                {
                    'word': 'las'
                },
                {
                    'word': 'se'
                }
            ]
        },
        'opener_en': 'Tell me what you do for your friends.',
        'opener_es': 'Cuéntame qué haces por tus amigos.',
    },
    # --- GL 19: chat companion of `grammar_obj_combined_b` ---
    "grammar_obj_combined_b_chat": {
        "title": "Combined Object Pronouns (2/2) — Chat",
        "grammar_level": 19,
        "lesson_number": 5.1,
        "lesson_type": "rule",
        "word_workload": ["nos", "los", "las", "se"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "object_pronouns",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Combined Object Pronouns (2/2)', 'targets': [{'word': 'nos'}, {'word': 'los'}, {'word': 'las'}, {'word': 'se'}]},
    },
    'grammar_obj_chat_2': {
        'title': 'Object Pronouns — Chat 2',
        'grammar_level': 19,
        'lesson_number': 6,
        'lesson_type': 'rule',
        'word_workload': [
            'se',
            'me',
            'te',
            'nos',
            'lo',
            'la',
            'los',
            'las'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'object_pronouns',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Voice chat: combined object pronouns (se lo, me la, te los, etc.)',
            'targets': [
                {
                    'word': 'se'
                },
                {
                    'word': 'lo'
                },
                {
                    'word': 'la'
                },
                {
                    'word': 'me'
                },
                {
                    'word': 'te'
                },
                {
                    'word': 'nos'
                },
                {
                    'word': 'los'
                },
                {
                    'word': 'las'
                },
                {
                    'word': 'se'
                }
            ]
        },
        'opener_en': "Tell me about gifts you've given recently.",
        'opener_es': 'Cuéntame de regalos que has dado recientemente.',
    },
    # === GL 20 — Subjunctive (present + imperfect) ===
    'grammar_subj_pres_1': {
        'title': 'Present Subjunctive (1)',
        'grammar_level': 20,
        'lesson_number': 1,
        'lesson_type': 'conjugation',
        'word_workload': [
            'hablar',
            'comer'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'present_subjunctive',
        'drill_config': {
            'answers': {
                'hablar': {
                    'yo': 'hable',
                    'tú': 'hables',
                    'él': 'hable',
                    'ella': 'hable',
                    'usted': 'hable',
                    'nosotros': 'hablemos',
                    'nosotras': 'hablemos',
                    'ellos': 'hablen',
                    'ellas': 'hablen',
                    'ustedes': 'hablen'
                },
                'comer': {
                    'yo': 'coma',
                    'tú': 'comas',
                    'él': 'coma',
                    'ella': 'coma',
                    'usted': 'coma',
                    'nosotros': 'comamos',
                    'nosotras': 'comamos',
                    'ellos': 'coman',
                    'ellas': 'coman',
                    'ustedes': 'coman'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'I (that ___ ) — present subj the letter',
                'es': 'Yo coma la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You all (that ___ ) — present subj the book',
                'es': 'Ustedes coman el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You (that ___ ) — present subj water',
                'es': 'Tú comas agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'She (that ___ ) — present subj at home',
                'es': 'Ella hable en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            },
            {
                'en': 'They (f) (that ___ ) — present subj the coffee',
                'es': 'Ellas hablen el café',
                'noun_id': 'café',
                'type': 'written'
            },
            {
                'en': 'They (f) (that ___ ) — present subj the truth',
                'es': 'Ellas coman la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You (formal) (that ___ ) — present subj the letter',
                'es': 'Usted coma la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You (that ___ ) — present subj Spanish',
                'es': 'Tú hables español',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'We (f) (that ___ ) — present subj English',
                'es': 'Nosotras hablemos inglés',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You all (that ___ ) — present subj at home',
                'es': 'Ustedes hablen en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'comer',
                'pronoun': 'yo'
            },
            {
                'verb': 'comer',
                'pronoun': 'él'
            },
            {
                'verb': 'hablar',
                'pronoun': 'nosotros'
            },
            {
                'verb': 'comer',
                'pronoun': 'ustedes'
            },
            {
                'verb': 'comer',
                'pronoun': 'ella'
            }
        ],
        'phase_2_config': {
            'description': 'Present Subjunctive (1)',
            'targets': [
                {
                    'verb': 'comer',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'él'
                },
                {
                    'verb': 'hablar',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'ella'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_subj_pres_2': {
        'title': 'Present Subjunctive (2)',
        'grammar_level': 20,
        'lesson_number': 2,
        'lesson_type': 'conjugation',
        'word_workload': [
            'vivir',
            'estudiar'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'present_subjunctive',
        'drill_config': {
            'answers': {
                'vivir': {
                    'yo': 'viva',
                    'tú': 'vivas',
                    'él': 'viva',
                    'ella': 'viva',
                    'usted': 'viva',
                    'nosotros': 'vivamos',
                    'nosotras': 'vivamos',
                    'ellos': 'vivan',
                    'ellas': 'vivan',
                    'ustedes': 'vivan'
                },
                'estudiar': {
                    'yo': 'estudie',
                    'tú': 'estudies',
                    'él': 'estudie',
                    'ella': 'estudie',
                    'usted': 'estudie',
                    'nosotros': 'estudiemos',
                    'nosotras': 'estudiemos',
                    'ellos': 'estudien',
                    'ellas': 'estudien',
                    'ustedes': 'estudien'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'I (that ___ ) — present subj the letter',
                'es': 'Yo viva la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You all (that ___ ) — present subj Spanish',
                'es': 'Ustedes estudien español',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'I (that ___ ) — present subj English',
                'es': 'Yo estudie inglés',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You (formal) (that ___ ) — present subj the bread',
                'es': 'Usted viva el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'We (f) (that ___ ) — present subj here',
                'es': 'Nosotras vivamos aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You (that ___ ) — present subj the truth',
                'es': 'Tú vivas la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'She (that ___ ) — present subj the letter',
                'es': 'Ella viva la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You all (that ___ ) — present subj the book',
                'es': 'Ustedes vivan el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'She (that ___ ) — present subj English',
                'es': 'Ella estudie inglés',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'We (f) (that ___ ) — present subj at home',
                'es': 'Nosotras estudiemos en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'estudiar',
                'pronoun': 'ellas'
            },
            {
                'verb': 'estudiar',
                'pronoun': 'tú'
            },
            {
                'verb': 'estudiar',
                'pronoun': 'ellos'
            },
            {
                'verb': 'vivir',
                'pronoun': 'nosotras'
            },
            {
                'verb': 'vivir',
                'pronoun': 'ustedes'
            }
        ],
        'phase_2_config': {
            'description': 'Present Subjunctive (2)',
            'targets': [
                {
                    'verb': 'estudiar',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'ustedes'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_subj_pres_3': {
        'title': 'Present Subjunctive — Chat 1',
        'grammar_level': 20,
        'lesson_number': 3,
        'lesson_type': 'conjugation',
        'word_workload': [
            'hablar',
            'comer',
            'vivir',
            'estudiar'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'present_subjunctive',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Present Subjunctive — Chat 1: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'comer',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'él'
                },
                {
                    'verb': 'hablar',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'ustedes'
                }
            ]
        },
        'opener_en': 'What do you hope happens this week?',
        'opener_es': '¿Qué esperas que pase esta semana?',
    },
    'grammar_subj_pres_4': {
        'title': 'Present Subjunctive (4)',
        'grammar_level': 20,
        'lesson_number': 4,
        'lesson_type': 'conjugation',
        'word_workload': [
            'ser',
            'ir'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'present_subjunctive',
        'drill_config': {
            'answers': {
                'ser': {
                    'yo': 'sea',
                    'tú': 'seas',
                    'él': 'sea',
                    'ella': 'sea',
                    'usted': 'sea',
                    'nosotros': 'seamos',
                    'nosotras': 'seamos',
                    'ellos': 'sean',
                    'ellas': 'sean',
                    'ustedes': 'sean'
                },
                'ir': {
                    'yo': 'vaya',
                    'tú': 'vayas',
                    'él': 'vaya',
                    'ella': 'vaya',
                    'usted': 'vaya',
                    'nosotros': 'vayamos',
                    'nosotras': 'vayamos',
                    'ellos': 'vayan',
                    'ellas': 'vayan',
                    'ustedes': 'vayan'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'We (f) (that ___ ) — present subj the letter',
                'es': 'Nosotras seamos la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'She (that ___ ) — present subj the book',
                'es': 'Ella sea el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You (formal) (that ___ ) — present subj water',
                'es': 'Usted vaya agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (that ___ ) — present subj the bread',
                'es': 'Tú seas el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'We (f) (that ___ ) — present subj here',
                'es': 'Nosotras vayamos aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'I (that ___ ) — present subj the truth',
                'es': 'Yo vaya la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'I (that ___ ) — present subj the letter',
                'es': 'Yo sea la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You (that ___ ) — present subj the book',
                'es': 'Tú vayas el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'They (f) (that ___ ) — present subj water',
                'es': 'Ellas sean agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (formal) (that ___ ) — present subj the bread',
                'es': 'Usted sea el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'ir',
                'pronoun': 'ella'
            },
            {
                'verb': 'ser',
                'pronoun': 'yo'
            },
            {
                'verb': 'ir',
                'pronoun': 'ellas'
            },
            {
                'verb': 'ser',
                'pronoun': 'ellos'
            },
            {
                'verb': 'ir',
                'pronoun': 'él'
            }
        ],
        'phase_2_config': {
            'description': 'Present Subjunctive (4)',
            'targets': [
                {
                    'verb': 'ir',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'ser',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'ir',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'ser',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'ir',
                    'pronoun': 'él'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_subj_pres_5': {
        'title': 'Present Subjunctive (5)',
        'grammar_level': 20,
        'lesson_number': 5,
        'lesson_type': 'conjugation',
        'word_workload': [
            'estar',
            'dar'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'present_subjunctive',
        'drill_config': {
            'answers': {
                'estar': {
                    'yo': 'esté',
                    'tú': 'estés',
                    'él': 'esté',
                    'ella': 'esté',
                    'usted': 'esté',
                    'nosotros': 'estemos',
                    'nosotras': 'estemos',
                    'ellos': 'estén',
                    'ellas': 'estén',
                    'ustedes': 'estén'
                },
                'dar': {
                    'yo': 'dé',
                    'tú': 'des',
                    'él': 'dé',
                    'ella': 'dé',
                    'usted': 'dé',
                    'nosotros': 'demos',
                    'nosotras': 'demos',
                    'ellos': 'den',
                    'ellas': 'den',
                    'ustedes': 'den'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'She (that ___ ) — present subj the song',
                'es': 'Ella esté la canción',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'We (f) (that ___ ) — present subj Spanish',
                'es': 'Nosotras estemos español',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You all (that ___ ) — present subj English',
                'es': 'Ustedes estén inglés',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'They (f) (that ___ ) — present subj at home',
                'es': 'Ellas den en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            },
            {
                'en': 'You (formal) (that ___ ) — present subj the coffee',
                'es': 'Usted esté el café',
                'noun_id': 'café',
                'type': 'written'
            },
            {
                'en': 'I (that ___ ) — present subj the music',
                'es': 'Yo dé la música',
                'noun_id': 'música',
                'type': 'auditory'
            },
            {
                'en': 'You (that ___ ) — present subj the song',
                'es': 'Tú estés la canción',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'We (f) (that ___ ) — present subj Spanish',
                'es': 'Nosotras demos español',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You all (that ___ ) — present subj English',
                'es': 'Ustedes den inglés',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'They (f) (that ___ ) — present subj at home',
                'es': 'Ellas estén en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'dar',
                'pronoun': 'tú'
            },
            {
                'verb': 'dar',
                'pronoun': 'ella'
            },
            {
                'verb': 'estar',
                'pronoun': 'ella'
            },
            {
                'verb': 'estar',
                'pronoun': 'tú'
            },
            {
                'verb': 'dar',
                'pronoun': 'nosotros'
            }
        ],
        'phase_2_config': {
            'description': 'Present Subjunctive (5)',
            'targets': [
                {
                    'verb': 'dar',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'dar',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'estar',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'estar',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'dar',
                    'pronoun': 'nosotros'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_subj_pres_6': {
        'title': 'Present Subjunctive — Chat 2',
        'grammar_level': 20,
        'lesson_number': 6,
        'lesson_type': 'conjugation',
        'word_workload': [
            'ser',
            'ir',
            'estar',
            'dar'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'present_subjunctive',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Present Subjunctive — Chat 2: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'ir',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'ser',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'ir',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'ser',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'ir',
                    'pronoun': 'él'
                },
                {
                    'verb': 'dar',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'dar',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'estar',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'estar',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'dar',
                    'pronoun': 'nosotros'
                }
            ]
        },
        'opener_en': 'What do you want them to do?',
        'opener_es': '¿Qué quieres que hagan?',
    },
    'grammar_subj_pres_7': {
        'title': 'Present Subjunctive (7)',
        'grammar_level': 20,
        'lesson_number': 7,
        'lesson_type': 'conjugation',
        'word_workload': [
            'saber',
            'haber'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'present_subjunctive',
        'drill_config': {
            'answers': {
                'saber': {
                    'yo': 'sepa',
                    'tú': 'sepas',
                    'él': 'sepa',
                    'ella': 'sepa',
                    'usted': 'sepa',
                    'nosotros': 'sepamos',
                    'nosotras': 'sepamos',
                    'ellos': 'sepan',
                    'ellas': 'sepan',
                    'ustedes': 'sepan'
                },
                'haber': {
                    'yo': 'haya',
                    'tú': 'hayas',
                    'él': 'haya',
                    'ella': 'haya',
                    'usted': 'haya',
                    'nosotros': 'hayamos',
                    'nosotras': 'hayamos',
                    'ellos': 'hayan',
                    'ellas': 'hayan',
                    'ustedes': 'hayan'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'We (f) (that ___ ) — present subj the letter',
                'es': 'Nosotras sepamos la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You (formal) (that ___ ) — present subj the book',
                'es': 'Usted haya el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'We (f) (that ___ ) — present subj water',
                'es': 'Nosotras hayamos agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (that ___ ) — present subj the bread',
                'es': 'Tú sepas el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'They (f) (that ___ ) — present subj here',
                'es': 'Ellas hayan aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'She (that ___ ) — present subj the truth',
                'es': 'Ella haya la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'I (that ___ ) — present subj the letter',
                'es': 'Yo sepa la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You all (that ___ ) — present subj the book',
                'es': 'Ustedes sepan el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'She (that ___ ) — present subj water',
                'es': 'Ella sepa agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'They (f) (that ___ ) — present subj the bread',
                'es': 'Ellas sepan el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'saber',
                'pronoun': 'tú'
            },
            {
                'verb': 'haber',
                'pronoun': 'ellas'
            },
            {
                'verb': 'haber',
                'pronoun': 'usted'
            },
            {
                'verb': 'saber',
                'pronoun': 'ustedes'
            },
            {
                'verb': 'haber',
                'pronoun': 'ellos'
            }
        ],
        'phase_2_config': {
            'description': 'Present Subjunctive (7)',
            'targets': [
                {
                    'verb': 'saber',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'haber',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'haber',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'saber',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'haber',
                    'pronoun': 'ellos'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_subj_pres_8': {
        'title': 'Present Subjunctive — Chat 3',
        'grammar_level': 20,
        'lesson_number': 8,
        'lesson_type': 'conjugation',
        'word_workload': [
            'saber',
            'haber'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'present_subjunctive',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Present Subjunctive — Chat 3: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'saber',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'haber',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'haber',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'saber',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'haber',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'saber',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'haber',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'haber',
                    'pronoun': 'usted'
                },
                {
                    'verb': 'saber',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'haber',
                    'pronoun': 'ellos'
                }
            ]
        },
        'opener_en': 'What do you need them to know?',
        'opener_es': '¿Qué necesitas que sepan?',
    },
    'grammar_subj_impf_1': {
        'title': 'Imperfect Subjunctive (1)',
        'grammar_level': 20,
        'lesson_number': 9,
        'lesson_type': 'conjugation',
        'word_workload': [
            'hablar',
            'comer'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'imperfect_subjunctive',
        'drill_config': {
            'answers': {
                'hablar': {
                    'yo': 'hablara',
                    'tú': 'hablaras',
                    'él': 'hablara',
                    'ella': 'hablara',
                    'usted': 'hablara',
                    'nosotros': 'habláramos',
                    'nosotras': 'habláramos',
                    'ellos': 'hablaran',
                    'ellas': 'hablaran',
                    'ustedes': 'hablaran'
                },
                'comer': {
                    'yo': 'comiera',
                    'tú': 'comieras',
                    'él': 'comiera',
                    'ella': 'comiera',
                    'usted': 'comiera',
                    'nosotros': 'comiéramos',
                    'nosotras': 'comiéramos',
                    'ellos': 'comieran',
                    'ellas': 'comieran',
                    'ustedes': 'comieran'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'You (if ___ ) — imperfect subj the song',
                'es': 'Tú hablaras la canción',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'I (if ___ ) — imperfect subj Spanish',
                'es': 'Yo hablara español',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'We (f) (if ___ ) — imperfect subj English',
                'es': 'Nosotras habláramos inglés',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'We (f) (if ___ ) — imperfect subj the bread',
                'es': 'Nosotras comiéramos el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'She (if ___ ) — imperfect subj the coffee',
                'es': 'Ella hablara el café',
                'noun_id': 'café',
                'type': 'written'
            },
            {
                'en': 'She (if ___ ) — imperfect subj the truth',
                'es': 'Ella comiera la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You all (if ___ ) — imperfect subj the song',
                'es': 'Ustedes hablaran la canción',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You (formal) (if ___ ) — imperfect subj Spanish',
                'es': 'Usted hablara español',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You (if ___ ) — imperfect subj water',
                'es': 'Tú comieras agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You all (if ___ ) — imperfect subj the bread',
                'es': 'Ustedes comieran el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'comer',
                'pronoun': 'yo'
            },
            {
                'verb': 'comer',
                'pronoun': 'él'
            },
            {
                'verb': 'hablar',
                'pronoun': 'nosotros'
            },
            {
                'verb': 'comer',
                'pronoun': 'ustedes'
            },
            {
                'verb': 'comer',
                'pronoun': 'ella'
            }
        ],
        'phase_2_config': {
            'description': 'Imperfect Subjunctive (1)',
            'targets': [
                {
                    'verb': 'comer',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'él'
                },
                {
                    'verb': 'hablar',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'ella'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_subj_impf_2': {
        'title': 'Imperfect Subjunctive (2)',
        'grammar_level': 20,
        'lesson_number': 10,
        'lesson_type': 'conjugation',
        'word_workload': [
            'vivir',
            'estudiar'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'imperfect_subjunctive',
        'drill_config': {
            'answers': {
                'vivir': {
                    'yo': 'viviera',
                    'tú': 'vivieras',
                    'él': 'viviera',
                    'ella': 'viviera',
                    'usted': 'viviera',
                    'nosotros': 'viviéramos',
                    'nosotras': 'viviéramos',
                    'ellos': 'vivieran',
                    'ellas': 'vivieran',
                    'ustedes': 'vivieran'
                },
                'estudiar': {
                    'yo': 'estudiara',
                    'tú': 'estudiaras',
                    'él': 'estudiara',
                    'ella': 'estudiara',
                    'usted': 'estudiara',
                    'nosotros': 'estudiáramos',
                    'nosotras': 'estudiáramos',
                    'ellos': 'estudiaran',
                    'ellas': 'estudiaran',
                    'ustedes': 'estudiaran'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'We (f) (if ___ ) — imperfect subj the song',
                'es': 'Nosotras estudiáramos la canción',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You (if ___ ) — imperfect subj the book',
                'es': 'Tú vivieras el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'We (f) (if ___ ) — imperfect subj water',
                'es': 'Nosotras viviéramos agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (if ___ ) — imperfect subj at home',
                'es': 'Tú estudiaras en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            },
            {
                'en': 'You all (if ___ ) — imperfect subj here',
                'es': 'Ustedes vivieran aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'They (f) (if ___ ) — imperfect subj the music',
                'es': 'Ellas estudiaran la música',
                'noun_id': 'música',
                'type': 'auditory'
            },
            {
                'en': 'You (formal) (if ___ ) — imperfect subj the song',
                'es': 'Usted estudiara la canción',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'I (if ___ ) — imperfect subj the book',
                'es': 'Yo viviera el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'She (if ___ ) — imperfect subj English',
                'es': 'Ella estudiara inglés',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'I (if ___ ) — imperfect subj at home',
                'es': 'Yo estudiara en casa',
                'noun_id': 'casa',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'estudiar',
                'pronoun': 'ellas'
            },
            {
                'verb': 'estudiar',
                'pronoun': 'tú'
            },
            {
                'verb': 'estudiar',
                'pronoun': 'ellos'
            },
            {
                'verb': 'vivir',
                'pronoun': 'nosotras'
            },
            {
                'verb': 'vivir',
                'pronoun': 'ustedes'
            }
        ],
        'phase_2_config': {
            'description': 'Imperfect Subjunctive (2)',
            'targets': [
                {
                    'verb': 'estudiar',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'ustedes'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_subj_impf_3': {
        'title': 'Imperfect Subjunctive — Chat 1',
        'grammar_level': 20,
        'lesson_number': 11,
        'lesson_type': 'conjugation',
        'word_workload': [
            'hablar',
            'comer',
            'vivir',
            'estudiar'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'imperfect_subjunctive',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Imperfect Subjunctive — Chat 1: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'comer',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'él'
                },
                {
                    'verb': 'hablar',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'comer',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'estudiar',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'vivir',
                    'pronoun': 'ustedes'
                }
            ]
        },
        'opener_en': 'If you had more time, what would you do?',
        'opener_es': 'Si tuvieras más tiempo, ¿qué harías?',
    },
    'grammar_subj_impf_4': {
        'title': 'Imperfect Subjunctive (4)',
        'grammar_level': 20,
        'lesson_number': 12,
        'lesson_type': 'conjugation',
        'word_workload': [
            'ser',
            'tener'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'imperfect_subjunctive',
        'drill_config': {
            'answers': {
                'ser': {
                    'yo': 'fuera',
                    'tú': 'fueras',
                    'él': 'fuera',
                    'ella': 'fuera',
                    'usted': 'fuera',
                    'ellos': 'fueran',
                    'ellas': 'fueran',
                    'ustedes': 'fueran',
                    'nosotros': 'fuéramos',
                    'nosotras': 'fuéramos'
                },
                'tener': {
                    'yo': 'tuviera',
                    'tú': 'tuvieras',
                    'él': 'tuviera',
                    'ella': 'tuviera',
                    'usted': 'tuviera',
                    'ellos': 'tuvieran',
                    'ellas': 'tuvieran',
                    'ustedes': 'tuvieran',
                    'nosotros': 'tuviéramos',
                    'nosotras': 'tuviéramos'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'You (if ___ ) — imperfect subj the letter',
                'es': 'Tú fueras la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You all (if ___ ) — imperfect subj the book',
                'es': 'Ustedes fueran el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You all (if ___ ) — imperfect subj water',
                'es': 'Ustedes tuvieran agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'She (if ___ ) — imperfect subj the bread',
                'es': 'Ella fuera el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'We (f) (if ___ ) — imperfect subj here',
                'es': 'Nosotras tuviéramos aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'I (if ___ ) — imperfect subj the truth',
                'es': 'Yo tuviera la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'She (if ___ ) — imperfect subj the letter',
                'es': 'Ella tuviera la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You (if ___ ) — imperfect subj the book',
                'es': 'Tú tuvieras el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'They (f) (if ___ ) — imperfect subj water',
                'es': 'Ellas fueran agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (formal) (if ___ ) — imperfect subj the bread',
                'es': 'Usted fuera el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'ser',
                'pronoun': 'tú'
            },
            {
                'verb': 'tener',
                'pronoun': 'nosotras'
            },
            {
                'verb': 'ser',
                'pronoun': 'yo'
            },
            {
                'verb': 'ser',
                'pronoun': 'nosotros'
            },
            {
                'verb': 'ser',
                'pronoun': 'ella'
            }
        ],
        'phase_2_config': {
            'description': 'Imperfect Subjunctive (4)',
            'targets': [
                {
                    'verb': 'ser',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'tener',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'ser',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'ser',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'ser',
                    'pronoun': 'ella'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_subj_impf_5': {
        'title': 'Imperfect Subjunctive (5)',
        'grammar_level': 20,
        'lesson_number': 13,
        'lesson_type': 'conjugation',
        'word_workload': [
            'hacer',
            'querer'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'imperfect_subjunctive',
        'drill_config': {
            'answers': {
                'hacer': {
                    'yo': 'hiciera',
                    'tú': 'hicieras',
                    'él': 'hiciera',
                    'ella': 'hiciera',
                    'usted': 'hiciera',
                    'ellos': 'hicieran',
                    'ellas': 'hicieran',
                    'ustedes': 'hicieran',
                    'nosotros': 'hiciéramos',
                    'nosotras': 'hiciéramos'
                },
                'querer': {
                    'yo': 'quisiera',
                    'tú': 'quisieras',
                    'él': 'quisiera',
                    'ella': 'quisiera',
                    'usted': 'quisiera',
                    'ellos': 'quisieran',
                    'ellas': 'quisieran',
                    'ustedes': 'quisieran',
                    'nosotros': 'quisiéramos',
                    'nosotras': 'quisiéramos'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'You all (if ___ ) — imperfect subj the letter',
                'es': 'Ustedes hicieran la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You (if ___ ) — imperfect subj the book',
                'es': 'Tú hicieras el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'I (if ___ ) — imperfect subj water',
                'es': 'Yo hiciera agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'You (formal) (if ___ ) — imperfect subj the bread',
                'es': 'Usted hiciera el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'She (if ___ ) — imperfect subj here',
                'es': 'Ella quisiera aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You (formal) (if ___ ) — imperfect subj the truth',
                'es': 'Usted quisiera la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'They (f) (if ___ ) — imperfect subj the letter',
                'es': 'Ellas quisieran la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You all (if ___ ) — imperfect subj the book',
                'es': 'Ustedes quisieran el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'I (if ___ ) — imperfect subj water',
                'es': 'Yo quisiera agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'We (f) (if ___ ) — imperfect subj the bread',
                'es': 'Nosotras hiciéramos el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'querer',
                'pronoun': 'nosotras'
            },
            {
                'verb': 'querer',
                'pronoun': 'ella'
            },
            {
                'verb': 'querer',
                'pronoun': 'ellos'
            },
            {
                'verb': 'hacer',
                'pronoun': 'ellos'
            },
            {
                'verb': 'querer',
                'pronoun': 'ellas'
            }
        ],
        'phase_2_config': {
            'description': 'Imperfect Subjunctive (5)',
            'targets': [
                {
                    'verb': 'querer',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'querer',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'querer',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'hacer',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'querer',
                    'pronoun': 'ellas'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_subj_impf_6': {
        'title': 'Imperfect Subjunctive — Chat 2',
        'grammar_level': 20,
        'lesson_number': 14,
        'lesson_type': 'conjugation',
        'word_workload': [
            'ser',
            'tener',
            'hacer',
            'querer'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'imperfect_subjunctive',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Imperfect Subjunctive — Chat 2: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'ser',
                    'pronoun': 'tú'
                },
                {
                    'verb': 'tener',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'ser',
                    'pronoun': 'yo'
                },
                {
                    'verb': 'ser',
                    'pronoun': 'nosotros'
                },
                {
                    'verb': 'ser',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'querer',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'querer',
                    'pronoun': 'ella'
                },
                {
                    'verb': 'querer',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'hacer',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'querer',
                    'pronoun': 'ellas'
                }
            ]
        },
        'opener_en': 'What if you had a different job?',
        'opener_es': '¿Y si tuvieras un trabajo diferente?',
    },
    'grammar_subj_impf_7': {
        'title': 'Imperfect Subjunctive (7)',
        'grammar_level': 20,
        'lesson_number': 15,
        'lesson_type': 'conjugation',
        'word_workload': [
            'decir',
            'poder'
        ],
        'video_embed_id': None,
        'drill_type': 'conjugation',
        'tense': 'imperfect_subjunctive',
        'drill_config': {
            'answers': {
                'decir': {
                    'yo': 'dijera',
                    'tú': 'dijeras',
                    'él': 'dijera',
                    'ella': 'dijera',
                    'usted': 'dijera',
                    'ellos': 'dijeran',
                    'ellas': 'dijeran',
                    'ustedes': 'dijeran',
                    'nosotros': 'dijéramos',
                    'nosotras': 'dijéramos'
                },
                'poder': {
                    'yo': 'pudiera',
                    'tú': 'pudieras',
                    'él': 'pudiera',
                    'ella': 'pudiera',
                    'usted': 'pudiera',
                    'ellos': 'pudieran',
                    'ellas': 'pudieran',
                    'ustedes': 'pudieran',
                    'nosotros': 'pudiéramos',
                    'nosotras': 'pudiéramos'
                }
            }
        },
        'phases': {
            '0a': True,
            '0b': True,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': False,
            '3': False
        },
        'phase_1c_config': {
            'total_items': 5,
            'mode': 'random_pronoun_verb'
        },
        'drill_sentences': [
            {
                'en': 'We (f) (if ___ ) — imperfect subj the letter',
                'es': 'Nosotras pudiéramos la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'You (if ___ ) — imperfect subj the book',
                'es': 'Tú dijeras el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'You (formal) (if ___ ) — imperfect subj water',
                'es': 'Usted dijera agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'I (if ___ ) — imperfect subj the bread',
                'es': 'Yo pudiera el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            },
            {
                'en': 'She (if ___ ) — imperfect subj here',
                'es': 'Ella pudiera aquí',
                'noun_id': None,
                'type': 'written'
            },
            {
                'en': 'You all (if ___ ) — imperfect subj the truth',
                'es': 'Ustedes pudieran la verdad',
                'noun_id': None,
                'type': 'auditory'
            },
            {
                'en': 'You (if ___ ) — imperfect subj the letter',
                'es': 'Tú pudieras la carta',
                'noun_id': 'carta',
                'type': 'written'
            },
            {
                'en': 'They (f) (if ___ ) — imperfect subj the book',
                'es': 'Ellas dijeran el libro',
                'noun_id': 'libro',
                'type': 'auditory'
            },
            {
                'en': 'We (f) (if ___ ) — imperfect subj water',
                'es': 'Nosotras dijéramos agua',
                'noun_id': 'agua',
                'type': 'written'
            },
            {
                'en': 'She (if ___ ) — imperfect subj the bread',
                'es': 'Ella dijera el pan',
                'noun_id': 'pan',
                'type': 'auditory'
            }
        ],
        'drill_targets': [
            {
                'verb': 'poder',
                'pronoun': 'ellos'
            },
            {
                'verb': 'poder',
                'pronoun': 'él'
            },
            {
                'verb': 'poder',
                'pronoun': 'ustedes'
            },
            {
                'verb': 'poder',
                'pronoun': 'ellas'
            },
            {
                'verb': 'poder',
                'pronoun': 'nosotras'
            }
        ],
        'phase_2_config': {
            'description': 'Imperfect Subjunctive (7)',
            'targets': [
                {
                    'verb': 'poder',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'él'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'nosotras'
                }
            ]
        },
        'opener_en': None,
        'opener_es': None,
    },
    'grammar_subj_impf_8': {
        'title': 'Imperfect Subjunctive — Chat 3',
        'grammar_level': 20,
        'lesson_number': 16,
        'lesson_type': 'conjugation',
        'word_workload': [
            'decir',
            'poder'
        ],
        'video_embed_id': None,
        'drill_type': 'skip',
        'tense': 'imperfect_subjunctive',
        'phases': {
            '0a': False,
            '0b': False,
            '1a': False,
            '1b': False,
            '1c': False,
            '2': True,
            '3': True
        },
        'phase_2_config': {
            'description': 'Imperfect Subjunctive — Chat 3: pulls from previous two drill lessons',
            'targets': [
                {
                    'verb': 'poder',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'él'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'nosotras'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'ellos'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'él'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'ustedes'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'ellas'
                },
                {
                    'verb': 'poder',
                    'pronoun': 'nosotras'
                }
            ]
        },
        'opener_en': 'Tell me what you wished you had said.',
        'opener_es': 'Cuéntame qué quisieras haber dicho.',
    },

}


def get_grammar_config(situation_id: str) -> dict | None:
    """Get grammar config for a situation ID, or None if not a grammar situation."""
    return GRAMMAR_SITUATIONS.get(situation_id)


def get_all_grammar_situation_ids() -> list[str]:
    """Get all grammar situation IDs sorted by grammar_level."""
    return sorted(GRAMMAR_SITUATIONS.keys(), key=lambda k: GRAMMAR_SITUATIONS[k]["grammar_level"])


# Build reverse lookup: grammar_level -> list of situation_ids (for multi-lesson GLs)
_GL_TO_SITUATIONS: dict[float, list[str]] = {}
for _sid, _cfg in GRAMMAR_SITUATIONS.items():
    _gl = _cfg["grammar_level"]
    _GL_TO_SITUATIONS.setdefault(_gl, []).append(_sid)
# Sort each list by lesson_number if available, else by situation_id
for _gl in _GL_TO_SITUATIONS:
    _GL_TO_SITUATIONS[_gl].sort(
        key=lambda s: (GRAMMAR_SITUATIONS[s].get("lesson_number", 0), s)
    )


def get_situations_for_gl(gl: float) -> list[str]:
    """Get all situation IDs at a given grammar level, sorted by lesson_number."""
    return _GL_TO_SITUATIONS.get(gl, [])


def get_next_gate(current_gl: float, vocab_level: int) -> dict | None:
    """Determine the next grammar gate for a user.

    Walks GL_SORTED to find the first GL > current_gl.
    If the user's vocab_level >= that GL's VL threshold, they are gated.

    Returns a dict with gate info, or None if not gated:
        {
            "grammar_level": float,
            "situation_id": str | None,   (first lesson at this GL)
            "title": str,
            "vl_threshold": int,
            "has_content": bool,
            "total_lessons": int,
        }
    """
    for gl in GL_SORTED:
        if gl <= current_gl:
            continue
        vl_threshold = GL_VL_THRESHOLDS[gl]
        if vocab_level >= vl_threshold:
            situations = get_situations_for_gl(gl)
            first_situation = situations[0] if situations else None
            return {
                "grammar_level": gl,
                "situation_id": first_situation,
                "title": GL_TITLES[gl],
                "vl_threshold": vl_threshold,
                "has_content": len(situations) > 0,
                "total_lessons": len(situations),
            }
        # VL hasn't reached this threshold yet — not gated
        return None
    # No more grammar levels above current — never gated
    return None
