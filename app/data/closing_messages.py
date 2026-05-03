"""Per-scene closing messages used to wrap up encounters cleanly.

When the student ticks the last chip of an encounter, the avatar's
normal v3 prompt still forces a turn-closing question (`?`) — that's
the TURN-CLOSING RULE in `prompts.json`. The result is a wasted extra
question after the lesson is functionally over: the avatar says
"¿Quiere algo más?" or similar, the student is left with nothing to
say, and the encounter end feels abrupt.

The fix is to bypass the LLM entirely on the wrap-up turn and have
the avatar read aloud one of these canned closings instead. Each
animation_type has multiple variants so consecutive replays of the
same situation don't collapse to the same closing line.

Languages supported here: Spanish (default), Catalan, Swedish — same
set the rest of the BE handles via `alt_language`. `core` is
intentionally short and generic since the legacy `core` situation
isn't a roleplay; `grammar` is short for the same reason.

Adding a new animation_type:
  1. Add a key to every language's dict below.
  2. Provide >= 3 messages per language.
  3. Each message must end on `.` or `!` — never `?` (the whole
     point is to stop asking).
  4. Run `pytest tests/test_closing_messages.py --noconftest`; the
     coverage test will catch missing entries.
"""
from __future__ import annotations


_AIRPORT_ES = [
    "¡Perfecto! Todo en orden. Que tenga un excelente vuelo.",
    "Listo. Su tarjeta de embarque está confirmada. ¡Buen viaje!",
    "¡Excelente! Diríjase a la puerta cuando esté listo.",
    "Perfecto, ya está todo. Que disfrute mucho su viaje.",
    "Listo. ¡Buen vuelo y gracias por volar con nosotros!",
]

_BANKING_ES = [
    "Listo. Gracias por venir y que tenga un buen día.",
    "¡Perfecto! Su transacción está completa. Hasta luego.",
    "Todo en orden. ¡Que tenga una excelente jornada!",
    "Gracias por su visita. ¡Hasta la próxima!",
    "¡Listo! Avísenos si necesita algo más.",
]

_CLOTHING_ES = [
    "¡Perfecto! Le va a quedar genial. Pase por caja cuando esté listo.",
    "¡Excelente elección! Hasta pronto.",
    "Listo. ¡Que disfrute mucho su nueva compra!",
    "Gracias por venir. ¡Vuelva pronto!",
    "¡Buena elección! Que tenga un excelente día.",
]

_CONTRACTOR_ES = [
    "Perfecto. Le confirmo los detalles por mensaje. ¡Hasta luego!",
    "Listo. Empezamos cuando me confirme. ¡Hasta pronto!",
    "Excelente. Cualquier cosa, me llama. Que tenga buen día.",
    "Listo, todo claro. Nos vemos.",
    "¡Perfecto! Le mando un mensaje en la semana.",
]

_CORE_ES = [
    "¡Genial! Hasta pronto.",
    "Listo. ¡Que tenga un excelente día!",
    "¡Perfecto! Nos vemos.",
    "Excelente. ¡Hasta luego!",
    "Listo, gracias.",
]

_GROCERIES_ES = [
    "Listo. ¡Que tenga un buen día!",
    "Gracias por venir. ¡Hasta luego!",
    "Perfecto. ¡Buen provecho!",
    "Listo. ¡Vuelva pronto!",
    "¡Que disfrute! Hasta pronto.",
]

_INTERNET_ES = [
    "Listo. El técnico le llamará para coordinar. ¡Gracias!",
    "Perfecto. Recibirá un mensaje con la cita. Hasta luego.",
    "Listo. ¡Le agradezco la llamada!",
    "Excelente. Cualquier consulta, llámenos. Hasta pronto.",
    "Gracias por contactarnos. ¡Que tenga buen día!",
]

_MECHANIC_ES = [
    "Listo. Se lo dejo arreglado. ¡Hasta luego!",
    "Perfecto. Le aviso cuando esté listo el auto.",
    "Excelente. Pase mañana a recogerlo.",
    "Listo. Cualquier cosa, me llama. Hasta pronto.",
    "Gracias. ¡Que tenga buen día!",
]

_POLICE_ES = [
    "Tenga cuidado en la carretera. Buen día.",
    "Listo. Conduzca con precaución. Hasta luego.",
    "Esté atento a las señales. Buen viaje.",
    "Manéjese con cuidado. Buen día.",
    "Hasta luego. Conduzca seguro.",
]

_RESTAURANT_ES = [
    "¡Perfecto! Enseguida le traigo todo. ¡Buen provecho!",
    "Listo. Disfrute mucho. ¡Hasta luego!",
    "Excelente elección. ¡Que disfrute la comida!",
    "Listo. ¡Vuelva pronto!",
    "Gracias por su visita. ¡Que tenga buen día!",
]

_SMALL_TALK_ES = [
    "¡Qué gusto verla! Hasta pronto.",
    "¡Que tenga un excelente día! Hasta luego.",
    "Buenísimo charlar con usted. ¡Nos vemos!",
    "¡Cuídese mucho! Hasta la próxima.",
    "¡Hasta pronto! Que ande bien.",
]

_GRAMMAR_ES = [
    "¡Perfecto! Lo hicimos bien.",
    "Listo, ¡buen trabajo!",
    "¡Excelente! Hasta la próxima.",
    "Bien hecho. Nos vemos.",
    "¡Buen trabajo!",
]

CLOSING_MESSAGES_ES: dict[str, list[str]] = {
    "airport": _AIRPORT_ES,
    "banking": _BANKING_ES,
    "clothing": _CLOTHING_ES,
    "contractor": _CONTRACTOR_ES,
    "core": _CORE_ES,
    "groceries": _GROCERIES_ES,
    "internet": _INTERNET_ES,
    "mechanic": _MECHANIC_ES,
    "police": _POLICE_ES,
    "restaurant": _RESTAURANT_ES,
    "small_talk": _SMALL_TALK_ES,
    "grammar": _GRAMMAR_ES,
}


# Catalan and Swedish banks mirror the Spanish structure key-for-key
# so the picker can fall back to ES if a translation isn't filled in.
# The opening pre-generation script already supports per-language
# audio; the closing picker uses the same `alt_language` parameter.

CLOSING_MESSAGES_CA: dict[str, list[str]] = {
    "airport": [
        "Perfecte! Tot a punt. Que tingui un bon vol!",
        "Llest. La seva targeta d'embarcament està confirmada. Bon viatge!",
        "Excel·lent! Dirigeixi's a la porta quan estigui llest.",
    ],
    "banking": [
        "Llest. Gràcies per venir, que tingui un bon dia!",
        "Perfecte! La seva transacció està completa. Fins aviat.",
        "Tot en ordre. Que tingui una excel·lent jornada!",
    ],
    "clothing": [
        "Perfecte! Li quedarà genial. Passi per caixa quan estigui llest.",
        "Excel·lent elecció! Fins aviat.",
        "Llest. Que gaudeixi de la seva nova compra!",
    ],
    "contractor": [
        "Perfecte. Li confirmo els detalls per missatge. Fins aviat!",
        "Llest. Comencem quan em confirmi. Fins aviat!",
        "Excel·lent. Qualsevol cosa, em truca. Bon dia.",
    ],
    "core": [
        "Genial! Fins aviat.",
        "Llest. Que tingui un excel·lent dia!",
        "Perfecte! Ens veiem.",
    ],
    "groceries": [
        "Llest. Que tingui un bon dia!",
        "Gràcies per venir. Fins aviat!",
        "Perfecte. Bon profit!",
    ],
    "internet": [
        "Llest. El tècnic li trucarà per coordinar. Gràcies!",
        "Perfecte. Rebrà un missatge amb la cita. Fins aviat.",
        "Llest. Li agraeixo la trucada!",
    ],
    "mechanic": [
        "Llest. Li ho deixo arreglat. Fins aviat!",
        "Perfecte. Li aviso quan estigui llest el cotxe.",
        "Excel·lent. Passi demà a recollir-lo.",
    ],
    "police": [
        "Tingui cura a la carretera. Bon dia.",
        "Llest. Condueixi amb precaució. Fins aviat.",
        "Estigui atent als senyals. Bon viatge.",
    ],
    "restaurant": [
        "Perfecte! De seguida li porto tot. Bon profit!",
        "Llest. Gaudeixi molt. Fins aviat!",
        "Excel·lent elecció. Que gaudeixi del menjar!",
    ],
    "small_talk": [
        "Quin gust veure-la! Fins aviat.",
        "Que tingui un excel·lent dia! Fins aviat.",
        "Molt bé xerrar amb vostè. Ens veiem!",
    ],
    "grammar": [
        "Perfecte! Ho hem fet bé.",
        "Llest, bon treball!",
        "Excel·lent! Fins la pròxima.",
    ],
}

CLOSING_MESSAGES_SV: dict[str, list[str]] = {
    "airport": [
        "Perfekt! Allt är klart. Ha en bra flygresa!",
        "Klart. Ditt boardingkort är bekräftat. Trevlig resa!",
        "Utmärkt! Gå till gaten när du är redo.",
    ],
    "banking": [
        "Klart. Tack för besöket, ha en bra dag!",
        "Perfekt! Din transaktion är klar. Hej då.",
        "Allt i ordning. Ha en utmärkt dag!",
    ],
    "clothing": [
        "Perfekt! Det kommer passa bra. Gå till kassan när du är redo.",
        "Utmärkt val! Vi ses.",
        "Klart. Hoppas du njuter av ditt nya köp!",
    ],
    "contractor": [
        "Perfekt. Jag bekräftar detaljerna via meddelande. Vi ses!",
        "Klart. Vi börjar när du bekräftar. Vi ses!",
        "Utmärkt. Ring mig vid behov. Ha en bra dag.",
    ],
    "core": [
        "Toppen! Vi ses.",
        "Klart. Ha en utmärkt dag!",
        "Perfekt! Vi ses.",
    ],
    "groceries": [
        "Klart. Ha en bra dag!",
        "Tack för besöket. Hej då!",
        "Perfekt. Smaklig måltid!",
    ],
    "internet": [
        "Klart. Teknikern ringer för att boka tid. Tack!",
        "Perfekt. Du får ett meddelande med tiden. Hej då.",
        "Klart. Tack för samtalet!",
    ],
    "mechanic": [
        "Klart. Jag lagar den åt dig. Vi ses!",
        "Perfekt. Jag hör av mig när bilen är klar.",
        "Utmärkt. Kom imorgon och hämta den.",
    ],
    "police": [
        "Var försiktig på vägen. Ha en bra dag.",
        "Klart. Kör försiktigt. Hej då.",
        "Var uppmärksam på skyltarna. Trevlig resa.",
    ],
    "restaurant": [
        "Perfekt! Jag kommer strax med allt. Smaklig måltid!",
        "Klart. Njut av maten. Vi ses!",
        "Utmärkt val. Hoppas det smakar!",
    ],
    "small_talk": [
        "Så trevligt att se dig! Vi ses.",
        "Ha en utmärkt dag! Hej då.",
        "Riktigt trevligt att prata. Vi ses!",
    ],
    "grammar": [
        "Perfekt! Vi gjorde det bra.",
        "Klart, bra jobbat!",
        "Utmärkt! Tills nästa gång.",
    ],
}

# Generic safety net for animation_types that aren't in the table —
# returns Spanish since that's the canonical practice language.
GENERIC_CLOSING_ES: list[str] = [
    "¡Buen trabajo! Hasta pronto.",
    "Listo. ¡Hasta luego!",
    "¡Excelente! Nos vemos.",
]


# Per-language dispatch table consumed by the picker service. Adding a
# new language means: (1) add the locale dict above with the same keys
# as CLOSING_MESSAGES_ES, (2) add an entry here, (3) extend the
# `alt_language_service.get_target_language_name` table.
CLOSING_BANKS: dict[str, dict[str, list[str]]] = {
    "es": CLOSING_MESSAGES_ES,
    "catalan": CLOSING_MESSAGES_CA,
    "swedish": CLOSING_MESSAGES_SV,
}
