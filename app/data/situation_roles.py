"""Role definitions for AI conversation agents.

Each situation has an ai_role, user_role, and situation_description used to
build the system prompt for voice chat phases 2 & 3.

Grammar situations map to one of the 10 main scenes via GRAMMAR_SCENE_MAP,
and have additional grammar_structure + example prompts.
"""

# ── Main situation roles (keyed by animation_type) ───────────────────────────

SITUATION_ROLES = {
    "airport": {
        "ai_role": "a 40 year old woman who works as an airline check-in agent - meticulous, dry-witted, and unflappable",
        "user_role": "a traveler at the airport",
        "situation_description": "the traveler is checking in for their flight. You are helping them at the airline counter.",
    },
    "banking": {
        "ai_role": "a 40 year old woman who works as a bank teller - poised, methodical, and quietly observant",
        "user_role": "a customer at the bank",
        "situation_description": "the customer needs help with their bank account. You are assisting them at the counter.",
    },
    "clothing": {
        "ai_role": "a younger mother who works as a shop assistant - bubbly, opinionated, and reassuring",
        "user_role": "a customer shopping for clothes",
        "situation_description": "the customer is looking for clothes in your store. You are helping them find what they need.",
    },
    "contractor": {
        "ai_role": "a middle-aged dad who works as a contractor - blunt, resourceful, and oddly philosophical",
        "user_role": "a homeowner hiring a contractor",
        "situation_description": "the homeowner wants work done on their house. You are discussing the renovation project.",
    },
    "groceries": {
        "ai_role": "an early 20s guy who works as a supermarket cashier - laidback, chatty, and surprisingly perceptive",
        "user_role": "a customer at the supermarket",
        "situation_description": "the customer is buying groceries. You are helping them at checkout.",
    },
    "mechanic": {
        "ai_role": "a middle-aged guy who works as a mechanic - gruff, thorough, and unexpectedly tender",
        "user_role": "a customer at the garage",
        "situation_description": "the customer's car is not working correctly. You are talking to the customer in your garage.",
    },
    "police": {
        "ai_role": "a 30 year old woman who works as a police officer - firm, perceptive, and disarmingly calm",
        "user_role": "a driver pulled over",
        "situation_description": "you have pulled over the driver for a routine traffic stop. You are speaking to them through the car window.",
    },
    "restaurant": {
        "ai_role": "a 30 year old man who works as a waiter - charming, attentive, and playfully sarcastic",
        "user_role": "a diner at a restaurant",
        "situation_description": "the diner is ordering food. You are their server for the evening.",
    },
    "small_talk": {
        "ai_role": "a 65 year old woman who is your neighbor - nostalgic, warm-hearted, and delightfully nosy",
        "user_role": "a new resident in the neighborhood",
        "situation_description": "you just met your new neighbor. You are making friendly small talk.",
    },
    "internet": {
        "ai_role": "a nerdy young woman who works as an internet technician - earnest, precise, and endearingly awkward",
        "user_role": "a customer setting up WiFi",
        "situation_description": "the customer needs help setting up their home internet. You are the technician on site.",
    },
    "core": {
        "ai_role": "Eric - a local 31 year old man who is enthusiastic, joyful, and present",
        "user_role": "an expat",
        "situation_description": "you are both standing in a Latin American rainforest during the day.",
    },
}

# ── Grammar situation → main scene mapping ───────────────────────────────────
# Round-robin over 4 scenes matching grammar_a/b/c/d background videos:
#   grammar_a → small_talk,  grammar_b → mechanic,
#   grammar_c → banking,     grammar_d → clothing

GRAMMAR_SCENE_MAP = {
    "grammar_pronouns": "core",
    "grammar_gender": "core",
    "grammar_gustar_1": "core",
    "grammar_gustar_2": "core",
    "grammar_gustar_3": "core",
}
# Auto-populate scene map for multi-lesson grammar situations (all map to "core")
# Matches IDs like grammar_regular_present_1, grammar_irregular_present_2, etc.
from app.data.grammar_situations import GRAMMAR_SITUATIONS as _GS
for _sid in _GS:
    if _sid not in GRAMMAR_SCENE_MAP:
        GRAMMAR_SCENE_MAP[_sid] = "core"

# ── Per-chat-lesson scene overrides (drives the cold-open redesign) ──────────
# Source of truth lives alongside the openers in `grammar_chat_openers.py`.
# Each entry there carries an `opener_es` / `opener_en` AND a `scene`; the
# openers are merged into GRAMMAR_SITUATIONS, the scenes are flipped here.
# Override AFTER the auto-populate so these win over the default `core`.
from app.data.grammar_chat_openers import CHAT_OPENERS as _CHAT_OPENERS
for _sid, _opener in _CHAT_OPENERS.items():
    if _sid in GRAMMAR_SCENE_MAP:
        GRAMMAR_SCENE_MAP[_sid] = _opener["scene"]
del _sid, _opener, _CHAT_OPENERS

# ── Grammar structure definitions ────────────────────────────────────────────
# Each grammar situation has a grammar_structure the user must deploy,
# plus bespoke example questions that naturally elicit that structure.

GRAMMAR_STRUCTURES = {
    "grammar_pronouns": {
        "grammar_structure": "subject pronouns (yo, tú, él, ella, usted, nosotros, ellos, ustedes)",
        "examples": [
            "My wife usually does the gardening but I do the cooking. What about you?",
            "Our kids go to the school down the road. Where do yours go?",
            "My husband and I moved here last year. How long have you lived here?",
        ],
    },
    "grammar_gender": {
        "grammar_structure": "gendered articles (el, la, los, las, un, una)",
        "examples": [
            "I need to check the oil. Can you pop the hood?",
            "The transmission is making a noise. When did it start?",
            "I'll need to order a new part for the engine.",
        ],
    },
    "grammar_regular_present": {
        "grammar_structure": "regular present tense conjugation (-ar, -er, -ir verbs like hablar, comer, vivir)",
        "examples": [
            "How often do you come to this branch?",
            "Do you live near here or do you work in the area?",
            "We open at nine. What time do you usually arrive?",
        ],
    },
    "grammar_irregular_present": {
        "grammar_structure": "irregular present tense (ser, estar, ir, tener, venir, dar)",
        "examples": [
            "This dress is lovely. Are you looking for something for a special occasion?",
            "Do you have your receipt? Where did you get this?",
            "We're going to check in the back. Can you come this way?",
        ],
    },
    "grammar_irregular_present_ii": {
        "grammar_structure": "irregular present tense (hacer, poner, salir, decir, oír, traer, caer, valer)",
        "examples": [
            "What do you usually do on weekends around here?",
            "I always put the recycling out on Tuesdays. When do you put yours out?",
            "My dog makes so much noise. Do you hear him from your place?",
        ],
    },
    "grammar_spelling_changes": {
        "grammar_structure": "spelling-change verbs in present tense (conseguir, conocer, construir, etc.)",
        "examples": [
            "We're trying to get a new alternator. Where do you usually get your parts?",
            "Do you know a good body shop nearby?",
            "They're building a new dealership down the road. Did you know that?",
        ],
    },
    "grammar_present_o_ue": {
        "grammar_structure": "stem-changing verbs O→UE (mover, almorzar, morir, poder, dormir)",
        "examples": [
            "We can move your appointment to Thursday. Can you come in the morning?",
            "Where do you usually eat lunch? We have a break room you can use.",
            "The ATM sometimes dies at night. Does that happen at your branch too?",
        ],
    },
    "grammar_present_e_ie": {
        "grammar_structure": "stem-changing verbs E→IE (cerrar, entender, pensar, querer, preferir)",
        "examples": [
            "We close at eight tonight. Do you want to try anything else before then?",
            "Do you prefer the blue or the green? I think the blue suits you.",
            "I don't understand the return policy. Can you explain it?",
        ],
    },
    "grammar_present_e_i": {
        "grammar_structure": "stem-changing verbs E→I (pedir, repetir, seguir, servir)",
        "examples": [
            "Can you repeat your address for me? I didn't catch the street name.",
            "My kids always ask for ice cream when we walk past the shop. Do yours do that?",
            "I follow the local news group online. Do you follow any neighborhood groups?",
        ],
    },
    "grammar_preterite_regular": {
        "grammar_structure": "regular preterite tense (past tense of -ar, -er, -ir verbs)",
        "examples": [
            "When did you first notice the noise? Did it happen suddenly?",
            "Did you drive here today or did someone drop you off?",
            "I checked the brakes last time. Did you notice any improvement?",
        ],
    },
    "grammar_preterite_irregular": {
        "grammar_structure": "irregular preterite (ser/ir→fui, hacer→hice, decir→dije, tener→tuve, etc.)",
        "examples": [
            "What did you do when the check engine light came on?",
            "Did you go to another mechanic before coming here?",
            "I had a similar problem last week. What did the previous mechanic say?",
        ],
    },
    "grammar_gerund": {
        "grammar_structure": "gerund / present progressive (estar + -ando/-iendo)",
        "examples": [
            "What are you looking for today? Are you shopping for a gift?",
            "I'm checking if we have your size. Are you wearing a medium right now?",
            "The tailor is working on alterations. Are you waiting for something?",
        ],
    },
    "grammar_gustar_1": {
        "grammar_structure": "gustar with singular nouns (me gusta, te gusta, le gusta)",
        "examples": [
            "I love this neighborhood. Do you like living here so far?",
            "My daughter likes the park down the street. Does your family like it?",
            "I like cooking Italian food. What kind of food do you like?",
        ],
    },
    "grammar_gustar_2": {
        "grammar_structure": "gustar with plural nouns (me gustan, te gustan, le gustan)",
        "examples": [
            "Do you like the new brake pads? Some customers prefer the ceramic ones.",
            "I like Japanese cars for reliability. What brands do you like?",
            "Do the warning lights bother you? Some people ignore them.",
        ],
    },
    "grammar_gustar_3": {
        "grammar_structure": "gustar with emphasis pronouns (a mí me gusta, a ti te gusta, a él le gusta)",
        "examples": [
            "I personally prefer to save in a fixed-term account. What about you specifically?",
            "My colleague likes the old system, but I prefer the new one. Which do you prefer?",
            "Some customers like online banking. Do you yourself prefer coming in person?",
        ],
    },
    "grammar_ir_a_inf": {
        "grammar_structure": "ir a + infinitive for near future (voy a hablar, vas a comer, etc.)",
        "examples": [
            "Are you going to try this on? We're going to close soon.",
            "I'm going to check the back for your size. Are you going to wait here?",
            "What are you going to wear it for? We're going to get new stock next week.",
        ],
    },
    "grammar_possessive_adj": {
        "grammar_structure": "possessive adjectives (mi, tu, su, nuestro/nuestra) before nouns",
        "examples": [
            "Is this your card? Or is it your husband's?",
            "Our policies require ID. Do you have yours?",
            "My branch closes early on Fridays. What about your usual one?",
        ],
    },
    "grammar_possessive_pronouns": {
        "grammar_structure": "possessive pronouns (mío, tuyo, suyo, nuestro) standing alone",
        "examples": [
            "This account is mine. Is yours new or established?",
            "The card on the desk — is it yours? Mine is in my wallet.",
            "My signature is here, ours both go on the joint account.",
        ],
    },
    "grammar_demonstratives": {
        "grammar_structure": "demonstratives (este, ese, aquel and feminine/plural variants)",
        "examples": [
            "This avocado is ripe, that one's not. Want this or that?",
            "These tomatoes are local; those over there are imported.",
            "That bread by the window is from yesterday. This here is fresh.",
        ],
    },
    "grammar_ser_estar_rules": {
        "grammar_structure": "ser vs estar (ser = identity / permanent, estar = state / location)",
        "examples": [
            "Are you tired? You look it. Where are you from originally?",
            "This dress is silk, but it's wrinkled — I can steam it. Is it for tonight?",
            "The fitting room's over there. Are you ready to try it on?",
        ],
    },
    "grammar_por_para": {
        "grammar_structure": "por (cause / route / duration / exchange) vs para (recipient / deadline / destination)",
        "examples": [
            "Is this for your wife? You can pay for it by card if you'd like.",
            "We deliver for free for orders over $50. When is it for?",
            "Thanks for waiting. We close for an hour at lunch.",
        ],
    },
    "grammar_saber_conocer": {
        "grammar_structure": "saber (facts / how-to) vs conocer (familiarity with people / places / things)",
        "examples": [
            "Do you know my colleague? She knows the system better than I do.",
            "I know how to check the balance — do you know your account number?",
            "Have you been to our other branch? They know the regulars there.",
        ],
    },
    "grammar_imperfect": {
        "grammar_structure": "imperfect tense for habits / background / ongoing past actions (-aba, -ía endings)",
        "examples": [
            "When I was younger, we used to come here every Sunday. Did you grow up nearby?",
            "We didn't have ATMs back then. How did you used to get cash?",
            "My grandmother always cooked on Sundays. What did your family use to do?",
        ],
    },
    "grammar_future": {
        "grammar_structure": "simple future tense (-é, -ás, -á, -emos, -án; irregular roots tendr-, har-, dir-, etc.)",
        "examples": [
            "Will you be paying with this card? I'll process it now.",
            "We'll have the new stock by Tuesday. What size will you need?",
            "I'll call when it arrives. When will you be in the area?",
        ],
    },
    "grammar_conditional": {
        "grammar_structure": "conditional tense for hypotheticals / polite requests (-ía, -ías, etc.)",
        "examples": [
            "Could you sign here, please? I would also need a second ID.",
            "What would you do if you got a third card? Would you still keep this one?",
            "Would it be possible to come back tomorrow? It would be quicker.",
        ],
    },
    "grammar_subj_pres": {
        "grammar_structure": "present subjunctive after que / cuando / espero que / etc. (-e/-a opposite-vowel endings)",
        "examples": [
            "I hope you have a good experience. Want me to walk you through the menu?",
            "When you're ready, just let me know. We don't want anyone to feel rushed.",
            "It's important that you know we serve this fresh. Anything you'd like us to recommend?",
        ],
    },
    "grammar_subj_impf": {
        "grammar_structure": "imperfect subjunctive for past hypothesis / si-clauses (-ara, -iera endings)",
        "examples": [
            "If I were you, I'd take the lobster. What would you order if money were no object?",
            "I wish you had told me you were vegetarian. Would you like me to bring something else?",
            "If we had known you were coming, we'd have set a better table.",
        ],
    },
    "grammar_imperatives": {
        "grammar_structure": "tú affirmative imperative (3rd-person form for regulars; ten/ven/pon/sal/di/haz/ve/sé for irregulars) and usted (subjunctive)",
        "examples": [
            "Open the hood and tell me what you hear when I rev it.",
            "Come back next week. Bring the receipt.",
            "Listen to this — does it sound like the noise you described?",
        ],
    },
    "grammar_reflexive": {
        "grammar_structure": "reflexive verbs with me/te/se/nos pronouns (levantarse, ducharse, vestirse, sentirse)",
        "examples": [
            "What time do you usually wake up? My alarm goes off at six.",
            "I get dressed in five minutes flat. How long does it take you?",
            "Does the new neighbor introduce himself, or does he keep to himself?",
        ],
    },
    "grammar_obj_direct": {
        "grammar_structure": "direct object pronouns (lo, la, los, las) replacing the thing receiving the action",
        "examples": [
            "I have the receipt — do you want it? I can leave it here.",
            "These keys — are they yours? I found them in the parking lot.",
            "The shirt fits well. Are you taking it or leaving it?",
        ],
    },
    "grammar_obj_indirect": {
        "grammar_structure": "indirect object pronouns (me, te, le, nos, les) for the recipient of an action",
        "examples": [
            "I gave him the change. Did he give you the receipt back?",
            "We're sending you a confirmation. Did the bank tell you the timeline?",
            "I'll bring you a sample. Does this work for you?",
        ],
    },
    "grammar_obj_combined": {
        "grammar_structure": "combined indirect + direct object pronouns (te lo, me la, se lo) — IO before DO",
        "examples": [
            "I'll bring it to you tomorrow. Did they send it to you already?",
            "She gave it to him last week. Have you given them yours?",
            "Bring it to me when you get a chance. I'll explain it to you then.",
        ],
    },
    "grammar_pret_vs_imperfect": {
        "grammar_structure": "preterite (completed event) vs imperfect (ongoing/habitual past) contrast",
        "examples": [
            "I was driving when the alarm went off. What were you doing when it happened?",
            "We always closed at six, but yesterday we stayed late. Did you used to come in?",
            "She was crossing the street when the car hit her. Did you see what happened?",
        ],
    },
    "grammar_pret_spelling": {
        "grammar_structure": "preterite spelling-change yo forms (-gué, -qué, -cé) for -gar / -car / -zar verbs",
        "examples": [
            "I paid the deposit yesterday. Did you also pay yours?",
            "I started the engine — it sputtered. When did the issue start for you?",
            "I parked just outside. Where did you park?",
        ],
    },
    "grammar_pret_strong": {
        "grammar_structure": "preterite strong-stem irregulars (tuv-, pus-, hic-, dij-, quis-, vin-) with -e/-iste/-o endings",
        "examples": [
            "I had to call backup yesterday. Did you have any incidents on your shift?",
            "I put the report on your desk. Where did you put yours?",
            "We did the inspection at noon. What did you do during the wait?",
        ],
    },
    "grammar_pret_ducir": {
        "grammar_structure": "preterite -ducir verbs (produj-, traduj-, conduj-) — strong stem with -j-",
        "examples": [
            "I drove all night. Did you drive yourself or take a cab?",
            "We translated the manual last spring. Have you translated documents before?",
            "The factory produced 500 units this quarter. How many did yours produce?",
        ],
    },
    "grammar_pret_e_to_i": {
        "grammar_structure": "preterite e→i / o→u stem changes in 3rd person (pidió, sirvió, durmió)",
        "examples": [
            "He asked for the menu twice. Did you order yet?",
            "She slept the whole flight. Did you sleep on the plane?",
            "They served fish last night. What did you serve at home?",
        ],
    },
    "grammar_gerund": {
        "grammar_structure": "gerund / present participle (-ando, -iendo) for ongoing actions, often with estar",
        "examples": [
            "What are you reading these days? I'm working through a thriller.",
            "Are you waiting for someone? I'm just looking around.",
            "She's living abroad now — what is she doing there?",
        ],
    },
    "grammar_perfect_tenses": {
        "grammar_structure": "perfect tenses (haber + past participle) — present perfect (he hablado) and pluperfect (había hablado)",
        "examples": [
            "Have you eaten here before? We've added new dishes this season.",
            "I had already ordered when she arrived. Have you been to the new place?",
            "We had lived in three cities before settling here. Have you moved a lot?",
        ],
    },
    "grammar_obj": {
        "grammar_structure": "object pronouns (direct lo/la/los/las, indirect me/te/le/nos/les, and combined te lo / se la)",
        "examples": [
            "I'll send it to you tomorrow. Did they bring it to you?",
            "Give me the receipt and I'll process it. Have you paid for it yet?",
            "She told us about it. Have you told them yet?",
        ],
    },
    "grammar_modal": {
        "grammar_structure": "modal helpers + infinitive: tener que (have to), me toca (it's my turn), necesitar (need to)",
        "examples": [
            "I have to renew this card. What do you need to take care of today?",
            "It's my turn to clean the office on Fridays. Whose turn is it at home?",
            "We need to verify your address. Do you have proof of residence?",
        ],
    },
}


def get_roles_for_situation(animation_type: str, situation_id: str = "") -> dict:
    """Get ai_role, user_role, situation_description for any situation.

    For grammar situations (animation_type='grammar'), looks up the scene
    via GRAMMAR_SCENE_MAP and returns roles from the mapped main situation.
    """
    if animation_type == "grammar" and situation_id in GRAMMAR_SCENE_MAP:
        mapped_scene = GRAMMAR_SCENE_MAP[situation_id]
        return SITUATION_ROLES.get(mapped_scene, SITUATION_ROLES["small_talk"])
    return SITUATION_ROLES.get(animation_type, SITUATION_ROLES["small_talk"])


def get_grammar_structure(situation_id: str) -> dict | None:
    """Get grammar_structure and examples for a grammar situation, or None."""
    return GRAMMAR_STRUCTURES.get(situation_id)
