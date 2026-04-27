"""Scene-anchored cold-open lines for every grammar `*_chat` situation.

Without these, every chat lesson falls through to the FE's generic
"Hello! How can I help you today?" fallback, which gives the learner no
situational anchor and no pressure to deploy the lesson's target words.

Each entry pairs:
  - opener_es / opener_en — the assistant's first line (≤ 15 words, scene-
    grounded, designed so a natural reply uses the lesson's targets).
  - scene             — which character/setting in `situation_roles.GRAMMAR_SCENE_MAP`
    this lesson should map to. The merge step in
    `grammar_situations.py` injects opener_es/opener_en into
    GRAMMAR_SITUATIONS; the scene field is consumed by
    `situation_roles.py` to override the auto-populated `core`.

Edit this file rather than the 12k-line `grammar_situations.py` when
re-tuning openers.
"""

CHAT_OPENERS: dict[str, dict[str, str]] = {
    "grammar_pronouns_chat": {
        "scene": "small_talk",
        "opener_es": "¡Mira esa pareja! Ella es de aquí, ¿y él?",
        "opener_en": "Look at that couple — she's from here, what about him?",
    },
    "grammar_possessive_adj_chat": {
        "scene": "small_talk",
        "opener_es": "Tu perro está en mi jardín otra vez. ¿Es solo tuyo?",
        "opener_en": "Your dog's in my garden again. Is he just yours?",
    },
    "grammar_gender_chat": {
        "scene": "groceries",
        "opener_es": "¿Quiere el aguacate o la manzana? Hoy tengo unos buenos.",
        "opener_en": "Want the avocado or the apple? Got some good ones today.",
    },
    "grammar_regular_present_1_chat": {
        "scene": "small_talk",
        "opener_es": "¿Hablas inglés en casa? ¿Y dónde vives ahora?",
        "opener_en": "Do you speak English at home? Where do you live now?",
    },
    "grammar_regular_present_2_chat": {
        "scene": "small_talk",
        "opener_es": "¿Escuchas música cuando comes? Yo escribo mejor sin ruido.",
        "opener_en": "Do you listen to music while you eat? I write better in silence.",
    },
    "grammar_regular_present_3_chat": {
        "scene": "small_talk",
        "opener_es": "Yo leo todas las noches. ¿Tú cantas o lees antes de dormir?",
        "opener_en": "I read every night. Do you sing or read before bed?",
    },
    "grammar_irregular_present_1_chat": {
        "scene": "small_talk",
        "opener_es": "¡Bienvenido! ¿De dónde eres? ¿Tienes familia aquí?",
        "opener_en": "Welcome! Where are you from? Do you have family here?",
    },
    "grammar_irregular_present_2_chat": {
        "scene": "small_talk",
        "opener_es": "¿A dónde vas hoy? ¿Vienes conmigo al mercado?",
        "opener_en": "Where are you headed today? Want to come to the market with me?",
    },
    "grammar_irregular_present_3_chat": {
        "scene": "small_talk",
        "opener_es": "Te ves cansado. ¿Estás bien? Te doy un café si quieres.",
        "opener_en": "You look tired. You okay? I'll give you a coffee if you want.",
    },
    "grammar_ser_estar_rules_chat": {
        "scene": "small_talk",
        "opener_es": "¿Eres de aquí? Pareces nervioso, ¿estás bien?",
        "opener_en": "Are you from around here? You look nervous — you ok?",
    },
    "grammar_por_para_chat": {
        "scene": "groceries",
        "opener_es": "Esto es para ti. Te lo cobro por los dos kilos, ¿sí?",
        "opener_en": "This is for you. I'll charge you for the two kilos, ok?",
    },
    "grammar_demonstratives_chat": {
        "scene": "clothing",
        "opener_es": "¿Quieres este suéter o ese de allá? Aquella camisa también es bonita.",
        "opener_en": "Want this sweater or that one over there? That shirt across the way is nice too.",
    },
    "grammar_possessive_pronouns_chat": {
        "scene": "small_talk",
        "opener_es": "Aquí están las llaves en la mesa. ¿Cuáles son las tuyas?",
        "opener_en": "Here are the keys on the table. Which ones are yours?",
    },
    "grammar_irregular_present_ii_1_chat": {
        "scene": "contractor",
        "opener_es": "¿Qué hace usted los sábados? ¿Sale temprano de casa?",
        "opener_en": "What do you do on Saturdays? Do you head out early?",
    },
    "grammar_irregular_present_ii_2_chat": {
        "scene": "contractor",
        "opener_es": "¿Oye ese ruido? ¿Le caen bien los obreros que traje ayer?",
        "opener_en": "Hear that noise? Do you like the workers I brought yesterday?",
    },
    "grammar_irregular_present_ii_3_chat": {
        "scene": "small_talk",
        "opener_es": "Cuéntame: ¿qué haces los domingos? ¿Sales con amigos?",
        "opener_en": "Tell me — what do you do on Sundays? Do you go out with friends?",
    },
    "grammar_irregular_present_ii_4_chat": {
        "scene": "small_talk",
        "opener_es": "Oigo música en tu casa todas las noches. ¿Qué pones a esa hora?",
        "opener_en": "I hear music from your place every night. What do you put on at that hour?",
    },
    "grammar_spelling_changes_1_chat": {
        "scene": "contractor",
        "opener_es": "¿Conoce a alguien que construya casas? Yo nunca consigo buenos contratistas.",
        "opener_en": "Know anyone who builds houses? I can never find good contractors.",
    },
    "grammar_spelling_changes_2_chat": {
        "scene": "contractor",
        "opener_es": "Yo dirijo el equipo aquí. ¿Continúa usted con el proyecto o lo paró?",
        "opener_en": "I run the team here. Are you continuing the project or did you stop it?",
    },
    "grammar_spelling_changes_3_chat": {
        "scene": "groceries",
        "opener_es": "Conozco bien a tu mamá. ¿Consigue ella las verduras aquí siempre?",
        "opener_en": "I know your mom well. Does she always get her vegetables here?",
    },
    "grammar_spelling_changes_4_chat": {
        "scene": "small_talk",
        "opener_es": "Te recojo a las ocho, ¿te convence el plan?",
        "opener_en": "I'll pick you up at eight — does the plan work for you?",
    },
    "grammar_saber_conocer_chat": {
        "scene": "small_talk",
        "opener_es": "¿Conoces este barrio? ¿Sabes dónde está la panadería?",
        "opener_en": "Do you know this neighborhood? Do you know where the bakery is?",
    },
    "grammar_present_o_ue_1_chat": {
        "scene": "restaurant",
        "opener_es": "¿Almuerza aquí seguido? Hoy puedo recomendarle el pescado.",
        "opener_en": "Do you eat lunch here often? Today I can recommend the fish.",
    },
    "grammar_present_o_ue_2_chat": {
        "scene": "small_talk",
        "opener_es": "¿A qué hora vuelves a casa? Yo duermo poco últimamente.",
        "opener_en": "What time do you get home? I haven't been sleeping much lately.",
    },
    "grammar_present_o_ue_3_chat": {
        "scene": "small_talk",
        "opener_es": "Me muero de hambre. ¿Almuerzas conmigo si puedes?",
        "opener_en": "I'm starving. Want to grab lunch if you can?",
    },
    "grammar_present_e_ie_1_chat": {
        "scene": "clothing",
        "opener_es": "Cerramos en una hora. ¿Quiere probarse algo más o prefiere pagar?",
        "opener_en": "We close in an hour. Want to try anything else, or you'd rather pay?",
    },
    "grammar_present_e_ie_2_chat": {
        "scene": "small_talk",
        "opener_es": "¿Entiendes el español rápido? Yo pienso que ya lo manejas bien.",
        "opener_en": "Do you follow fast Spanish? I think you handle it well already.",
    },
    "grammar_present_e_ie_3_chat": {
        "scene": "small_talk",
        "opener_es": "Empiezo a trabajar a las nueve. ¿A qué hora prefieres llamar?",
        "opener_en": "I start work at nine. What time would you rather call?",
    },
    "grammar_present_e_i_1_chat": {
        "scene": "restaurant",
        "opener_es": "¿Qué pide usted? El especial siempre lo elige la mayoría.",
        "opener_en": "What are you ordering? Most people pick the special.",
    },
    "grammar_present_e_i_2_chat": {
        "scene": "clothing",
        "opener_es": "¿Cómo te vistes para una fiesta? Yo siempre elijo algo cómodo.",
        "opener_en": "How do you dress for a party? I always pick something comfortable.",
    },
    "grammar_present_e_i_3_chat": {
        "scene": "restaurant",
        "opener_es": "¿Sigue con la dieta? Le sirvo lo de siempre o cambia hoy?",
        "opener_en": "Still on the diet? Should I serve you the usual or you switching today?",
    },
    "grammar_ir_a_inf_1_chat": {
        "scene": "small_talk",
        "opener_es": "¿Qué vas a hacer este finde? Yo voy a dormir mucho.",
        "opener_en": "What are you doing this weekend? I'm going to sleep a lot.",
    },
    "grammar_ir_a_inf_2_chat": {
        "scene": "small_talk",
        "opener_es": "Mañana voy a estudiar todo el día. ¿Tú vas a salir o vas a quedarte?",
        "opener_en": "Tomorrow I'm going to study all day. Are you going out or staying in?",
    },
    "grammar_ir_a_inf_3_chat": {
        "scene": "small_talk",
        "opener_es": "Pronto voy a vivir en otra ciudad. ¿Vas a venir a visitarme?",
        "opener_en": "I'm going to move to another city soon. Are you going to come visit?",
    },
    "grammar_gustar_1_chat": {
        "scene": "restaurant",
        "opener_es": "¿Le gusta el café fuerte? A mí me gusta con leche.",
        "opener_en": "Do you like strong coffee? I like mine with milk.",
    },
    "grammar_gustar_2_chat": {
        "scene": "clothing",
        "opener_es": "Estos zapatos están de moda este año. ¿Le gustan?",
        "opener_en": "These shoes are in style this year. Do you like them?",
    },
    "grammar_gustar_3_chat": {
        "scene": "groceries",
        "opener_es": "Tenemos mangos y una sandía linda. ¿Le gusta la sandía o le gustan los mangos?",
        "opener_en": "We've got mangoes and a beautiful watermelon. Do you like the watermelon or the mangoes?",
    },
    "grammar_imperatives_1_chat": {
        "scene": "small_talk",
        "opener_es": "Estoy súper estresado. Dame tres consejos rápidos.",
        "opener_en": "I'm super stressed. Give me three quick tips.",
    },
    "grammar_imperatives_2_chat": {
        "scene": "small_talk",
        "opener_es": "Mi sobrino está perdido en la vida. ¡Dile algo motivador!",
        "opener_en": "My nephew's lost in life. Tell him something motivating!",
    },
    "grammar_pret_vs_imperfect_chat": {
        "scene": "small_talk",
        "opener_es": "¿Qué hiciste ayer y cómo era el clima esta mañana?",
        "opener_en": "What did you do yesterday, and how was the weather this morning?",
    },
    "grammar_preterite_regular_1_chat": {
        "scene": "small_talk",
        "opener_es": "¿Saliste anoche? Yo encontré un lugar nuevo y comí muy bien.",
        "opener_en": "Did you go out last night? I found a new spot and ate really well.",
    },
    "grammar_preterite_regular_2_chat": {
        "scene": "small_talk",
        "opener_es": "Ayer hablé con tu mamá. ¿Bebiste algo en la fiesta?",
        "opener_en": "I talked to your mom yesterday. Did you drink anything at the party?",
    },
    "grammar_preterite_regular_3_chat": {
        "scene": "small_talk",
        "opener_es": "¿Comiste con tu familia este finde? Yo salí con primos.",
        "opener_en": "Did you eat with your family this weekend? I went out with cousins.",
    },
    "grammar_preterite_irregular_1_chat": {
        "scene": "small_talk",
        "opener_es": "Te vi ayer en el centro. ¿Qué hiciste? ¿Fuiste solo?",
        "opener_en": "I saw you downtown yesterday. What were you up to? Did you go alone?",
    },
    "grammar_preterite_irregular_2_chat": {
        "scene": "small_talk",
        "opener_es": "Anoche dormí pésimo. ¿Tú qué hiciste? ¿Trajiste algo de la fiesta?",
        "opener_en": "I slept terribly last night. What did you do? Did you bring anything from the party?",
    },
    "grammar_preterite_irregular_3_chat": {
        "scene": "small_talk",
        "opener_es": "El sábado fui al cine. ¿Tú qué hiciste? ¿Viste a alguien?",
        "opener_en": "Saturday I went to the movies. What did you do? See anyone?",
    },
    "grammar_preterite_irregular_4_chat": {
        "scene": "small_talk",
        "opener_es": "Casi me morí de la risa anoche. ¿Te dijeron lo que pasó?",
        "opener_en": "I almost died laughing last night. Did they tell you what happened?",
    },
    "grammar_gerund_1_chat": {
        "scene": "small_talk",
        "opener_es": "Estoy caminando al mercado. ¿Tú qué estás haciendo?",
        "opener_en": "I'm walking to the market. What are you up to?",
    },
    "grammar_gerund_2_chat": {
        "scene": "small_talk",
        "opener_es": "Estoy saliendo de casa ahora. ¿Estás bebiendo café o algo?",
        "opener_en": "I'm heading out now. Are you drinking coffee or something?",
    },
    "grammar_gerund_3_chat": {
        "scene": "small_talk",
        "opener_es": "Mi hermana está charlando con tu vecina. ¿Estás escuchando esto?",
        "opener_en": "My sister's chatting with your neighbor. You hearing this?",
    },
    "grammar_gerund_4_chat": {
        "scene": "small_talk",
        "opener_es": "Estoy saliendo a correr. ¿Estás bebiendo agua suficiente últimamente?",
        "opener_en": "I'm heading out for a run. You drinking enough water lately?",
    },
    "grammar_obj_direct_chat": {
        "scene": "groceries",
        "opener_es": "Aquí tienes las manzanas. ¿Las quieres en bolsa o las llevas así?",
        "opener_en": "Here are the apples. Want them in a bag or take them as-is?",
    },
    "grammar_obj_indirect_chat": {
        "scene": "restaurant",
        "opener_es": "Le traigo el menú. ¿Les pido algo de tomar a sus amigos también?",
        "opener_en": "I'll bring you the menu. Should I order drinks for your friends too?",
    },
    "grammar_obj_combined_a_chat": {
        "scene": "restaurant",
        "opener_es": "El postre es para tu novia. ¿Se lo llevo a ella o te lo doy a ti?",
        "opener_en": "The dessert's for your girlfriend. Should I take it to her or give it to you?",
    },
    "grammar_obj_combined_b_chat": {
        "scene": "restaurant",
        "opener_es": "Tenemos dos cafés listos. ¿Se los llevo a la mesa o nos los tomamos en la barra?",
        "opener_en": "Two coffees are ready. Should I bring them to the table or have them at the bar?",
    },
}
