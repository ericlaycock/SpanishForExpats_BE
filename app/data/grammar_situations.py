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


# ─────────────────────────────────────────────────────────────────────────────
# Slide packs — intro_chart + rule_chart shared across the lessons of a group.
#
# Each conjugation group teaches one rule across 2-4 lessons that vary the
# example verbs. The slide content is the same per group; the lesson's own
# `word_workload` supplies the verbs the user will actually drill.
# ─────────────────────────────────────────────────────────────────────────────

# --- GL 3: Regular Present (-ar / -er / -ir) ---
REGULAR_PRESENT_INTRO = {
    "kind": "cards",
    "title": "Regular present tense",
    "cards": [
        {
            "kind": "text",
            "title": "Verbs change to match who",
            "body": "In Spanish, the verb itself tells you who is doing the action. The infinitive form (the dictionary form, like *hablar* — to speak) drops its ending and gets a new one based on the subject.",
        },
        {
            "kind": "text",
            "title": "Three families: -ar, -er, -ir",
            "body": "Every Spanish infinitive ends in one of three letter pairs: **-ar** (hablar, escuchar), **-er** (beber, comer), or **-ir** (vivir, escribir). Each family takes its own set of endings.",
        },
        {
            "kind": "rule_pack",
            "title": "Drop the ending, add the new one",
            "sections": [
                {"heading": "-AR endings", "items": ["yo → -o (hablo)", "tú → -as (hablas)", "él/ella/usted → -a (habla)", "nosotros/as → -amos (hablamos)", "ellos/ellas/ustedes → -an (hablan)"]},
                {"heading": "-ER endings", "items": ["yo → -o (bebo)", "tú → -es (bebes)", "él/ella/usted → -e (bebe)", "nosotros/as → -emos (bebemos)", "ellos/ellas/ustedes → -en (beben)"]},
                {"heading": "-IR endings", "items": ["yo → -o (vivo)", "tú → -es (vives)", "él/ella/usted → -e (vive)", "nosotros/as → -imos (vivimos)", "ellos/ellas/ustedes → -en (viven)"]},
            ],
            "footnote": "Notice -er and -ir share the same endings except for nosotros (-emos vs. -imos).",
        },
    ],
}

REGULAR_PRESENT_RULE = {
    "kind": "table",
    "title": "Regular present — endings by ending type",
    "headers": ["Pronoun", "-AR (hablar)", "-ER (beber)", "-IR (vivir)"],
    "rows": [
        ["yo", "hablo", "bebo", "vivo"],
        ["tú", "hablas", "bebes", "vives"],
        ["él / ella / usted", "habla", "bebe", "vive"],
        ["nosotros / nosotras", "hablamos", "bebemos", "vivimos"],
        ["ellos / ellas / ustedes", "hablan", "beben", "viven"],
    ],
    "footnote": "All three families share the yo (-o) form. -er and -ir differ only in the nosotros row.",
}

# --- GL 3 sub-blocks: per-family slide packs (-AR only, then -ER, then -IR) ---
# Each sub-block is 2 drills + 1 chat. The intro_chart appears on the first drill
# of each block; the rule_chart stays for both drills as a reference. The "|" in
# verb forms marks the stem/ending boundary so the FE can render endings in
# crimson (see ConjugationCell).

REGULAR_PRESENT_AR_INTRO = {
    "kind": "cards",
    "title": "Regular present — -AR verbs",
    "cards": [
        {
            "kind": "text",
            "title": "Verbs change to match who",
            "body": "In Spanish, the verb itself tells you who is doing the action. The infinitive form (the dictionary form, like *hablar* — to speak) drops its ending and gets a new one based on the subject.",
        },
        {
            "kind": "text",
            "title": "Three families: -ar, -er, -ir — starting with -ar",
            "body": "Every Spanish infinitive ends in **-ar**, **-er**, or **-ir**. Each family takes its own endings. We'll start with the most common: **-ar** verbs (hablar, escuchar, cantar, trabajar…).",
        },
        {
            "kind": "mini_table",
            "title": "-AR endings (example: hablar)",
            "rows": [
                ["yo", "habl|o"],
                ["tú", "habl|as"],
                ["él / ella / usted", "habl|a"],
                ["nosotros / nosotras", "habl|amos"],
                ["ellos / ellas / ustedes", "habl|an"],
            ],
            "footnote": "The stem (habl-) stays the same. Only the ending changes with the subject.",
        },
    ],
    "recall": {
        "verb": "hablar",
        "answers": {
            "yo": "habl|o", "tú": "habl|as", "él": "habl|a",
            "nosotros": "habl|amos", "ellos": "habl|an",
        },
    },
}

REGULAR_PRESENT_AR_RULE = {
    "kind": "table",
    "title": "Regular present — -AR endings",
    "headers": ["Pronoun", "hablar", "escuchar"],
    "rows": [
        ["yo", "habl|o", "escuch|o"],
        ["tú", "habl|as", "escuch|as"],
        ["él / ella / usted", "habl|a", "escuch|a"],
        ["nosotros / nosotras", "habl|amos", "escuch|amos"],
        ["ellos / ellas / ustedes", "habl|an", "escuch|an"],
    ],
    "footnote": "Every regular -ar verb follows this pattern. Drop -ar, add -o / -as / -a / -amos / -an.",
}

REGULAR_PRESENT_ER_INTRO = {
    "kind": "cards",
    "title": "Regular present — -ER verbs",
    "cards": [
        {
            "kind": "text",
            "title": "Now: -er verbs",
            "body": "You already know the -ar pattern. -er verbs (beber, comer, leer, aprender…) work the same way — drop the ending, add a new one — but the endings are different.",
        },
        {
            "kind": "mini_table",
            "title": "-ER endings (example: beber)",
            "rows": [
                ["yo", "beb|o"],
                ["tú", "beb|es"],
                ["él / ella / usted", "beb|e"],
                ["nosotros / nosotras", "beb|emos"],
                ["ellos / ellas / ustedes", "beb|en"],
            ],
            "footnote": "Yo still ends in -o (same as -ar). The other forms swap the -a for -e: -es, -e, -emos, -en.",
        },
    ],
    "recall": {
        "verb": "beber",
        "answers": {
            "yo": "beb|o", "tú": "beb|es", "él": "beb|e",
            "nosotros": "beb|emos", "ellos": "beb|en",
        },
    },
}

REGULAR_PRESENT_ER_RULE = {
    "kind": "table",
    "title": "Regular present — -ER endings",
    "headers": ["Pronoun", "beber", "comer"],
    "rows": [
        ["yo", "beb|o", "com|o"],
        ["tú", "beb|es", "com|es"],
        ["él / ella / usted", "beb|e", "com|e"],
        ["nosotros / nosotras", "beb|emos", "com|emos"],
        ["ellos / ellas / ustedes", "beb|en", "com|en"],
    ],
    "footnote": "Every regular -er verb follows this pattern. Drop -er, add -o / -es / -e / -emos / -en.",
}

REGULAR_PRESENT_IR_INTRO = {
    "kind": "cards",
    "title": "Regular present — -IR verbs",
    "cards": [
        {
            "kind": "text",
            "title": "Last family: -ir verbs",
            "body": "-ir verbs (vivir, escribir, abrir, recibir…) share almost every ending with -er. The only difference is the *nosotros* form: -er says **-emos**, -ir says **-imos**.",
        },
        {
            "kind": "mini_table",
            "title": "-IR endings (example: vivir)",
            "rows": [
                ["yo", "viv|o"],
                ["tú", "viv|es"],
                ["él / ella / usted", "viv|e"],
                ["nosotros / nosotras", "viv|imos"],
                ["ellos / ellas / ustedes", "viv|en"],
            ],
            "footnote": "Same as -er except nosotros: -emos (beb|emos) vs -imos (viv|imos).",
        },
    ],
    "recall": {
        "verb": "vivir",
        "answers": {
            "yo": "viv|o", "tú": "viv|es", "él": "viv|e",
            "nosotros": "viv|imos", "ellos": "viv|en",
        },
    },
}

REGULAR_PRESENT_IR_RULE = {
    "kind": "table",
    "title": "Regular present — -IR endings",
    "headers": ["Pronoun", "vivir", "escribir"],
    "rows": [
        ["yo", "viv|o", "escrib|o"],
        ["tú", "viv|es", "escrib|es"],
        ["él / ella / usted", "viv|e", "escrib|e"],
        ["nosotros / nosotras", "viv|imos", "escrib|imos"],
        ["ellos / ellas / ustedes", "viv|en", "escrib|en"],
    ],
    "footnote": "Every regular -ir verb follows this pattern. Drop -ir, add -o / -es / -e / -imos / -en.",
}

# --- GL 1.5: Possessive Adjectives (intro only — rule chart already exists per lesson) ---
POSSESSIVE_ADJ_INTRO = {
    "kind": "cards",
    "title": "Possessive adjectives",
    "cards": [
        {
            "kind": "text",
            "title": "\"My,\" \"your,\" \"our\" — short words that go before the noun",
            "body": "Possessive adjectives sit *before* the noun, just like in English: **mi casa** (my house), **tu amigo** (your friend). They tell you who owns the thing.",
        },
        {
            "kind": "text",
            "title": "They agree with the THING, not the owner",
            "body": "The possessive matches the noun's number (and sometimes gender), not the speaker. *mi libro* / *mis libros* — \"my\" changes because *libros* is plural. The fact that I'm one person doesn't matter.",
        },
        {
            "kind": "rule_pack",
            "title": "The full set",
            "sections": [
                {"heading": "Singular noun", "items": ["mi (my)", "tu (your, informal)", "su (his / her / your-formal / their)", "nuestro / nuestra (our)"]},
                {"heading": "Plural noun", "items": ["mis", "tus", "sus", "nuestros / nuestras"]},
            ],
            "footnote": "Only nuestro/nuestra agrees with gender. The others change only with number (add -s).",
        },
    ],
}

# --- GL 4: Irregular Present (ser, estar, ir, dar, tener, venir) ---
IRREGULAR_PRESENT_INTRO = {
    "kind": "cards",
    "title": "Six irregular workhorse verbs",
    "cards": [
        {
            "kind": "text",
            "title": "These six don't follow the rules — and they're everywhere",
            "body": "**ser, estar, ir, dar, tener, venir** are the most common verbs in Spanish, and every one of them breaks the regular pattern. There's no shortcut: you memorize them once and they pay for themselves a thousand times.",
        },
        {
            "kind": "text",
            "title": "ser vs. estar — both mean \"to be\"",
            "body": "Spanish splits English's \"to be\" into two verbs. **ser** is for permanent identity (*soy americano*). **estar** is for location and temporary states (*estoy cansado*, *estoy en casa*). You'll see this contrast in every conversation.",
        },
        {
            "kind": "mini_table",
            "title": "ser (to be — identity)",
            "rows": [
                ["yo", "|soy"],
                ["tú", "|eres"],
                ["él / ella / usted", "|es"],
                ["nosotros / nosotras", "|somos"],
                ["ellos / ellas / ustedes", "|son"],
            ],
            "footnote": "Suppletive — every form is irregular.",
        },
        {
            "kind": "mini_table",
            "title": "estar (to be — state/location)",
            "rows": [
                ["yo", "est|oy"],
                ["tú", "est|ás"],
                ["él / ella / usted", "est|á"],
                ["nosotros / nosotras", "est|amos"],
                ["ellos / ellas / ustedes", "est|án"],
            ],
            "footnote": "Irregular yo (-oy); accents on tú, él, ellos.",
        },
        {
            "kind": "mini_table",
            "title": "ir (to go)",
            "rows": [
                ["yo", "|voy"],
                ["tú", "|vas"],
                ["él / ella / usted", "|va"],
                ["nosotros / nosotras", "va|mos"],
                ["ellos / ellas / ustedes", "|van"],
            ],
            "footnote": "Suppletive v- stem; nosotros uses a regular split.",
        },
        {
            "kind": "mini_table",
            "title": "dar (to give)",
            "rows": [
                ["yo", "|doy"],
                ["tú", "|das"],
                ["él / ella / usted", "|da"],
                ["nosotros / nosotras", "da|mos"],
                ["ellos / ellas / ustedes", "|dan"],
            ],
            "footnote": "Irregular yo (doy); otherwise looks like an -ar verb.",
        },
        {
            "kind": "mini_table",
            "title": "tener (to have)",
            "rows": [
                ["yo", "ten|go"],
                ["tú", "t|ienes"],
                ["él / ella / usted", "t|iene"],
                ["nosotros / nosotras", "ten|emos"],
                ["ellos / ellas / ustedes", "t|ienen"],
            ],
            "footnote": "Yo-go irregular plus e→ie stem change in tú/él/ellos.",
        },
        {
            "kind": "mini_table",
            "title": "venir (to come)",
            "rows": [
                ["yo", "ven|go"],
                ["tú", "v|ienes"],
                ["él / ella / usted", "v|iene"],
                ["nosotros / nosotras", "ven|imos"],
                ["ellos / ellas / ustedes", "v|ienen"],
            ],
            "footnote": "Same pattern as tener: -go yo + e→ie stem change.",
        },
    ],
    "recall": {
        "verb": "ser",
        "answers": {
            "yo": "|soy",
            "tú": "|eres",
            "él": "|es",
            "nosotros": "|somos",
            "ellos": "|son",
        },
    },
}

IRREGULAR_PRESENT_RULE = {
    "kind": "table",
    "title": "Irregular present — six core verbs",
    "headers": ["Pronoun", "ser", "estar", "ir", "dar", "tener", "venir"],
    "rows": [
        ["yo", "soy", "estoy", "voy", "doy", "tengo", "vengo"],
        ["tú", "eres", "estás", "vas", "das", "tienes", "vienes"],
        ["él / ella / usted", "es", "está", "va", "da", "tiene", "viene"],
        ["nosotros / nosotras", "somos", "estamos", "vamos", "damos", "tenemos", "venimos"],
        ["ellos / ellas / ustedes", "son", "están", "van", "dan", "tienen", "vienen"],
    ],
    "footnote": "ser is permanent identity; estar is state or location. tener/venir both go yo → -go.",
}

# --- GL 4.1: Ser vs. Estar (intro only — rule chart already exists) ---
SER_ESTAR_INTRO = {
    "kind": "cards",
    "title": "ser vs. estar",
    "cards": [
        {
            "kind": "text",
            "title": "Spanish has two verbs for \"to be\"",
            "body": "English uses *am / is / are* for everything. Spanish splits this into **ser** and **estar**. Choosing the wrong one is the most common beginner mistake — and the rule is mostly about *permanence vs. condition*.",
        },
        {
            "kind": "comparison",
            "title": "The core split",
            "left": {"heading": "ser — what something IS", "items": ["Identity (soy doctora)", "Nationality (soy mexicano)", "Profession (es ingeniero)", "Permanent traits (es alto)", "Time and date (son las tres)", "Material (es de madera)"]},
            "right": {"heading": "estar — how/where it IS right now", "items": ["Location (está en casa)", "Mood / health (estoy bien)", "Temporary state (la sopa está fría)", "Ongoing action (estoy comiendo)", "Result of change (está roto)"]},
            "footnote": "Trick: if you can swap \"is\" for \"feels\" or \"is currently,\" you almost always want estar.",
        },
        {
            "kind": "text",
            "title": "Same adjective, different meaning",
            "body": "**Es aburrido** = he's boring (a trait). **Está aburrido** = he's bored (right now). Same word, opposite meaning. The verb you pick changes everything.",
        },
    ],
}

# --- GL 4.2: por vs. para (intro only) ---
POR_PARA_INTRO = {
    "kind": "cards",
    "title": "por vs. para",
    "cards": [
        {
            "kind": "text",
            "title": "Both translate as \"for\" — but they mean very different things",
            "body": "**para** points forward — toward a goal, a recipient, a deadline, a destination. **por** points backward or sideways — to a cause, a duration, a route, an exchange.",
        },
        {
            "kind": "comparison",
            "title": "Which one when",
            "left": {"heading": "para → forward / purpose", "items": ["Recipient: para mi madre", "Deadline: para el lunes", "Destination: salgo para Lima", "Purpose: estudio para aprender", "Opinion: para mí, está bien"]},
            "right": {"heading": "por → cause / motion through", "items": ["Reason: gracias por la ayuda", "Duration: por dos horas", "Route: caminamos por el parque", "Exchange: pagué $10 por el libro", "On behalf of: lo hago por ti"]},
            "footnote": "Mnemonic: PARA → Purpose, Audience, Recipient, Arrival. POR → reason, route, time spent, swap.",
        },
    ],
}

# --- GL 4.3: Demonstratives (intro only) ---
DEMONSTRATIVES_INTRO = {
    "kind": "cards",
    "title": "Demonstratives — \"this,\" \"that,\" \"that over there\"",
    "cards": [
        {
            "kind": "text",
            "title": "Spanish has THREE distances, not two",
            "body": "English has *this* (here) and *that* (there). Spanish splits *that* into two: **ese/esa** (near the listener) and **aquel/aquella** (far from both of you). Three zones of distance.",
        },
        {
            "kind": "rule_pack",
            "title": "All forms by distance",
            "sections": [
                {"heading": "Near me (this)", "items": ["este libro (m sg)", "esta casa (f sg)", "estos libros (m pl)", "estas casas (f pl)"]},
                {"heading": "Near you (that)", "items": ["ese libro", "esa casa", "esos libros", "esas casas"]},
                {"heading": "Far from us both (that over there)", "items": ["aquel libro", "aquella casa", "aquellos libros", "aquellas casas"]},
            ],
            "footnote": "All three sets follow the same -e/-a/-os/-as pattern, just with different stems: est-, es-, aquel-.",
        },
    ],
}

# --- GL 4.4: Possessive Pronouns (intro only) ---
POSSESSIVE_PRONOUNS_INTRO = {
    "kind": "cards",
    "title": "Possessive pronouns — \"mine, yours, ours\"",
    "cards": [
        {
            "kind": "text",
            "title": "Different from possessive ADJECTIVES",
            "body": "Earlier you learned **mi casa** (my house) — that's a possessive *adjective*, sitting before a noun. Possessive *pronouns* REPLACE the noun: \"the house is **mine**\" → *la casa es **mía***. They stand on their own.",
        },
        {
            "kind": "text",
            "title": "They agree with the thing owned",
            "body": "Like adjectives, they match the noun's gender and number — but here you can hear it on every form: **mío / mía / míos / mías**. Same root, four endings.",
        },
        {
            "kind": "rule_pack",
            "title": "The forms",
            "sections": [
                {"heading": "mine", "items": ["mío, mía, míos, mías"]},
                {"heading": "yours (informal)", "items": ["tuyo, tuya, tuyos, tuyas"]},
                {"heading": "his / hers / yours-formal / theirs", "items": ["suyo, suya, suyos, suyas"]},
                {"heading": "ours", "items": ["nuestro, nuestra, nuestros, nuestras"]},
            ],
            "footnote": "Often used with the article: *el mío, la tuya, los suyos*.",
        },
    ],
}

# --- GL 4.5: Irregular Present II (yo-irregular: hacer/poner/salir/decir/oír/caer/traer/valer) ---
IRREGULAR_PRESENT_II_INTRO = {
    "kind": "cards",
    "title": "More irregulars — the \"yo-go\" verbs",
    "cards": [
        {
            "kind": "text",
            "title": "Strange yo, normal everywhere else",
            "body": "Eight common verbs share a quirk: their **yo** form ends in **-go** even though the rest of the conjugation is regular. *hacer* → *yo hago*, *poner* → *yo pongo*, *salir* → *yo salgo*. From tú onward, they behave like normal -er/-ir verbs.",
        },
        {
            "kind": "text",
            "title": "Two oddballs: oír and decir",
            "body": "**oír** (to hear) gets a y in tú/él/ellos: *oigo, oyes, oye, oímos, oyen*. **decir** (to say) does both: *yo digo* AND e→i stem change: *digo, dices, dice, decimos, dicen*.",
        },
        {
            "kind": "mini_table",
            "title": "hacer (to do, to make)",
            "rows": [
                ["yo", "ha|go"],
                ["tú", "hac|es"],
                ["él / ella / usted", "hac|e"],
                ["nosotros / nosotras", "hac|emos"],
                ["ellos / ellas / ustedes", "hac|en"],
            ],
            "footnote": "Yo-go irregular; otherwise regular -er.",
        },
        {
            "kind": "mini_table",
            "title": "poner (to put)",
            "rows": [
                ["yo", "pon|go"],
                ["tú", "pon|es"],
                ["él / ella / usted", "pon|e"],
                ["nosotros / nosotras", "pon|emos"],
                ["ellos / ellas / ustedes", "pon|en"],
            ],
            "footnote": "Yo-go irregular; otherwise regular -er.",
        },
        {
            "kind": "mini_table",
            "title": "salir (to leave, to go out)",
            "rows": [
                ["yo", "sal|go"],
                ["tú", "sal|es"],
                ["él / ella / usted", "sal|e"],
                ["nosotros / nosotras", "sal|imos"],
                ["ellos / ellas / ustedes", "sal|en"],
            ],
            "footnote": "Yo-go irregular; otherwise regular -ir.",
        },
        {
            "kind": "mini_table",
            "title": "traer (to bring)",
            "rows": [
                ["yo", "tra|igo"],
                ["tú", "tra|es"],
                ["él / ella / usted", "tra|e"],
                ["nosotros / nosotras", "tra|emos"],
                ["ellos / ellas / ustedes", "tra|en"],
            ],
            "footnote": "Yo form picks up an i: traigo.",
        },
        {
            "kind": "mini_table",
            "title": "decir (to say)",
            "rows": [
                ["yo", "di|go"],
                ["tú", "d|ices"],
                ["él / ella / usted", "d|ice"],
                ["nosotros / nosotras", "dec|imos"],
                ["ellos / ellas / ustedes", "d|icen"],
            ],
            "footnote": "Yo-go AND e→i stem change.",
        },
        {
            "kind": "mini_table",
            "title": "oír (to hear)",
            "rows": [
                ["yo", "o|igo"],
                ["tú", "o|yes"],
                ["él / ella / usted", "o|ye"],
                ["nosotros / nosotras", "o|ímos"],
                ["ellos / ellas / ustedes", "o|yen"],
            ],
            "footnote": "Yo picks up an i; tú/él/ellos add a y.",
        },
    ],
    "recall": {
        "verb": "hacer",
        "answers": {
            "yo": "ha|go",
            "tú": "hac|es",
            "él": "hac|e",
            "nosotros": "hac|emos",
            "ellos": "hac|en",
        },
    },
}

IRREGULAR_PRESENT_II_RULE = {
    "kind": "table",
    "title": "yo-go verbs — present tense",
    "headers": ["Pronoun", "hacer", "poner", "salir", "decir", "oír", "traer"],
    "rows": [
        ["yo", "hago", "pongo", "salgo", "digo", "oigo", "traigo"],
        ["tú", "haces", "pones", "sales", "dices", "oyes", "traes"],
        ["él / ella / usted", "hace", "pone", "sale", "dice", "oye", "trae"],
        ["nosotros / nosotras", "hacemos", "ponemos", "salimos", "decimos", "oímos", "traemos"],
        ["ellos / ellas / ustedes", "hacen", "ponen", "salen", "dicen", "oyen", "traen"],
    ],
    "footnote": "All take yo → -go. decir adds e→i (dices, dice, dicen). oír adds y in tú/él/ellos.",
}

# --- GL 5: Spelling Changes (consonant adjustments to keep sound) ---
SPELLING_CHANGES_INTRO = {
    "kind": "cards",
    "title": "Spelling changes — protecting the sound",
    "cards": [
        {
            "kind": "text",
            "title": "When the ending changes the consonant's sound",
            "body": "Spanish wants verbs to *sound* consistent across conjugation. So when an ending forces a soft consonant to go hard (or vice versa), Spanish swaps in a different letter to preserve the original sound. This only affects spelling — the ear hears the same verb.",
        },
        {
            "kind": "mini_table",
            "title": "conocer (to know — c → zc in yo)",
            "rows": [
                ["yo", "cono|zco"],
                ["tú", "conoc|es"],
                ["él / ella / usted", "conoc|e"],
                ["nosotros / nosotras", "conoc|emos"],
                ["ellos / ellas / ustedes", "conoc|en"],
            ],
            "footnote": "Only the yo form changes spelling; the rest is regular -er.",
        },
        {
            "kind": "mini_table",
            "title": "escoger (to choose — g → j in yo)",
            "rows": [
                ["yo", "esco|jo"],
                ["tú", "escog|es"],
                ["él / ella / usted", "escog|e"],
                ["nosotros / nosotras", "escog|emos"],
                ["ellos / ellas / ustedes", "escog|en"],
            ],
            "footnote": "g → j only in yo to keep the soft sound.",
        },
        {
            "kind": "mini_table",
            "title": "seguir (to follow — gu → g in yo, plus e→i stem)",
            "rows": [
                ["yo", "si|go"],
                ["tú", "s|igues"],
                ["él / ella / usted", "s|igue"],
                ["nosotros / nosotras", "segu|imos"],
                ["ellos / ellas / ustedes", "s|iguen"],
            ],
            "footnote": "Drop the silent u in yo (sigo), and apply the e→i stem change.",
        },
    ],
    "recall": {
        "verb": "conocer",
        "answers": {
            "yo": "cono|zco",
            "tú": "conoc|es",
            "él": "conoc|e",
            "nosotros": "conoc|emos",
            "ellos": "conoc|en",
        },
    },
}

SPELLING_CHANGES_RULE = {
    "kind": "table",
    "title": "Spelling-change verbs — present tense",
    "headers": ["Pronoun", "conocer", "recoger", "construir", "continuar", "conseguir"],
    "rows": [
        ["yo", "conozco", "recojo", "construyo", "continúo", "consigo"],
        ["tú", "conoces", "recoges", "construyes", "continúas", "consigues"],
        ["él / ella / usted", "conoce", "recoge", "construye", "continúa", "consigue"],
        ["nosotros / nosotras", "conocemos", "recogemos", "construimos", "continuamos", "conseguimos"],
        ["ellos / ellas / ustedes", "conocen", "recogen", "construyen", "continúan", "consiguen"],
    ],
    "footnote": "Only the spelling shifts — the SOUND of conoc-, recog-, etc. stays the same across all forms.",
}

# --- GL 5.5: saber vs. conocer ---
SABER_CONOCER_INTRO = {
    "kind": "cards",
    "title": "saber vs. conocer — two flavors of \"to know\"",
    "cards": [
        {
            "kind": "text",
            "title": "English uses one word; Spanish uses two",
            "body": "**saber** = to know a fact, a piece of information, or how to do something. **conocer** = to be familiar with a person, a place, or a thing through experience. Picking the wrong one rarely confuses meaning, but it always sounds non-native.",
        },
        {
            "kind": "comparison",
            "title": "Which to use",
            "left": {"heading": "saber → information / skills", "items": ["sé la respuesta (I know the answer)", "sé hablar francés (I know how to speak French)", "no sé qué hora es (I don't know what time it is)"]},
            "right": {"heading": "conocer → familiarity", "items": ["conozco a María (I know María)", "conozco Madrid (I've been to Madrid)", "no conozco esta canción (I don't know this song — never heard it)"]},
            "footnote": "Both have irregular yo: sé and conozco. Otherwise they conjugate normally.",
        },
        {
            "kind": "mini_table",
            "title": "saber (to know a fact)",
            "rows": [
                ["yo", "|sé"],
                ["tú", "sab|es"],
                ["él / ella / usted", "sab|e"],
                ["nosotros / nosotras", "sab|emos"],
                ["ellos / ellas / ustedes", "sab|en"],
            ],
            "footnote": "Irregular yo (sé with accent); rest is regular -er.",
        },
        {
            "kind": "mini_table",
            "title": "conocer (to be familiar with)",
            "rows": [
                ["yo", "cono|zco"],
                ["tú", "conoc|es"],
                ["él / ella / usted", "conoc|e"],
                ["nosotros / nosotras", "conoc|emos"],
                ["ellos / ellas / ustedes", "conoc|en"],
            ],
            "footnote": "c → zc spelling change in yo; rest is regular.",
        },
    ],
    "recall": {
        "verb": "saber",
        "answers": {
            "yo": "|sé",
            "tú": "sab|es",
            "él": "sab|e",
            "nosotros": "sab|emos",
            "ellos": "sab|en",
        },
    },
}

SABER_CONOCER_RULE = {
    "kind": "table",
    "title": "saber vs. conocer — present tense",
    "headers": ["Pronoun", "saber (know a fact)", "conocer (be familiar with)"],
    "rows": [
        ["yo", "sé", "conozco"],
        ["tú", "sabes", "conoces"],
        ["él / ella / usted", "sabe", "conoce"],
        ["nosotros / nosotras", "sabemos", "conocemos"],
        ["ellos / ellas / ustedes", "saben", "conocen"],
    ],
    "footnote": "saber for facts and skills; conocer for people, places, things you've experienced.",
}

# --- GL 6: Stem-changing O→UE (boot verbs) ---
PRESENT_O_UE_INTRO = {
    "kind": "cards",
    "title": "Stem change O → UE",
    "cards": [
        {
            "kind": "text",
            "title": "When stressed, the O breaks into UE",
            "body": "Some verbs change their stem vowel from **o** to **ue** when that vowel carries the stress — which happens in every form *except* nosotros/nosotras. The endings stay completely regular.",
        },
        {
            "kind": "text",
            "title": "Why it's called the \"boot\"",
            "body": "If you draw a line around the forms that change (yo, tú, él, ellos) and skip the ones that don't (nosotros, vosotros), the shape on a verb chart looks like a boot. Same idea applies to all stem-change patterns.",
        },
        {
            "kind": "mini_table",
            "title": "poder (to be able to)",
            "rows": [
                ["yo", "p|uedo"],
                ["tú", "p|uedes"],
                ["él / ella / usted", "p|uede"],
                ["nosotros / nosotras", "pod|emos"],
                ["ellos / ellas / ustedes", "p|ueden"],
            ],
            "footnote": "Boot pattern: o→ue everywhere except nosotros.",
        },
        {
            "kind": "mini_table",
            "title": "dormir (to sleep)",
            "rows": [
                ["yo", "d|uermo"],
                ["tú", "d|uermes"],
                ["él / ella / usted", "d|uerme"],
                ["nosotros / nosotras", "dorm|imos"],
                ["ellos / ellas / ustedes", "d|uermen"],
            ],
            "footnote": "Same boot: nosotros keeps the original o.",
        },
    ],
    "recall": {
        "verb": "poder",
        "answers": {
            "yo": "p|uedo",
            "tú": "p|uedes",
            "él": "p|uede",
            "nosotros": "pod|emos",
            "ellos": "p|ueden",
        },
    },
}

PRESENT_O_UE_RULE = {
    "kind": "table",
    "title": "O→UE stem change — present tense",
    "headers": ["Pronoun", "dormir", "poder", "almorzar", "volver"],
    "rows": [
        ["yo", "duermo", "puedo", "almuerzo", "vuelvo"],
        ["tú", "duermes", "puedes", "almuerzas", "vuelves"],
        ["él / ella / usted", "duerme", "puede", "almuerza", "vuelve"],
        ["nosotros / nosotras", "dormimos", "podemos", "almorzamos", "volvemos"],
        ["ellos / ellas / ustedes", "duermen", "pueden", "almuerzan", "vuelven"],
    ],
    "footnote": "The boot: every form changes EXCEPT nosotros, where the stress lands on the ending.",
}

# --- GL 7: Stem-changing E→IE ---
PRESENT_E_IE_INTRO = {
    "kind": "cards",
    "title": "Stem change E → IE",
    "cards": [
        {
            "kind": "text",
            "title": "Stressed E becomes IE",
            "body": "Same pattern as O→UE, with a different vowel. When the **e** in the verb's stem is stressed, it splits into **ie**. Every form changes except nosotros/nosotras (where the stress moves to the ending).",
        },
        {
            "kind": "mini_table",
            "title": "querer (to want)",
            "rows": [
                ["yo", "qu|iero"],
                ["tú", "qu|ieres"],
                ["él / ella / usted", "qu|iere"],
                ["nosotros / nosotras", "quer|emos"],
                ["ellos / ellas / ustedes", "qu|ieren"],
            ],
            "footnote": "Boot pattern: e→ie everywhere except nosotros.",
        },
        {
            "kind": "mini_table",
            "title": "pensar (to think)",
            "rows": [
                ["yo", "p|ienso"],
                ["tú", "p|iensas"],
                ["él / ella / usted", "p|iensa"],
                ["nosotros / nosotras", "pens|amos"],
                ["ellos / ellas / ustedes", "p|iensan"],
            ],
            "footnote": "Same boot; nosotros keeps the plain e.",
        },
    ],
    "recall": {
        "verb": "querer",
        "answers": {
            "yo": "qu|iero",
            "tú": "qu|ieres",
            "él": "qu|iere",
            "nosotros": "quer|emos",
            "ellos": "qu|ieren",
        },
    },
}

PRESENT_E_IE_RULE = {
    "kind": "table",
    "title": "E→IE stem change — present tense",
    "headers": ["Pronoun", "cerrar", "entender", "querer", "preferir"],
    "rows": [
        ["yo", "cierro", "entiendo", "quiero", "prefiero"],
        ["tú", "cierras", "entiendes", "quieres", "prefieres"],
        ["él / ella / usted", "cierra", "entiende", "quiere", "prefiere"],
        ["nosotros / nosotras", "cerramos", "entendemos", "queremos", "preferimos"],
        ["ellos / ellas / ustedes", "cierran", "entienden", "quieren", "prefieren"],
    ],
    "footnote": "Same boot pattern as O→UE — every form except nosotros.",
}

# --- GL 8: Stem-changing E→I (only -ir verbs) ---
PRESENT_E_I_INTRO = {
    "kind": "cards",
    "title": "Stem change E → I (only -ir verbs)",
    "cards": [
        {
            "kind": "text",
            "title": "A milder split — E becomes plain I",
            "body": "This pattern only affects **-ir** verbs. The stem **e** doesn't break into a diphthong like e→ie; it just slides to **i**. Same boot shape: every form except nosotros.",
        },
        {
            "kind": "mini_table",
            "title": "pedir (to ask for)",
            "rows": [
                ["yo", "p|ido"],
                ["tú", "p|ides"],
                ["él / ella / usted", "p|ide"],
                ["nosotros / nosotras", "ped|imos"],
                ["ellos / ellas / ustedes", "p|iden"],
            ],
            "footnote": "Boot pattern: e→i everywhere except nosotros.",
        },
        {
            "kind": "mini_table",
            "title": "servir (to serve)",
            "rows": [
                ["yo", "s|irvo"],
                ["tú", "s|irves"],
                ["él / ella / usted", "s|irve"],
                ["nosotros / nosotras", "serv|imos"],
                ["ellos / ellas / ustedes", "s|irven"],
            ],
            "footnote": "Same boot; nosotros keeps the plain e.",
        },
    ],
    "recall": {
        "verb": "pedir",
        "answers": {
            "yo": "p|ido",
            "tú": "p|ides",
            "él": "p|ide",
            "nosotros": "ped|imos",
            "ellos": "p|iden",
        },
    },
}

PRESENT_E_I_RULE = {
    "kind": "table",
    "title": "E→I stem change — present tense (-ir only)",
    "headers": ["Pronoun", "pedir", "repetir", "seguir", "servir"],
    "rows": [
        ["yo", "pido", "repito", "sigo", "sirvo"],
        ["tú", "pides", "repites", "sigues", "sirves"],
        ["él / ella / usted", "pide", "repite", "sigue", "sirve"],
        ["nosotros / nosotras", "pedimos", "repetimos", "seguimos", "servimos"],
        ["ellos / ellas / ustedes", "piden", "repiten", "siguen", "sirven"],
    ],
    "footnote": "seguir / conseguir / elegir also drop the silent gu/g in yo: sigo, consigo, elijo.",
}

# --- GL 9: ir + a + infinitive ---
IR_A_INF_INTRO = {
    "kind": "cards",
    "title": "ir + a + infinitive — \"going to\"",
    "cards": [
        {
            "kind": "text",
            "title": "The easiest way to talk about the future",
            "body": "Spanish has a true future tense, but in everyday speech people use **ir + a + [infinitive]** — exactly like English \"I'm going to + verb.\" *Voy a comer*. *Vamos a salir*. Conjugate **ir**, add **a**, then the verb in its dictionary form.",
        },
        {
            "kind": "mini_table",
            "title": "ir (to go)",
            "rows": [
                ["yo", "|voy"],
                ["tú", "|vas"],
                ["él / ella / usted", "|va"],
                ["nosotros / nosotras", "va|mos"],
                ["ellos / ellas / ustedes", "|van"],
            ],
            "footnote": "Suppletive v- stem; nosotros uses a regular split.",
        },
        {
            "kind": "rule_pack",
            "title": "Pattern: ir + a + infinitive",
            "sections": [
                {"heading": "Examples", "items": ["voy a hablar (I'm going to speak)", "vas a comer (you're going to eat)", "vamos a vivir (we're going to live)", "van a estudiar (they're going to study)"]},
            ],
            "footnote": "The infinitive never conjugates. All the work happens on ir.",
        },
    ],
    "recall": {
        "verb": "ir",
        "answers": {
            "yo": "|voy",
            "tú": "|vas",
            "él": "|va",
            "nosotros": "va|mos",
            "ellos": "|van",
        },
    },
}

IR_A_INF_RULE = {
    "kind": "table",
    "title": "ir + a + infinitive",
    "headers": ["Pronoun", "ir + a + hablar", "ir + a + comer", "ir + a + vivir"],
    "rows": [
        ["yo", "voy a hablar", "voy a comer", "voy a vivir"],
        ["tú", "vas a hablar", "vas a comer", "vas a vivir"],
        ["él / ella / usted", "va a hablar", "va a comer", "va a vivir"],
        ["nosotros / nosotras", "vamos a hablar", "vamos a comer", "vamos a vivir"],
        ["ellos / ellas / ustedes", "van a hablar", "van a comer", "van a vivir"],
    ],
    "footnote": "The infinitive (hablar / comer / vivir) never changes. Only ir conjugates.",
}

# --- GL 10 / 10.3 / 10.6: Gustar (used by gustar_1, _2, _3) ---
GUSTAR_INTRO = {
    "kind": "cards",
    "title": "gustar — Spanish doesn't \"like\" the way English does",
    "cards": [
        {
            "kind": "text",
            "title": "It's literally \"X is pleasing TO me\"",
            "body": "**Me gusta el café** doesn't translate as \"I like the coffee.\" It translates as \"the coffee is pleasing to me.\" The thing you like is the *subject*; you (the liker) are an indirect object. This flips the whole sentence.",
        },
        {
            "kind": "text",
            "title": "Two forms: gusta vs. gustan",
            "body": "Because the *thing* is the subject, the verb agrees with the thing. **Singular thing → gusta**: *me gusta el libro*. **Plural thing → gustan**: *me gustan los libros*. The pronoun (me/te/le/nos/les) stays the same.",
        },
        {
            "kind": "mini_table",
            "title": "gustar (to be pleasing — singular and plural forms)",
            "rows": [
                ["me + singular thing", "me gust|a"],
                ["te + singular thing", "te gust|a"],
                ["le + singular thing", "le gust|a"],
                ["nos + singular thing", "nos gust|a"],
                ["les + singular thing", "les gust|a"],
            ],
            "footnote": "Singular thing → gusta. Pronoun changes; verb stays in 3rd-person singular.",
        },
        {
            "kind": "mini_table",
            "title": "gustar — plural thing (gustan)",
            "rows": [
                ["me + plural things", "me gust|an"],
                ["te + plural things", "te gust|an"],
                ["le + plural things", "le gust|an"],
                ["nos + plural things", "nos gust|an"],
                ["les + plural things", "les gust|an"],
            ],
            "footnote": "Plural thing → gustan. The verb agrees with the THING, not the liker.",
        },
    ],
    "recall": {
        "verb": "gustar",
        "answers": {
            "yo": "me gust|a",
            "tú": "te gust|a",
            "él": "le gust|a",
            "nosotros": "nos gust|a",
            "ellos": "les gust|a",
        },
    },
}

GUSTAR_RULE = {
    "kind": "table",
    "title": "gustar — pronoun × singular/plural thing",
    "headers": ["Liker", "Singular thing", "Plural thing"],
    "rows": [
        ["yo (me)", "me gusta el libro", "me gustan los libros"],
        ["tú (te)", "te gusta", "te gustan"],
        ["él / ella / usted (le)", "le gusta", "le gustan"],
        ["nosotros / nosotras (nos)", "nos gusta", "nos gustan"],
        ["ellos / ellas / ustedes (les)", "les gusta", "les gustan"],
    ],
    "footnote": "The verb agrees with the THING (singular → gusta, plural → gustan), not the liker.",
}

# --- GL 11: Modal + infinitive (tengo que / me toca / necesito) ---
MODAL_INF_INTRO = {
    "kind": "cards",
    "title": "Modal + infinitive — \"have to,\" \"my turn to,\" \"need to\"",
    "cards": [
        {
            "kind": "text",
            "title": "Three everyday ways to say what you must do",
            "body": "Spanish has three super-common phrases that all take an infinitive: **tengo que + inf** (I have to), **me toca + inf** (it's my turn to), **necesito + inf** (I need to). The first verb conjugates; the action verb stays in its dictionary form.",
        },
        {
            "kind": "comparison",
            "title": "When to use which",
            "left": {"heading": "tengo que / necesito", "items": ["tengo que estudiar — obligation, external pressure", "necesito dormir — internal need", "Both conjugate normally: tengo, tienes, tiene… / necesito, necesitas, necesita…"]},
            "right": {"heading": "me toca", "items": ["me toca lavar los platos — \"it's my turn to do the dishes\"", "Conjugate the indirect object: me / te / le / nos / les + toca + inf", "The verb \"toca\" stays in 3rd person singular"]},
            "footnote": "tengo que: most common for obligations. necesito: emphasizes need. me toca: rotation/turn-taking.",
        },
        {
            "kind": "mini_table",
            "title": "tener que + inf (to have to)",
            "rows": [
                ["yo", "ten|go que"],
                ["tú", "t|ienes que"],
                ["él / ella / usted", "t|iene que"],
                ["nosotros / nosotras", "ten|emos que"],
                ["ellos / ellas / ustedes", "t|ienen que"],
            ],
            "footnote": "Tener stays irregular (yo-go + e→ie); add que + infinitive.",
        },
        {
            "kind": "mini_table",
            "title": "tocar + inf (it's __ turn to)",
            "rows": [
                ["yo (me)", "me toc|a"],
                ["tú (te)", "te toc|a"],
                ["él / ella / usted (le)", "le toc|a"],
                ["nosotros / nosotras (nos)", "nos toc|a"],
                ["ellos / ellas / ustedes (les)", "les toc|a"],
            ],
            "footnote": "Conjugate the indirect-object pronoun; toca stays in 3rd-person singular.",
        },
        {
            "kind": "mini_table",
            "title": "necesitar + inf (to need to)",
            "rows": [
                ["yo", "necesit|o"],
                ["tú", "necesit|as"],
                ["él / ella / usted", "necesit|a"],
                ["nosotros / nosotras", "necesit|amos"],
                ["ellos / ellas / ustedes", "necesit|an"],
            ],
            "footnote": "Fully regular -ar verb; add an infinitive after it.",
        },
    ],
    "recall": {
        "verb": "tener",
        "answers": {
            "yo": "ten|go",
            "tú": "t|ienes",
            "él": "t|iene",
            "nosotros": "ten|emos",
            "ellos": "t|ienen",
        },
    },
}

MODAL_INF_RULE = {
    "kind": "table",
    "title": "Modal + infinitive — three patterns",
    "headers": ["Pronoun", "tengo que + hablar", "me toca + hablar", "necesito + hablar"],
    "rows": [
        ["yo", "tengo que hablar", "me toca hablar", "necesito hablar"],
        ["tú", "tienes que hablar", "te toca hablar", "necesitas hablar"],
        ["él / ella / usted", "tiene que hablar", "le toca hablar", "necesita hablar"],
        ["nosotros / nosotras", "tenemos que hablar", "nos toca hablar", "necesitamos hablar"],
        ["ellos / ellas / ustedes", "tienen que hablar", "les toca hablar", "necesitan hablar"],
    ],
    "footnote": "The infinitive never changes. Only the modal verb conjugates (or, for me toca, the pronoun).",
}

# --- GL 12: Imperfect tense ---
IMPERFECT_INTRO = {
    "kind": "cards",
    "title": "Imperfect — the \"used to\" past",
    "cards": [
        {
            "kind": "text",
            "title": "A past tense for what kept happening",
            "body": "The imperfect describes what *used to happen*, what was *ongoing*, or what was *true for a while* in the past. It's the soundtrack of the story — background, habits, descriptions, age, time, weather.",
        },
        {
            "kind": "comparison",
            "title": "Imperfect vs. preterite (the other past)",
            "left": {"heading": "Imperfect — background / habit", "items": ["cuando era niño, vivía en Lima", "siempre comíamos juntos", "eran las tres de la tarde", "llovía mucho ese invierno"]},
            "right": {"heading": "Preterite — completed event", "items": ["ayer fui al cine", "comí toda la pizza", "nació en 1985", "llovió ayer"]},
            "footnote": "Imperfect = ongoing or repeated. Preterite = a single, finished event.",
        },
        {
            "kind": "mini_table",
            "title": "hablar — imperfect (-ar regular)",
            "rows": [
                ["yo", "habl|aba"],
                ["tú", "habl|abas"],
                ["él / ella / usted", "habl|aba"],
                ["nosotros / nosotras", "habl|ábamos"],
                ["ellos / ellas / ustedes", "habl|aban"],
            ],
            "footnote": "Yo and él are identical — context tells you who.",
        },
        {
            "kind": "mini_table",
            "title": "comer — imperfect (-er/-ir regular)",
            "rows": [
                ["yo", "com|ía"],
                ["tú", "com|ías"],
                ["él / ella / usted", "com|ía"],
                ["nosotros / nosotras", "com|íamos"],
                ["ellos / ellas / ustedes", "com|ían"],
            ],
            "footnote": "Same -ía endings on every -er and -ir verb.",
        },
        {
            "kind": "mini_table",
            "title": "ir — imperfect (irregular)",
            "rows": [
                ["yo", "|iba"],
                ["tú", "|ibas"],
                ["él / ella / usted", "|iba"],
                ["nosotros / nosotras", "|íbamos"],
                ["ellos / ellas / ustedes", "|iban"],
            ],
            "footnote": "Suppletive — just memorize.",
        },
        {
            "kind": "mini_table",
            "title": "ser — imperfect (irregular)",
            "rows": [
                ["yo", "|era"],
                ["tú", "|eras"],
                ["él / ella / usted", "|era"],
                ["nosotros / nosotras", "|éramos"],
                ["ellos / ellas / ustedes", "|eran"],
            ],
            "footnote": "Suppletive era- stem.",
        },
        {
            "kind": "mini_table",
            "title": "ver — imperfect (irregular)",
            "rows": [
                ["yo", "|veía"],
                ["tú", "|veías"],
                ["él / ella / usted", "|veía"],
                ["nosotros / nosotras", "|veíamos"],
                ["ellos / ellas / ustedes", "|veían"],
            ],
            "footnote": "Keeps the e from old veer-: veía.",
        },
    ],
    "recall": {
        "verb": "hablar",
        "answers": {
            "yo": "habl|aba",
            "tú": "habl|abas",
            "él": "habl|aba",
            "nosotros": "habl|ábamos",
            "ellos": "habl|aban",
        },
    },
}

IMPERFECT_RULE = {
    "kind": "table",
    "title": "Imperfect tense",
    "headers": ["Pronoun", "hablar", "comer", "vivir", "ir (irreg.)", "ser (irreg.)"],
    "rows": [
        ["yo", "hablaba", "comía", "vivía", "iba", "era"],
        ["tú", "hablabas", "comías", "vivías", "ibas", "eras"],
        ["él / ella / usted", "hablaba", "comía", "vivía", "iba", "era"],
        ["nosotros / nosotras", "hablábamos", "comíamos", "vivíamos", "íbamos", "éramos"],
        ["ellos / ellas / ustedes", "hablaban", "comían", "vivían", "iban", "eran"],
    ],
    "footnote": "Yo and él forms are identical — context tells you who. Only ir, ser, ver are irregular.",
}

# --- GL 13: Reflexive verbs ---
REFLEXIVE_INTRO = {
    "kind": "cards",
    "title": "Reflexive verbs — when the action loops back to the doer",
    "cards": [
        {
            "kind": "text",
            "title": "The doer and the receiver are the same person",
            "body": "Reflexive verbs describe actions you do *to yourself*: wash yourself, get yourself up, get yourself dressed. The infinitive ends in **-se** (lavarse, levantarse), and you replace -se with the right reflexive pronoun for whoever's doing it.",
        },
        {
            "kind": "mini_table",
            "title": "levantarse (to get oneself up)",
            "rows": [
                ["yo", "me levant|o"],
                ["tú", "te levant|as"],
                ["él / ella / usted", "se levant|a"],
                ["nosotros / nosotras", "nos levant|amos"],
                ["ellos / ellas / ustedes", "se levant|an"],
            ],
            "footnote": "Reflexive pronoun (me/te/se/nos/se) goes BEFORE the conjugated verb.",
        },
        {
            "kind": "text",
            "title": "When the verb has a stem change, the stem still changes",
            "body": "*acostarse* is o→ue: *me acuesto*, *te acuestas*… *vestirse* is e→i: *me visto*, *te vistes*… The reflexive pronoun doesn't suppress the stem-change rule.",
        },
    ],
    "recall": {
        "verb": "levantarse",
        "answers": {
            "yo": "me levant|o",
            "tú": "te levant|as",
            "él": "se levant|a",
            "nosotros": "nos levant|amos",
            "ellos": "se levant|an",
        },
    },
}

REFLEXIVE_RULE = {
    "kind": "table",
    "title": "Reflexive present tense",
    "headers": ["Pronoun + reflexive", "lavarse", "levantarse", "vestirse (e→i)", "acostarse (o→ue)"],
    "rows": [
        ["yo + me", "me lavo", "me levanto", "me visto", "me acuesto"],
        ["tú + te", "te lavas", "te levantas", "te vistes", "te acuestas"],
        ["él / ella / usted + se", "se lava", "se levanta", "se viste", "se acuesta"],
        ["nosotros / nosotras + nos", "nos lavamos", "nos levantamos", "nos vestimos", "nos acostamos"],
        ["ellos / ellas / ustedes + se", "se lavan", "se levantan", "se visten", "se acuestan"],
    ],
    "footnote": "The reflexive pronoun goes BEFORE the conjugated verb. Stem changes still apply.",
}

# --- GL 13.5: Imperatives (commands) ---
IMPERATIVES_INTRO = {
    "kind": "cards",
    "title": "Imperatives — telling someone what to do",
    "cards": [
        {
            "kind": "text",
            "title": "One form for tú, one for usted/ustedes",
            "body": "Spanish commands depend on who you're talking to. Informal **tú** uses the él/ella present-tense form. Formal **usted** and plural **ustedes** use the subjunctive form (it doubles as the command form). At this stage we focus on the affirmative — the \"do this\" version.",
        },
        {
            "kind": "mini_table",
            "title": "hablar — affirmative commands",
            "rows": [
                ["tú (informal)", "habl|a"],
                ["usted (formal)", "habl|e"],
                ["ustedes (plural)", "habl|en"],
            ],
            "footnote": "Regular -ar: tú = él present form. Usted/ustedes flip to -e endings.",
        },
        {
            "kind": "mini_table",
            "title": "comer — affirmative commands",
            "rows": [
                ["tú (informal)", "com|e"],
                ["usted (formal)", "com|a"],
                ["ustedes (plural)", "com|an"],
            ],
            "footnote": "Regular -er: usted/ustedes flip to -a endings.",
        },
        {
            "kind": "mini_table",
            "title": "vivir — affirmative commands",
            "rows": [
                ["tú (informal)", "viv|e"],
                ["usted (formal)", "viv|a"],
                ["ustedes (plural)", "viv|an"],
            ],
            "footnote": "Regular -ir: same -a endings as -er.",
        },
        {
            "kind": "mini_table",
            "title": "Irregular tú commands — eight to memorize",
            "rows": [
                ["ir → tú", "|ve"],
                ["ser → tú", "|sé"],
                ["tener → tú", "|ten"],
                ["venir → tú", "|ven"],
                ["salir → tú", "|sal"],
                ["poner → tú", "|pon"],
                ["hacer → tú", "|haz"],
                ["decir → tú", "|di"],
            ],
            "footnote": "Mnemonic: \"Vin Diesel has ten weapons\" → ven, di, sal, haz, ten, ve, pon, sé.",
        },
    ],
    "recall": {
        "verb": "hablar",
        "answers": {
            "yo": "habl|o",
            "tú": "habl|a",
            "él": "habl|e",
            "nosotros": "habl|emos",
            "ellos": "habl|en",
        },
    },
}

IMPERATIVES_RULE = {
    "kind": "table",
    "title": "Affirmative commands",
    "headers": ["Verb", "tú (informal)", "usted (formal)", "ustedes (plural)"],
    "rows": [
        ["hablar", "habla", "hable", "hablen"],
        ["comer", "come", "coma", "coman"],
        ["vivir", "vive", "viva", "vivan"],
        ["ir", "ve", "vaya", "vayan"],
        ["ser", "sé", "sea", "sean"],
        ["tener", "ten", "tenga", "tengan"],
    ],
    "footnote": "tú command = él present form (regular verbs). usted/ustedes commands use the subjunctive stem.",
}

# --- GL 14: Future tense ---
FUTURE_INTRO = {
    "kind": "cards",
    "title": "Future tense — \"will\" do something",
    "cards": [
        {
            "kind": "text",
            "title": "One set of endings, attached to the WHOLE infinitive",
            "body": "Unlike most tenses, the future doesn't drop -ar/-er/-ir. You take the whole infinitive (*hablar*, *comer*, *vivir*) and add the same set of endings — same set for all three verb families. That's the regular pattern.",
        },
        {
            "kind": "mini_table",
            "title": "hablar — future (regular)",
            "rows": [
                ["yo", "hablar|é"],
                ["tú", "hablar|ás"],
                ["él / ella / usted", "hablar|á"],
                ["nosotros / nosotras", "hablar|emos"],
                ["ellos / ellas / ustedes", "hablar|án"],
            ],
            "footnote": "Endings attach to the WHOLE infinitive. Same endings on -er and -ir verbs.",
        },
        {
            "kind": "mini_table",
            "title": "tener — future (irregular root tendr-)",
            "rows": [
                ["yo", "tendr|é"],
                ["tú", "tendr|ás"],
                ["él / ella / usted", "tendr|á"],
                ["nosotros / nosotras", "tendr|emos"],
                ["ellos / ellas / ustedes", "tendr|án"],
            ],
            "footnote": "Stem collapses to tendr-; endings stay identical to the regular set.",
        },
    ],
    "recall": {
        "verb": "hablar",
        "answers": {
            "yo": "hablar|é",
            "tú": "hablar|ás",
            "él": "hablar|á",
            "nosotros": "hablar|emos",
            "ellos": "hablar|án",
        },
    },
}

FUTURE_RULE = {
    "kind": "table",
    "title": "Future tense",
    "headers": ["Pronoun", "hablar", "comer", "vivir", "tener (irreg.)", "hacer (irreg.)"],
    "rows": [
        ["yo", "hablaré", "comeré", "viviré", "tendré", "haré"],
        ["tú", "hablarás", "comerás", "vivirás", "tendrás", "harás"],
        ["él / ella / usted", "hablará", "comerá", "vivirá", "tendrá", "hará"],
        ["nosotros / nosotras", "hablaremos", "comeremos", "viviremos", "tendremos", "haremos"],
        ["ellos / ellas / ustedes", "hablarán", "comerán", "vivirán", "tendrán", "harán"],
    ],
    "footnote": "Same endings on every verb. Irregulars only change the stem (tendr-, har-, dir-).",
}

# --- GL 15: Conditional ---
CONDITIONAL_INTRO = {
    "kind": "cards",
    "title": "Conditional — \"would\" do something",
    "cards": [
        {
            "kind": "text",
            "title": "Same stem as the future, different endings",
            "body": "Conditional shares the future's stem (full infinitive, or the same irregular shortcuts: *tendr-, har-, dir-…*). What changes are the endings: instead of future's -é/-ás/-á, conditional uses imperfect-style -ía endings. *Hablaría* = \"I would speak.\"",
        },
        {
            "kind": "mini_table",
            "title": "hablar — conditional (regular)",
            "rows": [
                ["yo", "hablar|ía"],
                ["tú", "hablar|ías"],
                ["él / ella / usted", "hablar|ía"],
                ["nosotros / nosotras", "hablar|íamos"],
                ["ellos / ellas / ustedes", "hablar|ían"],
            ],
            "footnote": "-ía endings attach to the whole infinitive. Yo and él are identical.",
        },
        {
            "kind": "mini_table",
            "title": "tener — conditional (irregular root tendr-)",
            "rows": [
                ["yo", "tendr|ía"],
                ["tú", "tendr|ías"],
                ["él / ella / usted", "tendr|ía"],
                ["nosotros / nosotras", "tendr|íamos"],
                ["ellos / ellas / ustedes", "tendr|ían"],
            ],
            "footnote": "Same irregular stems as the future; only endings differ.",
        },
        {
            "kind": "text",
            "title": "Use it for politeness, hypotheticals, soft suggestions",
            "body": "*¿Podrías ayudarme?* (Could you help me?) — softer than \"can you?\" *Yo iría contigo* (I'd go with you). *En tu lugar, hablaría con ella* (In your place, I would talk to her). It's the diplomat's tense.",
        },
    ],
    "recall": {
        "verb": "hablar",
        "answers": {
            "yo": "hablar|ía",
            "tú": "hablar|ías",
            "él": "hablar|ía",
            "nosotros": "hablar|íamos",
            "ellos": "hablar|ían",
        },
    },
}

CONDITIONAL_RULE = {
    "kind": "table",
    "title": "Conditional tense",
    "headers": ["Pronoun", "hablar", "comer", "vivir", "tener (irreg.)", "hacer (irreg.)"],
    "rows": [
        ["yo", "hablaría", "comería", "viviría", "tendría", "haría"],
        ["tú", "hablarías", "comerías", "vivirías", "tendrías", "harías"],
        ["él / ella / usted", "hablaría", "comería", "viviría", "tendría", "haría"],
        ["nosotros / nosotras", "hablaríamos", "comeríamos", "viviríamos", "tendríamos", "haríamos"],
        ["ellos / ellas / ustedes", "hablarían", "comerían", "vivirían", "tendrían", "harían"],
    ],
    "footnote": "Same stems as the future; -ía endings throughout. yo and él are identical forms.",
}

# --- GL 16: Preterite vs. Imperfect (intro only — rule chart already exists) ---
PRET_VS_IMPERFECT_INTRO = {
    "kind": "cards",
    "title": "Preterite vs. Imperfect — two flavors of past",
    "cards": [
        {
            "kind": "text",
            "title": "English uses one past; Spanish uses two",
            "body": "*\"I ate\"* could be one bite (preterite) or a regular habit (imperfect) — English doesn't care. Spanish makes you choose. The choice is about *aspect*: was the action a single completed event, or an ongoing/repeated background?",
        },
        {
            "kind": "comparison",
            "title": "How to choose",
            "left": {"heading": "Preterite — one finished event", "items": ["ayer comí pizza (yesterday I ate pizza)", "fue a Madrid en 2020", "se rompió la pierna", "el partido empezó a las ocho", "Marker words: ayer, anoche, una vez, en 1995"]},
            "right": {"heading": "Imperfect — ongoing / habitual / background", "items": ["de niño comía pizza todos los viernes", "cuando vivía en Madrid…", "estaba lloviendo", "siempre me llamaba", "Marker words: siempre, todos los días, mientras, cada"]},
            "footnote": "Preterite advances the story (\"and then…\"). Imperfect describes the scene (\"meanwhile, the room was…\").",
        },
        {
            "kind": "text",
            "title": "Often they appear in the same sentence",
            "body": "*Cuando **caminaba** por el parque (imp. — ongoing), **vi** a María (pret. — single event).* The imperfect sets the scene; the preterite is the thing that happened against that scene.",
        },
    ],
}

# --- GL 17: Preterite Regular ---
PRETERITE_REGULAR_INTRO = {
    "kind": "cards",
    "title": "Preterite — the \"and then this happened\" past",
    "cards": [
        {
            "kind": "text",
            "title": "For single, completed events",
            "body": "The preterite tells what *happened* — one event, finished, done. *Ayer hablé con Juan*. *Comimos pizza*. *Salieron a las ocho*. If you can put a beginning and an end on it, this is your tense.",
        },
        {
            "kind": "mini_table",
            "title": "hablar — preterite (-ar)",
            "rows": [
                ["yo", "habl|é"],
                ["tú", "habl|aste"],
                ["él / ella / usted", "habl|ó"],
                ["nosotros / nosotras", "habl|amos"],
                ["ellos / ellas / ustedes", "habl|aron"],
            ],
            "footnote": "Accents on yo (-é) and él (-ó) are load-bearing.",
        },
        {
            "kind": "mini_table",
            "title": "comer — preterite (-er)",
            "rows": [
                ["yo", "com|í"],
                ["tú", "com|iste"],
                ["él / ella / usted", "com|ió"],
                ["nosotros / nosotras", "com|imos"],
                ["ellos / ellas / ustedes", "com|ieron"],
            ],
            "footnote": "-er and -ir share the same preterite endings.",
        },
        {
            "kind": "mini_table",
            "title": "vivir — preterite (-ir)",
            "rows": [
                ["yo", "viv|í"],
                ["tú", "viv|iste"],
                ["él / ella / usted", "viv|ió"],
                ["nosotros / nosotras", "viv|imos"],
                ["ellos / ellas / ustedes", "viv|ieron"],
            ],
            "footnote": "Identical endings to -er. nosotros matches the present.",
        },
        {
            "kind": "text",
            "title": "-AR nosotros looks identical to the present",
            "body": "*hablamos* could be \"we speak\" OR \"we spoke.\" Spanish lets context disambiguate. -ir verbs do the same: *vivimos* = we live / we lived.",
        },
    ],
    "recall": {
        "verb": "hablar",
        "answers": {
            "yo": "habl|é",
            "tú": "habl|aste",
            "él": "habl|ó",
            "nosotros": "habl|amos",
            "ellos": "habl|aron",
        },
    },
}

PRETERITE_REGULAR_RULE = {
    "kind": "table",
    "title": "Regular preterite endings",
    "headers": ["Pronoun", "-AR (hablar)", "-ER (comer)", "-IR (vivir)"],
    "rows": [
        ["yo", "hablé", "comí", "viví"],
        ["tú", "hablaste", "comiste", "viviste"],
        ["él / ella / usted", "habló", "comió", "vivió"],
        ["nosotros / nosotras", "hablamos", "comimos", "vivimos"],
        ["ellos / ellas / ustedes", "hablaron", "comieron", "vivieron"],
    ],
    "footnote": "-er and -ir share endings completely. -ar nosotros / -ir nosotros match their present forms — context disambiguates.",
}

# --- GL 17.1: Preterite Irregular (highly irregular: ser/ir/dar/ver/hacer/decir/traer/dormir/morir) ---
PRETERITE_IRREGULAR_INTRO = {
    "kind": "cards",
    "title": "Highly irregular preterites — memorize these",
    "cards": [
        {
            "kind": "text",
            "title": "ser and ir share the SAME preterite",
            "body": "Both *ser* and *ir* conjugate to *fui, fuiste, fue, fuimos, fueron* in the preterite. Context tells you which: *fui a Lima* = I went; *fui doctora* = I was a doctor. They merge in this tense and only this one.",
        },
        {
            "kind": "mini_table",
            "title": "ser / ir — preterite (identical)",
            "rows": [
                ["yo", "|fui"],
                ["tú", "|fuiste"],
                ["él / ella / usted", "|fue"],
                ["nosotros / nosotras", "|fuimos"],
                ["ellos / ellas / ustedes", "|fueron"],
            ],
            "footnote": "Both verbs share these forms; context tells you which.",
        },
        {
            "kind": "mini_table",
            "title": "dar — preterite (uses -er/-ir endings, no accents)",
            "rows": [
                ["yo", "|di"],
                ["tú", "d|iste"],
                ["él / ella / usted", "d|io"],
                ["nosotros / nosotras", "d|imos"],
                ["ellos / ellas / ustedes", "d|ieron"],
            ],
            "footnote": "Treats itself like an -er/-ir verb in the preterite.",
        },
        {
            "kind": "mini_table",
            "title": "ver — preterite (no accents)",
            "rows": [
                ["yo", "|vi"],
                ["tú", "v|iste"],
                ["él / ella / usted", "v|io"],
                ["nosotros / nosotras", "v|imos"],
                ["ellos / ellas / ustedes", "v|ieron"],
            ],
            "footnote": "Like dar — short forms, no accents.",
        },
        {
            "kind": "mini_table",
            "title": "hacer — preterite (strong stem hic-)",
            "rows": [
                ["yo", "hic|e"],
                ["tú", "hic|iste"],
                ["él / ella / usted", "hi|zo"],
                ["nosotros / nosotras", "hic|imos"],
                ["ellos / ellas / ustedes", "hic|ieron"],
            ],
            "footnote": "él form: c → z to keep the soft sound (hizo).",
        },
        {
            "kind": "mini_table",
            "title": "decir — preterite (j-stem)",
            "rows": [
                ["yo", "dij|e"],
                ["tú", "dij|iste"],
                ["él / ella / usted", "dij|o"],
                ["nosotros / nosotras", "dij|imos"],
                ["ellos / ellas / ustedes", "dij|eron"],
            ],
            "footnote": "j-stem drops the i in ellos: dijeron, NOT dijieron.",
        },
        {
            "kind": "mini_table",
            "title": "traer — preterite (j-stem)",
            "rows": [
                ["yo", "traj|e"],
                ["tú", "traj|iste"],
                ["él / ella / usted", "traj|o"],
                ["nosotros / nosotras", "traj|imos"],
                ["ellos / ellas / ustedes", "traj|eron"],
            ],
            "footnote": "Same j-stem family as decir.",
        },
        {
            "kind": "mini_table",
            "title": "dormir — preterite (o→u in él/ellos)",
            "rows": [
                ["yo", "dorm|í"],
                ["tú", "dorm|iste"],
                ["él / ella / usted", "d|urmió"],
                ["nosotros / nosotras", "dorm|imos"],
                ["ellos / ellas / ustedes", "d|urmieron"],
            ],
            "footnote": "Stem o → u only in 3rd person. morir follows the same pattern.",
        },
    ],
    "recall": {
        "verb": "ser",
        "answers": {
            "yo": "|fui",
            "tú": "|fuiste",
            "él": "|fue",
            "nosotros": "|fuimos",
            "ellos": "|fueron",
        },
    },
}

PRETERITE_IRREGULAR_RULE = {
    "kind": "table",
    "title": "Highly irregular preterites",
    "headers": ["Pronoun", "ser / ir", "dar", "hacer", "decir", "dormir"],
    "rows": [
        ["yo", "fui", "di", "hice", "dije", "dormí"],
        ["tú", "fuiste", "diste", "hiciste", "dijiste", "dormiste"],
        ["él / ella / usted", "fue", "dio", "hizo", "dijo", "durmió"],
        ["nosotros / nosotras", "fuimos", "dimos", "hicimos", "dijimos", "dormimos"],
        ["ellos / ellas / ustedes", "fueron", "dieron", "hicieron", "dijeron", "durmieron"],
    ],
    "footnote": "ser and ir share fui/fuiste/… in preterite. j-stem verbs (decir, traer) drop the i in ellos.",
}

# --- GL 17.2: Preterite Spelling Changes (yo-form spelling shifts) ---
PRET_SPELLING_INTRO = {
    "kind": "cards",
    "title": "Preterite spelling changes — yo form only",
    "cards": [
        {
            "kind": "text",
            "title": "Same sound problem as the present, different fix",
            "body": "Some verbs need a spelling tweak in the **yo** form of the preterite to keep the original sound. The endings stay regular (-é, -aste, -ó…); only the consonant just before the ending shifts.",
        },
        {
            "kind": "mini_table",
            "title": "llegar — preterite (g → gu in yo)",
            "rows": [
                ["yo", "llegu|é"],
                ["tú", "lleg|aste"],
                ["él / ella / usted", "lleg|ó"],
                ["nosotros / nosotras", "lleg|amos"],
                ["ellos / ellas / ustedes", "lleg|aron"],
            ],
            "footnote": "Insert u after g in yo to keep the hard g sound: llegué.",
        },
        {
            "kind": "mini_table",
            "title": "comenzar — preterite (z → c in yo)",
            "rows": [
                ["yo", "comenc|é"],
                ["tú", "comenz|aste"],
                ["él / ella / usted", "comenz|ó"],
                ["nosotros / nosotras", "comenz|amos"],
                ["ellos / ellas / ustedes", "comenz|aron"],
            ],
            "footnote": "z → c before -é in yo: comencé.",
        },
        {
            "kind": "mini_table",
            "title": "sacar — preterite (c → qu in yo)",
            "rows": [
                ["yo", "saqu|é"],
                ["tú", "sac|aste"],
                ["él / ella / usted", "sac|ó"],
                ["nosotros / nosotras", "sac|amos"],
                ["ellos / ellas / ustedes", "sac|aron"],
            ],
            "footnote": "c → qu before -é in yo to keep the hard c sound.",
        },
        {
            "kind": "text",
            "title": "Vowel-stem verbs: i → y in él / ellos",
            "body": "Verbs like **leer, creer, oír, caer, construir** — where an unstressed *i* would land between vowels — turn that i into y. *Leyó* (not *leió*). *Construyeron* (not *construieron*).",
        },
    ],
    "recall": {
        "verb": "llegar",
        "answers": {
            "yo": "llegu|é",
            "tú": "lleg|aste",
            "él": "lleg|ó",
            "nosotros": "lleg|amos",
            "ellos": "lleg|aron",
        },
    },
}

PRET_SPELLING_RULE = {
    "kind": "table",
    "title": "Preterite spelling changes",
    "headers": ["Pronoun", "buscar (c→qu)", "pagar (g→gu)", "empezar (z→c)", "leer (i→y)"],
    "rows": [
        ["yo", "busqué", "pagué", "empecé", "leí"],
        ["tú", "buscaste", "pagaste", "empezaste", "leíste"],
        ["él / ella / usted", "buscó", "pagó", "empezó", "leyó"],
        ["nosotros / nosotras", "buscamos", "pagamos", "empezamos", "leímos"],
        ["ellos / ellas / ustedes", "buscaron", "pagaron", "empezaron", "leyeron"],
    ],
    "footnote": "-car/-gar/-zar shift only in yo. Vowel-stem verbs (leer, construir) shift i→y in él/ellos.",
}

# --- GL 17.3: Preterite Strong (-u-, -i- stem irregulars) ---
PRET_STRONG_INTRO = {
    "kind": "cards",
    "title": "Strong preterites — no accents, modified stems",
    "cards": [
        {
            "kind": "text",
            "title": "A different shape — and they share endings",
            "body": "About 15 important verbs use a special preterite called the \"strong\" preterite. They all swap their stem (estar → estuv-, tener → tuv-, poder → pud-…) and they all share the SAME set of endings — endings with NO accent marks.",
        },
        {
            "kind": "mini_table",
            "title": "tener — strong preterite (stem tuv-)",
            "rows": [
                ["yo", "tuv|e"],
                ["tú", "tuv|iste"],
                ["él / ella / usted", "tuv|o"],
                ["nosotros / nosotras", "tuv|imos"],
                ["ellos / ellas / ustedes", "tuv|ieron"],
            ],
            "footnote": "Plain -e in yo and -o in él (no accents).",
        },
        {
            "kind": "mini_table",
            "title": "poner — strong preterite (stem pus-)",
            "rows": [
                ["yo", "pus|e"],
                ["tú", "pus|iste"],
                ["él / ella / usted", "pus|o"],
                ["nosotros / nosotras", "pus|imos"],
                ["ellos / ellas / ustedes", "pus|ieron"],
            ],
            "footnote": "Same shared endings as tener.",
        },
        {
            "kind": "mini_table",
            "title": "hacer — strong preterite (stem hic-, él: hizo)",
            "rows": [
                ["yo", "hic|e"],
                ["tú", "hic|iste"],
                ["él / ella / usted", "hi|zo"],
                ["nosotros / nosotras", "hic|imos"],
                ["ellos / ellas / ustedes", "hic|ieron"],
            ],
            "footnote": "él form: c → z to keep the soft sound (hizo).",
        },
    ],
    "recall": {
        "verb": "tener",
        "answers": {
            "yo": "tuv|e",
            "tú": "tuv|iste",
            "él": "tuv|o",
            "nosotros": "tuv|imos",
            "ellos": "tuv|ieron",
        },
    },
}

PRET_STRONG_RULE = {
    "kind": "table",
    "title": "Strong preterites — shared endings, modified stems",
    "headers": ["Pronoun", "estar (estuv-)", "tener (tuv-)", "poder (pud-)", "poner (pus-)", "venir (vin-)"],
    "rows": [
        ["yo", "estuve", "tuve", "pude", "puse", "vine"],
        ["tú", "estuviste", "tuviste", "pudiste", "pusiste", "viniste"],
        ["él / ella / usted", "estuvo", "tuvo", "pudo", "puso", "vino"],
        ["nosotros / nosotras", "estuvimos", "tuvimos", "pudimos", "pusimos", "vinimos"],
        ["ellos / ellas / ustedes", "estuvieron", "tuvieron", "pudieron", "pusieron", "vinieron"],
    ],
    "footnote": "Plain -e in yo and -o in él (no accents) is the giveaway. Same endings across all strong preterites.",
}

# --- GL 17.4: Preterite -DUCIR verbs ---
PRET_DUCIR_INTRO = {
    "kind": "cards",
    "title": "Preterite of -ducir verbs",
    "cards": [
        {
            "kind": "text",
            "title": "All -DUCIR verbs use the j-stem pattern",
            "body": "Every Spanish verb ending in **-ducir** (traducir, conducir, producir, introducir, reducir…) uses the same preterite: stem ends in **-duj-** and takes strong-preterite endings. They share a special quirk with decir and traer: the ellos form drops the i.",
        },
        {
            "kind": "mini_table",
            "title": "producir — preterite (j-stem produj-)",
            "rows": [
                ["yo", "produj|e"],
                ["tú", "produj|iste"],
                ["él / ella / usted", "produj|o"],
                ["nosotros / nosotras", "produj|imos"],
                ["ellos / ellas / ustedes", "produj|eron"],
            ],
            "footnote": "ellos drops the i: produjeron, NOT produjieron.",
        },
        {
            "kind": "mini_table",
            "title": "traducir — preterite (j-stem traduj-)",
            "rows": [
                ["yo", "traduj|e"],
                ["tú", "traduj|iste"],
                ["él / ella / usted", "traduj|o"],
                ["nosotros / nosotras", "traduj|imos"],
                ["ellos / ellas / ustedes", "traduj|eron"],
            ],
            "footnote": "Same pattern as all -ducir verbs.",
        },
    ],
    "recall": {
        "verb": "producir",
        "answers": {
            "yo": "produj|e",
            "tú": "produj|iste",
            "él": "produj|o",
            "nosotros": "produj|imos",
            "ellos": "produj|eron",
        },
    },
}

PRET_DUCIR_RULE = {
    "kind": "table",
    "title": "Preterite of -DUCIR verbs",
    "headers": ["Pronoun", "traducir", "conducir", "producir", "introducir"],
    "rows": [
        ["yo", "traduje", "conduje", "produje", "introduje"],
        ["tú", "tradujiste", "condujiste", "produjiste", "introdujiste"],
        ["él / ella / usted", "tradujo", "condujo", "produjo", "introdujo"],
        ["nosotros / nosotras", "tradujimos", "condujimos", "produjimos", "introdujimos"],
        ["ellos / ellas / ustedes", "tradujeron", "condujeron", "produjeron", "introdujeron"],
    ],
    "footnote": "All -ducir verbs follow this pattern. ellos always drops the i: -jeron, never -jieron.",
}

# --- GL 17.5: Preterite e→i (only in él/ellos for -ir verbs) ---
PRET_E_TO_I_INTRO = {
    "kind": "cards",
    "title": "Preterite e→i — only -ir stem-changers",
    "cards": [
        {
            "kind": "text",
            "title": "A small change in just two forms",
            "body": "**-ir verbs** that have a stem change in the present (pedir, sentir, repetir, servir, dormir, morir) keep a smaller version of that change in the preterite — but only in the **él** and **ellos** forms. Everything else is regular.",
        },
        {
            "kind": "mini_table",
            "title": "pedir — preterite (e→i in él/ellos)",
            "rows": [
                ["yo", "ped|í"],
                ["tú", "ped|iste"],
                ["él / ella / usted", "p|idió"],
                ["nosotros / nosotras", "ped|imos"],
                ["ellos / ellas / ustedes", "p|idieron"],
            ],
            "footnote": "Stem changes only in 3rd person; everything else is regular -ir.",
        },
        {
            "kind": "mini_table",
            "title": "servir — preterite (e→i in él/ellos)",
            "rows": [
                ["yo", "serv|í"],
                ["tú", "serv|iste"],
                ["él / ella / usted", "s|irvió"],
                ["nosotros / nosotras", "serv|imos"],
                ["ellos / ellas / ustedes", "s|irvieron"],
            ],
            "footnote": "Same pattern as pedir.",
        },
        {
            "kind": "mini_table",
            "title": "dormir — preterite (o→u in él/ellos)",
            "rows": [
                ["yo", "dorm|í"],
                ["tú", "dorm|iste"],
                ["él / ella / usted", "d|urmió"],
                ["nosotros / nosotras", "dorm|imos"],
                ["ellos / ellas / ustedes", "d|urmieron"],
            ],
            "footnote": "o→u variant of the same -ir 3rd-person pattern. morir follows the same.",
        },
    ],
    "recall": {
        "verb": "pedir",
        "answers": {
            "yo": "ped|í",
            "tú": "ped|iste",
            "él": "p|idió",
            "nosotros": "ped|imos",
            "ellos": "p|idieron",
        },
    },
}

PRET_E_TO_I_RULE = {
    "kind": "table",
    "title": "Preterite e→i (-ir stem changers)",
    "headers": ["Pronoun", "pedir", "sentir", "repetir", "servir"],
    "rows": [
        ["yo", "pedí", "sentí", "repetí", "serví"],
        ["tú", "pediste", "sentiste", "repetiste", "serviste"],
        ["él / ella / usted", "pidió", "sintió", "repitió", "sirvió"],
        ["nosotros / nosotras", "pedimos", "sentimos", "repetimos", "servimos"],
        ["ellos / ellas / ustedes", "pidieron", "sintieron", "repitieron", "sirvieron"],
    ],
    "footnote": "Stem changes ONLY in él and ellos. yo, tú, nosotros stay fully regular.",
}

# --- GL 18: Gerund (estar + -ando / -iendo) ---
GERUND_INTRO = {
    "kind": "cards",
    "title": "Gerund — \"to be doing something\"",
    "cards": [
        {
            "kind": "text",
            "title": "estar + gerund — what's happening RIGHT NOW",
            "body": "When the action is in progress at this moment, Spanish uses **estar + the gerund** (-ando / -iendo). *Estoy comiendo* — I am eating (this very second). This is the present progressive: ongoing right now, not just \"I eat in general.\"",
        },
        {
            "kind": "mini_table",
            "title": "hablar — gerund (-ando)",
            "rows": [
                ["yo", "estoy habl|ando"],
                ["tú", "estás habl|ando"],
                ["él / ella / usted", "está habl|ando"],
                ["nosotros / nosotras", "estamos habl|ando"],
                ["ellos / ellas / ustedes", "están habl|ando"],
            ],
            "footnote": "-ar verbs take -ando. The gerund itself never changes.",
        },
        {
            "kind": "mini_table",
            "title": "comer — gerund (-iendo)",
            "rows": [
                ["yo", "estoy com|iendo"],
                ["tú", "estás com|iendo"],
                ["él / ella / usted", "está com|iendo"],
                ["nosotros / nosotras", "estamos com|iendo"],
                ["ellos / ellas / ustedes", "están com|iendo"],
            ],
            "footnote": "-er and -ir verbs both take -iendo.",
        },
        {
            "kind": "mini_table",
            "title": "leer — gerund (-yendo, vowel-stem)",
            "rows": [
                ["yo", "estoy le|yendo"],
                ["tú", "estás le|yendo"],
                ["él / ella / usted", "está le|yendo"],
                ["nosotros / nosotras", "estamos le|yendo"],
                ["ellos / ellas / ustedes", "están le|yendo"],
            ],
            "footnote": "i → y between vowels. Same shift in oír (oyendo), construir (construyendo).",
        },
        {
            "kind": "mini_table",
            "title": "dormir — gerund (stem o→u)",
            "rows": [
                ["yo", "estoy d|urmiendo"],
                ["tú", "estás d|urmiendo"],
                ["él / ella / usted", "está d|urmiendo"],
                ["nosotros / nosotras", "estamos d|urmiendo"],
                ["ellos / ellas / ustedes", "están d|urmiendo"],
            ],
            "footnote": "-ir stem-changers shift in the gerund: dormir → durmiendo, pedir → pidiendo.",
        },
        {
            "kind": "text",
            "title": "Don't use the gerund for the future",
            "body": "In English we say \"I'm leaving tomorrow.\" In Spanish, that's NOT *estoy saliendo mañana* — use simple present (*salgo mañana*) or *ir a + inf* (*voy a salir mañana*). The Spanish gerund really means \"in progress right now.\"",
        },
    ],
    "recall": {
        "verb": "hablar",
        "answers": {
            "yo": "estoy habl|ando",
            "tú": "estás habl|ando",
            "él": "está habl|ando",
            "nosotros": "estamos habl|ando",
            "ellos": "están habl|ando",
        },
    },
}

GERUND_RULE = {
    "kind": "table",
    "title": "estar + gerund — present progressive",
    "headers": ["Pronoun", "hablando (-ar)", "comiendo (-er)", "viviendo (-ir)", "leyendo (i→y)"],
    "rows": [
        ["yo", "estoy hablando", "estoy comiendo", "estoy viviendo", "estoy leyendo"],
        ["tú", "estás hablando", "estás comiendo", "estás viviendo", "estás leyendo"],
        ["él / ella / usted", "está hablando", "está comiendo", "está viviendo", "está leyendo"],
        ["nosotros / nosotras", "estamos hablando", "estamos comiendo", "estamos viviendo", "estamos leyendo"],
        ["ellos / ellas / ustedes", "están hablando", "están comiendo", "están viviendo", "están leyendo"],
    ],
    "footnote": "Only estar conjugates. The gerund stays fixed regardless of who's doing it.",
}

# --- GL 19: Object pronouns ---
OBJ_DIRECT_INTRO = {
    "kind": "cards",
    "title": "Direct object pronouns — \"it,\" \"them,\" \"him,\" \"her\"",
    "cards": [
        {
            "kind": "text",
            "title": "Replace the noun receiving the action",
            "body": "Instead of repeating *el libro* in every sentence, you say *lo*: \"I read **it**.\" Direct object pronouns answer *what?* or *who?* the verb is acting on, and they go BEFORE the conjugated verb.",
        },
        {
            "kind": "rule_pack",
            "title": "Forms",
            "sections": [
                {"heading": "Singular", "items": ["lo (it/him, masculine)", "la (it/her, feminine)"]},
                {"heading": "Plural", "items": ["los (them, masculine/mixed)", "las (them, all-feminine)"]},
                {"heading": "Examples", "items": ["¿Tienes el libro? — Sí, **lo** tengo.", "¿Conoces a María? — Sí, **la** conozco.", "¿Compraste los boletos? — Sí, **los** compré.", "¿Vas a hacer las tareas? — Sí, voy a hacer**las**. (or: las voy a hacer)"]},
            ],
            "footnote": "With infinitives and gerunds, the pronoun can attach to the end (hacerlas, comprándolos) or sit before the conjugated helper.",
        },
    ],
}

OBJ_INDIRECT_INTRO = {
    "kind": "cards",
    "title": "Indirect object pronouns — \"to me,\" \"to him,\" \"to them\"",
    "cards": [
        {
            "kind": "text",
            "title": "The recipient of the action",
            "body": "Indirect objects answer *to whom?* or *for whom?* In *I gave the book to María*, **to María** is the indirect object. Spanish uses pronouns: *Le di el libro*. They go before the verb, just like direct objects.",
        },
        {
            "kind": "rule_pack",
            "title": "Forms (these don't change for gender)",
            "sections": [
                {"heading": "Singular", "items": ["me (to me)", "te (to you, informal)", "le (to him / her / you-formal)"]},
                {"heading": "Plural", "items": ["nos (to us)", "les (to them / to you-all)"]},
                {"heading": "Examples", "items": ["**Me** dijo la verdad. (He told me the truth.)", "**Te** voy a comprar un regalo.", "**Le** escribí una carta a Juan.", "**Les** mandamos las fotos."]},
            ],
            "footnote": "Often you'll see redundancy: *Le di el libro a María.* The 'le' is required even though 'a María' clarifies. Spanish loves the double-mention.",
        },
    ],
}

OBJ_COMBINED_INTRO = {
    "kind": "cards",
    "title": "Two pronouns at once — indirect THEN direct",
    "cards": [
        {
            "kind": "text",
            "title": "Order matters: indirect first, then direct",
            "body": "When you have both — \"He gave it to me\" — the indirect goes first, the direct second, and both go before the verb. **Me lo dio.** (To-me + it + he-gave.) Always: indirect → direct → verb.",
        },
        {
            "kind": "text",
            "title": "le + lo / la / los / las → SE",
            "body": "Spanish doesn't allow two pronouns starting with l in a row. So **le lo** and **les la** and similar combos all change to **se**: *Se lo di* (I gave it to him), *Se las mandamos* (We sent them to her). The 'se' here doesn't mean reflexive — it's a phonetic workaround.",
        },
        {
            "kind": "rule_pack",
            "title": "All combinations",
            "sections": [
                {"heading": "me / te / nos + direct", "items": ["me lo, me la, me los, me las", "te lo, te la, te los, te las", "nos lo, nos la, nos los, nos las"]},
                {"heading": "le / les become se", "items": ["se lo, se la, se los, se las (used for him, her, you-formal, them, you-all)"]},
                {"heading": "Examples", "items": ["¿El libro? — **Me lo** dio ayer.", "¿La carta? — **Se la** mandé a Juan.", "¿Los boletos? — Te **los** compro yo."]},
            ],
            "footnote": "Order is rigid: indirect first, direct second, both before the verb (or both attached to an infinitive/gerund).",
        },
    ],
}

OBJ_COMBINED_RULE = {
    "kind": "table",
    "title": "Combined object pronouns",
    "headers": ["Indirect", "+ lo", "+ la", "+ los", "+ las"],
    "rows": [
        ["me", "me lo", "me la", "me los", "me las"],
        ["te", "te lo", "te la", "te los", "te las"],
        ["le → se", "se lo", "se la", "se los", "se las"],
        ["nos", "nos lo", "nos la", "nos los", "nos las"],
        ["les → se", "se lo", "se la", "se los", "se las"],
    ],
    "footnote": "Indirect (me/te/se/nos/se) goes BEFORE direct (lo/la/los/las). le/les always become se before lo/la/los/las.",
}

# --- GL 20: Present Subjunctive ---
SUBJ_PRES_INTRO = {
    "kind": "cards",
    "title": "Present Subjunctive — for desires, doubts, emotions",
    "cards": [
        {
            "kind": "text",
            "title": "Not a tense — a mood",
            "body": "The subjunctive isn't about *when* — it's about *attitude*. You use it when the speaker is expressing wishes, doubts, emotions, or things that aren't yet real: *Espero que vengas* (I hope you come). *Quiero que sepa la verdad* (I want him to know).",
        },
        {
            "kind": "text",
            "title": "Trigger phrases (the WEDDING acronym)",
            "body": "**W**ish: *quiero que…*  **E**motion: *me alegro de que…*  **D**oubt: *dudo que…*  **D**enial: *no creo que…*  **I**mpersonal: *es importante que…*  **N**egation: *no es verdad que…*  **G**od / wishes: *ojalá que…*  When you see one of these phrases, the verb that follows goes in the subjunctive.",
        },
        {
            "kind": "mini_table",
            "title": "hablar — present subjunctive (-ar → -e)",
            "rows": [
                ["yo", "habl|e"],
                ["tú", "habl|es"],
                ["él / ella / usted", "habl|e"],
                ["nosotros / nosotras", "habl|emos"],
                ["ellos / ellas / ustedes", "habl|en"],
            ],
            "footnote": "-ar verbs take opposite-vowel -e endings.",
        },
        {
            "kind": "mini_table",
            "title": "comer — present subjunctive (-er → -a)",
            "rows": [
                ["yo", "com|a"],
                ["tú", "com|as"],
                ["él / ella / usted", "com|a"],
                ["nosotros / nosotras", "com|amos"],
                ["ellos / ellas / ustedes", "com|an"],
            ],
            "footnote": "-er and -ir take -a endings. Same set on vivir.",
        },
        {
            "kind": "mini_table",
            "title": "ser — present subjunctive (irregular)",
            "rows": [
                ["yo", "|sea"],
                ["tú", "|seas"],
                ["él / ella / usted", "|sea"],
                ["nosotros / nosotras", "|seamos"],
                ["ellos / ellas / ustedes", "|sean"],
            ],
            "footnote": "Suppletive sea- stem.",
        },
        {
            "kind": "mini_table",
            "title": "ir — present subjunctive (irregular)",
            "rows": [
                ["yo", "|vaya"],
                ["tú", "|vayas"],
                ["él / ella / usted", "|vaya"],
                ["nosotros / nosotras", "|vayamos"],
                ["ellos / ellas / ustedes", "|vayan"],
            ],
            "footnote": "Suppletive vaya- stem.",
        },
        {
            "kind": "mini_table",
            "title": "haber — present subjunctive (irregular)",
            "rows": [
                ["yo", "|haya"],
                ["tú", "|hayas"],
                ["él / ella / usted", "|haya"],
                ["nosotros / nosotras", "|hayamos"],
                ["ellos / ellas / ustedes", "|hayan"],
            ],
            "footnote": "Auxiliary haber, used to form perfect subjunctives.",
        },
        {
            "kind": "mini_table",
            "title": "saber — present subjunctive (irregular)",
            "rows": [
                ["yo", "sep|a"],
                ["tú", "sep|as"],
                ["él / ella / usted", "sep|a"],
                ["nosotros / nosotras", "sep|amos"],
                ["ellos / ellas / ustedes", "sep|an"],
            ],
            "footnote": "Stem changes from sab- to sep-.",
        },
        {
            "kind": "mini_table",
            "title": "dar — present subjunctive (irregular)",
            "rows": [
                ["yo", "d|é"],
                ["tú", "d|es"],
                ["él / ella / usted", "d|é"],
                ["nosotros / nosotras", "d|emos"],
                ["ellos / ellas / ustedes", "d|en"],
            ],
            "footnote": "Accent on yo and él (dé) distinguishes from preposition de.",
        },
        {
            "kind": "mini_table",
            "title": "estar — present subjunctive (irregular)",
            "rows": [
                ["yo", "est|é"],
                ["tú", "est|és"],
                ["él / ella / usted", "est|é"],
                ["nosotros / nosotras", "est|emos"],
                ["ellos / ellas / ustedes", "est|én"],
            ],
            "footnote": "Accents on every form except nosotros. Mnemonic for irregulars: DISHES — Dar, Ir, Ser, Haber, Estar, Saber.",
        },
    ],
    "recall": {
        "verb": "hablar",
        "answers": {
            "yo": "habl|e",
            "tú": "habl|es",
            "él": "habl|e",
            "nosotros": "habl|emos",
            "ellos": "habl|en",
        },
    },
}

SUBJ_PRES_RULE = {
    "kind": "table",
    "title": "Present Subjunctive",
    "headers": ["Pronoun", "hablar", "comer", "vivir", "ser (irreg.)", "ir (irreg.)"],
    "rows": [
        ["yo", "hable", "coma", "viva", "sea", "vaya"],
        ["tú", "hables", "comas", "vivas", "seas", "vayas"],
        ["él / ella / usted", "hable", "coma", "viva", "sea", "vaya"],
        ["nosotros / nosotras", "hablemos", "comamos", "vivamos", "seamos", "vayamos"],
        ["ellos / ellas / ustedes", "hablen", "coman", "vivan", "sean", "vayan"],
    ],
    "footnote": "Opposite vowel: -ar → -e, -er/-ir → -a. yo and él identical. Six irregulars: D-I-S-H-E-S.",
}

# --- GL 20: Imperfect Subjunctive ---
SUBJ_IMPF_INTRO = {
    "kind": "cards",
    "title": "Imperfect Subjunctive — past wishes, hypotheticals",
    "cards": [
        {
            "kind": "text",
            "title": "Same triggers as present subjunctive, but in a past context",
            "body": "Same WEDDING triggers (wishes, doubts, emotions…), but for past or hypothetical situations: *Quería que vinieras* (I wanted you to come). *Si tuviera dinero…* (If I had money…). It's also the workhorse of \"if I were\" sentences.",
        },
        {
            "kind": "text",
            "title": "Built from the THIRD-person preterite",
            "body": "Take the **ellos** form of the preterite, drop the -ron, and add new endings: *hablaron → habla- → hablara, hablaras…* Because it's based on the preterite, every preterite irregularity comes along for the ride.",
        },
        {
            "kind": "mini_table",
            "title": "hablar — imperfect subjunctive (regular)",
            "rows": [
                ["yo", "habl|ara"],
                ["tú", "habl|aras"],
                ["él / ella / usted", "habl|ara"],
                ["nosotros / nosotras", "habl|áramos"],
                ["ellos / ellas / ustedes", "habl|aran"],
            ],
            "footnote": "Built from ellos preterite stem habla-. Accent on nosotros.",
        },
        {
            "kind": "mini_table",
            "title": "tener — imperfect subjunctive (strong stem tuv-)",
            "rows": [
                ["yo", "tuv|iera"],
                ["tú", "tuv|ieras"],
                ["él / ella / usted", "tuv|iera"],
                ["nosotros / nosotras", "tuv|iéramos"],
                ["ellos / ellas / ustedes", "tuv|ieran"],
            ],
            "footnote": "Inherits the strong-preterite stem.",
        },
        {
            "kind": "mini_table",
            "title": "ser / ir — imperfect subjunctive (identical)",
            "rows": [
                ["yo", "|fuera"],
                ["tú", "|fueras"],
                ["él / ella / usted", "|fuera"],
                ["nosotros / nosotras", "|fuéramos"],
                ["ellos / ellas / ustedes", "|fueran"],
            ],
            "footnote": "Both verbs share these forms (from the shared preterite fui-).",
        },
        {
            "kind": "text",
            "title": "Two valid endings: -ra and -se",
            "body": "There's an alternate form ending in -se: *hablase, hablases, hablase, hablásemos, hablasen*. They're interchangeable, but the **-ra form is far more common** in everyday speech and is what we'll teach. Recognize -se when you read; produce -ra when you speak.",
        },
    ],
    "recall": {
        "verb": "hablar",
        "answers": {
            "yo": "habl|ara",
            "tú": "habl|aras",
            "él": "habl|ara",
            "nosotros": "habl|áramos",
            "ellos": "habl|aran",
        },
    },
}

SUBJ_IMPF_RULE = {
    "kind": "table",
    "title": "Imperfect Subjunctive (-ra form)",
    "headers": ["Pronoun", "hablar", "comer", "vivir", "ser/ir", "tener"],
    "rows": [
        ["yo", "hablara", "comiera", "viviera", "fuera", "tuviera"],
        ["tú", "hablaras", "comieras", "vivieras", "fueras", "tuvieras"],
        ["él / ella / usted", "hablara", "comiera", "viviera", "fuera", "tuviera"],
        ["nosotros / nosotras", "habláramos", "comiéramos", "viviéramos", "fuéramos", "tuviéramos"],
        ["ellos / ellas / ustedes", "hablaran", "comieran", "vivieran", "fueran", "tuvieran"],
    ],
    "footnote": "Built from the ellos preterite stem. Inherits every preterite irregularity. nosotros always carries an accent.",
}

# --- GL 18.5: Perfect Tenses (haber + past participle) ---
PERFECT_TENSES_INTRO = {
    "kind": "cards",
    "title": "Perfect tenses — \"have done,\" \"had done\"",
    "cards": [
        {
            "kind": "text",
            "title": "Two pieces: haber + past participle",
            "body": "Every perfect tense in Spanish has the same shape: conjugate **haber** (the auxiliary) + add the **past participle** of the action verb. *He hablado* = I have spoken. *Habían comido* = they had eaten. Only haber moves; the participle never changes.",
        },
        {
            "kind": "mini_table",
            "title": "haber — present (auxiliary for present perfect)",
            "rows": [
                ["yo", "|he"],
                ["tú", "|has"],
                ["él / ella / usted", "|ha"],
                ["nosotros / nosotras", "|hemos"],
                ["ellos / ellas / ustedes", "|han"],
            ],
            "footnote": "haber is auxiliary-only here; never means \"to have something.\"",
        },
        {
            "kind": "mini_table",
            "title": "hablar — past participle pattern (he hablado, etc.)",
            "rows": [
                ["yo", "he habl|ado"],
                ["tú", "has habl|ado"],
                ["él / ella / usted", "ha habl|ado"],
                ["nosotros / nosotras", "hemos habl|ado"],
                ["ellos / ellas / ustedes", "han habl|ado"],
            ],
            "footnote": "Regular -ar participle = -ado. -er/-ir take -ido (comido, vivido). The participle never changes for gender or number when used with haber.",
        },
        {
            "kind": "comparison",
            "title": "Four perfect tenses, all built the same way",
            "left": {"heading": "Past-leaning", "items": ["Present perfect: he hablado (I have spoken — recent or relevant now)", "Pluperfect: había hablado (I had spoken — past before another past)"]},
            "right": {"heading": "Future-leaning", "items": ["Future perfect: habré hablado (I will have spoken)", "Conditional perfect: habría hablado (I would have spoken)"]},
            "footnote": "Same recipe each time — only haber's tense changes. We focus on the present perfect and pluperfect first.",
        },
        {
            "kind": "mini_table",
            "title": "haber — imperfect (auxiliary for pluperfect)",
            "rows": [
                ["yo", "hab|ía"],
                ["tú", "hab|ías"],
                ["él / ella / usted", "hab|ía"],
                ["nosotros / nosotras", "hab|íamos"],
                ["ellos / ellas / ustedes", "hab|ían"],
            ],
            "footnote": "Combine with the participle: había hablado (I had spoken).",
        },
    ],
    "recall": {
        "verb": "haber",
        "answers": {
            "yo": "|he",
            "tú": "|has",
            "él": "|ha",
            "nosotros": "|hemos",
            "ellos": "|han",
        },
    },
}

PERFECT_TENSES_RULE = {
    "kind": "table",
    "title": "Perfect tenses — present perfect & pluperfect",
    "headers": ["Pronoun", "Present perfect (hablar)", "Present perfect (comer)", "Pluperfect (vivir)", "Pluperfect (hacer — irreg.)"],
    "rows": [
        ["yo", "he hablado", "he comido", "había vivido", "había hecho"],
        ["tú", "has hablado", "has comido", "habías vivido", "habías hecho"],
        ["él / ella / usted", "ha hablado", "ha comido", "había vivido", "había hecho"],
        ["nosotros / nosotras", "hemos hablado", "hemos comido", "habíamos vivido", "habíamos hecho"],
        ["ellos / ellas / ustedes", "han hablado", "han comido", "habían vivido", "habían hecho"],
    ],
    "footnote": "Same recipe: conjugate haber (present → present perfect, imperfect → pluperfect) + invariant past participle.",
}


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
        "intro_chart": {
            "kind": "pronoun_pairs",
            "title": "Subject pronouns (singular)",
            "pairs": [
                {"es": "yo", "en": "I"},
                {"es": "tú", "en": "you"},
                {"es": "él", "en": "he"},
                {"es": "ella", "en": "she"},
                {"es": "usted", "en": "you (formal)"},
            ],
        },
        "rule_chart": {'kind': 'table', 'title': 'Subject pronouns (singular)', 'headers': ['Person', 'Pronoun', 'English', 'Note'], 'rows': [['1st sg', 'yo', 'I', ''], ['2nd sg informal', 'tú', 'you', 'casual / friends / family'], ['3rd sg masc', 'él', 'he', ''], ['3rd sg fem', 'ella', 'she', ''], ['2nd sg formal', 'usted', 'you', 'polite / strangers / older / authority']], 'footnote': "Latin America uses 'tú' and 'usted' for the singular 'you'. The choice is about register, not number."},
        "drill_sentences": [
            {"en": "I am tall", "es": "Yo soy alto", "noun_id": None, "type": "written",
             "glosses": {"tall": "alto", "alto": "tall"}},
            {"en": "You are a tourist", "es": "Tú eres turista", "noun_id": None, "type": "auditory",
             "glosses": {"tourist": "turista", "turista": "tourist"}},
            {"en": "He is important", "es": "Él es importante", "noun_id": None, "type": "written",
             "glosses": {"important": "importante", "importante": "important"}},
            {"en": "She is elegant", "es": "Ella es elegante", "noun_id": None, "type": "auditory",
             "glosses": {"elegant": "elegante", "elegante": "elegant"}},
            {"en": "You are professional", "es": "Usted es profesional", "noun_id": None, "type": "written",
             "glosses": {"professional": "profesional", "profesional": "professional"}},
            {"en": "I am sociable", "es": "Yo soy social", "noun_id": None, "type": "auditory",
             "glosses": {"sociable": "social", "social": "sociable"}},
            {"en": "You are international", "es": "Tú eres internacional", "noun_id": None, "type": "written",
             "glosses": {"international": "internacional", "internacional": "international"}},
            {"en": "He is sociable", "es": "Él es social", "noun_id": None, "type": "auditory",
             "glosses": {"sociable": "social", "social": "sociable"}},
            {"en": "She is important", "es": "Ella es importante", "noun_id": None, "type": "written",
             "glosses": {"important": "importante", "importante": "important"}},
            {"en": "You are likeable", "es": "Usted es simpático", "noun_id": None, "type": "auditory",
             "glosses": {"likeable": "simpático", "simpático": "likeable"}},
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
        "intro_chart": {
            "kind": "pronoun_pairs",
            "title": "Subject pronouns (plural)",
            "pairs": [
                {"es": "nosotros", "en": "we (all male or mixed)"},
                {"es": "nosotras", "en": "we (all female)"},
                {"es": "ustedes", "en": "you guys"},
                {"es": "ellos", "en": "they (all male or mixed)"},
                {"es": "ellas", "en": "they (all female)"},
            ],
        },
        "rule_chart": {'kind': 'table', 'title': 'Subject pronouns (plural)', 'headers': ['Person', 'Pronoun', 'English', 'Note'], 'rows': [['1st pl masc/mixed', 'nosotros', 'we', ''], ['1st pl all-fem', 'nosotras', 'we', 'all-female group'], ['3rd pl masc/mixed', 'ellos', 'they', ''], ['3rd pl all-fem', 'ellas', 'they', 'all-female group'], ['2nd pl', 'ustedes', 'you all', "Latin America uses 'ustedes' for both formal and informal plural."]]},
        "drill_sentences": [
            {"en": "We are Colombian", "es": "Nosotros somos colombianos", "noun_id": None, "type": "written",
             "glosses": {"Colombian": "colombianos", "colombianos": "Colombian"}},
            {"en": "We (f) are Latin", "es": "Nosotras somos latinas", "noun_id": None, "type": "auditory",
             "glosses": {"Latin": "latinas", "latinas": "Latin"}},
            {"en": "They are sociable", "es": "Ellos son sociales", "noun_id": None, "type": "written",
             "glosses": {"sociable": "sociales", "sociales": "sociable"}},
            {"en": "They (f) are professional", "es": "Ellas son profesionales", "noun_id": None, "type": "auditory",
             "glosses": {"professional": "profesionales", "profesionales": "professional"}},
            {"en": "You all are tourists", "es": "Ustedes son turistas", "noun_id": None, "type": "written",
             "glosses": {"tourists": "turistas", "turistas": "tourists"}},
            {"en": "We are important", "es": "Nosotros somos importantes", "noun_id": None, "type": "auditory",
             "glosses": {"important": "importantes", "importantes": "important"}},
            {"en": "We (f) are international", "es": "Nosotras somos internacionales", "noun_id": None, "type": "written",
             "glosses": {"international": "internacionales", "internacionales": "international"}},
            {"en": "They are likeable", "es": "Ellos son simpáticos", "noun_id": None, "type": "auditory",
             "glosses": {"likeable": "simpáticos", "simpáticos": "likeable"}},
            {"en": "They (f) are elegant", "es": "Ellas son elegantes", "noun_id": None, "type": "written",
             "glosses": {"elegant": "elegantes", "elegantes": "elegant"}},
            {"en": "You all are tall", "es": "Ustedes son altos", "noun_id": None, "type": "auditory",
             "glosses": {"tall": "altos", "altos": "tall"}},
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
        "intro_chart": POSSESSIVE_ADJ_INTRO,
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "rule_chart": {'kind': 'table', 'title': 'Possessive adjectives — singular', 'headers': ['Form', 'Used for', 'Example'], 'rows': [['mi', 'my', 'mi casa'], ['tu', 'your (informal)', 'tu amigo'], ['su', 'his / her / your (formal) / their', 'su carro'], ['nuestro', 'our (masculine noun)', 'nuestro perro'], ['nuestra', 'our (feminine noun)', 'nuestra familia']], 'footnote': "'nuestro' / 'nuestra' agrees with the noun's gender. The others don't change with gender — only with number (mi → mis, tu → tus, su → sus)."},
        "drill_sentences": [
            {"en": "my house", "es": "mi casa", "noun_id": "casa", "type": "written", "glosses": {"house": "casa", "casa": "house"}},
            {"en": "your friend", "es": "tu amigo", "noun_id": "amigo", "type": "auditory", "glosses": {"friend": "amigo", "amigo": "friend"}},
            {"en": "his car", "es": "su carro", "noun_id": "carro", "type": "written", "glosses": {"car": "carro", "carro": "car"}},
            {"en": "our (f) family", "es": "nuestra familia", "noun_id": "familia", "type": "auditory", "glosses": {"family": "familia", "familia": "family"}},
            {"en": "our (m) dog", "es": "nuestro perro", "noun_id": "perro", "type": "written", "glosses": {"dog": "perro", "perro": "dog"}},
            {"en": "my book", "es": "mi libro", "noun_id": "libro", "type": "auditory", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "your name", "es": "tu nombre", "noun_id": "nombre", "type": "written", "glosses": {"name": "nombre", "nombre": "name"}},
            {"en": "her work", "es": "su trabajo", "noun_id": "trabajo", "type": "auditory", "glosses": {"work": "trabajo", "trabajo": "work"}},
            {"en": "our (f) city", "es": "nuestra ciudad", "noun_id": "ciudad", "type": "written", "glosses": {"city": "ciudad", "ciudad": "city"}},
            {"en": "our (m) plan", "es": "nuestro plan", "noun_id": "plan", "type": "auditory", "glosses": {"plan": "plan"}},
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
        "intro_chart": POSSESSIVE_ADJ_INTRO,
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "rule_chart": {'kind': 'table', 'title': 'Possessive adjectives — plural', 'headers': ['Form', 'Used for', 'Example'], 'rows': [['mis', 'my (plural)', 'mis libros'], ['tus', 'your (plural)', 'tus amigos'], ['sus', 'his/her/your(formal)/their (plural)', 'sus carros'], ['nuestros', 'our (masc. plural)', 'nuestros perros'], ['nuestras', 'our (fem. plural)', 'nuestras familias']]},
        "drill_sentences": [
            {"en": "my books", "es": "mis libros", "noun_id": "libro", "type": "written", "glosses": {"books": "libros", "libros": "books"}},
            {"en": "your friends", "es": "tus amigos", "noun_id": "amigo", "type": "auditory", "glosses": {"friends": "amigos", "amigos": "friends"}},
            {"en": "their cars", "es": "sus carros", "noun_id": "carro", "type": "written", "glosses": {"cars": "carros", "carros": "cars"}},
            {"en": "our (f) families", "es": "nuestras familias", "noun_id": "familia", "type": "auditory", "glosses": {"families": "familias", "familias": "families"}},
            {"en": "our (m) dogs", "es": "nuestros perros", "noun_id": "perro", "type": "written", "glosses": {"dogs": "perros", "perros": "dogs"}},
            {"en": "my houses", "es": "mis casas", "noun_id": "casa", "type": "auditory", "glosses": {"houses": "casas", "casas": "houses"}},
            {"en": "your works", "es": "tus trabajos", "noun_id": "trabajo", "type": "written", "glosses": {"works": "trabajos", "trabajos": "works"}},
            {"en": "their plans", "es": "sus planes", "noun_id": "plan", "type": "auditory", "glosses": {"plans": "planes", "planes": "plans"}},
            {"en": "our (f) cities", "es": "nuestras ciudades", "noun_id": "ciudad", "type": "written", "glosses": {"cities": "ciudades", "ciudades": "cities"}},
            {"en": "our (m) names", "es": "nuestros nombres", "noun_id": "nombre", "type": "auditory", "glosses": {"names": "nombres", "nombres": "names"}},
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
        "intro_chart": {
            "kind": "cards",
            "title": "Grammatical gender",
            "cards": [
                {
                    "kind": "text",
                    "title": "Spanish has gender",
                    "body": "Spanish nouns are either masculine or feminine. There's a trick to knowing which is which — how the word ends.",
                },
                {
                    "kind": "rule_pack",
                    "title": "Spanish noun gender — endings",
                    "sections": [
                        {"heading": "MAJE LONERS — masculine endings", "items": ["-ma  →  el problema, el sistema", "-je  →  el viaje, el pasaje", "-l  →  el animal, el papel", "-o  →  el libro, el caso", "-n  →  el limón, el examen", "-e  →  el café, el coche", "-r  →  el doctor, el actor", "-s  →  el atlas, el lunes"]},
                        {"heading": "DIONZA — feminine endings", "items": ["-d  →  la libertad, la verdad", "-ion  →  la nación, la opción", "-z  →  la vez, la luz", "-a  →  la casa, la mesa"]},
                    ],
                    "footnote": "These rules cover most nouns; learn exceptions case-by-case.",
                },
                {
                    "kind": "text",
                    "title": "The articles: el / la",
                    "body": "Singular nouns use **el** (masculine, like *niño*) or **la** (feminine, like *niña*) to mean \"the\". When the noun is plural (*niños*, *niñas*), **el** becomes **los** and **la** becomes **las**.",
                },
                {
                    "kind": "text",
                    "title": "Forming the plural",
                    "body": "In Spanish, most nouns add **-s** when they end in a vowel (libro → libros, casa → casas). Nouns ending in a consonant add **-es** (papel → papeles, ciudad → ciudades). Nouns ending in **-z** change to **-ces** (luz → luces).",
                },
            ],
        },
        "rule_chart": {'kind': 'rule_pack', 'title': 'Spanish noun gender — endings', 'sections': [{'heading': 'MAJE LONERS — masculine endings', 'items': ['-ma  →  el problema, el sistema', '-je  →  el viaje, el pasaje', '-l  →  el animal, el papel', '-o  →  el libro, el caso', '-n  →  el limón, el examen', '-e  →  el café, el coche', '-r  →  el doctor, el actor', '-s  →  el atlas, el lunes']}, {'heading': 'DIONZA — feminine endings', 'items': ['-d  →  la libertad, la verdad', '-ion  →  la nación, la opción', '-z  →  la vez, la luz', '-a  →  la casa, la mesa']}], 'footnote': 'Definite articles: el / la (singular), los / las (plural). These rules cover most nouns; learn exceptions case-by-case.'},
        "drill_sentences": [
            # 5 masculine singular
            {"en": "the book", "es": "el libro", "noun_id": "libro", "type": "written", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "the problem", "es": "el problema", "noun_id": "problema", "type": "auditory", "glosses": {"problem": "problema", "problema": "problem"}},
            {"en": "the trip", "es": "el viaje", "noun_id": "viaje", "type": "written", "glosses": {"trip": "viaje", "viaje": "trip"}},
            {"en": "the paper", "es": "el papel", "noun_id": "papel", "type": "auditory", "glosses": {"paper": "papel", "papel": "paper"}},
            {"en": "the doctor", "es": "el doctor", "noun_id": "doctor", "type": "written", "glosses": {}},
            # 5 masculine plural
            {"en": "the books", "es": "los libros", "noun_id": "libro", "type": "auditory", "glosses": {"books": "libros", "libros": "books"}},
            {"en": "the lemons", "es": "los limones", "noun_id": "limón", "type": "written", "glosses": {}},
            {"en": "the coffees", "es": "los cafés", "noun_id": "café", "type": "auditory", "glosses": {"coffees": "cafés", "cafés": "coffees"}},
            {"en": "the actors", "es": "los actores", "noun_id": "actor", "type": "written", "glosses": {"actors": "actores", "actores": "actors"}},
            {"en": "the Mondays", "es": "los lunes", "noun_id": "lunes", "type": "auditory", "glosses": {"Mondays": "lunes", "lunes": "Mondays"}},
            # 5 feminine singular
            {"en": "the house", "es": "la casa", "noun_id": "casa", "type": "written", "glosses": {"house": "casa", "casa": "house"}},
            {"en": "the freedom", "es": "la libertad", "noun_id": "libertad", "type": "auditory", "glosses": {"freedom": "libertad", "libertad": "freedom"}},
            {"en": "the nation", "es": "la nación", "noun_id": "nación", "type": "written", "glosses": {"nation": "nación", "nación": "nation"}},
            {"en": "the light", "es": "la luz", "noun_id": "luz", "type": "auditory", "glosses": {"light": "luz", "luz": "light"}},
            {"en": "the table", "es": "la mesa", "noun_id": "mesa", "type": "written", "glosses": {}},
            # 5 feminine plural
            {"en": "the houses", "es": "las casas", "noun_id": "casa", "type": "auditory", "glosses": {"houses": "casas", "casas": "houses"}},
            {"en": "the truths", "es": "las verdades", "noun_id": "verdad", "type": "written", "glosses": {"truths": "verdades", "verdades": "truths"}},
            {"en": "the nations", "es": "las naciones", "noun_id": "nación", "type": "auditory", "glosses": {"nations": "naciones", "naciones": "nations"}},
            {"en": "the lights", "es": "las luces", "noun_id": "luz", "type": "written", "glosses": {"lights": "luces", "luces": "lights"}},
            {"en": "the options", "es": "las opciones", "noun_id": "opción", "type": "auditory", "glosses": {"options": "opciones", "opciones": "options"}},
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
        "intro_chart": {
            "kind": "cards",
            "title": "Indefinite articles — un / una / unos / unas",
            "cards": [
                {
                    "kind": "text",
                    "title": "Singular: un / una",
                    "body": "**un** + masculine noun → *un libro*, *un actor*\n\n**una** + feminine noun → *una verdad*, *una luz*",
                },
                {
                    "kind": "text",
                    "title": "Plural: unos / unas",
                    "body": "**unos** + masculine plural → *unos libros*, *unos actores*\n\n**unas** + feminine plural → *unas verdades*, *unas luces*",
                },
                {
                    "kind": "text",
                    "title": "What about \"uno\"?",
                    "body": "**uno** is only used for counting or numbers (*uno, dos, tres*; *tengo uno*). Never use it as an article before a noun — use **un** or **una**.",
                },
            ],
        },
        "rule_chart": {'kind': 'rule_pack', 'title': 'Indefinite articles — un / una / unos / unas', 'sections': [{'heading': 'Singular', 'items': ['un + masculine noun  →  un libro, un actor', 'una + feminine noun  →  una verdad, una luz']}, {'heading': 'Plural', 'items': ['unos + masculine plural  →  unos libros', 'unas + feminine plural  →  unas verdades']}], 'footnote': "MAJE LONERS / DIONZA still apply: pick the article from the noun's ending."},
        "drill_sentences": [
            {"en": "a system", "es": "un sistema", "noun_id": "sistema", "type": "written", "glosses": {}},
            {"en": "a passage", "es": "un pasaje", "noun_id": "pasaje", "type": "auditory", "glosses": {"passage": "pasaje", "pasaje": "passage"}},
            {"en": "a paper", "es": "un papel", "noun_id": "papel", "type": "written", "glosses": {}},
            {"en": "a case", "es": "un caso", "noun_id": "caso", "type": "auditory", "glosses": {"case": "caso", "caso": "case"}},
            {"en": "an exam", "es": "un examen", "noun_id": "examen", "type": "written", "glosses": {"exam": "examen", "examen": "exam"}},
            {"en": "an actor", "es": "un actor", "noun_id": "actor", "type": "auditory", "glosses": {}},
            {"en": "an atlas", "es": "un atlas", "noun_id": "atlas", "type": "written", "glosses": {}},
            {"en": "a truth", "es": "una verdad", "noun_id": "verdad", "type": "auditory", "glosses": {"truth": "verdad", "verdad": "truth"}},
            {"en": "an option", "es": "una opción", "noun_id": "opción", "type": "written", "glosses": {"option": "opción", "opción": "option"}},
            {"en": "a light", "es": "una luz", "noun_id": "luz", "type": "auditory", "glosses": {"light": "luz", "luz": "light"}},
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
    # --- GL 3: Regular Present — split into per-family sub-blocks ---
    # Each sub-block is 2 drills + 1 chat. Sequence: AR (lesson 1-2.5) →
    # ER (3-4.5) → IR (5-6.5). Verbs are pipe-encoded (stem|ending) so the
    # FE renders endings in crimson; see ConjugationCell.
    #
    # RETIRED 2026-05-02 — replaced by the per-family sub-blocks below:
    #   grammar_regular_present_1, _1_chat, _2, _2_chat, _3, _3_chat
    # These IDs are intentionally absent from GRAMMAR_SITUATIONS so the
    # dashboard's "next lesson" pointer skips them. DB rows referencing
    # them are untouched (per the "never change situation IDs" rule);
    # get_grammar_config() returns None for unknown IDs and the FE handles
    # None as "no active lesson".

    # --- AR sub-block ---
    "grammar_regular_present_ar_1": {
        "title": "Regular Present — -AR (1/2)",
        "grammar_level": 3,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "escuchar"],
        "video_embed_id": "6jpCj97AHMN",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": REGULAR_PRESENT_AR_INTRO,
        "rule_chart": REGULAR_PRESENT_AR_RULE,
        "drill_config": {
            "answers": {
                "hablar": {
                    "yo": "habl|o", "tú": "habl|as", "él": "habl|a", "ella": "habl|a",
                    "usted": "habl|a", "nosotros": "habl|amos", "nosotras": "habl|amos",
                    "ellos": "habl|an", "ellas": "habl|an", "ustedes": "habl|an",
                },
                "escuchar": {
                    "yo": "escuch|o", "tú": "escuch|as", "él": "escuch|a", "ella": "escuch|a",
                    "usted": "escuch|a", "nosotros": "escuch|amos", "nosotras": "escuch|amos",
                    "ellos": "escuch|an", "ellas": "escuch|an", "ustedes": "escuch|an",
                },
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I speak Spanish", "es": "Yo hablo español", "noun_id": None, "type": "written",
             "glosses": {"Spanish": "español", "español": "Spanish"}},
            {"en": "You speak fast", "es": "Tú hablas rápido", "noun_id": None, "type": "auditory",
             "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "She speaks English", "es": "Ella habla inglés", "noun_id": None, "type": "written",
             "glosses": {"English": "inglés", "inglés": "English"}},
            {"en": "We (f) speak well", "es": "Nosotras hablamos bien", "noun_id": None, "type": "auditory",
             "glosses": {"well": "bien", "bien": "well"}},
            {"en": "You all speak a lot", "es": "Ustedes hablan mucho", "noun_id": None, "type": "written",
             "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "I listen the radio", "es": "Yo escucho la radio", "noun_id": None, "type": "auditory",
             "glosses": {"radio": "radio"}},
            {"en": "You listen music", "es": "Tú escuchas música", "noun_id": None, "type": "written",
             "glosses": {"music": "música", "música": "music"}},
            {"en": "He listens the song", "es": "Él escucha la canción", "noun_id": None, "type": "auditory",
             "glosses": {"song": "canción", "canción": "song"}},
            {"en": "We listen carefully", "es": "Nosotros escuchamos atentamente", "noun_id": None, "type": "written",
             "glosses": {"carefully": "atentamente", "atentamente": "carefully"}},
            {"en": "They (f) listen the news", "es": "Ellas escuchan la noticia", "noun_id": None, "type": "auditory",
             "glosses": {"news": "noticia", "noticia": "news"}},
        ],
        "drill_targets": [
            {"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "tú"},
            {"verb": "hablar", "pronoun": "ella"}, {"verb": "hablar", "pronoun": "nosotras"},
            {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "escuchar", "pronoun": "yo"},
            {"verb": "escuchar", "pronoun": "tú"}, {"verb": "escuchar", "pronoun": "él"},
            {"verb": "escuchar", "pronoun": "nosotros"}, {"verb": "escuchar", "pronoun": "ellas"},
        ],
        "phase_2_config": {
            "description": "Regular Present -AR (1/2): hablar, escuchar",
            "targets": [
                {"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "tú"},
                {"verb": "hablar", "pronoun": "ella"}, {"verb": "hablar", "pronoun": "nosotras"},
                {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "escuchar", "pronoun": "yo"},
                {"verb": "escuchar", "pronoun": "tú"}, {"verb": "escuchar", "pronoun": "él"},
                {"verb": "escuchar", "pronoun": "nosotros"}, {"verb": "escuchar", "pronoun": "ellas"},
            ],
        },
        "opener_en": "Do you speak English?",
        "opener_es": "¿Hablas inglés?",
    },
    "grammar_regular_present_ar_2": {
        "title": "Regular Present — -AR (2/2)",
        "grammar_level": 3,
        "lesson_number": 2,
        "lesson_type": "conjugation",
        "word_workload": ["cantar", "escuchar"],
        "video_embed_id": "6jpCj97AHMN",
        "drill_type": "conjugation",
        "tense": "present",
        "rule_chart": REGULAR_PRESENT_AR_RULE,
        "drill_config": {
            "answers": {
                "cantar": {
                    "yo": "cant|o", "tú": "cant|as", "él": "cant|a", "ella": "cant|a",
                    "usted": "cant|a", "nosotros": "cant|amos", "nosotras": "cant|amos",
                    "ellos": "cant|an", "ellas": "cant|an", "ustedes": "cant|an",
                },
                "escuchar": {
                    "yo": "escuch|o", "tú": "escuch|as", "él": "escuch|a", "ella": "escuch|a",
                    "usted": "escuch|a", "nosotros": "escuch|amos", "nosotras": "escuch|amos",
                    "ellos": "escuch|an", "ellas": "escuch|an", "ustedes": "escuch|an",
                },
            },
        },
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I sing in Spanish", "es": "Yo canto en español", "noun_id": None, "type": "written",
             "glosses": {"Spanish": "español", "español": "Spanish"}},
            {"en": "You sing well", "es": "Tú cantas bien", "noun_id": None, "type": "auditory",
             "glosses": {"well": "bien", "bien": "well"}},
            {"en": "She sings loudly", "es": "Ella canta alto", "noun_id": None, "type": "written",
             "glosses": {"loudly": "alto", "alto": "loudly"}},
            {"en": "We (f) sing together", "es": "Nosotras cantamos juntas", "noun_id": None, "type": "auditory",
             "glosses": {"together": "juntas", "juntas": "together"}},
            {"en": "They sing a song", "es": "Ellos cantan una canción", "noun_id": None, "type": "written",
             "glosses": {"song": "canción", "canción": "song"}},
            {"en": "I listen attentively", "es": "Yo escucho atentamente", "noun_id": None, "type": "auditory",
             "glosses": {"attentively": "atentamente", "atentamente": "attentively"}},
            {"en": "You listen the news", "es": "Tú escuchas la noticia", "noun_id": None, "type": "written",
             "glosses": {"news": "noticia", "noticia": "news"}},
            {"en": "He listens his teacher", "es": "Él escucha a su maestro", "noun_id": None, "type": "auditory",
             "glosses": {"teacher": "maestro", "maestro": "teacher"}},
            {"en": "We listen the music", "es": "Nosotros escuchamos la música", "noun_id": None, "type": "written",
             "glosses": {"music": "música", "música": "music"}},
            {"en": "You all listen carefully", "es": "Ustedes escuchan con cuidado", "noun_id": None, "type": "auditory",
             "glosses": {"carefully": "con cuidado", "con cuidado": "carefully"}},
        ],
        "drill_targets": [
            {"verb": "cantar", "pronoun": "yo"}, {"verb": "cantar", "pronoun": "tú"},
            {"verb": "cantar", "pronoun": "ella"}, {"verb": "cantar", "pronoun": "nosotras"},
            {"verb": "cantar", "pronoun": "ellos"}, {"verb": "escuchar", "pronoun": "yo"},
            {"verb": "escuchar", "pronoun": "tú"}, {"verb": "escuchar", "pronoun": "él"},
            {"verb": "escuchar", "pronoun": "nosotros"}, {"verb": "escuchar", "pronoun": "ustedes"},
        ],
        "phase_2_config": {
            "description": "Regular Present -AR (2/2): cantar, escuchar",
            "targets": [
                {"verb": "cantar", "pronoun": "yo"}, {"verb": "cantar", "pronoun": "tú"},
                {"verb": "cantar", "pronoun": "ella"}, {"verb": "cantar", "pronoun": "nosotras"},
                {"verb": "cantar", "pronoun": "ellos"}, {"verb": "escuchar", "pronoun": "yo"},
                {"verb": "escuchar", "pronoun": "tú"}, {"verb": "escuchar", "pronoun": "él"},
                {"verb": "escuchar", "pronoun": "nosotros"}, {"verb": "escuchar", "pronoun": "ustedes"},
            ],
        },
        "opener_en": "Do you sing in the shower?",
        "opener_es": "¿Cantas en la ducha?",
    },
    "grammar_regular_present_ar_chat": {
        "title": "Regular Present — -AR Chat",
        "grammar_level": 3,
        "lesson_number": 2.5,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "escuchar", "cantar"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Regular Present -AR chat: hablar, escuchar, cantar", "targets": [
            {"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "ella"},
            {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "escuchar", "pronoun": "tú"},
            {"verb": "escuchar", "pronoun": "nosotros"}, {"verb": "escuchar", "pronoun": "ellas"},
            {"verb": "cantar", "pronoun": "yo"}, {"verb": "cantar", "pronoun": "nosotras"},
            {"verb": "cantar", "pronoun": "él"}, {"verb": "cantar", "pronoun": "ellos"},
        ]},
    },

    # --- ER sub-block ---
    "grammar_regular_present_er_1": {
        "title": "Regular Present — -ER (1/2)",
        "grammar_level": 3,
        "lesson_number": 3,
        "lesson_type": "conjugation",
        "word_workload": ["beber", "comer"],
        "video_embed_id": "6jpCj97AHMN",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": REGULAR_PRESENT_ER_INTRO,
        "rule_chart": REGULAR_PRESENT_ER_RULE,
        "drill_config": {
            "answers": {
                "beber": {
                    "yo": "beb|o", "tú": "beb|es", "él": "beb|e", "ella": "beb|e",
                    "usted": "beb|e", "nosotros": "beb|emos", "nosotras": "beb|emos",
                    "ellos": "beb|en", "ellas": "beb|en", "ustedes": "beb|en",
                },
                "comer": {
                    "yo": "com|o", "tú": "com|es", "él": "com|e", "ella": "com|e",
                    "usted": "com|e", "nosotros": "com|emos", "nosotras": "com|emos",
                    "ellos": "com|en", "ellas": "com|en", "ustedes": "com|en",
                },
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I drink water", "es": "Yo bebo agua", "noun_id": None, "type": "written",
             "glosses": {"water": "agua", "agua": "water"}},
            {"en": "You drink coffee", "es": "Tú bebes café", "noun_id": "café", "type": "auditory",
             "glosses": {"coffee": "café", "café": "coffee"}},
            {"en": "She drinks juice", "es": "Ella bebe jugo", "noun_id": None, "type": "written",
             "glosses": {"juice": "jugo", "jugo": "juice"}},
            {"en": "We (f) drink tea", "es": "Nosotras bebemos té", "noun_id": None, "type": "auditory",
             "glosses": {"tea": "té", "té": "tea"}},
            {"en": "They drink milk", "es": "Ellos beben leche", "noun_id": None, "type": "written",
             "glosses": {"milk": "leche", "leche": "milk"}},
            {"en": "I eat fruit", "es": "Yo como fruta", "noun_id": None, "type": "auditory",
             "glosses": {"fruit": "fruta", "fruta": "fruit"}},
            {"en": "You eat bread", "es": "Tú comes pan", "noun_id": None, "type": "written",
             "glosses": {"bread": "pan", "pan": "bread"}},
            {"en": "He eats meat", "es": "Él come carne", "noun_id": None, "type": "auditory",
             "glosses": {"meat": "carne", "carne": "meat"}},
            {"en": "We eat together", "es": "Nosotros comemos juntos", "noun_id": None, "type": "written",
             "glosses": {"together": "juntos", "juntos": "together"}},
            {"en": "You all eat fast", "es": "Ustedes comen rápido", "noun_id": None, "type": "auditory",
             "glosses": {"fast": "rápido", "rápido": "fast"}},
        ],
        "drill_targets": [
            {"verb": "beber", "pronoun": "yo"}, {"verb": "beber", "pronoun": "tú"},
            {"verb": "beber", "pronoun": "ella"}, {"verb": "beber", "pronoun": "nosotras"},
            {"verb": "beber", "pronoun": "ellos"}, {"verb": "comer", "pronoun": "yo"},
            {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "él"},
            {"verb": "comer", "pronoun": "nosotros"}, {"verb": "comer", "pronoun": "ustedes"},
        ],
        "phase_2_config": {
            "description": "Regular Present -ER (1/2): beber, comer",
            "targets": [
                {"verb": "beber", "pronoun": "yo"}, {"verb": "beber", "pronoun": "tú"},
                {"verb": "beber", "pronoun": "ella"}, {"verb": "beber", "pronoun": "nosotras"},
                {"verb": "beber", "pronoun": "ellos"}, {"verb": "comer", "pronoun": "yo"},
                {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "él"},
                {"verb": "comer", "pronoun": "nosotros"}, {"verb": "comer", "pronoun": "ustedes"},
            ],
        },
        "opener_en": "What do you eat for lunch?",
        "opener_es": "¿Qué comes para el almuerzo?",
    },
    "grammar_regular_present_er_2": {
        "title": "Regular Present — -ER (2/2)",
        "grammar_level": 3,
        "lesson_number": 4,
        "lesson_type": "conjugation",
        "word_workload": ["leer", "comer"],
        "video_embed_id": "6jpCj97AHMN",
        "drill_type": "conjugation",
        "tense": "present",
        "rule_chart": REGULAR_PRESENT_ER_RULE,
        "drill_config": {
            "answers": {
                "leer": {
                    "yo": "le|o", "tú": "le|es", "él": "le|e", "ella": "le|e",
                    "usted": "le|e", "nosotros": "le|emos", "nosotras": "le|emos",
                    "ellos": "le|en", "ellas": "le|en", "ustedes": "le|en",
                },
                "comer": {
                    "yo": "com|o", "tú": "com|es", "él": "com|e", "ella": "com|e",
                    "usted": "com|e", "nosotros": "com|emos", "nosotras": "com|emos",
                    "ellos": "com|en", "ellas": "com|en", "ustedes": "com|en",
                },
            },
        },
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I read a lot", "es": "Yo leo mucho", "noun_id": None, "type": "written",
             "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "You read out loud", "es": "Tú lees en voz alta", "noun_id": None, "type": "auditory",
             "glosses": {"out loud": "en voz alta", "en voz alta": "out loud"}},
            {"en": "She reads a book", "es": "Ella lee un libro", "noun_id": "libro", "type": "written",
             "glosses": {"book": "libro", "libro": "book"}},
            {"en": "We (f) read in Spanish", "es": "Nosotras leemos en español", "noun_id": None, "type": "auditory",
             "glosses": {"Spanish": "español", "español": "Spanish"}},
            {"en": "They read fast", "es": "Ellos leen rápido", "noun_id": None, "type": "written",
             "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "I eat at home", "es": "Yo como en casa", "noun_id": None, "type": "auditory",
             "glosses": {"home": "casa", "casa": "home"}},
            {"en": "You eat fish", "es": "Tú comes pescado", "noun_id": None, "type": "written",
             "glosses": {"fish": "pescado", "pescado": "fish"}},
            {"en": "He eats vegetables", "es": "Él come verduras", "noun_id": None, "type": "auditory",
             "glosses": {"vegetables": "verduras", "verduras": "vegetables"}},
            {"en": "We eat early", "es": "Nosotros comemos temprano", "noun_id": None, "type": "written",
             "glosses": {"early": "temprano", "temprano": "early"}},
            {"en": "You all eat well", "es": "Ustedes comen bien", "noun_id": None, "type": "auditory",
             "glosses": {"well": "bien", "bien": "well"}},
        ],
        "drill_targets": [
            {"verb": "leer", "pronoun": "yo"}, {"verb": "leer", "pronoun": "tú"},
            {"verb": "leer", "pronoun": "ella"}, {"verb": "leer", "pronoun": "nosotras"},
            {"verb": "leer", "pronoun": "ellos"}, {"verb": "comer", "pronoun": "yo"},
            {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "él"},
            {"verb": "comer", "pronoun": "nosotros"}, {"verb": "comer", "pronoun": "ustedes"},
        ],
        "phase_2_config": {
            "description": "Regular Present -ER (2/2): leer, comer",
            "targets": [
                {"verb": "leer", "pronoun": "yo"}, {"verb": "leer", "pronoun": "tú"},
                {"verb": "leer", "pronoun": "ella"}, {"verb": "leer", "pronoun": "nosotras"},
                {"verb": "leer", "pronoun": "ellos"}, {"verb": "comer", "pronoun": "yo"},
                {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "él"},
                {"verb": "comer", "pronoun": "nosotros"}, {"verb": "comer", "pronoun": "ustedes"},
            ],
        },
        "opener_en": "Do you read in Spanish?",
        "opener_es": "¿Lees en español?",
    },
    "grammar_regular_present_er_chat": {
        "title": "Regular Present — -ER Chat",
        "grammar_level": 3,
        "lesson_number": 4.5,
        "lesson_type": "conjugation",
        "word_workload": ["beber", "comer", "leer"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Regular Present -ER chat: beber, comer, leer", "targets": [
            {"verb": "beber", "pronoun": "yo"}, {"verb": "beber", "pronoun": "ella"},
            {"verb": "beber", "pronoun": "ustedes"}, {"verb": "comer", "pronoun": "tú"},
            {"verb": "comer", "pronoun": "nosotros"}, {"verb": "comer", "pronoun": "ellas"},
            {"verb": "leer", "pronoun": "yo"}, {"verb": "leer", "pronoun": "nosotras"},
            {"verb": "leer", "pronoun": "él"}, {"verb": "leer", "pronoun": "ellos"},
        ]},
    },

    # --- IR sub-block ---
    "grammar_regular_present_ir_1": {
        "title": "Regular Present — -IR (1/2)",
        "grammar_level": 3,
        "lesson_number": 5,
        "lesson_type": "conjugation",
        "word_workload": ["vivir", "escribir"],
        "video_embed_id": "6jpCj97AHMN",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": REGULAR_PRESENT_IR_INTRO,
        "rule_chart": REGULAR_PRESENT_IR_RULE,
        "drill_config": {
            "answers": {
                "vivir": {
                    "yo": "viv|o", "tú": "viv|es", "él": "viv|e", "ella": "viv|e",
                    "usted": "viv|e", "nosotros": "viv|imos", "nosotras": "viv|imos",
                    "ellos": "viv|en", "ellas": "viv|en", "ustedes": "viv|en",
                },
                "escribir": {
                    "yo": "escrib|o", "tú": "escrib|es", "él": "escrib|e", "ella": "escrib|e",
                    "usted": "escrib|e", "nosotros": "escrib|imos", "nosotras": "escrib|imos",
                    "ellos": "escrib|en", "ellas": "escrib|en", "ustedes": "escrib|en",
                },
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I live here", "es": "Yo vivo aquí", "noun_id": None, "type": "written",
             "glosses": {"here": "aquí", "aquí": "here"}},
            {"en": "You live nearby", "es": "Tú vives cerca", "noun_id": None, "type": "auditory",
             "glosses": {"nearby": "cerca", "cerca": "nearby"}},
            {"en": "She lives in Mexico", "es": "Ella vive en México", "noun_id": None, "type": "written",
             "glosses": {"Mexico": "México", "México": "Mexico"}},
            {"en": "We (f) live together", "es": "Nosotras vivimos juntas", "noun_id": None, "type": "auditory",
             "glosses": {"together": "juntas", "juntas": "together"}},
            {"en": "They live in the city", "es": "Ellos viven en la ciudad", "noun_id": None, "type": "written",
             "glosses": {"city": "ciudad", "ciudad": "city"}},
            {"en": "I write a letter", "es": "Yo escribo una carta", "noun_id": None, "type": "auditory",
             "glosses": {"letter": "carta", "carta": "letter"}},
            {"en": "You write well", "es": "Tú escribes bien", "noun_id": None, "type": "written",
             "glosses": {"well": "bien", "bien": "well"}},
            {"en": "He writes a book", "es": "Él escribe un libro", "noun_id": "libro", "type": "auditory",
             "glosses": {"book": "libro", "libro": "book"}},
            {"en": "We write messages", "es": "Nosotros escribimos mensajes", "noun_id": None, "type": "written",
             "glosses": {"messages": "mensajes", "mensajes": "messages"}},
            {"en": "You all write often", "es": "Ustedes escriben a menudo", "noun_id": None, "type": "auditory",
             "glosses": {"often": "a menudo", "a menudo": "often"}},
        ],
        "drill_targets": [
            {"verb": "vivir", "pronoun": "yo"}, {"verb": "vivir", "pronoun": "tú"},
            {"verb": "vivir", "pronoun": "ella"}, {"verb": "vivir", "pronoun": "nosotras"},
            {"verb": "vivir", "pronoun": "ellos"}, {"verb": "escribir", "pronoun": "yo"},
            {"verb": "escribir", "pronoun": "tú"}, {"verb": "escribir", "pronoun": "él"},
            {"verb": "escribir", "pronoun": "nosotros"}, {"verb": "escribir", "pronoun": "ustedes"},
        ],
        "phase_2_config": {
            "description": "Regular Present -IR (1/2): vivir, escribir",
            "targets": [
                {"verb": "vivir", "pronoun": "yo"}, {"verb": "vivir", "pronoun": "tú"},
                {"verb": "vivir", "pronoun": "ella"}, {"verb": "vivir", "pronoun": "nosotras"},
                {"verb": "vivir", "pronoun": "ellos"}, {"verb": "escribir", "pronoun": "yo"},
                {"verb": "escribir", "pronoun": "tú"}, {"verb": "escribir", "pronoun": "él"},
                {"verb": "escribir", "pronoun": "nosotros"}, {"verb": "escribir", "pronoun": "ustedes"},
            ],
        },
        "opener_en": "Where do you live?",
        "opener_es": "¿Dónde vives?",
    },
    "grammar_regular_present_ir_2": {
        "title": "Regular Present — -IR (2/2)",
        "grammar_level": 3,
        "lesson_number": 6,
        "lesson_type": "conjugation",
        "word_workload": ["abrir", "vivir"],
        "video_embed_id": "6jpCj97AHMN",
        "drill_type": "conjugation",
        "tense": "present",
        "rule_chart": REGULAR_PRESENT_IR_RULE,
        "drill_config": {
            "answers": {
                "abrir": {
                    "yo": "abr|o", "tú": "abr|es", "él": "abr|e", "ella": "abr|e",
                    "usted": "abr|e", "nosotros": "abr|imos", "nosotras": "abr|imos",
                    "ellos": "abr|en", "ellas": "abr|en", "ustedes": "abr|en",
                },
                "vivir": {
                    "yo": "viv|o", "tú": "viv|es", "él": "viv|e", "ella": "viv|e",
                    "usted": "viv|e", "nosotros": "viv|imos", "nosotras": "viv|imos",
                    "ellos": "viv|en", "ellas": "viv|en", "ustedes": "viv|en",
                },
            },
        },
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I open the door", "es": "Yo abro la puerta", "noun_id": None, "type": "written",
             "glosses": {"door": "puerta", "puerta": "door"}},
            {"en": "You open the window", "es": "Tú abres la ventana", "noun_id": None, "type": "auditory",
             "glosses": {"window": "ventana", "ventana": "window"}},
            {"en": "She opens the box", "es": "Ella abre la caja", "noun_id": None, "type": "written",
             "glosses": {"box": "caja", "caja": "box"}},
            {"en": "We (f) open the store", "es": "Nosotras abrimos la tienda", "noun_id": "tienda", "type": "auditory",
             "glosses": {"store": "tienda", "tienda": "store"}},
            {"en": "They open the gift", "es": "Ellos abren el regalo", "noun_id": None, "type": "written",
             "glosses": {"gift": "regalo", "regalo": "gift"}},
            {"en": "I live in the country", "es": "Yo vivo en el campo", "noun_id": None, "type": "auditory",
             "glosses": {"country": "campo", "campo": "country"}},
            {"en": "You live alone", "es": "Tú vives solo", "noun_id": None, "type": "written",
             "glosses": {"alone": "solo", "solo": "alone"}},
            {"en": "He lives far away", "es": "Él vive lejos", "noun_id": None, "type": "auditory",
             "glosses": {"far away": "lejos", "lejos": "far away"}},
            {"en": "We live in an apartment", "es": "Nosotros vivimos en un apartamento", "noun_id": None, "type": "written",
             "glosses": {"apartment": "apartamento", "apartamento": "apartment"}},
            {"en": "You all live well", "es": "Ustedes viven bien", "noun_id": None, "type": "auditory",
             "glosses": {"well": "bien", "bien": "well"}},
        ],
        "drill_targets": [
            {"verb": "abrir", "pronoun": "yo"}, {"verb": "abrir", "pronoun": "tú"},
            {"verb": "abrir", "pronoun": "ella"}, {"verb": "abrir", "pronoun": "nosotras"},
            {"verb": "abrir", "pronoun": "ellos"}, {"verb": "vivir", "pronoun": "yo"},
            {"verb": "vivir", "pronoun": "tú"}, {"verb": "vivir", "pronoun": "él"},
            {"verb": "vivir", "pronoun": "nosotros"}, {"verb": "vivir", "pronoun": "ustedes"},
        ],
        "phase_2_config": {
            "description": "Regular Present -IR (2/2): abrir, vivir",
            "targets": [
                {"verb": "abrir", "pronoun": "yo"}, {"verb": "abrir", "pronoun": "tú"},
                {"verb": "abrir", "pronoun": "ella"}, {"verb": "abrir", "pronoun": "nosotras"},
                {"verb": "abrir", "pronoun": "ellos"}, {"verb": "vivir", "pronoun": "yo"},
                {"verb": "vivir", "pronoun": "tú"}, {"verb": "vivir", "pronoun": "él"},
                {"verb": "vivir", "pronoun": "nosotros"}, {"verb": "vivir", "pronoun": "ustedes"},
            ],
        },
        "opener_en": "What time do you open the store?",
        "opener_es": "¿A qué hora abres la tienda?",
    },
    "grammar_regular_present_ir_chat": {
        "title": "Regular Present — -IR Chat",
        "grammar_level": 3,
        "lesson_number": 6.5,
        "lesson_type": "conjugation",
        "word_workload": ["vivir", "escribir", "abrir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Regular Present -IR chat: vivir, escribir, abrir", "targets": [
            {"verb": "vivir", "pronoun": "yo"}, {"verb": "vivir", "pronoun": "ella"},
            {"verb": "vivir", "pronoun": "ustedes"}, {"verb": "escribir", "pronoun": "tú"},
            {"verb": "escribir", "pronoun": "nosotros"}, {"verb": "escribir", "pronoun": "ellas"},
            {"verb": "abrir", "pronoun": "yo"}, {"verb": "abrir", "pronoun": "nosotras"},
            {"verb": "abrir", "pronoun": "él"}, {"verb": "abrir", "pronoun": "ellos"},
        ]},
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
        "intro_chart": IRREGULAR_PRESENT_INTRO,
        "rule_chart": IRREGULAR_PRESENT_RULE,
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
            {"en": "I am tall", "es": "Yo soy alto", "noun_id": None, "type": "written", "glosses": {"tall": "alto", "alto": "tall"}},
            {"en": "You are here", "es": "Tú estás aquí", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "He goes to the market", "es": "Él va al mercado", "noun_id": "mercado", "type": "written", "glosses": {"market": "mercado", "mercado": "market"}},
            {"en": "She gives the book", "es": "Ella da el libro", "noun_id": "libro", "type": "auditory", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "You have a dog", "es": "Usted tiene un perro", "noun_id": "perro", "type": "written", "glosses": {}},
            {"en": "We come home", "es": "Nosotros venimos a casa", "noun_id": "casa", "type": "auditory", "glosses": {"at home": "en casa", "en casa": "at home"}},
            {"en": "We (f) are professional", "es": "Nosotras somos profesional", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They are at home", "es": "Ellos están en casa", "noun_id": "casa", "type": "auditory", "glosses": {}},
            {"en": "They (f) go home", "es": "Ellas van a casa", "noun_id": "casa", "type": "written", "glosses": {}},
            {"en": "You all give money", "es": "Ustedes dan dinero", "noun_id": "dinero", "type": "auditory", "glosses": {"money": "dinero", "dinero": "money"}},
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
        "intro_chart": IRREGULAR_PRESENT_INTRO,
        "rule_chart": IRREGULAR_PRESENT_RULE,
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
            {"en": "I am professional", "es": "Yo soy profesional", "noun_id": None, "type": "written", "glosses": {"professional": "profesional", "profesional": "professional"}},
            {"en": "You are at home", "es": "Tú estás en casa", "noun_id": "casa", "type": "auditory", "glosses": {}},
            {"en": "He goes home", "es": "Él va a casa", "noun_id": "casa", "type": "written", "glosses": {}},
            {"en": "She gives money", "es": "Ella da dinero", "noun_id": "dinero", "type": "auditory", "glosses": {}},
            {"en": "You have a house", "es": "Usted tiene una casa", "noun_id": "casa", "type": "written", "glosses": {}},
            {"en": "We come from the park", "es": "Nosotros venimos del parque", "noun_id": "parque", "type": "auditory", "glosses": {"park": "parque", "parque": "park"}},
            {"en": "We (f) are important", "es": "Nosotras somos importante", "noun_id": None, "type": "written", "glosses": {"important": "importante", "importante": "important"}},
            {"en": "They are tired", "es": "Ellos están cansado", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "They (f) go to the park", "es": "Ellas van al parque", "noun_id": "parque", "type": "written", "glosses": {}},
            {"en": "You all give water", "es": "Ustedes dan agua", "noun_id": None, "type": "auditory", "glosses": {"water": "agua", "agua": "water"}},
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
        "intro_chart": IRREGULAR_PRESENT_INTRO,
        "rule_chart": IRREGULAR_PRESENT_RULE,
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
            {"en": "I am important", "es": "Yo soy importante", "noun_id": None, "type": "written", "glosses": {"important": "importante", "importante": "important"}},
            {"en": "You are tired", "es": "Tú estás cansado", "noun_id": None, "type": "auditory", "glosses": {"tired": "cansado", "cansado": "tired"}},
            {"en": "He goes to the park", "es": "Él va al parque", "noun_id": "parque", "type": "written", "glosses": {}},
            {"en": "She gives water", "es": "Ella da agua", "noun_id": None, "type": "auditory", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "You have hunger", "es": "Usted tiene hambre", "noun_id": None, "type": "written", "glosses": {"hunger": "hambre", "hambre": "hunger"}},
            {"en": "We come early", "es": "Nosotros venimos temprano", "noun_id": None, "type": "auditory", "glosses": {"early": "temprano", "temprano": "early"}},
            {"en": "We (f) are likeable", "es": "Nosotras somos simpático", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They are well", "es": "Ellos están bien", "noun_id": None, "type": "auditory", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "They (f) go to the store", "es": "Ellas van a la tienda", "noun_id": "tienda", "type": "written", "glosses": {}},
            {"en": "You all give an answer", "es": "Ustedes dan una respuesta", "noun_id": None, "type": "auditory", "glosses": {"answer": "respuesta", "respuesta": "answer"}},
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
        "intro_chart": SER_ESTAR_INTRO,
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "rule_chart": {'kind': 'comparison', 'title': 'Ser vs. Estar', 'left': {'heading': 'ser', 'items': ['Identity / profession  →  Yo soy profesora', 'Origin / nationality  →  Ella es de Colombia', 'Permanent traits  →  La casa es grande', 'Time / dates  →  Son las tres']}, 'right': {'heading': 'estar', 'items': ['Location  →  Estoy en el mercado', 'Temporary states  →  Él está cansado', 'Conditions / feelings  →  La puerta está abierta', 'Ongoing actions  →  Estoy hablando']}, 'footnote': "Rule of thumb: ser = essence, estar = state. If it'll change in an hour, use estar."},
        "drill_sentences": [
            {"en": "I am a teacher", "es": "Yo soy profesora", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "The coffee is hot", "es": "El café está caliente", "noun_id": "café", "type": "auditory", "glosses": {"coffee": "café", "hot": "caliente", "café": "coffee", "caliente": "hot"}},
            {"en": "She is from Colombia", "es": "Ella es de Colombia", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "He is tired", "es": "Él está cansado", "noun_id": None, "type": "auditory", "glosses": {"tired": "cansado", "cansado": "tired"}},
            {"en": "The house is big", "es": "La casa es grande", "noun_id": "casa", "type": "written", "glosses": {"big": "grande", "grande": "big", "house": "casa", "casa": "house"}},
            {"en": "The door is open", "es": "La puerta está abierta", "noun_id": "puerta", "type": "auditory", "glosses": {"door": "puerta", "open": "abierta", "puerta": "door", "abierta": "open"}},
            {"en": "We are at the market", "es": "Nosotros estamos en el mercado", "noun_id": "mercado", "type": "written", "glosses": {"market": "mercado", "mercado": "market"}},
            {"en": "The water is cold", "es": "El agua está fría", "noun_id": "agua", "type": "auditory", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "You all are students", "es": "Ustedes son estudiantes", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "The restaurant is closed", "es": "El restaurante está cerrado", "noun_id": "restaurante", "type": "auditory", "glosses": {"restaurant": "restaurante", "restaurante": "restaurant"}},
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
        "intro_chart": POR_PARA_INTRO,
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "rule_chart": {'kind': 'comparison', 'title': 'Por vs. Para', 'left': {'heading': 'por', 'items': ['Movement through  →  Voy por el parque', 'Cause / reason  →  Trabaja por dinero', "Means / 'by'  →  Viajo por avión", 'Duration  →  Estudié por dos horas', 'Exchange  →  Gracias por el libro']}, 'right': {'heading': 'para', 'items': ['Recipient  →  Esto es para ti', 'Purpose / goal  →  Estudiamos para aprender', 'Deadline  →  Lo necesito para mañana', 'Destination  →  Salgo para Bogotá']}, 'footnote': 'para = forward (purpose, recipient, deadline); por = around / through / because.'},
        "drill_sentences": [
            {"en": "I go by the park", "es": "Yo voy por el parque", "noun_id": "parque", "type": "written", "glosses": {"park": "parque", "parque": "park"}},
            {"en": "This is for you", "es": "Esto es para ti", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "She works for money", "es": "Ella trabaja por dinero", "noun_id": "dinero", "type": "written", "glosses": {"money": "dinero", "dinero": "money"}},
            {"en": "We study in order to learn", "es": "Nosotros estudiamos para aprender", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "He comes by the house", "es": "Él pasa por la casa", "noun_id": "casa", "type": "written", "glosses": {"house": "casa", "casa": "house"}},
            {"en": "The book is for the class", "es": "El libro es para la clase", "noun_id": "libro", "type": "auditory", "glosses": {"book": "libro", "class": "clase", "libro": "book", "clase": "class"}},
            {"en": "She travels by car", "es": "Ella viaja en carro", "noun_id": "carro", "type": "written", "glosses": {}},
            {"en": "I need it for tomorrow", "es": "Lo necesito para mañana", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "Thank you for the water", "es": "Gracias por el agua", "noun_id": "agua", "type": "written", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "We (f) work to live", "es": "Nosotras trabajamos para vivir", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": DEMONSTRATIVES_INTRO,
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "rule_chart": {'kind': 'table', 'title': 'Demonstratives — this / that / that-yonder', 'headers': ['Distance', 'Masc. sg', 'Fem. sg', 'Masc. pl', 'Fem. pl'], 'rows': [['near (this)', 'este', 'esta', 'estos', 'estas'], ['far from speaker (that)', 'ese', 'esa', 'esos', 'esas'], ['far from both (that yonder)', 'aquel', 'aquella', 'aquellos', 'aquellas']], 'footnote': "Match gender + number with the noun. Use 'aquel' for things visibly distant from both speaker and listener."},
        "drill_sentences": [
            {"en": "This house is big", "es": "Esta casa es grande", "noun_id": "casa", "type": "written", "glosses": {"house": "casa", "big": "grande", "casa": "house", "grande": "big"}},
            {"en": "That book is interesting", "es": "Ese libro es interesante", "noun_id": "libro", "type": "auditory", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "That city over there is beautiful", "es": "Aquella ciudad es bonita", "noun_id": "ciudad", "type": "written", "glosses": {"city": "ciudad", "beautiful": "bonita", "ciudad": "city", "bonita": "beautiful"}},
            {"en": "This coffee is hot", "es": "Este café está caliente", "noun_id": "café", "type": "auditory", "glosses": {"coffee": "café", "hot": "caliente", "café": "coffee", "caliente": "hot"}},
            {"en": "That door is open", "es": "Esa puerta está abierta", "noun_id": "puerta", "type": "written", "glosses": {"door": "puerta", "open": "abierta", "puerta": "door", "abierta": "open"}},
            {"en": "That park over there is nice", "es": "Aquel parque es bonito", "noun_id": "parque", "type": "auditory", "glosses": {"park": "parque", "nice": "bonito", "parque": "park", "bonito": "nice"}},
            {"en": "This water is cold", "es": "Esta agua está fría", "noun_id": "agua", "type": "written", "glosses": {"water": "agua", "agua": "water", "cold": "fría", "fría": "cold"}},
            {"en": "That car is expensive", "es": "Ese carro es caro", "noun_id": "carro", "type": "auditory", "glosses": {}},
            {"en": "That restaurant over there is good", "es": "Aquel restaurante es bueno", "noun_id": "restaurante", "type": "written", "glosses": {"good": "bueno", "bueno": "good"}},
            {"en": "This music is great", "es": "Esta música es genial", "noun_id": "música", "type": "auditory", "glosses": {"music": "música", "música": "music"}},
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
        "intro_chart": POSSESSIVE_PRONOUNS_INTRO,
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "rule_chart": {'kind': 'table', 'title': "Possessive pronouns — 'mine / yours / his …'", 'headers': ['Form', 'Used for'], 'rows': [['el mío / la mía', 'mine'], ['el tuyo / la tuya', 'yours (informal)'], ['el suyo / la suya', 'his / hers / yours (formal) / theirs'], ['el nuestro / la nuestra', 'ours']], 'footnote': 'Stand-alone — replaces the noun. Agree in gender and number with the thing owned. Plural forms add -s (los míos, las nuestras).'},
        "drill_sentences": [
            {"en": "The book is mine", "es": "El libro es mío", "noun_id": "libro", "type": "written", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "The house is yours", "es": "La casa es tuya", "noun_id": "casa", "type": "auditory", "glosses": {"house": "casa", "casa": "house"}},
            {"en": "The car is his", "es": "El carro es suyo", "noun_id": "carro", "type": "written", "glosses": {}},
            {"en": "The money is ours", "es": "El dinero es nuestro", "noun_id": "dinero", "type": "auditory", "glosses": {"money": "dinero", "dinero": "money"}},
            {"en": "The bag is mine", "es": "La bolsa es mía", "noun_id": None, "type": "written", "glosses": {"bag": "bolsa", "bolsa": "bag"}},
            {"en": "The coffee is yours", "es": "El café es tuyo", "noun_id": "café", "type": "auditory", "glosses": {"coffee": "café", "café": "coffee"}},
            {"en": "The dog is hers", "es": "El perro es suyo", "noun_id": "perro", "type": "written", "glosses": {"dog": "perro", "perro": "dog"}},
            {"en": "The house is ours", "es": "La casa es nuestra", "noun_id": "casa", "type": "auditory", "glosses": {"house": "casa", "casa": "house"}},
            {"en": "The water is mine", "es": "El agua es mía", "noun_id": "agua", "type": "written", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "The book is theirs", "es": "El libro es suyo", "noun_id": "libro", "type": "auditory", "glosses": {"book": "libro", "libro": "book"}},
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
        "intro_chart": IRREGULAR_PRESENT_II_INTRO,
        "rule_chart": IRREGULAR_PRESENT_II_RULE,
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
            {"en": "I make homework", "es": "Yo hago la tarea", "noun_id": None, "type": "written", "glosses": {"homework": "tarea", "tarea": "homework"}},
            {"en": "You put the book here", "es": "Tú pones el libro aquí", "noun_id": "libro", "type": "auditory", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "He leaves early", "es": "Él sale temprano", "noun_id": None, "type": "written", "glosses": {"early": "temprano", "temprano": "early"}},
            {"en": "She says the truth", "es": "Ella dice la verdad", "noun_id": None, "type": "auditory", "glosses": {"truth": "verdad", "verdad": "truth"}},
            {"en": "You make food", "es": "Usted hace comida", "noun_id": None, "type": "written", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "We put the table", "es": "Nosotros ponemos la mesa", "noun_id": None, "type": "auditory", "glosses": {"table": "mesa", "mesa": "table"}},
            {"en": "We (f) leave from home", "es": "Nosotras salimos de casa", "noun_id": "casa", "type": "written", "glosses": {"at home": "en casa", "en casa": "at home"}},
            {"en": "They say hi", "es": "Ellos dicen hola", "noun_id": None, "type": "auditory", "glosses": {"hi": "hola", "hola": "hi"}},
            {"en": "They (f) make exercise", "es": "Ellas hacen ejercicio", "noun_id": None, "type": "written", "glosses": {"exercise": "ejercicio", "ejercicio": "exercise"}},
            {"en": "You all put water", "es": "Ustedes ponen agua", "noun_id": None, "type": "auditory", "glosses": {"water": "agua", "agua": "water"}},
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
        "intro_chart": IRREGULAR_PRESENT_II_INTRO,
        "rule_chart": IRREGULAR_PRESENT_II_RULE,
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
            {"en": "I hear the noise", "es": "Yo oigo el ruido", "noun_id": None, "type": "written", "glosses": {"noise": "ruido", "ruido": "noise"}},
            {"en": "You fall today", "es": "Tú caes hoy", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "He brings water", "es": "Él trae agua", "noun_id": None, "type": "written", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "She is worth it", "es": "Ella vale la pena", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You hear a song", "es": "Usted oye una canción", "noun_id": None, "type": "written", "glosses": {"song": "canción", "canción": "song"}},
            {"en": "We fall asleep", "es": "Nosotros caemos dormido", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) bring the book", "es": "Nosotras traemos el libro", "noun_id": "libro", "type": "written", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "They be worth little", "es": "Ellos valen poco", "noun_id": None, "type": "auditory", "glosses": {"little": "poco", "poco": "little"}},
            {"en": "They (f) hear well", "es": "Ellas oyen bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "You all fall here", "es": "Ustedes caen aquí", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": IRREGULAR_PRESENT_II_INTRO,
        "rule_chart": IRREGULAR_PRESENT_II_RULE,
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
            {"en": "I make exercise", "es": "Yo hago ejercicio", "noun_id": None, "type": "written", "glosses": {"exercise": "ejercicio", "ejercicio": "exercise"}},
            {"en": "You put water", "es": "Tú pones agua", "noun_id": None, "type": "auditory", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "He leaves from work", "es": "Él sale del trabajo", "noun_id": "trabajo", "type": "written", "glosses": {"work": "trabajo", "trabajo": "work"}},
            {"en": "She says thanks", "es": "Ella dice gracias", "noun_id": None, "type": "auditory", "glosses": {"thanks": "gracias", "gracias": "thanks"}},
            {"en": "You make a plan", "es": "Usted hace un plan", "noun_id": "plan", "type": "written", "glosses": {"plan": "plan"}},
            {"en": "We put music", "es": "Nosotros ponemos música", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) leave together", "es": "Nosotras salimos juntos", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They say nothing", "es": "Ellos dicen nada", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "They (f) make the bed", "es": "Ellas hacen la cama", "noun_id": None, "type": "written", "glosses": {"bed": "cama", "cama": "bed"}},
            {"en": "You all put the coffee", "es": "Ustedes ponen el café", "noun_id": "café", "type": "auditory", "glosses": {"coffee": "café", "café": "coffee"}},
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
        "intro_chart": IRREGULAR_PRESENT_II_INTRO,
        "rule_chart": IRREGULAR_PRESENT_II_RULE,
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
            {"en": "I hear well", "es": "Yo oigo bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "You fall here", "es": "Tú caes aquí", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "He brings gifts", "es": "Él trae regalos", "noun_id": None, "type": "written", "glosses": {"gifts": "regalos", "regalos": "gifts"}},
            {"en": "She is worth gold", "es": "Ella vale oro", "noun_id": None, "type": "auditory", "glosses": {"gold": "oro", "oro": "gold"}},
            {"en": "You hear the radio", "es": "Usted oye la radio", "noun_id": None, "type": "written", "glosses": {"radio": "radio"}},
            {"en": "We fall fast", "es": "Nosotros caemos rápido", "noun_id": None, "type": "auditory", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "We (f) bring coffee", "es": "Nosotras traemos café", "noun_id": "café", "type": "written", "glosses": {}},
            {"en": "They be worth the wait", "es": "Ellos valen la espera", "noun_id": None, "type": "auditory", "glosses": {"wait": "espera", "espera": "wait"}},
            {"en": "They (f) hear music", "es": "Ellas oyen música", "noun_id": None, "type": "written", "glosses": {"music": "música", "música": "music"}},
            {"en": "You all fall on the street", "es": "Ustedes caen en la calle", "noun_id": "calle", "type": "auditory", "glosses": {"street": "calle", "calle": "street"}},
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
        "intro_chart": SPELLING_CHANGES_INTRO,
        "rule_chart": SPELLING_CHANGES_RULE,
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
            {"en": "I know the city", "es": "Yo conozco la ciudad", "noun_id": "ciudad", "type": "written", "glosses": {"city": "ciudad", "ciudad": "city"}},
            {"en": "You produce food", "es": "Tú produces comida", "noun_id": None, "type": "auditory", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "He builds a house", "es": "Él construye una casa", "noun_id": "casa", "type": "written", "glosses": {}},
            {"en": "She gets the book", "es": "Ella consigue el libro", "noun_id": "libro", "type": "auditory", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "You know Maria", "es": "Usted conoce a María", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "We produce coffee", "es": "Nosotros producimos café", "noun_id": "café", "type": "auditory", "glosses": {"coffee": "café", "café": "coffee"}},
            {"en": "We (f) build a bridge", "es": "Nosotras construimos un puente", "noun_id": None, "type": "written", "glosses": {"bridge": "puente", "puente": "bridge"}},
            {"en": "They get money", "es": "Ellos consiguen dinero", "noun_id": "dinero", "type": "auditory", "glosses": {"money": "dinero", "dinero": "money"}},
            {"en": "They (f) know the neighborhood", "es": "Ellas conocen el barrio", "noun_id": None, "type": "written", "glosses": {"neighborhood": "barrio", "barrio": "neighborhood"}},
            {"en": "You all produce work", "es": "Ustedes producen trabajo", "noun_id": "trabajo", "type": "auditory", "glosses": {"work": "trabajo", "trabajo": "work"}},
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
        "intro_chart": SPELLING_CHANGES_INTRO,
        "rule_chart": SPELLING_CHANGES_RULE,
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
            {"en": "I pick up the bags", "es": "Yo recojo las bolsas", "noun_id": None, "type": "written", "glosses": {"bags": "bolsas", "bolsas": "bags"}},
            {"en": "You direct the team", "es": "Tú diriges el equipo", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "He convinces the family", "es": "Él convence a la familia", "noun_id": "familia", "type": "written", "glosses": {"family": "familia", "familia": "family"}},
            {"en": "She continues working", "es": "Ella continúa trabajando", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You pick up the books", "es": "Usted recoge los libros", "noun_id": "libro", "type": "written", "glosses": {"books": "libros", "libros": "books"}},
            {"en": "We direct the project", "es": "Nosotros dirigimos el proyecto", "noun_id": None, "type": "auditory", "glosses": {"project": "proyecto", "proyecto": "project"}},
            {"en": "We (f) convince the neighbors", "es": "Nosotras convencemos a los vecinos", "noun_id": None, "type": "written", "glosses": {"neighbors": "vecinos", "vecinos": "neighbors"}},
            {"en": "They continue here", "es": "Ellos continúan aquí", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "They (f) pick up the trash", "es": "Ellas recogen la basura", "noun_id": None, "type": "written", "glosses": {"trash": "basura", "basura": "trash"}},
            {"en": "You all direct the office", "es": "Ustedes dirigen la oficina", "noun_id": None, "type": "auditory", "glosses": {"office": "oficina", "oficina": "office"}},
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
        "intro_chart": SPELLING_CHANGES_INTRO,
        "rule_chart": SPELLING_CHANGES_RULE,
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
            {"en": "I know the neighborhood", "es": "Yo conozco el barrio", "noun_id": None, "type": "written", "glosses": {"neighborhood": "barrio", "barrio": "neighborhood"}},
            {"en": "You produce work", "es": "Tú produces trabajo", "noun_id": "trabajo", "type": "auditory", "glosses": {"work": "trabajo", "trabajo": "work"}},
            {"en": "He builds the office", "es": "Él construye la oficina", "noun_id": None, "type": "written", "glosses": {"office": "oficina", "oficina": "office"}},
            {"en": "She gets work", "es": "Ella consigue trabajo", "noun_id": "trabajo", "type": "auditory", "glosses": {"work": "trabajo", "trabajo": "work"}},
            {"en": "You know the neighbors", "es": "Usted conoce a los vecinos", "noun_id": None, "type": "written", "glosses": {"neighbors": "vecinos", "vecinos": "neighbors"}},
            {"en": "We produce good wine", "es": "Nosotros producimos buen vino", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) build fast", "es": "Nosotras construimos rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "They get a ticket", "es": "Ellos consiguen una entrada", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "They (f) know a good place", "es": "Ellas conocen un buen lugar", "noun_id": None, "type": "written", "glosses": {"good": "buen", "place": "lugar", "buen": "good", "lugar": "place"}},
            {"en": "You all produce results", "es": "Ustedes producen resultados", "noun_id": None, "type": "auditory", "glosses": {"results": "resultados", "resultados": "results"}},
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
        "intro_chart": SPELLING_CHANGES_INTRO,
        "rule_chart": SPELLING_CHANGES_RULE,
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
            {"en": "I pick up the trash", "es": "Yo recojo la basura", "noun_id": None, "type": "written", "glosses": {"trash": "basura", "basura": "trash"}},
            {"en": "You direct the office", "es": "Tú diriges la oficina", "noun_id": None, "type": "auditory", "glosses": {"office": "oficina", "oficina": "office"}},
            {"en": "He convinces Maria", "es": "Él convence a María", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "She continues talking", "es": "Ella continúa hablando", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You pick up flowers", "es": "Usted recoge flores", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "We direct an orchestra", "es": "Nosotros dirigimos una orquesta", "noun_id": None, "type": "auditory", "glosses": {"orchestra": "orquesta", "orquesta": "orchestra"}},
            {"en": "We (f) convince everyone", "es": "Nosotras convencemos a todos", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They continue together", "es": "Ellos continúan juntos", "noun_id": None, "type": "auditory", "glosses": {"together": "juntos", "juntos": "together"}},
            {"en": "They (f) pick up the food", "es": "Ellas recogen la comida", "noun_id": None, "type": "written", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "You all direct the work", "es": "Ustedes dirigen el trabajo", "noun_id": "trabajo", "type": "auditory", "glosses": {"work": "trabajo", "trabajo": "work"}},
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
        "intro_chart": SABER_CONOCER_INTRO,
        "rule_chart": SABER_CONOCER_RULE,
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
        "intro_chart": PRESENT_O_UE_INTRO,
        "rule_chart": PRESENT_O_UE_RULE,
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
            {"en": "I move the table", "es": "Yo muevo la mesa", "noun_id": None, "type": "written", "glosses": {"table": "mesa", "mesa": "table"}},
            {"en": "You have lunch together", "es": "Tú almuerzas juntos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "He dies laughing", "es": "Él muere de risa", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "She can speak", "es": "Ella puede hablar", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You sleep well", "es": "Usted duerme bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "We return home", "es": "Nosotros volvemos a casa", "noun_id": "casa", "type": "auditory", "glosses": {"at home": "en casa", "en casa": "at home"}},
            {"en": "We (f) move the chair", "es": "Nosotras movemos la silla", "noun_id": None, "type": "written", "glosses": {"chair": "silla", "silla": "chair"}},
            {"en": "They have lunch here", "es": "Ellos almuerzan aquí", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "They (f) die of hunger", "es": "Ellas mueren de hambre", "noun_id": None, "type": "written", "glosses": {"hunger": "hambre", "hambre": "hunger"}},
            {"en": "You all can come", "es": "Ustedes pueden venir", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": PRESENT_O_UE_INTRO,
        "rule_chart": PRESENT_O_UE_RULE,
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
            {"en": "I move the chair", "es": "Yo muevo la silla", "noun_id": None, "type": "written", "glosses": {"chair": "silla", "silla": "chair"}},
            {"en": "You have lunch here", "es": "Tú almuerzas aquí", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "He dies of hunger", "es": "Él muere de hambre", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "She can come", "es": "Ella puede venir", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You sleep eight hours", "es": "Usted duerme ocho horas", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "We return early", "es": "Nosotros volvemos temprano", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) move the car", "es": "Nosotras movemos el carro", "noun_id": "carro", "type": "written", "glosses": {"car": "carro", "carro": "car"}},
            {"en": "They have lunch early", "es": "Ellos almuerzan temprano", "noun_id": None, "type": "auditory", "glosses": {"early": "temprano", "temprano": "early"}},
            {"en": "They (f) die young", "es": "Ellas mueren joven", "noun_id": None, "type": "written", "glosses": {"young": "joven", "joven": "young"}},
            {"en": "You all can help", "es": "Ustedes pueden ayudar", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": PRESENT_O_UE_INTRO,
        "rule_chart": PRESENT_O_UE_RULE,
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
            {"en": "I move the car", "es": "Yo muevo el carro", "noun_id": "carro", "type": "written", "glosses": {"car": "carro", "carro": "car"}},
            {"en": "You have lunch early", "es": "Tú almuerzas temprano", "noun_id": None, "type": "auditory", "glosses": {"early": "temprano", "temprano": "early"}},
            {"en": "He dies young", "es": "Él muere joven", "noun_id": None, "type": "written", "glosses": {"young": "joven", "joven": "young"}},
            {"en": "She can help", "es": "Ella puede ayudar", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You sleep a lot", "es": "Usted duerme mucho", "noun_id": None, "type": "written", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "We return tomorrow", "es": "Nosotros volvemos mañana", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) move the boxes", "es": "Nosotras movemos las cajas", "noun_id": None, "type": "written", "glosses": {"boxes": "cajas", "cajas": "boxes"}},
            {"en": "They have lunch fast", "es": "Ellos almuerzan rápido", "noun_id": None, "type": "auditory", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "They (f) die of thirst", "es": "Ellas mueren de sed", "noun_id": None, "type": "written", "glosses": {"thirst": "sed", "sed": "thirst"}},
            {"en": "You all can go", "es": "Ustedes pueden ir", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": PRESENT_E_IE_INTRO,
        "rule_chart": PRESENT_E_IE_RULE,
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
            {"en": "I close the door", "es": "Yo cierro la puerta", "noun_id": "puerta", "type": "written", "glosses": {}},
            {"en": "You understand Spanish", "es": "Tú entiendes español", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "He thinks of you", "es": "Él piensa en ti", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "She wants coffee", "es": "Ella quiere café", "noun_id": "café", "type": "auditory", "glosses": {"coffee": "café", "café": "coffee"}},
            {"en": "You prefer coffee", "es": "Usted prefiere café", "noun_id": "café", "type": "written", "glosses": {"coffee": "café", "café": "coffee"}},
            {"en": "We start early", "es": "Nosotros empezamos temprano", "noun_id": None, "type": "auditory", "glosses": {"early": "temprano", "temprano": "early"}},
            {"en": "We (f) close the window", "es": "Nosotras cerramos la ventana", "noun_id": "ventana", "type": "written", "glosses": {"window": "ventana", "ventana": "window"}},
            {"en": "They understand the question", "es": "Ellos entienden la pregunta", "noun_id": None, "type": "auditory", "glosses": {"question": "pregunta", "pregunta": "question"}},
            {"en": "They (f) think a lot", "es": "Ellas piensan mucho", "noun_id": None, "type": "written", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "You all want water", "es": "Ustedes quieren agua", "noun_id": None, "type": "auditory", "glosses": {"water": "agua", "agua": "water"}},
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
        "intro_chart": PRESENT_E_IE_INTRO,
        "rule_chart": PRESENT_E_IE_RULE,
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
            {"en": "I close the window", "es": "Yo cierro la ventana", "noun_id": "ventana", "type": "written", "glosses": {}},
            {"en": "You understand the question", "es": "Tú entiendes la pregunta", "noun_id": None, "type": "auditory", "glosses": {"question": "pregunta", "pregunta": "question"}},
            {"en": "He thinks a lot", "es": "Él piensa mucho", "noun_id": None, "type": "written", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "She wants water", "es": "Ella quiere agua", "noun_id": None, "type": "auditory", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "You prefer the park", "es": "Usted prefiere el parque", "noun_id": "parque", "type": "written", "glosses": {"park": "parque", "parque": "park"}},
            {"en": "We start now", "es": "Nosotros empezamos ahora", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) close the store", "es": "Nosotras cerramos la tienda", "noun_id": "tienda", "type": "written", "glosses": {"store": "tienda", "tienda": "store"}},
            {"en": "They understand the plan", "es": "Ellos entienden el plan", "noun_id": "plan", "type": "auditory", "glosses": {}},
            {"en": "They (f) think fast", "es": "Ellas piensan rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "You all want to help", "es": "Ustedes quieren ayudar", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": PRESENT_E_IE_INTRO,
        "rule_chart": PRESENT_E_IE_RULE,
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
            {"en": "I close the store", "es": "Yo cierro la tienda", "noun_id": "tienda", "type": "written", "glosses": {}},
            {"en": "You understand the plan", "es": "Tú entiendes el plan", "noun_id": "plan", "type": "auditory", "glosses": {}},
            {"en": "He thinks fast", "es": "Él piensa rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "She wants to help", "es": "Ella quiere ayudar", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You prefer water", "es": "Usted prefiere agua", "noun_id": None, "type": "written", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "We start work", "es": "Nosotros empezamos el trabajo", "noun_id": "trabajo", "type": "auditory", "glosses": {"work": "trabajo", "trabajo": "work"}},
            {"en": "We (f) close the book", "es": "Nosotras cerramos el libro", "noun_id": "libro", "type": "written", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "They understand well", "es": "Ellos entienden bien", "noun_id": None, "type": "auditory", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "They (f) think about the plan", "es": "Ellas piensan en el plan", "noun_id": "plan", "type": "written", "glosses": {"plan": "plan"}},
            {"en": "You all want to go", "es": "Ustedes quieren ir", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": PRESENT_E_I_INTRO,
        "rule_chart": PRESENT_E_I_RULE,
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
            {"en": "I ask for coffee", "es": "Yo pido café", "noun_id": "café", "type": "written", "glosses": {"coffee": "café", "café": "coffee"}},
            {"en": "You repeat the word", "es": "Tú repites la palabra", "noun_id": None, "type": "auditory", "glosses": {"word": "palabra", "palabra": "word"}},
            {"en": "He follows the plan", "es": "Él sigue el plan", "noun_id": "plan", "type": "written", "glosses": {"plan": "plan"}},
            {"en": "She serves the food", "es": "Ella sirve la comida", "noun_id": None, "type": "auditory", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "You dress the child", "es": "Usted viste al niño", "noun_id": None, "type": "written", "glosses": {"child": "niño", "niño": "child"}},
            {"en": "We choose the book", "es": "Nosotros elegimos el libro", "noun_id": "libro", "type": "auditory", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "We (f) ask for water", "es": "Nosotras pedimos agua", "noun_id": None, "type": "written", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "They repeat the sentence", "es": "Ellos repiten la frase", "noun_id": None, "type": "auditory", "glosses": {"sentence": "frase", "frase": "sentence"}},
            {"en": "They (f) follow working", "es": "Ellas siguen trabajando", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You all serve the coffee", "es": "Ustedes sirven el café", "noun_id": "café", "type": "auditory", "glosses": {"coffee": "café", "café": "coffee"}},
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
        "intro_chart": PRESENT_E_I_INTRO,
        "rule_chart": PRESENT_E_I_RULE,
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
            {"en": "I ask for water", "es": "Yo pido agua", "noun_id": None, "type": "written", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "You repeat the sentence", "es": "Tú repites la frase", "noun_id": None, "type": "auditory", "glosses": {"sentence": "frase", "frase": "sentence"}},
            {"en": "He follows working", "es": "Él sigue trabajando", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "She serves the coffee", "es": "Ella sirve el café", "noun_id": "café", "type": "auditory", "glosses": {"coffee": "café", "café": "coffee"}},
            {"en": "You dress well", "es": "Usted viste bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "We choose the city", "es": "Nosotros elegimos la ciudad", "noun_id": "ciudad", "type": "auditory", "glosses": {}},
            {"en": "We (f) ask for help", "es": "Nosotras pedimos ayuda", "noun_id": None, "type": "written", "glosses": {"help": "ayuda", "ayuda": "help"}},
            {"en": "They repeat a song", "es": "Ellos repiten una canción", "noun_id": None, "type": "auditory", "glosses": {"song": "canción", "canción": "song"}},
            {"en": "They (f) follow here", "es": "Ellas siguen aquí", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You all serve water", "es": "Ustedes sirven agua", "noun_id": None, "type": "auditory", "glosses": {"water": "agua", "agua": "water"}},
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
        "intro_chart": PRESENT_E_I_INTRO,
        "rule_chart": PRESENT_E_I_RULE,
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
            {"en": "I ask for help", "es": "Yo pido ayuda", "noun_id": None, "type": "written", "glosses": {"help": "ayuda", "ayuda": "help"}},
            {"en": "You repeat a song", "es": "Tú repites una canción", "noun_id": None, "type": "auditory", "glosses": {"song": "canción", "canción": "song"}},
            {"en": "He follows here", "es": "Él sigue aquí", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "She serves water", "es": "Ella sirve agua", "noun_id": None, "type": "auditory", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "You dress fast", "es": "Usted viste rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "We choose the restaurant", "es": "Nosotros elegimos el restaurante", "noun_id": None, "type": "auditory", "glosses": {"restaurant": "restaurante", "restaurante": "restaurant"}},
            {"en": "We (f) ask for the bill", "es": "Nosotras pedimos la cuenta", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They repeat well", "es": "Ellos repiten bien", "noun_id": None, "type": "auditory", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "They (f) follow the recipe", "es": "Ellas siguen la receta", "noun_id": None, "type": "written", "glosses": {"recipe": "receta", "receta": "recipe"}},
            {"en": "You all serve the customers", "es": "Ustedes sirven a los clientes", "noun_id": None, "type": "auditory", "glosses": {"customers": "clientes", "clientes": "customers"}},
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
        "intro_chart": IR_A_INF_INTRO,
        "rule_chart": IR_A_INF_RULE,
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
            {"en": "I speak Spanish", "es": "Yo voy a hablar español", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You eat bread", "es": "Tú vas a comer pan", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "He sleeps well", "es": "Él va a dormir bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "She lives here", "es": "Ella va a vivir aquí", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You write a letter", "es": "Usted va a escribir una carta", "noun_id": "carta", "type": "written", "glosses": {"letter": "carta", "carta": "letter"}},
            {"en": "We study Spanish", "es": "Nosotros vamos a estudiar español", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) speak English", "es": "Nosotras vamos a hablar inglés", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They eat food", "es": "Ellos van a comer comida", "noun_id": None, "type": "auditory", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "They (f) sleep eight hours", "es": "Ellas van a dormir ocho horas", "noun_id": None, "type": "written", "glosses": {"hours": "horas", "horas": "hours"}},
            {"en": "You all live nearby", "es": "Ustedes van a vivir cerca", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": IR_A_INF_INTRO,
        "rule_chart": IR_A_INF_RULE,
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
            {"en": "I speak English", "es": "Yo voy a hablar inglés", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You eat food", "es": "Tú vas a comer comida", "noun_id": None, "type": "auditory", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "He sleeps eight hours", "es": "Él va a dormir ocho horas", "noun_id": None, "type": "written", "glosses": {"hours": "horas", "horas": "hours"}},
            {"en": "She lives nearby", "es": "Ella va a vivir cerca", "noun_id": None, "type": "auditory", "glosses": {"nearby": "cerca", "cerca": "nearby"}},
            {"en": "You write a book", "es": "Usted va a escribir un libro", "noun_id": "libro", "type": "written", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "We study a lot", "es": "Nosotros vamos a estudiar mucho", "noun_id": None, "type": "auditory", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "We (f) speak well", "es": "Nosotras vamos a hablar bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "They eat fruit", "es": "Ellos van a comer fruta", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "They (f) sleep a lot", "es": "Ellas van a dormir mucho", "noun_id": None, "type": "written", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "You all live together", "es": "Ustedes van a vivir juntos", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": IR_A_INF_INTRO,
        "rule_chart": IR_A_INF_RULE,
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
            {"en": "I speak well", "es": "Yo voy a hablar bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "You eat fruit", "es": "Tú vas a comer fruta", "noun_id": None, "type": "auditory", "glosses": {"fruit": "fruta", "fruta": "fruit"}},
            {"en": "He sleeps a lot", "es": "Él va a dormir mucho", "noun_id": None, "type": "written", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "She lives together", "es": "Ella va a vivir juntos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You write messages", "es": "Usted va a escribir mensajes", "noun_id": None, "type": "written", "glosses": {"messages": "mensajes", "mensajes": "messages"}},
            {"en": "We study at home", "es": "Nosotros vamos a estudiar en casa", "noun_id": "casa", "type": "auditory", "glosses": {}},
            {"en": "We (f) speak fast", "es": "Nosotras vamos a hablar rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "They eat meat", "es": "Ellos van a comer carne", "noun_id": None, "type": "auditory", "glosses": {"meat": "carne", "carne": "meat"}},
            {"en": "They (f) sleep here", "es": "Ellas van a dormir aquí", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You all live alone", "es": "Ustedes van a vivir solo", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": GUSTAR_INTRO,
        "rule_chart": GUSTAR_RULE,
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
            {"en": "I like the coffee", "es": "Me gusta el café", "noun_id": "café", "type": "written", "glosses": {"coffee": "café", "café": "coffee"}},
            {"en": "You like the music", "es": "Te gusta la música", "noun_id": None, "type": "auditory", "glosses": {"music": "música", "música": "music"}},
            {"en": "She likes the book", "es": "Le gusta el libro", "noun_id": "libro", "type": "written", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "He likes the water", "es": "Le gusta el agua", "noun_id": "agua", "type": "auditory", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "You (formal) like the food", "es": "Le gusta la comida", "noun_id": "comida", "type": "written", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "We like the plan", "es": "Nos gusta el plan", "noun_id": None, "type": "auditory", "glosses": {"plan": "plan"}},
            {"en": "They like the park", "es": "Les gusta el parque", "noun_id": "parque", "type": "written", "glosses": {"park": "parque", "parque": "park"}},
            {"en": "I like the dog", "es": "Me gusta el perro", "noun_id": "perro", "type": "auditory", "glosses": {}},
            {"en": "You like the city", "es": "Te gusta la ciudad", "noun_id": "ciudad", "type": "written", "glosses": {"city": "ciudad", "ciudad": "city"}},
            {"en": "She likes the house", "es": "Le gusta la casa", "noun_id": "casa", "type": "auditory", "glosses": {}},
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
        "phase_2_config": {
            "description": "5 pronoun+gusta+singular noun combos",
            "targets": [
                {"phrase": "me gusta"},
                {"phrase": "te gusta"},
                {"phrase": "le gusta"},
                {"phrase": "nos gusta"},
                {"phrase": "les gusta"},
            ],
            "pattern": "pronoun_gusta_singular",
        },
    },
    "grammar_gustar_2": {
        "title": "Gustar Part 2",
        "grammar_level": 10.3,
        "word_workload": ["gustan"],
        "video_embed_id": "WjOxPPu1uQo",
        "drill_type": "gustar",
        "tense": "gustar",
        "intro_chart": GUSTAR_INTRO,
        "rule_chart": GUSTAR_RULE,
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
            {"en": "I like the cats", "es": "Me gustan los gatos", "noun_id": "gato", "type": "written", "glosses": {}},
            {"en": "You like the books", "es": "Te gustan los libros", "noun_id": "libro", "type": "auditory", "glosses": {"books": "libros", "libros": "books"}},
            {"en": "She likes the dogs", "es": "Le gustan los perros", "noun_id": "perro", "type": "written", "glosses": {"dogs": "perros", "perros": "dogs"}},
            {"en": "He likes the cars", "es": "Le gustan los carros", "noun_id": "carro", "type": "auditory", "glosses": {"cars": "carros", "carros": "cars"}},
            {"en": "We like the movies", "es": "Nos gustan las películas", "noun_id": None, "type": "written", "glosses": {"movies": "películas", "películas": "movies"}},
            {"en": "They like the parks", "es": "Les gustan los parques", "noun_id": "parque", "type": "auditory", "glosses": {"parks": "parques", "parques": "parks"}},
            {"en": "You all like the beaches", "es": "Les gustan las playas", "noun_id": "playa", "type": "written", "glosses": {"beaches": "playas", "playas": "beaches"}},
            {"en": "I like the cities", "es": "Me gustan las ciudades", "noun_id": "ciudad", "type": "auditory", "glosses": {"cities": "ciudades", "ciudades": "cities"}},
            {"en": "You like the colors", "es": "Te gustan los colores", "noun_id": "color", "type": "written", "glosses": {"colors": "colores", "colores": "colors"}},
            {"en": "She likes the houses", "es": "Le gustan las casas", "noun_id": "casa", "type": "auditory", "glosses": {"houses": "casas", "casas": "houses"}},
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
        "phase_2_config": {
            "description": "5 pronoun+gustan+plural noun combos",
            "targets": [
                {"phrase": "me gustan"},
                {"phrase": "te gustan"},
                {"phrase": "le gustan"},
                {"phrase": "nos gustan"},
                {"phrase": "les gustan"},
            ],
            "pattern": "pronoun_gustan_plural",
        },
    },
    "grammar_gustar_3": {
        "title": "Gustar Part 3",
        "grammar_level": 10.6,
        "word_workload": ["gusta", "gustan"],
        "video_embed_id": "lIAdqI5fpun",
        "drill_type": "gustar_prefix",
        "tense": "gustar",
        "intro_chart": GUSTAR_INTRO,
        "rule_chart": GUSTAR_RULE,
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
            {"en": "I like the coffee (emphatic)", "es": "A mí me gusta el café", "noun_id": "café", "type": "written", "glosses": {"coffee": "café", "café": "coffee"}},
            {"en": "You like the music (emphatic)", "es": "A ti te gusta la música", "noun_id": None, "type": "auditory", "glosses": {"music": "música", "música": "music"}},
            {"en": "He likes the book (emphatic)", "es": "A él le gusta el libro", "noun_id": "libro", "type": "written", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "She likes the water (emphatic)", "es": "A ella le gusta el agua", "noun_id": "agua", "type": "auditory", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "You (formal) like the food (emphatic)", "es": "A usted le gusta la comida", "noun_id": "comida", "type": "written", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "We like the park (emphatic)", "es": "A nosotros nos gusta el parque", "noun_id": "parque", "type": "auditory", "glosses": {}},
            {"en": "They like the dog (emphatic)", "es": "A ellos les gusta el perro", "noun_id": "perro", "type": "written", "glosses": {"dog": "perro", "perro": "dog"}},
            {"en": "You all like the city (emphatic)", "es": "A ustedes les gusta la ciudad", "noun_id": "ciudad", "type": "auditory", "glosses": {"city": "ciudad", "ciudad": "city"}},
            {"en": "I like the house (emphatic)", "es": "A mí me gusta la casa", "noun_id": "casa", "type": "written", "glosses": {"house": "casa", "casa": "house"}},
            {"en": "She likes the car (emphatic)", "es": "A ella le gusta el carro", "noun_id": "carro", "type": "auditory", "glosses": {}},
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
        "phase_2_config": {
            "description": "1 emphatic 'a + pronoun' combo per pronoun type (10 total)",
            "targets": [
                {"phrase": "a mí me gusta"},
                {"phrase": "a ti te gusta"},
                {"phrase": "a él le gusta"},
                {"phrase": "a ella le gusta"},
                {"phrase": "a usted le gusta"},
                {"phrase": "a nosotros nos gusta"},
                {"phrase": "a nosotras nos gusta"},
                {"phrase": "a ellos les gusta"},
                {"phrase": "a ellas les gusta"},
                {"phrase": "a ustedes les gusta"},
            ],
            "pattern": "a_prefix",
        },
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
        "intro_chart": IMPERATIVES_INTRO,
        "rule_chart": IMPERATIVES_RULE,
        "drill_config": {"answers": {
            "hablar": {"tú": "habla", "usted": "hable", "nosotros": "hablemos", "vosotros": "hablad", "ustedes": "hablen"},
            "comer": {"tú": "come", "usted": "coma", "nosotros": "comamos", "vosotros": "comed", "ustedes": "coman"},
            "vivir": {"tú": "vive", "usted": "viva", "nosotros": "vivamos", "vosotros": "vivid", "ustedes": "vivan"},
        }},
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "Speak slowly (tú)", "es": "Habla despacio", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "Speak here (usted)", "es": "Hable aquí", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "Let's speak now (nosotros)", "es": "Hablemos ahora", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "Eat the bread (tú)", "es": "Come el pan", "noun_id": "pan", "type": "auditory", "glosses": {"bread": "pan", "pan": "bread"}},
            {"en": "Eat the food (usted)", "es": "Coma la comida", "noun_id": "comida", "type": "written", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "Let's eat together (nosotros)", "es": "Comamos juntos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You all eat now (ustedes)", "es": "Coman ahora", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "Live well (tú)", "es": "Vive bien", "noun_id": None, "type": "auditory", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "Live here (usted)", "es": "Viva aquí", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "Let's live well (nosotros)", "es": "Vivamos bien", "noun_id": None, "type": "auditory", "glosses": {"well": "bien", "bien": "well"}},
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
        "intro_chart": IMPERATIVES_INTRO,
        "rule_chart": IMPERATIVES_RULE,
        "drill_config": {"answers": {
            "ir": {"tú": "ve", "usted": "vaya", "nosotros": "vamos", "ustedes": "vayan"},
            "ser": {"tú": "sé", "usted": "sea", "nosotros": "seamos", "ustedes": "sean"},
            "tener": {"tú": "ten", "usted": "tenga", "nosotros": "tengamos", "ustedes": "tengan"},
        }},
        "phases": {"0a": False, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "Go now (tú)", "es": "Ve ahora", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "Go to the park (usted)", "es": "Vaya al parque", "noun_id": "parque", "type": "auditory", "glosses": {}},
            {"en": "Let's go (nosotros)", "es": "Vamos", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You all go now (ustedes)", "es": "Vayan ahora", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "Be calm (tú)", "es": "Sé tranquilo", "noun_id": None, "type": "written", "glosses": {"calm": "tranquilo", "tranquilo": "calm"}},
            {"en": "Be here (usted)", "es": "Sea aquí", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "Let's be calm (nosotros)", "es": "Seamos tranquilos", "noun_id": None, "type": "written", "glosses": {"calm": "tranquilos", "tranquilos": "calm"}},
            {"en": "Have the book (tú)", "es": "Ten el libro", "noun_id": "libro", "type": "auditory", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "Have patience (usted)", "es": "Tenga paciencia", "noun_id": None, "type": "written", "glosses": {"patience": "paciencia", "paciencia": "patience"}},
            {"en": "You all have the plan (ustedes)", "es": "Tengan el plan", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": PRETERITE_REGULAR_INTRO,
        "rule_chart": PRETERITE_REGULAR_RULE,
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
            {"en": "I spoke Spanish", "es": "Yo hablé español", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You found the book", "es": "Tú encontraste el libro", "noun_id": "libro", "type": "auditory", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "He ate bread", "es": "Él comió pan", "noun_id": None, "type": "written", "glosses": {"bread": "pan", "pan": "bread"}},
            {"en": "She united the family", "es": "Ella unió la familia", "noun_id": "familia", "type": "auditory", "glosses": {"family": "familia", "familia": "family"}},
            {"en": "You drank water", "es": "Usted bebió agua", "noun_id": None, "type": "written", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "We left early", "es": "Nosotros salimos temprano", "noun_id": None, "type": "auditory", "glosses": {"early": "temprano", "temprano": "early"}},
            {"en": "We (f) spoke English", "es": "Nosotras hablamos inglés", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They found work", "es": "Ellos encontraron trabajo", "noun_id": "trabajo", "type": "auditory", "glosses": {}},
            {"en": "They (f) ate food", "es": "Ellas comieron comida", "noun_id": None, "type": "written", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "You all united the team", "es": "Ustedes unieron al equipo", "noun_id": None, "type": "auditory", "glosses": {"team": "equipo", "equipo": "team"}},
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
        "intro_chart": PRETERITE_REGULAR_INTRO,
        "rule_chart": PRETERITE_REGULAR_RULE,
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
            {"en": "I spoke English", "es": "Yo hablé inglés", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You found work", "es": "Tú encontraste trabajo", "noun_id": "trabajo", "type": "auditory", "glosses": {"work": "trabajo", "trabajo": "work"}},
            {"en": "He ate food", "es": "Él comió comida", "noun_id": None, "type": "written", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "She united the team", "es": "Ella unió al equipo", "noun_id": None, "type": "auditory", "glosses": {"team": "equipo", "equipo": "team"}},
            {"en": "You drank coffee", "es": "Usted bebió café", "noun_id": "café", "type": "written", "glosses": {"coffee": "café", "café": "coffee"}},
            {"en": "We left from home", "es": "Nosotros salimos de casa", "noun_id": "casa", "type": "auditory", "glosses": {"at home": "en casa", "en casa": "at home"}},
            {"en": "We (f) spoke well", "es": "Nosotras hablamos bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "They found Maria", "es": "Ellos encontraron a María", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "They (f) ate fruit", "es": "Ellas comieron fruta", "noun_id": None, "type": "written", "glosses": {"fruit": "fruta", "fruta": "fruit"}},
            {"en": "You all united everyone", "es": "Ustedes unieron a todos", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": PRETERITE_REGULAR_INTRO,
        "rule_chart": PRETERITE_REGULAR_RULE,
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
            {"en": "I spoke well", "es": "Yo hablé bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "You found Maria", "es": "Tú encontraste a María", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "He ate fruit", "es": "Él comió fruta", "noun_id": None, "type": "written", "glosses": {"fruit": "fruta", "fruta": "fruit"}},
            {"en": "She united everyone", "es": "Ella unió a todos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You drank juice", "es": "Usted bebió jugo", "noun_id": None, "type": "written", "glosses": {"juice": "jugo", "jugo": "juice"}},
            {"en": "We left from work", "es": "Nosotros salimos del trabajo", "noun_id": "trabajo", "type": "auditory", "glosses": {"work": "trabajo", "trabajo": "work"}},
            {"en": "We (f) spoke fast", "es": "Nosotras hablamos rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "They found the answer", "es": "Ellos encontraron la respuesta", "noun_id": None, "type": "auditory", "glosses": {"answer": "respuesta", "respuesta": "answer"}},
            {"en": "They (f) ate meat", "es": "Ellas comieron carne", "noun_id": None, "type": "written", "glosses": {"meat": "carne", "carne": "meat"}},
            {"en": "You all united two houses", "es": "Ustedes unieron dos casas", "noun_id": "casa", "type": "auditory", "glosses": {"houses": "casas", "two": "dos", "casas": "houses", "dos": "two"}},
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
        "intro_chart": PRETERITE_IRREGULAR_INTRO,
        "rule_chart": PRETERITE_IRREGULAR_RULE,
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
            {"en": "I was tall", "es": "Yo fui alto", "noun_id": None, "type": "written", "glosses": {"tall": "alto", "alto": "tall"}},
            {"en": "You went to the market", "es": "Tú fuiste al mercado", "noun_id": "mercado", "type": "auditory", "glosses": {"market": "mercado", "mercado": "market"}},
            {"en": "He gave the book", "es": "Él dio el libro", "noun_id": "libro", "type": "written", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "She saw the movie", "es": "Ella vio la película", "noun_id": None, "type": "auditory", "glosses": {"movie": "película", "película": "movie"}},
            {"en": "You made homework", "es": "Usted hizo la tarea", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "We said the truth", "es": "Nosotros dijimos la verdad", "noun_id": None, "type": "auditory", "glosses": {"truth": "verdad", "verdad": "truth"}},
            {"en": "We (f) were professional", "es": "Nosotras fuimos profesional", "noun_id": None, "type": "written", "glosses": {"professional": "profesional", "profesional": "professional"}},
            {"en": "They went home", "es": "Ellos fueron a casa", "noun_id": "casa", "type": "auditory", "glosses": {}},
            {"en": "They (f) gave money", "es": "Ellas dieron dinero", "noun_id": "dinero", "type": "written", "glosses": {}},
            {"en": "You all saw the family", "es": "Ustedes vieron a la familia", "noun_id": "familia", "type": "auditory", "glosses": {"family": "familia", "familia": "family"}},
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
        "intro_chart": PRETERITE_IRREGULAR_INTRO,
        "rule_chart": PRETERITE_IRREGULAR_RULE,
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
            {"en": "I brought water", "es": "Yo traje agua", "noun_id": None, "type": "written", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "You slept eight hours", "es": "Tú dormiste ocho horas", "noun_id": None, "type": "auditory", "glosses": {"hours": "horas", "horas": "hours"}},
            {"en": "He died of hunger", "es": "Él murió de hambre", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "She was professional", "es": "Ella fue profesional", "noun_id": None, "type": "auditory", "glosses": {"professional": "profesional", "profesional": "professional"}},
            {"en": "You made food", "es": "Usted hizo comida", "noun_id": None, "type": "written", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "We brought the book", "es": "Nosotros trajimos el libro", "noun_id": "libro", "type": "auditory", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "We (f) slept a lot", "es": "Nosotras dormimos mucho", "noun_id": None, "type": "written", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "They died young", "es": "Ellos murieron joven", "noun_id": None, "type": "auditory", "glosses": {"young": "joven", "joven": "young"}},
            {"en": "They (f) were important", "es": "Ellas fueron importante", "noun_id": None, "type": "written", "glosses": {"important": "importante", "importante": "important"}},
            {"en": "You all made exercise", "es": "Ustedes hicieron ejercicio", "noun_id": None, "type": "auditory", "glosses": {"exercise": "ejercicio", "ejercicio": "exercise"}},
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
        "intro_chart": PRETERITE_IRREGULAR_INTRO,
        "rule_chart": PRETERITE_IRREGULAR_RULE,
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
            {"en": "I was important", "es": "Yo fui importante", "noun_id": None, "type": "written", "glosses": {"important": "importante", "importante": "important"}},
            {"en": "You went to the park", "es": "Tú fuiste al parque", "noun_id": "parque", "type": "auditory", "glosses": {}},
            {"en": "He gave water", "es": "Él dio agua", "noun_id": None, "type": "written", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "She saw a photo", "es": "Ella vio una foto", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You made exercise", "es": "Usted hizo ejercicio", "noun_id": None, "type": "written", "glosses": {"exercise": "ejercicio", "ejercicio": "exercise"}},
            {"en": "We said thanks", "es": "Nosotros dijimos gracias", "noun_id": None, "type": "auditory", "glosses": {"thanks": "gracias", "gracias": "thanks"}},
            {"en": "We (f) were likeable", "es": "Nosotras fuimos simpático", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They went to the store", "es": "Ellos fueron a la tienda", "noun_id": "tienda", "type": "auditory", "glosses": {}},
            {"en": "They (f) gave an answer", "es": "Ellas dieron una respuesta", "noun_id": None, "type": "written", "glosses": {"answer": "respuesta", "respuesta": "answer"}},
            {"en": "You all saw well", "es": "Ustedes vieron bien", "noun_id": None, "type": "auditory", "glosses": {"well": "bien", "bien": "well"}},
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
        "intro_chart": PRETERITE_IRREGULAR_INTRO,
        "rule_chart": PRETERITE_IRREGULAR_RULE,
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
            {"en": "I brought gifts", "es": "Yo traje regalos", "noun_id": None, "type": "written", "glosses": {"gifts": "regalos", "regalos": "gifts"}},
            {"en": "You slept here", "es": "Tú dormiste aquí", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "He died of thirst", "es": "Él murió de sed", "noun_id": None, "type": "written", "glosses": {"thirst": "sed", "sed": "thirst"}},
            {"en": "She went to the store", "es": "Ella fue a la tienda", "noun_id": "tienda", "type": "auditory", "glosses": {}},
            {"en": "You said nothing", "es": "Usted dijo nada", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "We brought coffee", "es": "Nosotros trajimos café", "noun_id": "café", "type": "auditory", "glosses": {"coffee": "café", "café": "coffee"}},
            {"en": "We (f) slept early", "es": "Nosotras dormimos temprano", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They died of exhaustion", "es": "Ellos murieron de cansancio", "noun_id": None, "type": "auditory", "glosses": {"exhaustion": "cansancio", "cansancio": "exhaustion"}},
            {"en": "They (f) went to work", "es": "Ellas fueron al trabajo", "noun_id": "trabajo", "type": "written", "glosses": {"work": "trabajo", "trabajo": "work"}},
            {"en": "You all said a story", "es": "Ustedes dijeron una historia", "noun_id": None, "type": "auditory", "glosses": {"story": "historia", "historia": "story"}},
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
        "intro_chart": GERUND_INTRO,
        "rule_chart": GERUND_RULE,
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
            {"en": "I speak Spanish", "es": "Yo estoy hablando español", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You walk together", "es": "Tú estás caminando juntos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "He chats together", "es": "Él está charlando juntos", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "She eats bread", "es": "Ella está comiendo pan", "noun_id": None, "type": "auditory", "glosses": {"bread": "pan", "pan": "bread"}},
            {"en": "You speak English", "es": "Usted está hablando inglés", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "We walk through the park", "es": "Nosotros estamos caminando por el parque", "noun_id": "parque", "type": "auditory", "glosses": {"park": "parque", "parque": "park"}},
            {"en": "We (f) chat here", "es": "Nosotras estamos charlando aquí", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They eat food", "es": "Ellos están comiendo comida", "noun_id": None, "type": "auditory", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "They (f) speak well", "es": "Ellas están hablando bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "You all walk fast", "es": "Ustedes están caminando rápido", "noun_id": None, "type": "auditory", "glosses": {"fast": "rápido", "rápido": "fast"}},
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
        "intro_chart": GERUND_INTRO,
        "rule_chart": GERUND_RULE,
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
            {"en": "I drink coffee", "es": "Yo estoy bebiendo café", "noun_id": "café", "type": "written", "glosses": {"coffee": "café", "café": "coffee"}},
            {"en": "You inhibit progress", "es": "Tú estás inhibiendo el progreso", "noun_id": None, "type": "auditory", "glosses": {"progress": "progreso", "progreso": "progress"}},
            {"en": "He prohibits smoking", "es": "Él está prohibiendo fumar", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "She leaves from home", "es": "Ella está saliendo de casa", "noun_id": "casa", "type": "auditory", "glosses": {"home": "casa", "casa": "home"}},
            {"en": "You drink juice", "es": "Usted está bebiendo jugo", "noun_id": None, "type": "written", "glosses": {"juice": "jugo", "jugo": "juice"}},
            {"en": "We inhibit the idea", "es": "Nosotros estamos inhibiendo la idea", "noun_id": None, "type": "auditory", "glosses": {"idea": "idea"}},
            {"en": "We (f) prohibit exit", "es": "Nosotras estamos prohibiendo la salida", "noun_id": None, "type": "written", "glosses": {"exit": "salida", "salida": "exit"}},
            {"en": "They leave from work", "es": "Ellos están saliendo del trabajo", "noun_id": "trabajo", "type": "auditory", "glosses": {"work": "trabajo", "trabajo": "work"}},
            {"en": "They (f) drink milk", "es": "Ellas están bebiendo leche", "noun_id": None, "type": "written", "glosses": {"milk": "leche", "leche": "milk"}},
            {"en": "You all inhibit the desire", "es": "Ustedes están inhibiendo el deseo", "noun_id": None, "type": "auditory", "glosses": {"desire": "deseo", "deseo": "desire"}},
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
        "intro_chart": GERUND_INTRO,
        "rule_chart": GERUND_RULE,
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
            {"en": "I speak well", "es": "Yo estoy hablando bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "You walk fast", "es": "Tú estás caminando rápido", "noun_id": None, "type": "auditory", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "He chats at home", "es": "Él está charlando en casa", "noun_id": "casa", "type": "written", "glosses": {"at home": "en casa", "en casa": "at home"}},
            {"en": "She eats fruit", "es": "Ella está comiendo fruta", "noun_id": None, "type": "auditory", "glosses": {"fruit": "fruta", "fruta": "fruit"}},
            {"en": "You speak fast", "es": "Usted está hablando rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "We walk home", "es": "Nosotros estamos caminando a casa", "noun_id": "casa", "type": "auditory", "glosses": {}},
            {"en": "We (f) chat well", "es": "Nosotras estamos charlando bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "They eat meat", "es": "Ellos están comiendo carne", "noun_id": None, "type": "auditory", "glosses": {"meat": "carne", "carne": "meat"}},
            {"en": "They (f) speak a lot", "es": "Ellas están hablando mucho", "noun_id": None, "type": "written", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "You all walk a lot", "es": "Ustedes están caminando mucho", "noun_id": None, "type": "auditory", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
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
        "intro_chart": GERUND_INTRO,
        "rule_chart": GERUND_RULE,
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
            {"en": "I drink milk", "es": "Yo estoy bebiendo leche", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You inhibit the desire", "es": "Tú estás inhibiendo el deseo", "noun_id": None, "type": "auditory", "glosses": {"desire": "deseo", "deseo": "desire"}},
            {"en": "He prohibits noise", "es": "Él está prohibiendo el ruido", "noun_id": None, "type": "written", "glosses": {"noise": "ruido", "ruido": "noise"}},
            {"en": "She leaves together", "es": "Ella está saliendo juntos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You drink wine", "es": "Usted está bebiendo vino", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "We inhibit the action", "es": "Nosotros estamos inhibiendo la acción", "noun_id": None, "type": "auditory", "glosses": {"action": "acción", "acción": "action"}},
            {"en": "We (f) prohibit that", "es": "Nosotras estamos prohibiendo eso", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They leave now", "es": "Ellos están saliendo ahora", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "They (f) drink water", "es": "Ellas están bebiendo agua", "noun_id": None, "type": "written", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "You all inhibit the response", "es": "Ustedes están inhibiendo la respuesta", "noun_id": None, "type": "auditory", "glosses": {"response": "respuesta", "respuesta": "response"}},
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

    # --- GL 18.5: Perfect Tenses — [drill_1][drill_2][chat] block ---
    # video_embed_id stays None until intro video is produced.
    "grammar_perfect_tenses_drill_1": {
        "title": "Perfect Tenses (1/2) — Present Perfect",
        "grammar_level": 18.5,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "comer", "vivir"],
        "video_embed_id": None,  # placeholder — content not yet produced
        "drill_type": "conjugation",
        "tense": "perfect",
        "intro_chart": PERFECT_TENSES_INTRO,
        "rule_chart": PERFECT_TENSES_RULE,
        "drill_config": {
            "answers": {
                "hablar": {
                    "yo": "he hablado", "tú": "has hablado", "él": "ha hablado", "ella": "ha hablado",
                    "usted": "ha hablado", "nosotros": "hemos hablado", "nosotras": "hemos hablado",
                    "ellos": "han hablado", "ellas": "han hablado", "ustedes": "han hablado",
                },
                "comer": {
                    "yo": "he comido", "tú": "has comido", "él": "ha comido", "ella": "ha comido",
                    "usted": "ha comido", "nosotros": "hemos comido", "nosotras": "hemos comido",
                    "ellos": "han comido", "ellas": "han comido", "ustedes": "han comido",
                },
                "vivir": {
                    "yo": "he vivido", "tú": "has vivido", "él": "ha vivido", "ella": "ha vivido",
                    "usted": "ha vivido", "nosotros": "hemos vivido", "nosotras": "hemos vivido",
                    "ellos": "han vivido", "ellas": "han vivido", "ustedes": "han vivido",
                },
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I have spoken with the doctor", "es": "He hablado con el doctor", "noun_id": "doctor", "type": "written", "glosses": {"doctor": "doctor"}},
            {"en": "You have eaten breakfast", "es": "Has comido el desayuno", "noun_id": None, "type": "auditory", "glosses": {"breakfast": "desayuno", "desayuno": "breakfast"}},
            {"en": "She has lived here for years", "es": "Ella ha vivido aquí por años", "noun_id": None, "type": "written", "glosses": {"years": "años", "años": "years"}},
            {"en": "We have spoken with our family", "es": "Hemos hablado con la familia", "noun_id": "familia", "type": "auditory", "glosses": {"family": "familia", "familia": "family"}},
            {"en": "They have eaten already", "es": "Ellos han comido ya", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You all have lived in many cities", "es": "Ustedes han vivido en muchas ciudades", "noun_id": "ciudad", "type": "auditory", "glosses": {"cities": "ciudades", "many": "muchas", "ciudades": "cities", "muchas": "many"}},
            {"en": "He has spoken English his whole life", "es": "Él ha hablado inglés toda su vida", "noun_id": None, "type": "written", "glosses": {"life": "vida", "whole": "toda", "vida": "life", "toda": "whole"}},
            {"en": "I have eaten too much", "es": "He comido demasiado", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) have lived together for a year", "es": "Nosotras hemos vivido juntas por un año", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You have spoken very well", "es": "Has hablado muy bien", "noun_id": None, "type": "auditory", "glosses": {"well": "bien", "bien": "well"}},
        ],
        "drill_targets": [
            {"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "ella"},
            {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "comer", "pronoun": "tú"},
            {"verb": "comer", "pronoun": "nosotras"}, {"verb": "comer", "pronoun": "él"},
            {"verb": "vivir", "pronoun": "usted"}, {"verb": "vivir", "pronoun": "nosotros"},
            {"verb": "vivir", "pronoun": "ellas"}, {"verb": "vivir", "pronoun": "ellos"},
        ],
        "phase_2_config": None,
    },
    "grammar_perfect_tenses_drill_2": {
        "title": "Perfect Tenses (2/2) — Pluperfect",
        "grammar_level": 18.5,
        "lesson_number": 2,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "comer", "vivir"],
        "video_embed_id": None,
        "drill_type": "conjugation",
        "tense": "perfect",
        "intro_chart": PERFECT_TENSES_INTRO,
        "rule_chart": PERFECT_TENSES_RULE,
        "drill_config": {
            "answers": {
                "hablar": {
                    "yo": "había hablado", "tú": "habías hablado", "él": "había hablado", "ella": "había hablado",
                    "usted": "había hablado", "nosotros": "habíamos hablado", "nosotras": "habíamos hablado",
                    "ellos": "habían hablado", "ellas": "habían hablado", "ustedes": "habían hablado",
                },
                "comer": {
                    "yo": "había comido", "tú": "habías comido", "él": "había comido", "ella": "había comido",
                    "usted": "había comido", "nosotros": "habíamos comido", "nosotras": "habíamos comido",
                    "ellos": "habían comido", "ellas": "habían comido", "ustedes": "habían comido",
                },
                "vivir": {
                    "yo": "había vivido", "tú": "habías vivido", "él": "había vivido", "ella": "había vivido",
                    "usted": "había vivido", "nosotros": "habíamos vivido", "nosotras": "habíamos vivido",
                    "ellos": "habían vivido", "ellas": "habían vivido", "ustedes": "habían vivido",
                },
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I had spoken before the meeting", "es": "Había hablado antes de la reunión", "noun_id": None, "type": "written", "glosses": {"meeting": "reunión", "reunión": "meeting"}},
            {"en": "You had eaten before we arrived", "es": "Habías comido antes de que llegáramos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "He had lived there for ten years", "es": "Él había vivido allí por diez años", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "We had spoken about that topic", "es": "Habíamos hablado de ese tema", "noun_id": None, "type": "auditory", "glosses": {"topic": "tema", "tema": "topic"}},
            {"en": "They had eaten everything", "es": "Ellos habían comido todo", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You all had lived in this house", "es": "Ustedes habían vivido en esta casa", "noun_id": "casa", "type": "auditory", "glosses": {}},
            {"en": "She had spoken with her sister", "es": "Ella había hablado con su hermana", "noun_id": None, "type": "written", "glosses": {"sister": "hermana", "hermana": "sister"}},
            {"en": "I had eaten in that restaurant", "es": "Había comido en ese restaurante", "noun_id": "restaurante", "type": "auditory", "glosses": {"restaurant": "restaurante", "restaurante": "restaurant"}},
            {"en": "We (f) had lived together for years", "es": "Nosotras habíamos vivido juntas por años", "noun_id": None, "type": "written", "glosses": {"years": "años", "together": "juntas", "años": "years", "juntas": "together"}},
            {"en": "You had spoken too quickly", "es": "Habías hablado demasiado rápido", "noun_id": None, "type": "auditory", "glosses": {"quickly": "rápido", "rápido": "quickly"}},
        ],
        "drill_targets": [
            {"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "ella"},
            {"verb": "hablar", "pronoun": "ellos"}, {"verb": "comer", "pronoun": "tú"},
            {"verb": "comer", "pronoun": "nosotros"}, {"verb": "comer", "pronoun": "ustedes"},
            {"verb": "vivir", "pronoun": "él"}, {"verb": "vivir", "pronoun": "usted"},
            {"verb": "vivir", "pronoun": "nosotras"}, {"verb": "vivir", "pronoun": "ellas"},
        ],
        "phase_2_config": None,
    },
    "grammar_perfect_tenses_chat": {
        "title": "Perfect Tenses — Chat",
        "grammar_level": 18.5,
        "lesson_number": 3,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "comer", "vivir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "perfect",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {
            "description": "Perfect-tense voice chat: practice present perfect (he/has/ha/hemos/han + participle) and pluperfect (había/habías/había/habíamos/habían + participle)",
            "targets": [
                {"phrase": "he hablado"},
                {"phrase": "has comido"},
                {"phrase": "ha vivido"},
                {"phrase": "hemos hablado"},
                {"phrase": "han comido"},
                {"phrase": "había hablado"},
                {"phrase": "habías comido"},
                {"phrase": "había vivido"},
                {"phrase": "habíamos hablado"},
                {"phrase": "habían vivido"},
            ],
        },
        "opener_en": "Have you been to the market today?",
        "opener_es": "¿Has ido al mercado hoy?",
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
        'intro_chart': MODAL_INF_INTRO,
        'rule_chart': MODAL_INF_RULE,
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
            {"en": "I have to speak Spanish", "es": "Yo tengo que hablar español", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You have to eat bread", "es": "Tú tienes que comer pan", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "He has to speak English", "es": "Él tiene que hablar inglés", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "She has to eat food", "es": "Ella tiene que comer comida", "noun_id": None, "type": "auditory", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "You have to speak well", "es": "Usted tiene que hablar bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "We have to eat fruit", "es": "Nosotros tenemos que comer fruta", "noun_id": None, "type": "auditory", "glosses": {"fruit": "fruta", "fruta": "fruit"}},
            {"en": "We (f) have to speak fast", "es": "Nosotras tenemos que hablar rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "They have to eat meat", "es": "Ellos tienen que comer carne", "noun_id": None, "type": "auditory", "glosses": {"meat": "carne", "carne": "meat"}},
            {"en": "They (f) have to speak a lot", "es": "Ellas tienen que hablar mucho", "noun_id": None, "type": "written", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "You all have to eat salad", "es": "Ustedes tienen que comer ensalada", "noun_id": None, "type": "auditory", "glosses": {}},
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
        'intro_chart': MODAL_INF_INTRO,
        'rule_chart': MODAL_INF_RULE,
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
            {"en": "It's my turn to live nearby", "es": "Yo me toca vivir cerca", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "It's your turn to study a lot", "es": "Tú te toca estudiar mucho", "noun_id": None, "type": "auditory", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "It's his turn to live together", "es": "Él le toca vivir juntos", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "It's her turn to study at home", "es": "Ella le toca estudiar en casa", "noun_id": "casa", "type": "auditory", "glosses": {"at home": "en casa", "en casa": "at home"}},
            {"en": "It's your turn to live alone", "es": "Usted le toca vivir solo", "noun_id": None, "type": "written", "glosses": {"alone": "solo", "solo": "alone"}},
            {"en": "It's our turn to study together", "es": "Nosotros nos toca estudiar juntos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "It's our (f) turn to live in the city", "es": "A nosotras nos toca vivir en la ciudad", "noun_id": "ciudad", "type": "written", "glosses": {"city": "ciudad", "ciudad": "city"}},
            {"en": "It's their turn to study here", "es": "Ellos les toca estudiar aquí", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "It's their (f) turn to live here", "es": "A ellas les toca vivir aquí", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "It's your turn to study Spanish", "es": "Ustedes les toca estudiar español", "noun_id": None, "type": "auditory", "glosses": {"Spanish": "español", "español": "Spanish"}},
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
        'lesson_number': 4,
        'lesson_type': 'conjugation',
        'word_workload': [
            'dormir',
            'escribir'
        ],
        'video_embed_id': None,
        'drill_type': 'ir_a_inf',
        'tense': 'modal_inf',
        'intro_chart': MODAL_INF_INTRO,
        'rule_chart': MODAL_INF_RULE,
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
            {"en": "I need to sleep a lot", "es": "Yo necesito dormir mucho", "noun_id": None, "type": "written", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "You need to write messages", "es": "Tú necesitas escribir mensajes", "noun_id": None, "type": "auditory", "glosses": {"messages": "mensajes", "mensajes": "messages"}},
            {"en": "He needs to sleep here", "es": "Él necesita dormir aquí", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "She needs to write names", "es": "Ella necesita escribir nombres", "noun_id": "nombre", "type": "auditory", "glosses": {"names": "nombres", "nombres": "names"}},
            {"en": "You need to sleep early", "es": "Usted necesita dormir temprano", "noun_id": None, "type": "written", "glosses": {"early": "temprano", "temprano": "early"}},
            {"en": "We need to write fast", "es": "Nosotros necesitamos escribir rápido", "noun_id": None, "type": "auditory", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "We (f) need to sleep well", "es": "Nosotras necesitamos dormir bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "They need to write a letter", "es": "Ellos necesitan escribir una carta", "noun_id": "carta", "type": "auditory", "glosses": {"letter": "carta", "carta": "letter"}},
            {"en": "They (f) need to sleep eight hours", "es": "Ellas necesitan dormir ocho horas", "noun_id": None, "type": "written", "glosses": {"hours": "horas", "horas": "hours"}},
            {"en": "You all need to write a book", "es": "Ustedes necesitan escribir un libro", "noun_id": "libro", "type": "auditory", "glosses": {"book": "libro", "libro": "book"}},
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
            'description': 'Necesito — Voice Chat: pulls from previous drill lesson',
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
        'intro_chart': IMPERFECT_INTRO,
        'rule_chart': IMPERFECT_RULE,
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
            {"en": "I used to speak Spanish", "es": "Yo hablaba español", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You used to listen music", "es": "Tú escuchabas música", "noun_id": None, "type": "auditory", "glosses": {"music": "música", "música": "music"}},
            {"en": "He used to speak English", "es": "Él hablaba inglés", "noun_id": None, "type": "written", "glosses": {"English": "inglés", "inglés": "English"}},
            {"en": "She used to listen the radio", "es": "Ella escuchaba la radio", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You used to speak well", "es": "Usted hablaba bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "We used to listen a song", "es": "Nosotros escuchábamos una canción", "noun_id": None, "type": "auditory", "glosses": {"song": "canción", "canción": "song"}},
            {"en": "We (f) used to speak fast", "es": "Nosotras hablábamos rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "They used to listen well", "es": "Ellos escuchaban bien", "noun_id": None, "type": "auditory", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "They (f) used to speak a lot", "es": "Ellas hablaban mucho", "noun_id": None, "type": "written", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "You all used to listen carefully", "es": "Ustedes escuchaban atentamente", "noun_id": None, "type": "auditory", "glosses": {}},
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
        'intro_chart': IMPERFECT_INTRO,
        'rule_chart': IMPERFECT_RULE,
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
            {"en": "I used to eat food", "es": "Yo comía comida", "noun_id": None, "type": "written", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "You used to live nearby", "es": "Tú vivías cerca", "noun_id": None, "type": "auditory", "glosses": {"nearby": "cerca", "cerca": "nearby"}},
            {"en": "He used to eat fruit", "es": "Él comía fruta", "noun_id": None, "type": "written", "glosses": {"fruit": "fruta", "fruta": "fruit"}},
            {"en": "She used to live together", "es": "Ella vivía juntos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You used to eat meat", "es": "Usted comía carne", "noun_id": None, "type": "written", "glosses": {"meat": "carne", "carne": "meat"}},
            {"en": "We used to live alone", "es": "Nosotros vivíamos solo", "noun_id": None, "type": "auditory", "glosses": {"alone": "solo", "solo": "alone"}},
            {"en": "We (f) used to eat salad", "es": "Nosotras comíamos ensalada", "noun_id": None, "type": "written", "glosses": {"salad": "ensalada", "ensalada": "salad"}},
            {"en": "They used to live in the city", "es": "Ellos vivían en la ciudad", "noun_id": "ciudad", "type": "auditory", "glosses": {"city": "ciudad", "ciudad": "city"}},
            {"en": "They (f) used to eat bread", "es": "Ellas comían pan", "noun_id": None, "type": "written", "glosses": {"bread": "pan", "pan": "bread"}},
            {"en": "You all used to live here", "es": "Ustedes vivían aquí", "noun_id": None, "type": "auditory", "glosses": {}},
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
        'intro_chart': IMPERFECT_INTRO,
        'rule_chart': IMPERFECT_RULE,
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
            {"en": "I used to go to the store", "es": "Yo iba a la tienda", "noun_id": "tienda", "type": "written", "glosses": {"store": "tienda", "tienda": "store"}},
            {"en": "You used to be likeable", "es": "Tú eras simpático", "noun_id": None, "type": "auditory", "glosses": {"likeable": "simpático", "simpático": "likeable"}},
            {"en": "He used to go to work", "es": "Él iba al trabajo", "noun_id": "trabajo", "type": "written", "glosses": {"work": "trabajo", "trabajo": "work"}},
            {"en": "She used to be Colombian", "es": "Ella era colombiano", "noun_id": None, "type": "auditory", "glosses": {"Colombian": "colombiano", "colombiano": "Colombian"}},
            {"en": "You used to go to the market", "es": "Usted iba al mercado", "noun_id": "mercado", "type": "written", "glosses": {"market": "mercado", "mercado": "market"}},
            {"en": "We used to be tall", "es": "Nosotros éramos alto", "noun_id": None, "type": "auditory", "glosses": {"tall": "alto", "alto": "tall"}},
            {"en": "We (f) used to go home", "es": "Nosotras íbamos a casa", "noun_id": "casa", "type": "written", "glosses": {"at home": "en casa", "en casa": "at home"}},
            {"en": "They used to be professional", "es": "Ellos eran profesional", "noun_id": None, "type": "auditory", "glosses": {"professional": "profesional", "profesional": "professional"}},
            {"en": "They (f) used to go to the park", "es": "Ellas iban al parque", "noun_id": "parque", "type": "written", "glosses": {"park": "parque", "parque": "park"}},
            {"en": "You all used to be important", "es": "Ustedes eran importante", "noun_id": None, "type": "auditory", "glosses": {"important": "importante", "importante": "important"}},
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
        'intro_chart': IMPERFECT_INTRO,
        'rule_chart': IMPERFECT_RULE,
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
            {"en": "I used to see the light", "es": "Yo veía la luz", "noun_id": "luz", "type": "written", "glosses": {"light": "luz", "luz": "light"}},
            {"en": "You used to write fast", "es": "Tú escribías rápido", "noun_id": None, "type": "auditory", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "He used to see the movie", "es": "Él veía la película", "noun_id": None, "type": "written", "glosses": {"movie": "película", "película": "movie"}},
            {"en": "She used to write a letter", "es": "Ella escribía una carta", "noun_id": "carta", "type": "auditory", "glosses": {"letter": "carta", "carta": "letter"}},
            {"en": "You used to see the family", "es": "Usted veía a la familia", "noun_id": "familia", "type": "written", "glosses": {"family": "familia", "familia": "family"}},
            {"en": "We used to write a book", "es": "Nosotros escribíamos un libro", "noun_id": "libro", "type": "auditory", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "We (f) used to see a photo", "es": "Nosotras veíamos una foto", "noun_id": None, "type": "written", "glosses": {"photo": "foto", "foto": "photo"}},
            {"en": "They used to write messages", "es": "Ellos escribían mensajes", "noun_id": None, "type": "auditory", "glosses": {"messages": "mensajes", "mensajes": "messages"}},
            {"en": "They (f) used to see well", "es": "Ellas veían bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "You all used to write names", "es": "Ustedes escribían nombres", "noun_id": "nombre", "type": "auditory", "glosses": {"names": "nombres", "nombres": "names"}},
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
        'intro_chart': REFLEXIVE_INTRO,
        'rule_chart': REFLEXIVE_RULE,
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
            {"en": "I wash hands", "es": "Yo me lavo las manos", "noun_id": None, "type": "written", "glosses": {"hands": "manos", "manos": "hands"}},
            {"en": "You are called Carlos", "es": "Tú te llamas Carlos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "He washes face", "es": "Él se lava la cara", "noun_id": None, "type": "written", "glosses": {"face": "cara", "cara": "face"}},
            {"en": "She is called Maria", "es": "Ella se llama María", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You wash hair", "es": "Usted se lava el pelo", "noun_id": None, "type": "written", "glosses": {"hair": "pelo", "pelo": "hair"}},
            {"en": "We are called Ana", "es": "Nosotros nos llamamos Ana", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) wash quickly", "es": "Nosotras nos lavamos rápido", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They are called Luis", "es": "Ellos se llaman Luis", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "They (f) wash well", "es": "Ellas se lavan bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "You all are called Sofía", "es": "Ustedes se llaman Sofía", "noun_id": None, "type": "auditory", "glosses": {}},
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
        'intro_chart': REFLEXIVE_INTRO,
        'rule_chart': REFLEXIVE_RULE,
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
            {"en": "I get up late", "es": "Yo me levanto tarde", "noun_id": None, "type": "written", "glosses": {"late": "tarde", "tarde": "late"}},
            {"en": "You shower well", "es": "Tú te duchas bien", "noun_id": None, "type": "auditory", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "He gets up fast", "es": "Él se levanta rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "She showers early", "es": "Ella se ducha temprano", "noun_id": None, "type": "auditory", "glosses": {"early": "temprano", "temprano": "early"}},
            {"en": "You get up at seven", "es": "Usted se levanta a las siete", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "We shower in the morning", "es": "Nosotros nos duchamos por la mañana", "noun_id": None, "type": "auditory", "glosses": {"morning": "mañana", "mañana": "morning"}},
            {"en": "We (f) get up together", "es": "Nosotras nos levantamos juntos", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They shower here", "es": "Ellos se duchan aquí", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "They (f) get up early", "es": "Ellas se levantan temprano", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You all shower fast", "es": "Ustedes se duchan rápido", "noun_id": None, "type": "auditory", "glosses": {"fast": "rápido", "rápido": "fast"}},
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
        'intro_chart': REFLEXIVE_INTRO,
        'rule_chart': REFLEXIVE_RULE,
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
            {"en": "I wake up fast", "es": "Yo me despierto rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "You go to bed here", "es": "Tú te acuestas aquí", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "He wakes up at six", "es": "Él se despierta a las seis", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "She goes to bed now", "es": "Ella se acuesta ahora", "noun_id": None, "type": "auditory", "glosses": {"now": "ahora", "ahora": "now"}},
            {"en": "You wake up early", "es": "Usted se despierta temprano", "noun_id": None, "type": "written", "glosses": {"early": "temprano", "temprano": "early"}},
            {"en": "We go to bed early", "es": "Nosotros nos acostamos temprano", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) wake up late", "es": "Nosotras nos despertamos tarde", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They go to bed late", "es": "Ellos se acuestan tarde", "noun_id": None, "type": "auditory", "glosses": {"late": "tarde", "tarde": "late"}},
            {"en": "They (f) wake up together", "es": "Ellas se despiertan juntos", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You all go to bed together", "es": "Ustedes se acuestan juntos", "noun_id": None, "type": "auditory", "glosses": {}},
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
        'intro_chart': REFLEXIVE_INTRO,
        'rule_chart': REFLEXIVE_RULE,
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
            {"en": "I get dressed together", "es": "Yo me visto juntos", "noun_id": None, "type": "written", "glosses": {"together": "juntos", "juntos": "together"}},
            {"en": "You sit down now", "es": "Tú te sientas ahora", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "He gets dressed fast", "es": "Él se viste rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "She sits down here", "es": "Ella se sienta aquí", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You get dressed well", "es": "Usted se viste bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "We sit down together", "es": "Nosotros nos sentamos juntos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) get dressed early", "es": "Nosotras nos vestemos temprano", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They sit down on the chair", "es": "Ellos se sientan en la silla", "noun_id": None, "type": "auditory", "glosses": {"chair": "silla", "silla": "chair"}},
            {"en": "They (f) get dressed for work", "es": "Ellas se visten para el trabajo", "noun_id": "trabajo", "type": "written", "glosses": {"work": "trabajo", "trabajo": "work"}},
            {"en": "You all sit down nearby", "es": "Ustedes se sientan cerca", "noun_id": None, "type": "auditory", "glosses": {}},
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
        'intro_chart': FUTURE_INTRO,
        'rule_chart': FUTURE_RULE,
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
            {"en": "I will speak Spanish", "es": "Yo hablaré español", "noun_id": None, "type": "written", "glosses": {"Spanish": "español", "español": "Spanish"}},
            {"en": "You will eat bread", "es": "Tú comerás pan", "noun_id": None, "type": "auditory", "glosses": {"bread": "pan", "pan": "bread"}},
            {"en": "He will speak English", "es": "Él hablará inglés", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "She will eat food", "es": "Ella comerá comida", "noun_id": None, "type": "auditory", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "You will speak well", "es": "Usted hablará bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "We will eat fruit", "es": "Nosotros comeremos fruta", "noun_id": None, "type": "auditory", "glosses": {"fruit": "fruta", "fruta": "fruit"}},
            {"en": "We (f) will speak fast", "es": "Nosotras hablaremos rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "They will eat meat", "es": "Ellos comerán carne", "noun_id": None, "type": "auditory", "glosses": {"meat": "carne", "carne": "meat"}},
            {"en": "They (f) will speak a lot", "es": "Ellas hablarán mucho", "noun_id": None, "type": "written", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "You all will eat salad", "es": "Ustedes comerán ensalada", "noun_id": None, "type": "auditory", "glosses": {"salad": "ensalada", "ensalada": "salad"}},
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
        'intro_chart': FUTURE_INTRO,
        'rule_chart': FUTURE_RULE,
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
            {"en": "I will live nearby", "es": "Yo viviré cerca", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You will study a lot", "es": "Tú estudiarás mucho", "noun_id": None, "type": "auditory", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "He will live together", "es": "Él vivirá juntos", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "She will study at home", "es": "Ella estudiará en casa", "noun_id": "casa", "type": "auditory", "glosses": {"at home": "en casa", "en casa": "at home"}},
            {"en": "You will live alone", "es": "Usted vivirá solo", "noun_id": None, "type": "written", "glosses": {"alone": "solo", "solo": "alone"}},
            {"en": "We will study together", "es": "Nosotros estudiaremos juntos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) will live in the city", "es": "Nosotras viviremos en la ciudad", "noun_id": "ciudad", "type": "written", "glosses": {"city": "ciudad", "ciudad": "city"}},
            {"en": "They will study here", "es": "Ellos estudiarán aquí", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "They (f) will live here", "es": "Ellas vivirán aquí", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You all will study Spanish", "es": "Ustedes estudiarán español", "noun_id": None, "type": "auditory", "glosses": {"Spanish": "español", "español": "Spanish"}},
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
        'intro_chart': FUTURE_INTRO,
        'rule_chart': FUTURE_RULE,
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
            {"en": "I will have the right answer", "es": "Yo tendré razón", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You will make a plan", "es": "Tú harás un plan", "noun_id": "plan", "type": "auditory", "glosses": {"plan": "plan"}},
            {"en": "He will have time", "es": "Él tendrá tiempo", "noun_id": "tiempo", "type": "written", "glosses": {"time": "tiempo", "tiempo": "time"}},
            {"en": "She will make the bed", "es": "Ella hará la cama", "noun_id": None, "type": "auditory", "glosses": {"bed": "cama", "cama": "bed"}},
            {"en": "You will have a dog", "es": "Usted tendrá un perro", "noun_id": "perro", "type": "written", "glosses": {}},
            {"en": "We will make homework", "es": "Nosotros haremos la tarea", "noun_id": None, "type": "auditory", "glosses": {"homework": "tarea", "tarea": "homework"}},
            {"en": "We (f) will have a house", "es": "Nosotras tendremos una casa", "noun_id": "casa", "type": "written", "glosses": {"house": "casa", "casa": "house"}},
            {"en": "They will make food", "es": "Ellos harán comida", "noun_id": None, "type": "auditory", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "They (f) will have hunger", "es": "Ellas tendrán hambre", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You all will make exercise", "es": "Ustedes harán ejercicio", "noun_id": None, "type": "auditory", "glosses": {"exercise": "ejercicio", "ejercicio": "exercise"}},
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
        'intro_chart': FUTURE_INTRO,
        'rule_chart': FUTURE_RULE,
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
            {"en": "I will say a story", "es": "Yo diré una historia", "noun_id": None, "type": "written", "glosses": {"story": "historia", "historia": "story"}},
            {"en": "You will be able work", "es": "Tú podrás trabajar", "noun_id": "trabajo", "type": "auditory", "glosses": {}},
            {"en": "He will say the truth", "es": "Él dirá la verdad", "noun_id": None, "type": "written", "glosses": {"truth": "verdad", "verdad": "truth"}},
            {"en": "She will be able speak", "es": "Ella podrá hablar", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You will say hi", "es": "Usted dirá hola", "noun_id": None, "type": "written", "glosses": {"hi": "hola", "hola": "hi"}},
            {"en": "We will be able come", "es": "Nosotros podremos venir", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) will say thanks", "es": "Nosotras diremos gracias", "noun_id": None, "type": "written", "glosses": {"thanks": "gracias", "gracias": "thanks"}},
            {"en": "They will be able help", "es": "Ellos podrán ayudar", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "They (f) will say nothing", "es": "Ellas dirán nada", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You all will be able go", "es": "Ustedes podrán ir", "noun_id": None, "type": "auditory", "glosses": {}},
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
        'intro_chart': FUTURE_INTRO,
        'rule_chart': FUTURE_RULE,
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
            {"en": "I will know the answer", "es": "Yo sabré la respuesta", "noun_id": None, "type": "written", "glosses": {"answer": "respuesta", "respuesta": "answer"}},
            {"en": "You will want water", "es": "Tú querrás agua", "noun_id": None, "type": "auditory", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "He will know the time", "es": "Él sabrá la hora", "noun_id": None, "type": "written", "glosses": {"time": "hora", "hora": "time"}},
            {"en": "She will want to help", "es": "Ella querrá ayudar", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You will know English", "es": "Usted sabrá inglés", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "We will want to go", "es": "Nosotros querremos ir", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) will know how to cook", "es": "Nosotras sabremos cocinar", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They will want to rest", "es": "Ellos querrán descansar", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "They (f) will know the truth", "es": "Ellas sabrán la verdad", "noun_id": None, "type": "written", "glosses": {"truth": "verdad", "verdad": "truth"}},
            {"en": "You all will want coffee", "es": "Ustedes querrán café", "noun_id": "café", "type": "auditory", "glosses": {"coffee": "café", "café": "coffee"}},
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
        'intro_chart': FUTURE_INTRO,
        'rule_chart': FUTURE_RULE,
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
            {"en": "I will come early", "es": "Yo vendré temprano", "noun_id": None, "type": "written", "glosses": {"early": "temprano", "temprano": "early"}},
            {"en": "You will leave from work", "es": "Tú saldrás del trabajo", "noun_id": "trabajo", "type": "auditory", "glosses": {"work": "trabajo", "trabajo": "work"}},
            {"en": "He will come tomorrow", "es": "Él vendrá mañana", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "She will leave together", "es": "Ella saldrá juntos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You will come from the store", "es": "Usted vendrá de la tienda", "noun_id": "tienda", "type": "written", "glosses": {"store": "tienda", "tienda": "store"}},
            {"en": "We will leave now", "es": "Nosotros saldremos ahora", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) will come home", "es": "Nosotras vendremos a casa", "noun_id": "casa", "type": "written", "glosses": {}},
            {"en": "They will leave early", "es": "Ellos saldrán temprano", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "They (f) will come from the park", "es": "Ellas vendrán del parque", "noun_id": "parque", "type": "written", "glosses": {"park": "parque", "parque": "park"}},
            {"en": "You all will leave from home", "es": "Ustedes saldrán de casa", "noun_id": "casa", "type": "auditory", "glosses": {"home": "casa", "casa": "home"}},
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
        'intro_chart': CONDITIONAL_INTRO,
        'rule_chart': CONDITIONAL_RULE,
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
            {"en": "I would speak Spanish", "es": "Yo hablaría español", "noun_id": None, "type": "written", "glosses": {"Spanish": "español", "español": "Spanish"}},
            {"en": "You would eat bread", "es": "Tú comerías pan", "noun_id": None, "type": "auditory", "glosses": {"bread": "pan", "pan": "bread"}},
            {"en": "He would speak English", "es": "Él hablaría inglés", "noun_id": None, "type": "written", "glosses": {"English": "inglés", "inglés": "English"}},
            {"en": "She would eat food", "es": "Ella comería comida", "noun_id": None, "type": "auditory", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "You would speak well", "es": "Usted hablaría bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "We would eat fruit", "es": "Nosotros comeríamos fruta", "noun_id": None, "type": "auditory", "glosses": {"fruit": "fruta", "fruta": "fruit"}},
            {"en": "We (f) would speak fast", "es": "Nosotras hablaríamos rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "They would eat meat", "es": "Ellos comerían carne", "noun_id": None, "type": "auditory", "glosses": {"meat": "carne", "carne": "meat"}},
            {"en": "They (f) would speak a lot", "es": "Ellas hablarían mucho", "noun_id": None, "type": "written", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "You all would eat salad", "es": "Ustedes comerían ensalada", "noun_id": None, "type": "auditory", "glosses": {}},
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
        'intro_chart': CONDITIONAL_INTRO,
        'rule_chart': CONDITIONAL_RULE,
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
            {"en": "I would live nearby", "es": "Yo viviría cerca", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You would study a lot", "es": "Tú estudiarías mucho", "noun_id": None, "type": "auditory", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "He would live together", "es": "Él viviría juntos", "noun_id": None, "type": "written", "glosses": {"together": "juntos", "juntos": "together"}},
            {"en": "She would study at home", "es": "Ella estudiaría en casa", "noun_id": "casa", "type": "auditory", "glosses": {"at home": "en casa", "en casa": "at home"}},
            {"en": "You would live alone", "es": "Usted viviría solo", "noun_id": None, "type": "written", "glosses": {"alone": "solo", "solo": "alone"}},
            {"en": "We would study together", "es": "Nosotros estudiaríamos juntos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) would live in the city", "es": "Nosotras viviríamos en la ciudad", "noun_id": "ciudad", "type": "written", "glosses": {"city": "ciudad", "ciudad": "city"}},
            {"en": "They would study here", "es": "Ellos estudiarían aquí", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "They (f) would live here", "es": "Ellas vivirían aquí", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You all would study Spanish", "es": "Ustedes estudiarían español", "noun_id": None, "type": "auditory", "glosses": {}},
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
        'intro_chart': CONDITIONAL_INTRO,
        'rule_chart': CONDITIONAL_RULE,
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
            {"en": "I would have the right answer", "es": "Yo tendría razón", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You would make a plan", "es": "Tú harías un plan", "noun_id": "plan", "type": "auditory", "glosses": {"plan": "plan"}},
            {"en": "He would have time", "es": "Él tendría tiempo", "noun_id": "tiempo", "type": "written", "glosses": {"time": "tiempo", "tiempo": "time"}},
            {"en": "She would make the bed", "es": "Ella haría la cama", "noun_id": None, "type": "auditory", "glosses": {"bed": "cama", "cama": "bed"}},
            {"en": "You would have a dog", "es": "Usted tendría un perro", "noun_id": "perro", "type": "written", "glosses": {}},
            {"en": "We would make homework", "es": "Nosotros haríamos la tarea", "noun_id": None, "type": "auditory", "glosses": {"homework": "tarea", "tarea": "homework"}},
            {"en": "We (f) would have a house", "es": "Nosotras tendríamos una casa", "noun_id": "casa", "type": "written", "glosses": {}},
            {"en": "They would make food", "es": "Ellos harían comida", "noun_id": None, "type": "auditory", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "They (f) would have hunger", "es": "Ellas tendrían hambre", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You all would make exercise", "es": "Ustedes harían ejercicio", "noun_id": None, "type": "auditory", "glosses": {"exercise": "ejercicio", "ejercicio": "exercise"}},
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
        'intro_chart': CONDITIONAL_INTRO,
        'rule_chart': CONDITIONAL_RULE,
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
            {"en": "I would say a story", "es": "Yo diría una historia", "noun_id": None, "type": "written", "glosses": {"story": "historia", "historia": "story"}},
            {"en": "You could work", "es": "Tú podrías trabajar", "noun_id": "trabajo", "type": "auditory", "glosses": {}},
            {"en": "He would say the truth", "es": "Él diría la verdad", "noun_id": None, "type": "written", "glosses": {"truth": "verdad", "verdad": "truth"}},
            {"en": "She could speak", "es": "Ella podría hablar", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You would say hi", "es": "Usted diría hola", "noun_id": None, "type": "written", "glosses": {"hi": "hola", "hola": "hi"}},
            {"en": "We could come", "es": "Nosotros podríamos venir", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) would say thanks", "es": "Nosotras diríamos gracias", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They could help", "es": "Ellos podrían ayudar", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "They (f) would say nothing", "es": "Ellas dirían nada", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You all could go", "es": "Ustedes podrían ir", "noun_id": None, "type": "auditory", "glosses": {}},
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
        'intro_chart': PRET_VS_IMPERFECT_INTRO,
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
            {"en": "I was reading when she arrived", "es": "Yo leía cuando ella llegó", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "We used to play every day", "es": "Jugábamos todos los días", "noun_id": None, "type": "auditory", "glosses": {"day": "día", "days": "días", "día": "day", "días": "days"}},
            {"en": "He ate the bread", "es": "Él comió el pan", "noun_id": "pan", "type": "written", "glosses": {"bread": "pan", "pan": "bread"}},
            {"en": "She was eating when I called", "es": "Ella comía cuando yo llamé", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "It was raining all morning", "es": "Llovía toda la mañana", "noun_id": None, "type": "written", "glosses": {"morning": "mañana", "mañana": "morning"}},
            {"en": "It rained yesterday", "es": "Llovió ayer", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "I was tired", "es": "Yo estaba cansado", "noun_id": None, "type": "written", "glosses": {"tired": "cansado", "cansado": "tired"}},
            {"en": "I was tired for an hour", "es": "Estuve cansado por una hora", "noun_id": "hora", "type": "auditory", "glosses": {"hour": "hora", "tired": "cansado", "hora": "hour", "cansado": "tired"}},
            {"en": "When I was a kid, I used to live in Mexico", "es": "Cuando era niño, vivía en México", "noun_id": None, "type": "written", "glosses": {"kid": "niño", "niño": "kid"}},
            {"en": "She lived in Mexico for five years", "es": "Ella vivió en México por cinco años", "noun_id": None, "type": "auditory", "glosses": {"five": "cinco", "years": "años", "cinco": "five", "años": "years"}}
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
        'intro_chart': PRET_SPELLING_INTRO,
        'rule_chart': PRET_SPELLING_RULE,
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
            {"en": "I paid the bill", "es": "Yo pagué la cuenta", "noun_id": None, "type": "written", "glosses": {"bill": "cuenta", "cuenta": "bill"}},
            {"en": "You played soccer", "es": "Tú jugaste fútbol", "noun_id": None, "type": "auditory", "glosses": {"soccer": "fútbol", "fútbol": "soccer"}},
            {"en": "He paid the food", "es": "Él pagó la comida", "noun_id": None, "type": "written", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "She played together", "es": "Ella jugó juntos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You paid the coffee", "es": "Usted pagó el café", "noun_id": "café", "type": "written", "glosses": {"coffee": "café", "café": "coffee"}},
            {"en": "We played in the park", "es": "Nosotros jugamos en el parque", "noun_id": "parque", "type": "auditory", "glosses": {"park": "parque", "parque": "park"}},
            {"en": "We (f) paid fast", "es": "Nosotras pagamos rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "They played well", "es": "Ellos jugaron bien", "noun_id": None, "type": "auditory", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "They (f) paid together", "es": "Ellas pagaron juntos", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You all played here", "es": "Ustedes jugaron aquí", "noun_id": None, "type": "auditory", "glosses": {}},
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
        'intro_chart': PRET_SPELLING_INTRO,
        'rule_chart': PRET_SPELLING_RULE,
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
            {"en": "I looked for work", "es": "Yo busqué trabajo", "noun_id": "trabajo", "type": "written", "glosses": {"work": "trabajo", "trabajo": "work"}},
            {"en": "You touched the piano", "es": "Tú tocaste el piano", "noun_id": None, "type": "auditory", "glosses": {"piano": "piano"}},
            {"en": "He looked for Maria", "es": "Él buscó a María", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "She touched the door", "es": "Ella tocó la puerta", "noun_id": "puerta", "type": "auditory", "glosses": {"door": "puerta", "puerta": "door"}},
            {"en": "You looked for the truth", "es": "Usted buscó la verdad", "noun_id": None, "type": "written", "glosses": {"truth": "verdad", "verdad": "truth"}},
            {"en": "We touched music", "es": "Nosotros tocamos música", "noun_id": None, "type": "auditory", "glosses": {"music": "música", "música": "music"}},
            {"en": "We (f) looked for an answer", "es": "Nosotras buscamos una respuesta", "noun_id": None, "type": "written", "glosses": {"answer": "respuesta", "respuesta": "answer"}},
            {"en": "They touched the song", "es": "Ellos tocaron la canción", "noun_id": None, "type": "auditory", "glosses": {"song": "canción", "canción": "song"}},
            {"en": "They (f) looked for the book", "es": "Ellas buscaron el libro", "noun_id": "libro", "type": "written", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "You all touched the guitar", "es": "Ustedes tocaron la guitarra", "noun_id": None, "type": "auditory", "glosses": {"guitar": "guitarra", "guitarra": "guitar"}},
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
        'intro_chart': PRET_SPELLING_INTRO,
        'rule_chart': PRET_SPELLING_RULE,
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
            {"en": "I started the class", "es": "Yo empecé la clase", "noun_id": None, "type": "written", "glosses": {"class": "clase", "clase": "class"}},
            {"en": "You had lunch fast", "es": "Tú almorzaste rápido", "noun_id": None, "type": "auditory", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "He started fast", "es": "Él empezó rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "She had lunch at home", "es": "Ella almorzó en casa", "noun_id": "casa", "type": "auditory", "glosses": {"at home": "en casa", "en casa": "at home"}},
            {"en": "You started early", "es": "Usted empezó temprano", "noun_id": None, "type": "written", "glosses": {"early": "temprano", "temprano": "early"}},
            {"en": "We had lunch together", "es": "Nosotros almorzamos juntos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) started now", "es": "Nosotras empezamos ahora", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They had lunch here", "es": "Ellos almorzaron aquí", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "They (f) started work", "es": "Ellas empezaron el trabajo", "noun_id": "trabajo", "type": "written", "glosses": {"work": "trabajo", "trabajo": "work"}},
            {"en": "You all had lunch early", "es": "Ustedes almorzaron temprano", "noun_id": None, "type": "auditory", "glosses": {"early": "temprano", "temprano": "early"}},
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
        'intro_chart': PRET_SPELLING_INTRO,
        'rule_chart': PRET_SPELLING_RULE,
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
            {"en": "I believed everything", "es": "Yo creí todo", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You read fast", "es": "Tú leíste rápido", "noun_id": None, "type": "auditory", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "He believed the story", "es": "Él creyó la historia", "noun_id": None, "type": "written", "glosses": {"story": "historia", "historia": "story"}},
            {"en": "She read a book", "es": "Ella leyó un libro", "noun_id": "libro", "type": "auditory", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "You believed the truth", "es": "Usted creyó la verdad", "noun_id": None, "type": "written", "glosses": {"truth": "verdad", "verdad": "truth"}},
            {"en": "We read the newspaper", "es": "Nosotros leímos el periódico", "noun_id": None, "type": "auditory", "glosses": {"newspaper": "periódico", "periódico": "newspaper"}},
            {"en": "We (f) believed in you", "es": "Nosotras creímos en ti", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They read a lot", "es": "Ellos leyeron mucho", "noun_id": None, "type": "auditory", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "They (f) believed Maria", "es": "Ellas creyeron a María", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You all read out loud", "es": "Ustedes leyeron en voz alta", "noun_id": None, "type": "auditory", "glosses": {"out loud": "en voz alta", "en voz alta": "out loud"}},
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
        'intro_chart': PRET_SPELLING_INTRO,
        'rule_chart': PRET_SPELLING_RULE,
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
            {"en": "I fell today", "es": "Yo caí hoy", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You heard the noise", "es": "Tú oíste el ruido", "noun_id": None, "type": "auditory", "glosses": {"noise": "ruido", "ruido": "noise"}},
            {"en": "He fell asleep", "es": "Él cayó dormido", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "She heard a song", "es": "Ella oyó una canción", "noun_id": None, "type": "auditory", "glosses": {"song": "canción", "canción": "song"}},
            {"en": "You fell here", "es": "Usted cayó aquí", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "We heard well", "es": "Nosotros oímos bien", "noun_id": None, "type": "auditory", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "We (f) fell fast", "es": "Nosotras caímos rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "They heard the radio", "es": "Ellos oyeron la radio", "noun_id": None, "type": "auditory", "glosses": {"radio": "radio"}},
            {"en": "They (f) fell on the street", "es": "Ellas cayeron en la calle", "noun_id": "calle", "type": "written", "glosses": {"street": "calle", "calle": "street"}},
            {"en": "You all heard music", "es": "Ustedes oyeron música", "noun_id": None, "type": "auditory", "glosses": {"music": "música", "música": "music"}},
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
        'intro_chart': PRET_SPELLING_INTRO,
        'rule_chart': PRET_SPELLING_RULE,
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
            {"en": "I built the office", "es": "Yo construí la oficina", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You flowed here", "es": "Tú fluiste aquí", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "He built fast", "es": "Él construyó rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "She flowed together", "es": "Ella fluyó juntos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You built a home", "es": "Usted construyó un hogar", "noun_id": None, "type": "written", "glosses": {"home": "hogar", "hogar": "home"}},
            {"en": "We flowed naturally", "es": "Nosotros fluimos naturalmente", "noun_id": None, "type": "auditory", "glosses": {"naturally": "naturalmente", "naturalmente": "naturally"}},
            {"en": "We (f) built a house", "es": "Nosotras construimos una casa", "noun_id": "casa", "type": "written", "glosses": {"house": "casa", "casa": "house"}},
            {"en": "They flowed fast", "es": "Ellos fluyeron rápido", "noun_id": None, "type": "auditory", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "They (f) built a bridge", "es": "Ellas construyeron un puente", "noun_id": None, "type": "written", "glosses": {"bridge": "puente", "puente": "bridge"}},
            {"en": "You all flowed well", "es": "Ustedes fluyeron bien", "noun_id": None, "type": "auditory", "glosses": {"well": "bien", "bien": "well"}},
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
        'intro_chart': PRET_STRONG_INTRO,
        'rule_chart': PRET_STRONG_RULE,
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
            {"en": "I was here", "es": "Yo estuve aquí", "noun_id": None, "type": "written", "glosses": {"here": "aquí", "aquí": "here"}},
            {"en": "You had a dog", "es": "Tú tuviste un perro", "noun_id": "perro", "type": "auditory", "glosses": {}},
            {"en": "He was at home", "es": "Él estuvo en casa", "noun_id": "casa", "type": "written", "glosses": {"at home": "en casa", "en casa": "at home"}},
            {"en": "She had a house", "es": "Ella tuvo una casa", "noun_id": "casa", "type": "auditory", "glosses": {"house": "casa", "casa": "house"}},
            {"en": "You were tired", "es": "Usted estuvo cansado", "noun_id": None, "type": "written", "glosses": {"tired": "cansado", "cansado": "tired"}},
            {"en": "We had hunger", "es": "Nosotros tuvimos hambre", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) were well", "es": "Nosotras estuvimos bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "They had the right answer", "es": "Ellos tuvieron razón", "noun_id": None, "type": "auditory", "glosses": {"right": "razón", "razón": "right"}},
            {"en": "They (f) were ready", "es": "Ellas estuvieron listo", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You all had time", "es": "Ustedes tuvieron tiempo", "noun_id": "tiempo", "type": "auditory", "glosses": {"time": "tiempo", "tiempo": "time"}},
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
        'intro_chart': PRET_STRONG_INTRO,
        'rule_chart': PRET_STRONG_RULE,
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
            {"en": "I could come", "es": "Yo pude venir", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You put the table", "es": "Tú pusiste la mesa", "noun_id": None, "type": "auditory", "glosses": {"table": "mesa", "mesa": "table"}},
            {"en": "He could help", "es": "Él pudo ayudar", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "She put water", "es": "Ella puso agua", "noun_id": None, "type": "auditory", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "You could go", "es": "Usted pudo ir", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "We put music", "es": "Nosotros pusimos música", "noun_id": None, "type": "auditory", "glosses": {"music": "música", "música": "music"}},
            {"en": "We (f) could work", "es": "Nosotras pudimos trabajar", "noun_id": "trabajo", "type": "written", "glosses": {}},
            {"en": "They put the coffee", "es": "Ellos pusieron el café", "noun_id": "café", "type": "auditory", "glosses": {"coffee": "café", "café": "coffee"}},
            {"en": "They (f) could speak", "es": "Ellas pudieron hablar", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You all put the book here", "es": "Ustedes pusieron el libro aquí", "noun_id": "libro", "type": "auditory", "glosses": {"book": "libro", "here": "aquí", "libro": "book", "aquí": "here"}},
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
        'intro_chart': PRET_STRONG_INTRO,
        'rule_chart': PRET_STRONG_RULE,
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
            {"en": "I knew English", "es": "Yo supe inglés", "noun_id": None, "type": "written", "glosses": {"English": "inglés", "inglés": "English"}},
            {"en": "You wanted to go", "es": "Tú quisiste ir", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "He knew how to cook", "es": "Él supo cocinar", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "She wanted to rest", "es": "Ella quiso descansar", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You knew the truth", "es": "Usted supo la verdad", "noun_id": None, "type": "written", "glosses": {"truth": "verdad", "verdad": "truth"}},
            {"en": "We wanted coffee", "es": "Nosotros quisimos café", "noun_id": "café", "type": "auditory", "glosses": {"coffee": "café", "café": "coffee"}},
            {"en": "We (f) knew the answer", "es": "Nosotras supimos la respuesta", "noun_id": None, "type": "written", "glosses": {"answer": "respuesta", "respuesta": "answer"}},
            {"en": "They wanted water", "es": "Ellos quisieron agua", "noun_id": None, "type": "auditory", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "They (f) knew the time", "es": "Ellas supieron la hora", "noun_id": None, "type": "written", "glosses": {"time": "hora", "hora": "time"}},
            {"en": "You all wanted to help", "es": "Ustedes quisieron ayudar", "noun_id": None, "type": "auditory", "glosses": {}},
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
        'intro_chart': PRET_STRONG_INTRO,
        'rule_chart': PRET_STRONG_RULE,
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
            {"en": "I walked alone", "es": "Yo anduve solo", "noun_id": None, "type": "written", "glosses": {"alone": "solo", "solo": "alone"}},
            {"en": "You came from the store", "es": "Tú viniste de la tienda", "noun_id": "tienda", "type": "auditory", "glosses": {"store": "tienda", "tienda": "store"}},
            {"en": "He walked fast", "es": "Él anduvo rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "She came home", "es": "Ella vino a casa", "noun_id": "casa", "type": "auditory", "glosses": {"at home": "en casa", "en casa": "at home"}},
            {"en": "You walked together", "es": "Usted anduvo juntos", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "We came from the park", "es": "Nosotros vinimos del parque", "noun_id": "parque", "type": "auditory", "glosses": {"park": "parque", "parque": "park"}},
            {"en": "We (f) walked through the park", "es": "Nosotras anduvimos por el parque", "noun_id": "parque", "type": "written", "glosses": {"park": "parque", "parque": "park"}},
            {"en": "They came early", "es": "Ellos vinieron temprano", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "They (f) walked here", "es": "Ellas anduvieron aquí", "noun_id": None, "type": "written", "glosses": {"here": "aquí", "aquí": "here"}},
            {"en": "You all came tomorrow", "es": "Ustedes vinieron mañana", "noun_id": None, "type": "auditory", "glosses": {"tomorrow": "mañana", "mañana": "tomorrow"}},
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
        'intro_chart': PRET_STRONG_INTRO,
        'rule_chart': PRET_STRONG_RULE,
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
            {"en": "I had eaten", "es": "Yo hube comido", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You fit in the box", "es": "Tú cupiste en la caja", "noun_id": None, "type": "auditory", "glosses": {"box": "caja", "caja": "box"}},
            {"en": "He had spoken", "es": "Él hubo hablado", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "She fit together", "es": "Ella cupo juntos", "noun_id": None, "type": "auditory", "glosses": {"together": "juntos", "juntos": "together"}},
            {"en": "You had gone", "es": "Usted hubo ido", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "We fit inside", "es": "Nosotros cupimos dentro", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) had lived", "es": "Nosotras hubimos vivido", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They fit well", "es": "Ellos cupieron bien", "noun_id": None, "type": "auditory", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "They (f) had been", "es": "Ellas hubieron estado", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You all fit here", "es": "Ustedes cupieron aquí", "noun_id": None, "type": "auditory", "glosses": {}},
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
        'intro_chart': PRET_STRONG_INTRO,
        'rule_chart': PRET_STRONG_RULE,
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
            {"en": "I maintained a promise", "es": "Yo mantuve una promesa", "noun_id": None, "type": "written", "glosses": {"promise": "promesa", "promesa": "promise"}},
            {"en": "You obtained an answer", "es": "Tú obtuviste una respuesta", "noun_id": None, "type": "auditory", "glosses": {"answer": "respuesta", "respuesta": "answer"}},
            {"en": "He maintained the house", "es": "Él mantuvo la casa", "noun_id": "casa", "type": "written", "glosses": {"house": "casa", "casa": "house"}},
            {"en": "She obtained permission", "es": "Ella obtuvo permiso", "noun_id": None, "type": "auditory", "glosses": {"permission": "permiso", "permiso": "permission"}},
            {"en": "You maintained the job", "es": "Usted mantuvo el trabajo", "noun_id": "trabajo", "type": "written", "glosses": {"job": "trabajo", "trabajo": "job"}},
            {"en": "We obtained information", "es": "Nosotros obtuvimos información", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) maintained calm", "es": "Nosotras mantuvimos la calma", "noun_id": None, "type": "written", "glosses": {"calm": "calma", "calma": "calm"}},
            {"en": "They obtained the book", "es": "Ellos obtuvieron el libro", "noun_id": "libro", "type": "auditory", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "They (f) maintained the plan", "es": "Ellas mantuvieron el plan", "noun_id": "plan", "type": "written", "glosses": {"plan": "plan"}},
            {"en": "You all obtained work", "es": "Ustedes obtuvieron trabajo", "noun_id": "trabajo", "type": "auditory", "glosses": {"work": "trabajo", "trabajo": "work"}},
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
        'intro_chart': PRET_DUCIR_INTRO,
        'rule_chart': PRET_DUCIR_RULE,
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
            {"en": "I translated the book", "es": "Yo traduje el libro", "noun_id": "libro", "type": "written", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "You drove fast", "es": "Tú condujiste rápido", "noun_id": None, "type": "auditory", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "He translated a letter", "es": "Él tradujo una carta", "noun_id": "carta", "type": "written", "glosses": {"letter": "carta", "carta": "letter"}},
            {"en": "She drove the car", "es": "Ella condujo el carro", "noun_id": "carro", "type": "auditory", "glosses": {}},
            {"en": "You translated fast", "es": "Usted tradujo rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "We drove to the city", "es": "Nosotros condujimos a la ciudad", "noun_id": "ciudad", "type": "auditory", "glosses": {"city": "ciudad", "ciudad": "city"}},
            {"en": "We (f) translated well", "es": "Nosotras tradujimos bien", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They drove carefully", "es": "Ellos condujeron con cuidado", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "They (f) translated the document", "es": "Ellas tradujeron el documento", "noun_id": None, "type": "written", "glosses": {"document": "documento", "documento": "document"}},
            {"en": "You all drove home", "es": "Ustedes condujeron a casa", "noun_id": "casa", "type": "auditory", "glosses": {"at home": "en casa", "en casa": "at home"}},
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
        'intro_chart': PRET_DUCIR_INTRO,
        'rule_chart': PRET_DUCIR_RULE,
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
            {"en": "I produced coffee", "es": "Yo produje café", "noun_id": "café", "type": "written", "glosses": {"coffee": "café", "café": "coffee"}},
            {"en": "You introduced an idea", "es": "Tú introdujiste una idea", "noun_id": None, "type": "auditory", "glosses": {"idea": "idea"}},
            {"en": "He produced work", "es": "Él produjo trabajo", "noun_id": "trabajo", "type": "written", "glosses": {"work": "trabajo", "trabajo": "work"}},
            {"en": "She introduced Maria", "es": "Ella introdujo a María", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You produced good wine", "es": "Usted produjo buen vino", "noun_id": None, "type": "written", "glosses": {"good": "buen", "buen": "good", "wine": "vino", "vino": "wine"}},
            {"en": "We introduced the topic", "es": "Nosotros introdujimos el tema", "noun_id": None, "type": "auditory", "glosses": {"topic": "tema", "tema": "topic"}},
            {"en": "We (f) produced results", "es": "Nosotras produjimos resultados", "noun_id": None, "type": "written", "glosses": {"results": "resultados", "resultados": "results"}},
            {"en": "They introduced the information", "es": "Ellos introdujeron la información", "noun_id": None, "type": "auditory", "glosses": {"information": "información", "información": "information"}},
            {"en": "They (f) produced food", "es": "Ellas produjeron comida", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You all introduced the book", "es": "Ustedes introdujeron el libro", "noun_id": "libro", "type": "auditory", "glosses": {"book": "libro", "libro": "book"}},
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
        'intro_chart': PRET_E_TO_I_INTRO,
        'rule_chart': PRET_E_TO_I_RULE,
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
            {"en": "I asked for coffee", "es": "Yo pedí café", "noun_id": "café", "type": "written", "glosses": {"coffee": "café", "café": "coffee"}},
            {"en": "You felt cold", "es": "Tú sentiste frío", "noun_id": None, "type": "auditory", "glosses": {"cold": "frío", "frío": "cold"}},
            {"en": "He asked for water", "es": "Él pidió agua", "noun_id": None, "type": "written", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "She felt heat", "es": "Ella sintió calor", "noun_id": None, "type": "auditory", "glosses": {"heat": "calor", "calor": "heat"}},
            {"en": "You asked for help", "es": "Usted pidió ayuda", "noun_id": None, "type": "written", "glosses": {"help": "ayuda", "ayuda": "help"}},
            {"en": "We felt the music", "es": "Nosotros sentimos la música", "noun_id": None, "type": "auditory", "glosses": {"music": "música", "música": "music"}},
            {"en": "We (f) asked for the bill", "es": "Nosotras pedimos la cuenta", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They felt pain", "es": "Ellos sintieron dolor", "noun_id": None, "type": "auditory", "glosses": {"pain": "dolor", "dolor": "pain"}},
            {"en": "They (f) asked for permission", "es": "Ellas pidieron permiso", "noun_id": None, "type": "written", "glosses": {"permission": "permiso", "permiso": "permission"}},
            {"en": "You all felt the breeze", "es": "Ustedes sintieron la brisa", "noun_id": None, "type": "auditory", "glosses": {"breeze": "brisa", "brisa": "breeze"}},
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
        'intro_chart': PRET_E_TO_I_INTRO,
        'rule_chart': PRET_E_TO_I_RULE,
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
            {"en": "I repeated the sentence", "es": "Yo repetí la frase", "noun_id": None, "type": "written", "glosses": {"sentence": "frase", "frase": "sentence"}},
            {"en": "You served the coffee", "es": "Tú serviste el café", "noun_id": "café", "type": "auditory", "glosses": {"coffee": "café", "café": "coffee"}},
            {"en": "He repeated a song", "es": "Él repitió una canción", "noun_id": None, "type": "written", "glosses": {"song": "canción", "canción": "song"}},
            {"en": "She served water", "es": "Ella sirvió agua", "noun_id": None, "type": "auditory", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "You repeated well", "es": "Usted repitió bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "We served the customers", "es": "Nosotros servimos a los clientes", "noun_id": None, "type": "auditory", "glosses": {"customers": "clientes", "clientes": "customers"}},
            {"en": "We (f) repeated fast", "es": "Nosotras repetimos rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "They served wine", "es": "Ellos sirvieron vino", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "They (f) repeated the word", "es": "Ellas repitieron la palabra", "noun_id": None, "type": "written", "glosses": {"word": "palabra", "palabra": "word"}},
            {"en": "You all served the food", "es": "Ustedes sirvieron la comida", "noun_id": None, "type": "auditory", "glosses": {"food": "comida", "comida": "food"}},
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
        'intro_chart': OBJ_DIRECT_INTRO,
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
            {"en": "I see it", "es": "Lo veo", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "She buys them", "es": "Las compra", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We eat it", "es": "Lo comemos", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They bring her", "es": "La traen", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You hear them", "es": "Los oyes", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "I read it", "es": "La leo", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "He drinks it", "es": "Lo bebe", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "We see them", "es": "Los vemos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "She wants it", "es": "Lo quiere", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "I take her", "es": "La llevo", "noun_id": None, "type": "auditory", "glosses": {}}
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
        'intro_chart': OBJ_INDIRECT_INTRO,
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
            {"en": "I give him the book", "es": "Le doy el libro", "noun_id": "libro", "type": "written", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "She tells them the truth", "es": "Les dice la verdad", "noun_id": "verdad", "type": "auditory", "glosses": {"truth": "verdad", "verdad": "truth"}},
            {"en": "We bring her the food", "es": "Le traemos la comida", "noun_id": "comida", "type": "written", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "They send him the letter", "es": "Le mandan la carta", "noun_id": "carta", "type": "auditory", "glosses": {"letter": "carta", "carta": "letter"}},
            {"en": "I write him a message", "es": "Le escribo un mensaje", "noun_id": "mensaje", "type": "written", "glosses": {"message": "mensaje", "mensaje": "message"}},
            {"en": "We pay them the money", "es": "Les pagamos el dinero", "noun_id": "dinero", "type": "auditory", "glosses": {"money": "dinero", "dinero": "money"}},
            {"en": "You give them the gift", "es": "Les das el regalo", "noun_id": "regalo", "type": "written", "glosses": {"gift": "regalo", "regalo": "gift"}},
            {"en": "She buys him the shirt", "es": "Le compra la camisa", "noun_id": "camisa", "type": "auditory", "glosses": {"shirt": "camisa", "camisa": "shirt"}},
            {"en": "I show him the photo", "es": "Le muestro la foto", "noun_id": "foto", "type": "written", "glosses": {}},
            {"en": "We tell them everything", "es": "Les decimos todo", "noun_id": None, "type": "auditory", "glosses": {}}
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
            'description': 'Recap voice chat (mid-section): consolidate direct + indirect object pronouns covered in obj_direct and obj_indirect',
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
        'intro_chart': OBJ_COMBINED_INTRO,
        'rule_chart': OBJ_COMBINED_RULE,
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
            {"en": "She gives it to me", "es": "Me lo da", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "I give it to you", "es": "Te lo doy", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "She gives it to him", "es": "Se lo da", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "We bring it to her", "es": "Se lo traemos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "I tell it to you", "es": "Te lo digo", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "He sends it to me", "es": "Me lo manda", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "She writes it to me", "es": "Me la escribe", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "We bring it to you", "es": "Te la traemos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "They give it to him", "es": "Se la dan", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "I show it to her", "es": "Se la muestro", "noun_id": None, "type": "auditory", "glosses": {}}
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
        'intro_chart': OBJ_COMBINED_INTRO,
        'rule_chart': OBJ_COMBINED_RULE,
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
            {"en": "They bring them to us", "es": "Nos los traen", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "She tells them to us", "es": "Nos los dice", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "He gives them to them", "es": "Se los da", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "We send them to her", "es": "Se las mandamos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "They show them to us", "es": "Nos las muestran", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "I write them to him", "es": "Se las escribo", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We pay them to them", "es": "Se los pagamos", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "You give them to us", "es": "Nos los das", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "She brings them to me", "es": "Me las trae", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "I send them to you", "es": "Te las mando", "noun_id": None, "type": "auditory", "glosses": {}}
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
            'description': 'Recap voice chat (end-of-section): consolidate combined object pronouns (se lo, me la, te los) covered in obj_combined_a and obj_combined_b',
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
        'intro_chart': SUBJ_PRES_INTRO,
        'rule_chart': SUBJ_PRES_RULE,
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
            {"en": "I hope that I speak Spanish", "es": "Espero que yo hable español", "noun_id": None, "type": "written", "glosses": {"Spanish": "español", "español": "Spanish"}},
            {"en": "I hope that you eat bread", "es": "Espero que tú comas pan", "noun_id": None, "type": "auditory", "glosses": {"bread": "pan", "pan": "bread"}},
            {"en": "I hope that he speaks English", "es": "Espero que él hable inglés", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "I hope that she eats food", "es": "Espero que ella coma comida", "noun_id": None, "type": "auditory", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "I hope that you speak well", "es": "Espero que usted hable bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "I hope that we eat fruit", "es": "Espero que nosotros comamos fruta", "noun_id": None, "type": "auditory", "glosses": {"fruit": "fruta", "fruta": "fruit"}},
            {"en": "I hope that we (f) speak fast", "es": "Espero que nosotras hablemos rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "I hope that they eat meat", "es": "Espero que ellos coman carne", "noun_id": None, "type": "auditory", "glosses": {"meat": "carne", "carne": "meat"}},
            {"en": "I hope that they (f) speak a lot", "es": "Espero que ellas hablen mucho", "noun_id": None, "type": "written", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "I hope that you all eat salad", "es": "Espero que ustedes coman ensalada", "noun_id": None, "type": "auditory", "glosses": {"salad": "ensalada", "ensalada": "salad"}},
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
        'intro_chart': SUBJ_PRES_INTRO,
        'rule_chart': SUBJ_PRES_RULE,
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
            {"en": "I hope that I live nearby", "es": "Espero que yo viva cerca", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "I hope that you study a lot", "es": "Espero que tú estudies mucho", "noun_id": None, "type": "auditory", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "I hope that he lives together", "es": "Espero que él viva juntos", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "I hope that she studies at home", "es": "Espero que ella estudie en casa", "noun_id": "casa", "type": "auditory", "glosses": {"at home": "en casa", "en casa": "at home"}},
            {"en": "I hope that you live alone", "es": "Espero que usted viva solo", "noun_id": None, "type": "written", "glosses": {"alone": "solo", "solo": "alone"}},
            {"en": "I hope that we study together", "es": "Espero que nosotros estudiemos juntos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "I hope that we (f) live in the city", "es": "Espero que nosotras vivamos en la ciudad", "noun_id": "ciudad", "type": "written", "glosses": {"city": "ciudad", "ciudad": "city"}},
            {"en": "I hope that they study here", "es": "Espero que ellos estudien aquí", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "I hope that they (f) live here", "es": "Espero que ellas vivan aquí", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "I hope that you all study Spanish", "es": "Espero que ustedes estudien español", "noun_id": None, "type": "auditory", "glosses": {}},
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
        'intro_chart': SUBJ_PRES_INTRO,
        'rule_chart': SUBJ_PRES_RULE,
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
            {"en": "I hope that I am likeable", "es": "Espero que yo sea simpático", "noun_id": None, "type": "written", "glosses": {"likeable": "simpático", "simpático": "likeable"}},
            {"en": "I hope that you go to the store", "es": "Espero que tú vayas a la tienda", "noun_id": "tienda", "type": "auditory", "glosses": {}},
            {"en": "I hope that he is Colombian", "es": "Espero que él sea colombiano", "noun_id": None, "type": "written", "glosses": {"Colombian": "colombiano", "colombiano": "Colombian"}},
            {"en": "I hope that she goes to work", "es": "Espero que ella vaya al trabajo", "noun_id": "trabajo", "type": "auditory", "glosses": {"work": "trabajo", "trabajo": "work"}},
            {"en": "I hope that you are tall", "es": "Espero que usted sea alto", "noun_id": None, "type": "written", "glosses": {"tall": "alto", "alto": "tall"}},
            {"en": "I hope that we go to the market", "es": "Espero que nosotros vayamos al mercado", "noun_id": "mercado", "type": "auditory", "glosses": {"market": "mercado", "mercado": "market"}},
            {"en": "I hope that we (f) are professional", "es": "Espero que nosotras seamos profesional", "noun_id": None, "type": "written", "glosses": {"professional": "profesional", "profesional": "professional"}},
            {"en": "I hope that they go home", "es": "Espero que ellos vayan a casa", "noun_id": "casa", "type": "auditory", "glosses": {"home": "casa", "casa": "home"}},
            {"en": "I hope that they (f) are important", "es": "Espero que ellas sean importante", "noun_id": None, "type": "written", "glosses": {"important": "importante", "importante": "important"}},
            {"en": "I hope that you all go to the park", "es": "Espero que ustedes vayan al parque", "noun_id": "parque", "type": "auditory", "glosses": {"park": "parque", "parque": "park"}},
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
        'intro_chart': SUBJ_PRES_INTRO,
        'rule_chart': SUBJ_PRES_RULE,
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
            {"en": "I hope that I am ready", "es": "Espero que yo esté listo", "noun_id": None, "type": "written", "glosses": {"ready": "listo", "listo": "ready"}},
            {"en": "I hope that you give thanks", "es": "Espero que tú des las gracias", "noun_id": None, "type": "auditory", "glosses": {"thanks": "gracias", "gracias": "thanks"}},
            {"en": "I hope that he is here", "es": "Espero que él esté aquí", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "I hope that she gives the book", "es": "Espero que ella dé el libro", "noun_id": "libro", "type": "auditory", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "I hope that you are at home", "es": "Espero que usted esté en casa", "noun_id": "casa", "type": "written", "glosses": {"at home": "en casa", "en casa": "at home"}},
            {"en": "I hope that we give money", "es": "Espero que nosotros demos dinero", "noun_id": "dinero", "type": "auditory", "glosses": {"money": "dinero", "dinero": "money"}},
            {"en": "I hope that we (f) are tired", "es": "Espero que nosotras estemos cansado", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "I hope that they give water", "es": "Espero que ellos den agua", "noun_id": None, "type": "auditory", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "I hope that they (f) are well", "es": "Espero que ellas estén bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "I hope that you all give an answer", "es": "Espero que ustedes den una respuesta", "noun_id": None, "type": "auditory", "glosses": {"answer": "respuesta", "respuesta": "answer"}},
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
        'intro_chart': SUBJ_PRES_INTRO,
        'rule_chart': SUBJ_PRES_RULE,
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
            {"en": "I hope that I know the answer", "es": "Espero que yo sepa la respuesta", "noun_id": None, "type": "written", "glosses": {"answer": "respuesta", "respuesta": "answer"}},
            {"en": "I hope that you have eaten", "es": "Espero que tú hayas comido", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "I hope that he knows the time", "es": "Espero que él sepa la hora", "noun_id": None, "type": "written", "glosses": {"time": "hora", "hora": "time"}},
            {"en": "I hope that she has spoken", "es": "Espero que ella haya hablado", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "I hope that you know English", "es": "Espero que usted sepa inglés", "noun_id": None, "type": "written", "glosses": {"English": "inglés", "inglés": "English"}},
            {"en": "I hope that we have gone", "es": "Espero que nosotros hayamos ido", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "I hope that we (f) know how to cook", "es": "Espero que nosotras sepamos cocinar", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "I hope that they have lived", "es": "Espero que ellos hayan vivido", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "I hope that they (f) know the truth", "es": "Espero que ellas sepan la verdad", "noun_id": None, "type": "written", "glosses": {"truth": "verdad", "verdad": "truth"}},
            {"en": "I hope that you all have been", "es": "Espero que ustedes hayan estado", "noun_id": None, "type": "auditory", "glosses": {}},
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
        'intro_chart': SUBJ_IMPF_INTRO,
        'rule_chart': SUBJ_IMPF_RULE,
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
            {"en": "If I spoke fast", "es": "Si yo hablara rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "If you ate meat", "es": "Si tú comieras carne", "noun_id": None, "type": "auditory", "glosses": {"meat": "carne", "carne": "meat"}},
            {"en": "If he spoke a lot", "es": "Si él hablara mucho", "noun_id": None, "type": "written", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "If she ate salad", "es": "Si ella comiera ensalada", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "If you spoke Spanish", "es": "Si usted hablara español", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "If we ate bread", "es": "Si nosotros comiéramos pan", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "If we (f) spoke English", "es": "Si nosotras habláramos inglés", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "If they ate food", "es": "Si ellos comieran comida", "noun_id": None, "type": "auditory", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "If they (f) spoke well", "es": "Si ellas hablaran bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "If you all ate fruit", "es": "Si ustedes comieran fruta", "noun_id": None, "type": "auditory", "glosses": {"fruit": "fruta", "fruta": "fruit"}},
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
        'intro_chart': SUBJ_IMPF_INTRO,
        'rule_chart': SUBJ_IMPF_RULE,
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
            {"en": "If I lived in the city", "es": "Si yo viviera en la ciudad", "noun_id": "ciudad", "type": "written", "glosses": {"city": "ciudad", "ciudad": "city"}},
            {"en": "If you studied here", "es": "Si tú estudiaras aquí", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "If he lived here", "es": "Si él viviera aquí", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "If she studied Spanish", "es": "Si ella estudiara español", "noun_id": None, "type": "auditory", "glosses": {"Spanish": "español", "español": "Spanish"}},
            {"en": "If you lived nearby", "es": "Si usted viviera cerca", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "If we studied a lot", "es": "Si nosotros estudiáramos mucho", "noun_id": None, "type": "auditory", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "If we (f) lived together", "es": "Si nosotras viviéramos juntos", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "If they studied at home", "es": "Si ellos estudiaran en casa", "noun_id": "casa", "type": "auditory", "glosses": {"at home": "en casa", "en casa": "at home"}},
            {"en": "If they (f) lived alone", "es": "Si ellas vivieran solo", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "If you all studied together", "es": "Si ustedes estudiaran juntos", "noun_id": None, "type": "auditory", "glosses": {}},
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
        'intro_chart': SUBJ_IMPF_INTRO,
        'rule_chart': SUBJ_IMPF_RULE,
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
            {"en": "If I was professional", "es": "Si yo fuera profesional", "noun_id": None, "type": "written", "glosses": {"professional": "profesional", "profesional": "professional"}},
            {"en": "If you had a house", "es": "Si tú tuvieras una casa", "noun_id": "casa", "type": "auditory", "glosses": {"house": "casa", "casa": "house"}},
            {"en": "If he was important", "es": "Si él fuera importante", "noun_id": None, "type": "written", "glosses": {"important": "importante", "importante": "important"}},
            {"en": "If she had hunger", "es": "Si ella tuviera hambre", "noun_id": None, "type": "auditory", "glosses": {"hunger": "hambre", "hambre": "hunger"}},
            {"en": "If you were likeable", "es": "Si usted fuera simpático", "noun_id": None, "type": "written", "glosses": {"likeable": "simpático", "simpático": "likeable"}},
            {"en": "If we had the right answer", "es": "Si nosotros tuviéramos razón", "noun_id": None, "type": "auditory", "glosses": {"right": "razón", "razón": "right"}},
            {"en": "If we (f) were Colombian", "es": "Si nosotras fuéramos colombiano", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "If they had time", "es": "Si ellos tuvieran tiempo", "noun_id": "tiempo", "type": "auditory", "glosses": {"time": "tiempo", "tiempo": "time"}},
            {"en": "If they (f) were tall", "es": "Si ellas fueran alto", "noun_id": None, "type": "written", "glosses": {"tall": "alto", "alto": "tall"}},
            {"en": "If you all had a dog", "es": "Si ustedes tuvieran un perro", "noun_id": "perro", "type": "auditory", "glosses": {"dog": "perro", "perro": "dog"}},
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
        'intro_chart': SUBJ_IMPF_INTRO,
        'rule_chart': SUBJ_IMPF_RULE,
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
            {"en": "If I made exercise", "es": "Si yo hiciera ejercicio", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "If you wanted to help", "es": "Si tú quisieras ayudar", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "If he made a plan", "es": "Si él hiciera un plan", "noun_id": "plan", "type": "written", "glosses": {"plan": "plan"}},
            {"en": "If she wanted to go", "es": "Si ella quisiera ir", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "If you made the bed", "es": "Si usted hiciera la cama", "noun_id": None, "type": "written", "glosses": {"bed": "cama", "cama": "bed"}},
            {"en": "If we wanted to rest", "es": "Si nosotros quisiéramos descansar", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "If we (f) made homework", "es": "Si nosotras hiciéramos la tarea", "noun_id": None, "type": "written", "glosses": {"homework": "tarea", "tarea": "homework"}},
            {"en": "If they wanted coffee", "es": "Si ellos quisieran café", "noun_id": "café", "type": "auditory", "glosses": {"coffee": "café", "café": "coffee"}},
            {"en": "If they (f) made food", "es": "Si ellas hicieran comida", "noun_id": None, "type": "written", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "If you all wanted water", "es": "Si ustedes quisieran agua", "noun_id": None, "type": "auditory", "glosses": {"water": "agua", "agua": "water"}},
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
        'intro_chart': SUBJ_IMPF_INTRO,
        'rule_chart': SUBJ_IMPF_RULE,
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
            {"en": "If I said a story", "es": "Si yo dijera una historia", "noun_id": None, "type": "written", "glosses": {"story": "historia", "historia": "story"}},
            {"en": "If you could work", "es": "Si tú pudieras trabajar", "noun_id": "trabajo", "type": "auditory", "glosses": {}},
            {"en": "If he said the truth", "es": "Si él dijera la verdad", "noun_id": None, "type": "written", "glosses": {"truth": "verdad", "verdad": "truth"}},
            {"en": "If she could speak", "es": "Si ella pudiera hablar", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "If you said hi", "es": "Si usted dijera hola", "noun_id": None, "type": "written", "glosses": {"hi": "hola", "hola": "hi"}},
            {"en": "If we could come", "es": "Si nosotros pudiéramos venir", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "If we (f) said thanks", "es": "Si nosotras dijéramos gracias", "noun_id": None, "type": "written", "glosses": {"thanks": "gracias", "gracias": "thanks"}},
            {"en": "If they could help", "es": "Si ellos pudieran ayudar", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "If they (f) said nothing", "es": "Si ellas dijeran nada", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "If you all could go", "es": "Si ustedes pudieran ir", "noun_id": None, "type": "auditory", "glosses": {}},
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


# ── Merge auto-generated noun-only glosses into each drill_sentence ──────────
# Sidecar `grammar_drill_glosses.py` is produced by
# `scripts/generate_drill_glosses.py`. Glosses are noun-only by design — they
# let learners look up unfamiliar nouns ("casa", "tienda", "maestro") without
# revealing the verb/conjugation/grammar form the drill is testing. We merge
# at import time so consumers see one uniform shape.
from app.data.grammar_drill_glosses import DRILL_GLOSSES as _DRILL_GLOSSES

for _sid, _glosses_per_sent in _DRILL_GLOSSES.items():
    _cfg = GRAMMAR_SITUATIONS.get(_sid)
    if not _cfg:
        continue
    _sents = _cfg.get('drill_sentences') or []
    for _i, _g in enumerate(_glosses_per_sent):
        if _g is None or _i >= len(_sents):
            continue
        _sent = _sents[_i]
        if not isinstance(_sent, dict):
            continue
        # Sidecar always wins — earlier hand-authored glosses included
        # verbs/adjectives that revealed the drill answer.
        _sent['glosses'] = _g

del _sid, _cfg, _sents, _i, _g, _sent, _glosses_per_sent, _DRILL_GLOSSES


# ── Merge scene-anchored opener lines for every grammar `*_chat` lesson ──────
# Sidecar `grammar_chat_openers.py` carries opener_es / opener_en / scene per
# chat lesson. Without it, every chat falls through to the FE's generic
# "Hello! How can I help you today?" line. The scene field is consumed by
# `situation_roles.py`; here we only patch in the openers.
from app.data.grammar_chat_openers import CHAT_OPENERS as _CHAT_OPENERS

for _sid, _opener in _CHAT_OPENERS.items():
    _cfg = GRAMMAR_SITUATIONS.get(_sid)
    if not _cfg:
        continue
    _cfg['opener_es'] = _opener['opener_es']
    _cfg['opener_en'] = _opener['opener_en']

del _sid, _cfg, _opener, _CHAT_OPENERS


def get_grammar_config(situation_id: str) -> dict | None:
    """Get grammar config for a situation ID, or None if not a grammar situation."""
    return GRAMMAR_SITUATIONS.get(situation_id)


def derive_intro_chart(config: dict) -> dict | None:
    """Compute the gentle-intro chart for a lesson on the fly when the author
    hasn't supplied one. Returns None for chat-only lessons.

    - If the lesson already carries an `intro_chart`, that wins (manual override).
    - Conjugation lessons → kind: 'verb_conjugation' built from word_workload + drill_config.answers.
    - Rule lessons with rule_chart of kind 'table' → drop the optional 'Note' column for a cleaner reveal/quiz.
    - Rule lessons with rule_chart of kinds 'comparison' / 'list' / 'rule_pack' → reused verbatim.
    - Rule lessons with no rule_chart → minimal kind: 'list' from word_workload (reveal-only fallback).
    - Chat-only lessons (drill_type='skip') → no intro.
    """
    authored = config.get("intro_chart")
    if authored:
        return authored

    drill_type = config.get("drill_type")
    if drill_type == "skip":
        return None

    # Conjugation pipeline
    if drill_type in ("conjugation", "ir_a_inf"):
        verbs = config.get("word_workload") or []
        answers = (config.get("drill_config") or {}).get("answers") or {}
        verbs_in_answers = [v for v in verbs if v in answers]
        if not verbs_in_answers:
            return None
        return {
            "kind": "verb_conjugation",
            "tense_label": config.get("tense") or "present",
            "verbs": verbs_in_answers,
            "answers": {v: answers[v] for v in verbs_in_answers},
        }

    # Rule pipeline — prefer existing rule_chart, simplified
    rule_chart = config.get("rule_chart")
    if rule_chart:
        kind = rule_chart.get("kind")
        if kind == "table":
            headers = list(rule_chart.get("headers") or [])
            rows = [list(r) for r in (rule_chart.get("rows") or [])]
            # Drop optional commentary columns (kept inputs are the prompt + Spanish target).
            DROP_HEADERS = {"note", "notes", "example", "examples"}
            drop_idxs = [i for i, h in enumerate(headers) if h.strip().lower() in DROP_HEADERS]
            if drop_idxs:
                keep = [i for i in range(len(headers)) if i not in drop_idxs]
                headers = [headers[i] for i in keep]
                rows = [[r[i] if i < len(r) else "" for i in keep] for r in rows]
            # Pick the Spanish-target column to blank for the recall quiz.
            # Headers like "Person", "Distance", "English", "Used for", "Replaces",
            # "Meaning" are *prompts* (English-side); the remaining column(s) hold
            # the Spanish forms the user should produce.
            NON_TARGET_HEADERS = {
                "person", "distance", "english", "used for", "meaning",
                "replaces", "rule", "category",
            }
            non_target_idxs = [i for i, h in enumerate(headers) if h.strip().lower() in NON_TARGET_HEADERS]
            target_idxs = [i for i in range(len(headers)) if i not in non_target_idxs]
            quiz_col = target_idxs[0] if target_idxs else 0
            # Prompts default to all non-target columns; if every header looks
            # Spanish-side, fall back to whichever column ISN'T the quiz column.
            prompt_idxs = non_target_idxs or [i for i in range(len(headers)) if i != quiz_col]
            return {
                "kind": "table",
                "title": rule_chart.get("title") or config.get("title") or "",
                "headers": headers,
                "rows": rows,
                "footnote": rule_chart.get("footnote"),
                "quiz_column_index": quiz_col,
                "prompt_column_indices": prompt_idxs,
            }
        if kind in ("comparison", "list", "rule_pack", "cards", "text"):
            return rule_chart

    # Last resort — show the new vocabulary as a list
    workload = config.get("word_workload") or []
    if workload:
        return {
            "kind": "list",
            "title": config.get("title") or "New words",
            "items": [str(w) for w in workload],
        }
    return None


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
