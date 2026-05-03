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
            "title": "hablar (to speak)",
            "rows": [
                ["yo", "habl|o"],
                ["tú", "habl|as"],
                ["él / ella / usted", "habl|a"],
                ["nosotros / nosotras", "habl|amos"],
                ["ellos / ellas / ustedes", "habl|an"],
            ],
            "footnote": "The stem (habl-) stays the same. Only the ending changes with the subject.",
        },
        {
            "kind": "mini_table",
            "title": "escuchar (to listen)",
            "rows": [
                ["yo", "escuch|o"],
                ["tú", "escuch|as"],
                ["él / ella / usted", "escuch|a"],
                ["nosotros / nosotras", "escuch|amos"],
                ["ellos / ellas / ustedes", "escuch|an"],
            ],
            "footnote": "Same -AR endings — the stem (escuch-) is the only difference.",
        },
    ],
    "recall": [
        {
            "verb": "hablar",
            "answers": {"yo": "habl|o", "tú": "habl|as", "él": "habl|a",
                        "nosotros": "habl|amos", "ellos": "habl|an"},
        },
        {
            "verb": "escuchar",
            "answers": {"yo": "escuch|o", "tú": "escuch|as", "él": "escuch|a",
                        "nosotros": "escuch|amos", "ellos": "escuch|an"},
        },
    ],
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
            "title": "beber (to drink)",
            "rows": [
                ["yo", "beb|o"],
                ["tú", "beb|es"],
                ["él / ella / usted", "beb|e"],
                ["nosotros / nosotras", "beb|emos"],
                ["ellos / ellas / ustedes", "beb|en"],
            ],
            "footnote": "Yo still ends in -o (same as -ar). The other forms swap the -a for -e: -es, -e, -emos, -en.",
        },
        {
            "kind": "mini_table",
            "title": "comer (to eat)",
            "rows": [
                ["yo", "com|o"],
                ["tú", "com|es"],
                ["él / ella / usted", "com|e"],
                ["nosotros / nosotras", "com|emos"],
                ["ellos / ellas / ustedes", "com|en"],
            ],
            "footnote": "Same -ER endings. Only the stem (com-) differs.",
        },
    ],
    "recall": [
        {
            "verb": "beber",
            "answers": {"yo": "beb|o", "tú": "beb|es", "él": "beb|e",
                        "nosotros": "beb|emos", "ellos": "beb|en"},
        },
        {
            "verb": "comer",
            "answers": {"yo": "com|o", "tú": "com|es", "él": "com|e",
                        "nosotros": "com|emos", "ellos": "com|en"},
        },
    ],
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
            "title": "vivir (to live)",
            "rows": [
                ["yo", "viv|o"],
                ["tú", "viv|es"],
                ["él / ella / usted", "viv|e"],
                ["nosotros / nosotras", "viv|imos"],
                ["ellos / ellas / ustedes", "viv|en"],
            ],
            "footnote": "Same as -er except nosotros: -emos (beb|emos) vs -imos (viv|imos).",
        },
        {
            "kind": "mini_table",
            "title": "escribir (to write)",
            "rows": [
                ["yo", "escrib|o"],
                ["tú", "escrib|es"],
                ["él / ella / usted", "escrib|e"],
                ["nosotros / nosotras", "escrib|imos"],
                ["ellos / ellas / ustedes", "escrib|en"],
            ],
            "footnote": "Same -IR endings. Only the stem (escrib-) differs.",
        },
    ],
    "recall": [
        {
            "verb": "vivir",
            "answers": {"yo": "viv|o", "tú": "viv|es", "él": "viv|e",
                        "nosotros": "viv|imos", "ellos": "viv|en"},
        },
        {
            "verb": "escribir",
            "answers": {"yo": "escrib|o", "tú": "escrib|es", "él": "escrib|e",
                        "nosotros": "escrib|imos", "ellos": "escrib|en"},
        },
    ],
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

IRREGULAR_PRESENT_SER_ESTAR_INTRO = {
    "kind": "cards",
    "title": "Irregular Present — ser + estar",
    "cards": [
        {
            "kind": "text",
            "title": "Spanish has two verbs for \"to be\"",
            "body": "English uses *am / is / are* for everything. Spanish splits this into **ser** and **estar**. Choosing the wrong one is the most common beginner mistake — and the rule is mostly about *permanence vs. condition*.",
        },
        {
            "kind": "comparison",
            "title": "The core split",
            "left": {
                "heading": "ser — what something IS",
                "items": [
                    "Identity (soy doctora)",
                    "Nationality (soy mexicano)",
                    "Profession (es ingeniero)",
                    "Permanent traits (es alto)",
                    "Time and date (son las tres)",
                    "Material (es de madera)",
                ],
            },
            "right": {
                "heading": "estar — how/where it IS right now",
                "items": [
                    "Location (está en casa)",
                    "Mood / health (estoy bien)",
                    "Temporary state (la sopa está fría)",
                    "Ongoing action (estoy comiendo)",
                    "Result of change (está roto)",
                ],
            },
            "footnote": "Trick: if you can swap \"is\" for \"feels\" or \"is currently,\" you almost always want estar.",
        },
        {
            "kind": "text",
            "title": "Same adjective, different meaning",
            "body": "**Es aburrido** = he's boring (a trait). **Está aburrido** = he's bored (right now). Same word, opposite meaning. The verb you pick changes everything.",
        },
        {
            "kind": "mini_table",
            "title": "ser (to be (identity))",
            "rows": [
            ["yo", "|soy"],
            ["tú", "|eres"],
            ["él / ella / usted", "|es"],
            ["nosotros / nosotras", "|somos"],
            ["ellos / ellas / ustedes", "|son"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "estar (to be (state))",
            "rows": [
            ["yo", "est|oy"],
            ["tú", "est|ás"],
            ["él / ella / usted", "est|á"],
            ["nosotros / nosotras", "est|amos"],
            ["ellos / ellas / ustedes", "est|án"],
            ],
        },
    ],
    "recall": [
        {"verb": "ser",
         "answers": {"yo": "|soy", "tú": "|eres", "él": "|es", "nosotros": "|somos", "ellos": "|son"}},
        {"verb": "estar",
         "answers": {"yo": "est|oy", "tú": "est|ás", "él": "est|á", "nosotros": "est|amos", "ellos": "est|án"}},
    ],
}

IRREGULAR_PRESENT_IR_DAR_INTRO = {
    "kind": "cards",
    "title": "Irregular Present — ir + dar",
    "cards": [
        {
            "kind": "text",
            "title": "ir + dar: high-frequency, hand-memorize",
            "body": "**ir** (to go) and **dar** (to give) are short, suppletive verbs. Both end in **-oy** in yo (voy / doy) and follow a similar pattern.",
        },
        {
            "kind": "text",
            "title": "Why these two together",
            "body": "ir is the workhorse for the *ir + a + infinitive* future construction (you'll meet it again in GL 9). dar is essential for any 'give' or 'pass' construction.",
        },
        {
            "kind": "mini_table",
            "title": "ir (to go)",
            "rows": [
            ["yo", "|voy"],
            ["tú", "|vas"],
            ["él / ella / usted", "|va"],
            ["nosotros / nosotras", "|vamos"],
            ["ellos / ellas / ustedes", "|van"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "dar (to give)",
            "rows": [
            ["yo", "d|oy"],
            ["tú", "d|as"],
            ["él / ella / usted", "d|a"],
            ["nosotros / nosotras", "d|amos"],
            ["ellos / ellas / ustedes", "d|an"],
            ],
        },
    ],
    "recall": [
        {"verb": "ir",
         "answers": {"yo": "|voy", "tú": "|vas", "él": "|va", "nosotros": "|vamos", "ellos": "|van"}},
        {"verb": "dar",
         "answers": {"yo": "d|oy", "tú": "d|as", "él": "d|a", "nosotros": "d|amos", "ellos": "d|an"}},
    ],
}

IRREGULAR_PRESENT_TENER_VENIR_INTRO = {
    "kind": "cards",
    "title": "Irregular Present — tener + venir",
    "cards": [
        {
            "kind": "text",
            "title": "tener + venir: high-frequency, hand-memorize",
            "body": "**tener** (to have) and **venir** (to come) share two irregularities: yo ends in **-go** (tengo, vengo), and the e→ie stem change appears in tú / él / ellos (tienes, viene, vienen).",
        },
        {
            "kind": "text",
            "title": "Why these two together",
            "body": "tener is also used for ages and obligations: *tengo 30 años*, *tengo que trabajar*. venir works for arrivals and origins.",
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
        },
    ],
    "recall": [
        {"verb": "tener",
         "answers": {"yo": "ten|go", "tú": "t|ienes", "él": "t|iene", "nosotros": "ten|emos", "ellos": "t|ienen"}},
        {"verb": "venir",
         "answers": {"yo": "ven|go", "tú": "v|ienes", "él": "v|iene", "nosotros": "ven|imos", "ellos": "v|ienen"}},
    ],
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
            "left": {
                "heading": "para → forward / in order to",
                "items": [
                    "Recipient: para mi madre (for my mother)",
                    "Deadline: para el lunes (for Monday)",
                    "Destination: salgo para Lima (I'm leaving for Lima)",
                    "In order to: estudio para aprender (I study in order to learn)",
                    "Opinion: para mí, está bien (for me, it's fine)",
                ],
            },
            "right": {
                "heading": "por → cause / motion / by",
                "items": [
                    "Reason: gracias por la ayuda (thanks for the help)",
                    "Duration: por dos horas (for two hours)",
                    "Route: caminamos por el parque (we walked through the park)",
                    "Exchange: pagué $10 por el libro (I paid $10 for the book)",
                    "On behalf of: lo hago por ti (I'm doing it for you / on your behalf)",
                    "By (agent): este libro fue escrito por mí (this book was written by me)",
                ],
            },
            "footnote": "Big clue: if you can swap \"for\" for \"in order to,\" use **para**. If you can swap it for \"by\" or \"because of,\" use **por**.",
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
            "kind": "text",
            "title": "Quick test: would \"I'm familiar with X\" sound weird?",
            "body": "If swapping \"I know\" for **\"I'm familiar with\"** sounds **fine**, use **conocer**. If it sounds **weird**, use **saber**.\n\n*\"I know this wine\"* → \"I'm familiar with this wine\" — sounds fine → **conozco este vino**.\n\n*\"I know a lot about wine\"* → \"I'm familiar with a lot about wine\" — sounds weird → **sé mucho sobre el vino**.\n\n*\"I know Russian politics\"* → \"I'm familiar with Russian politics\" — sounds fine → **conozco la política rusa**.\n\n**Exception:** With **people**, use *conocer* only if you've actually met them. With **countries / cities**, use *conocer* only if you've been there.",
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
    "title": "gustar — \"to be pleasing\"",
    "cards": [
        {
            "kind": "text",
            "title": "Flip the sentence around",
            "body": "Forget \"to like\" for a moment. **gustar** literally means **\"to be pleasing\"**.\n\nSo the Spanish thought is **the chocolate is pleasing to me** — not \"I like the chocolate.\" The *thing* does the action; *you* are the one it acts on.",
        },
        {
            "kind": "text",
            "title": "Try it in Spanish word-for-word",
            "body": "**el chocolate gusta a mí**\n→ \"the chocolate is pleasing to me\"\n\nThe word *gusta* means **is pleasing**. The phrase *a mí* means **to me**.",
        },
        {
            "kind": "comparison",
            "title": "Quick check: what does \"el chocolate gusta a mí\" mean?",
            "left": {
                "heading": "✓ This one",
                "items": ["the chocolate is pleasing to me"],
            },
            "right": {
                "heading": "✗ Not this",
                "items": ["I am pleasing to the chocolate"],
            },
            "footnote": "*A mí* = to me (the receiver). The chocolate is doing the pleasing — chocolate first, me second.",
        },
        {
            "kind": "comparison",
            "title": "Another one: \"el café gusta a mí\"",
            "left": {
                "heading": "✓ This one",
                "items": ["the coffee is pleasing to me"],
            },
            "right": {
                "heading": "✗ Not this",
                "items": ["I am pleasing to the coffee"],
            },
            "footnote": "Same shape — the noun is doing the pleasing, *a mí* is the receiver.",
        },
        {
            "kind": "comparison",
            "title": "One more: \"el libro gusta a mí\"",
            "left": {
                "heading": "✓ This one",
                "items": ["the book is pleasing to me"],
            },
            "right": {
                "heading": "✗ Not this",
                "items": ["I am pleasing to the book"],
            },
        },
        {
            "kind": "text",
            "title": "Shortcut: \"a mí\" → \"me\" (before the verb)",
            "body": "Spanish lets you replace *a mí* with the short form **me**, and slide it in front of the verb.\n\n**el chocolate me gusta** — same meaning, smoother to say.",
        },
        {
            "kind": "text",
            "title": "Re-order: noun goes to the end",
            "body": "Spanish also lets you put the noun at the end. The meaning doesn't change, only the order:\n\n**me gusta el chocolate**\n\nLined up word-for-word:\n*me* → to me\n*gusta* → is pleasing\n*el chocolate* → the chocolate\n\nThis is the form you'll hear and say most.",
        },
        {
            "kind": "text",
            "title": "Now: \"to you\" — te",
            "body": "**te gusta el chocolate** = the chocolate is pleasing to you (informal).\n\n*te* → to you\n*gusta* → is pleasing\n*el chocolate* → the chocolate",
        },
        {
            "kind": "text",
            "title": "\"to him / to her / to you (formal)\" all share one form: le",
            "body": "**le gusta el chocolate** = the chocolate is pleasing to **him** (or **her**, or **you (fml)**, depending on context).\n\n*le* → to him / to her / to you (fml)\n*gusta* → is pleasing\n*el chocolate* → the chocolate",
        },
        {
            "kind": "text",
            "title": "\"le\" can also mean \"to it\"",
            "body": "**le gusta el agua** = the water is pleasing **to it** (a dog, a cat, anything).\n\nContext tells you whether *le* refers to him, her, you (fml), or it. The form doesn't change.",
        },
        {
            "kind": "text",
            "title": "\"to us\" — nos",
            "body": "**nos gusta el chocolate** = the chocolate is pleasing to us.\n\n*nos* → to us\n*gusta* → is pleasing\n*el chocolate* → the chocolate",
        },
        {
            "kind": "text",
            "title": "\"to them / to you all\" — les",
            "body": "**les gusta el chocolate** = the chocolate is pleasing **to them** (or **to you all**).\n\n*les* → to them / to you all\n*gusta* → is pleasing\n*el chocolate* → the chocolate",
        },
        {
            "kind": "comparison",
            "title": "All five short forms",
            "left": {
                "heading": "Singular receivers",
                "items": [
                    "me  →  to me",
                    "te  →  to you",
                    "le  →  to him / her / you (fml) / it",
                ],
            },
            "right": {
                "heading": "Plural receivers",
                "items": [
                    "nos  →  to us",
                    "les  →  to them / you all",
                ],
            },
            "footnote": "Same five short forms you'll meet again later. For gustar, they always come right before the verb.",
        },
        {
            "kind": "text",
            "title": "How to translate it back to natural English",
            "body": "We don't normally say \"to me is pleasing the chocolate\" in English — we say **\"I like chocolate.\"**\n\nFor now, think it the other way around (*to me is pleasing*) until the form becomes habit. Once it sticks, you can flip back to \"I like\" mentally.",
        },
    ],
    "recall": [
        {
            "verb": "gustar",
            "answers": {
                "yo": "me gust|a",
                "tú": "te gust|a",
                "él": "le gust|a",
                "nosotros": "nos gust|a",
                "ellos": "les gust|a",
            },
        },
    ],
}

GUSTAR_PLURAL_INTRO = {
    "kind": "cards",
    "title": "gustar — when the thing is plural",
    "cards": [
        {
            "kind": "text",
            "title": "One thing → gusta. Many things → gustan.",
            "body": "In Part 1 you saw **me gusta el chocolate** — *the chocolate* is one thing, so the verb ends in *-a*: **gusta**.\n\nIf you swap in *more than one* thing, the verb adds an *-n* and becomes **gustan**.",
        },
        {
            "kind": "text",
            "title": "Side by side",
            "body": "**me gusta el chocolate** = the chocolate (one thing) is pleasing to me.\n\n**me gustan los chocolates** = the chocolates (many things) are pleasing to me.\n\nThe pronoun *me* doesn't change. Only the verb switches between *gusta* and *gustan*, depending on whether the thing is one or many.",
        },
        {
            "kind": "comparison",
            "title": "Quick check: which one fits?",
            "left": {
                "heading": "me ___ los libros (the books)",
                "items": ["**gustan** ✓ (the books = many things)"],
            },
            "right": {
                "heading": "me ___ el libro (the book)",
                "items": ["**gusta** ✓ (the book = one thing)"],
            },
            "footnote": "Look at the *thing* — is it singular or plural? That picks the verb.",
        },
        {
            "kind": "text",
            "title": "Same five pronouns, all paired with gustan",
            "body": "Pronoun stays the same; only the verb flips to **gustan** when the thing is plural.\n\n*me gustan los gatos* = I like cats\n*te gustan los libros* = you like books\n*le gustan las flores* = he/she/you-fml likes flowers\n*nos gustan las películas* = we like movies\n*les gustan los perros* = they / you all like dogs",
        },
        {
            "kind": "comparison",
            "title": "Watch the slot — singular vs plural",
            "left": {
                "heading": "Singular thing → gusta",
                "items": [
                    "me gusta el café",
                    "te gusta la música",
                    "le gusta el libro",
                ],
            },
            "right": {
                "heading": "Plural thing → gustan",
                "items": [
                    "me gustan los cafés",
                    "te gustan las canciones",
                    "le gustan los libros",
                ],
            },
            "footnote": "The verb agrees with the THING — never with the person.",
        },
    ],
    "recall": [
        {
            "verb": "gustar",
            "answers": {
                "yo": "me gust|an",
                "tú": "te gust|an",
                "él": "le gust|an",
                "nosotros": "nos gust|an",
                "ellos": "les gust|an",
            },
        },
    ],
}

GUSTAR_EMPHATIC_INTRO = {
    "kind": "cards",
    "title": "gustar — adding emphasis (a mí, a ti, a él…)",
    "cards": [
        {
            "kind": "text",
            "title": "What if you want to say \"*I* like it\" with stress?",
            "body": "**me gusta el café** is the everyday way to say it. But sometimes you want to **emphasize who** — \"*I* like coffee (and you don't)\" or \"as for me, I like it.\"\n\nSpanish has a longer form for that: tack **a mí** (or *a ti*, *a él*…) on the front.",
        },
        {
            "kind": "text",
            "title": "The pattern",
            "body": "**A mí me gusta el café** = *as for me*, I like coffee.\n\nThe shorter form (*me gusta el café*) is still there — you just *add* **a mí** in front for emphasis. Same meaning, more weight on \"me\".",
        },
        {
            "kind": "comparison",
            "title": "All the emphatic forms",
            "left": {
                "heading": "Singular",
                "items": [
                    "**a mí** me gusta…",
                    "**a ti** te gusta…",
                    "**a él / a ella / a usted** le gusta…",
                ],
            },
            "right": {
                "heading": "Plural",
                "items": [
                    "**a nosotros / a nosotras** nos gusta…",
                    "**a ellos / a ellas / a ustedes** les gusta…",
                ],
            },
            "footnote": "The short pronoun (me / te / le / nos / les) stays in. The emphatic *a mí* / *a ti* / etc. is an extra layer.",
        },
        {
            "kind": "text",
            "title": "When to use it",
            "body": "**Contrast**: *A mí me gusta el té, pero a ella le gusta el café.* (I like tea, but she likes coffee.)\n\n**Clarification of \"le\"**: since *le* could be him, her, or you-fml, *a él / a ella / a usted* clarifies which one you mean.\n\n**Politeness**: *A usted le gusta el vino, ¿no?* — directly addressing one person.",
        },
    ],
    "recall": [
        {
            "verb": "gustar",
            "answers": {
                "yo": "a mí me gust|a",
                "tú": "a ti te gust|a",
                "él": "a él le gust|a",
                "nosotros": "a nosotros nos gust|a",
                "ellos": "a ellos les gust|a",
            },
        },
    ],
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



# ─────────────────────────────────────────────────────────────────────────────
# Phase C.3 sub-block intros — auto-spliced from scripts/_glX_output.py
# ─────────────────────────────────────────────────────────────────────────────

# ── From _gl4_5_output.py ──

IRREGULAR_PRESENT_II_HACER_PONER_INTRO = {
    "kind": "cards",
    "title": "Irregular Present II — hacer + poner",
    "cards": [
        {
            "kind": "text",
            "title": "hacer + poner",
            "body": "**hacer** (to do/make) and **poner** (to put) both have a yo-form that ends in **-go** (hago, pongo). Outside of yo, they conjugate like regular -er verbs.",
        },
        {
            "kind": "text",
            "title": "Why these two together",
            "body": "This 'yo-go' pattern is one of the most common irregularities in Spanish. Once you spot it, you can predict yo for many verbs.",
        },
        {
            "kind": "mini_table",
            "title": "hacer (to do/make)",
            "rows": [
            ["yo", "ha|go"],
            ["tú", "hac|es"],
            ["él / ella / usted", "hac|e"],
            ["nosotros / nosotras", "hac|emos"],
            ["ellos / ellas / ustedes", "hac|en"],
            ],
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
        },
    ],
    "recall": [
        {"verb": "hacer", "answers": {"yo": "ha|go", "tú": "hac|es", "él": "hac|e", "nosotros": "hac|emos", "ellos": "hac|en"}},
        {"verb": "poner", "answers": {"yo": "pon|go", "tú": "pon|es", "él": "pon|e", "nosotros": "pon|emos", "ellos": "pon|en"}},
    ],
}

IRREGULAR_PRESENT_II_SALIR_DECIR_INTRO = {
    "kind": "cards",
    "title": "Irregular Present II — salir + decir",
    "cards": [
        {
            "kind": "text",
            "title": "salir + decir",
            "body": "**salir** (to leave/go out) is yo-go (salgo) and otherwise regular. **decir** (to say) is yo-go *plus* an e→i stem change (digo, dices, dice, dicen).",
        },
        {
            "kind": "text",
            "title": "Why these two together",
            "body": "decir is unusually irregular and very high-frequency — drill it until it's automatic.",
        },
        {
            "kind": "mini_table",
            "title": "salir (to leave/go out)",
            "rows": [
            ["yo", "sal|go"],
            ["tú", "sal|es"],
            ["él / ella / usted", "sal|e"],
            ["nosotros / nosotras", "sal|imos"],
            ["ellos / ellas / ustedes", "sal|en"],
            ],
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
        },
    ],
    "recall": [
        {"verb": "salir", "answers": {"yo": "sal|go", "tú": "sal|es", "él": "sal|e", "nosotros": "sal|imos", "ellos": "sal|en"}},
        {"verb": "decir", "answers": {"yo": "di|go", "tú": "d|ices", "él": "d|ice", "nosotros": "dec|imos", "ellos": "d|icen"}},
    ],
}

IRREGULAR_PRESENT_II_OIR_CAER_INTRO = {
    "kind": "cards",
    "title": "Irregular Present II — oír + caer",
    "cards": [
        {
            "kind": "text",
            "title": "oír + caer",
            "body": "**oír** (to hear) and **caer** (to fall) both take **-igo** in yo (oigo, caigo). oír also inserts a **y** in tú/él/ellos (oyes, oye, oyen).",
        },
        {
            "kind": "text",
            "title": "Why these two together",
            "body": "The y-insertion in oír makes the vowel cluster pronounceable. Watch for the same trick in construir / huir later (GL 5).",
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
        },
        {
            "kind": "mini_table",
            "title": "caer (to fall)",
            "rows": [
            ["yo", "ca|igo"],
            ["tú", "ca|es"],
            ["él / ella / usted", "ca|e"],
            ["nosotros / nosotras", "ca|emos"],
            ["ellos / ellas / ustedes", "ca|en"],
            ],
        },
    ],
    "recall": [
        {"verb": "oír", "answers": {"yo": "o|igo", "tú": "o|yes", "él": "o|ye", "nosotros": "o|ímos", "ellos": "o|yen"}},
        {"verb": "caer", "answers": {"yo": "ca|igo", "tú": "ca|es", "él": "ca|e", "nosotros": "ca|emos", "ellos": "ca|en"}},
    ],
}

IRREGULAR_PRESENT_II_TRAER_VALER_INTRO = {
    "kind": "cards",
    "title": "Irregular Present II — traer + valer",
    "cards": [
        {
            "kind": "text",
            "title": "traer + valer",
            "body": "**traer** (to bring) takes **-igo** in yo (traigo). **valer** (to be worth) takes **-go** in yo (valgo). Outside yo, both behave like regular -er verbs.",
        },
        {
            "kind": "text",
            "title": "Why these two together",
            "body": "valer shows up in fixed phrases like *vale la pena* (it's worth it) and *¿cuánto vale?* (how much is it?).",
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
        },
        {
            "kind": "mini_table",
            "title": "valer (to be worth)",
            "rows": [
            ["yo", "val|go"],
            ["tú", "val|es"],
            ["él / ella / usted", "val|e"],
            ["nosotros / nosotras", "val|emos"],
            ["ellos / ellas / ustedes", "val|en"],
            ],
        },
    ],
    "recall": [
        {"verb": "traer", "answers": {"yo": "tra|igo", "tú": "tra|es", "él": "tra|e", "nosotros": "tra|emos", "ellos": "tra|en"}},
        {"verb": "valer", "answers": {"yo": "val|go", "tú": "val|es", "él": "val|e", "nosotros": "val|emos", "ellos": "val|en"}},
    ],
}

# ── From _gl5_output.py ──

SPELLING_CHANGES_CONOCER_PRODUCIR_INTRO = {
    "kind": "cards",
    "title": "Spelling Changes — conocer + producir",
    "cards": [
        {
            "kind": "text",
            "title": "conocer + producir",
            "body": "Verbs ending in **-cer** / **-cir** preceded by a vowel insert a **z** before -co in the yo form: conoz**co**, produz**co**. The other forms stay regular.",
        },
        {
            "kind": "text",
            "title": "Why these two together",
            "body": "This is a spelling-only change to keep the soft /θ/ or /s/ sound before the back vowel. The pattern repeats in many useful verbs (parecer, ofrecer, traducir).",
        },
        {
            "kind": "mini_table",
            "title": "conocer (to know (a person/place))",
            "rows": [
            ["yo", "conoz|co"],
            ["tú", "conoc|es"],
            ["él / ella / usted", "conoc|e"],
            ["nosotros / nosotras", "conoc|emos"],
            ["ellos / ellas / ustedes", "conoc|en"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "producir (to produce)",
            "rows": [
            ["yo", "produz|co"],
            ["tú", "produc|es"],
            ["él / ella / usted", "produc|e"],
            ["nosotros / nosotras", "produc|imos"],
            ["ellos / ellas / ustedes", "produc|en"],
            ],
        },
    ],
    "recall": [
        {"verb": "conocer", "answers": {"yo": "conoz|co", "tú": "conoc|es", "él": "conoc|e", "nosotros": "conoc|emos", "ellos": "conoc|en"}},
        {"verb": "producir", "answers": {"yo": "produz|co", "tú": "produc|es", "él": "produc|e", "nosotros": "produc|imos", "ellos": "produc|en"}},
    ],
}

SPELLING_CHANGES_CONSTRUIR_CONSEGUIR_INTRO = {
    "kind": "cards",
    "title": "Spelling Changes — construir + conseguir",
    "cards": [
        {
            "kind": "text",
            "title": "construir + conseguir",
            "body": "**construir** inserts a **y** in all singular and 3rd-plural forms (constru**y**o). **conseguir** drops the **u** before -o/-a (consig**o**) — a pure spelling rule to keep the /g/ hard.",
        },
        {
            "kind": "text",
            "title": "Why these two together",
            "body": "construir's y-insertion mirrors oír (GL 4.5). conseguir's spelling shift parallels seguir, distinguir.",
        },
        {
            "kind": "mini_table",
            "title": "construir (to build)",
            "rows": [
            ["yo", "constr|uyo"],
            ["tú", "constr|uyes"],
            ["él / ella / usted", "constr|uye"],
            ["nosotros / nosotras", "constr|uimos"],
            ["ellos / ellas / ustedes", "constr|uyen"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "conseguir (to obtain/get)",
            "rows": [
            ["yo", "consig|o"],
            ["tú", "consig|ues"],
            ["él / ella / usted", "consig|ue"],
            ["nosotros / nosotras", "conseg|uimos"],
            ["ellos / ellas / ustedes", "consig|uen"],
            ],
        },
    ],
    "recall": [
        {"verb": "construir", "answers": {"yo": "constr|uyo", "tú": "constr|uyes", "él": "constr|uye", "nosotros": "constr|uimos", "ellos": "constr|uyen"}},
        {"verb": "conseguir", "answers": {"yo": "consig|o", "tú": "consig|ues", "él": "consig|ue", "nosotros": "conseg|uimos", "ellos": "consig|uen"}},
    ],
}

SPELLING_CHANGES_RECOGER_DIRIGIR_INTRO = {
    "kind": "cards",
    "title": "Spelling Changes — recoger + dirigir",
    "cards": [
        {
            "kind": "text",
            "title": "recoger + dirigir",
            "body": "**-ger** / **-gir** verbs change **g → j** before -o (yo only): reco**jo**, diri**jo**. Spelling-only — the sound stays the same.",
        },
        {
            "kind": "text",
            "title": "Why these two together",
            "body": "All other forms use plain g (recoges, diriges). Same trick repeats in coger, escoger, exigir, fingir.",
        },
        {
            "kind": "mini_table",
            "title": "recoger (to pick up)",
            "rows": [
            ["yo", "reco|jo"],
            ["tú", "recog|es"],
            ["él / ella / usted", "recog|e"],
            ["nosotros / nosotras", "recog|emos"],
            ["ellos / ellas / ustedes", "recog|en"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "dirigir (to direct)",
            "rows": [
            ["yo", "diri|jo"],
            ["tú", "dirig|es"],
            ["él / ella / usted", "dirig|e"],
            ["nosotros / nosotras", "dirig|imos"],
            ["ellos / ellas / ustedes", "dirig|en"],
            ],
        },
    ],
    "recall": [
        {"verb": "recoger", "answers": {"yo": "reco|jo", "tú": "recog|es", "él": "recog|e", "nosotros": "recog|emos", "ellos": "recog|en"}},
        {"verb": "dirigir", "answers": {"yo": "diri|jo", "tú": "dirig|es", "él": "dirig|e", "nosotros": "dirig|imos", "ellos": "dirig|en"}},
    ],
}

SPELLING_CHANGES_CONVENCER_CONTINUAR_INTRO = {
    "kind": "cards",
    "title": "Spelling Changes — convencer + continuar",
    "cards": [
        {
            "kind": "text",
            "title": "convencer + continuar",
            "body": "**-cer** preceded by a consonant changes **c → z** before -o (yo only): conven**zo**, ven**zo**. **continuar** carries a written accent on the **ú** in stressed forms (continúo, continúas, continúa, continúan).",
        },
        {
            "kind": "text",
            "title": "Why these two together",
            "body": "The accent on continuar marks a stressed vowel that would otherwise glide into a diphthong — same trick in actuar, graduarse.",
        },
        {
            "kind": "mini_table",
            "title": "convencer (to convince)",
            "rows": [
            ["yo", "conven|zo"],
            ["tú", "convenc|es"],
            ["él / ella / usted", "convenc|e"],
            ["nosotros / nosotras", "convenc|emos"],
            ["ellos / ellas / ustedes", "convenc|en"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "continuar (to continue)",
            "rows": [
            ["yo", "contin|úo"],
            ["tú", "contin|úas"],
            ["él / ella / usted", "contin|úa"],
            ["nosotros / nosotras", "contin|uamos"],
            ["ellos / ellas / ustedes", "contin|úan"],
            ],
        },
    ],
    "recall": [
        {"verb": "convencer", "answers": {"yo": "conven|zo", "tú": "convenc|es", "él": "convenc|e", "nosotros": "convenc|emos", "ellos": "convenc|en"}},
        {"verb": "continuar", "answers": {"yo": "contin|úo", "tú": "contin|úas", "él": "contin|úa", "nosotros": "contin|uamos", "ellos": "contin|úan"}},
    ],
}

# ── From _gl6_output.py ──

PRESENT_O_UE_PODER_VOLVER_INTRO = {
    "kind": "cards",
    "title": "Stem o→ue — poder + volver",
    "cards": [
        {
            "kind": "text",
            "title": "poder + volver",
            "body": "Stem-changing verbs change **o → ue** in the stressed syllable: p**ue**do, v**ue**lvo. The change skips nosotros / nosotras.",
        },
        {
            "kind": "text",
            "title": "Why these two together",
            "body": "**poder** is the modal 'can/be able' (puedo ir = I can go). **volver** means 'to come back' or 'to return'. Both are workhorses in spoken Spanish.",
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
        },
        {
            "kind": "mini_table",
            "title": "volver (to return)",
            "rows": [
            ["yo", "v|uelvo"],
            ["tú", "v|uelves"],
            ["él / ella / usted", "v|uelve"],
            ["nosotros / nosotras", "volv|emos"],
            ["ellos / ellas / ustedes", "v|uelven"],
            ],
        },
    ],
    "recall": [
        {"verb": "poder", "answers": {"yo": "p|uedo", "tú": "p|uedes", "él": "p|uede", "nosotros": "pod|emos", "ellos": "p|ueden"}},
        {"verb": "volver", "answers": {"yo": "v|uelvo", "tú": "v|uelves", "él": "v|uelve", "nosotros": "volv|emos", "ellos": "v|uelven"}},
    ],
}

PRESENT_O_UE_DORMIR_MORIR_INTRO = {
    "kind": "cards",
    "title": "Stem o→ue — dormir + morir",
    "cards": [
        {
            "kind": "text",
            "title": "dormir + morir",
            "body": "**dormir** (to sleep) and **morir** (to die) are the only two -ir o→ue stem-changers. Pattern: d**ue**rmo, m**ue**ro; nosotros stays unchanged (dormimos, morimos).",
        },
        {
            "kind": "text",
            "title": "Why these two together",
            "body": "Both share an extra quirk in the preterite (durmió, murió) — but in present they follow the standard o→ue pattern.",
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
        },
        {
            "kind": "mini_table",
            "title": "morir (to die)",
            "rows": [
            ["yo", "m|uero"],
            ["tú", "m|ueres"],
            ["él / ella / usted", "m|uere"],
            ["nosotros / nosotras", "mor|imos"],
            ["ellos / ellas / ustedes", "m|ueren"],
            ],
        },
    ],
    "recall": [
        {"verb": "dormir", "answers": {"yo": "d|uermo", "tú": "d|uermes", "él": "d|uerme", "nosotros": "dorm|imos", "ellos": "d|uermen"}},
        {"verb": "morir", "answers": {"yo": "m|uero", "tú": "m|ueres", "él": "m|uere", "nosotros": "mor|imos", "ellos": "m|ueren"}},
    ],
}

PRESENT_O_UE_MOVER_ALMORZAR_INTRO = {
    "kind": "cards",
    "title": "Stem o→ue — mover + almorzar",
    "cards": [
        {
            "kind": "text",
            "title": "mover + almorzar",
            "body": "**mover** (to move) and **almorzar** (to have lunch) follow the standard o→ue pattern. m**ue**vo, alm**ue**rzo; nosotros forms (movemos, almorzamos) stay regular.",
        },
        {
            "kind": "text",
            "title": "Why these two together",
            "body": "almorzar is built on **almuerzo** (the noun for 'lunch'). Many other -ar verbs follow this pattern: contar, encontrar, recordar.",
        },
        {
            "kind": "mini_table",
            "title": "mover (to move)",
            "rows": [
            ["yo", "m|uevo"],
            ["tú", "m|ueves"],
            ["él / ella / usted", "m|ueve"],
            ["nosotros / nosotras", "mov|emos"],
            ["ellos / ellas / ustedes", "m|ueven"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "almorzar (to have lunch)",
            "rows": [
            ["yo", "alm|uerzo"],
            ["tú", "alm|uerzas"],
            ["él / ella / usted", "alm|uerza"],
            ["nosotros / nosotras", "almorz|amos"],
            ["ellos / ellas / ustedes", "alm|uerzan"],
            ],
        },
    ],
    "recall": [
        {"verb": "mover", "answers": {"yo": "m|uevo", "tú": "m|ueves", "él": "m|ueve", "nosotros": "mov|emos", "ellos": "m|ueven"}},
        {"verb": "almorzar", "answers": {"yo": "alm|uerzo", "tú": "alm|uerzas", "él": "alm|uerza", "nosotros": "almorz|amos", "ellos": "alm|uerzan"}},
    ],
}

# ── From _gl7_output.py ──

PRESENT_E_IE_QUERER_PENSAR_INTRO = {
    "kind": "cards",
    "title": "Stem e→ie — querer + pensar",
    "cards": [
        {
            "kind": "text",
            "title": "querer + pensar",
            "body": "**e → ie** in stressed syllables: qu**ie**ro, p**ie**nso. Nosotros / nosotras stay regular (queremos, pensamos).",
        },
        {
            "kind": "text",
            "title": "Why these two together",
            "body": "**querer** is 'to want' (and 'to love' with people). **pensar** is 'to think' or 'to plan' (pienso ir = I plan to go).",
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
        },
    ],
    "recall": [
        {"verb": "querer", "answers": {"yo": "qu|iero", "tú": "qu|ieres", "él": "qu|iere", "nosotros": "quer|emos", "ellos": "qu|ieren"}},
        {"verb": "pensar", "answers": {"yo": "p|ienso", "tú": "p|iensas", "él": "p|iensa", "nosotros": "pens|amos", "ellos": "p|iensan"}},
    ],
}

PRESENT_E_IE_CERRAR_EMPEZAR_INTRO = {
    "kind": "cards",
    "title": "Stem e→ie — cerrar + empezar",
    "cards": [
        {
            "kind": "text",
            "title": "cerrar + empezar",
            "body": "Same e → ie pattern: c**ie**rro, emp**ie**zo. The **z** in empezar / empiezo is part of the stem; no spelling change needed in present tense.",
        },
        {
            "kind": "text",
            "title": "Why these two together",
            "body": "**cerrar** is 'to close' (a door, a deal). **empezar** is 'to begin'; followed by *a + infinitive* (empiezo a trabajar = I'm starting to work).",
        },
        {
            "kind": "mini_table",
            "title": "cerrar (to close)",
            "rows": [
            ["yo", "c|ierro"],
            ["tú", "c|ierras"],
            ["él / ella / usted", "c|ierra"],
            ["nosotros / nosotras", "cerr|amos"],
            ["ellos / ellas / ustedes", "c|ierran"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "empezar (to begin)",
            "rows": [
            ["yo", "emp|iezo"],
            ["tú", "emp|iezas"],
            ["él / ella / usted", "emp|ieza"],
            ["nosotros / nosotras", "empez|amos"],
            ["ellos / ellas / ustedes", "emp|iezan"],
            ],
        },
    ],
    "recall": [
        {"verb": "cerrar", "answers": {"yo": "c|ierro", "tú": "c|ierras", "él": "c|ierra", "nosotros": "cerr|amos", "ellos": "c|ierran"}},
        {"verb": "empezar", "answers": {"yo": "emp|iezo", "tú": "emp|iezas", "él": "emp|ieza", "nosotros": "empez|amos", "ellos": "emp|iezan"}},
    ],
}

PRESENT_E_IE_ENTENDER_PREFERIR_INTRO = {
    "kind": "cards",
    "title": "Stem e→ie — entender + preferir",
    "cards": [
        {
            "kind": "text",
            "title": "entender + preferir",
            "body": "Same e → ie pattern: ent**ie**ndo, pref**ie**ro. **preferir** is one of the few -ir verbs in this group; it shares the change with sentir, mentir.",
        },
        {
            "kind": "text",
            "title": "Why these two together",
            "body": "**entender** is 'to understand' (synonym: comprender). **preferir** takes a noun or an infinitive: prefiero el café, prefiero salir.",
        },
        {
            "kind": "mini_table",
            "title": "entender (to understand)",
            "rows": [
            ["yo", "ent|iendo"],
            ["tú", "ent|iendes"],
            ["él / ella / usted", "ent|iende"],
            ["nosotros / nosotras", "entend|emos"],
            ["ellos / ellas / ustedes", "ent|ienden"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "preferir (to prefer)",
            "rows": [
            ["yo", "pref|iero"],
            ["tú", "pref|ieres"],
            ["él / ella / usted", "pref|iere"],
            ["nosotros / nosotras", "prefer|imos"],
            ["ellos / ellas / ustedes", "pref|ieren"],
            ],
        },
    ],
    "recall": [
        {"verb": "entender", "answers": {"yo": "ent|iendo", "tú": "ent|iendes", "él": "ent|iende", "nosotros": "entend|emos", "ellos": "ent|ienden"}},
        {"verb": "preferir", "answers": {"yo": "pref|iero", "tú": "pref|ieres", "él": "pref|iere", "nosotros": "prefer|imos", "ellos": "pref|ieren"}},
    ],
}

# ── From _gl8_output.py ──

PRESENT_E_I_PEDIR_SERVIR_INTRO = {
    "kind": "cards",
    "title": "Stem e→i — pedir + servir",
    "cards": [
        {
            "kind": "text",
            "title": "pedir + servir",
            "body": "**e → i** in stressed syllables (only -ir verbs do this): p**i**do, s**i**rvo. Nosotros / nosotras stay regular (pedimos, servimos).",
        },
        {
            "kind": "text",
            "title": "Why these two together",
            "body": "**pedir** is 'to ask for' — used for ordering food, requesting things. **servir** is 'to serve' (food, a purpose).",
        },
        {
            "kind": "mini_table",
            "title": "pedir (to ask for/request)",
            "rows": [
            ["yo", "p|ido"],
            ["tú", "p|ides"],
            ["él / ella / usted", "p|ide"],
            ["nosotros / nosotras", "ped|imos"],
            ["ellos / ellas / ustedes", "p|iden"],
            ],
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
        },
    ],
    "recall": [
        {"verb": "pedir", "answers": {"yo": "p|ido", "tú": "p|ides", "él": "p|ide", "nosotros": "ped|imos", "ellos": "p|iden"}},
        {"verb": "servir", "answers": {"yo": "s|irvo", "tú": "s|irves", "él": "s|irve", "nosotros": "serv|imos", "ellos": "s|irven"}},
    ],
}

PRESENT_E_I_REPETIR_SEGUIR_INTRO = {
    "kind": "cards",
    "title": "Stem e→i — repetir + seguir",
    "cards": [
        {
            "kind": "text",
            "title": "repetir + seguir",
            "body": "Same e → i pattern: rep**i**to, s**i**go. **seguir** drops the **u** before -o/-a (yo sigo, not 'siguo') — same spelling rule we saw with conseguir.",
        },
        {
            "kind": "text",
            "title": "Why these two together",
            "body": "**repetir** is 'to repeat' (a word, an action). **seguir** is 'to follow' or 'to keep doing': sigo trabajando = I keep working.",
        },
        {
            "kind": "mini_table",
            "title": "repetir (to repeat)",
            "rows": [
            ["yo", "rep|ito"],
            ["tú", "rep|ites"],
            ["él / ella / usted", "rep|ite"],
            ["nosotros / nosotras", "repet|imos"],
            ["ellos / ellas / ustedes", "rep|iten"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "seguir (to follow)",
            "rows": [
            ["yo", "s|igo"],
            ["tú", "s|igues"],
            ["él / ella / usted", "s|igue"],
            ["nosotros / nosotras", "segu|imos"],
            ["ellos / ellas / ustedes", "s|iguen"],
            ],
        },
    ],
    "recall": [
        {"verb": "repetir", "answers": {"yo": "rep|ito", "tú": "rep|ites", "él": "rep|ite", "nosotros": "repet|imos", "ellos": "rep|iten"}},
        {"verb": "seguir", "answers": {"yo": "s|igo", "tú": "s|igues", "él": "s|igue", "nosotros": "segu|imos", "ellos": "s|iguen"}},
    ],
}

PRESENT_E_I_VESTIR_ELEGIR_INTRO = {
    "kind": "cards",
    "title": "Stem e→i — vestir + elegir",
    "cards": [
        {
            "kind": "text",
            "title": "vestir + elegir",
            "body": "Same e → i pattern: v**i**sto, el**i**jo. **elegir** changes **g → j** before -o (spelling-only): yo el**ijo**.",
        },
        {
            "kind": "text",
            "title": "Why these two together",
            "body": "**vestir** is 'to dress' (often reflexive: vestirse = to get dressed). **elegir** is 'to choose'.",
        },
        {
            "kind": "mini_table",
            "title": "vestir (to dress)",
            "rows": [
            ["yo", "v|isto"],
            ["tú", "v|istes"],
            ["él / ella / usted", "v|iste"],
            ["nosotros / nosotras", "vest|imos"],
            ["ellos / ellas / ustedes", "v|isten"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "elegir (to choose)",
            "rows": [
            ["yo", "el|ijo"],
            ["tú", "el|iges"],
            ["él / ella / usted", "el|ige"],
            ["nosotros / nosotras", "eleg|imos"],
            ["ellos / ellas / ustedes", "el|igen"],
            ],
        },
    ],
    "recall": [
        {"verb": "vestir", "answers": {"yo": "v|isto", "tú": "v|istes", "él": "v|iste", "nosotros": "vest|imos", "ellos": "v|isten"}},
        {"verb": "elegir", "answers": {"yo": "el|ijo", "tú": "el|iges", "él": "el|ige", "nosotros": "eleg|imos", "ellos": "el|igen"}},
    ],
}

# ── From _gl9_output.py ──

IR_A_INF_HABLAR_COMER_INTRO = {
    "kind": "cards",
    "title": "ir a + Infinitive — hablar + comer",
    "cards": [
        {
            "kind": "text",
            "title": "hablar + comer",
            "body": "**ir + a + infinitive** is the everyday Spanish 'going-to' future. Conjugate **ir** (voy, vas, va, vamos, van), add **a**, then any infinitive. *Voy a hablar* = I'm going to speak.",
        },
        {
            "kind": "text",
            "title": "What changes, what stays",
            "body": "This sub-block uses **hablar** (to speak) and **comer** (to eat) as the infinitives. The conjugated part — ir — is what you're learning to flex.",
        },
        {
            "kind": "mini_table",
            "title": "ir a + hablar (to speak)",
            "rows": [
            ["yo", "|voy a hablar"],
            ["tú", "|vas a hablar"],
            ["él / ella / usted", "|va a hablar"],
            ["nosotros / nosotras", "|vamos a hablar"],
            ["ellos / ellas / ustedes", "|van a hablar"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "ir a + comer (to eat)",
            "rows": [
            ["yo", "|voy a comer"],
            ["tú", "|vas a comer"],
            ["él / ella / usted", "|va a comer"],
            ["nosotros / nosotras", "|vamos a comer"],
            ["ellos / ellas / ustedes", "|van a comer"],
            ],
        },
    ],
    "recall": [
        {"verb": "hablar", "answers": {"yo": "|voy a hablar", "tú": "|vas a hablar", "él": "|va a hablar", "nosotros": "|vamos a hablar", "ellos": "|van a hablar"}},
        {"verb": "comer", "answers": {"yo": "|voy a comer", "tú": "|vas a comer", "él": "|va a comer", "nosotros": "|vamos a comer", "ellos": "|van a comer"}},
    ],
}

IR_A_INF_VIVIR_ESCRIBIR_INTRO = {
    "kind": "cards",
    "title": "ir a + Infinitive — vivir + escribir",
    "cards": [
        {
            "kind": "text",
            "title": "vivir + escribir",
            "body": "Same construction: **ir + a + infinitive**. Today we use **vivir** (to live) and **escribir** (to write) as the infinitives.",
        },
        {
            "kind": "text",
            "title": "What changes, what stays",
            "body": "Notice that the infinitive never changes — only **ir** flexes for the subject. The whole structure functions as a near-future tense.",
        },
        {
            "kind": "mini_table",
            "title": "ir a + vivir (to live)",
            "rows": [
            ["yo", "|voy a vivir"],
            ["tú", "|vas a vivir"],
            ["él / ella / usted", "|va a vivir"],
            ["nosotros / nosotras", "|vamos a vivir"],
            ["ellos / ellas / ustedes", "|van a vivir"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "ir a + escribir (to write)",
            "rows": [
            ["yo", "|voy a escribir"],
            ["tú", "|vas a escribir"],
            ["él / ella / usted", "|va a escribir"],
            ["nosotros / nosotras", "|vamos a escribir"],
            ["ellos / ellas / ustedes", "|van a escribir"],
            ],
        },
    ],
    "recall": [
        {"verb": "vivir", "answers": {"yo": "|voy a vivir", "tú": "|vas a vivir", "él": "|va a vivir", "nosotros": "|vamos a vivir", "ellos": "|van a vivir"}},
        {"verb": "escribir", "answers": {"yo": "|voy a escribir", "tú": "|vas a escribir", "él": "|va a escribir", "nosotros": "|vamos a escribir", "ellos": "|van a escribir"}},
    ],
}

IR_A_INF_DORMIR_ESTUDIAR_INTRO = {
    "kind": "cards",
    "title": "ir a + Infinitive — dormir + estudiar",
    "cards": [
        {
            "kind": "text",
            "title": "dormir + estudiar",
            "body": "Same construction with **dormir** (to sleep) and **estudiar** (to study). Even stem-changers like dormir keep their plain infinitive shape here — only **ir** flexes.",
        },
        {
            "kind": "text",
            "title": "What changes, what stays",
            "body": "ir + a + inf is more common in spoken Spanish than the simple future tense (hablaré). Drill it until it's automatic.",
        },
        {
            "kind": "mini_table",
            "title": "ir a + dormir (to sleep)",
            "rows": [
            ["yo", "|voy a dormir"],
            ["tú", "|vas a dormir"],
            ["él / ella / usted", "|va a dormir"],
            ["nosotros / nosotras", "|vamos a dormir"],
            ["ellos / ellas / ustedes", "|van a dormir"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "ir a + estudiar (to study)",
            "rows": [
            ["yo", "|voy a estudiar"],
            ["tú", "|vas a estudiar"],
            ["él / ella / usted", "|va a estudiar"],
            ["nosotros / nosotras", "|vamos a estudiar"],
            ["ellos / ellas / ustedes", "|van a estudiar"],
            ],
        },
    ],
    "recall": [
        {"verb": "dormir", "answers": {"yo": "|voy a dormir", "tú": "|vas a dormir", "él": "|va a dormir", "nosotros": "|vamos a dormir", "ellos": "|van a dormir"}},
        {"verb": "estudiar", "answers": {"yo": "|voy a estudiar", "tú": "|vas a estudiar", "él": "|va a estudiar", "nosotros": "|vamos a estudiar", "ellos": "|van a estudiar"}},
    ],
}

# ── From _gl13_5_output.py ──

IMPERATIVES_HABLAR_COMER_INTRO = {
    "kind": "cards",
    "title": "Imperatives — hablar + comer (regular tú)",
    "cards": [
        {
            "kind": "text",
            "title": "hablar + comer (regular tú)",
            "body": "**Affirmative imperative** = command form. For regular -ar verbs, the **tú** command swaps -ar → -a (habla = speak!). For -er/-ir, swap to -e (come = eat!).",
        },
        {
            "kind": "text",
            "title": "Beyond tú",
            "body": "Other commands (usted, nosotros, ustedes) use the subjunctive stem: hable, hablemos, hablen. We'll cover those alongside tú so you see the whole picture.",
        },
        {
            "kind": "mini_table",
            "title": "hablar (to speak)",
            "rows": [
            ["tú", "habl|a"],
            ["usted", "habl|e"],
            ["nosotros", "habl|emos"],
            ["ustedes", "habl|en"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "comer (to eat)",
            "rows": [
            ["tú", "com|e"],
            ["usted", "com|a"],
            ["nosotros", "com|amos"],
            ["ustedes", "com|an"],
            ],
        },
    ],
    "recall": [
        {"verb": "hablar", "answers": {"tú": "habl|a", "usted": "habl|e", "nosotros": "habl|emos", "ustedes": "habl|en"}},
        {"verb": "comer", "answers": {"tú": "com|e", "usted": "com|a", "nosotros": "com|amos", "ustedes": "com|an"}},
    ],
}

IMPERATIVES_TENER_VENIR_INTRO = {
    "kind": "cards",
    "title": "Imperatives — tener + venir (irregular tú)",
    "cards": [
        {
            "kind": "text",
            "title": "tener + venir (irregular tú)",
            "body": "Eight common verbs have **short irregular tú commands**: di, haz, ve, pon, sal, sé, ten, ven. Here we drill **ten** (have!) and **ven** (come!).",
        },
        {
            "kind": "text",
            "title": "Beyond tú",
            "body": "Outside tú, these verbs use the regular subjunctive stem: tenga, tengamos, tengan / venga, vengamos, vengan. The yo-go pattern shows up here too (tengo → tenga).",
        },
        {
            "kind": "mini_table",
            "title": "tener (to have)",
            "rows": [
            ["tú", "|ten"],
            ["usted", "ten|ga"],
            ["nosotros", "ten|gamos"],
            ["ustedes", "ten|gan"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "venir (to come)",
            "rows": [
            ["tú", "|ven"],
            ["usted", "ven|ga"],
            ["nosotros", "ven|gamos"],
            ["ustedes", "ven|gan"],
            ],
        },
    ],
    "recall": [
        {"verb": "tener", "answers": {"tú": "|ten", "usted": "ten|ga", "nosotros": "ten|gamos", "ustedes": "ten|gan"}},
        {"verb": "venir", "answers": {"tú": "|ven", "usted": "ven|ga", "nosotros": "ven|gamos", "ustedes": "ven|gan"}},
    ],
}

# ── From _gl17_output.py ──

PRETERITE_REGULAR_HABLAR_ENCONTRAR_INTRO = {
    "kind": "cards",
    "title": "Preterite Regular — hablar + encontrar (-ar)",
    "cards": [
        {
            "kind": "text",
            "title": "hablar + encontrar (-ar)",
            "body": "**Preterite** is the simple past for completed actions: 'I spoke,' 'I found.' For -ar verbs, the endings are **-é, -aste, -ó, -amos, -aron**. Note the accents on the yo and él forms.",
        },
        {
            "kind": "text",
            "title": "Notes",
            "body": "encontrar is normally an o→ue stem-changer in the present (encuentro), but in the preterite it stays regular: encontré, encontraste...",
        },
        {
            "kind": "mini_table",
            "title": "hablar (to speak)",
            "rows": [
            ["yo", "habl|é"],
            ["tú", "habl|aste"],
            ["él / ella / usted", "habl|ó"],
            ["nosotros / nosotras", "habl|amos"],
            ["ellos / ellas / ustedes", "habl|aron"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "encontrar (to find)",
            "rows": [
            ["yo", "encontr|é"],
            ["tú", "encontr|aste"],
            ["él / ella / usted", "encontr|ó"],
            ["nosotros / nosotras", "encontr|amos"],
            ["ellos / ellas / ustedes", "encontr|aron"],
            ],
        },
    ],
    "recall": [
        {"verb": "hablar", "answers": {"yo": "habl|é", "tú": "habl|aste", "él": "habl|ó", "nosotros": "habl|amos", "ellos": "habl|aron"}},
        {"verb": "encontrar", "answers": {"yo": "encontr|é", "tú": "encontr|aste", "él": "encontr|ó", "nosotros": "encontr|amos", "ellos": "encontr|aron"}},
    ],
}

PRETERITE_REGULAR_COMER_BEBER_INTRO = {
    "kind": "cards",
    "title": "Preterite Regular — comer + beber (-er)",
    "cards": [
        {
            "kind": "text",
            "title": "comer + beber (-er)",
            "body": "For regular -er verbs in the preterite, the endings are **-í, -iste, -ió, -imos, -ieron**. Like -ar, the yo and él forms carry an accent.",
        },
        {
            "kind": "text",
            "title": "Notes",
            "body": "These same endings are shared by regular -ir verbs (you'll see in the next sub-block).",
        },
        {
            "kind": "mini_table",
            "title": "comer (to eat)",
            "rows": [
            ["yo", "com|í"],
            ["tú", "com|iste"],
            ["él / ella / usted", "com|ió"],
            ["nosotros / nosotras", "com|imos"],
            ["ellos / ellas / ustedes", "com|ieron"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "beber (to drink)",
            "rows": [
            ["yo", "beb|í"],
            ["tú", "beb|iste"],
            ["él / ella / usted", "beb|ió"],
            ["nosotros / nosotras", "beb|imos"],
            ["ellos / ellas / ustedes", "beb|ieron"],
            ],
        },
    ],
    "recall": [
        {"verb": "comer", "answers": {"yo": "com|í", "tú": "com|iste", "él": "com|ió", "nosotros": "com|imos", "ellos": "com|ieron"}},
        {"verb": "beber", "answers": {"yo": "beb|í", "tú": "beb|iste", "él": "beb|ió", "nosotros": "beb|imos", "ellos": "beb|ieron"}},
    ],
}

PRETERITE_REGULAR_SALIR_UNIR_INTRO = {
    "kind": "cards",
    "title": "Preterite Regular — salir + unir (-ir)",
    "cards": [
        {
            "kind": "text",
            "title": "salir + unir (-ir)",
            "body": "Regular -ir verbs use the **same preterite endings as -er**: -í, -iste, -ió, -imos, -ieron. salí, saliste, salió...",
        },
        {
            "kind": "text",
            "title": "Notes",
            "body": "salir is yo-go in present (salgo) but completely regular in the preterite. unir is straightforward in both tenses.",
        },
        {
            "kind": "mini_table",
            "title": "salir (to leave/go out)",
            "rows": [
            ["yo", "sal|í"],
            ["tú", "sal|iste"],
            ["él / ella / usted", "sal|ió"],
            ["nosotros / nosotras", "sal|imos"],
            ["ellos / ellas / ustedes", "sal|ieron"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "unir (to unite/join)",
            "rows": [
            ["yo", "un|í"],
            ["tú", "un|iste"],
            ["él / ella / usted", "un|ió"],
            ["nosotros / nosotras", "un|imos"],
            ["ellos / ellas / ustedes", "un|ieron"],
            ],
        },
    ],
    "recall": [
        {"verb": "salir", "answers": {"yo": "sal|í", "tú": "sal|iste", "él": "sal|ió", "nosotros": "sal|imos", "ellos": "sal|ieron"}},
        {"verb": "unir", "answers": {"yo": "un|í", "tú": "un|iste", "él": "un|ió", "nosotros": "un|imos", "ellos": "un|ieron"}},
    ],
}

# ── From _gl17_1_output.py ──

PRETERITE_IRREGULAR_SER_IR_INTRO = {
    "kind": "cards",
    "title": "Preterite Highly Irregular — ser + ir (identical)",
    "cards": [
        {
            "kind": "text",
            "title": "ser + ir (identical)",
            "body": "In the preterite, **ser** and **ir** share the **exact same forms**: fui, fuiste, fue, fuimos, fueron. Context tells you which one. *Fui médico* = I was a doctor. *Fui al mercado* = I went to the market.",
        },
        {
            "kind": "text",
            "title": "Notes",
            "body": "These forms are the most common irregular preterites in Spanish — overlearn them.",
        },
        {
            "kind": "mini_table",
            "title": "ser (to be (identity))",
            "rows": [
            ["yo", "|fui"],
            ["tú", "|fuiste"],
            ["él / ella / usted", "|fue"],
            ["nosotros / nosotras", "|fuimos"],
            ["ellos / ellas / ustedes", "|fueron"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "ir (to go)",
            "rows": [
            ["yo", "|fui"],
            ["tú", "|fuiste"],
            ["él / ella / usted", "|fue"],
            ["nosotros / nosotras", "|fuimos"],
            ["ellos / ellas / ustedes", "|fueron"],
            ],
        },
    ],
    "recall": [
        {"verb": "ser", "answers": {"yo": "|fui", "tú": "|fuiste", "él": "|fue", "nosotros": "|fuimos", "ellos": "|fueron"}},
        {"verb": "ir", "answers": {"yo": "|fui", "tú": "|fuiste", "él": "|fue", "nosotros": "|fuimos", "ellos": "|fueron"}},
    ],
}

PRETERITE_IRREGULAR_DAR_VER_INTRO = {
    "kind": "cards",
    "title": "Preterite Highly Irregular — dar + ver",
    "cards": [
        {
            "kind": "text",
            "title": "dar + ver",
            "body": "**dar** is -ar but takes the -er/-ir preterite endings, with no accents: di, diste, dio, dimos, dieron. **ver** is -er, also no accents: vi, viste, vio, vimos, vieron.",
        },
        {
            "kind": "text",
            "title": "Notes",
            "body": "The accent-free yo and él forms (di, dio, vi, vio) are the giveaway here. Most other -ar / -er preterites carry accents (hablé, comí).",
        },
        {
            "kind": "mini_table",
            "title": "dar (to give)",
            "rows": [
            ["yo", "d|i"],
            ["tú", "d|iste"],
            ["él / ella / usted", "d|io"],
            ["nosotros / nosotras", "d|imos"],
            ["ellos / ellas / ustedes", "d|ieron"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "ver (to see)",
            "rows": [
            ["yo", "v|i"],
            ["tú", "v|iste"],
            ["él / ella / usted", "v|io"],
            ["nosotros / nosotras", "v|imos"],
            ["ellos / ellas / ustedes", "v|ieron"],
            ],
        },
    ],
    "recall": [
        {"verb": "dar", "answers": {"yo": "d|i", "tú": "d|iste", "él": "d|io", "nosotros": "d|imos", "ellos": "d|ieron"}},
        {"verb": "ver", "answers": {"yo": "v|i", "tú": "v|iste", "él": "v|io", "nosotros": "v|imos", "ellos": "v|ieron"}},
    ],
}

PRETERITE_IRREGULAR_HACER_DECIR_INTRO = {
    "kind": "cards",
    "title": "Preterite Highly Irregular — hacer + decir (strong stems)",
    "cards": [
        {
            "kind": "text",
            "title": "hacer + decir (strong stems)",
            "body": "Strong-stem preterites: **hacer** uses **hic-** (hizo with z to keep the soft sound). **decir** uses **dij-** with a special 3rd-plural ending **-eron** (not -ieron): dijeron.",
        },
        {
            "kind": "text",
            "title": "Notes",
            "body": "All strong-stem preterites share unaccented yo and él endings: -e, -iste, -o, -imos, -ieron / -eron. No accent on the yo!",
        },
        {
            "kind": "mini_table",
            "title": "hacer (to do/make)",
            "rows": [
            ["yo", "hic|e"],
            ["tú", "hic|iste"],
            ["él / ella / usted", "hiz|o"],
            ["nosotros / nosotras", "hic|imos"],
            ["ellos / ellas / ustedes", "hic|ieron"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "decir (to say)",
            "rows": [
            ["yo", "dij|e"],
            ["tú", "dij|iste"],
            ["él / ella / usted", "dij|o"],
            ["nosotros / nosotras", "dij|imos"],
            ["ellos / ellas / ustedes", "dij|eron"],
            ],
        },
    ],
    "recall": [
        {"verb": "hacer", "answers": {"yo": "hic|e", "tú": "hic|iste", "él": "hiz|o", "nosotros": "hic|imos", "ellos": "hic|ieron"}},
        {"verb": "decir", "answers": {"yo": "dij|e", "tú": "dij|iste", "él": "dij|o", "nosotros": "dij|imos", "ellos": "dij|eron"}},
    ],
}

PRETERITE_IRREGULAR_TRAER_DORMIR_INTRO = {
    "kind": "cards",
    "title": "Preterite Highly Irregular — traer + dormir",
    "cards": [
        {
            "kind": "text",
            "title": "traer + dormir",
            "body": "**traer** is strong-stem **traj-** with the special **-eron** ending in 3rd plural: trajeron. **dormir** is mostly regular but **o → u** in 3rd-person forms: durmió, durmieron.",
        },
        {
            "kind": "text",
            "title": "Notes",
            "body": "The 3rd-person stem shift in dormir / morir mirrors what they do in the gerund (durmiendo, muriendo) — same trick.",
        },
        {
            "kind": "mini_table",
            "title": "traer (to bring)",
            "rows": [
            ["yo", "traj|e"],
            ["tú", "traj|iste"],
            ["él / ella / usted", "traj|o"],
            ["nosotros / nosotras", "traj|imos"],
            ["ellos / ellas / ustedes", "traj|eron"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "dormir (to sleep)",
            "rows": [
            ["yo", "dorm|í"],
            ["tú", "dorm|iste"],
            ["él / ella / usted", "d|urmió"],
            ["nosotros / nosotras", "dorm|imos"],
            ["ellos / ellas / ustedes", "d|urmieron"],
            ],
        },
    ],
    "recall": [
        {"verb": "traer", "answers": {"yo": "traj|e", "tú": "traj|iste", "él": "traj|o", "nosotros": "traj|imos", "ellos": "traj|eron"}},
        {"verb": "dormir", "answers": {"yo": "dorm|í", "tú": "dorm|iste", "él": "d|urmió", "nosotros": "dorm|imos", "ellos": "d|urmieron"}},
    ],
}

# ── From _gl18_output.py ──

GERUND_HABLAR_CAMINAR_INTRO = {
    "kind": "cards",
    "title": "Gerund / Present Progressive — hablar + caminar (-ar)",
    "cards": [
        {
            "kind": "text",
            "title": "hablar + caminar (-ar)",
            "body": "**Present progressive** = estar + gerund: 'estoy hablando' (I am speaking). For -ar verbs, the gerund ending is **-ando**: hablando, caminando.",
        },
        {
            "kind": "text",
            "title": "Notes",
            "body": "Spanish uses the progressive less often than English. Use it for actions happening *right now* or in a vivid moment, not for general habits.",
        },
        {
            "kind": "mini_table",
            "title": "hablar (to speak) — present progressive",
            "rows": [
            ["yo", "est|oy hablando"],
            ["tú", "est|ás hablando"],
            ["él / ella / usted", "est|á hablando"],
            ["nosotros / nosotras", "est|amos hablando"],
            ["ellos / ellas / ustedes", "est|án hablando"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "caminar (to walk) — present progressive",
            "rows": [
            ["yo", "est|oy caminando"],
            ["tú", "est|ás caminando"],
            ["él / ella / usted", "est|á caminando"],
            ["nosotros / nosotras", "est|amos caminando"],
            ["ellos / ellas / ustedes", "est|án caminando"],
            ],
        },
    ],
    "recall": [
        {"verb": "hablar", "answers": {"yo": "est|oy hablando", "tú": "est|ás hablando", "él": "est|á hablando", "nosotros": "est|amos hablando", "ellos": "est|án hablando"}},
        {"verb": "caminar", "answers": {"yo": "est|oy caminando", "tú": "est|ás caminando", "él": "est|á caminando", "nosotros": "est|amos caminando", "ellos": "est|án caminando"}},
    ],
}

GERUND_COMER_BEBER_INTRO = {
    "kind": "cards",
    "title": "Gerund / Present Progressive — comer + beber (-er)",
    "cards": [
        {
            "kind": "text",
            "title": "comer + beber (-er)",
            "body": "For regular -er verbs, the gerund ending is **-iendo**: comiendo, bebiendo. estar still flexes for the subject (estoy comiendo, estás bebiendo).",
        },
        {
            "kind": "text",
            "title": "Notes",
            "body": "The -iendo ending is shared with regular -ir verbs (next sub-block).",
        },
        {
            "kind": "mini_table",
            "title": "comer (to eat) — present progressive",
            "rows": [
            ["yo", "est|oy comiendo"],
            ["tú", "est|ás comiendo"],
            ["él / ella / usted", "est|á comiendo"],
            ["nosotros / nosotras", "est|amos comiendo"],
            ["ellos / ellas / ustedes", "est|án comiendo"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "beber (to drink) — present progressive",
            "rows": [
            ["yo", "est|oy bebiendo"],
            ["tú", "est|ás bebiendo"],
            ["él / ella / usted", "est|á bebiendo"],
            ["nosotros / nosotras", "est|amos bebiendo"],
            ["ellos / ellas / ustedes", "est|án bebiendo"],
            ],
        },
    ],
    "recall": [
        {"verb": "comer", "answers": {"yo": "est|oy comiendo", "tú": "est|ás comiendo", "él": "est|á comiendo", "nosotros": "est|amos comiendo", "ellos": "est|án comiendo"}},
        {"verb": "beber", "answers": {"yo": "est|oy bebiendo", "tú": "est|ás bebiendo", "él": "est|á bebiendo", "nosotros": "est|amos bebiendo", "ellos": "est|án bebiendo"}},
    ],
}

GERUND_SALIR_INHIBIR_INTRO = {
    "kind": "cards",
    "title": "Gerund / Present Progressive — salir + inhibir (-ir)",
    "cards": [
        {
            "kind": "text",
            "title": "salir + inhibir (-ir)",
            "body": "Regular -ir verbs use the same **-iendo** ending: saliendo, inhibiendo.",
        },
        {
            "kind": "text",
            "title": "Notes",
            "body": "Some -ir verbs have stem changes in the gerund (durmiendo, pidiendo, sintiendo) — but salir and inhibir are regular here.",
        },
        {
            "kind": "mini_table",
            "title": "salir (to leave/go out) — present progressive",
            "rows": [
            ["yo", "est|oy saliendo"],
            ["tú", "est|ás saliendo"],
            ["él / ella / usted", "est|á saliendo"],
            ["nosotros / nosotras", "est|amos saliendo"],
            ["ellos / ellas / ustedes", "est|án saliendo"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "inhibir (to inhibit) — present progressive",
            "rows": [
            ["yo", "est|oy inhibiendo"],
            ["tú", "est|ás inhibiendo"],
            ["él / ella / usted", "est|á inhibiendo"],
            ["nosotros / nosotras", "est|amos inhibiendo"],
            ["ellos / ellas / ustedes", "est|án inhibiendo"],
            ],
        },
    ],
    "recall": [
        {"verb": "salir", "answers": {"yo": "est|oy saliendo", "tú": "est|ás saliendo", "él": "est|á saliendo", "nosotros": "est|amos saliendo", "ellos": "est|án saliendo"}},
        {"verb": "inhibir", "answers": {"yo": "est|oy inhibiendo", "tú": "est|ás inhibiendo", "él": "est|á inhibiendo", "nosotros": "est|amos inhibiendo", "ellos": "est|án inhibiendo"}},
    ],
}

# ── From _gl18_5_output.py ──

PERFECT_TENSES_PRESENT_INTRO = {
    "kind": "cards",
    "title": "Perfect Tenses — present perfect (hablar + comer)",
    "cards": [
        {
            "kind": "text",
            "title": "present perfect (hablar + comer)",
            "body": "**Present perfect** = haber-present + past participle: 'he hablado' (I have spoken). The endings of haber are: he, has, ha, hemos, han.",
        },
        {
            "kind": "text",
            "title": "Notes",
            "body": "Past participles for regular verbs: -ar → -ado (hablado), -er/-ir → -ido (comido, vivido). They never agree in gender or number when used with haber.",
        },
        {
            "kind": "mini_table",
            "title": "hablar (to speak)",
            "rows": [
            ["yo", "|he hablado"],
            ["tú", "|has hablado"],
            ["él / ella / usted", "|ha hablado"],
            ["nosotros / nosotras", "|hemos hablado"],
            ["ellos / ellas / ustedes", "|han hablado"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "comer (to eat)",
            "rows": [
            ["yo", "|he comido"],
            ["tú", "|has comido"],
            ["él / ella / usted", "|ha comido"],
            ["nosotros / nosotras", "|hemos comido"],
            ["ellos / ellas / ustedes", "|han comido"],
            ],
        },
    ],
    "recall": [
        {"verb": "hablar", "answers": {"yo": "|he hablado", "tú": "|has hablado", "él": "|ha hablado", "nosotros": "|hemos hablado", "ellos": "|han hablado"}},
        {"verb": "comer", "answers": {"yo": "|he comido", "tú": "|has comido", "él": "|ha comido", "nosotros": "|hemos comido", "ellos": "|han comido"}},
    ],
}

PERFECT_TENSES_PLUPERFECT_INTRO = {
    "kind": "cards",
    "title": "Perfect Tenses — pluperfect (hablar + vivir)",
    "cards": [
        {
            "kind": "text",
            "title": "pluperfect (hablar + vivir)",
            "body": "**Pluperfect** = haber-imperfect + past participle: 'había hablado' (I had spoken). The endings: había, habías, había, habíamos, habían.",
        },
        {
            "kind": "text",
            "title": "Notes",
            "body": "Use the pluperfect for actions that happened *before* another past action: 'cuando llegué, ya había comido' (when I arrived, I had already eaten).",
        },
        {
            "kind": "mini_table",
            "title": "hablar (to speak)",
            "rows": [
            ["yo", "|había hablado"],
            ["tú", "|habías hablado"],
            ["él / ella / usted", "|había hablado"],
            ["nosotros / nosotras", "|habíamos hablado"],
            ["ellos / ellas / ustedes", "|habían hablado"],
            ],
        },
        {
            "kind": "mini_table",
            "title": "vivir (to live)",
            "rows": [
            ["yo", "|había vivido"],
            ["tú", "|habías vivido"],
            ["él / ella / usted", "|había vivido"],
            ["nosotros / nosotras", "|habíamos vivido"],
            ["ellos / ellas / ustedes", "|habían vivido"],
            ],
        },
    ],
    "recall": [
        {"verb": "hablar", "answers": {"yo": "|había hablado", "tú": "|habías hablado", "él": "|había hablado", "nosotros": "|habíamos hablado", "ellos": "|habían hablado"}},
        {"verb": "vivir", "answers": {"yo": "|había vivido", "tú": "|habías vivido", "él": "|había vivido", "nosotros": "|habíamos vivido", "ellos": "|habían vivido"}},
    ],
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
        "drill_sentences": [
            {"en": "I am tall", "es": "Yo soy alto", "noun_id": None, "type": "written",
             "glosses": {"am": "soy", "soy": "am", "tall": "alto", "alto": "tall"}},
            {"en": "You are a tourist", "es": "Tú eres turista", "noun_id": None, "type": "auditory",
             "glosses": {"are": "eres", "eres": "are", "tourist": "turista", "turista": "tourist"}},
            {"en": "He is important", "es": "Él es importante", "noun_id": None, "type": "written",
             "glosses": {"is": "es", "es": "is", "important": "importante", "importante": "important"}},
            {"en": "She is elegant", "es": "Ella es elegante", "noun_id": None, "type": "auditory",
             "glosses": {"is": "es", "es": "is", "elegant": "elegante", "elegante": "elegant"}},
            {"en": "You are professional", "es": "Usted es profesional", "noun_id": None, "type": "written",
             "glosses": {"are": "es", "es": "are", "professional": "profesional", "profesional": "professional"}},
            {"en": "I am sociable", "es": "Yo soy social", "noun_id": None, "type": "auditory",
             "glosses": {"am": "soy", "soy": "am", "sociable": "social", "social": "sociable"}},
            {"en": "You are international", "es": "Tú eres internacional", "noun_id": None, "type": "written",
             "glosses": {"are": "eres", "eres": "are", "international": "internacional", "internacional": "international"}},
            {"en": "He is sociable", "es": "Él es social", "noun_id": None, "type": "auditory",
             "glosses": {"is": "es", "es": "is", "sociable": "social", "social": "sociable"}},
            {"en": "She is important", "es": "Ella es importante", "noun_id": None, "type": "written",
             "glosses": {"is": "es", "es": "is", "important": "importante", "importante": "important"}},
            {"en": "You are likeable", "es": "Usted es simpático", "noun_id": None, "type": "auditory",
             "glosses": {"are": "es", "es": "are", "likeable": "simpático", "simpático": "likeable"}},
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
        "drill_sentences": [
            {"en": "We (m) are Colombian", "es": "Nosotros somos colombianos", "noun_id": None, "type": "written",
             "glosses": {"are": "somos", "somos": "are", "Colombian": "colombianos", "colombianos": "Colombian"}},
            {"en": "We (f) are Latin", "es": "Nosotras somos latinas", "noun_id": None, "type": "auditory",
             "glosses": {"are": "somos", "somos": "are", "Latin": "latinas", "latinas": "Latin"}},
            {"en": "They (m) are sociable", "es": "Ellos son sociales", "noun_id": None, "type": "written",
             "glosses": {"are": "son", "son": "are", "sociable": "sociales", "sociales": "sociable"}},
            {"en": "They (f) are professional", "es": "Ellas son profesionales", "noun_id": None, "type": "auditory",
             "glosses": {"are": "son", "son": "are", "professional": "profesionales", "profesionales": "professional"}},
            {"en": "You all are tourists", "es": "Ustedes son turistas", "noun_id": None, "type": "written",
             "glosses": {"are": "son", "son": "are", "tourists": "turistas", "turistas": "tourists"}},
            {"en": "We (m) are important", "es": "Nosotros somos importantes", "noun_id": None, "type": "auditory",
             "glosses": {"are": "somos", "somos": "are", "important": "importantes", "importantes": "important"}},
            {"en": "We (f) are international", "es": "Nosotras somos internacionales", "noun_id": None, "type": "written",
             "glosses": {"are": "somos", "somos": "are", "international": "internacionales", "internacionales": "international"}},
            {"en": "They (m) are likeable", "es": "Ellos son simpáticos", "noun_id": None, "type": "auditory",
             "glosses": {"are": "son", "son": "are", "likeable": "simpáticos", "simpáticos": "likeable"}},
            {"en": "They (f) are elegant", "es": "Ellas son elegantes", "noun_id": None, "type": "written",
             "glosses": {"are": "son", "son": "are", "elegant": "elegantes", "elegantes": "elegant"}},
            {"en": "You all are tall", "es": "Ustedes son altos", "noun_id": None, "type": "auditory",
             "glosses": {"are": "son", "son": "are", "tall": "altos", "altos": "tall"}},
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
        "title": "Possessive Adjectives",
        "grammar_level": 1.5,
        "lesson_number": 1,
        "lesson_type": "rule",
        "word_workload": ["mi", "tu", "su", "nuestro", "nuestra", "mis", "tus", "sus", "nuestros", "nuestras"],
        "video_embed_id": None,
        "drill_type": "rule",
        "tense": "possessive",
        "intro_chart": POSSESSIVE_ADJ_INTRO,
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "drill_sentences": [
            {"en": 'our (m) names', "es": 'nuestros nombres', "noun_id": 'nombre', "type": 'auditory', "glosses": {'names': 'nombres', 'nombres': 'names'}},
            {"en": 'our (f) family', "es": 'nuestra familia', "noun_id": 'familia', "type": 'auditory', "glosses": {'family': 'familia', 'familia': 'family'}},
            {"en": 'my houses', "es": 'mis casas', "noun_id": 'casa', "type": 'auditory', "glosses": {'houses': 'casas', 'casas': 'houses'}},
            {"en": 'my book', "es": 'mi libro', "noun_id": 'libro', "type": 'auditory', "glosses": {'book': 'libro', 'libro': 'book'}},
            {"en": 'his car', "es": 'su carro', "noun_id": 'carro', "type": 'written', "glosses": {'car': 'carro', 'carro': 'car'}},
            {"en": 'our (f) families', "es": 'nuestras familias', "noun_id": 'familia', "type": 'auditory', "glosses": {'families': 'familias', 'familias': 'families'}},
            {"en": 'her work', "es": 'su trabajo', "noun_id": 'trabajo', "type": 'auditory', "glosses": {'work': 'trabajo', 'trabajo': 'work'}},
            {"en": 'my house', "es": 'mi casa', "noun_id": 'casa', "type": 'written', "glosses": {'house': 'casa', 'casa': 'house'}},
            {"en": 'their plans', "es": 'sus planes', "noun_id": 'plan', "type": 'auditory', "glosses": {'plans': 'planes', 'planes': 'plans'}},
            {"en": 'our (m) dogs', "es": 'nuestros perros', "noun_id": 'perro', "type": 'written', "glosses": {'dogs': 'perros', 'perros': 'dogs'}},
            {"en": 'your friends', "es": 'tus amigos', "noun_id": 'amigo', "type": 'auditory', "glosses": {'friends': 'amigos', 'amigos': 'friends'}},
            {"en": 'your friend', "es": 'tu amigo', "noun_id": 'amigo', "type": 'auditory', "glosses": {'friend': 'amigo', 'amigo': 'friend'}},
            {"en": 'my books', "es": 'mis libros', "noun_id": 'libro', "type": 'written', "glosses": {'books': 'libros', 'libros': 'books'}},
            {"en": 'your name', "es": 'tu nombre', "noun_id": 'nombre', "type": 'written', "glosses": {'name': 'nombre', 'nombre': 'name'}},
            {"en": 'our (f) city', "es": 'nuestra ciudad', "noun_id": 'ciudad', "type": 'written', "glosses": {'city': 'ciudad', 'ciudad': 'city'}},
            {"en": 'our (f) cities', "es": 'nuestras ciudades', "noun_id": 'ciudad', "type": 'written', "glosses": {'cities': 'ciudades', 'ciudades': 'cities'}},
            {"en": 'your works', "es": 'tus trabajos', "noun_id": 'trabajo', "type": 'written', "glosses": {'works': 'trabajos', 'trabajos': 'works'}},
            {"en": 'our (m) dog', "es": 'nuestro perro', "noun_id": 'perro', "type": 'written', "glosses": {'dog': 'perro', 'perro': 'dog'}},
            {"en": 'our (m) plan', "es": 'nuestro plan', "noun_id": 'plan', "type": 'auditory', "glosses": {'plan': 'plan'}},
            {"en": 'their cars', "es": 'sus carros', "noun_id": 'carro', "type": 'written', "glosses": {'cars': 'carros', 'carros': 'cars'}},
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
                    "title": "What do un / una / unos / unas mean?",
                    "body": "**un / una** means \"a\" (singular) — *un libro* = \"a book\", *una casa* = \"a house\".\n\n**unos / unas** means \"some\" (plural) — *unos libros* = \"some books\", *unas casas* = \"some houses\".",
                },
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
            {"en": "I listen to the radio", "es": "Yo escucho la radio", "noun_id": None, "type": "auditory",
             "glosses": {"radio": "radio"}},
            {"en": "You listen to music", "es": "Tú escuchas música", "noun_id": None, "type": "written",
             "glosses": {"music": "música", "música": "music"}},
            {"en": "He listens to the song", "es": "Él escucha la canción", "noun_id": None, "type": "auditory",
             "glosses": {"song": "canción", "canción": "song"}},
            {"en": "We (m) listen carefully", "es": "Nosotros escuchamos atentamente", "noun_id": None, "type": "written",
             "glosses": {"carefully": "atentamente", "atentamente": "carefully"}},
            {"en": "They (f) listen to the news", "es": "Ellas escuchan la noticia", "noun_id": None, "type": "auditory",
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
        "intro_chart": {'kind': 'cards', 'title': 'Regular present — -AR verbs', 'cards': [{'kind': 'text', 'title': 'Verbs change to match who', 'body': 'In Spanish, the verb itself tells you who is doing the action. The infinitive form (the dictionary form, like *hablar* — to speak) drops its ending and gets a new one based on the subject.'}, {'kind': 'text', 'title': 'Three families: -ar, -er, -ir — starting with -ar', 'body': "Every Spanish infinitive ends in **-ar**, **-er**, or **-ir**. Each family takes its own endings. We'll start with the most common: **-ar** verbs (hablar, escuchar, cantar, trabajar…)."}, {'kind': 'mini_table', 'title': 'cantar (to sing)', 'rows': [['yo', 'cant|o'], ['tú', 'cant|as'], ['él / ella / usted', 'cant|a'], ['nosotros / nosotras', 'cant|amos'], ['ellos / ellas / ustedes', 'cant|an']]}, {'kind': 'mini_table', 'title': 'escuchar (to listen)', 'rows': [['yo', 'escuch|o'], ['tú', 'escuch|as'], ['él / ella / usted', 'escuch|a'], ['nosotros / nosotras', 'escuch|amos'], ['ellos / ellas / ustedes', 'escuch|an']]}], 'recall': [{'verb': 'cantar', 'answers': {'yo': 'cant|o', 'tú': 'cant|as', 'él': 'cant|a', 'nosotros': 'cant|amos', 'ellos': 'cant|an'}}, {'verb': 'escuchar', 'answers': {'yo': 'escuch|o', 'tú': 'escuch|as', 'él': 'escuch|a', 'nosotros': 'escuch|amos', 'ellos': 'escuch|an'}}]},
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
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
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
            {"en": "They (m) sing a song", "es": "Ellos cantan una canción", "noun_id": None, "type": "written",
             "glosses": {"song": "canción", "canción": "song"}},
            {"en": "I listen attentively", "es": "Yo escucho atentamente", "noun_id": None, "type": "auditory",
             "glosses": {"attentively": "atentamente", "atentamente": "attentively"}},
            {"en": "You listen to the news", "es": "Tú escuchas la noticia", "noun_id": None, "type": "written",
             "glosses": {"news": "noticia", "noticia": "news"}},
            {"en": "He listens to his teacher", "es": "Él escucha a su maestro", "noun_id": None, "type": "auditory",
             "glosses": {"teacher": "maestro", "maestro": "teacher"}},
            {"en": "We (m) listen to the music", "es": "Nosotros escuchamos la música", "noun_id": None, "type": "written",
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
            {"en": "They (m) drink milk", "es": "Ellos beben leche", "noun_id": None, "type": "written",
             "glosses": {"milk": "leche", "leche": "milk"}},
            {"en": "I eat fruit", "es": "Yo como fruta", "noun_id": None, "type": "auditory",
             "glosses": {"fruit": "fruta", "fruta": "fruit"}},
            {"en": "You eat bread", "es": "Tú comes pan", "noun_id": None, "type": "written",
             "glosses": {"bread": "pan", "pan": "bread"}},
            {"en": "He eats meat", "es": "Él come carne", "noun_id": None, "type": "auditory",
             "glosses": {"meat": "carne", "carne": "meat"}},
            {"en": "We (m) eat together", "es": "Nosotros comemos juntos", "noun_id": None, "type": "written",
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
        "intro_chart": {'kind': 'cards', 'title': 'Regular present — -ER verbs', 'cards': [{'kind': 'text', 'title': 'Now: -er verbs', 'body': 'You already know the -ar pattern. -er verbs (beber, comer, leer, aprender…) work the same way — drop the ending, add a new one — but the endings are different.'}, {'kind': 'mini_table', 'title': 'leer (to read)', 'rows': [['yo', 'le|o'], ['tú', 'le|es'], ['él / ella / usted', 'le|e'], ['nosotros / nosotras', 'le|emos'], ['ellos / ellas / ustedes', 'le|en']]}, {'kind': 'mini_table', 'title': 'comer (to eat)', 'rows': [['yo', 'com|o'], ['tú', 'com|es'], ['él / ella / usted', 'com|e'], ['nosotros / nosotras', 'com|emos'], ['ellos / ellas / ustedes', 'com|en']]}], 'recall': [{'verb': 'leer', 'answers': {'yo': 'le|o', 'tú': 'le|es', 'él': 'le|e', 'nosotros': 'le|emos', 'ellos': 'le|en'}}, {'verb': 'comer', 'answers': {'yo': 'com|o', 'tú': 'com|es', 'él': 'com|e', 'nosotros': 'com|emos', 'ellos': 'com|en'}}]},
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
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
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
            {"en": "They (m) read fast", "es": "Ellos leen rápido", "noun_id": None, "type": "written",
             "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "I eat at home", "es": "Yo como en casa", "noun_id": None, "type": "auditory",
             "glosses": {"home": "casa", "casa": "home"}},
            {"en": "You eat fish", "es": "Tú comes pescado", "noun_id": None, "type": "written",
             "glosses": {"fish": "pescado", "pescado": "fish"}},
            {"en": "He eats vegetables", "es": "Él come verduras", "noun_id": None, "type": "auditory",
             "glosses": {"vegetables": "verduras", "verduras": "vegetables"}},
            {"en": "We (m) eat early", "es": "Nosotros comemos temprano", "noun_id": None, "type": "written",
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
            {"en": "They (m) live in the city", "es": "Ellos viven en la ciudad", "noun_id": None, "type": "written",
             "glosses": {"city": "ciudad", "ciudad": "city"}},
            {"en": "I write a letter", "es": "Yo escribo una carta", "noun_id": None, "type": "auditory",
             "glosses": {"letter": "carta", "carta": "letter"}},
            {"en": "You write well", "es": "Tú escribes bien", "noun_id": None, "type": "written",
             "glosses": {"well": "bien", "bien": "well"}},
            {"en": "He writes a book", "es": "Él escribe un libro", "noun_id": "libro", "type": "auditory",
             "glosses": {"book": "libro", "libro": "book"}},
            {"en": "We (m) write messages", "es": "Nosotros escribimos mensajes", "noun_id": None, "type": "written",
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
        "intro_chart": {'kind': 'cards', 'title': 'Regular present — -IR verbs', 'cards': [{'kind': 'text', 'title': 'Last family: -ir verbs', 'body': '-ir verbs (vivir, escribir, abrir, recibir…) share almost every ending with -er. The only difference is the *nosotros* form: -er says **-emos**, -ir says **-imos**.'}, {'kind': 'mini_table', 'title': 'abrir (to open)', 'rows': [['yo', 'abr|o'], ['tú', 'abr|es'], ['él / ella / usted', 'abr|e'], ['nosotros / nosotras', 'abr|imos'], ['ellos / ellas / ustedes', 'abr|en']]}, {'kind': 'mini_table', 'title': 'vivir (to live)', 'rows': [['yo', 'viv|o'], ['tú', 'viv|es'], ['él / ella / usted', 'viv|e'], ['nosotros / nosotras', 'viv|imos'], ['ellos / ellas / ustedes', 'viv|en']]}], 'recall': [{'verb': 'abrir', 'answers': {'yo': 'abr|o', 'tú': 'abr|es', 'él': 'abr|e', 'nosotros': 'abr|imos', 'ellos': 'abr|en'}}, {'verb': 'vivir', 'answers': {'yo': 'viv|o', 'tú': 'viv|es', 'él': 'viv|e', 'nosotros': 'viv|imos', 'ellos': 'viv|en'}}]},
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
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
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
            {"en": "They (m) open the gift", "es": "Ellos abren el regalo", "noun_id": None, "type": "written",
             "glosses": {"gift": "regalo", "regalo": "gift"}},
            {"en": "I live in the country", "es": "Yo vivo en el campo", "noun_id": None, "type": "auditory",
             "glosses": {"country": "campo", "campo": "country"}},
            {"en": "You live alone", "es": "Tú vives solo", "noun_id": None, "type": "written",
             "glosses": {"alone": "solo", "solo": "alone"}},
            {"en": "He lives far away", "es": "Él vive lejos", "noun_id": None, "type": "auditory",
             "glosses": {"far away": "lejos", "lejos": "far away"}},
            {"en": "We (m) live in an apartment", "es": "Nosotros vivimos en un apartamento", "noun_id": None, "type": "written",
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
    # --- GL 4: Irregular Present I — split into 3 sub-blocks of 2 verbs each ---
    # Each sub-block is 2 drills + 1 chat. Sequence: ser+estar (1, 2, 2.5) →
    # ir+dar (3, 4, 4.5) → tener+venir (5, 6, 6.5).
    #
    # RETIRED 2026-05-02 — replaced by the per-pair sub-blocks below:
    #   grammar_irregular_present_1, _1_chat, _2, _2_chat, _3, _3_chat
    # These IDs are intentionally absent from GRAMMAR_SITUATIONS so the
    # dashboard's "next lesson" pointer skips them. DB rows referencing them
    # are untouched (per the "never change situation IDs" rule);
    # get_grammar_config() returns None for unknown IDs and the FE handles
    # None as "no active lesson".

    "grammar_irregular_present_ser_estar_1": {
        "title": "Irregular Present — ser + estar (1/2)",
        "grammar_level": 4,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ["ser", "estar"],
        "video_embed_id": "6jpCj97AHMN",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": IRREGULAR_PRESENT_SER_ESTAR_INTRO,
        "drill_config": {
            "answers": {
                "ser": {"yo": "|soy", "tú": "|eres", "él": "|es", "ella": "|es", "usted": "|es", "nosotros": "|somos", "nosotras": "|somos", "ellos": "|son", "ellas": "|son", "ustedes": "|son"},
                "estar": {"yo": "est|oy", "tú": "est|ás", "él": "est|á", "ella": "est|á", "usted": "est|á", "nosotros": "est|amos", "nosotras": "est|amos", "ellos": "est|án", "ellas": "est|án", "ustedes": "est|án"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": 'We (m) are friends', "es": 'Nosotros somos amigos', "noun_id": None, "type": 'auditory', "glosses": {'friends': 'amigos', 'amigos': 'friends'}},
            {"en": 'They (f) are teachers', "es": 'Ellas son profesoras', "noun_id": None, "type": 'written', "glosses": {'teachers': 'profesoras', 'profesoras': 'teachers'}},
            {"en": 'You are tired', "es": 'Tú estás cansado', "noun_id": None, "type": 'auditory', "glosses": {'tired': 'cansado', 'cansado': 'tired'}},
            {"en": 'We (f) are here', "es": 'Nosotras estamos aquí', "noun_id": None, "type": 'auditory', "glosses": {'here': 'aquí', 'aquí': 'here'}},
            {"en": 'I am tall', "es": 'Yo soy alto', "noun_id": None, "type": 'auditory', "glosses": {'tall': 'alto', 'alto': 'tall'}},
            {"en": 'I am a teacher', "es": 'Yo soy profesora', "noun_id": None, "type": 'written', "glosses": {'teacher': 'profesora', 'profesora': 'teacher'}},
            {"en": 'You are happy', "es": 'Tú estás feliz', "noun_id": None, "type": 'written', "glosses": {'happy': 'feliz', 'feliz': 'happy'}},
            {"en": 'We (f) are here', "es": 'Nosotras estamos aquí', "noun_id": None, "type": 'auditory', "glosses": {'here': 'aquí', 'aquí': 'here'}},
            {"en": 'You all are doctors', "es": 'Ustedes son doctores', "noun_id": None, "type": 'written', "glosses": {'doctors': 'doctores', 'doctores': 'doctors'}},
            {"en": 'He is a doctor', "es": 'Él es doctor', "noun_id": None, "type": 'written', "glosses": {'doctor': 'doctor'}},
            {"en": 'You all are busy', "es": 'Ustedes están ocupados', "noun_id": None, "type": 'written', "glosses": {'busy': 'ocupados', 'ocupados': 'busy'}},
            {"en": 'You are tall', "es": 'Tú eres alto', "noun_id": None, "type": 'auditory', "glosses": {'tall': 'alto', 'alto': 'tall'}},
            {"en": 'We (f) are friends', "es": 'Nosotras somos amigas', "noun_id": None, "type": 'auditory', "glosses": {'friends': 'amigas', 'amigas': 'friends'}},
            {"en": 'I am at home', "es": 'Yo estoy en casa', "noun_id": None, "type": 'auditory', "glosses": {'home': 'casa', 'casa': 'home'}},
            {"en": 'They (f) are busy', "es": 'Ellas están ocupadas', "noun_id": None, "type": 'written', "glosses": {'busy': 'ocupadas', 'ocupadas': 'busy'}},
            {"en": 'She is a student', "es": 'Ella es estudiante', "noun_id": None, "type": 'written', "glosses": {'student': 'estudiante', 'estudiante': 'student'}},
            {"en": 'He is tired', "es": 'Él está cansado', "noun_id": None, "type": 'written', "glosses": {'tired': 'cansado', 'cansado': 'tired'}},
            {"en": 'You are a student', "es": 'Tú eres estudiante', "noun_id": None, "type": 'written', "glosses": {'student': 'estudiante', 'estudiante': 'student'}},
            {"en": 'I am happy', "es": 'Yo estoy feliz', "noun_id": None, "type": 'written', "glosses": {'happy': 'feliz', 'feliz': 'happy'}},
            {"en": 'She is at home', "es": 'Ella está en casa', "noun_id": None, "type": 'written', "glosses": {'home': 'casa', 'casa': 'home'}},
        ],
        "drill_targets": [{"verb": "ser", "pronoun": "yo"}, {"verb": "ser", "pronoun": "tú"}, {"verb": "ser", "pronoun": "ella"}, {"verb": "ser", "pronoun": "nosotras"}, {"verb": "ser", "pronoun": "ustedes"}, {"verb": "estar", "pronoun": "yo"}, {"verb": "estar", "pronoun": "tú"}, {"verb": "estar", "pronoun": "ella"}, {"verb": "estar", "pronoun": "nosotras"}, {"verb": "estar", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Irregular Present ser + estar (1/2): ser, estar",
            "targets": [{"verb": "ser", "pronoun": "yo"}, {"verb": "ser", "pronoun": "tú"}, {"verb": "ser", "pronoun": "ella"}, {"verb": "ser", "pronoun": "nosotras"}, {"verb": "ser", "pronoun": "ustedes"}, {"verb": "estar", "pronoun": "yo"}, {"verb": "estar", "pronoun": "tú"}, {"verb": "estar", "pronoun": "ella"}, {"verb": "estar", "pronoun": "nosotras"}, {"verb": "estar", "pronoun": "ustedes"}],
        },
        "opener_en": "Where are you from?",
        "opener_es": "¿De dónde eres?",
    },


    "grammar_irregular_present_ir_dar_1": {
        "title": "Irregular Present — ir + dar (1/2)",
        "grammar_level": 4,
        "lesson_number": 3,
        "lesson_type": "conjugation",
        "word_workload": ["ir", "dar"],
        "video_embed_id": "6jpCj97AHMN",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": IRREGULAR_PRESENT_IR_DAR_INTRO,
        "drill_config": {
            "answers": {
                "ir": {"yo": "|voy", "tú": "|vas", "él": "|va", "ella": "|va", "usted": "|va", "nosotros": "|vamos", "nosotras": "|vamos", "ellos": "|van", "ellas": "|van", "ustedes": "|van"},
                "dar": {"yo": "d|oy", "tú": "d|as", "él": "d|a", "ella": "d|a", "usted": "d|a", "nosotros": "d|amos", "nosotras": "d|amos", "ellos": "d|an", "ellas": "d|an", "ustedes": "d|an"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": 'We (m) give food', "es": 'Nosotros damos comida', "noun_id": None, "type": 'auditory', "glosses": {'food': 'comida', 'comida': 'food'}},
            {"en": 'We (f) give food', "es": 'Nosotras damos comida', "noun_id": None, "type": 'auditory', "glosses": {'food': 'comida', 'comida': 'food'}},
            {"en": 'We (m) go to the beach', "es": 'Nosotros vamos a la playa', "noun_id": None, "type": 'auditory', "glosses": {'beach': 'playa', 'playa': 'beach'}},
            {"en": 'You all give money', "es": 'Ustedes dan dinero', "noun_id": None, "type": 'written', "glosses": {'money': 'dinero', 'dinero': 'money'}},
            {"en": 'He goes to the market', "es": 'Él va al mercado', "noun_id": None, "type": 'written', "glosses": {'market': 'mercado', 'mercado': 'market'}},
            {"en": 'I go to the park', "es": 'Yo voy al parque', "noun_id": None, "type": 'written', "glosses": {'park': 'parque', 'parque': 'park'}},
            {"en": 'You give a gift', "es": 'Tú das un regalo', "noun_id": None, "type": 'auditory', "glosses": {'gift': 'regalo', 'regalo': 'gift'}},
            {"en": 'She goes home', "es": 'Ella va a casa', "noun_id": None, "type": 'written', "glosses": {'home': 'casa', 'casa': 'home'}},
            {"en": 'I give a book', "es": 'Yo doy un libro', "noun_id": None, "type": 'written', "glosses": {'book': 'libro', 'libro': 'book'}},
            {"en": 'You go to school', "es": 'Tú vas a la escuela', "noun_id": None, "type": 'auditory', "glosses": {'school': 'escuela', 'escuela': 'school'}},
            {"en": 'I go to the park', "es": 'Yo voy al parque', "noun_id": None, "type": 'auditory', "glosses": {'park': 'parque', 'parque': 'park'}},
            {"en": 'She gives flowers', "es": 'Ella da flores', "noun_id": None, "type": 'written', "glosses": {'flowers': 'flores', 'flores': 'flowers'}},
            {"en": 'You give a gift', "es": 'Tú das un regalo', "noun_id": None, "type": 'written', "glosses": {'gift': 'regalo', 'regalo': 'gift'}},
            {"en": 'They (f) give flowers', "es": 'Ellas dan flores', "noun_id": None, "type": 'written', "glosses": {'flowers': 'flores', 'flores': 'flowers'}},
            {"en": 'You go to school', "es": 'Tú vas a la escuela', "noun_id": None, "type": 'written', "glosses": {'school': 'escuela', 'escuela': 'school'}},
            {"en": 'They (f) go to the museum', "es": 'Ellas van al museo', "noun_id": None, "type": 'written', "glosses": {'museum': 'museo', 'museo': 'museum'}},
            {"en": 'He gives a book', "es": 'Él da un libro', "noun_id": None, "type": 'written', "glosses": {'book': 'libro', 'libro': 'book'}},
            {"en": 'I give water', "es": 'Yo doy agua', "noun_id": None, "type": 'auditory', "glosses": {'water': 'agua', 'agua': 'water'}},
            {"en": 'You all go to the city', "es": 'Ustedes van a la ciudad', "noun_id": None, "type": 'written', "glosses": {'city': 'ciudad', 'ciudad': 'city'}},
            {"en": 'We (f) go to the market', "es": 'Nosotras vamos al mercado', "noun_id": None, "type": 'auditory', "glosses": {'market': 'mercado', 'mercado': 'market'}},
        ],
        "drill_targets": [{"verb": "ir", "pronoun": "yo"}, {"verb": "ir", "pronoun": "tú"}, {"verb": "ir", "pronoun": "ella"}, {"verb": "ir", "pronoun": "nosotras"}, {"verb": "ir", "pronoun": "ustedes"}, {"verb": "dar", "pronoun": "yo"}, {"verb": "dar", "pronoun": "tú"}, {"verb": "dar", "pronoun": "ella"}, {"verb": "dar", "pronoun": "nosotras"}, {"verb": "dar", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Irregular Present ir + dar (1/2): ir, dar",
            "targets": [{"verb": "ir", "pronoun": "yo"}, {"verb": "ir", "pronoun": "tú"}, {"verb": "ir", "pronoun": "ella"}, {"verb": "ir", "pronoun": "nosotras"}, {"verb": "ir", "pronoun": "ustedes"}, {"verb": "dar", "pronoun": "yo"}, {"verb": "dar", "pronoun": "tú"}, {"verb": "dar", "pronoun": "ella"}, {"verb": "dar", "pronoun": "nosotras"}, {"verb": "dar", "pronoun": "ustedes"}],
        },
        "opener_en": "Where are you going?",
        "opener_es": "¿Adónde vas?",
    },


    "grammar_irregular_present_tener_venir_1": {
        "title": "Irregular Present — tener + venir (1/2)",
        "grammar_level": 4,
        "lesson_number": 5,
        "lesson_type": "conjugation",
        "word_workload": ["tener", "venir"],
        "video_embed_id": "6jpCj97AHMN",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": IRREGULAR_PRESENT_TENER_VENIR_INTRO,
        "drill_config": {
            "answers": {
                "tener": {"yo": "ten|go", "tú": "t|ienes", "él": "t|iene", "ella": "t|iene", "usted": "t|iene", "nosotros": "ten|emos", "nosotras": "ten|emos", "ellos": "t|ienen", "ellas": "t|ienen", "ustedes": "t|ienen"},
                "venir": {"yo": "ven|go", "tú": "v|ienes", "él": "v|iene", "ella": "v|iene", "usted": "v|iene", "nosotros": "ven|imos", "nosotras": "ven|imos", "ellos": "v|ienen", "ellas": "v|ienen", "ustedes": "v|ienen"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": 'He has a red car', "es": 'Él tiene un coche rojo', "noun_id": None, "type": 'written', "glosses": {'car': 'coche', 'red': 'rojo', 'rojo': 'red', 'coche': 'car'}},
            {"en": 'I have two books', "es": 'Yo tengo dos libros', "noun_id": None, "type": 'auditory', "glosses": {'books': 'libros', 'libros': 'books', 'two': 'dos', 'dos': 'two'}},
            {"en": 'We (f) have new friends', "es": 'Nosotras tenemos amigas nuevas', "noun_id": None, "type": 'auditory', "glosses": {'friends': 'amigas', 'new': 'nuevas', 'amigas': 'friends', 'nuevas': 'new'}},
            {"en": 'She comes with her mother', "es": 'Ella viene con su madre', "noun_id": None, "type": 'written', "glosses": {'mother': 'madre', 'madre': 'mother'}},
            {"en": 'We (m) come early today', "es": 'Nosotros venimos temprano hoy', "noun_id": None, "type": 'auditory', "glosses": {'early': 'temprano', 'temprano': 'early', 'today': 'hoy', 'hoy': 'today'}},
            {"en": 'She has a big house', "es": 'Ella tiene una casa grande', "noun_id": None, "type": 'written', "glosses": {'house': 'casa', 'big': 'grande', 'casa': 'house', 'grande': 'big'}},
            {"en": 'I have a red book', "es": 'Yo tengo un libro rojo', "noun_id": None, "type": 'written', "glosses": {'book': 'libro', 'red': 'rojo', 'libro': 'book', 'rojo': 'red'}},
            {"en": 'You have two cats', "es": 'Tú tienes dos gatos', "noun_id": None, "type": 'auditory', "glosses": {'cats': 'gatos', 'gatos': 'cats'}},
            {"en": 'I come from Spain', "es": 'Yo vengo de España', "noun_id": None, "type": 'written', "glosses": {'Spain': 'España', 'España': 'Spain'}},
            {"en": 'You (pl) come late every day', "es": 'Ustedes vienen tarde todos los días', "noun_id": None, "type": 'written', "glosses": {'late': 'tarde', 'every day': 'todos los días', 'tarde': 'late', 'todos los días': 'every day'}},
            {"en": 'You come early today', "es": 'Tú vienes temprano hoy', "noun_id": None, "type": 'auditory', "glosses": {'early': 'temprano', 'today': 'hoy', 'temprano': 'early', 'hoy': 'today'}},
            {"en": 'We (f) come to the park', "es": 'Nosotras venimos al parque', "noun_id": None, "type": 'auditory', "glosses": {'park': 'parque', 'parque': 'park'}},
            {"en": 'You have a small dog', "es": 'Tú tienes un perro pequeño', "noun_id": None, "type": 'written', "glosses": {'dog': 'perro', 'small': 'pequeño', 'pequeño': 'small', 'perro': 'dog'}},
            {"en": 'You come to the school', "es": 'Tú vienes a la escuela', "noun_id": None, "type": 'written', "glosses": {'school': 'escuela', 'escuela': 'school'}},
            {"en": 'You (pl) have many questions', "es": 'Ustedes tienen muchas preguntas', "noun_id": None, "type": 'written', "glosses": {'questions': 'preguntas', 'many': 'muchas', 'preguntas': 'questions', 'muchas': 'many'}},
            {"en": 'I come from the city', "es": 'Yo vengo de la ciudad', "noun_id": None, "type": 'auditory', "glosses": {'city': 'ciudad', 'ciudad': 'city'}},
            {"en": 'He comes with his friend', "es": 'Él viene con su amigo', "noun_id": None, "type": 'written', "glosses": {'friend': 'amigo', 'amigo': 'friend'}},
            {"en": 'We (m) have a big house', "es": 'Nosotros tenemos una casa grande', "noun_id": None, "type": 'auditory', "glosses": {'house': 'casa', 'big': 'grande', 'grande': 'big', 'casa': 'house'}},
            {"en": 'They (f) come from Spain', "es": 'Ellas vienen de España', "noun_id": None, "type": 'written', "glosses": {'Spain': 'España', 'España': 'Spain'}},
            {"en": 'They (f) have three cats', "es": 'Ellas tienen tres gatos', "noun_id": None, "type": 'written', "glosses": {'cats': 'gatos', 'gatos': 'cats', 'three': 'tres', 'tres': 'three'}},
        ],
        "drill_targets": [{"verb": "tener", "pronoun": "yo"}, {"verb": "tener", "pronoun": "tú"}, {"verb": "tener", "pronoun": "ella"}, {"verb": "tener", "pronoun": "nosotras"}, {"verb": "tener", "pronoun": "ustedes"}, {"verb": "venir", "pronoun": "yo"}, {"verb": "venir", "pronoun": "tú"}, {"verb": "venir", "pronoun": "ella"}, {"verb": "venir", "pronoun": "nosotras"}, {"verb": "venir", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Irregular Present tener + venir (1/2): tener, venir",
            "targets": [{"verb": "tener", "pronoun": "yo"}, {"verb": "tener", "pronoun": "tú"}, {"verb": "tener", "pronoun": "ella"}, {"verb": "tener", "pronoun": "nosotras"}, {"verb": "tener", "pronoun": "ustedes"}, {"verb": "venir", "pronoun": "yo"}, {"verb": "venir", "pronoun": "tú"}, {"verb": "venir", "pronoun": "ella"}, {"verb": "venir", "pronoun": "nosotras"}, {"verb": "venir", "pronoun": "ustedes"}],
        },
        "opener_en": "Do you have time?",
        "opener_es": "¿Tienes tiempo?",
    },


    "grammar_irregular_present_ser_estar_chat": {
        "title": "Irregular Present — ser + estar Chat",
        "grammar_level": 4,
        "lesson_number": 2.5,
        "lesson_type": "conjugation",
        "word_workload": ["ser", "estar"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Irregular Present ser + estar chat: ser, estar", "targets": [{"verb": "ser", "pronoun": "yo"}, {"verb": "ser", "pronoun": "tú"}, {"verb": "ser", "pronoun": "ella"}, {"verb": "ser", "pronoun": "nosotras"}, {"verb": "ser", "pronoun": "ustedes"}, {"verb": "estar", "pronoun": "tú"}, {"verb": "estar", "pronoun": "yo"}, {"verb": "estar", "pronoun": "él"}, {"verb": "estar", "pronoun": "nosotros"}, {"verb": "estar", "pronoun": "ellas"}]},
    },

    "grammar_irregular_present_ir_dar_chat": {
        "title": "Irregular Present — ir + dar Chat",
        "grammar_level": 4,
        "lesson_number": 4.5,
        "lesson_type": "conjugation",
        "word_workload": ["ir", "dar"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Irregular Present ir + dar chat: ir, dar", "targets": [{"verb": "ir", "pronoun": "yo"}, {"verb": "ir", "pronoun": "tú"}, {"verb": "ir", "pronoun": "ella"}, {"verb": "ir", "pronoun": "nosotras"}, {"verb": "ir", "pronoun": "ustedes"}, {"verb": "dar", "pronoun": "tú"}, {"verb": "dar", "pronoun": "yo"}, {"verb": "dar", "pronoun": "él"}, {"verb": "dar", "pronoun": "nosotros"}, {"verb": "dar", "pronoun": "ellas"}]},
    },

    "grammar_irregular_present_tener_venir_chat": {
        "title": "Irregular Present — tener + venir Chat",
        "grammar_level": 4,
        "lesson_number": 6.5,
        "lesson_type": "conjugation",
        "word_workload": ["tener", "venir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Irregular Present tener + venir chat: tener, venir", "targets": [{"verb": "tener", "pronoun": "yo"}, {"verb": "tener", "pronoun": "tú"}, {"verb": "tener", "pronoun": "ella"}, {"verb": "tener", "pronoun": "nosotras"}, {"verb": "tener", "pronoun": "ustedes"}, {"verb": "venir", "pronoun": "tú"}, {"verb": "venir", "pronoun": "yo"}, {"verb": "venir", "pronoun": "él"}, {"verb": "venir", "pronoun": "nosotros"}, {"verb": "venir", "pronoun": "ellas"}]},
    },

    # --- GL 4.1: Ser vs. Estar ---
    # --- GL 4.1: chat companion of `grammar_ser_estar_rules` ---
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
        "drill_sentences": [
            {"en": "I go by the park", "es": "Yo voy por el parque", "noun_id": "parque", "type": "written", "glosses": {"park": "parque", "parque": "park"}},
            {"en": "This is for you", "es": "Esto es para ti", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "She works for money", "es": "Ella trabaja por dinero", "noun_id": "dinero", "type": "written", "glosses": {"money": "dinero", "dinero": "money"}},
            {"en": "We (m) study in order to learn", "es": "Nosotros estudiamos para aprender", "noun_id": None, "type": "auditory", "glosses": {}},
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
    # --- GL 4.2: 4 chat companions in different situations, each requiring por
    # and para several times so the user gets reps in varied contexts. ---
    "grammar_por_para_chat": {
        "title": "Por vs. Para — Chat (café)",
        "grammar_level": 4.2,
        "lesson_number": 1.1,
        "lesson_type": "rule",
        "word_workload": ["por", "para"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Por vs. Para — café scene: ordering, paying, asking on behalf of someone', 'targets': [{'word': 'por'}, {'word': 'para'}, {'word': 'por'}, {'word': 'para'}, {'word': 'por'}, {'word': 'para'}, {'word': 'por'}, {'word': 'para'}]},
    },
    "grammar_por_para_chat_2": {
        "title": "Por vs. Para — Chat (work)",
        "grammar_level": 4.2,
        "lesson_number": 1.2,
        "lesson_type": "rule",
        "word_workload": ["por", "para"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Por vs. Para — workplace scene: deadlines, working on/for projects, working through a problem', 'targets': [{'word': 'por'}, {'word': 'para'}, {'word': 'por'}, {'word': 'para'}, {'word': 'por'}, {'word': 'para'}, {'word': 'por'}, {'word': 'para'}]},
    },
    "grammar_por_para_chat_3": {
        "title": "Por vs. Para — Chat (travel)",
        "grammar_level": 4.2,
        "lesson_number": 1.3,
        "lesson_type": "rule",
        "word_workload": ["por", "para"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Por vs. Para — travel scene: destinations, going through cities, paying for tickets', 'targets': [{'word': 'por'}, {'word': 'para'}, {'word': 'por'}, {'word': 'para'}, {'word': 'por'}, {'word': 'para'}, {'word': 'por'}, {'word': 'para'}]},
    },
    "grammar_por_para_chat_4": {
        "title": "Por vs. Para — Chat (gift shop)",
        "grammar_level": 4.2,
        "lesson_number": 1.4,
        "lesson_type": "rule",
        "word_workload": ["por", "para"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Por vs. Para — gift shop scene: gifts for people, prices paid, deadlines (mother\'s day)', 'targets': [{'word': 'por'}, {'word': 'para'}, {'word': 'por'}, {'word': 'para'}, {'word': 'por'}, {'word': 'para'}, {'word': 'por'}, {'word': 'para'}]},
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
        "title": "Possessive Pronouns — Chat (mine / yours)",
        "grammar_level": 4.4,
        "lesson_number": 1.1,
        "lesson_type": "rule",
        "word_workload": ["el mío", "el tuyo"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "possessive_pronouns",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Possessive pronouns: mío/mía/míos/mías + tuyo/tuya/tuyos/tuyas', 'targets': [{'word': 'mío'}, {'word': 'mía'}, {'word': 'míos'}, {'word': 'mías'}, {'word': 'tuyo'}, {'word': 'tuya'}, {'word': 'tuyos'}, {'word': 'tuyas'}]},
    },
    "grammar_possessive_pronouns_chat_2": {
        "title": "Possessive Pronouns — Chat (his/hers/yours-fml/theirs / ours)",
        "grammar_level": 4.4,
        "lesson_number": 1.2,
        "lesson_type": "rule",
        "word_workload": ["el suyo", "el nuestro"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "possessive_pronouns",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {'description': 'Possessive pronouns: suyo/suya/suyos/suyas + nuestro/nuestra/nuestros/nuestras', 'targets': [{'word': 'suyo'}, {'word': 'suya'}, {'word': 'suyos'}, {'word': 'suyas'}, {'word': 'nuestro'}, {'word': 'nuestra'}, {'word': 'nuestros'}, {'word': 'nuestras'}]},
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
        "intro_chart": {'kind': 'cards', 'title': 'saber vs. conocer — two flavors of "to know"', 'cards': [{'kind': 'text', 'title': 'English uses one word; Spanish uses two', 'body': '**saber** = to know a fact, a piece of information, or how to do something. **conocer** = to be familiar with a person, a place, or a thing through experience. Picking the wrong one rarely confuses meaning, but it always sounds non-native.'}, {'kind': 'mini_table', 'title': 'saber (to know)', 'rows': [['yo', 'sé'], ['tú', 'sabes'], ['él / ella / usted', 'sabe'], ['nosotros / nosotras', 'sabemos'], ['ellos / ellas / ustedes', 'saben']]}, {'kind': 'mini_table', 'title': 'conocer (to know / be familiar)', 'rows': [['yo', 'conozco'], ['tú', 'conoces'], ['él / ella / usted', 'conoce'], ['nosotros / nosotras', 'conocemos'], ['ellos / ellas / ustedes', 'conocen']]}], 'recall': [{'verb': 'saber', 'answers': {'yo': 'sé', 'tú': 'sabes', 'él': 'sabe', 'nosotros': 'sabemos', 'ellos': 'saben'}}, {'verb': 'conocer', 'answers': {'yo': 'conozco', 'tú': 'conoces', 'él': 'conoce', 'nosotros': 'conocemos', 'ellos': 'conocen'}}]},
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
    "grammar_gustar_1": {
        "title": "Gustar Part 1",
        "grammar_level": 10,
        "word_workload": ["gusta"],
        "video_embed_id": "rfPPtJI9prc",
        "drill_type": "gustar",
        "tense": "gustar",
        "intro_chart": GUSTAR_INTRO,
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
        "title": "Gustar Part 1 — Chat (food / drinks)",
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
            "description": "Food/drink scene: ask + answer about preferences with all 5 short pronouns + singular nouns (me/te/le/nos/les + gusta)",
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
    "grammar_gustar_1_chat_2": {
        "title": "Gustar Part 1 — Chat (activities)",
        "grammar_level": 10,
        "lesson_number": 1.2,
        "lesson_type": "rule",
        "word_workload": ["gusta"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "gustar",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {
            "description": "Free-time scene (sports, music, movies): same 5 short pronouns + gusta with singular activity nouns",
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
        "intro_chart": GUSTAR_PLURAL_INTRO,
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
        "title": "Gustar Part 2 — Chat (food / drinks, plural)",
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
            "description": "Food/drink scene: ask about plural nouns (los tacos, las galletas) — every short pronoun + gustan",
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
    "grammar_gustar_2_chat_2": {
        "title": "Gustar Part 2 — Chat (people / animals, plural)",
        "grammar_level": 10.3,
        "lesson_number": 1.2,
        "lesson_type": "rule",
        "word_workload": ["gustan"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "gustar",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {
            "description": "People/animals scene: ask about groups (los niños, las flores, los gatos) — same 5 short pronouns + gustan",
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
        "intro_chart": GUSTAR_EMPHATIC_INTRO,
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
            {"en": "We (m) like the park (emphatic)", "es": "A nosotros nos gusta el parque", "noun_id": "parque", "type": "auditory", "glosses": {}},
            {"en": "They (m) like the dog (emphatic)", "es": "A ellos les gusta el perro", "noun_id": "perro", "type": "written", "glosses": {"dog": "perro", "perro": "dog"}},
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
        "title": "Gustar Part 3 — Chat (contrasting opinions)",
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
            "description": "Contrast scene: \"I like X, but he likes Y\" — emphatic 'a + pronoun' across all 10 pronoun forms",
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
    "grammar_gustar_3_chat_2": {
        "title": "Gustar Part 3 — Chat (clarifying \"le\" / \"les\")",
        "grammar_level": 10.6,
        "lesson_number": 1.2,
        "lesson_type": "rule",
        "word_workload": ["gusta", "gustan"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "gustar",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {
            "description": "Clarification scene: practice using a él / a ella / a usted / a ellos / a ellas / a ustedes to disambiguate the bare le and les forms",
            "targets": [
                {"phrase": "a él le gusta"},
                {"phrase": "a ella le gusta"},
                {"phrase": "a usted le gusta"},
                {"phrase": "a ellos les gusta"},
                {"phrase": "a ellas les gusta"},
                {"phrase": "a ustedes les gusta"},
                {"phrase": "a él le gustan"},
                {"phrase": "a ellos les gustan"},
            ],
            "pattern": "a_prefix",
        },
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
        'title': 'Tengo que / Me toca / Necesito',
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
        "intro_chart": {'kind': 'cards', 'title': 'Modal + infinitive — "have to," "my turn to," "need to"', 'cards': [{'kind': 'text', 'title': 'Three everyday ways to say what you must do', 'body': "Spanish has three super-common phrases that all take an infinitive: **tengo que + inf** (I have to), **me toca + inf** (it's my turn to), **necesito + inf** (I need to). The first verb conjugates; the action verb stays in its dictionary form."}, {'kind': 'mini_table', 'title': 'hablar (to speak)', 'rows': [['yo', 'tengo que hablar'], ['tú', 'tienes que hablar'], ['él / ella / usted', 'tiene que hablar'], ['nosotros / nosotras', 'tenemos que hablar'], ['ellos / ellas / ustedes', 'tienen que hablar']]}, {'kind': 'mini_table', 'title': 'comer (to eat)', 'rows': [['yo', 'tengo que comer'], ['tú', 'tienes que comer'], ['él / ella / usted', 'tiene que comer'], ['nosotros / nosotras', 'tenemos que comer'], ['ellos / ellas / ustedes', 'tienen que comer']]}], 'recall': [{'verb': 'hablar', 'answers': {'yo': 'tengo que hablar', 'tú': 'tienes que hablar', 'él': 'tiene que hablar', 'nosotros': 'tenemos que hablar', 'ellos': 'tienen que hablar'}}, {'verb': 'comer', 'answers': {'yo': 'tengo que comer', 'tú': 'tienes que comer', 'él': 'tiene que comer', 'nosotros': 'tenemos que comer', 'ellos': 'tienen que comer'}}]},
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
        "drill_sentences": [
            {"en": "It's your turn to study a lot", "es": 'Tú te toca estudiar mucho', "noun_id": None, "type": 'auditory', "glosses": {}},
            {"en": 'They (m) have to eat meat', "es": 'Ellos tienen que comer carne', "noun_id": None, "type": 'auditory', "glosses": {'meat': 'carne', 'carne': 'meat'}},
            {"en": "It's his turn to live together", "es": 'Él le toca vivir juntos', "noun_id": None, "type": 'written', "glosses": {}},
            {"en": 'You need to write messages', "es": 'Tú necesitas escribir mensajes', "noun_id": None, "type": 'auditory', "glosses": {'messages': 'mensajes', 'mensajes': 'messages'}},
            {"en": 'They (f) need to sleep eight hours', "es": 'Ellas necesitan dormir ocho horas', "noun_id": None, "type": 'written', "glosses": {'hours': 'horas', 'horas': 'hours'}},
            {"en": "It's their (m) turn to study here", "es": 'Ellos les toca estudiar aquí', "noun_id": None, "type": 'auditory', "glosses": {}},
            {"en": 'She needs to write names', "es": 'Ella necesita escribir nombres', "noun_id": 'nombre', "type": 'auditory', "glosses": {'names': 'nombres', 'nombres': 'names'}},
            {"en": 'We (m) need to write fast', "es": 'Nosotros necesitamos escribir rápido', "noun_id": None, "type": 'auditory', "glosses": {}},
            {"en": 'We (f) have to speak fast', "es": 'Nosotras tenemos que hablar rápido', "noun_id": None, "type": 'written', "glosses": {}},
            {"en": 'You all need to write a book', "es": 'Ustedes necesitan escribir un libro', "noun_id": 'libro', "type": 'auditory', "glosses": {'book': 'libro', 'libro': 'book'}},
            {"en": "It's their (f) turn to live here", "es": 'A ellas les toca vivir aquí', "noun_id": None, "type": 'written', "glosses": {}},
            {"en": "It's our (f) turn to live in the city", "es": 'A nosotras nos toca vivir en la ciudad', "noun_id": 'ciudad', "type": 'written', "glosses": {'turn': 'turno', 'city': 'ciudad', 'turno': 'turn', 'ciudad': 'city'}},
            {"en": "It's our (m) turn to study together", "es": 'Nosotros nos toca estudiar juntos', "noun_id": None, "type": 'auditory', "glosses": {}},
            {"en": 'She has to eat food', "es": 'Ella tiene que comer comida', "noun_id": None, "type": 'auditory', "glosses": {'food': 'comida', 'comida': 'food'}},
            {"en": 'We (f) need to sleep well', "es": 'Nosotras necesitamos dormir bien', "noun_id": None, "type": 'written', "glosses": {}},
            {"en": 'They (f) have to speak a lot', "es": 'Ellas tienen que hablar mucho', "noun_id": None, "type": 'written', "glosses": {}},
            {"en": 'We (m) have to eat fruit', "es": 'Nosotros tenemos que comer fruta', "noun_id": None, "type": 'auditory', "glosses": {'fruit': 'fruta', 'fruta': 'fruit'}},
            {"en": 'I have to speak Spanish', "es": 'Yo tengo que hablar español', "noun_id": None, "type": 'written', "glosses": {'spanish': 'español', 'español': 'spanish'}},
            {"en": 'He needs to sleep here', "es": 'Él necesita dormir aquí', "noun_id": None, "type": 'written', "glosses": {}},
            {"en": 'I need to sleep a lot', "es": 'Yo necesito dormir mucho', "noun_id": None, "type": 'written', "glosses": {}},
            {"en": "It's your turn to study Spanish", "es": 'Ustedes les toca estudiar español', "noun_id": None, "type": 'auditory', "glosses": {'spanish': 'español', 'español': 'spanish'}},
            {"en": 'You all have to eat salad', "es": 'Ustedes tienen que comer ensalada', "noun_id": None, "type": 'auditory', "glosses": {'salad': 'ensalada', 'ensalada': 'salad'}},
            {"en": 'You need to sleep early', "es": 'Usted necesita dormir temprano', "noun_id": None, "type": 'written', "glosses": {}},
            {"en": 'They (m) need to write a letter', "es": 'Ellos necesitan escribir una carta', "noun_id": 'carta', "type": 'auditory', "glosses": {'letter': 'carta', 'carta': 'letter'}},
            {"en": 'You have to eat bread', "es": 'Tú tienes que comer pan', "noun_id": None, "type": 'auditory', "glosses": {'bread': 'pan', 'pan': 'bread'}},
            {"en": "It's your turn to live alone", "es": 'Usted le toca vivir solo', "noun_id": None, "type": 'written', "glosses": {}},
            {"en": "It's her turn to study at home", "es": 'Ella le toca estudiar en casa', "noun_id": 'casa', "type": 'auditory', "glosses": {'turn': 'turno', 'turno': 'turn', 'home': 'casa', 'casa': 'home'}},
            {"en": 'You have to speak well', "es": 'Usted tiene que hablar bien', "noun_id": None, "type": 'written', "glosses": {}},
            {"en": 'He has to speak English', "es": 'Él tiene que hablar inglés', "noun_id": None, "type": 'written', "glosses": {'english': 'inglés', 'inglés': 'english'}},
            {"en": "It's my turn to live nearby", "es": 'Yo me toca vivir cerca', "noun_id": None, "type": 'written', "glosses": {}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Imperfect — the "used to" past', 'cards': [{'kind': 'text', 'title': 'A past tense for what kept happening', 'body': "The imperfect describes what *used to happen*, what was *ongoing*, or what was *true for a while* in the past. It's the soundtrack of the story — background, habits, descriptions, age, time, weather."}, {'kind': 'mini_table', 'title': 'hablar (to speak)', 'rows': [['yo', 'hablaba'], ['tú', 'hablabas'], ['él / ella / usted', 'hablaba'], ['nosotros / nosotras', 'hablábamos'], ['ellos / ellas / ustedes', 'hablaban']]}, {'kind': 'mini_table', 'title': 'escuchar (to listen)', 'rows': [['yo', 'escuchaba'], ['tú', 'escuchabas'], ['él / ella / usted', 'escuchaba'], ['nosotros / nosotras', 'escuchábamos'], ['ellos / ellas / ustedes', 'escuchaban']]}], 'recall': [{'verb': 'hablar', 'answers': {'yo': 'hablaba', 'tú': 'hablabas', 'él': 'hablaba', 'nosotros': 'hablábamos', 'ellos': 'hablaban'}}, {'verb': 'escuchar', 'answers': {'yo': 'escuchaba', 'tú': 'escuchabas', 'él': 'escuchaba', 'nosotros': 'escuchábamos', 'ellos': 'escuchaban'}}]},
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
            {"en": "You used to listen to music", "es": "Tú escuchabas música", "noun_id": None, "type": "auditory", "glosses": {"music": "música", "música": "music"}},
            {"en": "He used to speak English", "es": "Él hablaba inglés", "noun_id": None, "type": "written", "glosses": {"English": "inglés", "inglés": "English"}},
            {"en": "She used to listen to the radio", "es": "Ella escuchaba la radio", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You used to speak well", "es": "Usted hablaba bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "We (m) used to listen to a song", "es": "Nosotros escuchábamos una canción", "noun_id": None, "type": "auditory", "glosses": {"song": "canción", "canción": "song"}},
            {"en": "We (f) used to speak fast", "es": "Nosotras hablábamos rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "They (m) used to listen well", "es": "Ellos escuchaban bien", "noun_id": None, "type": "auditory", "glosses": {"well": "bien", "bien": "well"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Imperfect — the "used to" past', 'cards': [{'kind': 'text', 'title': 'A past tense for what kept happening', 'body': "The imperfect describes what *used to happen*, what was *ongoing*, or what was *true for a while* in the past. It's the soundtrack of the story — background, habits, descriptions, age, time, weather."}, {'kind': 'mini_table', 'title': 'comer (to eat)', 'rows': [['yo', 'comía'], ['tú', 'comías'], ['él / ella / usted', 'comía'], ['nosotros / nosotras', 'comíamos'], ['ellos / ellas / ustedes', 'comían']]}, {'kind': 'mini_table', 'title': 'vivir (to live)', 'rows': [['yo', 'vivía'], ['tú', 'vivías'], ['él / ella / usted', 'vivía'], ['nosotros / nosotras', 'vivíamos'], ['ellos / ellas / ustedes', 'vivían']]}], 'recall': [{'verb': 'comer', 'answers': {'yo': 'comía', 'tú': 'comías', 'él': 'comía', 'nosotros': 'comíamos', 'ellos': 'comían'}}, {'verb': 'vivir', 'answers': {'yo': 'vivía', 'tú': 'vivías', 'él': 'vivía', 'nosotros': 'vivíamos', 'ellos': 'vivían'}}]},
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
            {"en": "We (m) used to live alone", "es": "Nosotros vivíamos solo", "noun_id": None, "type": "auditory", "glosses": {"alone": "solo", "solo": "alone"}},
            {"en": "We (f) used to eat salad", "es": "Nosotras comíamos ensalada", "noun_id": None, "type": "written", "glosses": {"salad": "ensalada", "ensalada": "salad"}},
            {"en": "They (m) used to live in the city", "es": "Ellos vivían en la ciudad", "noun_id": "ciudad", "type": "auditory", "glosses": {"city": "ciudad", "ciudad": "city"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Imperfect — the "used to" past', 'cards': [{'kind': 'text', 'title': 'A past tense for what kept happening', 'body': "The imperfect describes what *used to happen*, what was *ongoing*, or what was *true for a while* in the past. It's the soundtrack of the story — background, habits, descriptions, age, time, weather."}, {'kind': 'mini_table', 'title': 'ir (to go)', 'rows': [['yo', 'iba'], ['tú', 'ibas'], ['él / ella / usted', 'iba'], ['nosotros / nosotras', 'íbamos'], ['ellos / ellas / ustedes', 'iban']]}, {'kind': 'mini_table', 'title': 'ser (to be)', 'rows': [['yo', 'era'], ['tú', 'eras'], ['él / ella / usted', 'era'], ['nosotros / nosotras', 'éramos'], ['ellos / ellas / ustedes', 'eran']]}], 'recall': [{'verb': 'ir', 'answers': {'yo': 'iba', 'tú': 'ibas', 'él': 'iba', 'nosotros': 'íbamos', 'ellos': 'iban'}}, {'verb': 'ser', 'answers': {'yo': 'era', 'tú': 'eras', 'él': 'era', 'nosotros': 'éramos', 'ellos': 'eran'}}]},
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
            {"en": "We (m) used to be tall", "es": "Nosotros éramos alto", "noun_id": None, "type": "auditory", "glosses": {"tall": "alto", "alto": "tall"}},
            {"en": "We (f) used to go home", "es": "Nosotras íbamos a casa", "noun_id": "casa", "type": "written", "glosses": {"at home": "en casa", "en casa": "at home"}},
            {"en": "They (m) used to be professional", "es": "Ellos eran profesional", "noun_id": None, "type": "auditory", "glosses": {"professional": "profesional", "profesional": "professional"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Imperfect — the "used to" past', 'cards': [{'kind': 'text', 'title': 'A past tense for what kept happening', 'body': "The imperfect describes what *used to happen*, what was *ongoing*, or what was *true for a while* in the past. It's the soundtrack of the story — background, habits, descriptions, age, time, weather."}, {'kind': 'mini_table', 'title': 'ver (to see)', 'rows': [['yo', 'veía'], ['tú', 'veías'], ['él / ella / usted', 'veía'], ['nosotros / nosotras', 'veíamos'], ['ellos / ellas / ustedes', 'veían']]}, {'kind': 'mini_table', 'title': 'escribir (to write)', 'rows': [['yo', 'escribía'], ['tú', 'escribías'], ['él / ella / usted', 'escribía'], ['nosotros / nosotras', 'escribíamos'], ['ellos / ellas / ustedes', 'escribían']]}], 'recall': [{'verb': 'ver', 'answers': {'yo': 'veía', 'tú': 'veías', 'él': 'veía', 'nosotros': 'veíamos', 'ellos': 'veían'}}, {'verb': 'escribir', 'answers': {'yo': 'escribía', 'tú': 'escribías', 'él': 'escribía', 'nosotros': 'escribíamos', 'ellos': 'escribían'}}]},
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
            {"en": "We (m) used to write a book", "es": "Nosotros escribíamos un libro", "noun_id": "libro", "type": "auditory", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "We (f) used to see a photo", "es": "Nosotras veíamos una foto", "noun_id": None, "type": "written", "glosses": {"photo": "foto", "foto": "photo"}},
            {"en": "They (m) used to write messages", "es": "Ellos escribían mensajes", "noun_id": None, "type": "auditory", "glosses": {"messages": "mensajes", "mensajes": "messages"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Reflexive verbs — when the action loops back to the doer', 'cards': [{'kind': 'text', 'title': 'The doer and the receiver are the same person', 'body': "Reflexive verbs describe actions you do *to yourself*: wash yourself, get yourself up, get yourself dressed. The infinitive ends in **-se** (lavarse, levantarse), and you replace -se with the right reflexive pronoun for whoever's doing it."}, {'kind': 'text', 'title': 'When the verb has a stem change, the stem still changes', 'body': "*acostarse* is o→ue: *me acuesto*, *te acuestas*… *vestirse* is e→i: *me visto*, *te vistes*… The reflexive pronoun doesn't suppress the stem-change rule."}, {'kind': 'mini_table', 'title': 'lavarse (to wash oneself)', 'rows': [['yo', 'me lavo'], ['tú', 'te lavas'], ['él / ella / usted', 'se lava'], ['nosotros / nosotras', 'nos lavamos'], ['ellos / ellas / ustedes', 'se lavan']]}, {'kind': 'mini_table', 'title': 'llamarse (to be called)', 'rows': [['yo', 'me llamo'], ['tú', 'te llamas'], ['él / ella / usted', 'se llama'], ['nosotros / nosotras', 'nos llamamos'], ['ellos / ellas / ustedes', 'se llaman']]}], 'recall': [{'verb': 'lavarse', 'answers': {'yo': 'me lavo', 'tú': 'te lavas', 'él': 'se lava', 'nosotros': 'nos lavamos', 'ellos': 'se lavan'}}, {'verb': 'llamarse', 'answers': {'yo': 'me llamo', 'tú': 'te llamas', 'él': 'se llama', 'nosotros': 'nos llamamos', 'ellos': 'se llaman'}}]},
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
            {"en": "We (m) are called Ana", "es": "Nosotros nos llamamos Ana", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) wash quickly", "es": "Nosotras nos lavamos rápido", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They (m) are called Luis", "es": "Ellos se llaman Luis", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Reflexive verbs — when the action loops back to the doer', 'cards': [{'kind': 'text', 'title': 'The doer and the receiver are the same person', 'body': "Reflexive verbs describe actions you do *to yourself*: wash yourself, get yourself up, get yourself dressed. The infinitive ends in **-se** (lavarse, levantarse), and you replace -se with the right reflexive pronoun for whoever's doing it."}, {'kind': 'text', 'title': 'When the verb has a stem change, the stem still changes', 'body': "*acostarse* is o→ue: *me acuesto*, *te acuestas*… *vestirse* is e→i: *me visto*, *te vistes*… The reflexive pronoun doesn't suppress the stem-change rule."}, {'kind': 'mini_table', 'title': 'levantarse (to get up)', 'rows': [['yo', 'me levanto'], ['tú', 'te levantas'], ['él / ella / usted', 'se levanta'], ['nosotros / nosotras', 'nos levantamos'], ['ellos / ellas / ustedes', 'se levantan']]}, {'kind': 'mini_table', 'title': 'ducharse (to shower)', 'rows': [['yo', 'me ducho'], ['tú', 'te duchas'], ['él / ella / usted', 'se ducha'], ['nosotros / nosotras', 'nos duchamos'], ['ellos / ellas / ustedes', 'se duchan']]}], 'recall': [{'verb': 'levantarse', 'answers': {'yo': 'me levanto', 'tú': 'te levantas', 'él': 'se levanta', 'nosotros': 'nos levantamos', 'ellos': 'se levantan'}}, {'verb': 'ducharse', 'answers': {'yo': 'me ducho', 'tú': 'te duchas', 'él': 'se ducha', 'nosotros': 'nos duchamos', 'ellos': 'se duchan'}}]},
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
            {"en": "We (m) shower in the morning", "es": "Nosotros nos duchamos por la mañana", "noun_id": None, "type": "auditory", "glosses": {"morning": "mañana", "mañana": "morning"}},
            {"en": "We (f) get up together", "es": "Nosotras nos levantamos juntos", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They (m) shower here", "es": "Ellos se duchan aquí", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Reflexive verbs — when the action loops back to the doer', 'cards': [{'kind': 'text', 'title': 'The doer and the receiver are the same person', 'body': "Reflexive verbs describe actions you do *to yourself*: wash yourself, get yourself up, get yourself dressed. The infinitive ends in **-se** (lavarse, levantarse), and you replace -se with the right reflexive pronoun for whoever's doing it."}, {'kind': 'text', 'title': 'When the verb has a stem change, the stem still changes', 'body': "*acostarse* is o→ue: *me acuesto*, *te acuestas*… *vestirse* is e→i: *me visto*, *te vistes*… The reflexive pronoun doesn't suppress the stem-change rule."}, {'kind': 'mini_table', 'title': 'despertarse (to wake up)', 'rows': [['yo', 'me despierto'], ['tú', 'te despiertas'], ['él / ella / usted', 'se despierta'], ['nosotros / nosotras', 'nos despertamos'], ['ellos / ellas / ustedes', 'se despiertan']]}, {'kind': 'mini_table', 'title': 'acostarse (to go to bed)', 'rows': [['yo', 'me acuesto'], ['tú', 'te acuestas'], ['él / ella / usted', 'se acuesta'], ['nosotros / nosotras', 'nos acostamos'], ['ellos / ellas / ustedes', 'se acuestan']]}], 'recall': [{'verb': 'despertarse', 'answers': {'yo': 'me despierto', 'tú': 'te despiertas', 'él': 'se despierta', 'nosotros': 'nos despertamos', 'ellos': 'se despiertan'}}, {'verb': 'acostarse', 'answers': {'yo': 'me acuesto', 'tú': 'te acuestas', 'él': 'se acuesta', 'nosotros': 'nos acostamos', 'ellos': 'se acuestan'}}]},
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
            {"en": "We (m) go to bed early", "es": "Nosotros nos acostamos temprano", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) wake up late", "es": "Nosotras nos despertamos tarde", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They (m) go to bed late", "es": "Ellos se acuestan tarde", "noun_id": None, "type": "auditory", "glosses": {"late": "tarde", "tarde": "late"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Reflexive verbs — when the action loops back to the doer', 'cards': [{'kind': 'text', 'title': 'The doer and the receiver are the same person', 'body': "Reflexive verbs describe actions you do *to yourself*: wash yourself, get yourself up, get yourself dressed. The infinitive ends in **-se** (lavarse, levantarse), and you replace -se with the right reflexive pronoun for whoever's doing it."}, {'kind': 'text', 'title': 'When the verb has a stem change, the stem still changes', 'body': "*acostarse* is o→ue: *me acuesto*, *te acuestas*… *vestirse* is e→i: *me visto*, *te vistes*… The reflexive pronoun doesn't suppress the stem-change rule."}, {'kind': 'mini_table', 'title': 'vestirse (to get dressed)', 'rows': [['yo', 'me visto'], ['tú', 'te vistes'], ['él / ella / usted', 'se viste'], ['nosotros / nosotras', 'nos vestemos'], ['ellos / ellas / ustedes', 'se visten']]}, {'kind': 'mini_table', 'title': 'sentarse (to sit down)', 'rows': [['yo', 'me siento'], ['tú', 'te sientas'], ['él / ella / usted', 'se sienta'], ['nosotros / nosotras', 'nos sentamos'], ['ellos / ellas / ustedes', 'se sientan']]}], 'recall': [{'verb': 'vestirse', 'answers': {'yo': 'me visto', 'tú': 'te vistes', 'él': 'se viste', 'nosotros': 'nos vestemos', 'ellos': 'se visten'}}, {'verb': 'sentarse', 'answers': {'yo': 'me siento', 'tú': 'te sientas', 'él': 'se sienta', 'nosotros': 'nos sentamos', 'ellos': 'se sientan'}}]},
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
            {"en": "We (m) sit down together", "es": "Nosotros nos sentamos juntos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) get dressed early", "es": "Nosotras nos vestemos temprano", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They (m) sit down on the chair", "es": "Ellos se sientan en la silla", "noun_id": None, "type": "auditory", "glosses": {"chair": "silla", "silla": "chair"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Future tense — "will" do something', 'cards': [{'kind': 'text', 'title': 'One set of endings, attached to the WHOLE infinitive', 'body': "Unlike most tenses, the future doesn't drop -ar/-er/-ir. You take the whole infinitive (*hablar*, *comer*, *vivir*) and add the same set of endings — same set for all three verb families. That's the regular pattern."}, {'kind': 'mini_table', 'title': 'hablar (to speak)', 'rows': [['yo', 'hablaré'], ['tú', 'hablarás'], ['él / ella / usted', 'hablará'], ['nosotros / nosotras', 'hablaremos'], ['ellos / ellas / ustedes', 'hablarán']]}, {'kind': 'mini_table', 'title': 'comer (to eat)', 'rows': [['yo', 'comeré'], ['tú', 'comerás'], ['él / ella / usted', 'comerá'], ['nosotros / nosotras', 'comeremos'], ['ellos / ellas / ustedes', 'comerán']]}], 'recall': [{'verb': 'hablar', 'answers': {'yo': 'hablaré', 'tú': 'hablarás', 'él': 'hablará', 'nosotros': 'hablaremos', 'ellos': 'hablarán'}}, {'verb': 'comer', 'answers': {'yo': 'comeré', 'tú': 'comerás', 'él': 'comerá', 'nosotros': 'comeremos', 'ellos': 'comerán'}}]},
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
            {"en": "We (m) will eat fruit", "es": "Nosotros comeremos fruta", "noun_id": None, "type": "auditory", "glosses": {"fruit": "fruta", "fruta": "fruit"}},
            {"en": "We (f) will speak fast", "es": "Nosotras hablaremos rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "They (m) will eat meat", "es": "Ellos comerán carne", "noun_id": None, "type": "auditory", "glosses": {"meat": "carne", "carne": "meat"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Future tense — "will" do something', 'cards': [{'kind': 'text', 'title': 'One set of endings, attached to the WHOLE infinitive', 'body': "Unlike most tenses, the future doesn't drop -ar/-er/-ir. You take the whole infinitive (*hablar*, *comer*, *vivir*) and add the same set of endings — same set for all three verb families. That's the regular pattern."}, {'kind': 'mini_table', 'title': 'vivir (to live)', 'rows': [['yo', 'viviré'], ['tú', 'vivirás'], ['él / ella / usted', 'vivirá'], ['nosotros / nosotras', 'viviremos'], ['ellos / ellas / ustedes', 'vivirán']]}, {'kind': 'mini_table', 'title': 'estudiar (to study)', 'rows': [['yo', 'estudiaré'], ['tú', 'estudiarás'], ['él / ella / usted', 'estudiará'], ['nosotros / nosotras', 'estudiaremos'], ['ellos / ellas / ustedes', 'estudiarán']]}], 'recall': [{'verb': 'vivir', 'answers': {'yo': 'viviré', 'tú': 'vivirás', 'él': 'vivirá', 'nosotros': 'viviremos', 'ellos': 'vivirán'}}, {'verb': 'estudiar', 'answers': {'yo': 'estudiaré', 'tú': 'estudiarás', 'él': 'estudiará', 'nosotros': 'estudiaremos', 'ellos': 'estudiarán'}}]},
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
            {"en": "We (m) will study together", "es": "Nosotros estudiaremos juntos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) will live in the city", "es": "Nosotras viviremos en la ciudad", "noun_id": "ciudad", "type": "written", "glosses": {"city": "ciudad", "ciudad": "city"}},
            {"en": "They (m) will study here", "es": "Ellos estudiarán aquí", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Future tense — "will" do something', 'cards': [{'kind': 'text', 'title': 'One set of endings, attached to the WHOLE infinitive', 'body': "Unlike most tenses, the future doesn't drop -ar/-er/-ir. You take the whole infinitive (*hablar*, *comer*, *vivir*) and add the same set of endings — same set for all three verb families. That's the regular pattern."}, {'kind': 'mini_table', 'title': 'tener (to have)', 'rows': [['yo', 'tendré'], ['tú', 'tendrás'], ['él / ella / usted', 'tendrá'], ['nosotros / nosotras', 'tendremos'], ['ellos / ellas / ustedes', 'tendrán']]}, {'kind': 'mini_table', 'title': 'hacer (to do/make)', 'rows': [['yo', 'haré'], ['tú', 'harás'], ['él / ella / usted', 'hará'], ['nosotros / nosotras', 'haremos'], ['ellos / ellas / ustedes', 'harán']]}], 'recall': [{'verb': 'tener', 'answers': {'yo': 'tendré', 'tú': 'tendrás', 'él': 'tendrá', 'nosotros': 'tendremos', 'ellos': 'tendrán'}}, {'verb': 'hacer', 'answers': {'yo': 'haré', 'tú': 'harás', 'él': 'hará', 'nosotros': 'haremos', 'ellos': 'harán'}}]},
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
            {"en": "We (m) will make homework", "es": "Nosotros haremos la tarea", "noun_id": None, "type": "auditory", "glosses": {"homework": "tarea", "tarea": "homework"}},
            {"en": "We (f) will have a house", "es": "Nosotras tendremos una casa", "noun_id": "casa", "type": "written", "glosses": {"house": "casa", "casa": "house"}},
            {"en": "They (m) will make food", "es": "Ellos harán comida", "noun_id": None, "type": "auditory", "glosses": {"food": "comida", "comida": "food"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Future tense — "will" do something', 'cards': [{'kind': 'text', 'title': 'One set of endings, attached to the WHOLE infinitive', 'body': "Unlike most tenses, the future doesn't drop -ar/-er/-ir. You take the whole infinitive (*hablar*, *comer*, *vivir*) and add the same set of endings — same set for all three verb families. That's the regular pattern."}, {'kind': 'mini_table', 'title': 'decir (to say)', 'rows': [['yo', 'diré'], ['tú', 'dirás'], ['él / ella / usted', 'dirá'], ['nosotros / nosotras', 'diremos'], ['ellos / ellas / ustedes', 'dirán']]}, {'kind': 'mini_table', 'title': 'poder (to be able)', 'rows': [['yo', 'podré'], ['tú', 'podrás'], ['él / ella / usted', 'podrá'], ['nosotros / nosotras', 'podremos'], ['ellos / ellas / ustedes', 'podrán']]}], 'recall': [{'verb': 'decir', 'answers': {'yo': 'diré', 'tú': 'dirás', 'él': 'dirá', 'nosotros': 'diremos', 'ellos': 'dirán'}}, {'verb': 'poder', 'answers': {'yo': 'podré', 'tú': 'podrás', 'él': 'podrá', 'nosotros': 'podremos', 'ellos': 'podrán'}}]},
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
            {"en": "We (m) will be able come", "es": "Nosotros podremos venir", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) will say thanks", "es": "Nosotras diremos gracias", "noun_id": None, "type": "written", "glosses": {"thanks": "gracias", "gracias": "thanks"}},
            {"en": "They (m) will be able help", "es": "Ellos podrán ayudar", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Future tense — "will" do something', 'cards': [{'kind': 'text', 'title': 'One set of endings, attached to the WHOLE infinitive', 'body': "Unlike most tenses, the future doesn't drop -ar/-er/-ir. You take the whole infinitive (*hablar*, *comer*, *vivir*) and add the same set of endings — same set for all three verb families. That's the regular pattern."}, {'kind': 'mini_table', 'title': 'saber (to know)', 'rows': [['yo', 'sabré'], ['tú', 'sabrás'], ['él / ella / usted', 'sabrá'], ['nosotros / nosotras', 'sabremos'], ['ellos / ellas / ustedes', 'sabrán']]}, {'kind': 'mini_table', 'title': 'querer (to want)', 'rows': [['yo', 'querré'], ['tú', 'querrás'], ['él / ella / usted', 'querrá'], ['nosotros / nosotras', 'querremos'], ['ellos / ellas / ustedes', 'querrán']]}], 'recall': [{'verb': 'saber', 'answers': {'yo': 'sabré', 'tú': 'sabrás', 'él': 'sabrá', 'nosotros': 'sabremos', 'ellos': 'sabrán'}}, {'verb': 'querer', 'answers': {'yo': 'querré', 'tú': 'querrás', 'él': 'querrá', 'nosotros': 'querremos', 'ellos': 'querrán'}}]},
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
            {"en": "We (m) will want to go", "es": "Nosotros querremos ir", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) will know how to cook", "es": "Nosotras sabremos cocinar", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They (m) will want to rest", "es": "Ellos querrán descansar", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Future tense — "will" do something', 'cards': [{'kind': 'text', 'title': 'One set of endings, attached to the WHOLE infinitive', 'body': "Unlike most tenses, the future doesn't drop -ar/-er/-ir. You take the whole infinitive (*hablar*, *comer*, *vivir*) and add the same set of endings — same set for all three verb families. That's the regular pattern."}, {'kind': 'mini_table', 'title': 'venir (to come)', 'rows': [['yo', 'vendré'], ['tú', 'vendrás'], ['él / ella / usted', 'vendrá'], ['nosotros / nosotras', 'vendremos'], ['ellos / ellas / ustedes', 'vendrán']]}, {'kind': 'mini_table', 'title': 'salir (to leave)', 'rows': [['yo', 'saldré'], ['tú', 'saldrás'], ['él / ella / usted', 'saldrá'], ['nosotros / nosotras', 'saldremos'], ['ellos / ellas / ustedes', 'saldrán']]}], 'recall': [{'verb': 'venir', 'answers': {'yo': 'vendré', 'tú': 'vendrás', 'él': 'vendrá', 'nosotros': 'vendremos', 'ellos': 'vendrán'}}, {'verb': 'salir', 'answers': {'yo': 'saldré', 'tú': 'saldrás', 'él': 'saldrá', 'nosotros': 'saldremos', 'ellos': 'saldrán'}}]},
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
            {"en": "We (m) will leave now", "es": "Nosotros saldremos ahora", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) will come home", "es": "Nosotras vendremos a casa", "noun_id": "casa", "type": "written", "glosses": {}},
            {"en": "They (m) will leave early", "es": "Ellos saldrán temprano", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Conditional — "would" do something', 'cards': [{'kind': 'text', 'title': 'Same stem as the future, different endings', 'body': 'Conditional shares the future\'s stem (full infinitive, or the same irregular shortcuts: *tendr-, har-, dir-…*). What changes are the endings: instead of future\'s -é/-ás/-á, conditional uses imperfect-style -ía endings. *Hablaría* = "I would speak."'}, {'kind': 'text', 'title': 'Use it for politeness, hypotheticals, soft suggestions', 'body': '*¿Podrías ayudarme?* (Could you help me?) — softer than "can you?" *Yo iría contigo* (I\'d go with you). *En tu lugar, hablaría con ella* (In your place, I would talk to her). It\'s the diplomat\'s tense.'}, {'kind': 'mini_table', 'title': 'hablar (to speak)', 'rows': [['yo', 'hablaría'], ['tú', 'hablarías'], ['él / ella / usted', 'hablaría'], ['nosotros / nosotras', 'hablaríamos'], ['ellos / ellas / ustedes', 'hablarían']]}, {'kind': 'mini_table', 'title': 'comer (to eat)', 'rows': [['yo', 'comería'], ['tú', 'comerías'], ['él / ella / usted', 'comería'], ['nosotros / nosotras', 'comeríamos'], ['ellos / ellas / ustedes', 'comerían']]}], 'recall': [{'verb': 'hablar', 'answers': {'yo': 'hablaría', 'tú': 'hablarías', 'él': 'hablaría', 'nosotros': 'hablaríamos', 'ellos': 'hablarían'}}, {'verb': 'comer', 'answers': {'yo': 'comería', 'tú': 'comerías', 'él': 'comería', 'nosotros': 'comeríamos', 'ellos': 'comerían'}}]},
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
            {"en": "We (m) would eat fruit", "es": "Nosotros comeríamos fruta", "noun_id": None, "type": "auditory", "glosses": {"fruit": "fruta", "fruta": "fruit"}},
            {"en": "We (f) would speak fast", "es": "Nosotras hablaríamos rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "They (m) would eat meat", "es": "Ellos comerían carne", "noun_id": None, "type": "auditory", "glosses": {"meat": "carne", "carne": "meat"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Conditional — "would" do something', 'cards': [{'kind': 'text', 'title': 'Same stem as the future, different endings', 'body': 'Conditional shares the future\'s stem (full infinitive, or the same irregular shortcuts: *tendr-, har-, dir-…*). What changes are the endings: instead of future\'s -é/-ás/-á, conditional uses imperfect-style -ía endings. *Hablaría* = "I would speak."'}, {'kind': 'text', 'title': 'Use it for politeness, hypotheticals, soft suggestions', 'body': '*¿Podrías ayudarme?* (Could you help me?) — softer than "can you?" *Yo iría contigo* (I\'d go with you). *En tu lugar, hablaría con ella* (In your place, I would talk to her). It\'s the diplomat\'s tense.'}, {'kind': 'mini_table', 'title': 'vivir (to live)', 'rows': [['yo', 'viviría'], ['tú', 'vivirías'], ['él / ella / usted', 'viviría'], ['nosotros / nosotras', 'viviríamos'], ['ellos / ellas / ustedes', 'vivirían']]}, {'kind': 'mini_table', 'title': 'estudiar (to study)', 'rows': [['yo', 'estudiaría'], ['tú', 'estudiarías'], ['él / ella / usted', 'estudiaría'], ['nosotros / nosotras', 'estudiaríamos'], ['ellos / ellas / ustedes', 'estudiarían']]}], 'recall': [{'verb': 'vivir', 'answers': {'yo': 'viviría', 'tú': 'vivirías', 'él': 'viviría', 'nosotros': 'viviríamos', 'ellos': 'vivirían'}}, {'verb': 'estudiar', 'answers': {'yo': 'estudiaría', 'tú': 'estudiarías', 'él': 'estudiaría', 'nosotros': 'estudiaríamos', 'ellos': 'estudiarían'}}]},
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
            {"en": "We (m) would study together", "es": "Nosotros estudiaríamos juntos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) would live in the city", "es": "Nosotras viviríamos en la ciudad", "noun_id": "ciudad", "type": "written", "glosses": {"city": "ciudad", "ciudad": "city"}},
            {"en": "They (m) would study here", "es": "Ellos estudiarían aquí", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Conditional — "would" do something', 'cards': [{'kind': 'text', 'title': 'Same stem as the future, different endings', 'body': 'Conditional shares the future\'s stem (full infinitive, or the same irregular shortcuts: *tendr-, har-, dir-…*). What changes are the endings: instead of future\'s -é/-ás/-á, conditional uses imperfect-style -ía endings. *Hablaría* = "I would speak."'}, {'kind': 'text', 'title': 'Use it for politeness, hypotheticals, soft suggestions', 'body': '*¿Podrías ayudarme?* (Could you help me?) — softer than "can you?" *Yo iría contigo* (I\'d go with you). *En tu lugar, hablaría con ella* (In your place, I would talk to her). It\'s the diplomat\'s tense.'}, {'kind': 'mini_table', 'title': 'tener (to have)', 'rows': [['yo', 'tendría'], ['tú', 'tendrías'], ['él / ella / usted', 'tendría'], ['nosotros / nosotras', 'tendríamos'], ['ellos / ellas / ustedes', 'tendrían']]}, {'kind': 'mini_table', 'title': 'hacer (to do/make)', 'rows': [['yo', 'haría'], ['tú', 'harías'], ['él / ella / usted', 'haría'], ['nosotros / nosotras', 'haríamos'], ['ellos / ellas / ustedes', 'harían']]}], 'recall': [{'verb': 'tener', 'answers': {'yo': 'tendría', 'tú': 'tendrías', 'él': 'tendría', 'nosotros': 'tendríamos', 'ellos': 'tendrían'}}, {'verb': 'hacer', 'answers': {'yo': 'haría', 'tú': 'harías', 'él': 'haría', 'nosotros': 'haríamos', 'ellos': 'harían'}}]},
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
            {"en": "We (m) would make homework", "es": "Nosotros haríamos la tarea", "noun_id": None, "type": "auditory", "glosses": {"homework": "tarea", "tarea": "homework"}},
            {"en": "We (f) would have a house", "es": "Nosotras tendríamos una casa", "noun_id": "casa", "type": "written", "glosses": {}},
            {"en": "They (m) would make food", "es": "Ellos harían comida", "noun_id": None, "type": "auditory", "glosses": {"food": "comida", "comida": "food"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Conditional — "would" do something', 'cards': [{'kind': 'text', 'title': 'Same stem as the future, different endings', 'body': 'Conditional shares the future\'s stem (full infinitive, or the same irregular shortcuts: *tendr-, har-, dir-…*). What changes are the endings: instead of future\'s -é/-ás/-á, conditional uses imperfect-style -ía endings. *Hablaría* = "I would speak."'}, {'kind': 'text', 'title': 'Use it for politeness, hypotheticals, soft suggestions', 'body': '*¿Podrías ayudarme?* (Could you help me?) — softer than "can you?" *Yo iría contigo* (I\'d go with you). *En tu lugar, hablaría con ella* (In your place, I would talk to her). It\'s the diplomat\'s tense.'}, {'kind': 'mini_table', 'title': 'decir (to say)', 'rows': [['yo', 'diría'], ['tú', 'dirías'], ['él / ella / usted', 'diría'], ['nosotros / nosotras', 'diríamos'], ['ellos / ellas / ustedes', 'dirían']]}, {'kind': 'mini_table', 'title': 'poder (to be able)', 'rows': [['yo', 'podría'], ['tú', 'podrías'], ['él / ella / usted', 'podría'], ['nosotros / nosotras', 'podríamos'], ['ellos / ellas / ustedes', 'podrían']]}], 'recall': [{'verb': 'decir', 'answers': {'yo': 'diría', 'tú': 'dirías', 'él': 'diría', 'nosotros': 'diríamos', 'ellos': 'dirían'}}, {'verb': 'poder', 'answers': {'yo': 'podría', 'tú': 'podrías', 'él': 'podría', 'nosotros': 'podríamos', 'ellos': 'podrían'}}]},
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
            {"en": "We (m) could come", "es": "Nosotros podríamos venir", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) would say thanks", "es": "Nosotras diríamos gracias", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They (m) could help", "es": "Ellos podrían ayudar", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Preterite spelling changes — yo form only', 'cards': [{'kind': 'text', 'title': 'Same sound problem as the present, different fix', 'body': 'Some verbs need a spelling tweak in the **yo** form of the preterite to keep the original sound. The endings stay regular (-é, -aste, -ó…); only the consonant just before the ending shifts.'}, {'kind': 'text', 'title': 'Vowel-stem verbs: i → y in él / ellos', 'body': 'Verbs like **leer, creer, oír, caer, construir** — where an unstressed *i* would land between vowels — turn that i into y. *Leyó* (not *leió*). *Construyeron* (not *construieron*).'}, {'kind': 'mini_table', 'title': 'pagar (to pay)', 'rows': [['yo', 'pagué'], ['tú', 'pagaste'], ['él / ella / usted', 'pagó'], ['nosotros / nosotras', 'pagamos'], ['ellos / ellas / ustedes', 'pagaron']]}, {'kind': 'mini_table', 'title': 'jugar (to play)', 'rows': [['yo', 'jugué'], ['tú', 'jugaste'], ['él / ella / usted', 'jugó'], ['nosotros / nosotras', 'jugamos'], ['ellos / ellas / ustedes', 'jugaron']]}], 'recall': [{'verb': 'pagar', 'answers': {'yo': 'pagué', 'tú': 'pagaste', 'él': 'pagó', 'nosotros': 'pagamos', 'ellos': 'pagaron'}}, {'verb': 'jugar', 'answers': {'yo': 'jugué', 'tú': 'jugaste', 'él': 'jugó', 'nosotros': 'jugamos', 'ellos': 'jugaron'}}]},
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
            {"en": "We (m) played in the park", "es": "Nosotros jugamos en el parque", "noun_id": "parque", "type": "auditory", "glosses": {"park": "parque", "parque": "park"}},
            {"en": "We (f) paid fast", "es": "Nosotras pagamos rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "They (m) played well", "es": "Ellos jugaron bien", "noun_id": None, "type": "auditory", "glosses": {"well": "bien", "bien": "well"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Preterite spelling changes — yo form only', 'cards': [{'kind': 'text', 'title': 'Same sound problem as the present, different fix', 'body': 'Some verbs need a spelling tweak in the **yo** form of the preterite to keep the original sound. The endings stay regular (-é, -aste, -ó…); only the consonant just before the ending shifts.'}, {'kind': 'text', 'title': 'Vowel-stem verbs: i → y in él / ellos', 'body': 'Verbs like **leer, creer, oír, caer, construir** — where an unstressed *i* would land between vowels — turn that i into y. *Leyó* (not *leió*). *Construyeron* (not *construieron*).'}, {'kind': 'mini_table', 'title': 'buscar (to search)', 'rows': [['yo', 'busqué'], ['tú', 'buscaste'], ['él / ella / usted', 'buscó'], ['nosotros / nosotras', 'buscamos'], ['ellos / ellas / ustedes', 'buscaron']]}, {'kind': 'mini_table', 'title': 'tocar (to touch / play)', 'rows': [['yo', 'toqué'], ['tú', 'tocaste'], ['él / ella / usted', 'tocó'], ['nosotros / nosotras', 'tocamos'], ['ellos / ellas / ustedes', 'tocaron']]}], 'recall': [{'verb': 'buscar', 'answers': {'yo': 'busqué', 'tú': 'buscaste', 'él': 'buscó', 'nosotros': 'buscamos', 'ellos': 'buscaron'}}, {'verb': 'tocar', 'answers': {'yo': 'toqué', 'tú': 'tocaste', 'él': 'tocó', 'nosotros': 'tocamos', 'ellos': 'tocaron'}}]},
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
            {"en": "We (m) touched music", "es": "Nosotros tocamos música", "noun_id": None, "type": "auditory", "glosses": {"music": "música", "música": "music"}},
            {"en": "We (f) looked for an answer", "es": "Nosotras buscamos una respuesta", "noun_id": None, "type": "written", "glosses": {"answer": "respuesta", "respuesta": "answer"}},
            {"en": "They (m) touched the song", "es": "Ellos tocaron la canción", "noun_id": None, "type": "auditory", "glosses": {"song": "canción", "canción": "song"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Preterite spelling changes — yo form only', 'cards': [{'kind': 'text', 'title': 'Same sound problem as the present, different fix', 'body': 'Some verbs need a spelling tweak in the **yo** form of the preterite to keep the original sound. The endings stay regular (-é, -aste, -ó…); only the consonant just before the ending shifts.'}, {'kind': 'text', 'title': 'Vowel-stem verbs: i → y in él / ellos', 'body': 'Verbs like **leer, creer, oír, caer, construir** — where an unstressed *i* would land between vowels — turn that i into y. *Leyó* (not *leió*). *Construyeron* (not *construieron*).'}, {'kind': 'mini_table', 'title': 'empezar (to begin)', 'rows': [['yo', 'empecé'], ['tú', 'empezaste'], ['él / ella / usted', 'empezó'], ['nosotros / nosotras', 'empezamos'], ['ellos / ellas / ustedes', 'empezaron']]}, {'kind': 'mini_table', 'title': 'almorzar (to have lunch)', 'rows': [['yo', 'almorcé'], ['tú', 'almorzaste'], ['él / ella / usted', 'almorzó'], ['nosotros / nosotras', 'almorzamos'], ['ellos / ellas / ustedes', 'almorzaron']]}], 'recall': [{'verb': 'empezar', 'answers': {'yo': 'empecé', 'tú': 'empezaste', 'él': 'empezó', 'nosotros': 'empezamos', 'ellos': 'empezaron'}}, {'verb': 'almorzar', 'answers': {'yo': 'almorcé', 'tú': 'almorzaste', 'él': 'almorzó', 'nosotros': 'almorzamos', 'ellos': 'almorzaron'}}]},
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
            {"en": "We (m) had lunch together", "es": "Nosotros almorzamos juntos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) started now", "es": "Nosotras empezamos ahora", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They (m) had lunch here", "es": "Ellos almorzaron aquí", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Preterite spelling changes — yo form only', 'cards': [{'kind': 'text', 'title': 'Same sound problem as the present, different fix', 'body': 'Some verbs need a spelling tweak in the **yo** form of the preterite to keep the original sound. The endings stay regular (-é, -aste, -ó…); only the consonant just before the ending shifts.'}, {'kind': 'text', 'title': 'Vowel-stem verbs: i → y in él / ellos', 'body': 'Verbs like **leer, creer, oír, caer, construir** — where an unstressed *i* would land between vowels — turn that i into y. *Leyó* (not *leió*). *Construyeron* (not *construieron*).'}, {'kind': 'mini_table', 'title': 'creer (to believe)', 'rows': [['yo', 'creí'], ['tú', 'creíste'], ['él / ella / usted', 'creyó'], ['nosotros / nosotras', 'creímos'], ['ellos / ellas / ustedes', 'creyeron']]}, {'kind': 'mini_table', 'title': 'leer (to read)', 'rows': [['yo', 'leí'], ['tú', 'leíste'], ['él / ella / usted', 'leyó'], ['nosotros / nosotras', 'leímos'], ['ellos / ellas / ustedes', 'leyeron']]}], 'recall': [{'verb': 'creer', 'answers': {'yo': 'creí', 'tú': 'creíste', 'él': 'creyó', 'nosotros': 'creímos', 'ellos': 'creyeron'}}, {'verb': 'leer', 'answers': {'yo': 'leí', 'tú': 'leíste', 'él': 'leyó', 'nosotros': 'leímos', 'ellos': 'leyeron'}}]},
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
            {"en": "We (m) read the newspaper", "es": "Nosotros leímos el periódico", "noun_id": None, "type": "auditory", "glosses": {"newspaper": "periódico", "periódico": "newspaper"}},
            {"en": "We (f) believed in you", "es": "Nosotras creímos en ti", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They (m) read a lot", "es": "Ellos leyeron mucho", "noun_id": None, "type": "auditory", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Preterite spelling changes — yo form only', 'cards': [{'kind': 'text', 'title': 'Same sound problem as the present, different fix', 'body': 'Some verbs need a spelling tweak in the **yo** form of the preterite to keep the original sound. The endings stay regular (-é, -aste, -ó…); only the consonant just before the ending shifts.'}, {'kind': 'text', 'title': 'Vowel-stem verbs: i → y in él / ellos', 'body': 'Verbs like **leer, creer, oír, caer, construir** — where an unstressed *i* would land between vowels — turn that i into y. *Leyó* (not *leió*). *Construyeron* (not *construieron*).'}, {'kind': 'mini_table', 'title': 'caer (to fall)', 'rows': [['yo', 'caí'], ['tú', 'caíste'], ['él / ella / usted', 'cayó'], ['nosotros / nosotras', 'caímos'], ['ellos / ellas / ustedes', 'cayeron']]}, {'kind': 'mini_table', 'title': 'oír (to hear)', 'rows': [['yo', 'oí'], ['tú', 'oíste'], ['él / ella / usted', 'oyó'], ['nosotros / nosotras', 'oímos'], ['ellos / ellas / ustedes', 'oyeron']]}], 'recall': [{'verb': 'caer', 'answers': {'yo': 'caí', 'tú': 'caíste', 'él': 'cayó', 'nosotros': 'caímos', 'ellos': 'cayeron'}}, {'verb': 'oír', 'answers': {'yo': 'oí', 'tú': 'oíste', 'él': 'oyó', 'nosotros': 'oímos', 'ellos': 'oyeron'}}]},
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
            {"en": "We (m) heard well", "es": "Nosotros oímos bien", "noun_id": None, "type": "auditory", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "We (f) fell fast", "es": "Nosotras caímos rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "They (m) heard the radio", "es": "Ellos oyeron la radio", "noun_id": None, "type": "auditory", "glosses": {"radio": "radio"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Preterite spelling changes — yo form only', 'cards': [{'kind': 'text', 'title': 'Same sound problem as the present, different fix', 'body': 'Some verbs need a spelling tweak in the **yo** form of the preterite to keep the original sound. The endings stay regular (-é, -aste, -ó…); only the consonant just before the ending shifts.'}, {'kind': 'text', 'title': 'Vowel-stem verbs: i → y in él / ellos', 'body': 'Verbs like **leer, creer, oír, caer, construir** — where an unstressed *i* would land between vowels — turn that i into y. *Leyó* (not *leió*). *Construyeron* (not *construieron*).'}, {'kind': 'mini_table', 'title': 'construir (to build)', 'rows': [['yo', 'construí'], ['tú', 'construiste'], ['él / ella / usted', 'construyó'], ['nosotros / nosotras', 'construimos'], ['ellos / ellas / ustedes', 'construyeron']]}, {'kind': 'mini_table', 'title': 'fluir (to flow)', 'rows': [['yo', 'fluí'], ['tú', 'fluiste'], ['él / ella / usted', 'fluyó'], ['nosotros / nosotras', 'fluimos'], ['ellos / ellas / ustedes', 'fluyeron']]}], 'recall': [{'verb': 'construir', 'answers': {'yo': 'construí', 'tú': 'construiste', 'él': 'construyó', 'nosotros': 'construimos', 'ellos': 'construyeron'}}, {'verb': 'fluir', 'answers': {'yo': 'fluí', 'tú': 'fluiste', 'él': 'fluyó', 'nosotros': 'fluimos', 'ellos': 'fluyeron'}}]},
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
            {"en": "We (m) flowed naturally", "es": "Nosotros fluimos naturalmente", "noun_id": None, "type": "auditory", "glosses": {"naturally": "naturalmente", "naturalmente": "naturally"}},
            {"en": "We (f) built a house", "es": "Nosotras construimos una casa", "noun_id": "casa", "type": "written", "glosses": {"house": "casa", "casa": "house"}},
            {"en": "They (m) flowed fast", "es": "Ellos fluyeron rápido", "noun_id": None, "type": "auditory", "glosses": {"fast": "rápido", "rápido": "fast"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Strong preterites — no accents, modified stems', 'cards': [{'kind': 'text', 'title': 'A different shape — and they share endings', 'body': 'About 15 important verbs use a special preterite called the "strong" preterite. They all swap their stem (estar → estuv-, tener → tuv-, poder → pud-…) and they all share the SAME set of endings — endings with NO accent marks.'}, {'kind': 'mini_table', 'title': 'estar (to be)', 'rows': [['yo', 'estuve'], ['tú', 'estuviste'], ['él / ella / usted', 'estuvo'], ['nosotros / nosotras', 'estuvimos'], ['ellos / ellas / ustedes', 'estuvieron']]}, {'kind': 'mini_table', 'title': 'tener (to have)', 'rows': [['yo', 'tuve'], ['tú', 'tuviste'], ['él / ella / usted', 'tuvo'], ['nosotros / nosotras', 'tuvimos'], ['ellos / ellas / ustedes', 'tuvieron']]}], 'recall': [{'verb': 'estar', 'answers': {'yo': 'estuve', 'tú': 'estuviste', 'él': 'estuvo', 'nosotros': 'estuvimos', 'ellos': 'estuvieron'}}, {'verb': 'tener', 'answers': {'yo': 'tuve', 'tú': 'tuviste', 'él': 'tuvo', 'nosotros': 'tuvimos', 'ellos': 'tuvieron'}}]},
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
            {"en": "We (m) had hunger", "es": "Nosotros tuvimos hambre", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) were well", "es": "Nosotras estuvimos bien", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "They (m) had the right answer", "es": "Ellos tuvieron razón", "noun_id": None, "type": "auditory", "glosses": {"right": "razón", "razón": "right"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Strong preterites — no accents, modified stems', 'cards': [{'kind': 'text', 'title': 'A different shape — and they share endings', 'body': 'About 15 important verbs use a special preterite called the "strong" preterite. They all swap their stem (estar → estuv-, tener → tuv-, poder → pud-…) and they all share the SAME set of endings — endings with NO accent marks.'}, {'kind': 'mini_table', 'title': 'poder (to be able)', 'rows': [['yo', 'pude'], ['tú', 'pudiste'], ['él / ella / usted', 'pudo'], ['nosotros / nosotras', 'pudimos'], ['ellos / ellas / ustedes', 'pudieron']]}, {'kind': 'mini_table', 'title': 'poner (to put)', 'rows': [['yo', 'puse'], ['tú', 'pusiste'], ['él / ella / usted', 'puso'], ['nosotros / nosotras', 'pusimos'], ['ellos / ellas / ustedes', 'pusieron']]}], 'recall': [{'verb': 'poder', 'answers': {'yo': 'pude', 'tú': 'pudiste', 'él': 'pudo', 'nosotros': 'pudimos', 'ellos': 'pudieron'}}, {'verb': 'poner', 'answers': {'yo': 'puse', 'tú': 'pusiste', 'él': 'puso', 'nosotros': 'pusimos', 'ellos': 'pusieron'}}]},
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
            {"en": "We (m) put music", "es": "Nosotros pusimos música", "noun_id": None, "type": "auditory", "glosses": {"music": "música", "música": "music"}},
            {"en": "We (f) could work", "es": "Nosotras pudimos trabajar", "noun_id": "trabajo", "type": "written", "glosses": {}},
            {"en": "They (m) put the coffee", "es": "Ellos pusieron el café", "noun_id": "café", "type": "auditory", "glosses": {"coffee": "café", "café": "coffee"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Strong preterites — no accents, modified stems', 'cards': [{'kind': 'text', 'title': 'A different shape — and they share endings', 'body': 'About 15 important verbs use a special preterite called the "strong" preterite. They all swap their stem (estar → estuv-, tener → tuv-, poder → pud-…) and they all share the SAME set of endings — endings with NO accent marks.'}, {'kind': 'mini_table', 'title': 'saber (to know)', 'rows': [['yo', 'supe'], ['tú', 'supiste'], ['él / ella / usted', 'supo'], ['nosotros / nosotras', 'supimos'], ['ellos / ellas / ustedes', 'supieron']]}, {'kind': 'mini_table', 'title': 'querer (to want)', 'rows': [['yo', 'quise'], ['tú', 'quisiste'], ['él / ella / usted', 'quiso'], ['nosotros / nosotras', 'quisimos'], ['ellos / ellas / ustedes', 'quisieron']]}], 'recall': [{'verb': 'saber', 'answers': {'yo': 'supe', 'tú': 'supiste', 'él': 'supo', 'nosotros': 'supimos', 'ellos': 'supieron'}}, {'verb': 'querer', 'answers': {'yo': 'quise', 'tú': 'quisiste', 'él': 'quiso', 'nosotros': 'quisimos', 'ellos': 'quisieron'}}]},
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
            {"en": "We (m) wanted coffee", "es": "Nosotros quisimos café", "noun_id": "café", "type": "auditory", "glosses": {"coffee": "café", "café": "coffee"}},
            {"en": "We (f) knew the answer", "es": "Nosotras supimos la respuesta", "noun_id": None, "type": "written", "glosses": {"answer": "respuesta", "respuesta": "answer"}},
            {"en": "They (m) wanted water", "es": "Ellos quisieron agua", "noun_id": None, "type": "auditory", "glosses": {"water": "agua", "agua": "water"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Strong preterites — no accents, modified stems', 'cards': [{'kind': 'text', 'title': 'A different shape — and they share endings', 'body': 'About 15 important verbs use a special preterite called the "strong" preterite. They all swap their stem (estar → estuv-, tener → tuv-, poder → pud-…) and they all share the SAME set of endings — endings with NO accent marks.'}, {'kind': 'mini_table', 'title': 'andar (to walk)', 'rows': [['yo', 'anduve'], ['tú', 'anduviste'], ['él / ella / usted', 'anduvo'], ['nosotros / nosotras', 'anduvimos'], ['ellos / ellas / ustedes', 'anduvieron']]}, {'kind': 'mini_table', 'title': 'venir (to come)', 'rows': [['yo', 'vine'], ['tú', 'viniste'], ['él / ella / usted', 'vino'], ['nosotros / nosotras', 'vinimos'], ['ellos / ellas / ustedes', 'vinieron']]}], 'recall': [{'verb': 'andar', 'answers': {'yo': 'anduve', 'tú': 'anduviste', 'él': 'anduvo', 'nosotros': 'anduvimos', 'ellos': 'anduvieron'}}, {'verb': 'venir', 'answers': {'yo': 'vine', 'tú': 'viniste', 'él': 'vino', 'nosotros': 'vinimos', 'ellos': 'vinieron'}}]},
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
            {"en": "We (m) came from the park", "es": "Nosotros vinimos del parque", "noun_id": "parque", "type": "auditory", "glosses": {"park": "parque", "parque": "park"}},
            {"en": "We (f) walked through the park", "es": "Nosotras anduvimos por el parque", "noun_id": "parque", "type": "written", "glosses": {"park": "parque", "parque": "park"}},
            {"en": "They (m) came early", "es": "Ellos vinieron temprano", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Strong preterites — no accents, modified stems', 'cards': [{'kind': 'text', 'title': 'A different shape — and they share endings', 'body': 'About 15 important verbs use a special preterite called the "strong" preterite. They all swap their stem (estar → estuv-, tener → tuv-, poder → pud-…) and they all share the SAME set of endings — endings with NO accent marks.'}, {'kind': 'mini_table', 'title': 'haber (to have, aux.)', 'rows': [['yo', 'hube'], ['tú', 'hubiste'], ['él / ella / usted', 'hubo'], ['nosotros / nosotras', 'hubimos'], ['ellos / ellas / ustedes', 'hubieron']]}, {'kind': 'mini_table', 'title': 'caber (to fit)', 'rows': [['yo', 'cupe'], ['tú', 'cupiste'], ['él / ella / usted', 'cupo'], ['nosotros / nosotras', 'cupimos'], ['ellos / ellas / ustedes', 'cupieron']]}], 'recall': [{'verb': 'haber', 'answers': {'yo': 'hube', 'tú': 'hubiste', 'él': 'hubo', 'nosotros': 'hubimos', 'ellos': 'hubieron'}}, {'verb': 'caber', 'answers': {'yo': 'cupe', 'tú': 'cupiste', 'él': 'cupo', 'nosotros': 'cupimos', 'ellos': 'cupieron'}}]},
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
            {"en": "We (m) fit inside", "es": "Nosotros cupimos dentro", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) had lived", "es": "Nosotras hubimos vivido", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They (m) fit well", "es": "Ellos cupieron bien", "noun_id": None, "type": "auditory", "glosses": {"well": "bien", "bien": "well"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Strong preterites — no accents, modified stems', 'cards': [{'kind': 'text', 'title': 'A different shape — and they share endings', 'body': 'About 15 important verbs use a special preterite called the "strong" preterite. They all swap their stem (estar → estuv-, tener → tuv-, poder → pud-…) and they all share the SAME set of endings — endings with NO accent marks.'}, {'kind': 'mini_table', 'title': 'mantener (to maintain)', 'rows': [['yo', 'mantuve'], ['tú', 'mantuviste'], ['él / ella / usted', 'mantuvo'], ['nosotros / nosotras', 'mantuvimos'], ['ellos / ellas / ustedes', 'mantuvieron']]}, {'kind': 'mini_table', 'title': 'obtener (to obtain)', 'rows': [['yo', 'obtuve'], ['tú', 'obtuviste'], ['él / ella / usted', 'obtuvo'], ['nosotros / nosotras', 'obtuvimos'], ['ellos / ellas / ustedes', 'obtuvieron']]}], 'recall': [{'verb': 'mantener', 'answers': {'yo': 'mantuve', 'tú': 'mantuviste', 'él': 'mantuvo', 'nosotros': 'mantuvimos', 'ellos': 'mantuvieron'}}, {'verb': 'obtener', 'answers': {'yo': 'obtuve', 'tú': 'obtuviste', 'él': 'obtuvo', 'nosotros': 'obtuvimos', 'ellos': 'obtuvieron'}}]},
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
            {"en": "We (m) obtained information", "es": "Nosotros obtuvimos información", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "We (f) maintained calm", "es": "Nosotras mantuvimos la calma", "noun_id": None, "type": "written", "glosses": {"calm": "calma", "calma": "calm"}},
            {"en": "They (m) obtained the book", "es": "Ellos obtuvieron el libro", "noun_id": "libro", "type": "auditory", "glosses": {"book": "libro", "libro": "book"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Preterite of -ducir verbs', 'cards': [{'kind': 'text', 'title': 'All -DUCIR verbs use the j-stem pattern', 'body': 'Every Spanish verb ending in **-ducir** (traducir, conducir, producir, introducir, reducir…) uses the same preterite: stem ends in **-duj-** and takes strong-preterite endings. They share a special quirk with decir and traer: the ellos form drops the i.'}, {'kind': 'mini_table', 'title': 'traducir (to translate)', 'rows': [['yo', 'traduje'], ['tú', 'tradujiste'], ['él / ella / usted', 'tradujo'], ['nosotros / nosotras', 'tradujimos'], ['ellos / ellas / ustedes', 'tradujeron']]}, {'kind': 'mini_table', 'title': 'conducir (to drive)', 'rows': [['yo', 'conduje'], ['tú', 'condujiste'], ['él / ella / usted', 'condujo'], ['nosotros / nosotras', 'condujimos'], ['ellos / ellas / ustedes', 'condujeron']]}], 'recall': [{'verb': 'traducir', 'answers': {'yo': 'traduje', 'tú': 'tradujiste', 'él': 'tradujo', 'nosotros': 'tradujimos', 'ellos': 'tradujeron'}}, {'verb': 'conducir', 'answers': {'yo': 'conduje', 'tú': 'condujiste', 'él': 'condujo', 'nosotros': 'condujimos', 'ellos': 'condujeron'}}]},
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
            {"en": "We (m) drove to the city", "es": "Nosotros condujimos a la ciudad", "noun_id": "ciudad", "type": "auditory", "glosses": {"city": "ciudad", "ciudad": "city"}},
            {"en": "We (f) translated well", "es": "Nosotras tradujimos bien", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They (m) drove carefully", "es": "Ellos condujeron con cuidado", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Preterite of -ducir verbs', 'cards': [{'kind': 'text', 'title': 'All -DUCIR verbs use the j-stem pattern', 'body': 'Every Spanish verb ending in **-ducir** (traducir, conducir, producir, introducir, reducir…) uses the same preterite: stem ends in **-duj-** and takes strong-preterite endings. They share a special quirk with decir and traer: the ellos form drops the i.'}, {'kind': 'mini_table', 'title': 'producir (to produce)', 'rows': [['yo', 'produje'], ['tú', 'produjiste'], ['él / ella / usted', 'produjo'], ['nosotros / nosotras', 'produjimos'], ['ellos / ellas / ustedes', 'produjeron']]}, {'kind': 'mini_table', 'title': 'introducir (to introduce)', 'rows': [['yo', 'introduje'], ['tú', 'introdujiste'], ['él / ella / usted', 'introdujo'], ['nosotros / nosotras', 'introdujimos'], ['ellos / ellas / ustedes', 'introdujeron']]}], 'recall': [{'verb': 'producir', 'answers': {'yo': 'produje', 'tú': 'produjiste', 'él': 'produjo', 'nosotros': 'produjimos', 'ellos': 'produjeron'}}, {'verb': 'introducir', 'answers': {'yo': 'introduje', 'tú': 'introdujiste', 'él': 'introdujo', 'nosotros': 'introdujimos', 'ellos': 'introdujeron'}}]},
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
            {"en": "We (m) introduced the topic", "es": "Nosotros introdujimos el tema", "noun_id": None, "type": "auditory", "glosses": {"topic": "tema", "tema": "topic"}},
            {"en": "We (f) produced results", "es": "Nosotras produjimos resultados", "noun_id": None, "type": "written", "glosses": {"results": "resultados", "resultados": "results"}},
            {"en": "They (m) introduced the information", "es": "Ellos introdujeron la información", "noun_id": None, "type": "auditory", "glosses": {"information": "información", "información": "information"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Preterite e→i — only -ir stem-changers', 'cards': [{'kind': 'text', 'title': 'A small change in just two forms', 'body': '**-ir verbs** that have a stem change in the present (pedir, sentir, repetir, servir, dormir, morir) keep a smaller version of that change in the preterite — but only in the **él** and **ellos** forms. Everything else is regular.'}, {'kind': 'mini_table', 'title': 'pedir (to ask for)', 'rows': [['yo', 'pedí'], ['tú', 'pediste'], ['él / ella / usted', 'pidió'], ['nosotros / nosotras', 'pedimos'], ['ellos / ellas / ustedes', 'pidieron']]}, {'kind': 'mini_table', 'title': 'sentir (to feel)', 'rows': [['yo', 'sentí'], ['tú', 'sentiste'], ['él / ella / usted', 'sintió'], ['nosotros / nosotras', 'sentimos'], ['ellos / ellas / ustedes', 'sintieron']]}], 'recall': [{'verb': 'pedir', 'answers': {'yo': 'pedí', 'tú': 'pediste', 'él': 'pidió', 'nosotros': 'pedimos', 'ellos': 'pidieron'}}, {'verb': 'sentir', 'answers': {'yo': 'sentí', 'tú': 'sentiste', 'él': 'sintió', 'nosotros': 'sentimos', 'ellos': 'sintieron'}}]},
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
            {"en": "We (m) felt the music", "es": "Nosotros sentimos la música", "noun_id": None, "type": "auditory", "glosses": {"music": "música", "música": "music"}},
            {"en": "We (f) asked for the bill", "es": "Nosotras pedimos la cuenta", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "They (m) felt pain", "es": "Ellos sintieron dolor", "noun_id": None, "type": "auditory", "glosses": {"pain": "dolor", "dolor": "pain"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Preterite e→i — only -ir stem-changers', 'cards': [{'kind': 'text', 'title': 'A small change in just two forms', 'body': '**-ir verbs** that have a stem change in the present (pedir, sentir, repetir, servir, dormir, morir) keep a smaller version of that change in the preterite — but only in the **él** and **ellos** forms. Everything else is regular.'}, {'kind': 'mini_table', 'title': 'repetir (to repeat)', 'rows': [['yo', 'repetí'], ['tú', 'repetiste'], ['él / ella / usted', 'repitió'], ['nosotros / nosotras', 'repetimos'], ['ellos / ellas / ustedes', 'repitieron']]}, {'kind': 'mini_table', 'title': 'servir (to serve)', 'rows': [['yo', 'serví'], ['tú', 'serviste'], ['él / ella / usted', 'sirvió'], ['nosotros / nosotras', 'servimos'], ['ellos / ellas / ustedes', 'sirvieron']]}], 'recall': [{'verb': 'repetir', 'answers': {'yo': 'repetí', 'tú': 'repetiste', 'él': 'repitió', 'nosotros': 'repetimos', 'ellos': 'repitieron'}}, {'verb': 'servir', 'answers': {'yo': 'serví', 'tú': 'serviste', 'él': 'sirvió', 'nosotros': 'servimos', 'ellos': 'sirvieron'}}]},
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
            {"en": "We (m) served the customers", "es": "Nosotros servimos a los clientes", "noun_id": None, "type": "auditory", "glosses": {"customers": "clientes", "clientes": "customers"}},
            {"en": "We (f) repeated fast", "es": "Nosotras repetimos rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "They (m) served wine", "es": "Ellos sirvieron vino", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Present Subjunctive — for desires, doubts, emotions', 'cards': [{'kind': 'text', 'title': 'Not a tense — a mood', 'body': "The subjunctive isn't about *when* — it's about *attitude*. You use it when the speaker is expressing wishes, doubts, emotions, or things that aren't yet real: *Espero que vengas* (I hope you come). *Quiero que sepa la verdad* (I want him to know)."}, {'kind': 'text', 'title': 'Trigger phrases (the WEDDING acronym)', 'body': '**W**ish: *quiero que…*  **E**motion: *me alegro de que…*  **D**oubt: *dudo que…*  **D**enial: *no creo que…*  **I**mpersonal: *es importante que…*  **N**egation: *no es verdad que…*  **G**od / wishes: *ojalá que…*  When you see one of these phrases, the verb that follows goes in the subjunctive.'}, {'kind': 'mini_table', 'title': 'hablar (to speak)', 'rows': [['yo', 'hable'], ['tú', 'hables'], ['él / ella / usted', 'hable'], ['nosotros / nosotras', 'hablemos'], ['ellos / ellas / ustedes', 'hablen']]}, {'kind': 'mini_table', 'title': 'comer (to eat)', 'rows': [['yo', 'coma'], ['tú', 'comas'], ['él / ella / usted', 'coma'], ['nosotros / nosotras', 'comamos'], ['ellos / ellas / ustedes', 'coman']]}], 'recall': [{'verb': 'hablar', 'answers': {'yo': 'hable', 'tú': 'hables', 'él': 'hable', 'nosotros': 'hablemos', 'ellos': 'hablen'}}, {'verb': 'comer', 'answers': {'yo': 'coma', 'tú': 'comas', 'él': 'coma', 'nosotros': 'comamos', 'ellos': 'coman'}}]},
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
            {"en": "I hope that we (m) eat fruit", "es": "Espero que nosotros comamos fruta", "noun_id": None, "type": "auditory", "glosses": {"fruit": "fruta", "fruta": "fruit"}},
            {"en": "I hope that we (f) speak fast", "es": "Espero que nosotras hablemos rápido", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
            {"en": "I hope that they (m) eat meat", "es": "Espero que ellos coman carne", "noun_id": None, "type": "auditory", "glosses": {"meat": "carne", "carne": "meat"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Present Subjunctive — for desires, doubts, emotions', 'cards': [{'kind': 'text', 'title': 'Not a tense — a mood', 'body': "The subjunctive isn't about *when* — it's about *attitude*. You use it when the speaker is expressing wishes, doubts, emotions, or things that aren't yet real: *Espero que vengas* (I hope you come). *Quiero que sepa la verdad* (I want him to know)."}, {'kind': 'text', 'title': 'Trigger phrases (the WEDDING acronym)', 'body': '**W**ish: *quiero que…*  **E**motion: *me alegro de que…*  **D**oubt: *dudo que…*  **D**enial: *no creo que…*  **I**mpersonal: *es importante que…*  **N**egation: *no es verdad que…*  **G**od / wishes: *ojalá que…*  When you see one of these phrases, the verb that follows goes in the subjunctive.'}, {'kind': 'mini_table', 'title': 'vivir (to live)', 'rows': [['yo', 'viva'], ['tú', 'vivas'], ['él / ella / usted', 'viva'], ['nosotros / nosotras', 'vivamos'], ['ellos / ellas / ustedes', 'vivan']]}, {'kind': 'mini_table', 'title': 'estudiar (to study)', 'rows': [['yo', 'estudie'], ['tú', 'estudies'], ['él / ella / usted', 'estudie'], ['nosotros / nosotras', 'estudiemos'], ['ellos / ellas / ustedes', 'estudien']]}], 'recall': [{'verb': 'vivir', 'answers': {'yo': 'viva', 'tú': 'vivas', 'él': 'viva', 'nosotros': 'vivamos', 'ellos': 'vivan'}}, {'verb': 'estudiar', 'answers': {'yo': 'estudie', 'tú': 'estudies', 'él': 'estudie', 'nosotros': 'estudiemos', 'ellos': 'estudien'}}]},
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
            {"en": "I hope that we (m) study together", "es": "Espero que nosotros estudiemos juntos", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "I hope that we (f) live in the city", "es": "Espero que nosotras vivamos en la ciudad", "noun_id": "ciudad", "type": "written", "glosses": {"city": "ciudad", "ciudad": "city"}},
            {"en": "I hope that they (m) study here", "es": "Espero que ellos estudien aquí", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Present Subjunctive — for desires, doubts, emotions', 'cards': [{'kind': 'text', 'title': 'Not a tense — a mood', 'body': "The subjunctive isn't about *when* — it's about *attitude*. You use it when the speaker is expressing wishes, doubts, emotions, or things that aren't yet real: *Espero que vengas* (I hope you come). *Quiero que sepa la verdad* (I want him to know)."}, {'kind': 'text', 'title': 'Trigger phrases (the WEDDING acronym)', 'body': '**W**ish: *quiero que…*  **E**motion: *me alegro de que…*  **D**oubt: *dudo que…*  **D**enial: *no creo que…*  **I**mpersonal: *es importante que…*  **N**egation: *no es verdad que…*  **G**od / wishes: *ojalá que…*  When you see one of these phrases, the verb that follows goes in the subjunctive.'}, {'kind': 'mini_table', 'title': 'ser (to be)', 'rows': [['yo', 'sea'], ['tú', 'seas'], ['él / ella / usted', 'sea'], ['nosotros / nosotras', 'seamos'], ['ellos / ellas / ustedes', 'sean']]}, {'kind': 'mini_table', 'title': 'ir (to go)', 'rows': [['yo', 'vaya'], ['tú', 'vayas'], ['él / ella / usted', 'vaya'], ['nosotros / nosotras', 'vayamos'], ['ellos / ellas / ustedes', 'vayan']]}], 'recall': [{'verb': 'ser', 'answers': {'yo': 'sea', 'tú': 'seas', 'él': 'sea', 'nosotros': 'seamos', 'ellos': 'sean'}}, {'verb': 'ir', 'answers': {'yo': 'vaya', 'tú': 'vayas', 'él': 'vaya', 'nosotros': 'vayamos', 'ellos': 'vayan'}}]},
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
            {"en": "I hope that we (m) go to the market", "es": "Espero que nosotros vayamos al mercado", "noun_id": "mercado", "type": "auditory", "glosses": {"market": "mercado", "mercado": "market"}},
            {"en": "I hope that we (f) are professional", "es": "Espero que nosotras seamos profesional", "noun_id": None, "type": "written", "glosses": {"professional": "profesional", "profesional": "professional"}},
            {"en": "I hope that they (m) go home", "es": "Espero que ellos vayan a casa", "noun_id": "casa", "type": "auditory", "glosses": {"home": "casa", "casa": "home"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Present Subjunctive — for desires, doubts, emotions', 'cards': [{'kind': 'text', 'title': 'Not a tense — a mood', 'body': "The subjunctive isn't about *when* — it's about *attitude*. You use it when the speaker is expressing wishes, doubts, emotions, or things that aren't yet real: *Espero que vengas* (I hope you come). *Quiero que sepa la verdad* (I want him to know)."}, {'kind': 'text', 'title': 'Trigger phrases (the WEDDING acronym)', 'body': '**W**ish: *quiero que…*  **E**motion: *me alegro de que…*  **D**oubt: *dudo que…*  **D**enial: *no creo que…*  **I**mpersonal: *es importante que…*  **N**egation: *no es verdad que…*  **G**od / wishes: *ojalá que…*  When you see one of these phrases, the verb that follows goes in the subjunctive.'}, {'kind': 'mini_table', 'title': 'estar (to be)', 'rows': [['yo', 'esté'], ['tú', 'estés'], ['él / ella / usted', 'esté'], ['nosotros / nosotras', 'estemos'], ['ellos / ellas / ustedes', 'estén']]}, {'kind': 'mini_table', 'title': 'dar (to give)', 'rows': [['yo', 'dé'], ['tú', 'des'], ['él / ella / usted', 'dé'], ['nosotros / nosotras', 'demos'], ['ellos / ellas / ustedes', 'den']]}], 'recall': [{'verb': 'estar', 'answers': {'yo': 'esté', 'tú': 'estés', 'él': 'esté', 'nosotros': 'estemos', 'ellos': 'estén'}}, {'verb': 'dar', 'answers': {'yo': 'dé', 'tú': 'des', 'él': 'dé', 'nosotros': 'demos', 'ellos': 'den'}}]},
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
            {"en": "I hope that we (m) give money", "es": "Espero que nosotros demos dinero", "noun_id": "dinero", "type": "auditory", "glosses": {"money": "dinero", "dinero": "money"}},
            {"en": "I hope that we (f) are tired", "es": "Espero que nosotras estemos cansado", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "I hope that they (m) give water", "es": "Espero que ellos den agua", "noun_id": None, "type": "auditory", "glosses": {"water": "agua", "agua": "water"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Present Subjunctive — for desires, doubts, emotions', 'cards': [{'kind': 'text', 'title': 'Not a tense — a mood', 'body': "The subjunctive isn't about *when* — it's about *attitude*. You use it when the speaker is expressing wishes, doubts, emotions, or things that aren't yet real: *Espero que vengas* (I hope you come). *Quiero que sepa la verdad* (I want him to know)."}, {'kind': 'text', 'title': 'Trigger phrases (the WEDDING acronym)', 'body': '**W**ish: *quiero que…*  **E**motion: *me alegro de que…*  **D**oubt: *dudo que…*  **D**enial: *no creo que…*  **I**mpersonal: *es importante que…*  **N**egation: *no es verdad que…*  **G**od / wishes: *ojalá que…*  When you see one of these phrases, the verb that follows goes in the subjunctive.'}, {'kind': 'mini_table', 'title': 'saber (to know)', 'rows': [['yo', 'sepa'], ['tú', 'sepas'], ['él / ella / usted', 'sepa'], ['nosotros / nosotras', 'sepamos'], ['ellos / ellas / ustedes', 'sepan']]}, {'kind': 'mini_table', 'title': 'haber (to have, aux.)', 'rows': [['yo', 'haya'], ['tú', 'hayas'], ['él / ella / usted', 'haya'], ['nosotros / nosotras', 'hayamos'], ['ellos / ellas / ustedes', 'hayan']]}], 'recall': [{'verb': 'saber', 'answers': {'yo': 'sepa', 'tú': 'sepas', 'él': 'sepa', 'nosotros': 'sepamos', 'ellos': 'sepan'}}, {'verb': 'haber', 'answers': {'yo': 'haya', 'tú': 'hayas', 'él': 'haya', 'nosotros': 'hayamos', 'ellos': 'hayan'}}]},
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
            {"en": "I hope that we (m) have gone", "es": "Espero que nosotros hayamos ido", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "I hope that we (f) know how to cook", "es": "Espero que nosotras sepamos cocinar", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "I hope that they (m) have lived", "es": "Espero que ellos hayan vivido", "noun_id": None, "type": "auditory", "glosses": {}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Imperfect Subjunctive — past wishes, hypotheticals', 'cards': [{'kind': 'text', 'title': 'Same triggers as present subjunctive, but in a past context', 'body': 'Same WEDDING triggers (wishes, doubts, emotions…), but for past or hypothetical situations: *Quería que vinieras* (I wanted you to come). *Si tuviera dinero…* (If I had money…). It\'s also the workhorse of "if I were" sentences.'}, {'kind': 'text', 'title': 'Built from the THIRD-person preterite', 'body': "Take the **ellos** form of the preterite, drop the -ron, and add new endings: *hablaron → habla- → hablara, hablaras…* Because it's based on the preterite, every preterite irregularity comes along for the ride."}, {'kind': 'text', 'title': 'Two valid endings: -ra and -se', 'body': "There's an alternate form ending in -se: *hablase, hablases, hablase, hablásemos, hablasen*. They're interchangeable, but the **-ra form is far more common** in everyday speech and is what we'll teach. Recognize -se when you read; produce -ra when you speak."}, {'kind': 'mini_table', 'title': 'hablar (to speak)', 'rows': [['yo', 'hablara'], ['tú', 'hablaras'], ['él / ella / usted', 'hablara'], ['nosotros / nosotras', 'habláramos'], ['ellos / ellas / ustedes', 'hablaran']]}, {'kind': 'mini_table', 'title': 'comer (to eat)', 'rows': [['yo', 'comiera'], ['tú', 'comieras'], ['él / ella / usted', 'comiera'], ['nosotros / nosotras', 'comiéramos'], ['ellos / ellas / ustedes', 'comieran']]}], 'recall': [{'verb': 'hablar', 'answers': {'yo': 'hablara', 'tú': 'hablaras', 'él': 'hablara', 'nosotros': 'habláramos', 'ellos': 'hablaran'}}, {'verb': 'comer', 'answers': {'yo': 'comiera', 'tú': 'comieras', 'él': 'comiera', 'nosotros': 'comiéramos', 'ellos': 'comieran'}}]},
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
            {"en": "If we (m) ate bread", "es": "Si nosotros comiéramos pan", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "If we (f) spoke English", "es": "Si nosotras habláramos inglés", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "If they (m) ate food", "es": "Si ellos comieran comida", "noun_id": None, "type": "auditory", "glosses": {"food": "comida", "comida": "food"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Imperfect Subjunctive — past wishes, hypotheticals', 'cards': [{'kind': 'text', 'title': 'Same triggers as present subjunctive, but in a past context', 'body': 'Same WEDDING triggers (wishes, doubts, emotions…), but for past or hypothetical situations: *Quería que vinieras* (I wanted you to come). *Si tuviera dinero…* (If I had money…). It\'s also the workhorse of "if I were" sentences.'}, {'kind': 'text', 'title': 'Built from the THIRD-person preterite', 'body': "Take the **ellos** form of the preterite, drop the -ron, and add new endings: *hablaron → habla- → hablara, hablaras…* Because it's based on the preterite, every preterite irregularity comes along for the ride."}, {'kind': 'text', 'title': 'Two valid endings: -ra and -se', 'body': "There's an alternate form ending in -se: *hablase, hablases, hablase, hablásemos, hablasen*. They're interchangeable, but the **-ra form is far more common** in everyday speech and is what we'll teach. Recognize -se when you read; produce -ra when you speak."}, {'kind': 'mini_table', 'title': 'vivir (to live)', 'rows': [['yo', 'viviera'], ['tú', 'vivieras'], ['él / ella / usted', 'viviera'], ['nosotros / nosotras', 'viviéramos'], ['ellos / ellas / ustedes', 'vivieran']]}, {'kind': 'mini_table', 'title': 'estudiar (to study)', 'rows': [['yo', 'estudiara'], ['tú', 'estudiaras'], ['él / ella / usted', 'estudiara'], ['nosotros / nosotras', 'estudiáramos'], ['ellos / ellas / ustedes', 'estudiaran']]}], 'recall': [{'verb': 'vivir', 'answers': {'yo': 'viviera', 'tú': 'vivieras', 'él': 'viviera', 'nosotros': 'viviéramos', 'ellos': 'vivieran'}}, {'verb': 'estudiar', 'answers': {'yo': 'estudiara', 'tú': 'estudiaras', 'él': 'estudiara', 'nosotros': 'estudiáramos', 'ellos': 'estudiaran'}}]},
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
            {"en": "If we (m) studied a lot", "es": "Si nosotros estudiáramos mucho", "noun_id": None, "type": "auditory", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "If we (f) lived together", "es": "Si nosotras viviéramos juntos", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "If they (m) studied at home", "es": "Si ellos estudiaran en casa", "noun_id": "casa", "type": "auditory", "glosses": {"at home": "en casa", "en casa": "at home"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Imperfect Subjunctive — past wishes, hypotheticals', 'cards': [{'kind': 'text', 'title': 'Same triggers as present subjunctive, but in a past context', 'body': 'Same WEDDING triggers (wishes, doubts, emotions…), but for past or hypothetical situations: *Quería que vinieras* (I wanted you to come). *Si tuviera dinero…* (If I had money…). It\'s also the workhorse of "if I were" sentences.'}, {'kind': 'text', 'title': 'Built from the THIRD-person preterite', 'body': "Take the **ellos** form of the preterite, drop the -ron, and add new endings: *hablaron → habla- → hablara, hablaras…* Because it's based on the preterite, every preterite irregularity comes along for the ride."}, {'kind': 'text', 'title': 'Two valid endings: -ra and -se', 'body': "There's an alternate form ending in -se: *hablase, hablases, hablase, hablásemos, hablasen*. They're interchangeable, but the **-ra form is far more common** in everyday speech and is what we'll teach. Recognize -se when you read; produce -ra when you speak."}, {'kind': 'mini_table', 'title': 'ser (to be)', 'rows': [['yo', 'fuera'], ['tú', 'fueras'], ['él / ella / usted', 'fuera'], ['nosotros / nosotras', 'fuéramos'], ['ellos / ellas / ustedes', 'fueran']]}, {'kind': 'mini_table', 'title': 'tener (to have)', 'rows': [['yo', 'tuviera'], ['tú', 'tuvieras'], ['él / ella / usted', 'tuviera'], ['nosotros / nosotras', 'tuviéramos'], ['ellos / ellas / ustedes', 'tuvieran']]}], 'recall': [{'verb': 'ser', 'answers': {'yo': 'fuera', 'tú': 'fueras', 'él': 'fuera', 'nosotros': 'fuéramos', 'ellos': 'fueran'}}, {'verb': 'tener', 'answers': {'yo': 'tuviera', 'tú': 'tuvieras', 'él': 'tuviera', 'nosotros': 'tuviéramos', 'ellos': 'tuvieran'}}]},
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
            {"en": "If we (m) had the right answer", "es": "Si nosotros tuviéramos razón", "noun_id": None, "type": "auditory", "glosses": {"right": "razón", "razón": "right"}},
            {"en": "If we (f) were Colombian", "es": "Si nosotras fuéramos colombiano", "noun_id": None, "type": "written", "glosses": {}},
            {"en": "If they (m) had time", "es": "Si ellos tuvieran tiempo", "noun_id": "tiempo", "type": "auditory", "glosses": {"time": "tiempo", "tiempo": "time"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Imperfect Subjunctive — past wishes, hypotheticals', 'cards': [{'kind': 'text', 'title': 'Same triggers as present subjunctive, but in a past context', 'body': 'Same WEDDING triggers (wishes, doubts, emotions…), but for past or hypothetical situations: *Quería que vinieras* (I wanted you to come). *Si tuviera dinero…* (If I had money…). It\'s also the workhorse of "if I were" sentences.'}, {'kind': 'text', 'title': 'Built from the THIRD-person preterite', 'body': "Take the **ellos** form of the preterite, drop the -ron, and add new endings: *hablaron → habla- → hablara, hablaras…* Because it's based on the preterite, every preterite irregularity comes along for the ride."}, {'kind': 'text', 'title': 'Two valid endings: -ra and -se', 'body': "There's an alternate form ending in -se: *hablase, hablases, hablase, hablásemos, hablasen*. They're interchangeable, but the **-ra form is far more common** in everyday speech and is what we'll teach. Recognize -se when you read; produce -ra when you speak."}, {'kind': 'mini_table', 'title': 'hacer (to do/make)', 'rows': [['yo', 'hiciera'], ['tú', 'hicieras'], ['él / ella / usted', 'hiciera'], ['nosotros / nosotras', 'hiciéramos'], ['ellos / ellas / ustedes', 'hicieran']]}, {'kind': 'mini_table', 'title': 'querer (to want)', 'rows': [['yo', 'quisiera'], ['tú', 'quisieras'], ['él / ella / usted', 'quisiera'], ['nosotros / nosotras', 'quisiéramos'], ['ellos / ellas / ustedes', 'quisieran']]}], 'recall': [{'verb': 'hacer', 'answers': {'yo': 'hiciera', 'tú': 'hicieras', 'él': 'hiciera', 'nosotros': 'hiciéramos', 'ellos': 'hicieran'}}, {'verb': 'querer', 'answers': {'yo': 'quisiera', 'tú': 'quisieras', 'él': 'quisiera', 'nosotros': 'quisiéramos', 'ellos': 'quisieran'}}]},
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
            {"en": "If we (m) wanted to rest", "es": "Si nosotros quisiéramos descansar", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "If we (f) made homework", "es": "Si nosotras hiciéramos la tarea", "noun_id": None, "type": "written", "glosses": {"homework": "tarea", "tarea": "homework"}},
            {"en": "If they (m) wanted coffee", "es": "Si ellos quisieran café", "noun_id": "café", "type": "auditory", "glosses": {"coffee": "café", "café": "coffee"}},
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
        "intro_chart": {'kind': 'cards', 'title': 'Imperfect Subjunctive — past wishes, hypotheticals', 'cards': [{'kind': 'text', 'title': 'Same triggers as present subjunctive, but in a past context', 'body': 'Same WEDDING triggers (wishes, doubts, emotions…), but for past or hypothetical situations: *Quería que vinieras* (I wanted you to come). *Si tuviera dinero…* (If I had money…). It\'s also the workhorse of "if I were" sentences.'}, {'kind': 'text', 'title': 'Built from the THIRD-person preterite', 'body': "Take the **ellos** form of the preterite, drop the -ron, and add new endings: *hablaron → habla- → hablara, hablaras…* Because it's based on the preterite, every preterite irregularity comes along for the ride."}, {'kind': 'text', 'title': 'Two valid endings: -ra and -se', 'body': "There's an alternate form ending in -se: *hablase, hablases, hablase, hablásemos, hablasen*. They're interchangeable, but the **-ra form is far more common** in everyday speech and is what we'll teach. Recognize -se when you read; produce -ra when you speak."}, {'kind': 'mini_table', 'title': 'decir (to say)', 'rows': [['yo', 'dijera'], ['tú', 'dijeras'], ['él / ella / usted', 'dijera'], ['nosotros / nosotras', 'dijéramos'], ['ellos / ellas / ustedes', 'dijeran']]}, {'kind': 'mini_table', 'title': 'poder (to be able)', 'rows': [['yo', 'pudiera'], ['tú', 'pudieras'], ['él / ella / usted', 'pudiera'], ['nosotros / nosotras', 'pudiéramos'], ['ellos / ellas / ustedes', 'pudieran']]}], 'recall': [{'verb': 'decir', 'answers': {'yo': 'dijera', 'tú': 'dijeras', 'él': 'dijera', 'nosotros': 'dijéramos', 'ellos': 'dijeran'}}, {'verb': 'poder', 'answers': {'yo': 'pudiera', 'tú': 'pudieras', 'él': 'pudiera', 'nosotros': 'pudiéramos', 'ellos': 'pudieran'}}]},
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
            {"en": "If we (m) could come", "es": "Si nosotros pudiéramos venir", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "If we (f) said thanks", "es": "Si nosotras dijéramos gracias", "noun_id": None, "type": "written", "glosses": {"thanks": "gracias", "gracias": "thanks"}},
            {"en": "If they (m) could help", "es": "Si ellos pudieran ayudar", "noun_id": None, "type": "auditory", "glosses": {}},
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


    # ─────────────────────────────────────────────────────────────────────────
    # Phase C.3 sub-block lessons — auto-spliced from scripts/_glX_output.py
    # ─────────────────────────────────────────────────────────────────────────

    # ── From _gl4_5_output.py ──

"grammar_irregular_present_ii_hacer_poner_1": {
        "title": "Irregular Present II — hacer + poner (1/2)",
        "grammar_level": 4.5,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ["hacer", "poner"],
        "video_embed_id": "Bg9XcrNn3LL",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": IRREGULAR_PRESENT_II_HACER_PONER_INTRO,
        "drill_config": {
            "answers": {
                "hacer": {"yo": "ha|go", "tú": "hac|es", "él": "hac|e", "ella": "hac|e", "usted": "hac|e", "nosotros": "hac|emos", "nosotras": "hac|emos", "ellos": "hac|en", "ellas": "hac|en", "ustedes": "hac|en"},
                "poner": {"yo": "pon|go", "tú": "pon|es", "él": "pon|e", "ella": "pon|e", "usted": "pon|e", "nosotros": "pon|emos", "nosotras": "pon|emos", "ellos": "pon|en", "ellas": "pon|en", "ustedes": "pon|en"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": 'I put the keys here.', "es": 'Yo pongo las llaves aquí.', "noun_id": None, "type": 'auditory', "glosses": {'keys': 'llaves', 'here': 'aquí', 'llaves': 'keys', 'aquí': 'here'}},
            {"en": 'I put the book on the table.', "es": 'Yo pongo el libro sobre la mesa.', "noun_id": None, "type": 'written', "glosses": {'book': 'libro', 'table': 'mesa', 'the': 'la', 'libro': 'book', 'mesa': 'table', 'la': 'the'}},
            {"en": 'We (f) put the chairs outside.', "es": 'Nosotras ponemos las sillas afuera.', "noun_id": None, "type": 'auditory', "glosses": {'chairs': 'sillas', 'outside': 'afuera', 'the': 'las', 'sillas': 'chairs', 'afuera': 'outside', 'las': 'the'}},
            {"en": 'You put the keys here.', "es": 'Tú pones las llaves aquí.', "noun_id": None, "type": 'auditory', "glosses": {'keys': 'llaves', 'here': 'aquí', 'the': 'las', 'llaves': 'keys', 'aquí': 'here', 'las': 'the'}},
            {"en": 'They (f) do the cleaning.', "es": 'Ellas hacen la limpieza.', "noun_id": None, "type": 'written', "glosses": {'cleaning': 'limpieza', 'limpieza': 'cleaning'}},
            {"en": 'They (f) put the flowers in the vase.', "es": 'Ellas ponen las flores en el jarrón.', "noun_id": None, "type": 'written', "glosses": {'flowers': 'flores', 'vase': 'jarrón', 'flores': 'flowers', 'jarrón': 'vase'}},
            {"en": 'You put the book on the table.', "es": 'Tú pones el libro sobre la mesa.', "noun_id": None, "type": 'written', "glosses": {'book': 'libro', 'table': 'mesa', 'libro': 'book', 'mesa': 'table'}},
            {"en": 'I do my homework.', "es": 'Yo hago mi tarea.', "noun_id": None, "type": 'written', "glosses": {'homework': 'tarea', 'mi': 'mi', 'tarea': 'homework'}},
            {"en": 'We (m) put the plates on the table.', "es": 'Nosotros ponemos los platos en la mesa.', "noun_id": None, "type": 'auditory', "glosses": {'plates': 'platos', 'table': 'mesa', 'platos': 'plates', 'mesa': 'table'}},
            {"en": 'You all put the food on the table.', "es": 'Ustedes ponen la comida en la mesa.', "noun_id": None, "type": 'written', "glosses": {'food': 'comida', 'table': 'mesa', 'the': 'la', 'comida': 'food', 'mesa': 'table', 'la': 'the'}},
            {"en": 'We (f) do exercises every day.', "es": 'Nosotras hacemos ejercicios todos los días.', "noun_id": None, "type": 'auditory', "glosses": {'exercises': 'ejercicios', 'day': 'días', 'every': 'todos', 'the': 'los', 'ejercicios': 'exercises', 'días': 'day', 'todos': 'every', 'los': 'the'}},
            {"en": 'You do the dishes.', "es": 'Tú haces los platos.', "noun_id": None, "type": 'auditory', "glosses": {'dishes': 'platos', 'the': 'los', 'platos': 'dishes', 'los': 'the'}},
            {"en": 'She puts flowers in the vase.', "es": 'Ella pone flores en el florero.', "noun_id": None, "type": 'written', "glosses": {'flowers': 'flores', 'vase': 'florero', 'the': 'el', 'flores': 'flowers', 'florero': 'vase', 'el': 'the'}},
            {"en": 'He does the work.', "es": 'Él hace el trabajo.', "noun_id": None, "type": 'written', "glosses": {'work': 'trabajo', 'trabajo': 'work'}},
            {"en": 'I do the breakfast.', "es": 'Yo hago el desayuno.', "noun_id": None, "type": 'auditory', "glosses": {'breakfast': 'desayuno', 'desayuno': 'breakfast'}},
            {"en": 'You all do the cleaning.', "es": 'Ustedes hacen la limpieza.', "noun_id": None, "type": 'written', "glosses": {'cleaning': 'limpieza', 'the': 'la', 'limpieza': 'cleaning', 'la': 'the'}},
            {"en": 'You do the homework.', "es": 'Tú haces la tarea.', "noun_id": None, "type": 'written', "glosses": {'homework': 'tarea', 'tarea': 'homework'}},
            {"en": 'She does a good job.', "es": 'Ella hace un buen trabajo.', "noun_id": None, "type": 'written', "glosses": {'job': 'trabajo', 'good': 'buen', 'trabajo': 'job', 'buen': 'good'}},
            {"en": 'He puts the jacket in the closet.', "es": 'Él pone la chaqueta en el armario.', "noun_id": None, "type": 'written', "glosses": {'jacket': 'chaqueta', 'closet': 'armario', 'chaqueta': 'jacket', 'armario': 'closet'}},
            {"en": 'We (m) do the exercises.', "es": 'Nosotros hacemos los ejercicios.', "noun_id": None, "type": 'auditory', "glosses": {'exercises': 'ejercicios', 'ejercicios': 'exercises'}},
        ],
        "drill_targets": [{"verb": "hacer", "pronoun": "yo"}, {"verb": "hacer", "pronoun": "tú"}, {"verb": "hacer", "pronoun": "ella"}, {"verb": "hacer", "pronoun": "nosotras"}, {"verb": "hacer", "pronoun": "ustedes"}, {"verb": "poner", "pronoun": "yo"}, {"verb": "poner", "pronoun": "tú"}, {"verb": "poner", "pronoun": "ella"}, {"verb": "poner", "pronoun": "nosotras"}, {"verb": "poner", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Irregular Present II hacer + poner (1/2): hacer, poner",
            "targets": [{"verb": "hacer", "pronoun": "yo"}, {"verb": "hacer", "pronoun": "tú"}, {"verb": "hacer", "pronoun": "ella"}, {"verb": "hacer", "pronoun": "nosotras"}, {"verb": "hacer", "pronoun": "ustedes"}, {"verb": "poner", "pronoun": "yo"}, {"verb": "poner", "pronoun": "tú"}, {"verb": "poner", "pronoun": "ella"}, {"verb": "poner", "pronoun": "nosotras"}, {"verb": "poner", "pronoun": "ustedes"}],
        },
        "opener_en": "What do you do for work?",
        "opener_es": "¿Qué haces de trabajo?",
    },


    "grammar_irregular_present_ii_salir_decir_1": {
        "title": "Irregular Present II — salir + decir (1/2)",
        "grammar_level": 4.5,
        "lesson_number": 3,
        "lesson_type": "conjugation",
        "word_workload": ["salir", "decir"],
        "video_embed_id": "Bg9XcrNn3LL",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": IRREGULAR_PRESENT_II_SALIR_DECIR_INTRO,
        "drill_config": {
            "answers": {
                "salir": {"yo": "sal|go", "tú": "sal|es", "él": "sal|e", "ella": "sal|e", "usted": "sal|e", "nosotros": "sal|imos", "nosotras": "sal|imos", "ellos": "sal|en", "ellas": "sal|en", "ustedes": "sal|en"},
                "decir": {"yo": "di|go", "tú": "d|ices", "él": "d|ice", "ella": "d|ice", "usted": "d|ice", "nosotros": "dec|imos", "nosotras": "dec|imos", "ellos": "d|icen", "ellas": "d|icen", "ustedes": "d|icen"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": 'You all leave after lunch.', "es": 'Ustedes salen después del almuerzo.', "noun_id": None, "type": 'written', "glosses": {'lunch': 'almuerzo', 'almuerzo': 'lunch'}},
            {"en": 'I say good morning to her.', "es": 'Yo digo buenos días a ella.', "noun_id": None, "type": 'auditory', "glosses": {'morning': 'días', 'good': 'buenos', 'días': 'morning', 'buenos': 'good'}},
            {"en": 'I say the truth always.', "es": 'Yo digo la verdad siempre.', "noun_id": None, "type": 'written', "glosses": {'truth': 'verdad', 'always': 'siempre', 'verdad': 'truth', 'siempre': 'always'}},
            {"en": 'We (f) leave every morning.', "es": 'Nosotras salimos cada mañana.', "noun_id": None, "type": 'auditory', "glosses": {'morning': 'mañana', 'mañana': 'morning'}},
            {"en": 'He leaves the office at five.', "es": 'Él sale de la oficina a las cinco.', "noun_id": None, "type": 'written', "glosses": {'office': 'oficina', 'cinco': 'five', 'five': 'cinco', 'oficina': 'office'}},
            {"en": 'We say hello to our friends.', "es": 'Nosotros decimos hola a nuestros amigos.', "noun_id": None, "type": 'auditory', "glosses": {'hello': 'hola', 'friends': 'amigos', 'hola': 'hello', 'amigos': 'friends'}},
            {"en": 'He says funny things sometimes.', "es": 'Él dice cosas divertidas a veces.', "noun_id": None, "type": 'written', "glosses": {'things': 'cosas', 'funny': 'divertidas', 'cosas': 'things', 'divertidas': 'funny'}},
            {"en": 'They (f) say many words fast.', "es": 'Ellas dicen muchas palabras rápido.', "noun_id": None, "type": 'written', "glosses": {'words': 'palabras', 'many': 'muchas', 'fast': 'rápido', 'palabras': 'words', 'muchas': 'many', 'rápido': 'fast'}},
            {"en": "She leaves at five o'clock.", "es": 'Ella sale a las cinco.', "noun_id": None, "type": 'written', "glosses": {}},
            {"en": 'You all say good things.', "es": 'Ustedes dicen cosas buenas.', "noun_id": None, "type": 'written', "glosses": {'things': 'cosas', 'good': 'buenas', 'cosas': 'things', 'buenas': 'good'}},
            {"en": 'You leave the house now.', "es": 'Tú sales de la casa ahora.', "noun_id": None, "type": 'written', "glosses": {'house': 'casa', 'casa': 'house'}},
            {"en": 'She says something important.', "es": 'Ella dice algo importante.', "noun_id": None, "type": 'written', "glosses": {'something': 'algo', 'important': 'importante', 'algo': 'something', 'importante': 'important'}},
            {"en": 'I leave early every day.', "es": 'Yo salgo temprano todos los días.', "noun_id": None, "type": 'auditory', "glosses": {'early': 'temprano', 'temprano': 'early'}},
            {"en": 'You say the truth always.', "es": 'Tú dices la verdad siempre.', "noun_id": None, "type": 'written', "glosses": {'truth': 'verdad', 'verdad': 'truth'}},
            {"en": 'We leave the park together.', "es": 'Nosotros salimos del parque juntos.', "noun_id": None, "type": 'auditory', "glosses": {'park': 'parque', 'parque': 'park'}},
            {"en": 'They (f) leave the school now.', "es": 'Ellas salen de la escuela ahora.', "noun_id": None, "type": 'written', "glosses": {'school': 'escuela', 'escuela': 'school'}},
            {"en": 'You say many words.', "es": 'Tú dices muchas palabras.', "noun_id": None, "type": 'auditory', "glosses": {'words': 'palabras', 'many': 'muchas', 'palabras': 'words', 'muchas': 'many'}},
            {"en": 'You leave with your friend.', "es": 'Tú sales con tu amigo.', "noun_id": None, "type": 'auditory', "glosses": {'friend': 'amigo', 'amigo': 'friend'}},
            {"en": 'I leave the house early.', "es": 'Yo salgo de la casa temprano.', "noun_id": None, "type": 'written', "glosses": {'house': 'casa', 'early': 'temprano', 'casa': 'house', 'temprano': 'early'}},
            {"en": 'We (f) say the answer clearly.', "es": 'Nosotras decimos la respuesta claramente.', "noun_id": None, "type": 'auditory', "glosses": {'answer': 'respuesta', 'clearly': 'claramente', 'respuesta': 'answer', 'claramente': 'clearly'}},
        ],
        "drill_targets": [{"verb": "salir", "pronoun": "yo"}, {"verb": "salir", "pronoun": "tú"}, {"verb": "salir", "pronoun": "ella"}, {"verb": "salir", "pronoun": "nosotras"}, {"verb": "salir", "pronoun": "ustedes"}, {"verb": "decir", "pronoun": "yo"}, {"verb": "decir", "pronoun": "tú"}, {"verb": "decir", "pronoun": "ella"}, {"verb": "decir", "pronoun": "nosotras"}, {"verb": "decir", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Irregular Present II salir + decir (1/2): salir, decir",
            "targets": [{"verb": "salir", "pronoun": "yo"}, {"verb": "salir", "pronoun": "tú"}, {"verb": "salir", "pronoun": "ella"}, {"verb": "salir", "pronoun": "nosotras"}, {"verb": "salir", "pronoun": "ustedes"}, {"verb": "decir", "pronoun": "yo"}, {"verb": "decir", "pronoun": "tú"}, {"verb": "decir", "pronoun": "ella"}, {"verb": "decir", "pronoun": "nosotras"}, {"verb": "decir", "pronoun": "ustedes"}],
        },
        "opener_en": "What time do you leave?",
        "opener_es": "¿A qué hora sales?",
    },


    "grammar_irregular_present_ii_oir_caer_1": {
        "title": "Irregular Present II — oír + caer (1/2)",
        "grammar_level": 4.5,
        "lesson_number": 5,
        "lesson_type": "conjugation",
        "word_workload": ["oír", "caer"],
        "video_embed_id": "Bg9XcrNn3LL",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": IRREGULAR_PRESENT_II_OIR_CAER_INTRO,
        "drill_config": {
            "answers": {
                "oír": {"yo": "o|igo", "tú": "o|yes", "él": "o|ye", "ella": "o|ye", "usted": "o|ye", "nosotros": "o|ímos", "nosotras": "o|ímos", "ellos": "o|yen", "ellas": "o|yen", "ustedes": "o|yen"},
                "caer": {"yo": "ca|igo", "tú": "ca|es", "él": "ca|e", "ella": "ca|e", "usted": "ca|e", "nosotros": "ca|emos", "nosotras": "ca|emos", "ellos": "ca|en", "ellas": "ca|en", "ustedes": "ca|en"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": 'They (f) hear the voices.', "es": 'Ellas oyen las voces.', "noun_id": None, "type": 'written', "glosses": {'voices': 'voces', 'voces': 'voices'}},
            {"en": 'You fall very fast.', "es": 'Tú caes muy rápido.', "noun_id": None, "type": 'auditory', "glosses": {'fast': 'rápido', 'rápido': 'fast'}},
            {"en": 'You all fall on the street.', "es": 'Ustedes caen en la calle.', "noun_id": None, "type": 'written', "glosses": {'street': 'calle', 'calle': 'street'}},
            {"en": 'She falls in the park.', "es": 'Ella cae en el parque.', "noun_id": None, "type": 'written', "glosses": {'park': 'parque', 'parque': 'park'}},
            {"en": 'We (f) fall during the game.', "es": 'Nosotras caemos durante el juego.', "noun_id": None, "type": 'auditory', "glosses": {'game': 'juego', 'juego': 'game'}},
            {"en": 'We hear the ocean waves.', "es": 'Nosotros oímos las olas del océano.', "noun_id": None, "type": 'auditory', "glosses": {'ocean': 'océano', 'waves': 'olas', 'olas': 'waves', 'océano': 'ocean'}},
            {"en": 'I fall from the ladder.', "es": 'Yo caigo de la escalera.', "noun_id": None, "type": 'auditory', "glosses": {'ladder': 'escalera', 'escalera': 'ladder'}},
            {"en": 'You all hear the teacher.', "es": 'Ustedes oyen al profesor.', "noun_id": None, "type": 'written', "glosses": {'teacher': 'profesor', 'profesor': 'teacher'}},
            {"en": 'Do you fall often?', "es": '¿Tú caes a menudo?', "noun_id": None, "type": 'written', "glosses": {'often': 'a menudo', 'a menudo': 'often'}},
            {"en": 'Do you hear the birds?', "es": '¿Tú oyes los pájaros?', "noun_id": None, "type": 'auditory', "glosses": {'birds': 'pájaros', 'pájaros': 'birds'}},
            {"en": 'He falls in the park.', "es": 'Él cae en el parque.', "noun_id": None, "type": 'written', "glosses": {'park': 'parque', 'parque': 'park'}},
            {"en": 'I hear the birds outside.', "es": 'Yo oigo los pájaros afuera.', "noun_id": None, "type": 'auditory', "glosses": {'birds': 'pájaros', 'afuera': 'outside', 'pájaros': 'birds', 'outside': 'afuera'}},
            {"en": 'I hear the music.', "es": 'Yo oigo la música.', "noun_id": None, "type": 'written', "glosses": {'music': 'música', 'música': 'music'}},
            {"en": 'She hears a noise.', "es": 'Ella oye un ruido.', "noun_id": None, "type": 'written', "glosses": {'noise': 'ruido', 'ruido': 'noise'}},
            {"en": 'He hears a strange noise.', "es": 'Él oye un ruido extraño.', "noun_id": None, "type": 'written', "glosses": {'noise': 'ruido', 'strange': 'extraño', 'ruido': 'noise', 'extraño': 'strange'}},
            {"en": 'They (f) fall on the ice.', "es": 'Ellas caen sobre el hielo.', "noun_id": None, "type": 'written', "glosses": {'ice': 'hielo', 'hielo': 'ice'}},
            {"en": 'We fall during the game.', "es": 'Nosotros caemos durante el juego.', "noun_id": None, "type": 'auditory', "glosses": {'game': 'juego', 'juego': 'game'}},
            {"en": 'Do you hear the music?', "es": '¿Tú oyes la música?', "noun_id": None, "type": 'written', "glosses": {'music': 'música', 'música': 'music'}},
            {"en": 'I fall from the ladder.', "es": 'Yo caigo de la escalera.', "noun_id": None, "type": 'written', "glosses": {'ladder': 'escalera', 'escalera': 'ladder'}},
            {"en": 'We (f) hear the ocean.', "es": 'Nosotras oímos el océano.', "noun_id": None, "type": 'auditory', "glosses": {'ocean': 'océano', 'océano': 'ocean'}},
        ],
        "drill_targets": [{"verb": "oír", "pronoun": "yo"}, {"verb": "oír", "pronoun": "tú"}, {"verb": "oír", "pronoun": "ella"}, {"verb": "oír", "pronoun": "nosotras"}, {"verb": "oír", "pronoun": "ustedes"}, {"verb": "caer", "pronoun": "yo"}, {"verb": "caer", "pronoun": "tú"}, {"verb": "caer", "pronoun": "ella"}, {"verb": "caer", "pronoun": "nosotras"}, {"verb": "caer", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Irregular Present II oír + caer (1/2): oír, caer",
            "targets": [{"verb": "oír", "pronoun": "yo"}, {"verb": "oír", "pronoun": "tú"}, {"verb": "oír", "pronoun": "ella"}, {"verb": "oír", "pronoun": "nosotras"}, {"verb": "oír", "pronoun": "ustedes"}, {"verb": "caer", "pronoun": "yo"}, {"verb": "caer", "pronoun": "tú"}, {"verb": "caer", "pronoun": "ella"}, {"verb": "caer", "pronoun": "nosotras"}, {"verb": "caer", "pronoun": "ustedes"}],
        },
        "opener_en": "Do you hear the music?",
        "opener_es": "¿Oyes la música?",
    },


    "grammar_irregular_present_ii_traer_valer_1": {
        "title": "Irregular Present II — traer + valer (1/2)",
        "grammar_level": 4.5,
        "lesson_number": 7,
        "lesson_type": "conjugation",
        "word_workload": ["traer", "valer"],
        "video_embed_id": "Bg9XcrNn3LL",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": IRREGULAR_PRESENT_II_TRAER_VALER_INTRO,
        "drill_config": {
            "answers": {
                "traer": {"yo": "tra|igo", "tú": "tra|es", "él": "tra|e", "ella": "tra|e", "usted": "tra|e", "nosotros": "tra|emos", "nosotras": "tra|emos", "ellos": "tra|en", "ellas": "tra|en", "ustedes": "tra|en"},
                "valer": {"yo": "val|go", "tú": "val|es", "él": "val|e", "ella": "val|e", "usted": "val|e", "nosotros": "val|emos", "nosotras": "val|emos", "ellos": "val|en", "ellas": "val|en", "ustedes": "val|en"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": 'He is worth five dollars.', "es": 'Él vale cinco dólares.', "noun_id": None, "type": 'written', "glosses": {'dollars': 'dólares', 'five': 'cinco', 'dólares': 'dollars', 'cinco': 'five'}},
            {"en": 'He brings the keys.', "es": 'Él trae las llaves.', "noun_id": None, "type": 'written', "glosses": {'keys': 'llaves', 'llaves': 'keys'}},
            {"en": 'I bring fresh bread.', "es": 'Yo traigo pan fresco.', "noun_id": None, "type": 'written', "glosses": {'bread': 'pan', 'fresh': 'fresco', 'pan': 'bread', 'fresco': 'fresh'}},
            {"en": 'I am worth a lot.', "es": 'Yo valgo mucho.', "noun_id": None, "type": 'written', "glosses": {'much': 'mucho', 'mucho': 'much'}},
            {"en": 'I bring fresh fruit.', "es": 'Yo traigo fruta fresca.', "noun_id": None, "type": 'auditory', "glosses": {'fruit': 'fruta', 'fresh': 'fresca', 'fruta': 'fruit', 'fresca': 'fresh'}},
            {"en": 'You all are worth many coins.', "es": 'Ustedes valen muchas monedas.', "noun_id": None, "type": 'written', "glosses": {'coins': 'monedas', 'many': 'muchas', 'monedas': 'coins', 'muchas': 'many'}},
            {"en": 'She is worth a fortune.', "es": 'Ella vale una fortuna.', "noun_id": None, "type": 'written', "glosses": {'fortune': 'fortuna', 'fortuna': 'fortune'}},
            {"en": 'You are worth a lot.', "es": 'Tú vales mucho.', "noun_id": None, "type": 'written', "glosses": {'much': 'mucho', 'mucho': 'much'}},
            {"en": 'We (f) are worth much money.', "es": 'Nosotras valemos mucho dinero.', "noun_id": None, "type": 'auditory', "glosses": {'money': 'dinero', 'much': 'mucho', 'dinero': 'money', 'mucho': 'much'}},
            {"en": 'You are worth little.', "es": 'Tú vales poco.', "noun_id": None, "type": 'auditory', "glosses": {'little': 'poco', 'poco': 'little'}},
            {"en": 'We (m) are worth a lot.', "es": 'Nosotros valemos mucho.', "noun_id": None, "type": 'auditory', "glosses": {'much': 'mucho', 'mucho': 'much'}},
            {"en": 'They (f) bring cold water.', "es": 'Ellas traen agua fría.', "noun_id": None, "type": 'written', "glosses": {'water': 'agua', 'cold': 'fría', 'agua': 'water', 'fría': 'cold'}},
            {"en": 'We (m) bring good news.', "es": 'Nosotros traemos buenas noticias.', "noun_id": None, "type": 'auditory', "glosses": {'news': 'noticias', 'good': 'buenas', 'noticias': 'news', 'buenas': 'good'}},
            {"en": 'They (f) are worth nothing.', "es": 'Ellas valen nada.', "noun_id": None, "type": 'written', "glosses": {'nothing': 'nada', 'nada': 'nothing'}},
            {"en": 'I am worth little money.', "es": 'Yo valgo poco dinero.', "noun_id": None, "type": 'auditory', "glosses": {'money': 'dinero', 'little': 'poco', 'dinero': 'money', 'poco': 'little'}},
            {"en": 'We (f) bring big bags.', "es": 'Nosotras traemos bolsas grandes.', "noun_id": None, "type": 'auditory', "glosses": {'bags': 'bolsas', 'big': 'grandes', 'bolsas': 'bags', 'grandes': 'big'}},
            {"en": 'You bring the books.', "es": 'Tú traes los libros.', "noun_id": None, "type": 'written', "glosses": {'books': 'libros', 'libros': 'books'}},
            {"en": 'You bring cold water.', "es": 'Tú traes agua fría.', "noun_id": None, "type": 'auditory', "glosses": {'water': 'agua', 'cold': 'fría', 'agua': 'water', 'fría': 'cold'}},
            {"en": 'She brings new books.', "es": 'Ella trae libros nuevos.', "noun_id": None, "type": 'written', "glosses": {'books': 'libros', 'new': 'nuevos', 'libros': 'books', 'nuevos': 'new'}},
            {"en": 'You all bring warm jackets.', "es": 'Ustedes traen chaquetas calientes.', "noun_id": None, "type": 'written', "glosses": {'jackets': 'chaquetas', 'warm': 'calientes', 'chaquetas': 'jackets', 'calientes': 'warm'}},
        ],
        "drill_targets": [{"verb": "traer", "pronoun": "yo"}, {"verb": "traer", "pronoun": "tú"}, {"verb": "traer", "pronoun": "ella"}, {"verb": "traer", "pronoun": "nosotras"}, {"verb": "traer", "pronoun": "ustedes"}, {"verb": "valer", "pronoun": "yo"}, {"verb": "valer", "pronoun": "tú"}, {"verb": "valer", "pronoun": "ella"}, {"verb": "valer", "pronoun": "nosotras"}, {"verb": "valer", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Irregular Present II traer + valer (1/2): traer, valer",
            "targets": [{"verb": "traer", "pronoun": "yo"}, {"verb": "traer", "pronoun": "tú"}, {"verb": "traer", "pronoun": "ella"}, {"verb": "traer", "pronoun": "nosotras"}, {"verb": "traer", "pronoun": "ustedes"}, {"verb": "valer", "pronoun": "yo"}, {"verb": "valer", "pronoun": "tú"}, {"verb": "valer", "pronoun": "ella"}, {"verb": "valer", "pronoun": "nosotras"}, {"verb": "valer", "pronoun": "ustedes"}],
        },
        "opener_en": "What are you bringing?",
        "opener_es": "¿Qué traes?",
    },


    "grammar_irregular_present_ii_hacer_poner_chat": {
        "title": "Irregular Present II — hacer + poner Chat",
        "grammar_level": 4.5,
        "lesson_number": 2.5,
        "lesson_type": "conjugation",
        "word_workload": ["hacer", "poner"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Irregular Present II hacer + poner chat: hacer, poner", "targets": [{"verb": "hacer", "pronoun": "yo"}, {"verb": "hacer", "pronoun": "tú"}, {"verb": "hacer", "pronoun": "ella"}, {"verb": "hacer", "pronoun": "nosotras"}, {"verb": "hacer", "pronoun": "ustedes"}, {"verb": "poner", "pronoun": "tú"}, {"verb": "poner", "pronoun": "yo"}, {"verb": "poner", "pronoun": "él"}, {"verb": "poner", "pronoun": "nosotros"}, {"verb": "poner", "pronoun": "ellas"}]},
    },

    "grammar_irregular_present_ii_salir_decir_chat": {
        "title": "Irregular Present II — salir + decir Chat",
        "grammar_level": 4.5,
        "lesson_number": 4.5,
        "lesson_type": "conjugation",
        "word_workload": ["salir", "decir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Irregular Present II salir + decir chat: salir, decir", "targets": [{"verb": "salir", "pronoun": "yo"}, {"verb": "salir", "pronoun": "tú"}, {"verb": "salir", "pronoun": "ella"}, {"verb": "salir", "pronoun": "nosotras"}, {"verb": "salir", "pronoun": "ustedes"}, {"verb": "decir", "pronoun": "tú"}, {"verb": "decir", "pronoun": "yo"}, {"verb": "decir", "pronoun": "él"}, {"verb": "decir", "pronoun": "nosotros"}, {"verb": "decir", "pronoun": "ellas"}]},
    },

    "grammar_irregular_present_ii_oir_caer_chat": {
        "title": "Irregular Present II — oír + caer Chat",
        "grammar_level": 4.5,
        "lesson_number": 6.5,
        "lesson_type": "conjugation",
        "word_workload": ["oír", "caer"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Irregular Present II oír + caer chat: oír, caer", "targets": [{"verb": "oír", "pronoun": "yo"}, {"verb": "oír", "pronoun": "tú"}, {"verb": "oír", "pronoun": "ella"}, {"verb": "oír", "pronoun": "nosotras"}, {"verb": "oír", "pronoun": "ustedes"}, {"verb": "caer", "pronoun": "tú"}, {"verb": "caer", "pronoun": "yo"}, {"verb": "caer", "pronoun": "él"}, {"verb": "caer", "pronoun": "nosotros"}, {"verb": "caer", "pronoun": "ellas"}]},
    },

    "grammar_irregular_present_ii_traer_valer_chat": {
        "title": "Irregular Present II — traer + valer Chat",
        "grammar_level": 4.5,
        "lesson_number": 8.5,
        "lesson_type": "conjugation",
        "word_workload": ["traer", "valer"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Irregular Present II traer + valer chat: traer, valer", "targets": [{"verb": "traer", "pronoun": "yo"}, {"verb": "traer", "pronoun": "tú"}, {"verb": "traer", "pronoun": "ella"}, {"verb": "traer", "pronoun": "nosotras"}, {"verb": "traer", "pronoun": "ustedes"}, {"verb": "valer", "pronoun": "tú"}, {"verb": "valer", "pronoun": "yo"}, {"verb": "valer", "pronoun": "él"}, {"verb": "valer", "pronoun": "nosotros"}, {"verb": "valer", "pronoun": "ellas"}]},
    },

    # ── From _gl5_output.py ──

"grammar_spelling_changes_conocer_producir_1": {
        "title": "Spelling Changes — conocer + producir (1/2)",
        "grammar_level": 5,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ["conocer", "producir"],
        "video_embed_id": "ZxefHnILbqs",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": SPELLING_CHANGES_CONOCER_PRODUCIR_INTRO,
        "drill_config": {
            "answers": {
                "conocer": {"yo": "conoz|co", "tú": "conoc|es", "él": "conoc|e", "ella": "conoc|e", "usted": "conoc|e", "nosotros": "conoc|emos", "nosotras": "conoc|emos", "ellos": "conoc|en", "ellas": "conoc|en", "ustedes": "conoc|en"},
                "producir": {"yo": "produz|co", "tú": "produc|es", "él": "produc|e", "ella": "produc|e", "usted": "produc|e", "nosotros": "produc|imos", "nosotras": "produc|imos", "ellos": "produc|en", "ellas": "produc|en", "ustedes": "produc|en"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": 'I know a good restaurant.', "es": 'Yo conozco un buen restaurante.', "noun_id": None, "type": 'auditory', "glosses": {'restaurant': 'restaurante', 'good': 'buen', 'restaurante': 'restaurant', 'buen': 'good'}},
            {"en": 'He produces new ideas.', "es": 'Él produce ideas nuevas.', "noun_id": None, "type": 'written', "glosses": {'ideas': 'ideas', 'new': 'nuevas', 'nuevas': 'new'}},
            {"en": 'You all know the students.', "es": 'Ustedes conocen a los estudiantes.', "noun_id": None, "type": 'written', "glosses": {'students': 'estudiantes', 'estudiantes': 'students'}},
            {"en": 'She produces beautiful art.', "es": 'Ella produce arte hermosa.', "noun_id": None, "type": 'written', "glosses": {'art': 'arte', 'beautiful': 'hermosa', 'arte': 'art', 'hermosa': 'beautiful'}},
            {"en": 'We (f) know the museum.', "es": 'Nosotras conocemos el museo.', "noun_id": None, "type": 'auditory', "glosses": {'museum': 'museo', 'museo': 'museum'}},
            {"en": 'They (f) produce beautiful paintings.', "es": 'Ellas producen pinturas bonitas.', "noun_id": None, "type": 'written', "glosses": {'paintings': 'pinturas', 'beautiful': 'bonitas', 'pinturas': 'paintings', 'bonitas': 'beautiful'}},
            {"en": 'I know the city well.', "es": 'Yo conozco bien la ciudad.', "noun_id": None, "type": 'written', "glosses": {'city': 'ciudad', 'well': 'bien', 'ciudad': 'city', 'bien': 'well'}},
            {"en": 'They (f) know the Spanish songs.', "es": 'Ellas conocen las canciones españolas.', "noun_id": None, "type": 'written', "glosses": {'songs': 'canciones', 'Spanish': 'españolas', 'canciones': 'songs', 'españolas': 'Spanish'}},
            {"en": 'You all produce quality wine.', "es": 'Ustedes producen vino de calidad.', "noun_id": None, "type": 'written', "glosses": {'wine': 'vino', 'quality': 'calidad', 'vino': 'wine', 'calidad': 'quality'}},
            {"en": 'You know my brother.', "es": 'Tú conoces a mi hermano.', "noun_id": None, "type": 'auditory', "glosses": {'brother': 'hermano', 'hermano': 'brother'}},
            {"en": 'I produce fresh juice.', "es": 'Yo produzco jugo fresco.', "noun_id": None, "type": 'auditory', "glosses": {'juice': 'jugo', 'fresh': 'fresco', 'jugo': 'juice', 'fresco': 'fresh'}},
            {"en": 'You produce fresh fruit.', "es": 'Tú produces fruta fresca.', "noun_id": None, "type": 'auditory', "glosses": {'fruit': 'fruta', 'fresh': 'fresca', 'fruta': 'fruit', 'fresca': 'fresh'}},
            {"en": 'You produce many books.', "es": 'Tú produces muchos libros.', "noun_id": None, "type": 'written', "glosses": {'books': 'libros', 'many': 'muchos', 'libros': 'books', 'muchos': 'many'}},
            {"en": 'I produce many books.', "es": 'Yo produzco muchos libros.', "noun_id": None, "type": 'written', "glosses": {'books': 'libros', 'many': 'muchos', 'libros': 'books', 'muchos': 'many'}},
            {"en": 'We know the old museum.', "es": 'Nosotros conocemos el museo antiguo.', "noun_id": None, "type": 'auditory', "glosses": {'museum': 'museo', 'old': 'antiguo', 'museo': 'museum', 'antiguo': 'old'}},
            {"en": 'You know the city well.', "es": 'Tú conoces bien la ciudad.', "noun_id": None, "type": 'written', "glosses": {'city': 'ciudad', 'well': 'bien', 'ciudad': 'city', 'bien': 'well'}},
            {"en": 'She knows the teacher.', "es": 'Ella conoce a la profesora.', "noun_id": None, "type": 'written', "glosses": {'teacher': 'profesora', 'profesora': 'teacher'}},
            {"en": 'We produce organic vegetables.', "es": 'Nosotros producimos verduras orgánicas.', "noun_id": None, "type": 'auditory', "glosses": {'vegetables': 'verduras', 'organic': 'orgánicas', 'verduras': 'vegetables', 'orgánicas': 'organic'}},
            {"en": 'We (f) produce organic vegetables.', "es": 'Nosotras producimos verduras orgánicas.', "noun_id": None, "type": 'auditory', "glosses": {'vegetables': 'verduras', 'organic': 'orgánicas', 'verduras': 'vegetables', 'orgánicas': 'organic'}},
            {"en": 'He knows the new teacher.', "es": 'Él conoce a la profesora nueva.', "noun_id": None, "type": 'written', "glosses": {'teacher': 'profesora', 'new': 'nueva', 'profesora': 'teacher', 'nueva': 'new'}},
        ],
        "drill_targets": [{"verb": "conocer", "pronoun": "yo"}, {"verb": "conocer", "pronoun": "tú"}, {"verb": "conocer", "pronoun": "ella"}, {"verb": "conocer", "pronoun": "nosotras"}, {"verb": "conocer", "pronoun": "ustedes"}, {"verb": "producir", "pronoun": "yo"}, {"verb": "producir", "pronoun": "tú"}, {"verb": "producir", "pronoun": "ella"}, {"verb": "producir", "pronoun": "nosotras"}, {"verb": "producir", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Spelling Changes conocer + producir (1/2): conocer, producir",
            "targets": [{"verb": "conocer", "pronoun": "yo"}, {"verb": "conocer", "pronoun": "tú"}, {"verb": "conocer", "pronoun": "ella"}, {"verb": "conocer", "pronoun": "nosotras"}, {"verb": "conocer", "pronoun": "ustedes"}, {"verb": "producir", "pronoun": "yo"}, {"verb": "producir", "pronoun": "tú"}, {"verb": "producir", "pronoun": "ella"}, {"verb": "producir", "pronoun": "nosotras"}, {"verb": "producir", "pronoun": "ustedes"}],
        },
        "opener_en": "Do you know my brother?",
        "opener_es": "¿Conoces a mi hermano?",
    },


    "grammar_spelling_changes_construir": {
        "title": "Spelling Changes — construir ",
        "grammar_level": 5,
        "lesson_number": 3,
        "lesson_type": "conjugation",
        "word_workload": ["construir"],
        "video_embed_id": "ZxefHnILbqs",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": SPELLING_CHANGES_CONSTRUIR_CONSEGUIR_INTRO,
        "drill_config": {
            "answers": {
                "construir": {'yo': 'constr|uyo', 'tú': 'constr|uyes', 'él': 'constr|uye', 'ella': 'constr|uye', 'usted': 'constr|uye', 'nosotros': 'constr|uimos', 'nosotras': 'constr|uimos', 'ellos': 'constr|uyen', 'ellas': 'constr|uyen', 'ustedes': 'constr|uyen'},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": 'I build a new house.', "es": 'Yo construyo una casa nueva.', "noun_id": None, "type": 'written', "glosses": {'house': 'casa', 'new': 'nueva', 'casa': 'house', 'nueva': 'new'}},
            {"en": 'You build tall buildings.', "es": 'Tú construyes edificios altos.', "noun_id": None, "type": 'auditory', "glosses": {'buildings': 'edificios', 'tall': 'altos', 'edificios': 'buildings', 'altos': 'tall'}},
            {"en": 'She builds a big school.', "es": 'Ella construye una escuela grande.', "noun_id": None, "type": 'written', "glosses": {'school': 'escuela', 'big': 'grande', 'escuela': 'school', 'grande': 'big'}},
            {"en": 'We (f) build strong bridges.', "es": 'Nosotras construimos puentes fuertes.', "noun_id": None, "type": 'auditory', "glosses": {'bridges': 'puentes', 'strong': 'fuertes', 'puentes': 'bridges', 'fuertes': 'strong'}},
            {"en": 'You all build new roads.', "es": 'Ustedes construyen carreteras nuevas.', "noun_id": None, "type": 'written', "glosses": {'roads': 'carreteras', 'new': 'nuevas', 'carreteras': 'roads', 'nuevas': 'new'}},
            {"en": 'You build a new house.', "es": 'Tú construyes una casa nueva.', "noun_id": None, "type": 'written', "glosses": {'house': 'casa', 'new': 'nueva', 'casa': 'house', 'nueva': 'new'}},
            {"en": 'I build a small bridge.', "es": 'Yo construyo un puente pequeño.', "noun_id": None, "type": 'auditory', "glosses": {'bridge': 'puente', 'small': 'pequeño', 'puente': 'bridge', 'pequeño': 'small'}},
            {"en": 'He builds a tall tower.', "es": 'Él construye una torre alta.', "noun_id": None, "type": 'written', "glosses": {'tower': 'torre', 'tall': 'alta', 'torre': 'tower', 'alta': 'tall'}},
            {"en": 'We build a big school.', "es": 'Nosotros construimos una escuela grande.', "noun_id": None, "type": 'auditory', "glosses": {'school': 'escuela', 'big': 'grande', 'escuela': 'school', 'grande': 'big'}},
            {"en": 'They (f) build strong walls.', "es": 'Ellas construyen muros fuertes.', "noun_id": None, "type": 'written', "glosses": {'walls': 'muros', 'strong': 'fuertes', 'muros': 'walls', 'fuertes': 'strong'}},
        ],
        "drill_targets": [{'verb': 'construir', 'pronoun': 'yo'}, {'verb': 'construir', 'pronoun': 'tú'}, {'verb': 'construir', 'pronoun': 'ella'}, {'verb': 'construir', 'pronoun': 'nosotras'}, {'verb': 'construir', 'pronoun': 'ustedes'}],
        "phase_2_config": {
            "description": "Spelling Changes construir: construir",
            "targets": [{'verb': 'construir', 'pronoun': 'yo'}, {'verb': 'construir', 'pronoun': 'tú'}, {'verb': 'construir', 'pronoun': 'ella'}, {'verb': 'construir', 'pronoun': 'nosotras'}, {'verb': 'construir', 'pronoun': 'ustedes'}],
        },
        "opener_en": "What are you building?",
        "opener_es": "¿Qué construyes?",
    },
    "grammar_spelling_changes_conseguir": {
        "title": "Spelling Changes — conseguir ",
        "grammar_level": 5,
        "lesson_number": 4,
        "lesson_type": "conjugation",
        "word_workload": ["conseguir"],
        "video_embed_id": "ZxefHnILbqs",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": SPELLING_CHANGES_CONSTRUIR_CONSEGUIR_INTRO,
        "drill_config": {
            "answers": {
                "conseguir": {'yo': 'consig|o', 'tú': 'consig|ues', 'él': 'consig|ue', 'ella': 'consig|ue', 'usted': 'consig|ue', 'nosotros': 'conseg|uimos', 'nosotras': 'conseg|uimos', 'ellos': 'consig|uen', 'ellas': 'consig|uen', 'ustedes': 'consig|uen'},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": 'I get good results.', "es": 'Yo consigo buenos resultados.', "noun_id": None, "type": 'written', "glosses": {'results': 'resultados', 'good': 'buenos', 'resultados': 'results', 'buenos': 'good'}},
            {"en": 'You get fresh water.', "es": 'Tú consigues agua fresca.', "noun_id": None, "type": 'auditory', "glosses": {'water': 'agua', 'fresh': 'fresca', 'agua': 'water', 'fresca': 'fresh'}},
            {"en": 'She gets important information.', "es": 'Ella consigue información importante.', "noun_id": None, "type": 'written', "glosses": {'information': 'información', 'important': 'importante', 'información': 'information', 'importante': 'important'}},
            {"en": 'We (f) get clean food.', "es": 'Nosotras conseguimos comida limpia.', "noun_id": None, "type": 'auditory', "glosses": {'food': 'comida', 'clean': 'limpia', 'comida': 'food', 'limpia': 'clean'}},
            {"en": 'You all get fast cars.', "es": 'Ustedes consiguen coches rápidos.', "noun_id": None, "type": 'written', "glosses": {'cars': 'coches', 'fast': 'rápidos', 'coches': 'cars', 'rápidos': 'fast'}},
            {"en": 'You get fresh fruits.', "es": 'Tú consigues frutas frescas.', "noun_id": None, "type": 'written', "glosses": {'fruits': 'frutas', 'fresh': 'frescas', 'frutas': 'fruits', 'frescas': 'fresh'}},
            {"en": 'I get good grades.', "es": 'Yo consigo buenas notas.', "noun_id": None, "type": 'auditory', "glosses": {'grades': 'notas', 'good': 'buenas', 'notas': 'grades', 'buenas': 'good'}},
            {"en": 'He gets a new job.', "es": 'Él consigue un trabajo nuevo.', "noun_id": None, "type": 'written', "glosses": {'job': 'trabajo', 'new': 'nuevo', 'trabajo': 'job', 'nuevo': 'new'}},
            {"en": 'We (m) get tickets early.', "es": 'Nosotros conseguimos entradas temprano.', "noun_id": None, "type": 'auditory', "glosses": {'tickets': 'entradas', 'early': 'temprano', 'entradas': 'tickets', 'temprano': 'early'}},
            {"en": 'They (f) get cold water.', "es": 'Ellas consiguen agua fría.', "noun_id": None, "type": 'written', "glosses": {'water': 'agua', 'cold': 'fría', 'agua': 'water', 'fría': 'cold'}},
        ],
        "drill_targets": [{'verb': 'conseguir', 'pronoun': 'yo'}, {'verb': 'conseguir', 'pronoun': 'tú'}, {'verb': 'conseguir', 'pronoun': 'ella'}, {'verb': 'conseguir', 'pronoun': 'nosotras'}, {'verb': 'conseguir', 'pronoun': 'ustedes'}],
        "phase_2_config": {
            "description": "Spelling Changes conseguir: conseguir",
            "targets": [{'verb': 'conseguir', 'pronoun': 'yo'}, {'verb': 'conseguir', 'pronoun': 'tú'}, {'verb': 'conseguir', 'pronoun': 'ella'}, {'verb': 'conseguir', 'pronoun': 'nosotras'}, {'verb': 'conseguir', 'pronoun': 'ustedes'}],
        },
        "opener_en": "Do you get good prices?",
        "opener_es": "¿Consigues buenos precios?",
    },


    "grammar_spelling_changes_recoger_dirigir_1": {
        "title": "Spelling Changes — recoger + dirigir (1/2)",
        "grammar_level": 5,
        "lesson_number": 5,
        "lesson_type": "conjugation",
        "word_workload": ["recoger", "dirigir"],
        "video_embed_id": "ZxefHnILbqs",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": SPELLING_CHANGES_RECOGER_DIRIGIR_INTRO,
        "drill_config": {
            "answers": {
                "recoger": {"yo": "reco|jo", "tú": "recog|es", "él": "recog|e", "ella": "recog|e", "usted": "recog|e", "nosotros": "recog|emos", "nosotras": "recog|emos", "ellos": "recog|en", "ellas": "recog|en", "ustedes": "recog|en"},
                "dirigir": {"yo": "diri|jo", "tú": "dirig|es", "él": "dirig|e", "ella": "dirig|e", "usted": "dirig|e", "nosotros": "dirig|imos", "nosotras": "dirig|imos", "ellos": "dirig|en", "ellas": "dirig|en", "ustedes": "dirig|en"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": 'You direct the busy traffic.', "es": 'Tú diriges el tráfico ocupado.', "noun_id": None, "type": 'written', "glosses": {'traffic': 'tráfico', 'busy': 'ocupado', 'tráfico': 'traffic', 'ocupado': 'busy'}},
            {"en": 'You pick up the toys.', "es": 'Tú recoges los juguetes.', "noun_id": None, "type": 'auditory', "glosses": {'toys': 'juguetes', 'juguetes': 'toys'}},
            {"en": 'You direct the team.', "es": 'Tú diriges el equipo.', "noun_id": None, "type": 'auditory', "glosses": {'team': 'equipo', 'equipo': 'team'}},
            {"en": 'You all pick up the papers.', "es": 'Ustedes recogen los papeles.', "noun_id": None, "type": 'written', "glosses": {'papers': 'papeles', 'papeles': 'papers'}},
            {"en": 'He picks up the big boxes.', "es": 'Él recoge las cajas grandes.', "noun_id": None, "type": 'written', "glosses": {'boxes': 'cajas', 'big': 'grandes', 'cajas': 'boxes', 'grandes': 'big'}},
            {"en": 'He directs the large team.', "es": 'Él dirige el equipo grande.', "noun_id": None, "type": 'written', "glosses": {'team': 'equipo', 'large': 'grande', 'equipo': 'team', 'grande': 'large'}},
            {"en": 'We (f) pick up the clothes.', "es": 'Nosotras recogemos la ropa.', "noun_id": None, "type": 'auditory', "glosses": {'clothes': 'ropa', 'ropa': 'clothes'}},
            {"en": 'We (m) pick up the old books.', "es": 'Nosotros recogemos los libros viejos.', "noun_id": None, "type": 'auditory', "glosses": {'books': 'libros', 'old': 'viejos', 'libros': 'books', 'viejos': 'old'}},
            {"en": 'We (f) direct the class.', "es": 'Nosotras dirigimos la clase.', "noun_id": None, "type": 'auditory', "glosses": {'class': 'clase', 'clase': 'class'}},
            {"en": 'They (f) direct the small school.', "es": 'Ellas dirigen la escuela pequeña.', "noun_id": None, "type": 'written', "glosses": {'school': 'escuela', 'small': 'pequeña', 'escuela': 'school', 'pequeña': 'small'}},
            {"en": 'You pick up the red apples.', "es": 'Tú recoges las manzanas rojas.', "noun_id": None, "type": 'written', "glosses": {'apples': 'manzanas', 'red': 'rojas', 'manzanas': 'apples', 'rojas': 'red'}},
            {"en": 'She picks up the letters.', "es": 'Ella recoge las cartas.', "noun_id": None, "type": 'written', "glosses": {'letters': 'cartas', 'cartas': 'letters'}},
            {"en": 'We (m) direct the important meeting.', "es": 'Nosotros dirigimos la reunión importante.', "noun_id": None, "type": 'auditory', "glosses": {'meeting': 'reunión', 'important': 'importante', 'reunión': 'meeting', 'importante': 'important'}},
            {"en": 'She directs the play.', "es": 'Ella dirige la obra.', "noun_id": None, "type": 'written', "glosses": {'play': 'obra', 'obra': 'play'}},
            {"en": 'You all direct the project.', "es": 'Ustedes dirigen el proyecto.', "noun_id": None, "type": 'written', "glosses": {'project': 'proyecto', 'proyecto': 'project'}},
            {"en": 'I direct the movie.', "es": 'Yo dirijo la película.', "noun_id": None, "type": 'written', "glosses": {'movie': 'película', 'película': 'movie'}},
            {"en": 'They (f) pick up the small toys.', "es": 'Ellas recogen los juguetes pequeños.', "noun_id": None, "type": 'written', "glosses": {'toys': 'juguetes', 'small': 'pequeños', 'juguetes': 'toys', 'pequeños': 'small'}},
            {"en": 'I pick up the books.', "es": 'Yo recojo los libros.', "noun_id": None, "type": 'written', "glosses": {'books': 'libros', 'libros': 'books'}},
            {"en": 'I direct the new project.', "es": 'Yo dirijo el proyecto nuevo.', "noun_id": None, "type": 'auditory', "glosses": {'project': 'proyecto', 'new': 'nuevo', 'proyecto': 'project', 'nuevo': 'new'}},
            {"en": 'I pick up the clean clothes.', "es": 'Yo recojo la ropa limpia.', "noun_id": None, "type": 'auditory', "glosses": {'clothes': 'ropa', 'clean': 'limpia', 'ropa': 'clothes', 'limpia': 'clean'}},
        ],
        "drill_targets": [{"verb": "recoger", "pronoun": "yo"}, {"verb": "recoger", "pronoun": "tú"}, {"verb": "recoger", "pronoun": "ella"}, {"verb": "recoger", "pronoun": "nosotras"}, {"verb": "recoger", "pronoun": "ustedes"}, {"verb": "dirigir", "pronoun": "yo"}, {"verb": "dirigir", "pronoun": "tú"}, {"verb": "dirigir", "pronoun": "ella"}, {"verb": "dirigir", "pronoun": "nosotras"}, {"verb": "dirigir", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Spelling Changes recoger + dirigir (1/2): recoger, dirigir",
            "targets": [{"verb": "recoger", "pronoun": "yo"}, {"verb": "recoger", "pronoun": "tú"}, {"verb": "recoger", "pronoun": "ella"}, {"verb": "recoger", "pronoun": "nosotras"}, {"verb": "recoger", "pronoun": "ustedes"}, {"verb": "dirigir", "pronoun": "yo"}, {"verb": "dirigir", "pronoun": "tú"}, {"verb": "dirigir", "pronoun": "ella"}, {"verb": "dirigir", "pronoun": "nosotras"}, {"verb": "dirigir", "pronoun": "ustedes"}],
        },
        "opener_en": "Do you pick up the kids?",
        "opener_es": "¿Recoges a los niños?",
    },


    "grammar_spelling_changes_convencer": {
        "title": "Spelling Changes — convencer ",
        "grammar_level": 5,
        "lesson_number": 7,
        "lesson_type": "conjugation",
        "word_workload": ["convencer"],
        "video_embed_id": "ZxefHnILbqs",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": SPELLING_CHANGES_CONVENCER_CONTINUAR_INTRO,
        "drill_config": {
            "answers": {
                "convencer": {'yo': 'conven|zo', 'tú': 'convenc|es', 'él': 'convenc|e', 'ella': 'convenc|e', 'usted': 'convenc|e', 'nosotros': 'convenc|emos', 'nosotras': 'convenc|emos', 'ellos': 'convenc|en', 'ellas': 'convenc|en', 'ustedes': 'convenc|en'},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": 'I convince my friends.', "es": 'Yo convenzo a mis amigos.', "noun_id": None, "type": 'written', "glosses": {'friends': 'amigos', 'amigos': 'friends'}},
            {"en": 'You convince your mother.', "es": 'Tú convences a tu madre.', "noun_id": None, "type": 'auditory', "glosses": {'mother': 'madre', 'madre': 'mother'}},
            {"en": 'She convinces the teacher.', "es": 'Ella convence al profesor.', "noun_id": None, "type": 'written', "glosses": {'teacher': 'profesor', 'profesor': 'teacher'}},
            {"en": 'We (f) convince the clients.', "es": 'Nosotras convencemos a las clientas.', "noun_id": None, "type": 'auditory', "glosses": {'clients': 'clientas', 'clientas': 'clients'}},
            {"en": 'You all convince the students.', "es": 'Ustedes convencen a los estudiantes.', "noun_id": None, "type": 'written', "glosses": {'students': 'estudiantes', 'estudiantes': 'students'}},
            {"en": 'You convince the teacher.', "es": 'Tú convences al profesor.', "noun_id": None, "type": 'written', "glosses": {'teacher': 'profesor', 'profesor': 'teacher'}},
            {"en": 'I convince my friends.', "es": 'Yo convenzo a mis amigos.', "noun_id": None, "type": 'auditory', "glosses": {'friends': 'amigos', 'amigos': 'friends'}},
            {"en": 'He convinces the client.', "es": 'Él convence al cliente.', "noun_id": None, "type": 'written', "glosses": {'client': 'cliente', 'cliente': 'client'}},
            {"en": 'We convince the team.', "es": 'Nosotros convencemos al equipo.', "noun_id": None, "type": 'auditory', "glosses": {'team': 'equipo', 'equipo': 'team'}},
            {"en": 'They (f) convince the neighbors.', "es": 'Ellas convencen a las vecinas.', "noun_id": None, "type": 'written', "glosses": {'neighbors': 'vecinas', 'vecinas': 'neighbors'}},
        ],
        "drill_targets": [{'verb': 'convencer', 'pronoun': 'yo'}, {'verb': 'convencer', 'pronoun': 'tú'}, {'verb': 'convencer', 'pronoun': 'ella'}, {'verb': 'convencer', 'pronoun': 'nosotras'}, {'verb': 'convencer', 'pronoun': 'ustedes'}],
        "phase_2_config": {
            "description": "Spelling Changes convencer: convencer",
            "targets": [{'verb': 'convencer', 'pronoun': 'yo'}, {'verb': 'convencer', 'pronoun': 'tú'}, {'verb': 'convencer', 'pronoun': 'ella'}, {'verb': 'convencer', 'pronoun': 'nosotras'}, {'verb': 'convencer', 'pronoun': 'ustedes'}],
        },
        "opener_en": "Do you convince your friends?",
        "opener_es": "¿Convences a tus amigos?",
    },
    "grammar_spelling_changes_continuar": {
        "title": "Spelling Changes — continuar ",
        "grammar_level": 5,
        "lesson_number": 8,
        "lesson_type": "conjugation",
        "word_workload": ["continuar"],
        "video_embed_id": "ZxefHnILbqs",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": SPELLING_CHANGES_CONVENCER_CONTINUAR_INTRO,
        "drill_config": {
            "answers": {
                "continuar": {'yo': 'contin|úo', 'tú': 'contin|úas', 'él': 'contin|úa', 'ella': 'contin|úa', 'usted': 'contin|úa', 'nosotros': 'contin|uamos', 'nosotras': 'contin|uamos', 'ellos': 'contin|úan', 'ellas': 'contin|úan', 'ustedes': 'contin|úan'},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": 'I continue the project.', "es": 'Yo continúo el proyecto.', "noun_id": None, "type": 'written', "glosses": {'project': 'proyecto', 'proyecto': 'project'}},
            {"en": 'You continue your studies.', "es": 'Tú continúas tus estudios.', "noun_id": None, "type": 'auditory', "glosses": {'studies': 'estudios', 'estudios': 'studies'}},
            {"en": 'She continues the story.', "es": 'Ella continúa la historia.', "noun_id": None, "type": 'written', "glosses": {'story': 'historia', 'historia': 'story'}},
            {"en": 'We (f) continue the conversation.', "es": 'Nosotras continuamos la conversación.', "noun_id": None, "type": 'auditory', "glosses": {'conversation': 'conversación', 'conversación': 'conversation'}},
            {"en": 'You all continue the work.', "es": 'Ustedes continúan el trabajo.', "noun_id": None, "type": 'written', "glosses": {'work': 'trabajo', 'trabajo': 'work'}},
            {"en": 'You continue the story.', "es": 'Tú continúas la historia.', "noun_id": None, "type": 'written', "glosses": {'story': 'historia', 'historia': 'story'}},
            {"en": 'I continue the work.', "es": 'Yo continúo el trabajo.', "noun_id": None, "type": 'auditory', "glosses": {'work': 'trabajo', 'trabajo': 'work'}},
            {"en": 'He continues the journey.', "es": 'Él continúa el viaje.', "noun_id": None, "type": 'written', "glosses": {'journey': 'viaje', 'viaje': 'journey'}},
            {"en": 'We continue the lesson.', "es": 'Nosotros continuamos la lección.', "noun_id": None, "type": 'auditory', "glosses": {'lesson': 'lección', 'lección': 'lesson'}},
            {"en": 'They (f) continue the game.', "es": 'Ellas continúan el juego.', "noun_id": None, "type": 'written', "glosses": {'game': 'juego', 'juego': 'game'}},
        ],
        "drill_targets": [{'verb': 'continuar', 'pronoun': 'yo'}, {'verb': 'continuar', 'pronoun': 'tú'}, {'verb': 'continuar', 'pronoun': 'ella'}, {'verb': 'continuar', 'pronoun': 'nosotras'}, {'verb': 'continuar', 'pronoun': 'ustedes'}],
        "phase_2_config": {
            "description": "Spelling Changes continuar: continuar",
            "targets": [{'verb': 'continuar', 'pronoun': 'yo'}, {'verb': 'continuar', 'pronoun': 'tú'}, {'verb': 'continuar', 'pronoun': 'ella'}, {'verb': 'continuar', 'pronoun': 'nosotras'}, {'verb': 'continuar', 'pronoun': 'ustedes'}],
        },
        "opener_en": "Do you continue studying?",
        "opener_es": "¿Continúas estudiando?",
    },


    "grammar_spelling_changes_conocer_producir_chat": {
        "title": "Spelling Changes — conocer + producir Chat",
        "grammar_level": 5,
        "lesson_number": 2.5,
        "lesson_type": "conjugation",
        "word_workload": ["conocer", "producir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Spelling Changes conocer + producir chat: conocer, producir", "targets": [{"verb": "conocer", "pronoun": "yo"}, {"verb": "conocer", "pronoun": "tú"}, {"verb": "conocer", "pronoun": "ella"}, {"verb": "conocer", "pronoun": "nosotras"}, {"verb": "conocer", "pronoun": "ustedes"}, {"verb": "producir", "pronoun": "tú"}, {"verb": "producir", "pronoun": "yo"}, {"verb": "producir", "pronoun": "él"}, {"verb": "producir", "pronoun": "nosotros"}, {"verb": "producir", "pronoun": "ellas"}]},
    },

    "grammar_spelling_changes_construir_conseguir_chat": {
        "title": "Spelling Changes — construir + conseguir Chat",
        "grammar_level": 5,
        "lesson_number": 4.5,
        "lesson_type": "conjugation",
        "word_workload": ["construir", "conseguir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Spelling Changes construir + conseguir chat: construir, conseguir", "targets": [{"verb": "construir", "pronoun": "yo"}, {"verb": "construir", "pronoun": "tú"}, {"verb": "construir", "pronoun": "ella"}, {"verb": "construir", "pronoun": "nosotras"}, {"verb": "construir", "pronoun": "ustedes"}, {"verb": "conseguir", "pronoun": "tú"}, {"verb": "conseguir", "pronoun": "yo"}, {"verb": "conseguir", "pronoun": "él"}, {"verb": "conseguir", "pronoun": "nosotros"}, {"verb": "conseguir", "pronoun": "ellas"}]},
    },

    "grammar_spelling_changes_recoger_dirigir_chat": {
        "title": "Spelling Changes — recoger + dirigir Chat",
        "grammar_level": 5,
        "lesson_number": 6.5,
        "lesson_type": "conjugation",
        "word_workload": ["recoger", "dirigir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Spelling Changes recoger + dirigir chat: recoger, dirigir", "targets": [{"verb": "recoger", "pronoun": "yo"}, {"verb": "recoger", "pronoun": "tú"}, {"verb": "recoger", "pronoun": "ella"}, {"verb": "recoger", "pronoun": "nosotras"}, {"verb": "recoger", "pronoun": "ustedes"}, {"verb": "dirigir", "pronoun": "tú"}, {"verb": "dirigir", "pronoun": "yo"}, {"verb": "dirigir", "pronoun": "él"}, {"verb": "dirigir", "pronoun": "nosotros"}, {"verb": "dirigir", "pronoun": "ellas"}]},
    },

    "grammar_spelling_changes_convencer_continuar_chat": {
        "title": "Spelling Changes — convencer + continuar Chat",
        "grammar_level": 5,
        "lesson_number": 8.5,
        "lesson_type": "conjugation",
        "word_workload": ["convencer", "continuar"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Spelling Changes convencer + continuar chat: convencer, continuar", "targets": [{"verb": "convencer", "pronoun": "yo"}, {"verb": "convencer", "pronoun": "tú"}, {"verb": "convencer", "pronoun": "ella"}, {"verb": "convencer", "pronoun": "nosotras"}, {"verb": "convencer", "pronoun": "ustedes"}, {"verb": "continuar", "pronoun": "tú"}, {"verb": "continuar", "pronoun": "yo"}, {"verb": "continuar", "pronoun": "él"}, {"verb": "continuar", "pronoun": "nosotros"}, {"verb": "continuar", "pronoun": "ellas"}]},
    },

    # ── From _gl6_output.py ──

"grammar_present_o_ue_poder_volver_1": {
        "title": "Stem o→ue — poder + volver (1/2)",
        "grammar_level": 6,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ["poder", "volver"],
        "video_embed_id": "9JFpAFFVQzc",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": PRESENT_O_UE_PODER_VOLVER_INTRO,
        "drill_config": {
            "answers": {
                "poder": {"yo": "p|uedo", "tú": "p|uedes", "él": "p|uede", "ella": "p|uede", "usted": "p|uede", "nosotros": "pod|emos", "nosotras": "pod|emos", "ellos": "p|ueden", "ellas": "p|ueden", "ustedes": "p|ueden"},
                "volver": {"yo": "v|uelvo", "tú": "v|uelves", "él": "v|uelve", "ella": "v|uelve", "usted": "v|uelve", "nosotros": "volv|emos", "nosotras": "volv|emos", "ellos": "v|uelven", "ellas": "v|uelven", "ustedes": "v|uelven"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": 'You return home early.', "es": 'Tú vuelves a casa temprano.', "noun_id": None, "type": 'written', "glosses": {'home': 'casa', 'casa': 'home', 'early': 'temprano', 'temprano': 'early'}},
            {"en": 'I return to the park.', "es": 'Yo vuelvo al parque.', "noun_id": None, "type": 'auditory', "glosses": {'park': 'parque', 'parque': 'park'}},
            {"en": 'You can speak Spanish.', "es": 'Tú puedes hablar español.', "noun_id": None, "type": 'written', "glosses": {'Spanish': 'español', 'spanish': 'español', 'español': 'Spanish'}},
            {"en": 'I can swim well', "es": 'Yo puedo nadar bien', "noun_id": None, "type": 'written', "glosses": {'well': 'bien', 'bien': 'well'}},
            {"en": 'You all return now', "es": 'Ustedes vuelven ahora', "noun_id": None, "type": 'written', "glosses": {'now': 'ahora', 'ahora': 'now'}},
            {"en": 'You all can eat lunch', "es": 'Ustedes pueden comer el almuerzo', "noun_id": None, "type": 'written', "glosses": {'lunch': 'almuerzo', 'almuerzo': 'lunch'}},
            {"en": 'You can open the door', "es": 'Tú puedes abrir la puerta', "noun_id": None, "type": 'auditory', "glosses": {'door': 'puerta', 'puerta': 'door'}},
            {"en": 'We (f) can speak Spanish', "es": 'Nosotras podemos hablar español', "noun_id": None, "type": 'auditory', "glosses": {'spanish': 'español', 'español': 'spanish'}},
            {"en": 'We (m) can eat lunch.', "es": 'Nosotros podemos comer el almuerzo.', "noun_id": None, "type": 'auditory', "glosses": {'lunch': 'almuerzo', 'almuerzo': 'lunch'}},
            {"en": 'She returns from school', "es": 'Ella vuelve de la escuela', "noun_id": None, "type": 'written', "glosses": {'school': 'escuela', 'escuela': 'school'}},
            {"en": 'They (f) return late.', "es": 'Ellas vuelven tarde.', "noun_id": None, "type": 'written', "glosses": {'late': 'tarde', 'tarde': 'late'}},
            {"en": 'We (m) return with friends.', "es": 'Nosotros volvemos con amigos.', "noun_id": None, "type": 'auditory', "glosses": {'friends': 'amigos', 'amigos': 'friends'}},
            {"en": 'He returns the book today.', "es": 'Él vuelve el libro hoy.', "noun_id": None, "type": 'written', "glosses": {'book': 'libro', 'libro': 'book', 'today': 'hoy', 'hoy': 'today'}},
            {"en": 'They (f) can run fast.', "es": 'Ellas pueden correr rápido.', "noun_id": None, "type": 'written', "glosses": {'fast': 'rápido', 'rápido': 'fast'}},
            {"en": 'I return home late', "es": 'Yo vuelvo a casa tarde', "noun_id": None, "type": 'written', "glosses": {'home': 'casa', 'late': 'tarde', 'casa': 'home', 'tarde': 'late'}},
            {"en": 'She can read the book', "es": 'Ella puede leer el libro', "noun_id": None, "type": 'written', "glosses": {'book': 'libro', 'libro': 'book'}},
            {"en": 'He can open the door.', "es": 'Él puede abrir la puerta.', "noun_id": None, "type": 'written', "glosses": {'door': 'puerta', 'puerta': 'door'}},
            {"en": 'We (f) return at five', "es": 'Nosotras volvemos a las cinco', "noun_id": None, "type": 'auditory', "glosses": {'five': 'cinco', 'cinco': 'five'}},
            {"en": 'I can read the book.', "es": 'Yo puedo leer el libro.', "noun_id": None, "type": 'auditory', "glosses": {'book': 'libro', 'libro': 'book'}},
            {"en": 'You return every day', "es": 'Tú vuelves todos los días', "noun_id": None, "type": 'auditory', "glosses": {'day': 'días', 'every': 'todos', 'días': 'day', 'todos': 'every'}},
        ],
        "drill_targets": [{"verb": "poder", "pronoun": "yo"}, {"verb": "poder", "pronoun": "tú"}, {"verb": "poder", "pronoun": "ella"}, {"verb": "poder", "pronoun": "nosotras"}, {"verb": "poder", "pronoun": "ustedes"}, {"verb": "volver", "pronoun": "yo"}, {"verb": "volver", "pronoun": "tú"}, {"verb": "volver", "pronoun": "ella"}, {"verb": "volver", "pronoun": "nosotras"}, {"verb": "volver", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Stem o→ue poder + volver (1/2): poder, volver",
            "targets": [{"verb": "poder", "pronoun": "yo"}, {"verb": "poder", "pronoun": "tú"}, {"verb": "poder", "pronoun": "ella"}, {"verb": "poder", "pronoun": "nosotras"}, {"verb": "poder", "pronoun": "ustedes"}, {"verb": "volver", "pronoun": "yo"}, {"verb": "volver", "pronoun": "tú"}, {"verb": "volver", "pronoun": "ella"}, {"verb": "volver", "pronoun": "nosotras"}, {"verb": "volver", "pronoun": "ustedes"}],
        },
        "opener_en": "Can you help me?",
        "opener_es": "¿Puedes ayudarme?",
    },


    "grammar_present_o_ue_dormir_morir_1": {
        "title": "Stem o→ue — dormir + morir (1/2)",
        "grammar_level": 6,
        "lesson_number": 3,
        "lesson_type": "conjugation",
        "word_workload": ["dormir", "morir"],
        "video_embed_id": "9JFpAFFVQzc",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": PRESENT_O_UE_DORMIR_MORIR_INTRO,
        "drill_config": {
            "answers": {
                "dormir": {"yo": "d|uermo", "tú": "d|uermes", "él": "d|uerme", "ella": "d|uerme", "usted": "d|uerme", "nosotros": "dorm|imos", "nosotras": "dorm|imos", "ellos": "d|uermen", "ellas": "d|uermen", "ustedes": "d|uermen"},
                "morir": {"yo": "m|uero", "tú": "m|ueres", "él": "m|uere", "ella": "m|uere", "usted": "m|uere", "nosotros": "mor|imos", "nosotras": "mor|imos", "ellos": "m|ueren", "ellas": "m|ueren", "ustedes": "m|ueren"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": 'I die old.', "es": 'Yo muero viejo.', "noun_id": None, "type": 'auditory', "glosses": {'old': 'viejo', 'viejo': 'old'}},
            {"en": 'I die in the story.', "es": 'Yo muero en la historia.', "noun_id": None, "type": 'written', "glosses": {'story': 'historia', 'historia': 'story'}},
            {"en": 'You die young.', "es": 'Tú mueres joven.', "noun_id": None, "type": 'written', "glosses": {'young': 'joven', 'joven': 'young'}},
            {"en": 'He dies peacefully.', "es": 'Él muere pacíficamente.', "noun_id": None, "type": 'written', "glosses": {'peacefully': 'pacíficamente', 'pacíficamente': 'peacefully'}},
            {"en": 'You all sleep during the day.', "es": 'Ustedes duermen durante el día.', "noun_id": None, "type": 'written', "glosses": {'day': 'día', 'all': 'all', 'día': 'day'}},
            {"en": 'She dies at the end.', "es": 'Ella muere al final.', "noun_id": None, "type": 'written', "glosses": {'end': 'final', 'final': 'end'}},
            {"en": 'We (m) die bravely.', "es": 'Nosotros morimos valientemente.', "noun_id": None, "type": 'auditory', "glosses": {'bravely': 'valientemente', 'valientemente': 'bravely'}},
            {"en": 'You die in the movie.', "es": 'Tú mueres en la película.', "noun_id": None, "type": 'auditory', "glosses": {'movie': 'película', 'película': 'movie'}},
            {"en": 'You sleep early today.', "es": 'Tú duermes temprano hoy.', "noun_id": None, "type": 'auditory', "glosses": {'today': 'hoy', 'early': 'temprano', 'hoy': 'today', 'temprano': 'early'}},
            {"en": 'She sleeps in the bedroom.', "es": 'Ella duerme en el dormitorio.', "noun_id": None, "type": 'written', "glosses": {'bedroom': 'dormitorio', 'dormitorio': 'bedroom'}},
            {"en": 'We (f) die in the legend.', "es": 'Nosotras morimos en la leyenda.', "noun_id": None, "type": 'auditory', "glosses": {'legend': 'leyenda', 'leyenda': 'legend'}},
            {"en": 'He sleeps in the room.', "es": 'Él duerme en la habitación.', "noun_id": None, "type": 'written', "glosses": {'room': 'habitación', 'habitación': 'room'}},
            {"en": 'I sleep well every night.', "es": 'Yo duermo bien cada noche.', "noun_id": None, "type": 'written', "glosses": {'night': 'noche', 'bien': 'well', 'every': 'cada', 'noche': 'night', 'well': 'bien', 'cada': 'every'}},
            {"en": 'You all die in the game.', "es": 'Ustedes mueren en el juego.', "noun_id": None, "type": 'written', "glosses": {'game': 'juego', 'juego': 'game'}},
            {"en": 'They (f) sleep deeply.', "es": 'Ellas duermen profundamente.', "noun_id": None, "type": 'written', "glosses": {'deeply': 'profundamente', 'profundamente': 'deeply'}},
            {"en": 'They (f) die quietly.', "es": 'Ellas mueren silenciosamente.', "noun_id": None, "type": 'written', "glosses": {'quietly': 'silenciosamente', 'silenciosamente': 'quietly'}},
            {"en": 'I sleep eight hours.', "es": 'Yo duermo ocho horas.', "noun_id": None, "type": 'auditory', "glosses": {'hours': 'horas', 'eight': 'ocho', 'horas': 'hours', 'ocho': 'eight'}},
            {"en": 'We (m) sleep early.', "es": 'Nosotros dormimos temprano.', "noun_id": None, "type": 'auditory', "glosses": {'early': 'temprano', 'temprano': 'early'}},
            {"en": 'You sleep well.', "es": 'Tú duermes bien.', "noun_id": None, "type": 'written', "glosses": {'well': 'bien', 'bien': 'well'}},
            {"en": 'We (f) sleep eight hours.', "es": 'Nosotras dormimos ocho horas.', "noun_id": None, "type": 'auditory', "glosses": {'hours': 'horas', 'eight': 'ocho', 'horas': 'hours', 'ocho': 'eight'}},
        ],
        "drill_targets": [{"verb": "dormir", "pronoun": "yo"}, {"verb": "dormir", "pronoun": "tú"}, {"verb": "dormir", "pronoun": "ella"}, {"verb": "dormir", "pronoun": "nosotras"}, {"verb": "dormir", "pronoun": "ustedes"}, {"verb": "morir", "pronoun": "yo"}, {"verb": "morir", "pronoun": "tú"}, {"verb": "morir", "pronoun": "ella"}, {"verb": "morir", "pronoun": "nosotras"}, {"verb": "morir", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Stem o→ue dormir + morir (1/2): dormir, morir",
            "targets": [{"verb": "dormir", "pronoun": "yo"}, {"verb": "dormir", "pronoun": "tú"}, {"verb": "dormir", "pronoun": "ella"}, {"verb": "dormir", "pronoun": "nosotras"}, {"verb": "dormir", "pronoun": "ustedes"}, {"verb": "morir", "pronoun": "yo"}, {"verb": "morir", "pronoun": "tú"}, {"verb": "morir", "pronoun": "ella"}, {"verb": "morir", "pronoun": "nosotras"}, {"verb": "morir", "pronoun": "ustedes"}],
        },
        "opener_en": "Do you sleep well?",
        "opener_es": "¿Duermes bien?",
    },


    "grammar_present_o_ue_mover_almorzar_1": {
        "title": "Stem o→ue — mover + almorzar (1/2)",
        "grammar_level": 6,
        "lesson_number": 5,
        "lesson_type": "conjugation",
        "word_workload": ["mover", "almorzar"],
        "video_embed_id": "9JFpAFFVQzc",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": PRESENT_O_UE_MOVER_ALMORZAR_INTRO,
        "drill_config": {
            "answers": {
                "mover": {"yo": "m|uevo", "tú": "m|ueves", "él": "m|ueve", "ella": "m|ueve", "usted": "m|ueve", "nosotros": "mov|emos", "nosotras": "mov|emos", "ellos": "m|ueven", "ellas": "m|ueven", "ustedes": "m|ueven"},
                "almorzar": {"yo": "alm|uerzo", "tú": "alm|uerzas", "él": "alm|uerza", "ella": "alm|uerza", "usted": "alm|uerza", "nosotros": "almorz|amos", "nosotras": "almorz|amos", "ellos": "alm|uerzan", "ellas": "alm|uerzan", "ustedes": "alm|uerzan"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": 'You have lunch with friends.', "es": 'Tú almuerzas con amigos.', "noun_id": None, "type": 'auditory', "glosses": {'friends': 'amigos', 'amigos': 'friends'}},
            {"en": 'We (f) have lunch early.', "es": 'Nosotras almorzamos temprano.', "noun_id": None, "type": 'auditory', "glosses": {'early': 'temprano', 'temprano': 'early'}},
            {"en": 'They (f) move the books.', "es": 'Ellas mueven los libros.', "noun_id": None, "type": 'written', "glosses": {'books': 'libros', 'libros': 'books'}},
            {"en": 'She moves the box.', "es": 'Ella mueve la caja.', "noun_id": None, "type": 'written', "glosses": {'box': 'caja', 'caja': 'box'}},
            {"en": 'We (m) move the sofa.', "es": 'Nosotros movemos el sofá.', "noun_id": None, "type": 'auditory', "glosses": {'sofa': 'sofá', 'sofá': 'sofa'}},
            {"en": 'She has lunch at the park.', "es": 'Ella almuerza en el parque.', "noun_id": None, "type": 'written', "glosses": {'park': 'parque', 'parque': 'park'}},
            {"en": 'He has lunch in the park.', "es": 'Él almuerza en el parque.', "noun_id": None, "type": 'written', "glosses": {'park': 'parque', 'parque': 'park'}},
            {"en": 'You have lunch at noon.', "es": 'Tú almuerzas al mediodía.', "noun_id": None, "type": 'written', "glosses": {'noon': 'mediodía', 'mediodía': 'noon'}},
            {"en": 'I move the table.', "es": 'Yo muevo la mesa.', "noun_id": None, "type": 'written', "glosses": {'table': 'mesa', 'mesa': 'table'}},
            {"en": 'I move the chair.', "es": 'Yo muevo la silla.', "noun_id": None, "type": 'auditory', "glosses": {'chair': 'silla', 'silla': 'chair'}},
            {"en": 'We (m) have lunch early.', "es": 'Nosotros almorzamos temprano.', "noun_id": None, "type": 'auditory', "glosses": {'early': 'temprano', 'temprano': 'early'}},
            {"en": 'You move the table.', "es": 'Tú mueves la mesa.', "noun_id": None, "type": 'written', "glosses": {'table': 'mesa', 'mesa': 'table'}},
            {"en": 'He moves the box.', "es": 'Él mueve la caja.', "noun_id": None, "type": 'written', "glosses": {'box': 'caja', 'caja': 'box'}},
            {"en": 'We (f) move the books.', "es": 'Nosotras movemos los libros.', "noun_id": None, "type": 'auditory', "glosses": {'books': 'libros', 'libros': 'books'}},
            {"en": 'They (f) have lunch together.', "es": 'Ellas almuerzan juntas.', "noun_id": None, "type": 'written', "glosses": {'together': 'juntas', 'juntas': 'together'}},
            {"en": 'I have lunch at noon.', "es": 'Yo almuerzo al mediodía.', "noun_id": None, "type": 'written', "glosses": {'noon': 'mediodía', 'mediodía': 'noon'}},
            {"en": 'You move the chair.', "es": 'Tú mueves la silla.', "noun_id": None, "type": 'auditory', "glosses": {'chair': 'silla', 'silla': 'chair'}},
            {"en": 'I have lunch with friends.', "es": 'Yo almuerzo con amigos.', "noun_id": None, "type": 'auditory', "glosses": {'friends': 'amigos', 'amigos': 'friends'}},
            {"en": 'You all move the furniture.', "es": 'Ustedes mueven los muebles.', "noun_id": None, "type": 'written', "glosses": {'furniture': 'muebles', 'muebles': 'furniture'}},
            {"en": 'You all have lunch together.', "es": 'Ustedes almuerzan juntos.', "noun_id": None, "type": 'written', "glosses": {'together': 'juntos', 'juntos': 'together'}},
        ],
        "drill_targets": [{"verb": "mover", "pronoun": "yo"}, {"verb": "mover", "pronoun": "tú"}, {"verb": "mover", "pronoun": "ella"}, {"verb": "mover", "pronoun": "nosotras"}, {"verb": "mover", "pronoun": "ustedes"}, {"verb": "almorzar", "pronoun": "yo"}, {"verb": "almorzar", "pronoun": "tú"}, {"verb": "almorzar", "pronoun": "ella"}, {"verb": "almorzar", "pronoun": "nosotras"}, {"verb": "almorzar", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Stem o→ue mover + almorzar (1/2): mover, almorzar",
            "targets": [{"verb": "mover", "pronoun": "yo"}, {"verb": "mover", "pronoun": "tú"}, {"verb": "mover", "pronoun": "ella"}, {"verb": "mover", "pronoun": "nosotras"}, {"verb": "mover", "pronoun": "ustedes"}, {"verb": "almorzar", "pronoun": "yo"}, {"verb": "almorzar", "pronoun": "tú"}, {"verb": "almorzar", "pronoun": "ella"}, {"verb": "almorzar", "pronoun": "nosotras"}, {"verb": "almorzar", "pronoun": "ustedes"}],
        },
        "opener_en": "Do you move the chair?",
        "opener_es": "¿Mueves la silla?",
    },


    "grammar_present_o_ue_poder_volver_chat": {
        "title": "Stem o→ue — poder + volver Chat",
        "grammar_level": 6,
        "lesson_number": 2.5,
        "lesson_type": "conjugation",
        "word_workload": ["poder", "volver"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Stem o→ue poder + volver chat: poder, volver", "targets": [{"verb": "poder", "pronoun": "yo"}, {"verb": "poder", "pronoun": "tú"}, {"verb": "poder", "pronoun": "ella"}, {"verb": "poder", "pronoun": "nosotras"}, {"verb": "poder", "pronoun": "ustedes"}, {"verb": "volver", "pronoun": "tú"}, {"verb": "volver", "pronoun": "yo"}, {"verb": "volver", "pronoun": "él"}, {"verb": "volver", "pronoun": "nosotros"}, {"verb": "volver", "pronoun": "ellas"}]},
    },

    "grammar_present_o_ue_dormir_morir_chat": {
        "title": "Stem o→ue — dormir + morir Chat",
        "grammar_level": 6,
        "lesson_number": 4.5,
        "lesson_type": "conjugation",
        "word_workload": ["dormir", "morir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Stem o→ue dormir + morir chat: dormir, morir", "targets": [{"verb": "dormir", "pronoun": "yo"}, {"verb": "dormir", "pronoun": "tú"}, {"verb": "dormir", "pronoun": "ella"}, {"verb": "dormir", "pronoun": "nosotras"}, {"verb": "dormir", "pronoun": "ustedes"}, {"verb": "morir", "pronoun": "tú"}, {"verb": "morir", "pronoun": "yo"}, {"verb": "morir", "pronoun": "él"}, {"verb": "morir", "pronoun": "nosotros"}, {"verb": "morir", "pronoun": "ellas"}]},
    },

    "grammar_present_o_ue_mover_almorzar_chat": {
        "title": "Stem o→ue — mover + almorzar Chat",
        "grammar_level": 6,
        "lesson_number": 6.5,
        "lesson_type": "conjugation",
        "word_workload": ["mover", "almorzar"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Stem o→ue mover + almorzar chat: mover, almorzar", "targets": [{"verb": "mover", "pronoun": "yo"}, {"verb": "mover", "pronoun": "tú"}, {"verb": "mover", "pronoun": "ella"}, {"verb": "mover", "pronoun": "nosotras"}, {"verb": "mover", "pronoun": "ustedes"}, {"verb": "almorzar", "pronoun": "tú"}, {"verb": "almorzar", "pronoun": "yo"}, {"verb": "almorzar", "pronoun": "él"}, {"verb": "almorzar", "pronoun": "nosotros"}, {"verb": "almorzar", "pronoun": "ellas"}]},
    },

    # ── From _gl7_output.py ──

"grammar_present_e_ie_querer_pensar_1": {
        "title": "Stem e→ie — querer + pensar (1/2)",
        "grammar_level": 7,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ["querer", "pensar"],
        "video_embed_id": "rk0AwBA9PEa",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": PRESENT_E_IE_QUERER_PENSAR_INTRO,
        "drill_config": {
            "answers": {
                "querer": {"yo": "qu|iero", "tú": "qu|ieres", "él": "qu|iere", "ella": "qu|iere", "usted": "qu|iere", "nosotros": "quer|emos", "nosotras": "quer|emos", "ellos": "qu|ieren", "ellas": "qu|ieren", "ustedes": "qu|ieren"},
                "pensar": {"yo": "p|ienso", "tú": "p|iensas", "él": "p|iensa", "ella": "p|iensa", "usted": "p|iensa", "nosotros": "pens|amos", "nosotras": "pens|amos", "ellos": "p|iensan", "ellas": "p|iensan", "ustedes": "p|iensan"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": 'You want a coffee.', "es": 'Tú quieres un café.', "noun_id": None, "type": 'written', "glosses": {'coffee': 'café', 'café': 'coffee'}},
            {"en": 'We (f) think about our friends.', "es": 'Nosotras pensamos en nuestras amigas.', "noun_id": None, "type": 'auditory', "glosses": {'friend': 'amigas', 'amigas': 'friend', 'our': 'nuestras', 'nuestras': 'our'}},
            {"en": 'I want a new book.', "es": 'Yo quiero un libro nuevo.', "noun_id": None, "type": 'auditory', "glosses": {'book': 'libro', 'new': 'nuevo', 'libro': 'book', 'nuevo': 'new'}},
            {"en": 'We (f) want fresh water.', "es": 'Nosotras queremos agua fresca.', "noun_id": None, "type": 'auditory', "glosses": {'water': 'agua', 'agua': 'water', 'fresh': 'fresca', 'fresca': 'fresh'}},
            {"en": 'We (m) want to eat now.', "es": 'Nosotros queremos comer ahora.', "noun_id": None, "type": 'auditory', "glosses": {'now': 'ahora', 'ahora': 'now'}},
            {"en": 'They (f) want big houses.', "es": 'Ellas quieren casas grandes.', "noun_id": None, "type": 'written', "glosses": {'houses': 'casas', 'big': 'grande', 'casas': 'houses', 'grande': 'big'}},
            {"en": 'I think about the blue sky.', "es": 'Yo pienso en el cielo azul.', "noun_id": None, "type": 'written', "glosses": {'sky': 'cielo', 'cielo': 'sky', 'blue': 'azul', 'azul': 'blue'}},
            {"en": 'They (f) think the city is beautiful.', "es": 'Ellas piensan que la ciudad es hermosa.', "noun_id": None, "type": 'written', "glosses": {'city': 'ciudad', 'beautiful': 'hermosa', 'ciudad': 'city', 'hermosa': 'beautiful'}},
            {"en": 'You think the movie is good.', "es": 'Tú piensas que la película es buena.', "noun_id": None, "type": 'auditory', "glosses": {'movie': 'película', 'película': 'movie', 'good': 'buena', 'buena': 'good'}},
            {"en": 'She wants a new book.', "es": 'Ella quiere un libro nuevo.', "noun_id": None, "type": 'written', "glosses": {'book': 'libro', 'libro': 'book', 'new': 'nuevo', 'nuevo': 'new'}},
            {"en": 'You (pl) want cold drinks.', "es": 'Ustedes quieren bebidas frías.', "noun_id": None, "type": 'written', "glosses": {'drink': 'bebidas', 'bebidas': 'drink', 'cold': 'frías', 'frías': 'cold'}},
            {"en": 'You (pl) think the test is easy.', "es": 'Ustedes piensan que el examen es fácil.', "noun_id": None, "type": 'written', "glosses": {'test': 'examen', 'examen': 'test', 'easy': 'fácil', 'fácil': 'easy'}},
            {"en": 'She thinks the city is big.', "es": 'Ella piensa que la ciudad es grande.', "noun_id": None, "type": 'written', "glosses": {'city': 'ciudad', 'ciudad': 'city', 'big': 'grande', 'grande': 'big'}},
            {"en": 'I want a red apple.', "es": 'Yo quiero una manzana roja.', "noun_id": None, "type": 'written', "glosses": {'apple': 'manzana', 'manzana': 'apple', 'red': 'roja', 'roja': 'red'}},
            {"en": 'He thinks the movie is good.', "es": 'Él piensa que la película es buena.', "noun_id": None, "type": 'written', "glosses": {'movie': 'película', 'good': 'buena', 'película': 'movie', 'buena': 'good'}},
            {"en": 'He wants the red car.', "es": 'Él quiere el coche rojo.', "noun_id": None, "type": 'written', "glosses": {'car': 'coche', 'red': 'rojo', 'coche': 'car', 'rojo': 'red'}},
            {"en": 'I think about my family.', "es": 'Yo pienso en mi familia.', "noun_id": None, "type": 'auditory', "glosses": {'family': 'familia', 'familia': 'family'}},
            {"en": 'You want the big house.', "es": 'Tú quieres la casa grande.', "noun_id": None, "type": 'auditory', "glosses": {'house': 'casa', 'casa': 'house', 'big': 'grande', 'grande': 'big'}},
            {"en": 'We (m) think a lot.', "es": 'Nosotros pensamos mucho.', "noun_id": None, "type": 'auditory', "glosses": {'much': 'mucho', 'mucho': 'much'}},
            {"en": 'You think the test is easy.', "es": 'Tú piensas que el examen es fácil.', "noun_id": None, "type": 'written', "glosses": {'test': 'examen', 'easy': 'fácil', 'examen': 'test', 'fácil': 'easy'}},
        ],
        "drill_targets": [{"verb": "querer", "pronoun": "yo"}, {"verb": "querer", "pronoun": "tú"}, {"verb": "querer", "pronoun": "ella"}, {"verb": "querer", "pronoun": "nosotras"}, {"verb": "querer", "pronoun": "ustedes"}, {"verb": "pensar", "pronoun": "yo"}, {"verb": "pensar", "pronoun": "tú"}, {"verb": "pensar", "pronoun": "ella"}, {"verb": "pensar", "pronoun": "nosotras"}, {"verb": "pensar", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Stem e→ie querer + pensar (1/2): querer, pensar",
            "targets": [{"verb": "querer", "pronoun": "yo"}, {"verb": "querer", "pronoun": "tú"}, {"verb": "querer", "pronoun": "ella"}, {"verb": "querer", "pronoun": "nosotras"}, {"verb": "querer", "pronoun": "ustedes"}, {"verb": "pensar", "pronoun": "yo"}, {"verb": "pensar", "pronoun": "tú"}, {"verb": "pensar", "pronoun": "ella"}, {"verb": "pensar", "pronoun": "nosotras"}, {"verb": "pensar", "pronoun": "ustedes"}],
        },
        "opener_en": "What do you want?",
        "opener_es": "¿Qué quieres?",
    },


    "grammar_present_e_ie_cerrar_empezar_1": {
        "title": "Stem e→ie — cerrar + empezar (1/2)",
        "grammar_level": 7,
        "lesson_number": 3,
        "lesson_type": "conjugation",
        "word_workload": ["cerrar", "empezar"],
        "video_embed_id": "rk0AwBA9PEa",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": PRESENT_E_IE_CERRAR_EMPEZAR_INTRO,
        "drill_config": {
            "answers": {
                "cerrar": {"yo": "c|ierro", "tú": "c|ierras", "él": "c|ierra", "ella": "c|ierra", "usted": "c|ierra", "nosotros": "cerr|amos", "nosotras": "cerr|amos", "ellos": "c|ierran", "ellas": "c|ierran", "ustedes": "c|ierran"},
                "empezar": {"yo": "emp|iezo", "tú": "emp|iezas", "él": "emp|ieza", "ella": "emp|ieza", "usted": "emp|ieza", "nosotros": "empez|amos", "nosotras": "empez|amos", "ellos": "emp|iezan", "ellas": "emp|iezan", "ustedes": "emp|iezan"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": 'They (f) begin the meeting.', "es": 'Ellas empiezan la reunión.', "noun_id": None, "type": 'written', "glosses": {'meeting': 'reunión', 'reunión': 'meeting'}},
            {"en": 'You all begin the exams', "es": 'Ustedes empiezan los exámenes', "noun_id": None, "type": 'written', "glosses": {'exams': 'exámenes', 'exámenes': 'exams'}},
            {"en": 'I begin the class', "es": 'Yo empiezo la clase', "noun_id": None, "type": 'written', "glosses": {'class': 'clase', 'clase': 'class'}},
            {"en": 'She begins the meeting', "es": 'Ella empieza la reunión', "noun_id": None, "type": 'written', "glosses": {'meeting': 'reunión', 'reunión': 'meeting'}},
            {"en": 'They (f) close the schools.', "es": 'Ellas cierran las escuelas.', "noun_id": None, "type": 'written', "glosses": {'schools': 'escuelas', 'escuelas': 'schools'}},
            {"en": 'You begin the class.', "es": 'Tú empiezas la clase.', "noun_id": None, "type": 'written', "glosses": {'class': 'clase', 'clase': 'class'}},
            {"en": 'We (f) begin the project', "es": 'Nosotras empezamos el proyecto', "noun_id": None, "type": 'auditory', "glosses": {'project': 'proyecto', 'proyecto': 'project'}},
            {"en": 'You close the door.', "es": 'Tú cierras la puerta.', "noun_id": None, "type": 'written', "glosses": {'door': 'puerta', 'puerta': 'door'}},
            {"en": 'He begins the game.', "es": 'Él empieza el juego.', "noun_id": None, "type": 'written', "glosses": {'game': 'juego', 'juego': 'game'}},
            {"en": 'He closes the shop.', "es": 'Él cierra la tienda.', "noun_id": None, "type": 'written', "glosses": {'shop': 'tienda', 'tienda': 'shop'}},
            {"en": 'You close the window', "es": 'Tú cierras la ventana', "noun_id": None, "type": 'auditory', "glosses": {'window': 'ventana', 'ventana': 'window'}},
            {"en": 'We begin the lesson.', "es": 'Nosotros empezamos la lección.', "noun_id": None, "type": 'auditory', "glosses": {'lesson': 'lección', 'lección': 'lesson'}},
            {"en": 'We close the books.', "es": 'Nosotros cerramos los libros.', "noun_id": None, "type": 'auditory', "glosses": {'books': 'libros', 'libros': 'books'}},
            {"en": 'You begin the game', "es": 'Tú empiezas el juego', "noun_id": None, "type": 'auditory', "glosses": {'game': 'juego', 'juego': 'game'}},
            {"en": 'I close the window.', "es": 'Yo cierro la ventana.', "noun_id": None, "type": 'auditory', "glosses": {'window': 'ventana', 'ventana': 'window'}},
            {"en": 'I begin the project.', "es": 'Yo empiezo el proyecto.', "noun_id": None, "type": 'auditory', "glosses": {'project': 'proyecto', 'proyecto': 'project'}},
            {"en": 'I close the door', "es": 'Yo cierro la puerta', "noun_id": None, "type": 'written', "glosses": {'door': 'puerta', 'puerta': 'door'}},
            {"en": 'We (f) close the books', "es": 'Nosotras cerramos los libros', "noun_id": None, "type": 'auditory', "glosses": {'books': 'libros', 'libros': 'books'}},
            {"en": 'She closes the shop', "es": 'Ella cierra la tienda', "noun_id": None, "type": 'written', "glosses": {'shop': 'tienda', 'tienda': 'shop'}},
            {"en": 'You all close the offices', "es": 'Ustedes cierran las oficinas', "noun_id": None, "type": 'written', "glosses": {'offices': 'oficinas', 'oficinas': 'offices'}},
        ],
        "drill_targets": [{"verb": "cerrar", "pronoun": "yo"}, {"verb": "cerrar", "pronoun": "tú"}, {"verb": "cerrar", "pronoun": "ella"}, {"verb": "cerrar", "pronoun": "nosotras"}, {"verb": "cerrar", "pronoun": "ustedes"}, {"verb": "empezar", "pronoun": "yo"}, {"verb": "empezar", "pronoun": "tú"}, {"verb": "empezar", "pronoun": "ella"}, {"verb": "empezar", "pronoun": "nosotras"}, {"verb": "empezar", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Stem e→ie cerrar + empezar (1/2): cerrar, empezar",
            "targets": [{"verb": "cerrar", "pronoun": "yo"}, {"verb": "cerrar", "pronoun": "tú"}, {"verb": "cerrar", "pronoun": "ella"}, {"verb": "cerrar", "pronoun": "nosotras"}, {"verb": "cerrar", "pronoun": "ustedes"}, {"verb": "empezar", "pronoun": "yo"}, {"verb": "empezar", "pronoun": "tú"}, {"verb": "empezar", "pronoun": "ella"}, {"verb": "empezar", "pronoun": "nosotras"}, {"verb": "empezar", "pronoun": "ustedes"}],
        },
        "opener_en": "Do you close the windows?",
        "opener_es": "¿Cierras las ventanas?",
    },


    "grammar_present_e_ie_entender_preferir_1": {
        "title": "Stem e→ie — entender + preferir (1/2)",
        "grammar_level": 7,
        "lesson_number": 5,
        "lesson_type": "conjugation",
        "word_workload": ["entender", "preferir"],
        "video_embed_id": "rk0AwBA9PEa",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": PRESENT_E_IE_ENTENDER_PREFERIR_INTRO,
        "drill_config": {
            "answers": {
                "entender": {"yo": "ent|iendo", "tú": "ent|iendes", "él": "ent|iende", "ella": "ent|iende", "usted": "ent|iende", "nosotros": "entend|emos", "nosotras": "entend|emos", "ellos": "ent|ienden", "ellas": "ent|ienden", "ustedes": "ent|ienden"},
                "preferir": {"yo": "pref|iero", "tú": "pref|ieres", "él": "pref|iere", "ella": "pref|iere", "usted": "pref|iere", "nosotros": "prefer|imos", "nosotras": "prefer|imos", "ellos": "pref|ieren", "ellas": "pref|ieren", "ustedes": "pref|ieren"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": 'You all understand the rules.', "es": 'Ustedes entienden las reglas.', "noun_id": None, "type": 'written', "glosses": {'rules': 'reglas', 'reglas': 'rules'}},
            {"en": 'I prefer the red apple.', "es": 'Yo prefiero la manzana roja.', "noun_id": None, "type": 'written', "glosses": {'apple': 'manzana', 'manzana': 'apple', 'red': 'roja', 'roja': 'red'}},
            {"en": 'You understand the lesson.', "es": 'Tú entiendes la lección.', "noun_id": None, "type": 'auditory', "glosses": {'lesson': 'lección', 'lección': 'lesson'}},
            {"en": 'We (f) prefer quiet places.', "es": 'Nosotras preferimos lugares tranquilos.', "noun_id": None, "type": 'auditory', "glosses": {'places': 'lugares', 'lugares': 'places', 'quiet': 'tranquilos', 'tranquilos': 'quiet'}},
            {"en": 'You understand the question.', "es": 'Tú entiendes la pregunta.', "noun_id": None, "type": 'written', "glosses": {'question': 'pregunta', 'pregunta': 'question'}},
            {"en": 'He understands the problem.', "es": 'Él entiende el problema.', "noun_id": None, "type": 'written', "glosses": {'problem': 'problema', 'problema': 'problem'}},
            {"en": 'I understand the lesson well.', "es": 'Yo entiendo bien la lección.', "noun_id": None, "type": 'auditory', "glosses": {'lesson': 'lección', 'lección': 'lesson', 'well': 'bien', 'bien': 'well'}},
            {"en": 'I prefer cold water.', "es": 'Yo prefiero el agua fría.', "noun_id": None, "type": 'auditory', "glosses": {'water': 'agua', 'agua': 'water', 'cold': 'fría', 'fría': 'cold'}},
            {"en": 'They (f) understand the rules.', "es": 'Ellas entienden las reglas.', "noun_id": None, "type": 'written', "glosses": {'rules': 'reglas', 'reglas': 'rules'}},
            {"en": 'I understand the question.', "es": 'Yo entiendo la pregunta.', "noun_id": None, "type": 'written', "glosses": {'question': 'pregunta', 'pregunta': 'question'}},
            {"en": 'She understands the problem.', "es": 'Ella entiende el problema.', "noun_id": None, "type": 'written', "glosses": {'problem': 'problema', 'problema': 'problem'}},
            {"en": 'We understand the instructions.', "es": 'Nosotros entendemos las instrucciones.', "noun_id": None, "type": 'auditory', "glosses": {'instructions': 'instrucciones', 'instrucciones': 'instructions'}},
            {"en": 'They (f) prefer hot coffee.', "es": 'Ellas prefieren el café caliente.', "noun_id": None, "type": 'written', "glosses": {'coffee': 'café', 'café': 'coffee', 'hot': 'caliente', 'caliente': 'hot'}},
            {"en": 'He prefers the blue jacket.', "es": 'Él prefiere la chaqueta azul.', "noun_id": None, "type": 'written', "glosses": {'jacket': 'chaqueta', 'chaqueta': 'jacket', 'blue': 'azul', 'azul': 'blue'}},
            {"en": 'We (f) understand the explanation.', "es": 'Nosotras entendemos la explicación.', "noun_id": None, "type": 'auditory', "glosses": {'explanation': 'explicación', 'explicación': 'explanation'}},
            {"en": 'She prefers the blue dress.', "es": 'Ella prefiere el vestido azul.', "noun_id": None, "type": 'written', "glosses": {'dress': 'vestido', 'vestido': 'dress', 'blue': 'azul', 'azul': 'blue'}},
            {"en": 'You prefer cold water.', "es": 'Tú prefieres el agua fría.', "noun_id": None, "type": 'auditory', "glosses": {'water': 'agua', 'agua': 'water', 'cold': 'fría', 'fría': 'cold'}},
            {"en": 'You prefer the red shirt.', "es": 'Tú prefieres la camisa roja.', "noun_id": None, "type": 'written', "glosses": {'shirt': 'camisa', 'camisa': 'shirt', 'red': 'roja', 'roja': 'red'}},
            {"en": 'We prefer the big house.', "es": 'Nosotros preferimos la casa grande.', "noun_id": None, "type": 'auditory', "glosses": {'house': 'casa', 'casa': 'house', 'big': 'grande', 'grande': 'big'}},
            {"en": 'You all prefer hot coffee.', "es": 'Ustedes prefieren el café caliente.', "noun_id": None, "type": 'written', "glosses": {'coffee': 'café', 'café': 'coffee', 'hot': 'caliente', 'caliente': 'hot'}},
        ],
        "drill_targets": [{"verb": "entender", "pronoun": "yo"}, {"verb": "entender", "pronoun": "tú"}, {"verb": "entender", "pronoun": "ella"}, {"verb": "entender", "pronoun": "nosotras"}, {"verb": "entender", "pronoun": "ustedes"}, {"verb": "preferir", "pronoun": "yo"}, {"verb": "preferir", "pronoun": "tú"}, {"verb": "preferir", "pronoun": "ella"}, {"verb": "preferir", "pronoun": "nosotras"}, {"verb": "preferir", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Stem e→ie entender + preferir (1/2): entender, preferir",
            "targets": [{"verb": "entender", "pronoun": "yo"}, {"verb": "entender", "pronoun": "tú"}, {"verb": "entender", "pronoun": "ella"}, {"verb": "entender", "pronoun": "nosotras"}, {"verb": "entender", "pronoun": "ustedes"}, {"verb": "preferir", "pronoun": "yo"}, {"verb": "preferir", "pronoun": "tú"}, {"verb": "preferir", "pronoun": "ella"}, {"verb": "preferir", "pronoun": "nosotras"}, {"verb": "preferir", "pronoun": "ustedes"}],
        },
        "opener_en": "Do you understand me?",
        "opener_es": "¿Me entiendes?",
    },


    "grammar_present_e_ie_querer_pensar_chat": {
        "title": "Stem e→ie — querer + pensar Chat",
        "grammar_level": 7,
        "lesson_number": 2.5,
        "lesson_type": "conjugation",
        "word_workload": ["querer", "pensar"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Stem e→ie querer + pensar chat: querer, pensar", "targets": [{"verb": "querer", "pronoun": "yo"}, {"verb": "querer", "pronoun": "tú"}, {"verb": "querer", "pronoun": "ella"}, {"verb": "querer", "pronoun": "nosotras"}, {"verb": "querer", "pronoun": "ustedes"}, {"verb": "pensar", "pronoun": "tú"}, {"verb": "pensar", "pronoun": "yo"}, {"verb": "pensar", "pronoun": "él"}, {"verb": "pensar", "pronoun": "nosotros"}, {"verb": "pensar", "pronoun": "ellas"}]},
    },

    "grammar_present_e_ie_cerrar_empezar_chat": {
        "title": "Stem e→ie — cerrar + empezar Chat",
        "grammar_level": 7,
        "lesson_number": 4.5,
        "lesson_type": "conjugation",
        "word_workload": ["cerrar", "empezar"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Stem e→ie cerrar + empezar chat: cerrar, empezar", "targets": [{"verb": "cerrar", "pronoun": "yo"}, {"verb": "cerrar", "pronoun": "tú"}, {"verb": "cerrar", "pronoun": "ella"}, {"verb": "cerrar", "pronoun": "nosotras"}, {"verb": "cerrar", "pronoun": "ustedes"}, {"verb": "empezar", "pronoun": "tú"}, {"verb": "empezar", "pronoun": "yo"}, {"verb": "empezar", "pronoun": "él"}, {"verb": "empezar", "pronoun": "nosotros"}, {"verb": "empezar", "pronoun": "ellas"}]},
    },

    "grammar_present_e_ie_entender_preferir_chat": {
        "title": "Stem e→ie — entender + preferir Chat",
        "grammar_level": 7,
        "lesson_number": 6.5,
        "lesson_type": "conjugation",
        "word_workload": ["entender", "preferir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Stem e→ie entender + preferir chat: entender, preferir", "targets": [{"verb": "entender", "pronoun": "yo"}, {"verb": "entender", "pronoun": "tú"}, {"verb": "entender", "pronoun": "ella"}, {"verb": "entender", "pronoun": "nosotras"}, {"verb": "entender", "pronoun": "ustedes"}, {"verb": "preferir", "pronoun": "tú"}, {"verb": "preferir", "pronoun": "yo"}, {"verb": "preferir", "pronoun": "él"}, {"verb": "preferir", "pronoun": "nosotros"}, {"verb": "preferir", "pronoun": "ellas"}]},
    },

    # ── From _gl8_output.py ──

"grammar_present_e_i_pedir_servir_1": {
        "title": "Stem e→i — pedir + servir (1/2)",
        "grammar_level": 8,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ["pedir", "servir"],
        "video_embed_id": "L8M2P3RDsfx",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": PRESENT_E_I_PEDIR_SERVIR_INTRO,
        "drill_config": {
            "answers": {
                "pedir": {"yo": "p|ido", "tú": "p|ides", "él": "p|ide", "ella": "p|ide", "usted": "p|ide", "nosotros": "ped|imos", "nosotras": "ped|imos", "ellos": "p|iden", "ellas": "p|iden", "ustedes": "p|iden"},
                "servir": {"yo": "s|irvo", "tú": "s|irves", "él": "s|irve", "ella": "s|irve", "usted": "s|irve", "nosotros": "serv|imos", "nosotras": "serv|imos", "ellos": "s|irven", "ellas": "s|irven", "ustedes": "s|irven"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": 'They (f) serve the desserts.', "es": 'Ellas sirven los postres.', "noun_id": None, "type": 'written', "glosses": {'desserts': 'postres', 'postres': 'desserts'}},
            {"en": 'Do you serve the soup hot?', "es": '¿Sirves la sopa caliente?', "noun_id": None, "type": 'written', "glosses": {'soup': 'sopa', 'sopa': 'soup', 'hot': 'caliente', 'caliente': 'hot'}},
            {"en": 'You serve the soup.', "es": 'Tú sirves la sopa.', "noun_id": None, "type": 'auditory', "glosses": {'soup': 'sopa', 'sopa': 'soup'}},
            {"en": 'She serves the dessert.', "es": 'Ella sirve el postre.', "noun_id": None, "type": 'written', "glosses": {'dessert': 'postre', 'postre': 'dessert'}},
            {"en": 'He asks for the bill.', "es": 'Él pide la cuenta.', "noun_id": None, "type": 'written', "glosses": {'bill': 'cuenta', 'cuenta': 'bill'}},
            {"en": 'I serve the salad.', "es": 'Yo sirvo la ensalada.', "noun_id": None, "type": 'written', "glosses": {'salad': 'ensalada', 'ensalada': 'salad'}},
            {"en": 'You all ask for coffee.', "es": 'Ustedes piden café.', "noun_id": None, "type": 'written', "glosses": {'coffee': 'café', 'café': 'coffee'}},
            {"en": 'I ask for water.', "es": 'Yo pido agua.', "noun_id": None, "type": 'written', "glosses": {'water': 'agua', 'agua': 'water'}},
            {"en": 'You all serve the food.', "es": 'Ustedes sirven la comida.', "noun_id": None, "type": 'written', "glosses": {'food': 'comida', 'comida': 'food'}},
            {"en": 'He serves the dishes quickly.', "es": 'Él sirve los platos rápido.', "noun_id": None, "type": 'written', "glosses": {'dishes': 'platos', 'platos': 'dishes', 'quickly': 'rápido', 'rápido': 'quickly'}},
            {"en": 'We (f) serve the drinks.', "es": 'Nosotras servimos las bebidas.', "noun_id": None, "type": 'auditory', "glosses": {'drinks': 'bebidas', 'bebidas': 'drinks'}},
            {"en": 'I ask for water every day.', "es": 'Pido agua todos los días.', "noun_id": None, "type": 'auditory', "glosses": {'water': 'agua', 'agua': 'water', 'every day': 'todos los días', 'todos los días': 'every day'}},
            {"en": 'They (f) ask for the salad.', "es": 'Ellas piden la ensalada.', "noun_id": None, "type": 'written', "glosses": {'salad': 'ensalada', 'ensalada': 'salad'}},
            {"en": 'You ask for bread.', "es": 'Tú pides pan.', "noun_id": None, "type": 'auditory', "glosses": {'bread': 'pan', 'pan': 'bread'}},
            {"en": 'Do you ask for the menu?', "es": '¿Pides el menú?', "noun_id": None, "type": 'written', "glosses": {'menu': 'menú', 'menú': 'menu'}},
            {"en": 'We (f) ask for the bill.', "es": 'Nosotras pedimos la cuenta.', "noun_id": None, "type": 'auditory', "glosses": {'bill': 'cuenta', 'cuenta': 'bill'}},
            {"en": 'I serve the coffee in the morning.', "es": 'Sirvo el café por la mañana.', "noun_id": None, "type": 'auditory', "glosses": {'coffee': 'café', 'café': 'coffee', 'morning': 'mañana', 'mañana': 'morning'}},
            {"en": 'She asks for the menu.', "es": 'Ella pide el menú.', "noun_id": None, "type": 'written', "glosses": {'menu': 'menú', 'menú': 'menu'}},
            {"en": 'We (m) serve the guests now.', "es": 'Servimos a los invitados ahora.', "noun_id": None, "type": 'auditory', "glosses": {'guests': 'invitados', 'invitados': 'guests', 'now': 'ahora', 'ahora': 'now'}},
            {"en": 'We (m) ask for more bread.', "es": 'Pedimos más pan.', "noun_id": None, "type": 'auditory', "glosses": {'bread': 'pan', 'pan': 'bread', 'more': 'más', 'más': 'more'}},
        ],
        "drill_targets": [{"verb": "pedir", "pronoun": "yo"}, {"verb": "pedir", "pronoun": "tú"}, {"verb": "pedir", "pronoun": "ella"}, {"verb": "pedir", "pronoun": "nosotras"}, {"verb": "pedir", "pronoun": "ustedes"}, {"verb": "servir", "pronoun": "yo"}, {"verb": "servir", "pronoun": "tú"}, {"verb": "servir", "pronoun": "ella"}, {"verb": "servir", "pronoun": "nosotras"}, {"verb": "servir", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Stem e→i pedir + servir (1/2): pedir, servir",
            "targets": [{"verb": "pedir", "pronoun": "yo"}, {"verb": "pedir", "pronoun": "tú"}, {"verb": "pedir", "pronoun": "ella"}, {"verb": "pedir", "pronoun": "nosotras"}, {"verb": "pedir", "pronoun": "ustedes"}, {"verb": "servir", "pronoun": "yo"}, {"verb": "servir", "pronoun": "tú"}, {"verb": "servir", "pronoun": "ella"}, {"verb": "servir", "pronoun": "nosotras"}, {"verb": "servir", "pronoun": "ustedes"}],
        },
        "opener_en": "What do you order?",
        "opener_es": "¿Qué pides?",
    },


    "grammar_present_e_i_repetir_seguir_1": {
        "title": "Stem e→i — repetir + seguir (1/2)",
        "grammar_level": 8,
        "lesson_number": 3,
        "lesson_type": "conjugation",
        "word_workload": ["repetir", "seguir"],
        "video_embed_id": "L8M2P3RDsfx",
        "drill_type": "conjugation",
        "tense": "present",
        "intro_chart": PRESENT_E_I_REPETIR_SEGUIR_INTRO,
        "drill_config": {
            "answers": {
                "repetir": {"yo": "rep|ito", "tú": "rep|ites", "él": "rep|ite", "ella": "rep|ite", "usted": "rep|ite", "nosotros": "repet|imos", "nosotras": "repet|imos", "ellos": "rep|iten", "ellas": "rep|iten", "ustedes": "rep|iten"},
                "seguir": {"yo": "s|igo", "tú": "s|igues", "él": "s|igue", "ella": "s|igue", "usted": "s|igue", "nosotros": "segu|imos", "nosotras": "segu|imos", "ellos": "s|iguen", "ellas": "s|iguen", "ustedes": "s|iguen"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": 'We follow the map.', "es": 'Nosotros seguimos el mapa.', "noun_id": None, "type": 'auditory', "glosses": {'map': 'mapa', 'mapa': 'map'}},
            {"en": 'He repeats the sentence.', "es": 'Él repite la frase.', "noun_id": None, "type": 'written', "glosses": {'sentence': 'frase', 'frase': 'sentence'}},
            {"en": 'They (f) repeat the story.', "es": 'Ellas repiten la historia.', "noun_id": None, "type": 'written', "glosses": {'story': 'historia', 'historia': 'story'}},
            {"en": 'He follows the car.', "es": 'Él sigue el coche.', "noun_id": None, "type": 'written', "glosses": {'car': 'coche', 'coche': 'car'}},
            {"en": 'I follow the rules.', "es": 'Yo sigo las reglas.', "noun_id": None, "type": 'auditory', "glosses": {'rules': 'reglas', 'reglas': 'rules'}},
            {"en": 'We (f) repeat the instructions', "es": 'Nosotras repetimos las instrucciones', "noun_id": None, "type": 'auditory', "glosses": {'instructions': 'instrucciones', 'instrucciones': 'instructions'}},
            {"en": 'You repeat my words', "es": 'Tú repites mis palabras', "noun_id": None, "type": 'auditory', "glosses": {'words': 'palabras', 'palabras': 'words'}},
            {"en": 'They (f) follow the leader.', "es": 'Ellas siguen a la líder.', "noun_id": None, "type": 'written', "glosses": {'leader': 'líder', 'líder': 'leader'}},
            {"en": 'She repeats the lesson', "es": 'Ella repite la lección', "noun_id": None, "type": 'written', "glosses": {'lesson': 'lección', 'lección': 'lesson'}},
            {"en": 'You follow the path.', "es": 'Tú sigues el camino.', "noun_id": None, "type": 'written', "glosses": {'path': 'camino', 'camino': 'path'}},
            {"en": 'She follows the rules', "es": 'Ella sigue las reglas', "noun_id": None, "type": 'written', "glosses": {'rules': 'reglas', 'reglas': 'rules'}},
            {"en": 'You all repeat the song', "es": 'Ustedes repiten la canción', "noun_id": None, "type": 'written', "glosses": {'song': 'canción', 'canción': 'song'}},
            {"en": 'We (f) follow the signs', "es": 'Nosotras seguimos las señales', "noun_id": None, "type": 'auditory', "glosses": {'signs': 'señales', 'señales': 'signs'}},
            {"en": 'You follow the map', "es": 'Tú sigues el mapa', "noun_id": None, "type": 'auditory', "glosses": {'map': 'mapa', 'mapa': 'map'}},
            {"en": 'You all follow the leader', "es": 'Ustedes siguen al líder', "noun_id": None, "type": 'written', "glosses": {'leader': 'líder', 'líder': 'leader'}},
            {"en": 'I follow the path', "es": 'Yo sigo el camino', "noun_id": None, "type": 'written', "glosses": {'path': 'camino', 'camino': 'path'}},
            {"en": 'We repeat the instructions.', "es": 'Nosotros repetimos las instrucciones.', "noun_id": None, "type": 'auditory', "glosses": {'instructions': 'instrucciones', 'instrucciones': 'instructions'}},
            {"en": 'I repeat the words.', "es": 'Yo repito las palabras.', "noun_id": None, "type": 'auditory', "glosses": {'words': 'palabras', 'palabras': 'words'}},
            {"en": 'I repeat the question', "es": 'Yo repito la pregunta', "noun_id": None, "type": 'written', "glosses": {'question': 'pregunta', 'pregunta': 'question'}},
            {"en": 'You repeat the question.', "es": 'Tú repites la pregunta.', "noun_id": None, "type": 'written', "glosses": {'question': 'pregunta', 'pregunta': 'question'}},
        ],
        "drill_targets": [{"verb": "repetir", "pronoun": "yo"}, {"verb": "repetir", "pronoun": "tú"}, {"verb": "repetir", "pronoun": "ella"}, {"verb": "repetir", "pronoun": "nosotras"}, {"verb": "repetir", "pronoun": "ustedes"}, {"verb": "seguir", "pronoun": "yo"}, {"verb": "seguir", "pronoun": "tú"}, {"verb": "seguir", "pronoun": "ella"}, {"verb": "seguir", "pronoun": "nosotras"}, {"verb": "seguir", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Stem e→i repetir + seguir (1/2): repetir, seguir",
            "targets": [{"verb": "repetir", "pronoun": "yo"}, {"verb": "repetir", "pronoun": "tú"}, {"verb": "repetir", "pronoun": "ella"}, {"verb": "repetir", "pronoun": "nosotras"}, {"verb": "repetir", "pronoun": "ustedes"}, {"verb": "seguir", "pronoun": "yo"}, {"verb": "seguir", "pronoun": "tú"}, {"verb": "seguir", "pronoun": "ella"}, {"verb": "seguir", "pronoun": "nosotras"}, {"verb": "seguir", "pronoun": "ustedes"}],
        },
        "opener_en": "Can you repeat that?",
        "opener_es": "¿Puedes repetir?",
    },




    "grammar_present_e_i_pedir_servir_chat": {
        "title": "Stem e→i — pedir + servir Chat",
        "grammar_level": 8,
        "lesson_number": 2.5,
        "lesson_type": "conjugation",
        "word_workload": ["pedir", "servir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Stem e→i pedir + servir chat: pedir, servir", "targets": [{"verb": "pedir", "pronoun": "yo"}, {"verb": "pedir", "pronoun": "tú"}, {"verb": "pedir", "pronoun": "ella"}, {"verb": "pedir", "pronoun": "nosotras"}, {"verb": "pedir", "pronoun": "ustedes"}, {"verb": "servir", "pronoun": "tú"}, {"verb": "servir", "pronoun": "yo"}, {"verb": "servir", "pronoun": "él"}, {"verb": "servir", "pronoun": "nosotros"}, {"verb": "servir", "pronoun": "ellas"}]},
    },

    "grammar_present_e_i_repetir_seguir_chat": {
        "title": "Stem e→i — repetir + seguir Chat",
        "grammar_level": 8,
        "lesson_number": 4.5,
        "lesson_type": "conjugation",
        "word_workload": ["repetir", "seguir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Stem e→i repetir + seguir chat: repetir, seguir", "targets": [{"verb": "repetir", "pronoun": "yo"}, {"verb": "repetir", "pronoun": "tú"}, {"verb": "repetir", "pronoun": "ella"}, {"verb": "repetir", "pronoun": "nosotras"}, {"verb": "repetir", "pronoun": "ustedes"}, {"verb": "seguir", "pronoun": "tú"}, {"verb": "seguir", "pronoun": "yo"}, {"verb": "seguir", "pronoun": "él"}, {"verb": "seguir", "pronoun": "nosotros"}, {"verb": "seguir", "pronoun": "ellas"}]},
    },

    "grammar_present_e_i_vestir_elegir_chat": {
        "title": "Stem e→i — vestir + elegir Chat",
        "grammar_level": 8,
        "lesson_number": 6.5,
        "lesson_type": "conjugation",
        "word_workload": ["vestir", "elegir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "present",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Stem e→i vestir + elegir chat: vestir, elegir", "targets": [{"verb": "vestir", "pronoun": "yo"}, {"verb": "vestir", "pronoun": "tú"}, {"verb": "vestir", "pronoun": "ella"}, {"verb": "vestir", "pronoun": "nosotras"}, {"verb": "vestir", "pronoun": "ustedes"}, {"verb": "elegir", "pronoun": "tú"}, {"verb": "elegir", "pronoun": "yo"}, {"verb": "elegir", "pronoun": "él"}, {"verb": "elegir", "pronoun": "nosotros"}, {"verb": "elegir", "pronoun": "ellas"}]},
    },

    # ── From _gl9_output.py ──

"grammar_ir_a_inf_hablar_comer_1": {
        "title": "ir a + Infinitive — hablar + comer (1/2)",
        "grammar_level": 9,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "comer"],
        "video_embed_id": "geHPDI9tMdH",
        "drill_type": "ir_a_inf",
        "tense": "ir_a_infinitive",
        "intro_chart": {'kind': 'cards', 'title': 'ir a + Infinitive — hablar + comer', 'cards': [{'kind': 'text', 'title': 'hablar + comer', 'body': "**ir + a + infinitive** is the everyday Spanish 'going-to' future. Conjugate **ir** (voy, vas, va, vamos, van), add **a**, then any infinitive. *Voy a hablar* = I'm going to speak."}, {'kind': 'text', 'title': 'What changes, what stays', 'body': "This sub-block uses **hablar** (to speak) and **comer** (to eat) as the infinitives. The conjugated part — ir — is what you're learning to flex."}, {'kind': 'mini_table', 'title': 'hablar (to speak)', 'rows': [['yo', '|voy a hablar'], ['tú', '|vas a hablar'], ['él / ella / usted', '|va a hablar'], ['nosotros / nosotras', '|vamos a hablar'], ['ellos / ellas / ustedes', '|van a hablar']]}, {'kind': 'mini_table', 'title': 'comer (to eat)', 'rows': [['yo', '|voy a comer'], ['tú', '|vas a comer'], ['él / ella / usted', '|va a comer'], ['nosotros / nosotras', '|vamos a comer'], ['ellos / ellas / ustedes', '|van a comer']]}], 'recall': [{'verb': 'hablar', 'answers': {'yo': '|voy a hablar', 'tú': '|vas a hablar', 'él': '|va a hablar', 'nosotros': '|vamos a hablar', 'ellos': '|van a hablar'}}, {'verb': 'comer', 'answers': {'yo': '|voy a comer', 'tú': '|vas a comer', 'él': '|va a comer', 'nosotros': '|vamos a comer', 'ellos': '|van a comer'}}]},
        "drill_config": {
            "answers": {
                "hablar": {"yo": "|voy a hablar", "tú": "|vas a hablar", "él": "|va a hablar", "ella": "|va a hablar", "usted": "|va a hablar", "nosotros": "|vamos a hablar", "nosotras": "|vamos a hablar", "ellos": "|van a hablar", "ellas": "|van a hablar", "ustedes": "|van a hablar"},
                "comer": {"yo": "|voy a comer", "tú": "|vas a comer", "él": "|va a comer", "ella": "|va a comer", "usted": "|va a comer", "nosotros": "|vamos a comer", "nosotras": "|vamos a comer", "ellos": "|van a comer", "ellas": "|van a comer", "ustedes": "|van a comer"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I'm going to speak Spanish.", "es": "Voy a hablar español.", "noun_id": None, "type": "written", "glosses": {"Spanish": "español", "español": "Spanish"}},
            {"en": "Are you going to speak now?", "es": "¿Vas a hablar ahora?", "noun_id": None, "type": "auditory", "glosses": {"now": "ahora", "ahora": "now"}},
            {"en": "She is going to speak with the teacher.", "es": "Ella va a hablar con la profesora.", "noun_id": None, "type": "written", "glosses": {"teacher": "profesora", "profesora": "teacher"}},
            {"en": "We (f) are going to speak loudly.", "es": "Nosotras vamos a hablar fuerte.", "noun_id": None, "type": "auditory", "glosses": {"loudly": "fuerte", "fuerte": "loudly"}},
            {"en": "You (pl) are going to speak tomorrow.", "es": "Ustedes van a hablar mañana.", "noun_id": None, "type": "written", "glosses": {"tomorrow": "mañana", "mañana": "tomorrow"}},
            {"en": "I'm going to eat an apple.", "es": "Voy a comer una manzana.", "noun_id": None, "type": "written", "glosses": {"apple": "manzana", "manzana": "apple"}},
            {"en": "Are you going to eat breakfast?", "es": "¿Vas a comer el desayuno?", "noun_id": None, "type": "auditory", "glosses": {"breakfast": "desayuno", "desayuno": "breakfast"}},
            {"en": "She is going to eat rice.", "es": "Ella va a comer arroz.", "noun_id": None, "type": "written", "glosses": {"rice": "arroz", "arroz": "rice"}},
            {"en": "We (f) are going to eat early.", "es": "Nosotras vamos a comer temprano.", "noun_id": None, "type": "auditory", "glosses": {"early": "temprano", "temprano": "early"}},
            {"en": "You (pl) are going to eat dinner.", "es": "Ustedes van a comer la cena.", "noun_id": None, "type": "written", "glosses": {"dinner": "cena", "cena": "dinner"}},
        ],
        "drill_targets": [{"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "ella"}, {"verb": "hablar", "pronoun": "nosotras"}, {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "comer", "pronoun": "yo"}, {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "ella"}, {"verb": "comer", "pronoun": "nosotras"}, {"verb": "comer", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "ir a + Infinitive hablar + comer (1/2): hablar, comer",
            "targets": [{"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "ella"}, {"verb": "hablar", "pronoun": "nosotras"}, {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "comer", "pronoun": "yo"}, {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "ella"}, {"verb": "comer", "pronoun": "nosotras"}, {"verb": "comer", "pronoun": "ustedes"}],
        },
        "opener_en": "What are you going to say?",
        "opener_es": "¿Qué vas a decir?",
    },

    "grammar_ir_a_inf_hablar_comer_2": {
        "title": "ir a + Infinitive — hablar + comer (2/2)",
        "grammar_level": 9,
        "lesson_number": 2,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "comer"],
        "video_embed_id": "geHPDI9tMdH",
        "drill_type": "ir_a_inf",
        "tense": "ir_a_infinitive",
        "intro_chart": {'kind': 'cards', 'title': 'ir a + Infinitive — hablar + comer', 'cards': [{'kind': 'text', 'title': 'hablar + comer', 'body': "**ir + a + infinitive** is the everyday Spanish 'going-to' future. Conjugate **ir** (voy, vas, va, vamos, van), add **a**, then any infinitive. *Voy a hablar* = I'm going to speak."}, {'kind': 'text', 'title': 'What changes, what stays', 'body': "This sub-block uses **hablar** (to speak) and **comer** (to eat) as the infinitives. The conjugated part — ir — is what you're learning to flex."}, {'kind': 'mini_table', 'title': 'hablar (to speak)', 'rows': [['yo', '|voy a hablar'], ['tú', '|vas a hablar'], ['él / ella / usted', '|va a hablar'], ['nosotros / nosotras', '|vamos a hablar'], ['ellos / ellas / ustedes', '|van a hablar']]}, {'kind': 'mini_table', 'title': 'comer (to eat)', 'rows': [['yo', '|voy a comer'], ['tú', '|vas a comer'], ['él / ella / usted', '|va a comer'], ['nosotros / nosotras', '|vamos a comer'], ['ellos / ellas / ustedes', '|van a comer']]}], 'recall': [{'verb': 'hablar', 'answers': {'yo': '|voy a hablar', 'tú': '|vas a hablar', 'él': '|va a hablar', 'nosotros': '|vamos a hablar', 'ellos': '|van a hablar'}}, {'verb': 'comer', 'answers': {'yo': '|voy a comer', 'tú': '|vas a comer', 'él': '|va a comer', 'nosotros': '|vamos a comer', 'ellos': '|van a comer'}}]},
        "drill_config": {
            "answers": {
                "hablar": {"yo": "|voy a hablar", "tú": "|vas a hablar", "él": "|va a hablar", "ella": "|va a hablar", "usted": "|va a hablar", "nosotros": "|vamos a hablar", "nosotras": "|vamos a hablar", "ellos": "|van a hablar", "ellas": "|van a hablar", "ustedes": "|van a hablar"},
                "comer": {"yo": "|voy a comer", "tú": "|vas a comer", "él": "|va a comer", "ella": "|va a comer", "usted": "|va a comer", "nosotros": "|vamos a comer", "nosotras": "|vamos a comer", "ellos": "|van a comer", "ellas": "|van a comer", "ustedes": "|van a comer"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You are going to speak with the teacher.", "es": "Tú vas a hablar con el profesor.", "noun_id": None, "type": "written", "glosses": {"teacher": "profesor", "profesor": "teacher"}},
            {"en": "I am going to speak Spanish today.", "es": "Yo voy a hablar español hoy.", "noun_id": None, "type": "auditory", "glosses": {"Spanish": "español", "hoy": "today", "español": "Spanish", "today": "hoy"}},
            {"en": "He is going to speak at the meeting.", "es": "Él va a hablar en la reunión.", "noun_id": None, "type": "written", "glosses": {"meeting": "reunión", "reunión": "meeting"}},
            {"en": "We (m) are going to speak about the project.", "es": "Nosotros vamos a hablar sobre el proyecto.", "noun_id": None, "type": "auditory", "glosses": {"project": "proyecto", "proyecto": "project"}},
            {"en": "They (f) are going to speak very clearly.", "es": "Ellas van a hablar muy claro.", "noun_id": None, "type": "written", "glosses": {"clear": "claro", "claro": "clear"}},
            {"en": "You are going to eat the apples.", "es": "Tú vas a comer las manzanas.", "noun_id": None, "type": "written", "glosses": {"apples": "manzanas", "manzanas": "apples"}},
            {"en": "I am going to eat lunch now.", "es": "Yo voy a comer el almuerzo ahora.", "noun_id": None, "type": "auditory", "glosses": {"lunch": "almuerzo", "now": "ahora", "almuerzo": "lunch", "ahora": "now"}},
            {"en": "He is going to eat a big sandwich.", "es": "Él va a comer un sándwich grande.", "noun_id": None, "type": "written", "glosses": {"sandwich": "sándwich", "big": "grande", "sándwich": "sandwich", "grande": "big"}},
            {"en": "We (m) are going to eat at the restaurant.", "es": "Nosotros vamos a comer en el restaurante.", "noun_id": None, "type": "auditory", "glosses": {"restaurant": "restaurante", "restaurante": "restaurant"}},
            {"en": "They (f) are going to eat fresh fruit.", "es": "Ellas van a comer fruta fresca.", "noun_id": None, "type": "written", "glosses": {"fruit": "fruta", "fresh": "fresca", "fruta": "fruit", "fresca": "fresh"}},
        ],
        "drill_targets": [{"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "él"}, {"verb": "hablar", "pronoun": "nosotros"}, {"verb": "hablar", "pronoun": "ellas"}, {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "yo"}, {"verb": "comer", "pronoun": "él"}, {"verb": "comer", "pronoun": "nosotros"}, {"verb": "comer", "pronoun": "ellas"}],
        "phase_2_config": {
            "description": "ir a + Infinitive hablar + comer (2/2): hablar, comer",
            "targets": [{"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "él"}, {"verb": "hablar", "pronoun": "nosotros"}, {"verb": "hablar", "pronoun": "ellas"}, {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "yo"}, {"verb": "comer", "pronoun": "él"}, {"verb": "comer", "pronoun": "nosotros"}, {"verb": "comer", "pronoun": "ellas"}],
        },
        "opener_en": "What are you going to eat?",
        "opener_es": "¿Qué vas a comer?",
    },

    "grammar_ir_a_inf_vivir_escribir_1": {
        "title": "ir a + Infinitive — vivir + escribir (1/2)",
        "grammar_level": 9,
        "lesson_number": 3,
        "lesson_type": "conjugation",
        "word_workload": ["vivir", "escribir"],
        "video_embed_id": "geHPDI9tMdH",
        "drill_type": "ir_a_inf",
        "tense": "ir_a_infinitive",
        "intro_chart": {'kind': 'cards', 'title': 'ir a + Infinitive — vivir + escribir', 'cards': [{'kind': 'text', 'title': 'vivir + escribir', 'body': 'Same construction: **ir + a + infinitive**. Today we use **vivir** (to live) and **escribir** (to write) as the infinitives.'}, {'kind': 'text', 'title': 'What changes, what stays', 'body': 'Notice that the infinitive never changes — only **ir** flexes for the subject. The whole structure functions as a near-future tense.'}, {'kind': 'mini_table', 'title': 'vivir (to live)', 'rows': [['yo', '|voy a vivir'], ['tú', '|vas a vivir'], ['él / ella / usted', '|va a vivir'], ['nosotros / nosotras', '|vamos a vivir'], ['ellos / ellas / ustedes', '|van a vivir']]}, {'kind': 'mini_table', 'title': 'escribir (to write)', 'rows': [['yo', '|voy a escribir'], ['tú', '|vas a escribir'], ['él / ella / usted', '|va a escribir'], ['nosotros / nosotras', '|vamos a escribir'], ['ellos / ellas / ustedes', '|van a escribir']]}], 'recall': [{'verb': 'vivir', 'answers': {'yo': '|voy a vivir', 'tú': '|vas a vivir', 'él': '|va a vivir', 'nosotros': '|vamos a vivir', 'ellos': '|van a vivir'}}, {'verb': 'escribir', 'answers': {'yo': '|voy a escribir', 'tú': '|vas a escribir', 'él': '|va a escribir', 'nosotros': '|vamos a escribir', 'ellos': '|van a escribir'}}]},
        "drill_config": {
            "answers": {
                "vivir": {"yo": "|voy a vivir", "tú": "|vas a vivir", "él": "|va a vivir", "ella": "|va a vivir", "usted": "|va a vivir", "nosotros": "|vamos a vivir", "nosotras": "|vamos a vivir", "ellos": "|van a vivir", "ellas": "|van a vivir", "ustedes": "|van a vivir"},
                "escribir": {"yo": "|voy a escribir", "tú": "|vas a escribir", "él": "|va a escribir", "ella": "|va a escribir", "usted": "|va a escribir", "nosotros": "|vamos a escribir", "nosotras": "|vamos a escribir", "ellos": "|van a escribir", "ellas": "|van a escribir", "ustedes": "|van a escribir"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I'm going to live in Madrid.", "es": "Voy a vivir en Madrid.", "noun_id": None, "type": "written", "glosses": {"Madrid": "Madrid"}},
            {"en": "You are going to live near the beach.", "es": "Vas a vivir cerca de la playa.", "noun_id": None, "type": "auditory", "glosses": {"beach": "playa", "playa": "beach"}},
            {"en": "She is going to live in a big house.", "es": "Ella va a vivir en una casa grande.", "noun_id": None, "type": "written", "glosses": {"house": "casa", "big": "grande", "casa": "house", "grande": "big"}},
            {"en": "We (f) are going to live in the city.", "es": "Nosotras vamos a vivir en la ciudad.", "noun_id": None, "type": "auditory", "glosses": {"city": "ciudad", "ciudad": "city"}},
            {"en": "You all are going to live in new apartments.", "es": "Ustedes van a vivir en apartamentos nuevos.", "noun_id": None, "type": "written", "glosses": {"apartments": "apartamentos", "new": "nuevos", "apartamentos": "apartments", "nuevos": "new"}},
            {"en": "I'm going to write a letter.", "es": "Voy a escribir una carta.", "noun_id": None, "type": "written", "glosses": {"letter": "carta", "carta": "letter"}},
            {"en": "You are going to write a story.", "es": "Vas a escribir un cuento.", "noun_id": None, "type": "auditory", "glosses": {"story": "cuento", "cuento": "story"}},
            {"en": "She is going to write poems.", "es": "Ella va a escribir poemas.", "noun_id": None, "type": "written", "glosses": {"poems": "poemas", "poemas": "poems"}},
            {"en": "We (f) are going to write emails.", "es": "Nosotras vamos a escribir correos electrónicos.", "noun_id": None, "type": "auditory", "glosses": {"emails": "correos electrónicos", "correos electrónicos": "emails"}},
            {"en": "You all are going to write reports.", "es": "Ustedes van a escribir informes.", "noun_id": None, "type": "written", "glosses": {"reports": "informes", "informes": "reports"}},
        ],
        "drill_targets": [{"verb": "vivir", "pronoun": "yo"}, {"verb": "vivir", "pronoun": "tú"}, {"verb": "vivir", "pronoun": "ella"}, {"verb": "vivir", "pronoun": "nosotras"}, {"verb": "vivir", "pronoun": "ustedes"}, {"verb": "escribir", "pronoun": "yo"}, {"verb": "escribir", "pronoun": "tú"}, {"verb": "escribir", "pronoun": "ella"}, {"verb": "escribir", "pronoun": "nosotras"}, {"verb": "escribir", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "ir a + Infinitive vivir + escribir (1/2): vivir, escribir",
            "targets": [{"verb": "vivir", "pronoun": "yo"}, {"verb": "vivir", "pronoun": "tú"}, {"verb": "vivir", "pronoun": "ella"}, {"verb": "vivir", "pronoun": "nosotras"}, {"verb": "vivir", "pronoun": "ustedes"}, {"verb": "escribir", "pronoun": "yo"}, {"verb": "escribir", "pronoun": "tú"}, {"verb": "escribir", "pronoun": "ella"}, {"verb": "escribir", "pronoun": "nosotras"}, {"verb": "escribir", "pronoun": "ustedes"}],
        },
        "opener_en": "Where are you going to live?",
        "opener_es": "¿Dónde vas a vivir?",
    },




    "grammar_ir_a_inf_hablar_comer_chat": {
        "title": "ir a + Infinitive — hablar + comer Chat",
        "grammar_level": 9,
        "lesson_number": 2.5,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "comer"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "ir_a_infinitive",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "ir a + Infinitive hablar + comer chat: hablar, comer", "targets": [{"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "ella"}, {"verb": "hablar", "pronoun": "nosotras"}, {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "yo"}, {"verb": "comer", "pronoun": "él"}, {"verb": "comer", "pronoun": "nosotros"}, {"verb": "comer", "pronoun": "ellas"}]},
    },

    "grammar_ir_a_inf_vivir_escribir_chat": {
        "title": "ir a + Infinitive — vivir + escribir Chat",
        "grammar_level": 9,
        "lesson_number": 4.5,
        "lesson_type": "conjugation",
        "word_workload": ["vivir", "escribir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "ir_a_infinitive",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "ir a + Infinitive vivir + escribir chat: vivir, escribir", "targets": [{"verb": "vivir", "pronoun": "yo"}, {"verb": "vivir", "pronoun": "tú"}, {"verb": "vivir", "pronoun": "ella"}, {"verb": "vivir", "pronoun": "nosotras"}, {"verb": "vivir", "pronoun": "ustedes"}, {"verb": "escribir", "pronoun": "tú"}, {"verb": "escribir", "pronoun": "yo"}, {"verb": "escribir", "pronoun": "él"}, {"verb": "escribir", "pronoun": "nosotros"}, {"verb": "escribir", "pronoun": "ellas"}]},
    },

    "grammar_ir_a_inf_dormir_estudiar_chat": {
        "title": "ir a + Infinitive — dormir + estudiar Chat",
        "grammar_level": 9,
        "lesson_number": 6.5,
        "lesson_type": "conjugation",
        "word_workload": ["dormir", "estudiar"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "ir_a_infinitive",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "ir a + Infinitive dormir + estudiar chat: dormir, estudiar", "targets": [{"verb": "dormir", "pronoun": "yo"}, {"verb": "dormir", "pronoun": "tú"}, {"verb": "dormir", "pronoun": "ella"}, {"verb": "dormir", "pronoun": "nosotras"}, {"verb": "dormir", "pronoun": "ustedes"}, {"verb": "estudiar", "pronoun": "tú"}, {"verb": "estudiar", "pronoun": "yo"}, {"verb": "estudiar", "pronoun": "él"}, {"verb": "estudiar", "pronoun": "nosotros"}, {"verb": "estudiar", "pronoun": "ellas"}]},
    },

    # ── From _gl13_5_output.py ──

"grammar_imperatives_hablar_comer_1": {
        "title": "Imperatives — hablar + comer (regular tú) (1/2)",
        "grammar_level": 13.5,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "comer"],
        "video_embed_id": None,
        "drill_type": "conjugation",
        "tense": "imperative",
        "intro_chart": IMPERATIVES_HABLAR_COMER_INTRO,
        "drill_config": {
            "answers": {
                "hablar": {"tú": "habl|a", "usted": "habl|e", "nosotros": "habl|emos", "ustedes": "habl|en"},
                "comer": {"tú": "com|e", "usted": "com|a", "nosotros": "com|amos", "ustedes": "com|an"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "Speak clearly.", "es": "Habla claramente.", "noun_id": None, "type": "written", "glosses": {"clearly": "claramente", "claramente": "clearly"}},
            {"en": "Speak slowly, please.", "es": "Hable despacio, por favor.", "noun_id": None, "type": "auditory", "glosses": {"slowly": "despacio", "despacio": "slowly"}},
            {"en": "Let's speak Spanish.", "es": "Hablemos español.", "noun_id": None, "type": "written", "glosses": {"Spanish": "español", "español": "Spanish"}},
            {"en": "Speak, you all.", "es": "Hablen.", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "Speak louder.", "es": "Habla más fuerte.", "noun_id": None, "type": "written", "glosses": {"louder": "más fuerte", "más fuerte": "louder"}},
            {"en": "Eat the fruit.", "es": "Come la fruta.", "noun_id": None, "type": "written", "glosses": {"fruit": "fruta", "fruta": "fruit"}},
            {"en": "Eat slowly, please.", "es": "Coma despacio, por favor.", "noun_id": None, "type": "auditory", "glosses": {"slowly": "despacio", "despacio": "slowly"}},
            {"en": "Let's eat together.", "es": "Comamos juntos.", "noun_id": None, "type": "written", "glosses": {"together": "juntos", "juntos": "together"}},
            {"en": "Eat, you all.", "es": "Coman.", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "Eat now.", "es": "Come ahora.", "noun_id": None, "type": "written", "glosses": {"now": "ahora", "ahora": "now"}},
        ],
        "drill_targets": [{"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "usted"}, {"verb": "hablar", "pronoun": "nosotros"}, {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "hablar", "pronoun": "tú"}, {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "usted"}, {"verb": "comer", "pronoun": "nosotros"}, {"verb": "comer", "pronoun": "ustedes"}, {"verb": "comer", "pronoun": "tú"}],
        "phase_2_config": {
            "description": "Imperatives hablar + comer (regular tú) (1/2): hablar, comer",
            "targets": [{"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "usted"}, {"verb": "hablar", "pronoun": "nosotros"}, {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "hablar", "pronoun": "tú"}, {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "usted"}, {"verb": "comer", "pronoun": "nosotros"}, {"verb": "comer", "pronoun": "ustedes"}, {"verb": "comer", "pronoun": "tú"}],
        },
        "opener_en": "Speak slowly, please.",
        "opener_es": "Habla despacio, por favor.",
    },

    "grammar_imperatives_hablar_comer_2": {
        "title": "Imperatives — hablar + comer (regular tú) (2/2)",
        "grammar_level": 13.5,
        "lesson_number": 2,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "comer"],
        "video_embed_id": None,
        "drill_type": "conjugation",
        "tense": "imperative",
        "intro_chart": IMPERATIVES_HABLAR_COMER_INTRO,
        "drill_config": {
            "answers": {
                "hablar": {"tú": "habl|a", "usted": "habl|e", "nosotros": "habl|emos", "ustedes": "habl|en"},
                "comer": {"tú": "com|e", "usted": "com|a", "nosotros": "com|amos", "ustedes": "com|an"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "Speak slowly, please.", "es": "Hable despacio, por favor.", "noun_id": None, "type": "written", "glosses": {"slowly": "despacio", "despacio": "slowly"}},
            {"en": "Speak Spanish!", "es": "Habla español!", "noun_id": None, "type": "auditory", "glosses": {"Spanish": "español", "español": "Spanish"}},
            {"en": "Speak louder, you all.", "es": "Hablen más alto, ustedes.", "noun_id": None, "type": "written", "glosses": {"louder": "alto", "alto": "louder"}},
            {"en": "Let's speak about the movie.", "es": "Hablemos sobre la película.", "noun_id": None, "type": "auditory", "glosses": {"movie": "película", "película": "movie"}},
            {"en": "Speak clearly.", "es": "Hable claramente.", "noun_id": None, "type": "written", "glosses": {"clearly": "claramente", "claramente": "clearly"}},
            {"en": "Eat the fruit, please.", "es": "Coma la fruta, por favor.", "noun_id": None, "type": "written", "glosses": {"fruit": "fruta", "fruta": "fruit"}},
            {"en": "Eat now!", "es": "Come ahora!", "noun_id": None, "type": "auditory", "glosses": {"now": "ahora", "ahora": "now"}},
            {"en": "Eat all the vegetables, you all.", "es": "Coman todas las verduras, ustedes.", "noun_id": None, "type": "written", "glosses": {"vegetables": "verduras", "all": "todas", "verduras": "vegetables", "todas": "all"}},
            {"en": "Let's eat together.", "es": "Comamos juntos.", "noun_id": None, "type": "auditory", "glosses": {"together": "juntos", "juntos": "together"}},
            {"en": "Eat the bread.", "es": "Coma el pan.", "noun_id": None, "type": "written", "glosses": {"bread": "pan", "pan": "bread"}},
        ],
        "drill_targets": [{"verb": "hablar", "pronoun": "usted"}, {"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "hablar", "pronoun": "nosotros"}, {"verb": "hablar", "pronoun": "usted"}, {"verb": "comer", "pronoun": "usted"}, {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "ustedes"}, {"verb": "comer", "pronoun": "nosotros"}, {"verb": "comer", "pronoun": "usted"}],
        "phase_2_config": {
            "description": "Imperatives hablar + comer (regular tú) (2/2): hablar, comer",
            "targets": [{"verb": "hablar", "pronoun": "usted"}, {"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "hablar", "pronoun": "nosotros"}, {"verb": "hablar", "pronoun": "usted"}, {"verb": "comer", "pronoun": "usted"}, {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "ustedes"}, {"verb": "comer", "pronoun": "nosotros"}, {"verb": "comer", "pronoun": "usted"}],
        },
        "opener_en": "Eat the bread now.",
        "opener_es": "Come el pan ahora.",
    },

    "grammar_imperatives_tener_venir_1": {
        "title": "Imperatives — tener + venir (irregular tú) (1/2)",
        "grammar_level": 13.5,
        "lesson_number": 3,
        "lesson_type": "conjugation",
        "word_workload": ["tener", "venir"],
        "video_embed_id": None,
        "drill_type": "conjugation",
        "tense": "imperative",
        "intro_chart": IMPERATIVES_TENER_VENIR_INTRO,
        "drill_config": {
            "answers": {
                "tener": {"tú": "|ten", "usted": "ten|ga", "nosotros": "ten|gamos", "ustedes": "ten|gan"},
                "venir": {"tú": "|ven", "usted": "ven|ga", "nosotros": "ven|gamos", "ustedes": "ven|gan"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "Have patience.", "es": "Ten paciencia.", "noun_id": None, "type": "written", "glosses": {"patience": "paciencia", "paciencia": "patience"}},
            {"en": "Have a seat, please.", "es": "Tenga un asiento, por favor.", "noun_id": None, "type": "auditory", "glosses": {"seat": "asiento", "asiento": "seat"}},
            {"en": "Let's have fun.", "es": "Tengamos diversión.", "noun_id": None, "type": "written", "glosses": {"fun": "diversión", "diversión": "fun"}},
            {"en": "Have the tickets ready.", "es": "Tengan los boletos listos.", "noun_id": None, "type": "auditory", "glosses": {"tickets": "boletos", "boletos": "tickets"}},
            {"en": "Have courage.", "es": "Ten valor.", "noun_id": None, "type": "written", "glosses": {"courage": "valor", "valor": "courage"}},
            {"en": "Come quickly.", "es": "Ven rápido.", "noun_id": None, "type": "written", "glosses": {"quickly": "rápido", "rápido": "quickly"}},
            {"en": "Come inside, please.", "es": "Venga adentro, por favor.", "noun_id": None, "type": "auditory", "glosses": {"inside": "adentro", "adentro": "inside"}},
            {"en": "Let's come early.", "es": "Vengamos temprano.", "noun_id": None, "type": "written", "glosses": {"early": "temprano", "temprano": "early"}},
            {"en": "Come to the party.", "es": "Vengan a la fiesta.", "noun_id": None, "type": "auditory", "glosses": {"party": "fiesta", "fiesta": "party"}},
            {"en": "Come here.", "es": "Ven aquí.", "noun_id": None, "type": "written", "glosses": {"here": "aquí", "aquí": "here"}},
        ],
        "drill_targets": [{"verb": "tener", "pronoun": "tú"}, {"verb": "tener", "pronoun": "usted"}, {"verb": "tener", "pronoun": "nosotros"}, {"verb": "tener", "pronoun": "ustedes"}, {"verb": "tener", "pronoun": "tú"}, {"verb": "venir", "pronoun": "tú"}, {"verb": "venir", "pronoun": "usted"}, {"verb": "venir", "pronoun": "nosotros"}, {"verb": "venir", "pronoun": "ustedes"}, {"verb": "venir", "pronoun": "tú"}],
        "phase_2_config": {
            "description": "Imperatives tener + venir (irregular tú) (1/2): tener, venir",
            "targets": [{"verb": "tener", "pronoun": "tú"}, {"verb": "tener", "pronoun": "usted"}, {"verb": "tener", "pronoun": "nosotros"}, {"verb": "tener", "pronoun": "ustedes"}, {"verb": "tener", "pronoun": "tú"}, {"verb": "venir", "pronoun": "tú"}, {"verb": "venir", "pronoun": "usted"}, {"verb": "venir", "pronoun": "nosotros"}, {"verb": "venir", "pronoun": "ustedes"}, {"verb": "venir", "pronoun": "tú"}],
        },
        "opener_en": "Have patience, please.",
        "opener_es": "Ten paciencia, por favor.",
    },

    "grammar_imperatives_tener_venir_2": {
        "title": "Imperatives — tener + venir (irregular tú) (2/2)",
        "grammar_level": 13.5,
        "lesson_number": 4,
        "lesson_type": "conjugation",
        "word_workload": ["tener", "venir"],
        "video_embed_id": None,
        "drill_type": "conjugation",
        "tense": "imperative",
        "intro_chart": IMPERATIVES_TENER_VENIR_INTRO,
        "drill_config": {
            "answers": {
                "tener": {"tú": "|ten", "usted": "ten|ga", "nosotros": "ten|gamos", "ustedes": "ten|gan"},
                "venir": {"tú": "|ven", "usted": "ven|ga", "nosotros": "ven|gamos", "ustedes": "ven|gan"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "Have patience, please.", "es": "Tenga paciencia, por favor.", "noun_id": None, "type": "written", "glosses": {"patience": "paciencia", "paciencia": "patience"}},
            {"en": "Have a good day.", "es": "Ten un buen día.", "noun_id": None, "type": "auditory", "glosses": {"day": "día", "good": "buen", "buen": "good", "día": "day"}},
            {"en": "Have your books ready.", "es": "Tengan sus libros listos.", "noun_id": None, "type": "written", "glosses": {"books": "libros", "libros": "books", "ready": "listos", "listos": "ready"}},
            {"en": "Let's have fun today.", "es": "Tengamos diversión hoy.", "noun_id": None, "type": "auditory", "glosses": {"fun": "diversión", "diversión": "fun", "today": "hoy", "hoy": "today"}},
            {"en": "Have courage now.", "es": "Tenga valor ahora.", "noun_id": None, "type": "written", "glosses": {"courage": "valor", "valor": "courage", "now": "ahora", "ahora": "now"}},
            {"en": "Come early, please.", "es": "Venga temprano, por favor.", "noun_id": None, "type": "written", "glosses": {"early": "temprano", "temprano": "early"}},
            {"en": "Come here.", "es": "Ven aquí.", "noun_id": None, "type": "auditory", "glosses": {"here": "aquí", "aquí": "here"}},
            {"en": "Come with us, you all.", "es": "Vengan con nosotros.", "noun_id": None, "type": "written", "glosses": {"us": "nosotros", "nosotros": "us"}},
            {"en": "Let's come together.", "es": "Vengamos juntos.", "noun_id": None, "type": "auditory", "glosses": {"together": "juntos", "juntos": "together"}},
            {"en": "Come quickly, please.", "es": "Venga rápido, por favor.", "noun_id": None, "type": "written", "glosses": {"quickly": "rápido", "rápido": "quickly"}},
        ],
        "drill_targets": [{"verb": "tener", "pronoun": "usted"}, {"verb": "tener", "pronoun": "tú"}, {"verb": "tener", "pronoun": "ustedes"}, {"verb": "tener", "pronoun": "nosotros"}, {"verb": "tener", "pronoun": "usted"}, {"verb": "venir", "pronoun": "usted"}, {"verb": "venir", "pronoun": "tú"}, {"verb": "venir", "pronoun": "ustedes"}, {"verb": "venir", "pronoun": "nosotros"}, {"verb": "venir", "pronoun": "usted"}],
        "phase_2_config": {
            "description": "Imperatives tener + venir (irregular tú) (2/2): tener, venir",
            "targets": [{"verb": "tener", "pronoun": "usted"}, {"verb": "tener", "pronoun": "tú"}, {"verb": "tener", "pronoun": "ustedes"}, {"verb": "tener", "pronoun": "nosotros"}, {"verb": "tener", "pronoun": "usted"}, {"verb": "venir", "pronoun": "usted"}, {"verb": "venir", "pronoun": "tú"}, {"verb": "venir", "pronoun": "ustedes"}, {"verb": "venir", "pronoun": "nosotros"}, {"verb": "venir", "pronoun": "usted"}],
        },
        "opener_en": "Come here right now.",
        "opener_es": "Ven aquí ahora mismo.",
    },

    "grammar_imperatives_hablar_comer_chat": {
        "title": "Imperatives — hablar + comer (regular tú) Chat",
        "grammar_level": 13.5,
        "lesson_number": 2.5,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "comer"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "imperative",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Imperatives hablar + comer (regular tú) chat: hablar, comer", "targets": [{"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "usted"}, {"verb": "hablar", "pronoun": "nosotros"}, {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "hablar", "pronoun": "tú"}, {"verb": "comer", "pronoun": "usted"}, {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "ustedes"}, {"verb": "comer", "pronoun": "nosotros"}, {"verb": "comer", "pronoun": "usted"}]},
    },

    "grammar_imperatives_tener_venir_chat": {
        "title": "Imperatives — tener + venir (irregular tú) Chat",
        "grammar_level": 13.5,
        "lesson_number": 4.5,
        "lesson_type": "conjugation",
        "word_workload": ["tener", "venir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "imperative",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Imperatives tener + venir (irregular tú) chat: tener, venir", "targets": [{"verb": "tener", "pronoun": "tú"}, {"verb": "tener", "pronoun": "usted"}, {"verb": "tener", "pronoun": "nosotros"}, {"verb": "tener", "pronoun": "ustedes"}, {"verb": "tener", "pronoun": "tú"}, {"verb": "venir", "pronoun": "usted"}, {"verb": "venir", "pronoun": "tú"}, {"verb": "venir", "pronoun": "ustedes"}, {"verb": "venir", "pronoun": "nosotros"}, {"verb": "venir", "pronoun": "usted"}]},
    },

    # ── From _gl17_output.py ──

"grammar_preterite_regular_hablar_encontrar_1": {
        "title": "Preterite Regular — hablar + encontrar (-ar) (1/2)",
        "grammar_level": 17,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "encontrar"],
        "video_embed_id": "uBOH6A3vO0U",
        "drill_type": "conjugation",
        "tense": "preterite",
        "intro_chart": PRETERITE_REGULAR_HABLAR_ENCONTRAR_INTRO,
        "drill_config": {
            "answers": {
                "hablar": {"yo": "habl|é", "tú": "habl|aste", "él": "habl|ó", "ella": "habl|ó", "usted": "habl|ó", "nosotros": "habl|amos", "nosotras": "habl|amos", "ellos": "habl|aron", "ellas": "habl|aron", "ustedes": "habl|aron"},
                "encontrar": {"yo": "encontr|é", "tú": "encontr|aste", "él": "encontr|ó", "ella": "encontr|ó", "usted": "encontr|ó", "nosotros": "encontr|amos", "nosotras": "encontr|amos", "ellos": "encontr|aron", "ellas": "encontr|aron", "ustedes": "encontr|aron"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I spoke with my friend.", "es": "Yo hablé con mi amigo.", "noun_id": None, "type": "written", "glosses": {"friend": "amigo", "amigo": "friend"}},
            {"en": "You spoke clearly.", "es": "Tú hablaste claramente.", "noun_id": None, "type": "auditory", "glosses": {"clearly": "claramente", "claramente": "clearly"}},
            {"en": "She spoke Spanish yesterday.", "es": "Ella habló español ayer.", "noun_id": None, "type": "written", "glosses": {"Spanish": "español", "español": "Spanish", "yesterday": "ayer", "ayer": "yesterday"}},
            {"en": "We (f) spoke a lot.", "es": "Nosotras hablamos mucho.", "noun_id": None, "type": "auditory", "glosses": {"much": "mucho", "mucho": "much"}},
            {"en": "You all spoke in class.", "es": "Ustedes hablaron en clase.", "noun_id": None, "type": "written", "glosses": {"class": "clase", "clase": "class"}},
            {"en": "I found a book.", "es": "Yo encontré un libro.", "noun_id": None, "type": "written", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "You found the keys.", "es": "Tú encontraste las llaves.", "noun_id": None, "type": "auditory", "glosses": {"keys": "llaves", "llaves": "keys"}},
            {"en": "She found her bag.", "es": "Ella encontró su bolso.", "noun_id": None, "type": "written", "glosses": {"bag": "bolso", "bolso": "bag"}},
            {"en": "We (f) found new places.", "es": "Nosotras encontramos lugares nuevos.", "noun_id": None, "type": "auditory", "glosses": {"places": "lugares", "new": "nuevos", "lugares": "places", "nuevos": "new"}},
            {"en": "You all found the solution.", "es": "Ustedes encontraron la solución.", "noun_id": None, "type": "written", "glosses": {"solution": "solución", "solución": "solution"}},
        ],
        "drill_targets": [{"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "ella"}, {"verb": "hablar", "pronoun": "nosotras"}, {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "encontrar", "pronoun": "yo"}, {"verb": "encontrar", "pronoun": "tú"}, {"verb": "encontrar", "pronoun": "ella"}, {"verb": "encontrar", "pronoun": "nosotras"}, {"verb": "encontrar", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Preterite Regular hablar + encontrar (-ar) (1/2): hablar, encontrar",
            "targets": [{"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "ella"}, {"verb": "hablar", "pronoun": "nosotras"}, {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "encontrar", "pronoun": "yo"}, {"verb": "encontrar", "pronoun": "tú"}, {"verb": "encontrar", "pronoun": "ella"}, {"verb": "encontrar", "pronoun": "nosotras"}, {"verb": "encontrar", "pronoun": "ustedes"}],
        },
        "opener_en": "What did you say yesterday?",
        "opener_es": "¿Qué hablaste ayer?",
    },

    "grammar_preterite_regular_hablar_encontrar_2": {
        "title": "Preterite Regular — hablar + encontrar (-ar) (2/2)",
        "grammar_level": 17,
        "lesson_number": 2,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "encontrar"],
        "video_embed_id": "uBOH6A3vO0U",
        "drill_type": "conjugation",
        "tense": "preterite",
        "intro_chart": PRETERITE_REGULAR_HABLAR_ENCONTRAR_INTRO,
        "drill_config": {
            "answers": {
                "hablar": {"yo": "habl|é", "tú": "habl|aste", "él": "habl|ó", "ella": "habl|ó", "usted": "habl|ó", "nosotros": "habl|amos", "nosotras": "habl|amos", "ellos": "habl|aron", "ellas": "habl|aron", "ustedes": "habl|aron"},
                "encontrar": {"yo": "encontr|é", "tú": "encontr|aste", "él": "encontr|ó", "ella": "encontr|ó", "usted": "encontr|ó", "nosotros": "encontr|amos", "nosotras": "encontr|amos", "ellos": "encontr|aron", "ellas": "encontr|aron", "ustedes": "encontr|aron"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You spoke with the teacher.", "es": "Tú hablaste con el profesor.", "noun_id": None, "type": "written", "glosses": {"teacher": "profesor", "profesor": "teacher"}},
            {"en": "I spoke Spanish yesterday.", "es": "Yo hablé español ayer.", "noun_id": None, "type": "auditory", "glosses": {"Spanish": "español", "español": "Spanish", "yesterday": "ayer", "ayer": "yesterday"}},
            {"en": "He spoke very clearly.", "es": "Él habló muy claro.", "noun_id": None, "type": "written", "glosses": {"very": "muy", "clear": "claro", "claro": "clear", "muy": "very"}},
            {"en": "We (m) spoke at the meeting.", "es": "Nosotros hablamos en la reunión.", "noun_id": None, "type": "auditory", "glosses": {"meeting": "reunión", "reunión": "meeting"}},
            {"en": "They (f) spoke to their friends.", "es": "Ellas hablaron con sus amigas.", "noun_id": None, "type": "written", "glosses": {"friends": "amigas", "amigas": "friends"}},
            {"en": "You found the keys.", "es": "Tú encontraste las llaves.", "noun_id": None, "type": "written", "glosses": {"keys": "llaves", "llaves": "keys"}},
            {"en": "I found a new book.", "es": "Yo encontré un libro nuevo.", "noun_id": None, "type": "auditory", "glosses": {"book": "libro", "new": "nuevo", "nuevo": "new", "libro": "book"}},
            {"en": "He found the restaurant quickly.", "es": "Él encontró el restaurante rápido.", "noun_id": None, "type": "written", "glosses": {"restaurant": "restaurante", "quickly": "rápido", "rápido": "quickly", "restaurante": "restaurant"}},
            {"en": "We (m) found old photos.", "es": "Nosotros encontramos fotos viejas.", "noun_id": None, "type": "auditory", "glosses": {"photos": "fotos", "old": "viejas", "viejas": "old", "fotos": "photos"}},
            {"en": "They (f) found a beautiful park.", "es": "Ellas encontraron un parque hermoso.", "noun_id": None, "type": "written", "glosses": {"park": "parque", "beautiful": "hermoso", "hermoso": "beautiful", "parque": "park"}},
        ],
        "drill_targets": [{"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "él"}, {"verb": "hablar", "pronoun": "nosotros"}, {"verb": "hablar", "pronoun": "ellas"}, {"verb": "encontrar", "pronoun": "tú"}, {"verb": "encontrar", "pronoun": "yo"}, {"verb": "encontrar", "pronoun": "él"}, {"verb": "encontrar", "pronoun": "nosotros"}, {"verb": "encontrar", "pronoun": "ellas"}],
        "phase_2_config": {
            "description": "Preterite Regular hablar + encontrar (-ar) (2/2): hablar, encontrar",
            "targets": [{"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "él"}, {"verb": "hablar", "pronoun": "nosotros"}, {"verb": "hablar", "pronoun": "ellas"}, {"verb": "encontrar", "pronoun": "tú"}, {"verb": "encontrar", "pronoun": "yo"}, {"verb": "encontrar", "pronoun": "él"}, {"verb": "encontrar", "pronoun": "nosotros"}, {"verb": "encontrar", "pronoun": "ellas"}],
        },
        "opener_en": "Where did you find your keys?",
        "opener_es": "¿Dónde encontraste tus llaves?",
    },

    "grammar_preterite_regular_comer_beber_1": {
        "title": "Preterite Regular — comer + beber (-er) (1/2)",
        "grammar_level": 17,
        "lesson_number": 3,
        "lesson_type": "conjugation",
        "word_workload": ["comer", "beber"],
        "video_embed_id": "uBOH6A3vO0U",
        "drill_type": "conjugation",
        "tense": "preterite",
        "intro_chart": PRETERITE_REGULAR_COMER_BEBER_INTRO,
        "drill_config": {
            "answers": {
                "comer": {"yo": "com|í", "tú": "com|iste", "él": "com|ió", "ella": "com|ió", "usted": "com|ió", "nosotros": "com|imos", "nosotras": "com|imos", "ellos": "com|ieron", "ellas": "com|ieron", "ustedes": "com|ieron"},
                "beber": {"yo": "beb|í", "tú": "beb|iste", "él": "beb|ió", "ella": "beb|ió", "usted": "beb|ió", "nosotros": "beb|imos", "nosotras": "beb|imos", "ellos": "beb|ieron", "ellas": "beb|ieron", "ustedes": "beb|ieron"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I ate an apple.", "es": "Yo comí una manzana.", "noun_id": None, "type": "written", "glosses": {"apple": "manzana", "manzana": "apple"}},
            {"en": "You ate the bread.", "es": "Tú comiste el pan.", "noun_id": None, "type": "auditory", "glosses": {"bread": "pan", "pan": "bread"}},
            {"en": "She ate fresh fish.", "es": "Ella comió pescado fresco.", "noun_id": None, "type": "written", "glosses": {"fish": "pescado", "fresh": "fresco", "pescado": "fish", "fresco": "fresh"}},
            {"en": "We (f) ate delicious pasta.", "es": "Nosotras comimos pasta deliciosa.", "noun_id": None, "type": "auditory", "glosses": {"pasta": "pasta", "delicious": "deliciosa", "deliciosa": "delicious"}},
            {"en": "You all ate big sandwiches.", "es": "Ustedes comieron sándwiches grandes.", "noun_id": None, "type": "written", "glosses": {"sandwiches": "sándwiches", "big": "grandes", "sándwiches": "sandwiches", "grandes": "big"}},
            {"en": "I drank cold water.", "es": "Yo bebí agua fría.", "noun_id": None, "type": "written", "glosses": {"water": "agua", "cold": "fría", "agua": "water", "fría": "cold"}},
            {"en": "You drank orange juice.", "es": "Tú bebiste jugo de naranja.", "noun_id": None, "type": "auditory", "glosses": {"juice": "jugo", "orange": "naranja", "jugo": "juice", "naranja": "orange"}},
            {"en": "She drank hot coffee.", "es": "Ella bebió café caliente.", "noun_id": None, "type": "written", "glosses": {"coffee": "café", "hot": "caliente", "café": "coffee", "caliente": "hot"}},
            {"en": "We (f) drank fresh milk.", "es": "Nosotras bebimos leche fresca.", "noun_id": None, "type": "auditory", "glosses": {"milk": "leche", "fresh": "fresca", "leche": "milk", "fresca": "fresh"}},
            {"en": "You all drank cold tea.", "es": "Ustedes bebieron té frío.", "noun_id": None, "type": "written", "glosses": {"tea": "té", "cold": "frío", "té": "tea", "frío": "cold"}},
        ],
        "drill_targets": [{"verb": "comer", "pronoun": "yo"}, {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "ella"}, {"verb": "comer", "pronoun": "nosotras"}, {"verb": "comer", "pronoun": "ustedes"}, {"verb": "beber", "pronoun": "yo"}, {"verb": "beber", "pronoun": "tú"}, {"verb": "beber", "pronoun": "ella"}, {"verb": "beber", "pronoun": "nosotras"}, {"verb": "beber", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Preterite Regular comer + beber (-er) (1/2): comer, beber",
            "targets": [{"verb": "comer", "pronoun": "yo"}, {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "ella"}, {"verb": "comer", "pronoun": "nosotras"}, {"verb": "comer", "pronoun": "ustedes"}, {"verb": "beber", "pronoun": "yo"}, {"verb": "beber", "pronoun": "tú"}, {"verb": "beber", "pronoun": "ella"}, {"verb": "beber", "pronoun": "nosotras"}, {"verb": "beber", "pronoun": "ustedes"}],
        },
        "opener_en": "What did you eat for lunch?",
        "opener_es": "¿Qué comiste para el almuerzo?",
    },

    "grammar_preterite_regular_comer_beber_2": {
        "title": "Preterite Regular — comer + beber (-er) (2/2)",
        "grammar_level": 17,
        "lesson_number": 4,
        "lesson_type": "conjugation",
        "word_workload": ["comer", "beber"],
        "video_embed_id": "uBOH6A3vO0U",
        "drill_type": "conjugation",
        "tense": "preterite",
        "intro_chart": PRETERITE_REGULAR_COMER_BEBER_INTRO,
        "drill_config": {
            "answers": {
                "comer": {"yo": "com|í", "tú": "com|iste", "él": "com|ió", "ella": "com|ió", "usted": "com|ió", "nosotros": "com|imos", "nosotras": "com|imos", "ellos": "com|ieron", "ellas": "com|ieron", "ustedes": "com|ieron"},
                "beber": {"yo": "beb|í", "tú": "beb|iste", "él": "beb|ió", "ella": "beb|ió", "usted": "beb|ió", "nosotros": "beb|imos", "nosotras": "beb|imos", "ellos": "beb|ieron", "ellas": "beb|ieron", "ustedes": "beb|ieron"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You ate the red apple.", "es": "Tú comiste la manzana roja.", "noun_id": None, "type": "written", "glosses": {"apple": "manzana", "red": "roja", "manzana": "apple", "roja": "red"}},
            {"en": "I ate fresh bread.", "es": "Yo comí pan fresco.", "noun_id": None, "type": "auditory", "glosses": {"bread": "pan", "fresh": "fresco", "pan": "bread", "fresco": "fresh"}},
            {"en": "He ate the big fish.", "es": "Él comió el pez grande.", "noun_id": None, "type": "written", "glosses": {"fish": "pez", "big": "grande", "pez": "fish", "grande": "big"}},
            {"en": "We (m) ate delicious meals.", "es": "Nosotros comimos comidas deliciosas.", "noun_id": None, "type": "auditory", "glosses": {"meal": "comidas", "delicious": "deliciosas", "comidas": "meal", "deliciosas": "delicious"}},
            {"en": "They (f) ate sweet fruits.", "es": "Ellas comieron frutas dulces.", "noun_id": None, "type": "written", "glosses": {"fruit": "frutas", "sweet": "dulces", "frutas": "fruit", "dulces": "sweet"}},
            {"en": "You drank cold water.", "es": "Tú bebiste agua fría.", "noun_id": None, "type": "written", "glosses": {"water": "agua", "cold": "fría", "agua": "water", "fría": "cold"}},
            {"en": "I drank hot coffee.", "es": "Yo bebí café caliente.", "noun_id": None, "type": "auditory", "glosses": {"coffee": "café", "hot": "caliente", "café": "coffee", "caliente": "hot"}},
            {"en": "He drank fresh juice.", "es": "Él bebió jugo fresco.", "noun_id": None, "type": "written", "glosses": {"juice": "jugo", "fresh": "fresco", "jugo": "juice", "fresco": "fresh"}},
            {"en": "We (m) drank sweet milk.", "es": "Nosotros bebimos leche dulce.", "noun_id": None, "type": "auditory", "glosses": {"milk": "leche", "sweet": "dulce", "leche": "milk", "dulce": "sweet"}},
            {"en": "They (f) drank cold tea.", "es": "Ellas bebieron té frío.", "noun_id": None, "type": "written", "glosses": {"tea": "té", "cold": "frío", "té": "tea", "frío": "cold"}},
        ],
        "drill_targets": [{"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "yo"}, {"verb": "comer", "pronoun": "él"}, {"verb": "comer", "pronoun": "nosotros"}, {"verb": "comer", "pronoun": "ellas"}, {"verb": "beber", "pronoun": "tú"}, {"verb": "beber", "pronoun": "yo"}, {"verb": "beber", "pronoun": "él"}, {"verb": "beber", "pronoun": "nosotros"}, {"verb": "beber", "pronoun": "ellas"}],
        "phase_2_config": {
            "description": "Preterite Regular comer + beber (-er) (2/2): comer, beber",
            "targets": [{"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "yo"}, {"verb": "comer", "pronoun": "él"}, {"verb": "comer", "pronoun": "nosotros"}, {"verb": "comer", "pronoun": "ellas"}, {"verb": "beber", "pronoun": "tú"}, {"verb": "beber", "pronoun": "yo"}, {"verb": "beber", "pronoun": "él"}, {"verb": "beber", "pronoun": "nosotros"}, {"verb": "beber", "pronoun": "ellas"}],
        },
        "opener_en": "What did you drink at the party?",
        "opener_es": "¿Qué bebiste en la fiesta?",
    },

    "grammar_preterite_regular_salir_unir_1": {
        "title": "Preterite Regular — salir + unir (-ir) (1/2)",
        "grammar_level": 17,
        "lesson_number": 5,
        "lesson_type": "conjugation",
        "word_workload": ["salir", "unir"],
        "video_embed_id": "uBOH6A3vO0U",
        "drill_type": "conjugation",
        "tense": "preterite",
        "intro_chart": PRETERITE_REGULAR_SALIR_UNIR_INTRO,
        "drill_config": {
            "answers": {
                "salir": {"yo": "sal|í", "tú": "sal|iste", "él": "sal|ió", "ella": "sal|ió", "usted": "sal|ió", "nosotros": "sal|imos", "nosotras": "sal|imos", "ellos": "sal|ieron", "ellas": "sal|ieron", "ustedes": "sal|ieron"},
                "unir": {"yo": "un|í", "tú": "un|iste", "él": "un|ió", "ella": "un|ió", "usted": "un|ió", "nosotros": "un|imos", "nosotras": "un|imos", "ellos": "un|ieron", "ellas": "un|ieron", "ustedes": "un|ieron"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I left the house early.", "es": "Yo salí de la casa temprano.", "noun_id": None, "type": "written", "glosses": {"house": "casa", "early": "temprano", "casa": "house", "temprano": "early"}},
            {"en": "You left with your friends.", "es": "Tú saliste con tus amigos.", "noun_id": None, "type": "auditory", "glosses": {"friends": "amigos", "amigos": "friends"}},
            {"en": "She left the party at midnight.", "es": "Ella salió de la fiesta a medianoche.", "noun_id": None, "type": "written", "glosses": {"party": "fiesta", "midnight": "medianoche", "fiesta": "party", "medianoche": "midnight"}},
            {"en": "We (f) left the school quickly.", "es": "Nosotras salimos de la escuela rápido.", "noun_id": None, "type": "auditory", "glosses": {"school": "escuela", "quickly": "rápido", "escuela": "school", "rápido": "quickly"}},
            {"en": "You all left the restaurant late.", "es": "Ustedes salieron del restaurante tarde.", "noun_id": None, "type": "written", "glosses": {"restaurant": "restaurante", "late": "tarde", "restaurante": "restaurant", "tarde": "late"}},
            {"en": "I joined the team yesterday.", "es": "Yo uní al equipo ayer.", "noun_id": None, "type": "written", "glosses": {"team": "equipo", "yesterday": "ayer", "equipo": "team", "ayer": "yesterday"}},
            {"en": "You joined the group quickly.", "es": "Tú uniste al grupo rápido.", "noun_id": None, "type": "auditory", "glosses": {"group": "grupo", "quickly": "rápido", "grupo": "group", "rápido": "quickly"}},
            {"en": "She joined the club last week.", "es": "Ella unió al club la semana pasada.", "noun_id": None, "type": "written", "glosses": {"club": "club", "week": "semana", "last": "pasada", "semana": "week", "pasada": "last"}},
            {"en": "We (f) joined the classes early.", "es": "Nosotras unimos a las clases temprano.", "noun_id": None, "type": "auditory", "glosses": {"classes": "clases", "early": "temprano", "clases": "classes", "temprano": "early"}},
            {"en": "You all joined the meeting yesterday.", "es": "Ustedes unieron a la reunión ayer.", "noun_id": None, "type": "written", "glosses": {"meeting": "reunión", "yesterday": "ayer", "reunión": "meeting", "ayer": "yesterday"}},
        ],
        "drill_targets": [{"verb": "salir", "pronoun": "yo"}, {"verb": "salir", "pronoun": "tú"}, {"verb": "salir", "pronoun": "ella"}, {"verb": "salir", "pronoun": "nosotras"}, {"verb": "salir", "pronoun": "ustedes"}, {"verb": "unir", "pronoun": "yo"}, {"verb": "unir", "pronoun": "tú"}, {"verb": "unir", "pronoun": "ella"}, {"verb": "unir", "pronoun": "nosotras"}, {"verb": "unir", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Preterite Regular salir + unir (-ir) (1/2): salir, unir",
            "targets": [{"verb": "salir", "pronoun": "yo"}, {"verb": "salir", "pronoun": "tú"}, {"verb": "salir", "pronoun": "ella"}, {"verb": "salir", "pronoun": "nosotras"}, {"verb": "salir", "pronoun": "ustedes"}, {"verb": "unir", "pronoun": "yo"}, {"verb": "unir", "pronoun": "tú"}, {"verb": "unir", "pronoun": "ella"}, {"verb": "unir", "pronoun": "nosotras"}, {"verb": "unir", "pronoun": "ustedes"}],
        },
        "opener_en": "What time did you leave?",
        "opener_es": "¿A qué hora saliste?",
    },

    "grammar_preterite_regular_salir_unir_2": {
        "title": "Preterite Regular — salir + unir (-ir) (2/2)",
        "grammar_level": 17,
        "lesson_number": 6,
        "lesson_type": "conjugation",
        "word_workload": ["salir", "unir"],
        "video_embed_id": "uBOH6A3vO0U",
        "drill_type": "conjugation",
        "tense": "preterite",
        "intro_chart": PRETERITE_REGULAR_SALIR_UNIR_INTRO,
        "drill_config": {
            "answers": {
                "salir": {"yo": "sal|í", "tú": "sal|iste", "él": "sal|ió", "ella": "sal|ió", "usted": "sal|ió", "nosotros": "sal|imos", "nosotras": "sal|imos", "ellos": "sal|ieron", "ellas": "sal|ieron", "ustedes": "sal|ieron"},
                "unir": {"yo": "un|í", "tú": "un|iste", "él": "un|ió", "ella": "un|ió", "usted": "un|ió", "nosotros": "un|imos", "nosotras": "un|imos", "ellos": "un|ieron", "ellas": "un|ieron", "ustedes": "un|ieron"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You left the house early.", "es": "Tú saliste de la casa temprano.", "noun_id": None, "type": "written", "glosses": {"house": "casa", "early": "temprano", "casa": "house", "temprano": "early"}},
            {"en": "I left the party at midnight.", "es": "Yo salí de la fiesta a medianoche.", "noun_id": None, "type": "auditory", "glosses": {"party": "fiesta", "midnight": "medianoche", "fiesta": "party", "medianoche": "midnight"}},
            {"en": "He left the restaurant quickly.", "es": "Él salió del restaurante rápidamente.", "noun_id": None, "type": "written", "glosses": {"restaurant": "restaurante", "quickly": "rápidamente", "restaurante": "restaurant", "rápidamente": "quickly"}},
            {"en": "We left the park together.", "es": "Nosotros salimos del parque juntos.", "noun_id": None, "type": "auditory", "glosses": {"park": "parque", "together": "juntos", "parque": "park", "juntos": "together"}},
            {"en": "They (f) left the school late.", "es": "Ellas salieron de la escuela tarde.", "noun_id": None, "type": "written", "glosses": {"school": "escuela", "late": "tarde", "escuela": "school", "tarde": "late"}},
            {"en": "You joined the group yesterday.", "es": "Tú uniste al grupo ayer.", "noun_id": None, "type": "written", "glosses": {"group": "grupo", "yesterday": "ayer", "grupo": "group", "ayer": "yesterday"}},
            {"en": "I joined the team last week.", "es": "Yo uní al equipo la semana pasada.", "noun_id": None, "type": "auditory", "glosses": {"team": "equipo", "week": "semana", "last": "pasada", "equipo": "team", "semana": "week", "pasada": "last"}},
            {"en": "He joined the class early.", "es": "Él unió la clase temprano.", "noun_id": None, "type": "written", "glosses": {"class": "clase", "early": "temprano", "clase": "class", "temprano": "early"}},
            {"en": "We joined the clubs quickly.", "es": "Nosotros unimos los clubes rápidamente.", "noun_id": None, "type": "auditory", "glosses": {"clubs": "clubes", "quickly": "rápidamente", "clubes": "clubs", "rápidamente": "quickly"}},
            {"en": "They (f) joined the teams yesterday.", "es": "Ellas unieron los equipos ayer.", "noun_id": None, "type": "written", "glosses": {"teams": "equipos", "yesterday": "ayer", "equipos": "teams", "ayer": "yesterday"}},
        ],
        "drill_targets": [{"verb": "salir", "pronoun": "tú"}, {"verb": "salir", "pronoun": "yo"}, {"verb": "salir", "pronoun": "él"}, {"verb": "salir", "pronoun": "nosotros"}, {"verb": "salir", "pronoun": "ellas"}, {"verb": "unir", "pronoun": "tú"}, {"verb": "unir", "pronoun": "yo"}, {"verb": "unir", "pronoun": "él"}, {"verb": "unir", "pronoun": "nosotros"}, {"verb": "unir", "pronoun": "ellas"}],
        "phase_2_config": {
            "description": "Preterite Regular salir + unir (-ir) (2/2): salir, unir",
            "targets": [{"verb": "salir", "pronoun": "tú"}, {"verb": "salir", "pronoun": "yo"}, {"verb": "salir", "pronoun": "él"}, {"verb": "salir", "pronoun": "nosotros"}, {"verb": "salir", "pronoun": "ellas"}, {"verb": "unir", "pronoun": "tú"}, {"verb": "unir", "pronoun": "yo"}, {"verb": "unir", "pronoun": "él"}, {"verb": "unir", "pronoun": "nosotros"}, {"verb": "unir", "pronoun": "ellas"}],
        },
        "opener_en": "Did the team unite?",
        "opener_es": "¿Se unió el equipo?",
    },

    "grammar_preterite_regular_hablar_encontrar_chat": {
        "title": "Preterite Regular — hablar + encontrar (-ar) Chat",
        "grammar_level": 17,
        "lesson_number": 2.5,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "encontrar"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "preterite",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Preterite Regular hablar + encontrar (-ar) chat: hablar, encontrar", "targets": [{"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "ella"}, {"verb": "hablar", "pronoun": "nosotras"}, {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "encontrar", "pronoun": "tú"}, {"verb": "encontrar", "pronoun": "yo"}, {"verb": "encontrar", "pronoun": "él"}, {"verb": "encontrar", "pronoun": "nosotros"}, {"verb": "encontrar", "pronoun": "ellas"}]},
    },

    "grammar_preterite_regular_comer_beber_chat": {
        "title": "Preterite Regular — comer + beber (-er) Chat",
        "grammar_level": 17,
        "lesson_number": 4.5,
        "lesson_type": "conjugation",
        "word_workload": ["comer", "beber"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "preterite",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Preterite Regular comer + beber (-er) chat: comer, beber", "targets": [{"verb": "comer", "pronoun": "yo"}, {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "ella"}, {"verb": "comer", "pronoun": "nosotras"}, {"verb": "comer", "pronoun": "ustedes"}, {"verb": "beber", "pronoun": "tú"}, {"verb": "beber", "pronoun": "yo"}, {"verb": "beber", "pronoun": "él"}, {"verb": "beber", "pronoun": "nosotros"}, {"verb": "beber", "pronoun": "ellas"}]},
    },

    "grammar_preterite_regular_salir_unir_chat": {
        "title": "Preterite Regular — salir + unir (-ir) Chat",
        "grammar_level": 17,
        "lesson_number": 6.5,
        "lesson_type": "conjugation",
        "word_workload": ["salir", "unir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "preterite",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Preterite Regular salir + unir (-ir) chat: salir, unir", "targets": [{"verb": "salir", "pronoun": "yo"}, {"verb": "salir", "pronoun": "tú"}, {"verb": "salir", "pronoun": "ella"}, {"verb": "salir", "pronoun": "nosotras"}, {"verb": "salir", "pronoun": "ustedes"}, {"verb": "unir", "pronoun": "tú"}, {"verb": "unir", "pronoun": "yo"}, {"verb": "unir", "pronoun": "él"}, {"verb": "unir", "pronoun": "nosotros"}, {"verb": "unir", "pronoun": "ellas"}]},
    },

    # ── From _gl17_1_output.py ──

"grammar_preterite_irregular_ser_ir_1": {
        "title": "Preterite Highly Irregular — ser + ir (identical) (1/2)",
        "grammar_level": 17.1,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ["ser", "ir"],
        "video_embed_id": "Ib68zJ3q7i8",
        "drill_type": "conjugation",
        "tense": "preterite",
        "intro_chart": PRETERITE_IRREGULAR_SER_IR_INTRO,
        "drill_config": {
            "answers": {
                "ser": {"yo": "|fui", "tú": "|fuiste", "él": "|fue", "ella": "|fue", "usted": "|fue", "nosotros": "|fuimos", "nosotras": "|fuimos", "ellos": "|fueron", "ellas": "|fueron", "ustedes": "|fueron"},
                "ir": {"yo": "|fui", "tú": "|fuiste", "él": "|fue", "ella": "|fue", "usted": "|fue", "nosotros": "|fuimos", "nosotras": "|fuimos", "ellos": "|fueron", "ellas": "|fueron", "ustedes": "|fueron"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I was a teacher.", "es": "Yo fui profesor.", "noun_id": None, "type": "written", "glosses": {"teacher": "profesor", "profesor": "teacher"}},
            {"en": "You were very kind.", "es": "Tú fuiste muy amable.", "noun_id": None, "type": "auditory", "glosses": {"kind": "amable", "amable": "kind"}},
            {"en": "She was happy yesterday.", "es": "Ella fue feliz ayer.", "noun_id": None, "type": "written", "glosses": {"happy": "feliz", "feliz": "happy", "yesterday": "ayer", "ayer": "yesterday"}},
            {"en": "We (f) were at the park.", "es": "Nosotras fuimos en el parque.", "noun_id": None, "type": "auditory", "glosses": {"park": "parque", "parque": "park"}},
            {"en": "You all were friends.", "es": "Ustedes fueron amigos.", "noun_id": None, "type": "written", "glosses": {"friends": "amigos", "amigos": "friends"}},
            {"en": "I went to the market.", "es": "Yo fui al mercado.", "noun_id": None, "type": "written", "glosses": {"market": "mercado", "mercado": "market"}},
            {"en": "You went to the cinema.", "es": "Tú fuiste al cine.", "noun_id": None, "type": "auditory", "glosses": {"cinema": "cine", "cine": "cinema"}},
            {"en": "She went to the library.", "es": "Ella fue a la biblioteca.", "noun_id": None, "type": "written", "glosses": {"library": "biblioteca", "biblioteca": "library"}},
            {"en": "We (f) went to the beach.", "es": "Nosotras fuimos a la playa.", "noun_id": None, "type": "auditory", "glosses": {"beach": "playa", "playa": "beach"}},
            {"en": "You all went to the museum.", "es": "Ustedes fueron al museo.", "noun_id": None, "type": "written", "glosses": {"museum": "museo", "museo": "museum"}},
        ],
        "drill_targets": [{"verb": "ser", "pronoun": "yo"}, {"verb": "ser", "pronoun": "tú"}, {"verb": "ser", "pronoun": "ella"}, {"verb": "ser", "pronoun": "nosotras"}, {"verb": "ser", "pronoun": "ustedes"}, {"verb": "ir", "pronoun": "yo"}, {"verb": "ir", "pronoun": "tú"}, {"verb": "ir", "pronoun": "ella"}, {"verb": "ir", "pronoun": "nosotras"}, {"verb": "ir", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Preterite Highly Irregular ser + ir (identical) (1/2): ser, ir",
            "targets": [{"verb": "ser", "pronoun": "yo"}, {"verb": "ser", "pronoun": "tú"}, {"verb": "ser", "pronoun": "ella"}, {"verb": "ser", "pronoun": "nosotras"}, {"verb": "ser", "pronoun": "ustedes"}, {"verb": "ir", "pronoun": "yo"}, {"verb": "ir", "pronoun": "tú"}, {"verb": "ir", "pronoun": "ella"}, {"verb": "ir", "pronoun": "nosotras"}, {"verb": "ir", "pronoun": "ustedes"}],
        },
        "opener_en": "Where did you go yesterday?",
        "opener_es": "¿Adónde fuiste ayer?",
    },

    "grammar_preterite_irregular_ser_ir_2": {
        "title": "Preterite Highly Irregular — ser + ir (identical) (2/2)",
        "grammar_level": 17.1,
        "lesson_number": 2,
        "lesson_type": "conjugation",
        "word_workload": ["ser", "ir"],
        "video_embed_id": "Ib68zJ3q7i8",
        "drill_type": "conjugation",
        "tense": "preterite",
        "intro_chart": PRETERITE_IRREGULAR_SER_IR_INTRO,
        "drill_config": {
            "answers": {
                "ser": {"yo": "|fui", "tú": "|fuiste", "él": "|fue", "ella": "|fue", "usted": "|fue", "nosotros": "|fuimos", "nosotras": "|fuimos", "ellos": "|fueron", "ellas": "|fueron", "ustedes": "|fueron"},
                "ir": {"yo": "|fui", "tú": "|fuiste", "él": "|fue", "ella": "|fue", "usted": "|fue", "nosotros": "|fuimos", "nosotras": "|fuimos", "ellos": "|fueron", "ellas": "|fueron", "ustedes": "|fueron"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You were the teacher.", "es": "Tú fuiste el profesor.", "noun_id": None, "type": "written", "glosses": {"teacher": "profesor", "profesor": "teacher"}},
            {"en": "I was happy yesterday.", "es": "Yo fui feliz ayer.", "noun_id": None, "type": "auditory", "glosses": {"happy": "feliz", "feliz": "happy", "yesterday": "ayer", "ayer": "yesterday"}},
            {"en": "He was very tall.", "es": "Él fue muy alto.", "noun_id": None, "type": "written", "glosses": {"tall": "alto", "alto": "tall", "very": "muy", "muy": "very"}},
            {"en": "We were at the park.", "es": "Nosotros fuimos en el parque.", "noun_id": None, "type": "auditory", "glosses": {"park": "parque", "parque": "park"}},
            {"en": "They (f) were friends.", "es": "Ellas fueron amigas.", "noun_id": None, "type": "written", "glosses": {"friends": "amigas", "amigas": "friends"}},
            {"en": "You went to the market.", "es": "Tú fuiste al mercado.", "noun_id": None, "type": "written", "glosses": {"market": "mercado", "mercado": "market"}},
            {"en": "I went to the beach.", "es": "Yo fui a la playa.", "noun_id": None, "type": "auditory", "glosses": {"beach": "playa", "playa": "beach"}},
            {"en": "He went home early.", "es": "Él fue a casa temprano.", "noun_id": None, "type": "written", "glosses": {"home": "casa", "casa": "home", "early": "temprano", "temprano": "early"}},
            {"en": "We went by car.", "es": "Nosotros fuimos en coche.", "noun_id": None, "type": "auditory", "glosses": {"car": "coche", "coche": "car"}},
            {"en": "They (f) went to school.", "es": "Ellas fueron a la escuela.", "noun_id": None, "type": "written", "glosses": {"school": "escuela", "escuela": "school"}},
        ],
        "drill_targets": [{"verb": "ser", "pronoun": "tú"}, {"verb": "ser", "pronoun": "yo"}, {"verb": "ser", "pronoun": "él"}, {"verb": "ser", "pronoun": "nosotros"}, {"verb": "ser", "pronoun": "ellas"}, {"verb": "ir", "pronoun": "tú"}, {"verb": "ir", "pronoun": "yo"}, {"verb": "ir", "pronoun": "él"}, {"verb": "ir", "pronoun": "nosotros"}, {"verb": "ir", "pronoun": "ellas"}],
        "phase_2_config": {
            "description": "Preterite Highly Irregular ser + ir (identical) (2/2): ser, ir",
            "targets": [{"verb": "ser", "pronoun": "tú"}, {"verb": "ser", "pronoun": "yo"}, {"verb": "ser", "pronoun": "él"}, {"verb": "ser", "pronoun": "nosotros"}, {"verb": "ser", "pronoun": "ellas"}, {"verb": "ir", "pronoun": "tú"}, {"verb": "ir", "pronoun": "yo"}, {"verb": "ir", "pronoun": "él"}, {"verb": "ir", "pronoun": "nosotros"}, {"verb": "ir", "pronoun": "ellas"}],
        },
        "opener_en": "Were you a student?",
        "opener_es": "¿Fuiste estudiante?",
    },

    "grammar_preterite_irregular_dar_ver_1": {
        "title": "Preterite Highly Irregular — dar + ver (1/2)",
        "grammar_level": 17.1,
        "lesson_number": 3,
        "lesson_type": "conjugation",
        "word_workload": ["dar", "ver"],
        "video_embed_id": "Ib68zJ3q7i8",
        "drill_type": "conjugation",
        "tense": "preterite",
        "intro_chart": PRETERITE_IRREGULAR_DAR_VER_INTRO,
        "drill_config": {
            "answers": {
                "dar": {"yo": "d|i", "tú": "d|iste", "él": "d|io", "ella": "d|io", "usted": "d|io", "nosotros": "d|imos", "nosotras": "d|imos", "ellos": "d|ieron", "ellas": "d|ieron", "ustedes": "d|ieron"},
                "ver": {"yo": "v|i", "tú": "v|iste", "él": "v|io", "ella": "v|io", "usted": "v|io", "nosotros": "v|imos", "nosotras": "v|imos", "ellos": "v|ieron", "ellas": "v|ieron", "ustedes": "v|ieron"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I gave the book.", "es": "Yo di el libro.", "noun_id": None, "type": "written", "glosses": {"book": "libro", "libro": "book"}},
            {"en": "You gave the keys.", "es": "Tú diste las llaves.", "noun_id": None, "type": "auditory", "glosses": {"keys": "llaves", "llaves": "keys"}},
            {"en": "She gave a gift.", "es": "Ella dio un regalo.", "noun_id": None, "type": "written", "glosses": {"gift": "regalo", "regalo": "gift"}},
            {"en": "We (f) gave flowers.", "es": "Nosotras dimos flores.", "noun_id": None, "type": "auditory", "glosses": {"flowers": "flores", "flores": "flowers"}},
            {"en": "You all gave money.", "es": "Ustedes dieron dinero.", "noun_id": None, "type": "written", "glosses": {"money": "dinero", "dinero": "money"}},
            {"en": "I saw the movie.", "es": "Yo vi la película.", "noun_id": None, "type": "written", "glosses": {"movie": "película", "película": "movie"}},
            {"en": "You saw the house.", "es": "Tú viste la casa.", "noun_id": None, "type": "auditory", "glosses": {"house": "casa", "casa": "house"}},
            {"en": "She saw the stars.", "es": "Ella vio las estrellas.", "noun_id": None, "type": "written", "glosses": {"stars": "estrellas", "estrellas": "stars"}},
            {"en": "We (f) saw the birds.", "es": "Nosotras vimos los pájaros.", "noun_id": None, "type": "auditory", "glosses": {"birds": "pájaros", "pájaros": "birds"}},
            {"en": "You all saw the city.", "es": "Ustedes vieron la ciudad.", "noun_id": None, "type": "written", "glosses": {"city": "ciudad", "ciudad": "city"}},
        ],
        "drill_targets": [{"verb": "dar", "pronoun": "yo"}, {"verb": "dar", "pronoun": "tú"}, {"verb": "dar", "pronoun": "ella"}, {"verb": "dar", "pronoun": "nosotras"}, {"verb": "dar", "pronoun": "ustedes"}, {"verb": "ver", "pronoun": "yo"}, {"verb": "ver", "pronoun": "tú"}, {"verb": "ver", "pronoun": "ella"}, {"verb": "ver", "pronoun": "nosotras"}, {"verb": "ver", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Preterite Highly Irregular dar + ver (1/2): dar, ver",
            "targets": [{"verb": "dar", "pronoun": "yo"}, {"verb": "dar", "pronoun": "tú"}, {"verb": "dar", "pronoun": "ella"}, {"verb": "dar", "pronoun": "nosotras"}, {"verb": "dar", "pronoun": "ustedes"}, {"verb": "ver", "pronoun": "yo"}, {"verb": "ver", "pronoun": "tú"}, {"verb": "ver", "pronoun": "ella"}, {"verb": "ver", "pronoun": "nosotras"}, {"verb": "ver", "pronoun": "ustedes"}],
        },
        "opener_en": "What did you give him?",
        "opener_es": "¿Qué le diste?",
    },

    "grammar_preterite_irregular_dar_ver_2": {
        "title": "Preterite Highly Irregular — dar + ver (2/2)",
        "grammar_level": 17.1,
        "lesson_number": 4,
        "lesson_type": "conjugation",
        "word_workload": ["dar", "ver"],
        "video_embed_id": "Ib68zJ3q7i8",
        "drill_type": "conjugation",
        "tense": "preterite",
        "intro_chart": PRETERITE_IRREGULAR_DAR_VER_INTRO,
        "drill_config": {
            "answers": {
                "dar": {"yo": "d|i", "tú": "d|iste", "él": "d|io", "ella": "d|io", "usted": "d|io", "nosotros": "d|imos", "nosotras": "d|imos", "ellos": "d|ieron", "ellas": "d|ieron", "ustedes": "d|ieron"},
                "ver": {"yo": "v|i", "tú": "v|iste", "él": "v|io", "ella": "v|io", "usted": "v|io", "nosotros": "v|imos", "nosotras": "v|imos", "ellos": "v|ieron", "ellas": "v|ieron", "ustedes": "v|ieron"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You gave her a red book.", "es": "Tú le diste un libro rojo.", "noun_id": None, "type": "written", "glosses": {"book": "libro", "red": "rojo", "libro": "book", "rojo": "red"}},
            {"en": "I gave my mother flowers.", "es": "Yo di flores a mi madre.", "noun_id": None, "type": "auditory", "glosses": {"flowers": "flores", "mother": "madre", "flores": "flowers", "madre": "mother"}},
            {"en": "He gave the teacher a pen.", "es": "Él dio un bolígrafo al profesor.", "noun_id": None, "type": "written", "glosses": {"pen": "bolígrafo", "teacher": "profesor", "bolígrafo": "pen", "profesor": "teacher"}},
            {"en": "We gave gifts yesterday.", "es": "Nosotros dimos regalos ayer.", "noun_id": None, "type": "auditory", "glosses": {"gifts": "regalos", "yesterday": "ayer", "regalos": "gifts", "ayer": "yesterday"}},
            {"en": "They (f) gave us good news.", "es": "Ellas nos dieron buenas noticias.", "noun_id": None, "type": "written", "glosses": {"news": "noticias", "good": "buenas", "noticias": "news", "buenas": "good"}},
            {"en": "You saw the big dog.", "es": "Tú viste el perro grande.", "noun_id": None, "type": "written", "glosses": {"dog": "perro", "big": "grande", "perro": "dog", "grande": "big"}},
            {"en": "I saw a movie last night.", "es": "Yo vi una película anoche.", "noun_id": None, "type": "auditory", "glosses": {"movie": "película", "last night": "anoche", "película": "movie", "anoche": "last night"}},
            {"en": "He saw the blue car.", "es": "Él vio el coche azul.", "noun_id": None, "type": "written", "glosses": {"car": "coche", "blue": "azul", "coche": "car", "azul": "blue"}},
            {"en": "We saw many stars today.", "es": "Nosotros vimos muchas estrellas hoy.", "noun_id": None, "type": "auditory", "glosses": {"stars": "estrellas", "many": "muchas", "today": "hoy", "estrellas": "stars", "muchas": "many", "hoy": "today"}},
            {"en": "They (f) saw a small house.", "es": "Ellas vieron una casa pequeña.", "noun_id": None, "type": "written", "glosses": {"house": "casa", "small": "pequeña", "casa": "house", "pequeña": "small"}},
        ],
        "drill_targets": [{"verb": "dar", "pronoun": "tú"}, {"verb": "dar", "pronoun": "yo"}, {"verb": "dar", "pronoun": "él"}, {"verb": "dar", "pronoun": "nosotros"}, {"verb": "dar", "pronoun": "ellas"}, {"verb": "ver", "pronoun": "tú"}, {"verb": "ver", "pronoun": "yo"}, {"verb": "ver", "pronoun": "él"}, {"verb": "ver", "pronoun": "nosotros"}, {"verb": "ver", "pronoun": "ellas"}],
        "phase_2_config": {
            "description": "Preterite Highly Irregular dar + ver (2/2): dar, ver",
            "targets": [{"verb": "dar", "pronoun": "tú"}, {"verb": "dar", "pronoun": "yo"}, {"verb": "dar", "pronoun": "él"}, {"verb": "dar", "pronoun": "nosotros"}, {"verb": "dar", "pronoun": "ellas"}, {"verb": "ver", "pronoun": "tú"}, {"verb": "ver", "pronoun": "yo"}, {"verb": "ver", "pronoun": "él"}, {"verb": "ver", "pronoun": "nosotros"}, {"verb": "ver", "pronoun": "ellas"}],
        },
        "opener_en": "What did you see at the museum?",
        "opener_es": "¿Qué viste en el museo?",
    },

    "grammar_preterite_irregular_hacer_decir_1": {
        "title": "Preterite Highly Irregular — hacer + decir (strong stems) (1/2)",
        "grammar_level": 17.1,
        "lesson_number": 5,
        "lesson_type": "conjugation",
        "word_workload": ["hacer", "decir"],
        "video_embed_id": "Ib68zJ3q7i8",
        "drill_type": "conjugation",
        "tense": "preterite",
        "intro_chart": PRETERITE_IRREGULAR_HACER_DECIR_INTRO,
        "drill_config": {
            "answers": {
                "hacer": {"yo": "hic|e", "tú": "hic|iste", "él": "hiz|o", "ella": "hiz|o", "usted": "hiz|o", "nosotros": "hic|imos", "nosotras": "hic|imos", "ellos": "hic|ieron", "ellas": "hic|ieron", "ustedes": "hic|ieron"},
                "decir": {"yo": "dij|e", "tú": "dij|iste", "él": "dij|o", "ella": "dij|o", "usted": "dij|o", "nosotros": "dij|imos", "nosotras": "dij|imos", "ellos": "dij|eron", "ellas": "dij|eron", "ustedes": "dij|eron"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I made a cake", "es": "Yo hice un pastel", "noun_id": None, "type": "written", "glosses": {"cake": "pastel", "pastel": "cake"}},
            {"en": "You did the homework", "es": "Tú hiciste la tarea", "noun_id": None, "type": "auditory", "glosses": {"homework": "tarea", "tarea": "homework"}},
            {"en": "She made a mistake", "es": "Ella hizo un error", "noun_id": None, "type": "written", "glosses": {"mistake": "error", "error": "mistake"}},
            {"en": "We (f) made dinner", "es": "Nosotras hicimos la cena", "noun_id": None, "type": "auditory", "glosses": {"dinner": "cena", "cena": "dinner"}},
            {"en": "You all made plans", "es": "Ustedes hicieron planes", "noun_id": None, "type": "written", "glosses": {"plans": "planes", "planes": "plans"}},
            {"en": "I said the truth", "es": "Yo dije la verdad", "noun_id": None, "type": "written", "glosses": {"truth": "verdad", "verdad": "truth"}},
            {"en": "You said a secret", "es": "Tú dijiste un secreto", "noun_id": None, "type": "auditory", "glosses": {"secret": "secreto", "secreto": "secret"}},
            {"en": "She said a joke", "es": "Ella dijo un chiste", "noun_id": None, "type": "written", "glosses": {"joke": "chiste", "chiste": "joke"}},
            {"en": "We (f) said nothing", "es": "Nosotras dijimos nada", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "You all said goodbye", "es": "Ustedes dijeron adiós", "noun_id": None, "type": "written", "glosses": {"goodbye": "adiós", "adiós": "goodbye"}},
        ],
        "drill_targets": [{"verb": "hacer", "pronoun": "yo"}, {"verb": "hacer", "pronoun": "tú"}, {"verb": "hacer", "pronoun": "ella"}, {"verb": "hacer", "pronoun": "nosotras"}, {"verb": "hacer", "pronoun": "ustedes"}, {"verb": "decir", "pronoun": "yo"}, {"verb": "decir", "pronoun": "tú"}, {"verb": "decir", "pronoun": "ella"}, {"verb": "decir", "pronoun": "nosotras"}, {"verb": "decir", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Preterite Highly Irregular hacer + decir (strong stems) (1/2): hacer, decir",
            "targets": [{"verb": "hacer", "pronoun": "yo"}, {"verb": "hacer", "pronoun": "tú"}, {"verb": "hacer", "pronoun": "ella"}, {"verb": "hacer", "pronoun": "nosotras"}, {"verb": "hacer", "pronoun": "ustedes"}, {"verb": "decir", "pronoun": "yo"}, {"verb": "decir", "pronoun": "tú"}, {"verb": "decir", "pronoun": "ella"}, {"verb": "decir", "pronoun": "nosotras"}, {"verb": "decir", "pronoun": "ustedes"}],
        },
        "opener_en": "What did you do last weekend?",
        "opener_es": "¿Qué hiciste el fin de semana?",
    },

    "grammar_preterite_irregular_hacer_decir_2": {
        "title": "Preterite Highly Irregular — hacer + decir (strong stems) (2/2)",
        "grammar_level": 17.1,
        "lesson_number": 6,
        "lesson_type": "conjugation",
        "word_workload": ["hacer", "decir"],
        "video_embed_id": "Ib68zJ3q7i8",
        "drill_type": "conjugation",
        "tense": "preterite",
        "intro_chart": PRETERITE_IRREGULAR_HACER_DECIR_INTRO,
        "drill_config": {
            "answers": {
                "hacer": {"yo": "hic|e", "tú": "hic|iste", "él": "hiz|o", "ella": "hiz|o", "usted": "hiz|o", "nosotros": "hic|imos", "nosotras": "hic|imos", "ellos": "hic|ieron", "ellas": "hic|ieron", "ustedes": "hic|ieron"},
                "decir": {"yo": "dij|e", "tú": "dij|iste", "él": "dij|o", "ella": "dij|o", "usted": "dij|o", "nosotros": "dij|imos", "nosotras": "dij|imos", "ellos": "dij|eron", "ellas": "dij|eron", "ustedes": "dij|eron"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You made a cake.", "es": "Tú hiciste un pastel.", "noun_id": None, "type": "written", "glosses": {"cake": "pastel", "pastel": "cake"}},
            {"en": "I made dinner last night.", "es": "Yo hice la cena anoche.", "noun_id": None, "type": "auditory", "glosses": {"dinner": "cena", "cena": "dinner", "last night": "anoche", "anoche": "last night"}},
            {"en": "He made a big mistake.", "es": "Él hizo un gran error.", "noun_id": None, "type": "written", "glosses": {"big": "gran", "gran": "big", "mistake": "error", "error": "mistake"}},
            {"en": "We made plans yesterday.", "es": "Nosotros hicimos planes ayer.", "noun_id": None, "type": "auditory", "glosses": {"plans": "planes", "planes": "plans", "yesterday": "ayer", "ayer": "yesterday"}},
            {"en": "They (f) made a new dress.", "es": "Ellas hicieron un vestido nuevo.", "noun_id": None, "type": "written", "glosses": {"dress": "vestido", "vestido": "dress", "new": "nuevo", "nuevo": "new"}},
            {"en": "You said the truth.", "es": "Tú dijiste la verdad.", "noun_id": None, "type": "written", "glosses": {"truth": "verdad", "verdad": "truth"}},
            {"en": "I said nothing.", "es": "Yo dije nada.", "noun_id": None, "type": "auditory", "glosses": {}},
            {"en": "He said a funny joke.", "es": "Él dijo un chiste gracioso.", "noun_id": None, "type": "written", "glosses": {"joke": "chiste", "chiste": "joke", "funny": "gracioso", "gracioso": "funny"}},
            {"en": "We said goodbye.", "es": "Nosotros dijimos adiós.", "noun_id": None, "type": "auditory", "glosses": {"goodbye": "adiós", "adiós": "goodbye"}},
            {"en": "They (f) said many things.", "es": "Ellas dijeron muchas cosas.", "noun_id": None, "type": "written", "glosses": {"many": "muchas", "muchas": "many", "things": "cosas", "cosas": "things"}},
        ],
        "drill_targets": [{"verb": "hacer", "pronoun": "tú"}, {"verb": "hacer", "pronoun": "yo"}, {"verb": "hacer", "pronoun": "él"}, {"verb": "hacer", "pronoun": "nosotros"}, {"verb": "hacer", "pronoun": "ellas"}, {"verb": "decir", "pronoun": "tú"}, {"verb": "decir", "pronoun": "yo"}, {"verb": "decir", "pronoun": "él"}, {"verb": "decir", "pronoun": "nosotros"}, {"verb": "decir", "pronoun": "ellas"}],
        "phase_2_config": {
            "description": "Preterite Highly Irregular hacer + decir (strong stems) (2/2): hacer, decir",
            "targets": [{"verb": "hacer", "pronoun": "tú"}, {"verb": "hacer", "pronoun": "yo"}, {"verb": "hacer", "pronoun": "él"}, {"verb": "hacer", "pronoun": "nosotros"}, {"verb": "hacer", "pronoun": "ellas"}, {"verb": "decir", "pronoun": "tú"}, {"verb": "decir", "pronoun": "yo"}, {"verb": "decir", "pronoun": "él"}, {"verb": "decir", "pronoun": "nosotros"}, {"verb": "decir", "pronoun": "ellas"}],
        },
        "opener_en": "What did she say?",
        "opener_es": "¿Qué dijo ella?",
    },

    "grammar_preterite_irregular_traer_dormir_1": {
        "title": "Preterite Highly Irregular — traer + dormir (1/2)",
        "grammar_level": 17.1,
        "lesson_number": 7,
        "lesson_type": "conjugation",
        "word_workload": ["traer", "dormir"],
        "video_embed_id": "Ib68zJ3q7i8",
        "drill_type": "conjugation",
        "tense": "preterite",
        "intro_chart": PRETERITE_IRREGULAR_TRAER_DORMIR_INTRO,
        "drill_config": {
            "answers": {
                "traer": {"yo": "traj|e", "tú": "traj|iste", "él": "traj|o", "ella": "traj|o", "usted": "traj|o", "nosotros": "traj|imos", "nosotras": "traj|imos", "ellos": "traj|eron", "ellas": "traj|eron", "ustedes": "traj|eron"},
                "dormir": {"yo": "dorm|í", "tú": "dorm|iste", "él": "d|urmió", "ella": "d|urmió", "usted": "d|urmió", "nosotros": "dorm|imos", "nosotras": "dorm|imos", "ellos": "d|urmieron", "ellas": "d|urmieron", "ustedes": "d|urmieron"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I brought the book yesterday.", "es": "Yo traje el libro ayer.", "noun_id": None, "type": "written", "glosses": {"book": "libro", "libro": "book", "yesterday": "ayer", "ayer": "yesterday"}},
            {"en": "You brought fresh fruit.", "es": "Tú trajiste fruta fresca.", "noun_id": None, "type": "auditory", "glosses": {"fruit": "fruta", "fruta": "fruit", "fresh": "fresca", "fresca": "fresh"}},
            {"en": "She brought the red dress.", "es": "Ella trajo el vestido rojo.", "noun_id": None, "type": "written", "glosses": {"dress": "vestido", "vestido": "dress", "red": "rojo", "rojo": "red"}},
            {"en": "We (f) brought cold water.", "es": "Nosotras trajimos agua fría.", "noun_id": None, "type": "auditory", "glosses": {"water": "agua", "agua": "water", "cold": "fría", "fría": "cold"}},
            {"en": "You all brought big bags.", "es": "Ustedes trajeron bolsas grandes.", "noun_id": None, "type": "written", "glosses": {"bags": "bolsas", "bolsas": "bags", "big": "grandes", "grandes": "big"}},
            {"en": "I slept well last night.", "es": "Yo dormí bien anoche.", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well", "last night": "anoche", "anoche": "last night"}},
            {"en": "You slept eight hours.", "es": "Tú dormiste ocho horas.", "noun_id": None, "type": "auditory", "glosses": {"hours": "horas", "horas": "hours", "eight": "ocho", "ocho": "eight"}},
            {"en": "She slept deeply.", "es": "Ella durmió profundamente.", "noun_id": None, "type": "written", "glosses": {"deeply": "profundamente", "profundamente": "deeply"}},
            {"en": "We (f) slept early.", "es": "Nosotras dormimos temprano.", "noun_id": None, "type": "auditory", "glosses": {"early": "temprano", "temprano": "early"}},
            {"en": "You all slept in the hotel.", "es": "Ustedes durmieron en el hotel.", "noun_id": None, "type": "written", "glosses": {"hotel": "hotel"}},
        ],
        "drill_targets": [{"verb": "traer", "pronoun": "yo"}, {"verb": "traer", "pronoun": "tú"}, {"verb": "traer", "pronoun": "ella"}, {"verb": "traer", "pronoun": "nosotras"}, {"verb": "traer", "pronoun": "ustedes"}, {"verb": "dormir", "pronoun": "yo"}, {"verb": "dormir", "pronoun": "tú"}, {"verb": "dormir", "pronoun": "ella"}, {"verb": "dormir", "pronoun": "nosotras"}, {"verb": "dormir", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Preterite Highly Irregular traer + dormir (1/2): traer, dormir",
            "targets": [{"verb": "traer", "pronoun": "yo"}, {"verb": "traer", "pronoun": "tú"}, {"verb": "traer", "pronoun": "ella"}, {"verb": "traer", "pronoun": "nosotras"}, {"verb": "traer", "pronoun": "ustedes"}, {"verb": "dormir", "pronoun": "yo"}, {"verb": "dormir", "pronoun": "tú"}, {"verb": "dormir", "pronoun": "ella"}, {"verb": "dormir", "pronoun": "nosotras"}, {"verb": "dormir", "pronoun": "ustedes"}],
        },
        "opener_en": "What did you bring to the party?",
        "opener_es": "¿Qué trajiste a la fiesta?",
    },

    "grammar_preterite_irregular_traer_dormir_2": {
        "title": "Preterite Highly Irregular — traer + dormir (2/2)",
        "grammar_level": 17.1,
        "lesson_number": 8,
        "lesson_type": "conjugation",
        "word_workload": ["traer", "dormir"],
        "video_embed_id": "Ib68zJ3q7i8",
        "drill_type": "conjugation",
        "tense": "preterite",
        "intro_chart": PRETERITE_IRREGULAR_TRAER_DORMIR_INTRO,
        "drill_config": {
            "answers": {
                "traer": {"yo": "traj|e", "tú": "traj|iste", "él": "traj|o", "ella": "traj|o", "usted": "traj|o", "nosotros": "traj|imos", "nosotras": "traj|imos", "ellos": "traj|eron", "ellas": "traj|eron", "ustedes": "traj|eron"},
                "dormir": {"yo": "dorm|í", "tú": "dorm|iste", "él": "d|urmió", "ella": "d|urmió", "usted": "d|urmió", "nosotros": "dorm|imos", "nosotras": "dorm|imos", "ellos": "d|urmieron", "ellas": "d|urmieron", "ustedes": "d|urmieron"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You brought the books.", "es": "Tú trajiste los libros.", "noun_id": None, "type": "written", "glosses": {"books": "libros", "libros": "books"}},
            {"en": "I brought a gift.", "es": "Yo traje un regalo.", "noun_id": None, "type": "auditory", "glosses": {"gift": "regalo", "regalo": "gift"}},
            {"en": "He brought water.", "es": "Él trajo agua.", "noun_id": None, "type": "written", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "We brought food.", "es": "Nosotros trajimos comida.", "noun_id": None, "type": "auditory", "glosses": {"food": "comida", "comida": "food"}},
            {"en": "They (f) brought flowers.", "es": "Ellas trajeron flores.", "noun_id": None, "type": "written", "glosses": {"flowers": "flores", "flores": "flowers"}},
            {"en": "You slept well.", "es": "Tú dormiste bien.", "noun_id": None, "type": "written", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "I slept early.", "es": "Yo dormí temprano.", "noun_id": None, "type": "auditory", "glosses": {"early": "temprano", "temprano": "early"}},
            {"en": "He slept a lot.", "es": "Él durmió mucho.", "noun_id": None, "type": "written", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "We slept late.", "es": "Nosotros dormimos tarde.", "noun_id": None, "type": "auditory", "glosses": {"late": "tarde", "tarde": "late"}},
            {"en": "They (f) slept quietly.", "es": "Ellas durmieron tranquilamente.", "noun_id": None, "type": "written", "glosses": {"quietly": "tranquilamente", "tranquilamente": "quietly"}},
        ],
        "drill_targets": [{"verb": "traer", "pronoun": "tú"}, {"verb": "traer", "pronoun": "yo"}, {"verb": "traer", "pronoun": "él"}, {"verb": "traer", "pronoun": "nosotros"}, {"verb": "traer", "pronoun": "ellas"}, {"verb": "dormir", "pronoun": "tú"}, {"verb": "dormir", "pronoun": "yo"}, {"verb": "dormir", "pronoun": "él"}, {"verb": "dormir", "pronoun": "nosotros"}, {"verb": "dormir", "pronoun": "ellas"}],
        "phase_2_config": {
            "description": "Preterite Highly Irregular traer + dormir (2/2): traer, dormir",
            "targets": [{"verb": "traer", "pronoun": "tú"}, {"verb": "traer", "pronoun": "yo"}, {"verb": "traer", "pronoun": "él"}, {"verb": "traer", "pronoun": "nosotros"}, {"verb": "traer", "pronoun": "ellas"}, {"verb": "dormir", "pronoun": "tú"}, {"verb": "dormir", "pronoun": "yo"}, {"verb": "dormir", "pronoun": "él"}, {"verb": "dormir", "pronoun": "nosotros"}, {"verb": "dormir", "pronoun": "ellas"}],
        },
        "opener_en": "How long did you sleep?",
        "opener_es": "¿Cuánto dormiste?",
    },

    "grammar_preterite_irregular_ser_ir_chat": {
        "title": "Preterite Highly Irregular — ser + ir (identical) Chat",
        "grammar_level": 17.1,
        "lesson_number": 2.5,
        "lesson_type": "conjugation",
        "word_workload": ["ser", "ir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "preterite",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Preterite Highly Irregular ser + ir (identical) chat: ser, ir", "targets": [{"verb": "ser", "pronoun": "yo"}, {"verb": "ser", "pronoun": "tú"}, {"verb": "ser", "pronoun": "ella"}, {"verb": "ser", "pronoun": "nosotras"}, {"verb": "ser", "pronoun": "ustedes"}, {"verb": "ir", "pronoun": "tú"}, {"verb": "ir", "pronoun": "yo"}, {"verb": "ir", "pronoun": "él"}, {"verb": "ir", "pronoun": "nosotros"}, {"verb": "ir", "pronoun": "ellas"}]},
    },

    "grammar_preterite_irregular_dar_ver_chat": {
        "title": "Preterite Highly Irregular — dar + ver Chat",
        "grammar_level": 17.1,
        "lesson_number": 4.5,
        "lesson_type": "conjugation",
        "word_workload": ["dar", "ver"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "preterite",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Preterite Highly Irregular dar + ver chat: dar, ver", "targets": [{"verb": "dar", "pronoun": "yo"}, {"verb": "dar", "pronoun": "tú"}, {"verb": "dar", "pronoun": "ella"}, {"verb": "dar", "pronoun": "nosotras"}, {"verb": "dar", "pronoun": "ustedes"}, {"verb": "ver", "pronoun": "tú"}, {"verb": "ver", "pronoun": "yo"}, {"verb": "ver", "pronoun": "él"}, {"verb": "ver", "pronoun": "nosotros"}, {"verb": "ver", "pronoun": "ellas"}]},
    },

    "grammar_preterite_irregular_hacer_decir_chat": {
        "title": "Preterite Highly Irregular — hacer + decir (strong stems) Chat",
        "grammar_level": 17.1,
        "lesson_number": 6.5,
        "lesson_type": "conjugation",
        "word_workload": ["hacer", "decir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "preterite",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Preterite Highly Irregular hacer + decir (strong stems) chat: hacer, decir", "targets": [{"verb": "hacer", "pronoun": "yo"}, {"verb": "hacer", "pronoun": "tú"}, {"verb": "hacer", "pronoun": "ella"}, {"verb": "hacer", "pronoun": "nosotras"}, {"verb": "hacer", "pronoun": "ustedes"}, {"verb": "decir", "pronoun": "tú"}, {"verb": "decir", "pronoun": "yo"}, {"verb": "decir", "pronoun": "él"}, {"verb": "decir", "pronoun": "nosotros"}, {"verb": "decir", "pronoun": "ellas"}]},
    },

    "grammar_preterite_irregular_traer_dormir_chat": {
        "title": "Preterite Highly Irregular — traer + dormir Chat",
        "grammar_level": 17.1,
        "lesson_number": 8.5,
        "lesson_type": "conjugation",
        "word_workload": ["traer", "dormir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "preterite",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Preterite Highly Irregular traer + dormir chat: traer, dormir", "targets": [{"verb": "traer", "pronoun": "yo"}, {"verb": "traer", "pronoun": "tú"}, {"verb": "traer", "pronoun": "ella"}, {"verb": "traer", "pronoun": "nosotras"}, {"verb": "traer", "pronoun": "ustedes"}, {"verb": "dormir", "pronoun": "tú"}, {"verb": "dormir", "pronoun": "yo"}, {"verb": "dormir", "pronoun": "él"}, {"verb": "dormir", "pronoun": "nosotros"}, {"verb": "dormir", "pronoun": "ellas"}]},
    },

    # ── From _gl18_output.py ──

"grammar_gerund_hablar_caminar_1": {
        "title": "Gerund — hablar + caminar (-ar) (1/2)",
        "grammar_level": 18,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "caminar"],
        "video_embed_id": "Xpma6w0jy7m",
        "drill_type": "conjugation",
        "tense": "gerund",
        "intro_chart": GERUND_HABLAR_CAMINAR_INTRO,
        "drill_config": {
            "answers": {
                "hablar": {"yo": "est|oy hablando", "tú": "est|ás hablando", "él": "est|á hablando", "ella": "est|á hablando", "usted": "est|á hablando", "nosotros": "est|amos hablando", "nosotras": "est|amos hablando", "ellos": "est|án hablando", "ellas": "est|án hablando", "ustedes": "est|án hablando"},
                "caminar": {"yo": "est|oy caminando", "tú": "est|ás caminando", "él": "est|á caminando", "ella": "est|á caminando", "usted": "est|á caminando", "nosotros": "est|amos caminando", "nosotras": "est|amos caminando", "ellos": "est|án caminando", "ellas": "est|án caminando", "ustedes": "est|án caminando"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I am speaking Spanish.", "es": "Yo estoy hablando español.", "noun_id": None, "type": "written", "glosses": {"Spanish": "español", "español": "Spanish"}},
            {"en": "You are speaking loudly.", "es": "Tú estás hablando fuerte.", "noun_id": None, "type": "auditory", "glosses": {"loudly": "fuerte", "fuerte": "loudly"}},
            {"en": "She is speaking with friends.", "es": "Ella está hablando con amigas.", "noun_id": None, "type": "written", "glosses": {"friends": "amigas", "amigas": "friends"}},
            {"en": "We (f) are speaking softly.", "es": "Nosotras estamos hablando suavemente.", "noun_id": None, "type": "auditory", "glosses": {"softly": "suavemente", "suavemente": "softly"}},
            {"en": "You all are speaking quickly.", "es": "Ustedes están hablando rápido.", "noun_id": None, "type": "written", "glosses": {"quickly": "rápido", "rápido": "quickly"}},
            {"en": "I am walking in the park.", "es": "Yo estoy caminando en el parque.", "noun_id": None, "type": "written", "glosses": {"park": "parque", "parque": "park"}},
            {"en": "You are walking slowly.", "es": "Tú estás caminando despacio.", "noun_id": None, "type": "auditory", "glosses": {"slowly": "despacio", "despacio": "slowly"}},
            {"en": "She is walking to school.", "es": "Ella está caminando a la escuela.", "noun_id": None, "type": "written", "glosses": {"school": "escuela", "escuela": "school"}},
            {"en": "We (f) are walking together.", "es": "Nosotras estamos caminando juntas.", "noun_id": None, "type": "auditory", "glosses": {"together": "juntas", "juntas": "together"}},
            {"en": "You all are walking fast.", "es": "Ustedes están caminando rápido.", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
        ],
        "drill_targets": [{"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "ella"}, {"verb": "hablar", "pronoun": "nosotras"}, {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "caminar", "pronoun": "yo"}, {"verb": "caminar", "pronoun": "tú"}, {"verb": "caminar", "pronoun": "ella"}, {"verb": "caminar", "pronoun": "nosotras"}, {"verb": "caminar", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Gerund hablar + caminar (-ar) (1/2): hablar, caminar",
            "targets": [{"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "ella"}, {"verb": "hablar", "pronoun": "nosotras"}, {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "caminar", "pronoun": "yo"}, {"verb": "caminar", "pronoun": "tú"}, {"verb": "caminar", "pronoun": "ella"}, {"verb": "caminar", "pronoun": "nosotras"}, {"verb": "caminar", "pronoun": "ustedes"}],
        },
        "opener_en": "What are you saying?",
        "opener_es": "¿Qué estás hablando?",
    },

    "grammar_gerund_hablar_caminar_2": {
        "title": "Gerund — hablar + caminar (-ar) (2/2)",
        "grammar_level": 18,
        "lesson_number": 2,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "caminar"],
        "video_embed_id": "Xpma6w0jy7m",
        "drill_type": "conjugation",
        "tense": "gerund",
        "intro_chart": GERUND_HABLAR_CAMINAR_INTRO,
        "drill_config": {
            "answers": {
                "hablar": {"yo": "est|oy hablando", "tú": "est|ás hablando", "él": "est|á hablando", "ella": "est|á hablando", "usted": "est|á hablando", "nosotros": "est|amos hablando", "nosotras": "est|amos hablando", "ellos": "est|án hablando", "ellas": "est|án hablando", "ustedes": "est|án hablando"},
                "caminar": {"yo": "est|oy caminando", "tú": "est|ás caminando", "él": "est|á caminando", "ella": "est|á caminando", "usted": "est|á caminando", "nosotros": "est|amos caminando", "nosotras": "est|amos caminando", "ellos": "est|án caminando", "ellas": "est|án caminando", "ustedes": "est|án caminando"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You are speaking Spanish.", "es": "Tú estás hablando español.", "noun_id": None, "type": "written", "glosses": {"Spanish": "español", "español": "Spanish"}},
            {"en": "I am speaking very clearly.", "es": "Yo estoy hablando muy claro.", "noun_id": None, "type": "auditory", "glosses": {"clearly": "claro", "claro": "clearly"}},
            {"en": "He is speaking with friends.", "es": "Él está hablando con amigos.", "noun_id": None, "type": "written", "glosses": {"friends": "amigos", "amigos": "friends"}},
            {"en": "We (m) are speaking loudly.", "es": "Nosotros estamos hablando fuerte.", "noun_id": None, "type": "auditory", "glosses": {"loudly": "fuerte", "fuerte": "loudly"}},
            {"en": "They (f) are speaking quickly.", "es": "Ellas están hablando rápido.", "noun_id": None, "type": "written", "glosses": {"quickly": "rápido", "rápido": "quickly"}},
            {"en": "You are walking to school.", "es": "Tú estás caminando a la escuela.", "noun_id": None, "type": "written", "glosses": {"school": "escuela", "escuela": "school"}},
            {"en": "I am walking slowly.", "es": "Yo estoy caminando despacio.", "noun_id": None, "type": "auditory", "glosses": {"slowly": "despacio", "despacio": "slowly"}},
            {"en": "He is walking in the park.", "es": "Él está caminando en el parque.", "noun_id": None, "type": "written", "glosses": {"park": "parque", "parque": "park"}},
            {"en": "We (m) are walking together.", "es": "Nosotros estamos caminando juntos.", "noun_id": None, "type": "auditory", "glosses": {"together": "juntos", "juntos": "together"}},
            {"en": "They (f) are walking fast.", "es": "Ellas están caminando rápido.", "noun_id": None, "type": "written", "glosses": {"fast": "rápido", "rápido": "fast"}},
        ],
        "drill_targets": [{"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "él"}, {"verb": "hablar", "pronoun": "nosotros"}, {"verb": "hablar", "pronoun": "ellas"}, {"verb": "caminar", "pronoun": "tú"}, {"verb": "caminar", "pronoun": "yo"}, {"verb": "caminar", "pronoun": "él"}, {"verb": "caminar", "pronoun": "nosotros"}, {"verb": "caminar", "pronoun": "ellas"}],
        "phase_2_config": {
            "description": "Gerund hablar + caminar (-ar) (2/2): hablar, caminar",
            "targets": [{"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "él"}, {"verb": "hablar", "pronoun": "nosotros"}, {"verb": "hablar", "pronoun": "ellas"}, {"verb": "caminar", "pronoun": "tú"}, {"verb": "caminar", "pronoun": "yo"}, {"verb": "caminar", "pronoun": "él"}, {"verb": "caminar", "pronoun": "nosotros"}, {"verb": "caminar", "pronoun": "ellas"}],
        },
        "opener_en": "Where are you walking?",
        "opener_es": "¿Por dónde estás caminando?",
    },

    "grammar_gerund_comer_beber_1": {
        "title": "Gerund — comer + beber (-er) (1/2)",
        "grammar_level": 18,
        "lesson_number": 3,
        "lesson_type": "conjugation",
        "word_workload": ["comer", "beber"],
        "video_embed_id": "Xpma6w0jy7m",
        "drill_type": "conjugation",
        "tense": "gerund",
        "intro_chart": GERUND_COMER_BEBER_INTRO,
        "drill_config": {
            "answers": {
                "comer": {"yo": "est|oy comiendo", "tú": "est|ás comiendo", "él": "est|á comiendo", "ella": "est|á comiendo", "usted": "est|á comiendo", "nosotros": "est|amos comiendo", "nosotras": "est|amos comiendo", "ellos": "est|án comiendo", "ellas": "est|án comiendo", "ustedes": "est|án comiendo"},
                "beber": {"yo": "est|oy bebiendo", "tú": "est|ás bebiendo", "él": "est|á bebiendo", "ella": "est|á bebiendo", "usted": "est|á bebiendo", "nosotros": "est|amos bebiendo", "nosotras": "est|amos bebiendo", "ellos": "est|án bebiendo", "ellas": "est|án bebiendo", "ustedes": "est|án bebiendo"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I am eating an apple.", "es": "Yo estoy comiendo una manzana.", "noun_id": None, "type": "written", "glosses": {"apple": "manzana", "manzana": "apple"}},
            {"en": "You are eating bread.", "es": "Tú estás comiendo pan.", "noun_id": None, "type": "auditory", "glosses": {"bread": "pan", "pan": "bread"}},
            {"en": "She is eating rice.", "es": "Ella está comiendo arroz.", "noun_id": None, "type": "written", "glosses": {"rice": "arroz", "arroz": "rice"}},
            {"en": "We (f) are eating salad.", "es": "Nosotras estamos comiendo ensalada.", "noun_id": None, "type": "auditory", "glosses": {"salad": "ensalada", "ensalada": "salad"}},
            {"en": "You (pl) are eating fish.", "es": "Ustedes están comiendo pescado.", "noun_id": None, "type": "written", "glosses": {"fish": "pescado", "pescado": "fish"}},
            {"en": "I am drinking water.", "es": "Yo estoy bebiendo agua.", "noun_id": None, "type": "written", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "You are drinking juice.", "es": "Tú estás bebiendo jugo.", "noun_id": None, "type": "auditory", "glosses": {"juice": "jugo", "jugo": "juice"}},
            {"en": "She is drinking tea.", "es": "Ella está bebiendo té.", "noun_id": None, "type": "written", "glosses": {"tea": "té", "té": "tea"}},
            {"en": "We (f) are drinking coffee.", "es": "Nosotras estamos bebiendo café.", "noun_id": None, "type": "auditory", "glosses": {"coffee": "café", "café": "coffee"}},
            {"en": "You (pl) are drinking milk.", "es": "Ustedes están bebiendo leche.", "noun_id": None, "type": "written", "glosses": {"milk": "leche", "leche": "milk"}},
        ],
        "drill_targets": [{"verb": "comer", "pronoun": "yo"}, {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "ella"}, {"verb": "comer", "pronoun": "nosotras"}, {"verb": "comer", "pronoun": "ustedes"}, {"verb": "beber", "pronoun": "yo"}, {"verb": "beber", "pronoun": "tú"}, {"verb": "beber", "pronoun": "ella"}, {"verb": "beber", "pronoun": "nosotras"}, {"verb": "beber", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Gerund comer + beber (-er) (1/2): comer, beber",
            "targets": [{"verb": "comer", "pronoun": "yo"}, {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "ella"}, {"verb": "comer", "pronoun": "nosotras"}, {"verb": "comer", "pronoun": "ustedes"}, {"verb": "beber", "pronoun": "yo"}, {"verb": "beber", "pronoun": "tú"}, {"verb": "beber", "pronoun": "ella"}, {"verb": "beber", "pronoun": "nosotras"}, {"verb": "beber", "pronoun": "ustedes"}],
        },
        "opener_en": "What are you eating?",
        "opener_es": "¿Qué estás comiendo?",
    },

    "grammar_gerund_comer_beber_2": {
        "title": "Gerund — comer + beber (-er) (2/2)",
        "grammar_level": 18,
        "lesson_number": 4,
        "lesson_type": "conjugation",
        "word_workload": ["comer", "beber"],
        "video_embed_id": "Xpma6w0jy7m",
        "drill_type": "conjugation",
        "tense": "gerund",
        "intro_chart": GERUND_COMER_BEBER_INTRO,
        "drill_config": {
            "answers": {
                "comer": {"yo": "est|oy comiendo", "tú": "est|ás comiendo", "él": "est|á comiendo", "ella": "est|á comiendo", "usted": "est|á comiendo", "nosotros": "est|amos comiendo", "nosotras": "est|amos comiendo", "ellos": "est|án comiendo", "ellas": "est|án comiendo", "ustedes": "est|án comiendo"},
                "beber": {"yo": "est|oy bebiendo", "tú": "est|ás bebiendo", "él": "est|á bebiendo", "ella": "est|á bebiendo", "usted": "est|á bebiendo", "nosotros": "est|amos bebiendo", "nosotras": "est|amos bebiendo", "ellos": "est|án bebiendo", "ellas": "est|án bebiendo", "ustedes": "est|án bebiendo"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You are eating an apple.", "es": "Tú estás comiendo una manzana.", "noun_id": None, "type": "written", "glosses": {"apple": "manzana", "manzana": "apple"}},
            {"en": "I am eating bread.", "es": "Yo estoy comiendo pan.", "noun_id": None, "type": "auditory", "glosses": {"bread": "pan", "pan": "bread"}},
            {"en": "He is eating rice.", "es": "Él está comiendo arroz.", "noun_id": None, "type": "written", "glosses": {"rice": "arroz", "arroz": "rice"}},
            {"en": "We (m) are eating salad.", "es": "Nosotros estamos comiendo ensalada.", "noun_id": None, "type": "auditory", "glosses": {"salad": "ensalada", "ensalada": "salad"}},
            {"en": "They (f) are eating fruit.", "es": "Ellas están comiendo fruta.", "noun_id": None, "type": "written", "glosses": {"fruit": "fruta", "fruta": "fruit"}},
            {"en": "You are drinking water.", "es": "Tú estás bebiendo agua.", "noun_id": None, "type": "written", "glosses": {"water": "agua", "agua": "water"}},
            {"en": "I am drinking juice.", "es": "Yo estoy bebiendo jugo.", "noun_id": None, "type": "auditory", "glosses": {"juice": "jugo", "jugo": "juice"}},
            {"en": "He is drinking milk.", "es": "Él está bebiendo leche.", "noun_id": None, "type": "written", "glosses": {"milk": "leche", "leche": "milk"}},
            {"en": "We (m) are drinking coffee.", "es": "Nosotros estamos bebiendo café.", "noun_id": None, "type": "auditory", "glosses": {"coffee": "café", "café": "coffee"}},
            {"en": "They (f) are drinking tea.", "es": "Ellas están bebiendo té.", "noun_id": None, "type": "written", "glosses": {"tea": "té", "té": "tea"}},
        ],
        "drill_targets": [{"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "yo"}, {"verb": "comer", "pronoun": "él"}, {"verb": "comer", "pronoun": "nosotros"}, {"verb": "comer", "pronoun": "ellas"}, {"verb": "beber", "pronoun": "tú"}, {"verb": "beber", "pronoun": "yo"}, {"verb": "beber", "pronoun": "él"}, {"verb": "beber", "pronoun": "nosotros"}, {"verb": "beber", "pronoun": "ellas"}],
        "phase_2_config": {
            "description": "Gerund comer + beber (-er) (2/2): comer, beber",
            "targets": [{"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "yo"}, {"verb": "comer", "pronoun": "él"}, {"verb": "comer", "pronoun": "nosotros"}, {"verb": "comer", "pronoun": "ellas"}, {"verb": "beber", "pronoun": "tú"}, {"verb": "beber", "pronoun": "yo"}, {"verb": "beber", "pronoun": "él"}, {"verb": "beber", "pronoun": "nosotros"}, {"verb": "beber", "pronoun": "ellas"}],
        },
        "opener_en": "What are you drinking?",
        "opener_es": "¿Qué estás bebiendo?",
    },

    "grammar_gerund_salir_inhibir_1": {
        "title": "Gerund — salir + inhibir (-ir) (1/2)",
        "grammar_level": 18,
        "lesson_number": 5,
        "lesson_type": "conjugation",
        "word_workload": ["salir", "inhibir"],
        "video_embed_id": "Xpma6w0jy7m",
        "drill_type": "conjugation",
        "tense": "gerund",
        "intro_chart": GERUND_SALIR_INHIBIR_INTRO,
        "drill_config": {
            "answers": {
                "salir": {"yo": "est|oy saliendo", "tú": "est|ás saliendo", "él": "est|á saliendo", "ella": "est|á saliendo", "usted": "est|á saliendo", "nosotros": "est|amos saliendo", "nosotras": "est|amos saliendo", "ellos": "est|án saliendo", "ellas": "est|án saliendo", "ustedes": "est|án saliendo"},
                "inhibir": {"yo": "est|oy inhibiendo", "tú": "est|ás inhibiendo", "él": "est|á inhibiendo", "ella": "est|á inhibiendo", "usted": "est|á inhibiendo", "nosotros": "est|amos inhibiendo", "nosotras": "est|amos inhibiendo", "ellos": "est|án inhibiendo", "ellas": "est|án inhibiendo", "ustedes": "est|án inhibiendo"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I am leaving the house.", "es": "Yo estoy saliendo de la casa.", "noun_id": None, "type": "written", "glosses": {"house": "casa", "casa": "house"}},
            {"en": "You are going out with friends.", "es": "Tú estás saliendo con amigos.", "noun_id": None, "type": "auditory", "glosses": {"friends": "amigos", "amigos": "friends"}},
            {"en": "She is leaving the office now.", "es": "Ella está saliendo de la oficina ahora.", "noun_id": None, "type": "written", "glosses": {"office": "oficina", "oficina": "office", "now": "ahora", "ahora": "now"}},
            {"en": "We (f) are leaving the park.", "es": "Nosotras estamos saliendo del parque.", "noun_id": None, "type": "auditory", "glosses": {"park": "parque", "parque": "park"}},
            {"en": "You all are leaving early today.", "es": "Ustedes están saliendo temprano hoy.", "noun_id": None, "type": "written", "glosses": {"today": "hoy", "hoy": "today", "early": "temprano", "temprano": "early"}},
            {"en": "I am inhibiting the process carefully.", "es": "Yo estoy inhibiendo el proceso cuidadosamente.", "noun_id": None, "type": "written", "glosses": {"process": "proceso", "proceso": "process", "carefully": "cuidadosamente", "cuidadosamente": "carefully"}},
            {"en": "You are inhibiting the reaction now.", "es": "Tú estás inhibiendo la reacción ahora.", "noun_id": None, "type": "auditory", "glosses": {"reaction": "reacción", "reacción": "reaction", "now": "ahora", "ahora": "now"}},
            {"en": "She is inhibiting the signal strongly.", "es": "Ella está inhibiendo la señal fuertemente.", "noun_id": None, "type": "written", "glosses": {"signal": "señal", "señal": "signal", "strongly": "fuertemente", "fuertemente": "strongly"}},
            {"en": "We (f) are inhibiting the effects.", "es": "Nosotras estamos inhibiendo los efectos.", "noun_id": None, "type": "auditory", "glosses": {"effects": "efectos", "efectos": "effects"}},
            {"en": "You all are inhibiting the enzymes.", "es": "Ustedes están inhibiendo las enzimas.", "noun_id": None, "type": "written", "glosses": {"enzymes": "enzimas", "enzimas": "enzymes"}},
        ],
        "drill_targets": [{"verb": "salir", "pronoun": "yo"}, {"verb": "salir", "pronoun": "tú"}, {"verb": "salir", "pronoun": "ella"}, {"verb": "salir", "pronoun": "nosotras"}, {"verb": "salir", "pronoun": "ustedes"}, {"verb": "inhibir", "pronoun": "yo"}, {"verb": "inhibir", "pronoun": "tú"}, {"verb": "inhibir", "pronoun": "ella"}, {"verb": "inhibir", "pronoun": "nosotras"}, {"verb": "inhibir", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Gerund salir + inhibir (-ir) (1/2): salir, inhibir",
            "targets": [{"verb": "salir", "pronoun": "yo"}, {"verb": "salir", "pronoun": "tú"}, {"verb": "salir", "pronoun": "ella"}, {"verb": "salir", "pronoun": "nosotras"}, {"verb": "salir", "pronoun": "ustedes"}, {"verb": "inhibir", "pronoun": "yo"}, {"verb": "inhibir", "pronoun": "tú"}, {"verb": "inhibir", "pronoun": "ella"}, {"verb": "inhibir", "pronoun": "nosotras"}, {"verb": "inhibir", "pronoun": "ustedes"}],
        },
        "opener_en": "Who is leaving the building?",
        "opener_es": "¿Quién está saliendo del edificio?",
    },

    "grammar_gerund_salir_inhibir_2": {
        "title": "Gerund — salir + inhibir (-ir) (2/2)",
        "grammar_level": 18,
        "lesson_number": 6,
        "lesson_type": "conjugation",
        "word_workload": ["salir", "inhibir"],
        "video_embed_id": "Xpma6w0jy7m",
        "drill_type": "conjugation",
        "tense": "gerund",
        "intro_chart": GERUND_SALIR_INHIBIR_INTRO,
        "drill_config": {
            "answers": {
                "salir": {"yo": "est|oy saliendo", "tú": "est|ás saliendo", "él": "est|á saliendo", "ella": "est|á saliendo", "usted": "est|á saliendo", "nosotros": "est|amos saliendo", "nosotras": "est|amos saliendo", "ellos": "est|án saliendo", "ellas": "est|án saliendo", "ustedes": "est|án saliendo"},
                "inhibir": {"yo": "est|oy inhibiendo", "tú": "est|ás inhibiendo", "él": "est|á inhibiendo", "ella": "est|á inhibiendo", "usted": "est|á inhibiendo", "nosotros": "est|amos inhibiendo", "nosotras": "est|amos inhibiendo", "ellos": "est|án inhibiendo", "ellas": "est|án inhibiendo", "ustedes": "est|án inhibiendo"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You are leaving the house.", "es": "Tú estás saliendo de la casa.", "noun_id": None, "type": "written", "glosses": {"house": "casa", "casa": "house"}},
            {"en": "I am leaving now.", "es": "Yo estoy saliendo ahora.", "noun_id": None, "type": "auditory", "glosses": {"now": "ahora", "ahora": "now"}},
            {"en": "He is leaving the room.", "es": "Él está saliendo del cuarto.", "noun_id": None, "type": "written", "glosses": {"room": "cuarto", "cuarto": "room"}},
            {"en": "We (m) are leaving together.", "es": "Nosotros estamos saliendo juntos.", "noun_id": None, "type": "auditory", "glosses": {"together": "juntos", "juntos": "together"}},
            {"en": "They (f) are leaving early.", "es": "Ellas están saliendo temprano.", "noun_id": None, "type": "written", "glosses": {"early": "temprano", "temprano": "early"}},
            {"en": "You are inhibiting the process.", "es": "Tú estás inhibiendo el proceso.", "noun_id": None, "type": "written", "glosses": {"process": "proceso", "proceso": "process"}},
            {"en": "I am inhibiting the reaction.", "es": "Yo estoy inhibiendo la reacción.", "noun_id": None, "type": "auditory", "glosses": {"reaction": "reacción", "reacción": "reaction"}},
            {"en": "He is inhibiting the signal.", "es": "Él está inhibiendo la señal.", "noun_id": None, "type": "written", "glosses": {"signal": "señal", "señal": "signal"}},
            {"en": "We (m) are inhibiting the response.", "es": "Nosotros estamos inhibiendo la respuesta.", "noun_id": None, "type": "auditory", "glosses": {"response": "respuesta", "respuesta": "response"}},
            {"en": "They (f) are inhibiting the effect.", "es": "Ellas están inhibiendo el efecto.", "noun_id": None, "type": "written", "glosses": {"effect": "efecto", "efecto": "effect"}},
        ],
        "drill_targets": [{"verb": "salir", "pronoun": "tú"}, {"verb": "salir", "pronoun": "yo"}, {"verb": "salir", "pronoun": "él"}, {"verb": "salir", "pronoun": "nosotros"}, {"verb": "salir", "pronoun": "ellas"}, {"verb": "inhibir", "pronoun": "tú"}, {"verb": "inhibir", "pronoun": "yo"}, {"verb": "inhibir", "pronoun": "él"}, {"verb": "inhibir", "pronoun": "nosotros"}, {"verb": "inhibir", "pronoun": "ellas"}],
        "phase_2_config": {
            "description": "Gerund salir + inhibir (-ir) (2/2): salir, inhibir",
            "targets": [{"verb": "salir", "pronoun": "tú"}, {"verb": "salir", "pronoun": "yo"}, {"verb": "salir", "pronoun": "él"}, {"verb": "salir", "pronoun": "nosotros"}, {"verb": "salir", "pronoun": "ellas"}, {"verb": "inhibir", "pronoun": "tú"}, {"verb": "inhibir", "pronoun": "yo"}, {"verb": "inhibir", "pronoun": "él"}, {"verb": "inhibir", "pronoun": "nosotros"}, {"verb": "inhibir", "pronoun": "ellas"}],
        },
        "opener_en": "Are you holding back the urge?",
        "opener_es": "¿Estás inhibiendo el impulso?",
    },

    "grammar_gerund_hablar_caminar_chat": {
        "title": "Gerund — hablar + caminar (-ar) Chat",
        "grammar_level": 18,
        "lesson_number": 2.5,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "caminar"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "gerund",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Gerund hablar + caminar (-ar) chat: hablar, caminar", "targets": [{"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "ella"}, {"verb": "hablar", "pronoun": "nosotras"}, {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "caminar", "pronoun": "tú"}, {"verb": "caminar", "pronoun": "yo"}, {"verb": "caminar", "pronoun": "él"}, {"verb": "caminar", "pronoun": "nosotros"}, {"verb": "caminar", "pronoun": "ellas"}]},
    },

    "grammar_gerund_comer_beber_chat": {
        "title": "Gerund — comer + beber (-er) Chat",
        "grammar_level": 18,
        "lesson_number": 4.5,
        "lesson_type": "conjugation",
        "word_workload": ["comer", "beber"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "gerund",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Gerund comer + beber (-er) chat: comer, beber", "targets": [{"verb": "comer", "pronoun": "yo"}, {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "ella"}, {"verb": "comer", "pronoun": "nosotras"}, {"verb": "comer", "pronoun": "ustedes"}, {"verb": "beber", "pronoun": "tú"}, {"verb": "beber", "pronoun": "yo"}, {"verb": "beber", "pronoun": "él"}, {"verb": "beber", "pronoun": "nosotros"}, {"verb": "beber", "pronoun": "ellas"}]},
    },

    "grammar_gerund_salir_inhibir_chat": {
        "title": "Gerund — salir + inhibir (-ir) Chat",
        "grammar_level": 18,
        "lesson_number": 6.5,
        "lesson_type": "conjugation",
        "word_workload": ["salir", "inhibir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "gerund",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Gerund salir + inhibir (-ir) chat: salir, inhibir", "targets": [{"verb": "salir", "pronoun": "yo"}, {"verb": "salir", "pronoun": "tú"}, {"verb": "salir", "pronoun": "ella"}, {"verb": "salir", "pronoun": "nosotras"}, {"verb": "salir", "pronoun": "ustedes"}, {"verb": "inhibir", "pronoun": "tú"}, {"verb": "inhibir", "pronoun": "yo"}, {"verb": "inhibir", "pronoun": "él"}, {"verb": "inhibir", "pronoun": "nosotros"}, {"verb": "inhibir", "pronoun": "ellas"}]},
    },

    # ── From _gl18_5_output.py ──

"grammar_perfect_tenses_present_perfect_1": {
        "title": "Perfect Tenses — present perfect (hablar + comer) (1/2)",
        "grammar_level": 18.5,
        "lesson_number": 1,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "comer"],
        "video_embed_id": None,
        "drill_type": "conjugation",
        "tense": "perfect",
        "intro_chart": PERFECT_TENSES_PRESENT_INTRO,
        "drill_config": {
            "answers": {
                "hablar": {"yo": "|he hablado", "tú": "|has hablado", "él": "|ha hablado", "ella": "|ha hablado", "usted": "|ha hablado", "nosotros": "|hemos hablado", "nosotras": "|hemos hablado", "ellos": "|han hablado", "ellas": "|han hablado", "ustedes": "|han hablado"},
                "comer": {"yo": "|he comido", "tú": "|has comido", "él": "|ha comido", "ella": "|ha comido", "usted": "|ha comido", "nosotros": "|hemos comido", "nosotras": "|hemos comido", "ellos": "|han comido", "ellas": "|han comido", "ustedes": "|han comido"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I have spoken with the teacher.", "es": "Yo he hablado con el profesor.", "noun_id": None, "type": "written", "glosses": {"teacher": "profesor", "profesor": "teacher"}},
            {"en": "You have spoken very clearly.", "es": "Tú has hablado muy claro.", "noun_id": None, "type": "auditory", "glosses": {"clearly": "claro", "claro": "clearly"}},
            {"en": "She has spoken about the problem.", "es": "Ella ha hablado sobre el problema.", "noun_id": None, "type": "written", "glosses": {"problem": "problema", "problema": "problem"}},
            {"en": "We (f) have spoken a lot today.", "es": "Nosotras hemos hablado mucho hoy.", "noun_id": None, "type": "auditory", "glosses": {"today": "hoy", "hoy": "today"}},
            {"en": "You (pl) have spoken with the students.", "es": "Ustedes han hablado con los estudiantes.", "noun_id": None, "type": "written", "glosses": {"students": "estudiantes", "estudiantes": "students"}},
            {"en": "I have eaten the red apple.", "es": "Yo he comido la manzana roja.", "noun_id": None, "type": "written", "glosses": {"apple": "manzana", "red": "roja", "manzana": "apple", "roja": "red"}},
            {"en": "You have eaten quickly.", "es": "Tú has comido rápido.", "noun_id": None, "type": "auditory", "glosses": {"quickly": "rápido", "rápido": "quickly"}},
            {"en": "She has eaten the fresh bread.", "es": "Ella ha comido el pan fresco.", "noun_id": None, "type": "written", "glosses": {"bread": "pan", "fresh": "fresco", "pan": "bread", "fresco": "fresh"}},
            {"en": "We (f) have eaten at home.", "es": "Nosotras hemos comido en casa.", "noun_id": None, "type": "auditory", "glosses": {"home": "casa", "casa": "home"}},
            {"en": "You (pl) have eaten the big meal.", "es": "Ustedes han comido la comida grande.", "noun_id": None, "type": "written", "glosses": {"meal": "comida", "big": "grande", "comida": "meal", "grande": "big"}},
        ],
        "drill_targets": [{"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "ella"}, {"verb": "hablar", "pronoun": "nosotras"}, {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "comer", "pronoun": "yo"}, {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "ella"}, {"verb": "comer", "pronoun": "nosotras"}, {"verb": "comer", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Perfect Tenses present perfect (hablar + comer) (1/2): hablar, comer",
            "targets": [{"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "ella"}, {"verb": "hablar", "pronoun": "nosotras"}, {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "comer", "pronoun": "yo"}, {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "ella"}, {"verb": "comer", "pronoun": "nosotras"}, {"verb": "comer", "pronoun": "ustedes"}],
        },
        "opener_en": "Have you spoken with him?",
        "opener_es": "¿Has hablado con él?",
    },

    "grammar_perfect_tenses_present_perfect_2": {
        "title": "Perfect Tenses — present perfect (hablar + comer) (2/2)",
        "grammar_level": 18.5,
        "lesson_number": 2,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "comer"],
        "video_embed_id": None,
        "drill_type": "conjugation",
        "tense": "perfect",
        "intro_chart": PERFECT_TENSES_PRESENT_INTRO,
        "drill_config": {
            "answers": {
                "hablar": {"yo": "|he hablado", "tú": "|has hablado", "él": "|ha hablado", "ella": "|ha hablado", "usted": "|ha hablado", "nosotros": "|hemos hablado", "nosotras": "|hemos hablado", "ellos": "|han hablado", "ellas": "|han hablado", "ustedes": "|han hablado"},
                "comer": {"yo": "|he comido", "tú": "|has comido", "él": "|ha comido", "ella": "|ha comido", "usted": "|ha comido", "nosotros": "|hemos comido", "nosotras": "|hemos comido", "ellos": "|han comido", "ellas": "|han comido", "ustedes": "|han comido"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You have spoken Spanish.", "es": "Tú has hablado español.", "noun_id": None, "type": "written", "glosses": {"Spanish": "español", "español": "Spanish"}},
            {"en": "I have spoken with friends.", "es": "Yo he hablado con amigos.", "noun_id": None, "type": "auditory", "glosses": {"friends": "amigos", "amigos": "friends"}},
            {"en": "He has spoken clearly.", "es": "Él ha hablado claramente.", "noun_id": None, "type": "written", "glosses": {"clearly": "claramente", "claramente": "clearly"}},
            {"en": "We (m) have spoken a lot.", "es": "Nosotros hemos hablado mucho.", "noun_id": None, "type": "auditory", "glosses": {"much": "mucho", "mucho": "much"}},
            {"en": "They (f) have spoken softly.", "es": "Ellas han hablado suavemente.", "noun_id": None, "type": "written", "glosses": {"softly": "suavemente", "suavemente": "softly"}},
            {"en": "You have eaten the apples.", "es": "Tú has comido las manzanas.", "noun_id": None, "type": "written", "glosses": {"apples": "manzanas", "manzanas": "apples"}},
            {"en": "I have eaten breakfast.", "es": "Yo he comido el desayuno.", "noun_id": None, "type": "auditory", "glosses": {"breakfast": "desayuno", "desayuno": "breakfast"}},
            {"en": "He has eaten quickly.", "es": "Él ha comido rápido.", "noun_id": None, "type": "written", "glosses": {"quickly": "rápido", "rápido": "quickly"}},
            {"en": "We (m) have eaten well.", "es": "Nosotros hemos comido bien.", "noun_id": None, "type": "auditory", "glosses": {"well": "bien", "bien": "well"}},
            {"en": "They (f) have eaten fruit.", "es": "Ellas han comido fruta.", "noun_id": None, "type": "written", "glosses": {"fruit": "fruta", "fruta": "fruit"}},
        ],
        "drill_targets": [{"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "él"}, {"verb": "hablar", "pronoun": "nosotros"}, {"verb": "hablar", "pronoun": "ellas"}, {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "yo"}, {"verb": "comer", "pronoun": "él"}, {"verb": "comer", "pronoun": "nosotros"}, {"verb": "comer", "pronoun": "ellas"}],
        "phase_2_config": {
            "description": "Perfect Tenses present perfect (hablar + comer) (2/2): hablar, comer",
            "targets": [{"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "él"}, {"verb": "hablar", "pronoun": "nosotros"}, {"verb": "hablar", "pronoun": "ellas"}, {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "yo"}, {"verb": "comer", "pronoun": "él"}, {"verb": "comer", "pronoun": "nosotros"}, {"verb": "comer", "pronoun": "ellas"}],
        },
        "opener_en": "Have you eaten lunch?",
        "opener_es": "¿Has comido el almuerzo?",
    },

    "grammar_perfect_tenses_pluperfect_1": {
        "title": "Perfect Tenses — pluperfect (hablar + vivir) (1/2)",
        "grammar_level": 18.5,
        "lesson_number": 3,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "vivir"],
        "video_embed_id": None,
        "drill_type": "conjugation",
        "tense": "perfect",
        "intro_chart": PERFECT_TENSES_PLUPERFECT_INTRO,
        "drill_config": {
            "answers": {
                "hablar": {"yo": "|había hablado", "tú": "|habías hablado", "él": "|había hablado", "ella": "|había hablado", "usted": "|había hablado", "nosotros": "|habíamos hablado", "nosotras": "|habíamos hablado", "ellos": "|habían hablado", "ellas": "|habían hablado", "ustedes": "|habían hablado"},
                "vivir": {"yo": "|había vivido", "tú": "|habías vivido", "él": "|había vivido", "ella": "|había vivido", "usted": "|había vivido", "nosotros": "|habíamos vivido", "nosotras": "|habíamos vivido", "ellos": "|habían vivido", "ellas": "|habían vivido", "ustedes": "|habían vivido"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "I had spoken Spanish.", "es": "Yo había hablado español.", "noun_id": None, "type": "written", "glosses": {"Spanish": "español", "español": "Spanish"}},
            {"en": "You had spoken clearly.", "es": "Tú habías hablado claramente.", "noun_id": None, "type": "auditory", "glosses": {"clearly": "claramente", "claramente": "clearly"}},
            {"en": "She had spoken softly.", "es": "Ella había hablado suavemente.", "noun_id": None, "type": "written", "glosses": {"softly": "suavemente", "suavemente": "softly"}},
            {"en": "We (f) had spoken a lot.", "es": "Nosotras habíamos hablado mucho.", "noun_id": None, "type": "auditory", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "You (pl) had spoken with friends.", "es": "Ustedes habían hablado con amigos.", "noun_id": None, "type": "written", "glosses": {"friends": "amigos", "amigos": "friends"}},
            {"en": "I had lived in a big city.", "es": "Yo había vivido en una ciudad grande.", "noun_id": None, "type": "written", "glosses": {"city": "ciudad", "big": "grande", "grande": "big", "ciudad": "city"}},
            {"en": "You had lived happily.", "es": "Tú habías vivido felizmente.", "noun_id": None, "type": "auditory", "glosses": {"happily": "felizmente", "felizmente": "happily"}},
            {"en": "She had lived near the beach.", "es": "Ella había vivido cerca de la playa.", "noun_id": None, "type": "written", "glosses": {"beach": "playa", "playa": "beach"}},
            {"en": "We (f) had lived in small houses.", "es": "Nosotras habíamos vivido en casas pequeñas.", "noun_id": None, "type": "auditory", "glosses": {"houses": "casas", "small": "pequeñas", "pequeñas": "small", "casas": "houses"}},
            {"en": "You (pl) had lived many years.", "es": "Ustedes habían vivido muchos años.", "noun_id": None, "type": "written", "glosses": {"years": "años", "many": "muchos", "muchos": "many", "años": "years"}},
        ],
        "drill_targets": [{"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "ella"}, {"verb": "hablar", "pronoun": "nosotras"}, {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "vivir", "pronoun": "yo"}, {"verb": "vivir", "pronoun": "tú"}, {"verb": "vivir", "pronoun": "ella"}, {"verb": "vivir", "pronoun": "nosotras"}, {"verb": "vivir", "pronoun": "ustedes"}],
        "phase_2_config": {
            "description": "Perfect Tenses pluperfect (hablar + vivir) (1/2): hablar, vivir",
            "targets": [{"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "ella"}, {"verb": "hablar", "pronoun": "nosotras"}, {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "vivir", "pronoun": "yo"}, {"verb": "vivir", "pronoun": "tú"}, {"verb": "vivir", "pronoun": "ella"}, {"verb": "vivir", "pronoun": "nosotras"}, {"verb": "vivir", "pronoun": "ustedes"}],
        },
        "opener_en": "Had you spoken to her before?",
        "opener_es": "¿Le habías hablado antes?",
    },

    "grammar_perfect_tenses_pluperfect_2": {
        "title": "Perfect Tenses — pluperfect (hablar + vivir) (2/2)",
        "grammar_level": 18.5,
        "lesson_number": 4,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "vivir"],
        "video_embed_id": None,
        "drill_type": "conjugation",
        "tense": "perfect",
        "intro_chart": PERFECT_TENSES_PLUPERFECT_INTRO,
        "drill_config": {
            "answers": {
                "hablar": {"yo": "|había hablado", "tú": "|habías hablado", "él": "|había hablado", "ella": "|había hablado", "usted": "|había hablado", "nosotros": "|habíamos hablado", "nosotras": "|habíamos hablado", "ellos": "|habían hablado", "ellas": "|habían hablado", "ustedes": "|habían hablado"},
                "vivir": {"yo": "|había vivido", "tú": "|habías vivido", "él": "|había vivido", "ella": "|había vivido", "usted": "|había vivido", "nosotros": "|habíamos vivido", "nosotras": "|habíamos vivido", "ellos": "|habían vivido", "ellas": "|habían vivido", "ustedes": "|habían vivido"},
            },
        },
        "phases": {"0a": True, "0b": True, "1a": False, "1b": False, "1c": False, "2": False, "3": False},
        "phase_1c_config": {"total_items": 5, "mode": "random_pronoun_verb"},
        "drill_sentences": [
            {"en": "You had spoken with the teacher.", "es": "Tú habías hablado con el profesor.", "noun_id": None, "type": "written", "glosses": {"teacher": "profesor", "profesor": "teacher"}},
            {"en": "I had spoken Spanish.", "es": "Yo había hablado español.", "noun_id": None, "type": "auditory", "glosses": {"Spanish": "español", "español": "Spanish"}},
            {"en": "He had spoken clearly.", "es": "Él había hablado claramente.", "noun_id": None, "type": "written", "glosses": {"clearly": "claramente", "claramente": "clearly"}},
            {"en": "We (m) had spoken a lot.", "es": "Nosotros habíamos hablado mucho.", "noun_id": None, "type": "auditory", "glosses": {"a lot": "mucho", "mucho": "a lot"}},
            {"en": "They (f) had spoken softly.", "es": "Ellas habían hablado suavemente.", "noun_id": None, "type": "written", "glosses": {"softly": "suavemente", "suavemente": "softly"}},
            {"en": "You had lived in a big city.", "es": "Tú habías vivido en una ciudad grande.", "noun_id": None, "type": "written", "glosses": {"city": "ciudad", "big": "grande", "ciudad": "city", "grande": "big"}},
            {"en": "I had lived near the beach.", "es": "Yo había vivido cerca de la playa.", "noun_id": None, "type": "auditory", "glosses": {"beach": "playa", "playa": "beach"}},
            {"en": "He had lived in a small house.", "es": "Él había vivido en una casa pequeña.", "noun_id": None, "type": "written", "glosses": {"house": "casa", "small": "pequeña", "casa": "house", "pequeña": "small"}},
            {"en": "We (m) had lived happily.", "es": "Nosotros habíamos vivido felizmente.", "noun_id": None, "type": "auditory", "glosses": {"happily": "felizmente", "felizmente": "happily"}},
            {"en": "They (f) had lived far away.", "es": "Ellas habían vivido lejos.", "noun_id": None, "type": "written", "glosses": {"far away": "lejos", "lejos": "far away"}},
        ],
        "drill_targets": [{"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "él"}, {"verb": "hablar", "pronoun": "nosotros"}, {"verb": "hablar", "pronoun": "ellas"}, {"verb": "vivir", "pronoun": "tú"}, {"verb": "vivir", "pronoun": "yo"}, {"verb": "vivir", "pronoun": "él"}, {"verb": "vivir", "pronoun": "nosotros"}, {"verb": "vivir", "pronoun": "ellas"}],
        "phase_2_config": {
            "description": "Perfect Tenses pluperfect (hablar + vivir) (2/2): hablar, vivir",
            "targets": [{"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "él"}, {"verb": "hablar", "pronoun": "nosotros"}, {"verb": "hablar", "pronoun": "ellas"}, {"verb": "vivir", "pronoun": "tú"}, {"verb": "vivir", "pronoun": "yo"}, {"verb": "vivir", "pronoun": "él"}, {"verb": "vivir", "pronoun": "nosotros"}, {"verb": "vivir", "pronoun": "ellas"}],
        },
        "opener_en": "Had you lived there before?",
        "opener_es": "¿Habías vivido allí antes?",
    },

    "grammar_perfect_tenses_present_perfect_chat": {
        "title": "Perfect Tenses — present perfect (hablar + comer) Chat",
        "grammar_level": 18.5,
        "lesson_number": 2.5,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "comer"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "perfect",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Perfect Tenses present perfect (hablar + comer) chat: hablar, comer", "targets": [{"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "ella"}, {"verb": "hablar", "pronoun": "nosotras"}, {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "comer", "pronoun": "tú"}, {"verb": "comer", "pronoun": "yo"}, {"verb": "comer", "pronoun": "él"}, {"verb": "comer", "pronoun": "nosotros"}, {"verb": "comer", "pronoun": "ellas"}]},
    },

    "grammar_perfect_tenses_pluperfect_chat": {
        "title": "Perfect Tenses — pluperfect (hablar + vivir) Chat",
        "grammar_level": 18.5,
        "lesson_number": 4.5,
        "lesson_type": "conjugation",
        "word_workload": ["hablar", "vivir"],
        "video_embed_id": None,
        "drill_type": "skip",
        "tense": "perfect",
        "phases": {"0a": False, "0b": False, "1a": False, "1b": False, "1c": False, "2": True, "3": False},
        "drill_sentences": [],
        "phase_2_config": {"description": "Perfect Tenses pluperfect (hablar + vivir) chat: hablar, vivir", "targets": [{"verb": "hablar", "pronoun": "yo"}, {"verb": "hablar", "pronoun": "tú"}, {"verb": "hablar", "pronoun": "ella"}, {"verb": "hablar", "pronoun": "nosotras"}, {"verb": "hablar", "pronoun": "ustedes"}, {"verb": "vivir", "pronoun": "tú"}, {"verb": "vivir", "pronoun": "yo"}, {"verb": "vivir", "pronoun": "él"}, {"verb": "vivir", "pronoun": "nosotros"}, {"verb": "vivir", "pronoun": "ellas"}]},
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


def find_any_grammar_form(word_spanish: str) -> str | None:
    """Pick a deployable conjugated form for a verb from any grammar lesson.

    Used as a fallback for the daily Grenade so a verb learned outside a
    grammar lesson (e.g. through a vocab encounter) still surfaces as a
    conjugation rather than the bare infinitive. Walks every conjugation
    lesson's `drill_config.answers`, prefers varied pronouns
    (ella/ellas/nosotras/usted/ustedes) before falling back to any pronoun,
    and strips the `|` rendering pipe.

    Returns None when no grammar lesson conjugates this lemma — caller should
    fall back to the lemma.
    """
    import random as _random
    # Prefer simple single-word conjugations over periphrases
    # (modal/ir-a-inf lessons store values like "va a vivir" or "tengo que comer";
    # those are deployable but a bare conjugation deploys cleaner).
    simple: list[dict[str, str]] = []
    compound: list[dict[str, str]] = []
    for cfg in GRAMMAR_SITUATIONS.values():
        if cfg.get("lesson_type") != "conjugation":
            continue
        answers = (cfg.get("drill_config") or {}).get("answers") or {}
        forms = answers.get(word_spanish)
        if not forms:
            continue
        if any(" " in (v or "") for v in forms.values()):
            compound.append(forms)
        else:
            simple.append(forms)
    pool = simple or compound
    if not pool:
        return None
    forms_for_verb = _random.choice(pool)
    preferred = ["ella", "ellas", "nosotras", "usted", "ustedes", "tú", "yo"]
    candidates = [p for p in preferred if forms_for_verb.get(p)]
    if not candidates:
        candidates = list(forms_for_verb.keys())
    chosen = _random.choice(candidates)
    form = forms_for_verb.get(chosen)
    return form.replace("|", "") if form else None


# ── Chat target forms (English-conjugation chips for grammar chat) ──────────

# Subject pronouns mapped to their English subject form. We use a simple
# default for usted/ustedes ("you" / "you all") rather than "(formal)" so the
# checklist chip stays compact.
_PRONOUN_EN_SUBJECT: dict[str, str] = {
    "yo": "I",
    "tú": "you",
    "él": "he",
    "ella": "she",
    "usted": "you",
    # Always gender-mark plural we/they so the chat chips don't render two
    # identical "we die" labels for nosotros + nosotras (or "they X" for
    # ellos + ellas). The marker travels with the subject everywhere
    # _conjugate_english_present is called.
    "nosotros": "we (m)",
    "nosotras": "we (f)",
    "ellos": "they (m)",
    "ellas": "they (f)",
    "ustedes": "you all",
}

# Hand-curated English conjugations for verbs that don't follow the
# default add-s rule. Keyed by EN lemma (sans "to ").
_EN_CONJ_OVERRIDES: dict[str, dict[str, str]] = {
    "be": {"yo": "I am", "tú": "you are", "él": "he is", "ella": "she is",
           "usted": "you are", "nosotros": "we (m) are", "nosotras": "we (f) are",
           "ellos": "they (m) are", "ellas": "they (f) are", "ustedes": "you all are"},
    "have": {"yo": "I have", "tú": "you have", "él": "he has", "ella": "she has",
             "usted": "you have", "nosotros": "we (m) have", "nosotras": "we (f) have",
             "ellos": "they (m) have", "ellas": "they (f) have", "ustedes": "you all have"},
    "do": {"yo": "I do", "tú": "you do", "él": "he does", "ella": "she does",
           "usted": "you do", "nosotros": "we (m) do", "nosotras": "we (f) do",
           "ellos": "they (m) do", "ellas": "they (f) do", "ustedes": "you all do"},
    "go": {"yo": "I go", "tú": "you go", "él": "he goes", "ella": "she goes",
           "usted": "you go", "nosotros": "we (m) go", "nosotras": "we (f) go",
           "ellos": "they (m) go", "ellas": "they (f) go", "ustedes": "you all go"},
}


def _conjugate_english_present(lemma_en: str, pronoun: str) -> str:
    """Render an English present-tense conjugation for a chat checklist chip.

    Strips a leading "to " from the lemma, applies a tiny set of irregulars,
    else falls back to a regular add-s rule for 3rd person singular.
    """
    base = lemma_en.lower().strip()
    if base.startswith("to "):
        base = base[3:]
    base = base.split("/")[0].strip()  # "to drink/take" → "drink"
    base = base.split(" or ")[0].strip()  # "drink or take" → "drink"
    base = base.split("(")[0].strip()  # "drink (water)" → "drink"

    overrides = _EN_CONJ_OVERRIDES.get(base)
    if overrides and pronoun in overrides:
        return overrides[pronoun]

    # Compound verbs ("be able", "have to", "go out", etc.) — conjugate the
    # head verb via the overrides and append the rest. Without this, "to be
    # worth" came out as "I be worth", "he be worths".
    head, _, rest = base.partition(" ")
    head_overrides = _EN_CONJ_OVERRIDES.get(head)
    if rest and head_overrides and pronoun in head_overrides:
        return f"{head_overrides[pronoun]} {rest}"

    subj = _PRONOUN_EN_SUBJECT.get(pronoun, "you")
    # Spanish 3sg includes usted, but English "you" never takes the -s
    # form ("you die", not "you dies"). Only flex for él / ella.
    is_3sg = pronoun in ("él", "ella")
    if is_3sg:
        if base.endswith(("s", "x", "z", "ch", "sh")):
            verb = f"{base}es"
        elif base.endswith("y") and len(base) > 1 and base[-2] not in "aeiou":
            verb = f"{base[:-1]}ies"
        else:
            verb = f"{base}s"
    else:
        verb = base
    return f"{subj} {verb}"


def get_chat_target_forms(chat_situation_id: str) -> list[dict]:
    """Sample 8 conjugated forms from the 2 preceding drill lessons of a
    grammar chat lesson's sub-block. Used by the conversation API to populate
    the "Use these words to progress" chips with actual drilled conjugations
    instead of the bare infinitives.

    Returns a list of dicts:
        {"verb": "hablar", "pronoun": "tú",
         "spanish": "hablas", "english": "you speak"}

    Returns [] if the chat isn't found, isn't a `_chat`-suffixed lesson, or
    the preceding drills aren't recoverable (caller falls back to the default
    word list in that case).
    """
    import random as _random

    chat = GRAMMAR_SITUATIONS.get(chat_situation_id)
    if not chat or not chat_situation_id.endswith("_chat"):
        return []

    gl = chat.get("grammar_level")
    chat_lesson_num = chat.get("lesson_number")
    if gl is None or chat_lesson_num is None:
        return []

    # The two preceding drill lessons are the two with lesson_number < chat
    # at the same GL, picked closest first.
    siblings = []
    for sid in get_situations_for_gl(gl):
        cfg = GRAMMAR_SITUATIONS.get(sid) or {}
        if cfg.get("drill_type") == "skip":
            continue
        ln = cfg.get("lesson_number")
        if ln is None or ln >= chat_lesson_num:
            continue
        siblings.append((ln, sid, cfg))
    siblings.sort(reverse=True)
    preceding = siblings[:2]
    if not preceding:
        return []

    # Build a candidate pool of (verb, pronoun, spanish_form) triples.
    candidates: list[tuple[str, str, str]] = []
    seen: set[tuple[str, str]] = set()
    for _ln, _sid, cfg in preceding:
        targets = cfg.get("drill_targets") or []
        answers = (cfg.get("drill_config") or {}).get("answers") or {}
        for t in targets:
            verb = t.get("verb")
            pronoun = t.get("pronoun")
            if not verb or not pronoun:
                continue
            form = (answers.get(verb) or {}).get(pronoun)
            if not form:
                continue
            form = form.replace("|", "")
            key = (verb, pronoun)
            if key in seen:
                continue
            seen.add(key)
            candidates.append((verb, pronoun, form))

    if not candidates:
        return []

    # Look up English lemma per verb from GRAMMAR_WORD_TRANSLATIONS.
    sampled = _random.sample(candidates, k=min(8, len(candidates)))
    out = []
    for verb, pronoun, spanish in sampled:
        en_lemma = GRAMMAR_WORD_TRANSLATIONS.get(verb, verb)
        en = _conjugate_english_present(en_lemma, pronoun)
        out.append({
            "verb": verb, "pronoun": pronoun,
            "spanish": spanish, "english": en,
        })
    return out


def _intro_mini_table_verbs(intro: dict | None) -> set[str]:
    """Verbs that have their own mini_table card in the intro deck."""
    if not intro:
        return set()
    return {
        (c.get("title") or "").split(" (", 1)[0].strip()
        for c in (intro.get("cards") or [])
        if c.get("kind") == "mini_table"
    }


def _intro_recall_verbs(intro: dict | None) -> set[str]:
    """Verbs covered by the recall step at the end of the intro deck."""
    if not intro:
        return set()
    recall = intro.get("recall")
    if not recall:
        return set()
    if isinstance(recall, dict):
        recall = [recall]
    return {r.get("verb") for r in recall if r.get("verb")}


def _validate_intro_coverage() -> list[str]:
    """Every conjugation lesson must model every drilled verb in its intro_chart
    — both as a `mini_table` card AND in the `recall` list. The drill no longer
    shows a chart, so the intro is the only place the user sees the conjugations
    before being tested. Skips chat-only lessons and non-conjugation lessons.
    """
    violations: list[str] = []
    for sid, cfg in GRAMMAR_SITUATIONS.items():
        if cfg.get("lesson_type") != "conjugation":
            continue
        if cfg.get("drill_type") == "skip":
            continue
        drilled = set(cfg.get("word_workload") or [])
        if not drilled:
            continue
        intro = cfg.get("intro_chart")
        missing_mt = sorted(drilled - _intro_mini_table_verbs(intro))
        missing_rc = sorted(drilled - _intro_recall_verbs(intro))
        if missing_mt or missing_rc:
            violations.append(
                f"{sid}: drills {sorted(drilled)}; "
                f"intro mini_tables miss {missing_mt}; recall misses {missing_rc}"
            )
    return violations


_intro_coverage_violations = _validate_intro_coverage()
if _intro_coverage_violations:
    raise RuntimeError(
        "grammar_situations.py: intro/drill mismatch — every drilled verb in a "
        "conjugation lesson must appear in its intro_chart's mini_tables AND recall.\n  "
        + "\n  ".join(_intro_coverage_violations)
    )


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
