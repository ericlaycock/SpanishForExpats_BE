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
    # GL 3 (Regular Present) — split into AR / ER / IR sub-blocks
    "grammar_regular_present_ar_chat": {
        "scene": "small_talk",
        "opener_es": "¿Hablas inglés en casa? ¿Escuchas música o las noticias?",
        "opener_en": "Do you speak English at home? Do you listen to music or the news?",
    },
    "grammar_regular_present_er_chat": {
        "scene": "small_talk",
        "opener_es": "¿Bebes café o té? ¿Comes mucho a esta hora?",
        "opener_en": "Do you drink coffee or tea? Do you eat much around this time?",
    },
    "grammar_regular_present_ir_chat": {
        "scene": "small_talk",
        "opener_es": "¿Dónde vives? ¿Escribes mensajes o cartas?",
        "opener_en": "Where do you live? Do you write messages or letters?",
    },

    # GL 4 (Irregular Present I) — split into ser+estar / ir+dar / tener+venir
    "grammar_irregular_present_ser_estar_chat": {
        "scene": "small_talk",
        "opener_es": "¿De dónde eres? ¿Estás cansado del viaje?",
        "opener_en": "Where are you from? Are you tired from the trip?",
    },
    "grammar_irregular_present_ir_dar_chat": {
        "scene": "small_talk",
        "opener_es": "¿A dónde vas hoy? ¿Le das el regalo a tu hermano?",
        "opener_en": "Where are you going today? Are you giving the gift to your brother?",
    },
    "grammar_irregular_present_tener_venir_chat": {
        "scene": "small_talk",
        "opener_es": "¿Tienes familia aquí? ¿Vienes mucho al mercado?",
        "opener_en": "Do you have family here? Do you come to the market often?",
    },

    # NOTE: the old GL 3/4 chat keys above are retired — they no longer
    # appear in GRAMMAR_SITUATIONS. New keys above replace them.
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

    # ── Phase C.3 sub-block chat openers ──
    # GL 4.5 Irregular Present II
    "grammar_irregular_present_ii_hacer_poner_chat": {
        "scene": "small_talk",
        "opener_es": "¿Qué haces los fines de semana? Yo pongo música y descanso.",
        "opener_en": "What do you do on weekends? I put on music and relax.",
    },
    "grammar_irregular_present_ii_salir_decir_chat": {
        "scene": "small_talk",
        "opener_es": "¿Sales mucho los viernes? Mis amigos siempre dicen que sí.",
        "opener_en": "Do you go out a lot on Fridays? My friends always say yes.",
    },
    "grammar_irregular_present_ii_oir_caer_chat": {
        "scene": "small_talk",
        "opener_es": "¿Oyes ese ruido? Algo se cae en la calle todas las noches.",
        "opener_en": "Do you hear that noise? Something falls in the street every night.",
    },
    "grammar_irregular_present_ii_traer_valer_chat": {
        "scene": "groceries",
        "opener_es": "¿Trae su bolsa? La fruta de hoy vale la pena.",
        "opener_en": "Did you bring your bag? Today's fruit is worth it.",
    },

    # GL 5 Spelling Changes
    "grammar_spelling_changes_conocer_producir_chat": {
        "scene": "contractor",
        "opener_es": "¿Conoce a alguien que produzca buenos materiales? Necesitamos un proveedor nuevo.",
        "opener_en": "Do you know anyone who produces good materials? We need a new supplier.",
    },
    "grammar_spelling_changes_construir_conseguir_chat": {
        "scene": "contractor",
        "opener_es": "¿Construye casas usted? Yo no consigo un buen contratista por aquí.",
        "opener_en": "Do you build houses? I can't find a good contractor around here.",
    },
    "grammar_spelling_changes_recoger_dirigir_chat": {
        "scene": "small_talk",
        "opener_es": "Yo dirijo el coro del barrio. ¿Recoges a los niños del colegio hoy?",
        "opener_en": "I run the neighborhood choir. Are you picking up the kids from school today?",
    },
    "grammar_spelling_changes_convencer_continuar_chat": {
        "scene": "small_talk",
        "opener_es": "¿Te convenzo de continuar con el plan? La idea es buena.",
        "opener_en": "Can I convince you to keep going with the plan? The idea's a good one.",
    },

    # GL 6 o→ue
    "grammar_present_o_ue_poder_volver_chat": {
        "scene": "small_talk",
        "opener_es": "¿Puedes volver el sábado? Yo no puedo trabajar ese día.",
        "opener_en": "Can you come back on Saturday? I can't work that day.",
    },
    "grammar_present_o_ue_dormir_morir_chat": {
        "scene": "small_talk",
        "opener_es": "Me muero de sueño hoy. ¿Duermes bien tú últimamente?",
        "opener_en": "I'm dying of sleepiness today. Have you been sleeping well lately?",
    },
    "grammar_present_o_ue_mover_almorzar_chat": {
        "scene": "restaurant",
        "opener_es": "¿Almuerza a esta hora siempre? Yo muevo el almuerzo según el día.",
        "opener_en": "Do you always have lunch at this time? I move my lunch around depending on the day.",
    },

    # GL 7 e→ie
    "grammar_present_e_ie_querer_pensar_chat": {
        "scene": "restaurant",
        "opener_es": "¿Qué quiere hoy? Pienso que el plato del día está rico.",
        "opener_en": "What do you want today? I think the daily special is good.",
    },
    "grammar_present_e_ie_cerrar_empezar_chat": {
        "scene": "small_talk",
        "opener_es": "Cerramos a las ocho. ¿A qué hora empiezas tú mañana?",
        "opener_en": "We close at eight. What time do you start tomorrow?",
    },
    "grammar_present_e_ie_entender_preferir_chat": {
        "scene": "clothing",
        "opener_es": "¿Entiende la talla europea? ¿Prefiere probarse el rojo o el azul?",
        "opener_en": "Do you understand European sizing? Would you rather try the red or the blue?",
    },

    # GL 8 e→i
    "grammar_present_e_i_pedir_servir_chat": {
        "scene": "restaurant",
        "opener_es": "¿Qué pide hoy? Le sirvo lo de siempre si quiere.",
        "opener_en": "What are you ordering today? I'll serve you the usual if you want.",
    },
    "grammar_present_e_i_repetir_seguir_chat": {
        "scene": "small_talk",
        "opener_es": "Repito la pregunta: ¿sigues con el mismo plan o cambiaste?",
        "opener_en": "Let me repeat the question — are you sticking with the plan or did you change it?",
    },
    "grammar_present_e_i_vestir_elegir_chat": {
        "scene": "clothing",
        "opener_es": "¿Cómo se viste para el trabajo? Yo elijo algo cómodo siempre.",
        "opener_en": "How do you dress for work? I always pick something comfortable.",
    },

    # GL 9 ir + a + infinitive
    "grammar_ir_a_inf_hablar_comer_chat": {
        "scene": "restaurant",
        "opener_es": "¿Va a comer aquí hoy? Voy a hablar con el chef sobre el especial.",
        "opener_en": "Are you going to eat here today? I'm going to talk to the chef about the special.",
    },
    "grammar_ir_a_inf_vivir_escribir_chat": {
        "scene": "small_talk",
        "opener_es": "¿Vas a vivir aquí mucho tiempo? Yo voy a escribir un libro sobre el barrio.",
        "opener_en": "Are you going to live here long? I'm going to write a book about the neighborhood.",
    },
    "grammar_ir_a_inf_dormir_estudiar_chat": {
        "scene": "small_talk",
        "opener_es": "Esta noche voy a dormir temprano. ¿Vas a estudiar mañana?",
        "opener_en": "Tonight I'm going to sleep early. Are you going to study tomorrow?",
    },

    # GL 13.5 Imperatives
    "grammar_imperatives_hablar_comer_chat": {
        "scene": "restaurant",
        "opener_es": "Habla con el chef y come algo rico. ¿Listo para pedir?",
        "opener_en": "Talk to the chef and eat something tasty. Ready to order?",
    },
    "grammar_imperatives_tener_venir_chat": {
        "scene": "small_talk",
        "opener_es": "Ten paciencia y ven mañana, ¿vale? Hoy estoy ocupada.",
        "opener_en": "Be patient and come back tomorrow, ok? I'm busy today.",
    },

    # GL 17 Preterite Regular
    "grammar_preterite_regular_hablar_encontrar_chat": {
        "scene": "small_talk",
        "opener_es": "¿Hablaste con la vecina ayer? Yo encontré las llaves perdidas.",
        "opener_en": "Did you talk to the neighbor yesterday? I found the lost keys.",
    },
    "grammar_preterite_regular_comer_beber_chat": {
        "scene": "restaurant",
        "opener_es": "¿Qué comió ayer aquí? Bebimos un vino muy rico anoche.",
        "opener_en": "What did you eat here yesterday? We had a really nice wine last night.",
    },
    "grammar_preterite_regular_salir_unir_chat": {
        "scene": "small_talk",
        "opener_es": "¿Saliste el fin de semana? Toda la familia se unió en mi casa.",
        "opener_en": "Did you go out over the weekend? The whole family got together at my place.",
    },

    # GL 17.1 Preterite Highly Irregular
    "grammar_preterite_irregular_ser_ir_chat": {
        "scene": "small_talk",
        "opener_es": "¿Adónde fuiste de vacaciones? El año pasado fui a la costa.",
        "opener_en": "Where did you go on vacation? Last year I went to the coast.",
    },
    "grammar_preterite_irregular_dar_ver_chat": {
        "scene": "small_talk",
        "opener_es": "¿Viste el partido anoche? Yo le di mi entrada a un amigo.",
        "opener_en": "Did you see the game last night? I gave my ticket to a friend.",
    },
    "grammar_preterite_irregular_hacer_decir_chat": {
        "scene": "small_talk",
        "opener_es": "¿Qué hiciste el sábado? Mi hijo me dijo algo raro.",
        "opener_en": "What did you do on Saturday? My son told me something strange.",
    },
    "grammar_preterite_irregular_traer_dormir_chat": {
        "scene": "small_talk",
        "opener_es": "¿Dormiste bien anoche? Mi vecino trajo música hasta tarde.",
        "opener_en": "Did you sleep well last night? My neighbor brought music until late.",
    },

    # GL 18 Gerund
    "grammar_gerund_hablar_caminar_chat": {
        "scene": "small_talk",
        "opener_es": "Estoy hablando con todos los vecinos hoy. ¿Estás caminando mucho últimamente?",
        "opener_en": "I'm talking to all the neighbors today. Are you walking a lot lately?",
    },
    "grammar_gerund_comer_beber_chat": {
        "scene": "restaurant",
        "opener_es": "¿Qué está comiendo? Estoy bebiendo el vino que me recomendó.",
        "opener_en": "What are you eating? I'm drinking the wine you recommended.",
    },
    "grammar_gerund_salir_inhibir_chat": {
        "scene": "small_talk",
        "opener_es": "Estoy saliendo más estos días. ¿Algo te está inhibiendo de venir conmigo?",
        "opener_en": "I'm going out more these days. Is something stopping you from coming with me?",
    },

    # GL 18.5 Perfect Tenses
    "grammar_perfect_tenses_present_perfect_chat": {
        "scene": "restaurant",
        "opener_es": "¿Ha comido aquí antes? Hemos cambiado el menú hace poco.",
        "opener_en": "Have you eaten here before? We've changed the menu recently.",
    },
    "grammar_perfect_tenses_pluperfect_chat": {
        "scene": "small_talk",
        "opener_es": "Antes de mudarme aquí, había vivido en tres ciudades. ¿Y tú?",
        "opener_en": "Before moving here, I had lived in three cities. What about you?",
    },
    "grammar_perfect_tenses_chat": {
        "scene": "restaurant",
        "opener_es": "¿Has probado el plato del día? Lo hemos preparado especialmente esta semana.",
        "opener_en": "Have you tried today's special? We've prepared it specially this week.",
    },

    # ── GL 4.2 Por/Para — chat sub-variants ──
    "grammar_por_para_chat_2": {
        "scene": "groceries",
        "opener_es": "Estos plátanos son para tu desayuno, ¿no? Los cobro por kilo o por bolsa.",
        "opener_en": "These bananas are for your breakfast, right? I charge by the kilo or by the bag.",
    },
    "grammar_por_para_chat_3": {
        "scene": "contractor",
        "opener_es": "Esto lo construimos para tu cocina nueva. ¿Pagas por adelantado o por etapas?",
        "opener_en": "We're building this for your new kitchen. Are you paying up front or in stages?",
    },
    "grammar_por_para_chat_4": {
        "scene": "restaurant",
        "opener_es": "Gracias por venir tan temprano. ¿Para cuántas personas es la mesa?",
        "opener_en": "Thanks for coming so early. The table's for how many?",
    },

    # ── GL 4.4 Possessive Pronouns — chat sub-variant ──
    "grammar_possessive_pronouns_chat_2": {
        "scene": "small_talk",
        "opener_es": "Esa bicicleta en el patio, ¿es la tuya o la suya?",
        "opener_en": "That bike in the yard — is it yours or theirs?",
    },

    # ── GL 10 Gustar — chat sub-variants ──
    "grammar_gustar_1_chat_2": {
        "scene": "restaurant",
        "opener_es": "Le traigo el menú. ¿Le gusta el pescado o prefiere la carne?",
        "opener_en": "Here's the menu. Do you like fish, or do you prefer meat?",
    },
    "grammar_gustar_2_chat_2": {
        "scene": "clothing",
        "opener_es": "Acabamos de recibir estos. ¿Le gustan los colores claros o los oscuros?",
        "opener_en": "We just got these in. Do you like the lighter colors or the darker ones?",
    },
    "grammar_gustar_3_chat_2": {
        "scene": "groceries",
        "opener_es": "Hoy tenemos fresas, y a mi señora le gustan mucho. ¿A usted le gusta la fruta dulce?",
        "opener_en": "We've got strawberries today and my wife loves them. Do you like sweet fruit?",
    },

    # ── GL 11 Modal + Infinitive — chat ──
    "grammar_modal_chat_1": {
        "scene": "small_talk",
        "opener_es": "¿Qué tienes que hacer hoy? Yo debo pasar al banco antes de las cinco.",
        "opener_en": "What do you have to do today? I need to swing by the bank before five.",
    },

    # ── GL 12 Imperfect — numbered chat lessons ──
    "grammar_imperfect_3": {
        "scene": "small_talk",
        "opener_es": "¿Qué hacías de niño? Yo escuchaba la radio todas las tardes.",
        "opener_en": "What did you used to do as a kid? I listened to the radio every afternoon.",
    },
    "grammar_imperfect_6": {
        "scene": "small_talk",
        "opener_es": "Cuéntame cómo eran las cosas antes. ¿Ibas mucho al centro?",
        "opener_en": "Tell me how things used to be. Did you go downtown a lot?",
    },

    # ── GL 13 Reflexive Present — numbered chat lessons ──
    "grammar_reflexive_3": {
        "scene": "small_talk",
        "opener_es": "Cuéntame sobre tu rutina de la mañana. ¿A qué hora te levantas?",
        "opener_en": "Tell me about your morning routine. What time do you get up?",
    },
    "grammar_reflexive_6": {
        "scene": "clothing",
        "opener_es": "¿Cómo te preparas en la mañana? ¿Te vistes antes o después de desayunar?",
        "opener_en": "How do you get ready in the morning? Do you get dressed before or after breakfast?",
    },

    # ── GL 14 Future — numbered chat lessons ──
    "grammar_future_3": {
        "scene": "small_talk",
        "opener_es": "¿Qué harás mañana? Yo estudiaré un poco y luego saldré con mis amigos.",
        "opener_en": "What will you do tomorrow? I'll study a bit and then go out with friends.",
    },
    "grammar_future_6": {
        "scene": "restaurant",
        "opener_es": "Cuéntame tus planes para el fin de semana. ¿Vendrá tu familia?",
        "opener_en": "Tell me your plans for the weekend. Will your family be coming?",
    },
    "grammar_future_9": {
        "scene": "banking",
        "opener_es": "¿Qué traerá el próximo año? ¿Sabrá usted ya cuánto querrá ahorrar?",
        "opener_en": "What will the next year bring? Do you know yet how much you'll want to save?",
    },

    # ── GL 15 Conditional — numbered chat lessons ──
    "grammar_conditional_3": {
        "scene": "banking",
        "opener_es": "¿Qué haría con un millón de dólares? Yo invertiría una buena parte.",
        "opener_en": "What would you do with a million dollars? I'd invest a good portion.",
    },
    "grammar_conditional_6": {
        "scene": "small_talk",
        "opener_es": "¿Dónde vivirías si pudieras elegir? Yo tendría una casa cerca del mar.",
        "opener_en": "Where would you live if you could choose? I'd have a house near the sea.",
    },

    # ── GL 17.2 Preterite Spelling Changes ──
    "grammar_pret_spelling_3": {
        "scene": "groceries",
        "opener_es": "¿Qué compraste ayer? Yo busqué tomates pero no toqué la fruta de la otra cesta.",
        "opener_en": "What did you buy yesterday? I looked for tomatoes but didn't touch the fruit in the other basket.",
    },
    "grammar_pret_spelling_6": {
        "scene": "restaurant",
        "opener_es": "¿Almorzó por aquí esta semana? Empezamos un menú nuevo el lunes.",
        "opener_en": "Did you have lunch here this week? We started a new menu on Monday.",
    },
    "grammar_pret_spelling_9": {
        "scene": "contractor",
        "opener_es": "¿Oyó lo de la pared? Se cayó el martes — construí un soporte nuevo, pero el agua no fluyó bien.",
        "opener_en": "Did you hear about the wall? It fell on Tuesday — I built a new support, but the water didn't flow right.",
    },

    # ── GL 17.3 Preterite Strong ──
    "grammar_pret_strong_3": {
        "scene": "police",
        "opener_es": "¿Dónde estuvo usted anoche entre las nueve y las diez? Tuvimos un reporte por aquí.",
        "opener_en": "Where were you last night between nine and ten? We had a report in this area.",
    },
    "grammar_pret_strong_6": {
        "scene": "small_talk",
        "opener_es": "¿Qué tuviste que hacer la semana pasada? Yo no quise salir mucho.",
        "opener_en": "What did you have to do last week? I didn't really want to go out much.",
    },
    "grammar_pret_strong_9": {
        "scene": "mechanic",
        "opener_es": "Cuéntame de una vez que no pudiste arreglar algo. A mí no me cupo el motor en el primer intento.",
        "opener_en": "Tell me about a time you couldn't fix something. I couldn't get the engine to fit on the first try.",
    },

    # ── GL 17.4 Preterite -ducir ──
    "grammar_pret_ducir_3": {
        "scene": "mechanic",
        "opener_es": "¿Condujo bien el coche ayer? Yo traduje el manual, pero no introduje la pieza correcta.",
        "opener_en": "Did the car drive okay yesterday? I translated the manual, but I didn't put in the right part.",
    },

    # ── GL 17.5 Preterite e→i ──
    "grammar_pret_e_to_i_3": {
        "scene": "restaurant",
        "opener_es": "¿Qué pidió usted la última vez? Le serví el especial, pero alguien repitió el postre.",
        "opener_en": "What did you order last time? I served you the special, but somebody had the dessert twice.",
    },

    # ── GL 19 Object Pronouns — numbered chat lessons ──
    "grammar_obj_chat_1": {
        "scene": "small_talk",
        "opener_es": "Hablemos de quién hace qué por quién. ¿Quién te ayuda a ti en la casa?",
        "opener_en": "Let's talk about who does what for whom. Who helps you out at home?",
    },
    "grammar_obj_chat_2": {
        "scene": "clothing",
        "opener_es": "Cuéntame de regalos que has dado este año. ¿Se los envolviste tú mismo?",
        "opener_en": "Tell me about gifts you've given this year. Did you wrap them yourself?",
    },

    # ── GL 20 Subjunctive Present — numbered chat lessons ──
    "grammar_subj_pres_3": {
        "scene": "small_talk",
        "opener_es": "¿Qué esperas que pase esta semana? Ojalá no llueva el sábado.",
        "opener_en": "What do you hope happens this week? Hopefully it doesn't rain on Saturday.",
    },
    "grammar_subj_pres_6": {
        "scene": "contractor",
        "opener_es": "¿Qué quieres que hagan los muchachos primero? Espero que estén aquí temprano.",
        "opener_en": "What do you want the guys to do first? I hope they're here early.",
    },
    "grammar_subj_pres_8": {
        "scene": "internet",
        "opener_es": "¿Qué necesita que sepan los técnicos antes de venir? Es importante que haya espacio cerca del módem.",
        "opener_en": "What do you need the technicians to know before they come? It's important that there's space near the modem.",
    },

    # ── GL 20 Subjunctive Imperfect — numbered chat lessons ──
    "grammar_subj_impf_3": {
        "scene": "small_talk",
        "opener_es": "Si tuvieras más tiempo, ¿qué harías? Yo viajaría a un país nuevo.",
        "opener_en": "If you had more time, what would you do? I'd travel to a new country.",
    },
    "grammar_subj_impf_6": {
        "scene": "mechanic",
        "opener_es": "¿Y si tuvieras un trabajo diferente? A veces pienso que sería más fácil si hiciera otra cosa.",
        "opener_en": "What if you had a different job? Sometimes I think it'd be easier if I did something else.",
    },
    "grammar_subj_impf_8": {
        "scene": "small_talk",
        "opener_es": "Cuéntame qué quisieras haber dicho. Yo siempre pienso en lo que pude haber dicho mejor.",
        "opener_en": "Tell me what you wished you had said. I always think about what I could've said better.",
    },
}
