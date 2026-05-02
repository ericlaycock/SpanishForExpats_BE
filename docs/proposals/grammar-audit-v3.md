> **PROPOSAL — NOT CURRENT STATE.** Do not treat this document as a description of the running system. It is a v3 audit/proposal that may not match what's in `grammar_situations.py` today. Last verified against code: never.
>
> For canonical grammar curriculum information, see `docs/grammar-curriculum.md` and `docs/decisions/grammar-data-shape.md`.

# Grammar Curriculum Audit (v3)

_Generated from `app/data/grammar_situations.py` — 130 lessons across 36 grammar levels._

## Conventions

- A lesson is **either** `chart + 10 drills` **or** `chat`. Never both.
- 'Chat' is just `chat` — no P2/P3 split.
- A chart+drill lesson teaches **at most 2 verbs/rules**.
- Drill sentences are **simple SVO** (default ≤ 6 words). One longer sentence per lesson is allowed.
- **No parenthetical clues** in the English prompt — they leak the answer.
- Every recognizable noun in a drill must have `noun_id` set so the existing `NounHint` UI can render the dotted-underline tooltip.
- **Drills are unique within a module** — no two drill-lessons share a sentence.
- Default split: pair items in 2s; each pair → 1 chart+drill lesson; after every 2 pairs (4 items), insert a chat lesson consolidating only those new items. Trailing orphan pair gets its own drill + chat.
- **Module-specific overrides** apply to **Pronouns**, **Possessive Adjectives**, and **Grammatical Gender** (see those sections — drafts include proposed Phase-1 sentences for review).

---

## Pronouns (GL 1)

### Current lessons

**`grammar_pronouns` — Pronouns** (lesson 1)

- **Verbs/rules:** yo, tú, él, ella, usted, nosotros, nosotras, ellos, ellas, ustedes, su
- **Current anatomy:** video chart (0a) + 11 flashcards (1a) + written test (1b) + chat P2
- **Issues:** 10 drill_sentences but 0b:off → dead data; uses 1a flashcards instead of drills; 2/10 drills have parenthetical clues — strip; missing noun_id for: amigo, casa, mercado, tienda
- **Drill sentences (10):**
  1. (written) I am from here → _Yo soy de aquí_ `[no noun_id]`
  2. (auditory) You are my friend → _Tú eres mi amigo_ `[no noun_id]`
  3. (written) He is at the store → _Él está en la tienda_ `[no noun_id]`
  4. (auditory) She lives downtown → _Ella vive en el centro_ `[no noun_id]`
  5. (written) You speak Spanish → _Usted habla español_ `[no noun_id]`
  6. (auditory) We go to the market → _Nosotros vamos al mercado_ `[no noun_id]`
  7. (written) We (f) live here → _cleaned:_ **We  live here** → _Nosotras vivimos aquí_ `[no noun_id]`
  8. (auditory) They are at home → _Ellos están en casa_ `[no noun_id]`
  9. (written) They (f) work here → _cleaned:_ **They  work here** → _Ellas trabajan aquí_ `[no noun_id]`
  10. (auditory) You all are welcome → _Ustedes son bienvenidos_ `[no noun_id]`

### Ideal lessons

**Lesson 1** — `drill` — Verbs/rules: yo, tú, él, ella, usted

- **Anatomy:** rule chart (singular pronouns + You-formal-vs-informal callout) + 10 drills (ser + cognate adjective)
- **Proposed drill sentences (10):**
  1. (written) I am tall → _Yo soy alto_
  2. (auditory) You are a tourist → _Tú eres turista_
  3. (written) He is important → _Él es importante_
  4. (auditory) She is elegant → _Ella es elegante_
  5. (written) You are professional → _Usted es profesional_
  6. (auditory) I am sociable → _Yo soy social_
  7. (written) You are international → _Tú eres internacional_
  8. (auditory) He is sociable → _Él es social_
  9. (written) She is important → _Ella es importante_
  10. (auditory) You are likeable → _Usted es simpático_

**Lesson 2** — `drill` — Verbs/rules: nosotros, nosotras, ellos, ellas, ustedes

- **Anatomy:** rule chart (plural pronouns + masculine/feminine forms) + 10 drills (ser + cognate adjective)
- **Proposed drill sentences (10):**
  1. (written) We are Colombian → _Nosotros somos colombianos_
  2. (auditory) We (f) are Latin → _Nosotras somos latinas_
  3. (written) They are sociable → _Ellos son sociales_
  4. (auditory) They (f) are professional → _Ellas son profesionales_
  5. (written) You all are tourists → _Ustedes son turistas_
  6. (auditory) We are important → _Nosotros somos importantes_
  7. (written) We (f) are international → _Nosotras somos internacionales_
  8. (auditory) They are likeable → _Ellos son simpáticos_
  9. (written) They (f) are elegant → _Ellas son elegantes_
  10. (auditory) You all are tall → _Ustedes son altos_

**Lesson 3** — `chat` — Verbs/rules: yo, tú, él, ella, usted, nosotros, nosotras, ellos, ellas, ustedes

- **Anatomy:** chat (all 10 pronouns in conversation)

---

## Possessive Adjectives (GL 1.5)

### Current lessons

**`grammar_possessive_adj` — Possessive Adjectives** (lesson 1)

- **Verbs/rules:** mi, tu, su, nuestro, sus
- **Current anatomy:** chat P2
- **Issues:** CHAT-ONLY (no teaching before chat); 10 drill_sentences but 0b:off → dead data; missing noun_id for: amigo, carro, casa, ciudad, familia…
- **Drill sentences (10):**
  1. (written) My house is big → _Mi casa es grande_ `[no noun_id]`
  2. (auditory) Your friend is here → _Tu amigo está aquí_ `[no noun_id]`
  3. (written) Her car is new → _Su carro es nuevo_ `[no noun_id]`
  4. (auditory) Our family is here → _Nuestra familia está aquí_ `[no noun_id]`
  5. (written) Their dogs are big → _Sus perros son grandes_ `[no noun_id]`
  6. (auditory) My book is here → _Mi libro está aquí_ `[no noun_id]`
  7. (written) Your house is beautiful → _Tu casa es bonita_ `[no noun_id]`
  8. (auditory) His name is Carlos → _Su nombre es Carlos_ `[no noun_id]`
  9. (written) Our city is big → _Nuestra ciudad es grande_ `[no noun_id]`
  10. (auditory) Their names are Ana and Luis → _Sus nombres son Ana y Luis_ `[no noun_id]`

### Ideal lessons

**Lesson 1** — `drill` — Verbs/rules: mi, tu, su, nuestro, nuestra

- **Anatomy:** rule chart (singular possessives + agreement) + 10 drills (possessive + noun)
- **Proposed drill sentences (10):**
  1. (written) my house → _mi casa_ `[noun_id=casa]`
  2. (auditory) your friend → _tu amigo_ `[noun_id=amigo]`
  3. (written) his car → _su carro_ `[noun_id=carro]`
  4. (auditory) our (f) family → _nuestra familia_ `[noun_id=familia]`
  5. (written) our (m) dog → _nuestro perro_ `[noun_id=perro]`
  6. (auditory) my book → _mi libro_ `[noun_id=libro]`
  7. (written) your name → _tu nombre_ `[noun_id=nombre]`
  8. (auditory) her work → _su trabajo_ `[noun_id=trabajo]`
  9. (written) our (f) city → _nuestra ciudad_ `[noun_id=ciudad]`
  10. (auditory) our (m) plan → _nuestro plan_ `[noun_id=plan]`

**Lesson 2** — `drill` — Verbs/rules: mis, tus, sus, nuestros, nuestras

- **Anatomy:** rule chart (plural possessives) + 10 drills (possessive + noun)
- **Proposed drill sentences (10):**
  1. (written) my books → _mis libros_ `[noun_id=libro]`
  2. (auditory) your friends → _tus amigos_ `[noun_id=amigo]`
  3. (written) their cars → _sus carros_ `[noun_id=carro]`
  4. (auditory) our (f) families → _nuestras familias_ `[noun_id=familia]`
  5. (written) our (m) dogs → _nuestros perros_ `[noun_id=perro]`
  6. (auditory) my houses → _mis casas_ `[noun_id=casa]`
  7. (written) your works → _tus trabajos_ `[noun_id=trabajo]`
  8. (auditory) their plans → _sus planes_ `[noun_id=plan]`
  9. (written) our (f) cities → _nuestras ciudades_ `[noun_id=ciudad]`
  10. (auditory) our (m) names → _nuestros nombres_ `[noun_id=nombre]`

**Lesson 3** — `chat` — Verbs/rules: mi/mis, tu/tus, su/sus, nuestro/-os/-a/-as

- **Anatomy:** chat (all possessives in conversation)

---

## Grammatical Gender (GL 2)

### Current lessons

**`grammar_gender` — Grammatical Gender** (lesson 1)

- **Verbs/rules:** el, los, la, las, un, unos, una, unas
- **Current anatomy:** video chart (0a) + 10 drills (0b)
- **Issues:** missing noun_id for: café, casa, ciudad, libro
- **Drill sentences (10):**
  1. (written) The book is here → _El libro está aquí_ `[no noun_id]`
  2. (auditory) A house is big → _Una casa es grande_ `[no noun_id]`
  3. (written) The dogs are here → _Los perros están aquí_ `[no noun_id]`
  4. (auditory) Some girls are from Mexico → _Unas chicas son de México_ `[no noun_id]`
  5. (written) The city is beautiful → _La ciudad es bonita_ `[no noun_id]`
  6. (auditory) A man is here → _Un hombre está aquí_ `[no noun_id]`
  7. (written) The tables are new → _Las mesas son nuevas_ `[no noun_id]`
  8. (auditory) Some books are here → _Unos libros están aquí_ `[no noun_id]`
  9. (written) The coffee is hot → _El café está caliente_ `[no noun_id]`
  10. (auditory) A city has many streets → _Una ciudad tiene muchas calles_ `[no noun_id]`

### Ideal lessons

**Lesson 1** — `drill` — Verbs/rules: el, la, los, las

- **Anatomy:** rule chart (DEFINITE articles) + masculine endings MAJE LONERS (-ma, -je, -l, -o, -n, -e, -r, -s) + feminine endings DIONZA (-d, -ion, -z, -a) + 10 drills (article + noun)
- **Proposed drill sentences (10):**
  1. (written) the problem → _el problema_ `[noun_id=problema]`
  2. (auditory) the trip → _el viaje_ `[noun_id=viaje]`
  3. (written) the animal → _el animal_ `[noun_id=animal]`
  4. (auditory) the book → _el libro_ `[noun_id=libro]`
  5. (written) the lemon → _el limón_ `[noun_id=limón]`
  6. (auditory) the coffee → _el café_ `[noun_id=café]`
  7. (written) the freedom → _la libertad_ `[noun_id=libertad]`
  8. (auditory) the nation → _la nación_ `[noun_id=nación]`
  9. (written) the time (occurrence) → _la vez_ `[noun_id=vez]`
  10. (auditory) the house → _la casa_ `[noun_id=casa]`

**Lesson 2** — `drill` — Verbs/rules: un, una, unos, unas

- **Anatomy:** rule chart (INDEFINITE articles) + reinforcement of MAJE LONERS / DIONZA + 10 drills (article + noun)
- **Proposed drill sentences (10):**
  1. (written) a system → _un sistema_ `[noun_id=sistema]`
  2. (auditory) a passage → _un pasaje_ `[noun_id=pasaje]`
  3. (written) a paper → _un papel_ `[noun_id=papel]`
  4. (auditory) a case → _un caso_ `[noun_id=caso]`
  5. (written) an exam → _un examen_ `[noun_id=examen]`
  6. (auditory) an actor → _un actor_ `[noun_id=actor]`
  7. (written) an atlas → _un atlas_ `[noun_id=atlas]`
  8. (auditory) a truth → _una verdad_ `[noun_id=verdad]`
  9. (written) an option → _una opción_ `[noun_id=opción]`
  10. (auditory) a light → _una luz_ `[noun_id=luz]`

**Lesson 3** — `chat` — Verbs/rules: el, la, los, las, un, una, unos, unas

- **Anatomy:** chat (gender + articles in conversation)

---

## Regular Present (GL 3)

### Current lessons

**`grammar_regular_present_1` — Regular Present (1/3)** (lesson 1)

- **Verbs/rules:** hablar, beber, vivir
- **Current anatomy:** video chart (0a) + 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) I speak Spanish at home → _Yo hablo español en casa_ `[noun_id=casa]`
  2. (auditory) She speaks English → _Ella habla inglés_ `[no noun_id]`
  3. (written) You all speak well → _Ustedes hablan bien_ `[no noun_id]`
  4. (auditory) You drink coffee every day → _Tú bebes café todos los días_ `[noun_id=café]`
  5. (written) We (f) drink water → _cleaned:_ **We  drink water** → _Nosotras bebemos agua_ `[noun_id=agua]`
  6. (auditory) He drinks juice in the morning → _Él bebe jugo por la mañana_ `[noun_id=jugo]`
  7. (written) You live in the city → _Usted vive en la ciudad_ `[noun_id=ciudad]`
  8. (auditory) We live in a house → _Nosotros vivimos en una casa_ `[noun_id=casa]`
  9. (written) They (f) live here → _cleaned:_ **They  live here** → _Ellas viven aquí_ `[no noun_id]`
  10. (auditory) They live in Colombia → _Ellos viven en Colombia_ `[no noun_id]`

**`grammar_regular_present_2` — Regular Present (2/3)** (lesson 2)

- **Verbs/rules:** escuchar, comer, escribir
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) I listen to music every day → _Yo escucho música todos los días_ `[noun_id=música]`
  2. (auditory) You listen to the radio → _Usted escucha la radio_ `[no noun_id]`
  3. (written) They (f) listen at home → _cleaned:_ **They  listen at home** → _Ellas escuchan en casa_ `[noun_id=casa]`
  4. (auditory) You eat meat at lunch → _Tú comes carne al almuerzo_ `[noun_id=carne]`
  5. (written) We eat bread every morning → _Nosotros comemos pan cada mañana_ `[noun_id=pan]`
  6. (auditory) She eats at the restaurant → _Ella come en el restaurante_ `[noun_id=restaurante]`
  7. (written) He writes a letter → _Él escribe una carta_ `[noun_id=carta]`
  8. (auditory) We (f) write in Spanish → _cleaned:_ **We  write in Spanish** → _Nosotras escribimos en español_ `[no noun_id]`
  9. (written) You all write your names → _Ustedes escriben sus nombres_ `[no noun_id]`
  10. (auditory) They write books → _Ellos escriben libros_ `[noun_id=libro]`

**`grammar_regular_present_3` — Regular Present (3/3)** (lesson 3)

- **Verbs/rules:** cantar, leer, abrir
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) I sing at home → _Yo canto en casa_ `[noun_id=casa]`
  2. (auditory) We (f) sing in Spanish → _cleaned:_ **We  sing in Spanish** → _Nosotras cantamos en español_ `[no noun_id]`
  3. (written) You all sing well → _Ustedes cantan bien_ `[no noun_id]`
  4. (auditory) You read a book every day → _Tú lees un libro cada día_ `[noun_id=libro]`
  5. (written) She reads a book → _Ella lee un libro_ `[noun_id=libro]`
  6. (auditory) They read Spanish books → _Ellos leen libros en español_ `[noun_id=libro]`
  7. (written) He opens the door → _Él abre la puerta_ `[noun_id=puerta]`
  8. (auditory) You open the window → _Usted abre la ventana_ `[noun_id=ventana]`
  9. (written) We open the store → _Nosotros abrimos la tienda_ `[noun_id=tienda]`
  10. (auditory) They (f) open their books → _cleaned:_ **They  open their books** → _Ellas abren sus libros_ `[noun_id=libro]`

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | hablar, beber | verb chart + 10 drills |
| 2 | **drill** | vivir, escuchar | verb chart + 10 drills |
| 3 | **chat** | hablar, beber, vivir, escuchar | chat (10 possible conjugations, user does 5) |
| 4 | **drill** | comer, escribir | verb chart + 10 drills |
| 5 | **drill** | cantar, leer | verb chart + 10 drills |
| 6 | **chat** | comer, escribir, cantar, leer | chat (10 possible conjugations, user does 5) |
| 7 | **drill** | abrir | verb chart + 10 drills |
| 8 | **chat** | abrir | chat (10 possible conjugations, user does 5) |

---

## Irregular Present (GL 4)

### Current lessons

**`grammar_irregular_present_1` — Irregular Present (1/3)** (lesson 1)

- **Verbs/rules:** ser, estar, ir, dar, tener, venir
- **Current anatomy:** video chart (0a) + 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 3/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) I am from Colombia → _Yo soy de Colombia_ `[no noun_id]`
  2. (auditory) She is at the bank → _Ella está en el banco_ `[noun_id=banco]`
  3. (written) You go to the market → _Usted va al mercado_ `[noun_id=mercado]`
  4. (auditory) You (f) are at home → _cleaned:_ **You  are at home** → _Tú estás en casa_ `[noun_id=casa]`
  5. (written) They (f) go to the store → _cleaned:_ **They  go to the store** → _Ellas van a la tienda_ `[noun_id=tienda]`
  6. (auditory) We (f) are from the city → _cleaned:_ **We  are from the city** → _Nosotras somos de la ciudad_ `[noun_id=ciudad]`
  7. (written) You all give money → _Ustedes dan dinero_ `[noun_id=dinero]`
  8. (auditory) He has a dog → _Él tiene un perro_ `[noun_id=perro]`
  9. (written) We have the book → _Nosotros tenemos el libro_ `[noun_id=libro]`
  10. (auditory) They come from the house → _Ellos vienen de la casa_ `[noun_id=casa]`

**`grammar_irregular_present_2` — Irregular Present (2/3)** (lesson 2)

- **Verbs/rules:** ser, estar, ir, dar, tener, venir
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) You are from Mexico → _Tú eres de México_ `[no noun_id]`
  2. (auditory) We are from here → _Nosotros somos de aquí_ `[no noun_id]`
  3. (written) He is at the office → _Él está en la oficina_ `[noun_id=oficina]`
  4. (auditory) You all are in the city → _Ustedes están en la ciudad_ `[noun_id=ciudad]`
  5. (written) She goes to the market → _Ella va al mercado_ `[noun_id=mercado]`
  6. (auditory) We (f) go to the store → _cleaned:_ **We  go to the store** → _Nosotras vamos a la tienda_ `[noun_id=tienda]`
  7. (written) I give the book to her → _Yo doy el libro_ `[noun_id=libro]`
  8. (auditory) They give money → _Ellos dan dinero_ `[noun_id=dinero]`
  9. (written) You have a car → _Usted tiene un carro_ `[noun_id=carro]`
  10. (auditory) They (f) come from the house → _cleaned:_ **They  come from the house** → _Ellas vienen de la casa_ `[noun_id=casa]`

**`grammar_irregular_present_3` — Irregular Present (3/3)** (lesson 3)

- **Verbs/rules:** ser, estar, ir, dar, tener, venir
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) You are a good person → _Usted es una buena persona_ `[no noun_id]`
  2. (auditory) They are at the restaurant → _Ellos están en el restaurante_ `[noun_id=restaurante]`
  3. (written) I am at the store → _Yo estoy en la tienda_ `[noun_id=tienda]`
  4. (auditory) They (f) are in the city → _cleaned:_ **They  are in the city** → _Ellas están en la ciudad_ `[noun_id=ciudad]`
  5. (written) You go to the office → _Tú vas a la oficina_ `[noun_id=oficina]`
  6. (auditory) We go to the park → _Nosotros vamos al parque_ `[noun_id=parque]`
  7. (written) She gives bread to them → _Ella da pan_ `[noun_id=pan]`
  8. (auditory) We (f) give water → _cleaned:_ **We  give water** → _Nosotras damos agua_ `[noun_id=agua]`
  9. (written) You all have a dog → _Ustedes tienen un perro_ `[noun_id=perro]`
  10. (auditory) He comes from the park → _Él viene del parque_ `[noun_id=parque]`

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | ser, estar | verb chart + 10 drills |
| 2 | **drill** | ir, dar | verb chart + 10 drills |
| 3 | **chat** | ser, estar, ir, dar | chat (10 possible conjugations, user does 5) |
| 4 | **drill** | tener, venir | verb chart + 10 drills |
| 5 | **chat** | tener, venir | chat (10 possible conjugations, user does 5) |

---

## Ser vs. Estar (GL 4.1)

### Current lessons

**`grammar_ser_estar_rules` — Ser vs. Estar** (lesson 1)

- **Verbs/rules:** ser, estar
- **Current anatomy:** chat P2
- **Issues:** CHAT-ONLY (no teaching before chat); 10 drill_sentences but 0b:off → dead data; 10/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) I am a teacher (permanent) → _cleaned:_ **I am a teacher** → _Yo soy profesora_ `[no noun_id]`
  2. (auditory) The coffee is hot (temporary) → _cleaned:_ **The coffee is hot** → _El café está caliente_ `[noun_id=café]`
  3. (written) She is from Colombia (origin) → _cleaned:_ **She is from Colombia** → _Ella es de Colombia_ `[no noun_id]`
  4. (auditory) He is tired (condition) → _cleaned:_ **He is tired** → _Él está cansado_ `[no noun_id]`
  5. (written) The house is big (characteristic) → _cleaned:_ **The house is big** → _La casa es grande_ `[noun_id=casa]`
  6. (auditory) The door is open (state) → _cleaned:_ **The door is open** → _La puerta está abierta_ `[noun_id=puerta]`
  7. (written) We are at the market (location) → _cleaned:_ **We are at the market** → _Nosotros estamos en el mercado_ `[noun_id=mercado]`
  8. (auditory) The water is cold (current state) → _cleaned:_ **The water is cold** → _El agua está fría_ `[noun_id=agua]`
  9. (written) You all are students (identity) → _cleaned:_ **You all are students** → _Ustedes son estudiantes_ `[no noun_id]`
  10. (auditory) The restaurant is closed (state) → _cleaned:_ **The restaurant is closed** → _El restaurante está cerrado_ `[noun_id=restaurante]`

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | ser, estar | rule chart + 10 drills |
| 2 | **chat** | ser, estar | chat (10 possible conjugations, user does 5) |

---

## Por vs. Para (GL 4.2)

### Current lessons

**`grammar_por_para` — Por vs. Para** (lesson 1)

- **Verbs/rules:** por, para
- **Current anatomy:** chat P2
- **Issues:** CHAT-ONLY (no teaching before chat); 10 drill_sentences but 0b:off → dead data; 9/10 drills have parenthetical clues — strip; 4 drills > 6 words — simplify (1 longer per lesson allowed)
- **Drill sentences (10):**
  1. (written) I go by the park (movement through) → _cleaned:_ **I go by the park** → _Yo voy por el parque_ `[noun_id=parque]`
  2. (auditory) This is for you (recipient) → _cleaned:_ **This is for you** → _Esto es para ti_ `[no noun_id]`
  3. (written) She works for money (exchange) → _cleaned:_ **She works for money** → _Ella trabaja por dinero_ `[noun_id=dinero]`
  4. (auditory) We study in order to learn (purpose) → _cleaned:_ **We study in order to learn** → _Nosotros estudiamos para aprender_ `[no noun_id]`
  5. (written) He comes by the house (passes by) → _cleaned:_ **He comes by the house** → _Él pasa por la casa_ `[noun_id=casa]`
  6. (auditory) The book is for the class (intended use) → _cleaned:_ **The book is for the class** → _El libro es para la clase_ `[noun_id=libro]`
  7. (written) She travels by car (means) → _cleaned:_ **She travels by car** → _Ella viaja en carro_ `[noun_id=carro]`
  8. (auditory) I need it for tomorrow (deadline) → _cleaned:_ **I need it for tomorrow** → _Lo necesito para mañana_ `[no noun_id]`
  9. (written) Thank you for the water → _Gracias por el agua_ `[noun_id=agua]`
  10. (auditory) We work to live (goal) → _cleaned:_ **We work to live** → _Nosotras trabajamos para vivir_ `[no noun_id]`

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | por, para | rule chart + 10 drills |
| 2 | **chat** | por, para | chat (10 possible conjugations, user does 5) |

---

## Demonstratives (GL 4.3)

### Current lessons

**`grammar_demonstratives` — Demonstratives** (lesson 1)

- **Verbs/rules:** este, esta, ese, esa, aquel, aquella
- **Current anatomy:** chat P2
- **Issues:** CHAT-ONLY (no teaching before chat); 10 drill_sentences but 0b:off → dead data; 3/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) This house is big (near) → _cleaned:_ **This house is big** → _Esta casa es grande_ `[noun_id=casa]`
  2. (auditory) That book is interesting (near listener) → _cleaned:_ **That book is interesting** → _Ese libro es interesante_ `[noun_id=libro]`
  3. (written) That city over there is beautiful (far) → _cleaned:_ **That city over there is beautiful** → _Aquella ciudad es bonita_ `[noun_id=ciudad]`
  4. (auditory) This coffee is hot → _Este café está caliente_ `[noun_id=café]`
  5. (written) That door is open → _Esa puerta está abierta_ `[noun_id=puerta]`
  6. (auditory) That park over there is nice → _Aquel parque es bonito_ `[noun_id=parque]`
  7. (written) This water is cold → _Esta agua está fría_ `[noun_id=agua]`
  8. (auditory) That car is expensive → _Ese carro es caro_ `[noun_id=carro]`
  9. (written) That restaurant over there is good → _Aquel restaurante es bueno_ `[noun_id=restaurante]`
  10. (auditory) This music is great → _Esta música es genial_ `[noun_id=música]`

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | este, esta | rule chart + 10 drills |
| 2 | **drill** | ese, esa | rule chart + 10 drills |
| 3 | **chat** | este, esta, ese, esa | chat (10 possible conjugations, user does 5) |
| 4 | **drill** | aquel, aquella | rule chart + 10 drills |
| 5 | **chat** | aquel, aquella | chat (10 possible conjugations, user does 5) |

---

## Possessive Pronouns (GL 4.4)

### Current lessons

**`grammar_possessive_pronouns` — Possessive Pronouns** (lesson 1)

- **Verbs/rules:** el mío, el tuyo, el suyo, el nuestro
- **Current anatomy:** chat P2
- **Issues:** CHAT-ONLY (no teaching before chat); 10 drill_sentences but 0b:off → dead data
- **Drill sentences (10):**
  1. (written) The book is mine → _El libro es mío_ `[noun_id=libro]`
  2. (auditory) The house is yours → _La casa es tuya_ `[noun_id=casa]`
  3. (written) The car is his → _El carro es suyo_ `[noun_id=carro]`
  4. (auditory) The money is ours → _El dinero es nuestro_ `[noun_id=dinero]`
  5. (written) The bag is mine → _La bolsa es mía_ `[no noun_id]`
  6. (auditory) The coffee is yours → _El café es tuyo_ `[noun_id=café]`
  7. (written) The dog is hers → _El perro es suyo_ `[noun_id=perro]`
  8. (auditory) The house is ours → _La casa es nuestra_ `[noun_id=casa]`
  9. (written) The water is mine → _El agua es mía_ `[noun_id=agua]`
  10. (auditory) The book is theirs → _El libro es suyo_ `[noun_id=libro]`

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | el mío, el tuyo | rule chart + 10 drills |
| 2 | **drill** | el suyo, el nuestro | rule chart + 10 drills |
| 3 | **chat** | el mío, el tuyo, el suyo, el nuestro | chat (10 possible conjugations, user does 5) |

---

## Irregular Present II (GL 4.5)

### Current lessons

**`grammar_irregular_present_ii_1` — Irregular Present II (1/4)** (lesson 1)

- **Verbs/rules:** hacer, poner, salir, decir
- **Current anatomy:** video chart (0a) + 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip; missing noun_id for: día, nombre, verdad
- **Drill sentences (10):**
  1. (written) I make the food at home → _Yo hago la comida en casa_ `[noun_id=comida]`
  2. (auditory) She makes the coffee → _Ella hace el café_ `[noun_id=café]`
  3. (written) You all do the work → _Ustedes hacen el trabajo_ `[noun_id=trabajo]`
  4. (auditory) You put the book here → _Tú pones el libro aquí_ `[noun_id=libro]`
  5. (written) We (f) put the water here → _cleaned:_ **We  put the water here** → _Nosotras ponemos el agua aquí_ `[noun_id=agua]`
  6. (auditory) He leaves the house → _Él sale de la casa_ `[noun_id=casa]`
  7. (written) They leave the office → _Ellos salen de la oficina_ `[noun_id=oficina]`
  8. (auditory) You say the truth → _Usted dice la verdad_ `[no noun_id]`
  9. (written) We say hello every day → _Nosotros decimos hola cada día_ `[no noun_id]`
  10. (auditory) They (f) say the name → _cleaned:_ **They  say the name** → _Ellas dicen el nombre_ `[no noun_id]`

**`grammar_irregular_present_ii_2` — Irregular Present II (2/4)** (lesson 2)

- **Verbs/rules:** oír, caer, traer, valer
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip; missing noun_id for: música
- **Drill sentences (10):**
  1. (written) I hear the music → _Yo oigo la música_ `[no noun_id]`
  2. (auditory) We hear the dog at night → _Nosotros oímos el perro de noche_ `[noun_id=perro]`
  3. (written) They (f) hear the door → _cleaned:_ **They  hear the door** → _Ellas oyen la puerta_ `[noun_id=puerta]`
  4. (auditory) You fall in the park → _Tú caes en el parque_ `[noun_id=parque]`
  5. (written) She falls in the house → _Ella cae en la casa_ `[noun_id=casa]`
  6. (auditory) He brings the food → _Él trae la comida_ `[noun_id=comida]`
  7. (written) You all bring water → _Ustedes traen agua_ `[noun_id=agua]`
  8. (auditory) It is worth the money → _Usted vale el dinero_ `[noun_id=dinero]`
  9. (written) We (f) are worth a lot → _cleaned:_ **We  are worth a lot** → _Nosotras valemos mucho_ `[no noun_id]`
  10. (auditory) They cost a lot → _Ellos valen mucho_ `[no noun_id]`

**`grammar_irregular_present_ii_3` — Irregular Present II (3/4)** (lesson 3)

- **Verbs/rules:** hacer, poner, salir, decir
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip; missing noun_id for: día, nombre, verdad
- **Drill sentences (10):**
  1. (written) You make breakfast every day → _Tú haces el desayuno cada día_ `[no noun_id]`
  2. (auditory) We do the work together → _Nosotros hacemos el trabajo juntos_ `[noun_id=trabajo]`
  3. (written) You put the book here → _Usted pone el libro aquí_ `[noun_id=libro]`
  4. (auditory) They (f) put the water here → _cleaned:_ **They  put the water here** → _Ellas ponen el agua aquí_ `[noun_id=agua]`
  5. (written) I leave the house → _Yo salgo de la casa_ `[noun_id=casa]`
  6. (auditory) We (f) leave early → _cleaned:_ **We  leave early** → _Nosotras salimos temprano_ `[no noun_id]`
  7. (written) You all leave the office → _Ustedes salen de la oficina_ `[noun_id=oficina]`
  8. (auditory) He says hello in Spanish → _Él dice hola en español_ `[no noun_id]`
  9. (written) She says the truth → _Ella dice la verdad_ `[no noun_id]`
  10. (auditory) They say the name → _Ellos dicen el nombre_ `[no noun_id]`

**`grammar_irregular_present_ii_4` — Irregular Present II (4/4)** (lesson 4)

- **Verbs/rules:** oír, caer, traer, valer
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip; missing noun_id for: calle
- **Drill sentences (10):**
  1. (written) You hear the music → _Tú oyes la música_ `[noun_id=música]`
  2. (auditory) You hear the dog → _Usted oye el perro_ `[noun_id=perro]`
  3. (written) I fall near the door → _Yo caigo cerca de la puerta_ `[noun_id=puerta]`
  4. (auditory) We (f) fall in the street → _cleaned:_ **We  fall in the street** → _Nosotras caemos en la calle_ `[no noun_id]`
  5. (written) They fall at the park → _Ellos caen en el parque_ `[noun_id=parque]`
  6. (auditory) She brings the food from the market → _Ella trae la comida del mercado_ `[noun_id=comida]`
  7. (written) We bring water → _Nosotros traemos agua_ `[noun_id=agua]`
  8. (auditory) It is worth the price → _Él vale el precio_ `[no noun_id]`
  9. (written) They (f) are worth a lot → _cleaned:_ **They  are worth a lot** → _Ellas valen mucho_ `[no noun_id]`
  10. (auditory) You all are worth the effort → _Ustedes valen el esfuerzo_ `[no noun_id]`

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | hacer, poner | verb chart + 10 drills |
| 2 | **drill** | salir, decir | verb chart + 10 drills |
| 3 | **chat** | hacer, poner, salir, decir | chat (10 possible conjugations, user does 5) |
| 4 | **drill** | oír, caer | verb chart + 10 drills |
| 5 | **drill** | traer, valer | verb chart + 10 drills |
| 6 | **chat** | oír, caer, traer, valer | chat (10 possible conjugations, user does 5) |

---

## Spelling Changes (GL 5)

### Current lessons

**`grammar_spelling_changes_1` — Spelling Changes (1/4)** (lesson 1)

- **Verbs/rules:** conocer, producir, construir, conseguir
- **Current anatomy:** video chart (0a) + 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) I know a good restaurant → _Yo conozco un buen restaurante_ `[noun_id=restaurante]`
  2. (auditory) She knows the city well → _Ella conoce la ciudad bien_ `[noun_id=ciudad]`
  3. (written) You all know the area → _Ustedes conocen la zona_ `[no noun_id]`
  4. (auditory) You produce food every day → _Tú produces comida cada día_ `[noun_id=comida]`
  5. (written) We (f) produce good work → _cleaned:_ **We  produce good work** → _Nosotras producimos buen trabajo_ `[noun_id=trabajo]`
  6. (auditory) He builds a house → _Él construye una casa_ `[noun_id=casa]`
  7. (written) They build in the city → _Ellos construyen en la ciudad_ `[noun_id=ciudad]`
  8. (auditory) You get the book → _Usted consigue el libro_ `[noun_id=libro]`
  9. (written) We get the money → _Nosotros conseguimos el dinero_ `[noun_id=dinero]`
  10. (auditory) They (f) get a good job → _cleaned:_ **They  get a good job** → _Ellas consiguen un buen trabajo_ `[noun_id=trabajo]`

**`grammar_spelling_changes_2` — Spelling Changes (2/4)** (lesson 2)

- **Verbs/rules:** recoger, dirigir, convencer, continuar
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip; missing noun_id for: día, familia, plan
- **Drill sentences (10):**
  1. (written) I pick up the food → _Yo recojo la comida_ `[noun_id=comida]`
  2. (auditory) We pick up the bags → _Nosotros recogemos las bolsas_ `[noun_id=bolsa]`
  3. (written) They (f) pick up the books → _cleaned:_ **They  pick up the books** → _Ellas recogen los libros_ `[noun_id=libro]`
  4. (auditory) You direct the work → _Tú diriges el trabajo_ `[noun_id=trabajo]`
  5. (written) She directs the team → _Ella dirige el equipo_ `[no noun_id]`
  6. (auditory) He convinces the client → _Él convence al cliente_ `[no noun_id]`
  7. (written) You all convince the family → _Ustedes convencen a la familia_ `[no noun_id]`
  8. (auditory) You continue working every day → _Usted continúa trabajando cada día_ `[no noun_id]`
  9. (written) We (f) continue with the plan → _cleaned:_ **We  continue with the plan** → _Nosotras continuamos con el plan_ `[no noun_id]`
  10. (auditory) They continue in the city → _Ellos continúan en la ciudad_ `[noun_id=ciudad]`

**`grammar_spelling_changes_3` — Spelling Changes (3/4)** (lesson 3)

- **Verbs/rules:** conocer, producir, construir, conseguir
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) You know a good park → _Tú conoces un buen parque_ `[noun_id=parque]`
  2. (auditory) We know this neighborhood → _Nosotros conocemos este barrio_ `[no noun_id]`
  3. (written) You produce good results → _Usted produce buenos resultados_ `[no noun_id]`
  4. (auditory) They (f) produce the best food → _cleaned:_ **They  produce the best food** → _Ellas producen la mejor comida_ `[noun_id=comida]`
  5. (written) I build a house → _Yo construyo una casa_ `[noun_id=casa]`
  6. (auditory) We (f) build near the market → _cleaned:_ **We  build near the market** → _Nosotras construimos cerca del mercado_ `[noun_id=mercado]`
  7. (written) You all build the office → _Ustedes construyen la oficina_ `[noun_id=oficina]`
  8. (auditory) He gets the job → _Él consigue el trabajo_ `[noun_id=trabajo]`
  9. (written) She gets the book → _Ella consigue el libro_ `[noun_id=libro]`
  10. (auditory) They get the money → _Ellos consiguen el dinero_ `[noun_id=dinero]`

**`grammar_spelling_changes_4` — Spelling Changes (4/4)** (lesson 4)

- **Verbs/rules:** recoger, dirigir, convencer, continuar
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip; missing noun_id for: plan, verdad
- **Drill sentences (10):**
  1. (written) You pick up the food → _Tú recoges la comida_ `[noun_id=comida]`
  2. (auditory) You pick up the book → _Usted recoge el libro_ `[noun_id=libro]`
  3. (written) I direct the work → _Yo dirijo el trabajo_ `[noun_id=trabajo]`
  4. (auditory) We (f) direct the project → _cleaned:_ **We  direct the project** → _Nosotras dirigimos el proyecto_ `[no noun_id]`
  5. (written) They direct from the office → _Ellos dirigen desde la oficina_ `[noun_id=oficina]`
  6. (auditory) She convinces the neighbor → _Ella convence a la vecina_ `[no noun_id]`
  7. (written) We convince with the truth → _Nosotros convencemos con la verdad_ `[no noun_id]`
  8. (auditory) He continues with the plan → _Él continúa con el plan_ `[no noun_id]`
  9. (written) They (f) continue in the city → _cleaned:_ **They  continue in the city** → _Ellas continúan en la ciudad_ `[noun_id=ciudad]`
  10. (auditory) You all continue working → _Ustedes continúan trabajando_ `[no noun_id]`

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | conocer, producir | verb chart + 10 drills |
| 2 | **drill** | construir, conseguir | verb chart + 10 drills |
| 3 | **chat** | conocer, producir, construir, conseguir | chat (10 possible conjugations, user does 5) |
| 4 | **drill** | recoger, dirigir | verb chart + 10 drills |
| 5 | **drill** | convencer, continuar | verb chart + 10 drills |
| 6 | **chat** | recoger, dirigir, convencer, continuar | chat (10 possible conjugations, user does 5) |

---

## Saber vs. Conocer (GL 5.5)

### Current lessons

**`grammar_saber_conocer` — Saber vs. Conocer** (lesson 1)

- **Verbs/rules:** saber, conocer
- **Current anatomy:** chat P2
- **Issues:** CHAT-ONLY (no teaching before chat); 10 drill_sentences but 0b:off → dead data; 10/10 drills have parenthetical clues — strip; 2 drills > 6 words — simplify (1 longer per lesson allowed); missing noun_id for: hora
- **Drill sentences (10):**
  1. (written) I know how to speak Spanish (fact/skill) → _cleaned:_ **I know how to speak Spanish** → _Yo sé hablar español_ `[no noun_id]`
  2. (auditory) You know the city (acquainted with) → _cleaned:_ **You know the city** → _Tú conoces la ciudad_ `[noun_id=ciudad]`
  3. (written) She knows the answer (knowledge) → _cleaned:_ **She knows the answer** → _Ella sabe la respuesta_ `[no noun_id]`
  4. (auditory) He knows the restaurant (familiar with) → _cleaned:_ **He knows the restaurant** → _Él conoce el restaurante_ `[noun_id=restaurante]`
  5. (written) We know how to cook (skill) → _cleaned:_ **We know how to cook** → _Nosotros sabemos cocinar_ `[no noun_id]`
  6. (auditory) We (f) know the market (place) → _cleaned:_ **We  know the market** → _Nosotras conocemos el mercado_ `[noun_id=mercado]`
  7. (written) They know the way (knowledge) → _cleaned:_ **They know the way** → _Ellos saben el camino_ `[no noun_id]`
  8. (auditory) They (f) know the park (familiarity) → _cleaned:_ **They  know the park** → _Ellas conocen el parque_ `[noun_id=parque]`
  9. (written) You know what time it is (fact) → _cleaned:_ **You know what time it is** → _Usted sabe qué hora es_ `[no noun_id]`
  10. (auditory) You all know the neighbors (acquaintance) → _cleaned:_ **You all know the neighbors** → _Ustedes conocen a los vecinos_ `[no noun_id]`

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | saber, conocer | verb chart + 10 drills |
| 2 | **chat** | saber, conocer | chat (10 possible conjugations, user does 5) |

---

## Present O→UE (GL 6)

### Current lessons

**`grammar_present_o_ue_1` — Present O→UE (1/3)** (lesson 1)

- **Verbs/rules:** mover, almorzar, morir, poder, dormir, volver
- **Current anatomy:** video chart (0a) + 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) I move the table → _Yo muevo la mesa_ `[no noun_id]`
  2. (auditory) You have lunch at the restaurant → _Tú almuerzas en el restaurante_ `[noun_id=restaurante]`
  3. (written) He is dying of hunger → _Él muere de hambre_ `[no noun_id]`
  4. (auditory) She can help at the office → _Ella puede ayudar en la oficina_ `[noun_id=oficina]`
  5. (written) You sleep eight hours → _Usted duerme ocho horas_ `[no noun_id]`
  6. (auditory) We return home → _Nosotros volvemos a casa_ `[noun_id=casa]`
  7. (written) We (f) move the chairs → _cleaned:_ **We  move the chairs** → _Nosotras movemos las sillas_ `[no noun_id]`
  8. (auditory) They have lunch in the city → _Ellos almuerzan en la ciudad_ `[noun_id=ciudad]`
  9. (written) They (f) die laughing → _cleaned:_ **They  die laughing** → _Ellas mueren de risa_ `[no noun_id]`
  10. (auditory) You all can speak Spanish → _Ustedes pueden hablar español_ `[no noun_id]`

**`grammar_present_o_ue_2` — Present O→UE (2/3)** (lesson 2)

- **Verbs/rules:** mover, almorzar, morir, poder, dormir, volver
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) You move the chair → _Tú mueves la silla_ `[noun_id=silla]`
  2. (auditory) I have lunch at the market → _Yo almuerzo en el mercado_ `[noun_id=mercado]`
  3. (written) She is dying of tiredness → _Ella muere de cansancio_ `[no noun_id]`
  4. (auditory) He can come to the house → _Él puede venir a la casa_ `[noun_id=casa]`
  5. (written) We sleep in the bedroom → _Nosotros dormimos en la habitación_ `[no noun_id]`
  6. (auditory) You return to the city → _Usted vuelve a la ciudad_ `[noun_id=ciudad]`
  7. (written) They move to the park → _Ellos mueven al parque_ `[noun_id=parque]`
  8. (auditory) We (f) have lunch near the store → _cleaned:_ **We  have lunch near the store** → _Nosotras almorzamos cerca de la tienda_ `[noun_id=tienda]`
  9. (written) You all are dying of laughter → _Ustedes mueren de risa_ `[no noun_id]`
  10. (auditory) They (f) can speak Spanish → _cleaned:_ **They  can speak Spanish** → _Ellas pueden hablar español_ `[no noun_id]`

**`grammar_present_o_ue_3` — Present O→UE (3/3)** (lesson 3)

- **Verbs/rules:** mover, almorzar, morir, poder, dormir, volver
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) He moves the car → _Él mueve el carro_ `[noun_id=carro]`
  2. (auditory) She has lunch at home → _Ella almuerza en casa_ `[noun_id=casa]`
  3. (written) I am dying of thirst → _Yo muero de sed_ `[no noun_id]`
  4. (auditory) You can go to the market → _Tú puedes ir al mercado_ `[noun_id=mercado]`
  5. (written) We (f) sleep eight hours at night → _cleaned:_ **We  sleep eight hours at night** → _Nosotras dormimos ocho horas de noche_ `[no noun_id]`
  6. (auditory) They return to the restaurant → _Ellos vuelven al restaurante_ `[noun_id=restaurante]`
  7. (written) You move to a new house → _Usted se mueve a una nueva casa_ `[noun_id=casa]`
  8. (auditory) We have lunch near the office → _Nosotros almorzamos cerca de la oficina_ `[noun_id=oficina]`
  9. (written) They (f) sleep in the house → _cleaned:_ **They  sleep in the house** → _Ellas duermen en la casa_ `[noun_id=casa]`
  10. (auditory) You all return to the city → _Ustedes vuelven a la ciudad_ `[noun_id=ciudad]`

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | mover, almorzar | verb chart + 10 drills |
| 2 | **drill** | morir, poder | verb chart + 10 drills |
| 3 | **chat** | mover, almorzar, morir, poder | chat (10 possible conjugations, user does 5) |
| 4 | **drill** | dormir, volver | verb chart + 10 drills |
| 5 | **chat** | dormir, volver | chat (10 possible conjugations, user does 5) |

---

## Present E→IE (GL 7)

### Current lessons

**`grammar_present_e_ie_1` — Present E→IE (1/3)** (lesson 1)

- **Verbs/rules:** cerrar, entender, pensar, querer, preferir, empezar
- **Current anatomy:** video chart (0a) + 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip; missing noun_id for: plan
- **Drill sentences (10):**
  1. (written) I close the door → _Yo cierro la puerta_ `[noun_id=puerta]`
  2. (auditory) You understand Spanish well → _Tú entiendes bien el español_ `[no noun_id]`
  3. (written) He thinks about the plan → _Él piensa en el plan_ `[no noun_id]`
  4. (auditory) She wants water → _Ella quiere agua_ `[noun_id=agua]`
  5. (written) You prefer coffee → _Usted prefiere el café_ `[noun_id=café]`
  6. (auditory) We start early → _Nosotros empezamos temprano_ `[no noun_id]`
  7. (written) We (f) close the store → _cleaned:_ **We  close the store** → _Nosotras cerramos la tienda_ `[noun_id=tienda]`
  8. (auditory) They understand the situation → _Ellos entienden la situación_ `[no noun_id]`
  9. (written) They (f) think about the house → _cleaned:_ **They  think about the house** → _Ellas piensan en la casa_ `[noun_id=casa]`
  10. (auditory) You all want to eat → _Ustedes quieren comer_ `[no noun_id]`

**`grammar_present_e_ie_2` — Present E→IE (2/3)** (lesson 2)

- **Verbs/rules:** cerrar, entender, pensar, querer, preferir, empezar
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip; missing noun_id for: día
- **Drill sentences (10):**
  1. (written) You close the window → _Tú cierras la ventana_ `[noun_id=ventana]`
  2. (auditory) I understand the problem → _Yo entiendo el problema_ `[no noun_id]`
  3. (written) She thinks about work → _Ella piensa en el trabajo_ `[noun_id=trabajo]`
  4. (auditory) He wants a coffee → _Él quiere un café_ `[noun_id=café]`
  5. (written) We prefer the park → _Nosotros preferimos el parque_ `[noun_id=parque]`
  6. (auditory) You start the day early → _Usted empieza el día temprano_ `[no noun_id]`
  7. (written) They close the door → _Ellos cierran la puerta_ `[noun_id=puerta]`
  8. (auditory) We (f) understand the situation → _cleaned:_ **We  understand the situation** → _Nosotras entendemos la situación_ `[no noun_id]`
  9. (written) You all think about it → _Ustedes piensan en eso_ `[no noun_id]`
  10. (auditory) They (f) want to go home → _cleaned:_ **They  want to go home** → _Ellas quieren ir a casa_ `[noun_id=casa]`

**`grammar_present_e_ie_3` — Present E→IE (3/3)** (lesson 3)

- **Verbs/rules:** cerrar, entender, pensar, querer, preferir, empezar
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip; missing noun_id for: plan
- **Drill sentences (10):**
  1. (written) He closes the shop at night → _Él cierra la tienda de noche_ `[noun_id=tienda]`
  2. (auditory) She understands Spanish → _Ella entiende español_ `[no noun_id]`
  3. (written) I think about the house → _Yo pienso en la casa_ `[noun_id=casa]`
  4. (auditory) You want a dog → _Tú quieres un perro_ `[noun_id=perro]`
  5. (written) We (f) prefer water → _cleaned:_ **We  prefer water** → _Nosotras preferimos agua_ `[noun_id=agua]`
  6. (auditory) They start the work early → _Ellos empiezan el trabajo temprano_ `[noun_id=trabajo]`
  7. (written) You close the door → _Usted cierra la puerta_ `[noun_id=puerta]`
  8. (auditory) We understand the plan → _Nosotros entendemos el plan_ `[no noun_id]`
  9. (written) They (f) prefer the city → _cleaned:_ **They  prefer the city** → _Ellas prefieren la ciudad_ `[noun_id=ciudad]`
  10. (auditory) You all start today → _Ustedes empiezan hoy_ `[no noun_id]`

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | cerrar, entender | verb chart + 10 drills |
| 2 | **drill** | pensar, querer | verb chart + 10 drills |
| 3 | **chat** | cerrar, entender, pensar, querer | chat (10 possible conjugations, user does 5) |
| 4 | **drill** | preferir, empezar | verb chart + 10 drills |
| 5 | **chat** | preferir, empezar | chat (10 possible conjugations, user does 5) |

---

## Present E→I (GL 8)

### Current lessons

**`grammar_present_e_i_1` — Present E→I (1/3)** (lesson 1)

- **Verbs/rules:** pedir, repetir, seguir, servir, vestir, elegir
- **Current anatomy:** video chart (0a) + 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) I order coffee at the restaurant → _Yo pido café en el restaurante_ `[noun_id=café]`
  2. (auditory) You repeat the word → _Tú repites la palabra_ `[no noun_id]`
  3. (written) He continues on the road → _Él sigue en el camino_ `[no noun_id]`
  4. (auditory) She serves the food → _Ella sirve la comida_ `[noun_id=comida]`
  5. (written) You dress the child → _Usted viste al niño_ `[no noun_id]`
  6. (auditory) We choose the book → _Nosotros elegimos el libro_ `[noun_id=libro]`
  7. (written) We (f) order water → _cleaned:_ **We  order water** → _Nosotras pedimos agua_ `[noun_id=agua]`
  8. (auditory) They repeat the sentence → _Ellos repiten la frase_ `[no noun_id]`
  9. (written) They (f) continue working → _cleaned:_ **They  continue working** → _Ellas siguen trabajando_ `[no noun_id]`
  10. (auditory) You all serve the coffee → _Ustedes sirven el café_ `[noun_id=café]`

**`grammar_present_e_i_2` — Present E→I (2/3)** (lesson 2)

- **Verbs/rules:** pedir, repetir, seguir, servir, vestir, elegir
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip; missing noun_id for: día, nombre, plan
- **Drill sentences (10):**
  1. (written) You order the food → _Tú pides la comida_ `[noun_id=comida]`
  2. (auditory) I repeat the name → _Yo repito el nombre_ `[no noun_id]`
  3. (written) She follows the plan → _Ella sigue el plan_ `[no noun_id]`
  4. (auditory) He serves the water → _Él sirve el agua_ `[noun_id=agua]`
  5. (written) We dress for work → _Nosotros vestimos para el trabajo_ `[noun_id=trabajo]`
  6. (auditory) You choose the restaurant → _Usted elige el restaurante_ `[noun_id=restaurante]`
  7. (written) They order at the restaurant → _Ellos piden en el restaurante_ `[noun_id=restaurante]`
  8. (auditory) We (f) repeat every day → _cleaned:_ **We  repeat every day** → _Nosotras repetimos cada día_ `[no noun_id]`
  9. (written) You all continue on the road → _Ustedes siguen en el camino_ `[no noun_id]`
  10. (auditory) They (f) serve the food → _cleaned:_ **They  serve the food** → _Ellas sirven la comida_ `[noun_id=comida]`

**`grammar_present_e_i_3` — Present E→I (3/3)** (lesson 3)

- **Verbs/rules:** pedir, repetir, seguir, servir, vestir, elegir
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) He orders a coffee → _Él pide un café_ `[noun_id=café]`
  2. (auditory) She repeats the word → _Ella repite la palabra_ `[no noun_id]`
  3. (written) I continue working at home → _Yo sigo trabajando en casa_ `[noun_id=casa]`
  4. (auditory) You serve the customers → _Tú sirves a los clientes_ `[no noun_id]`
  5. (written) We (f) dress well for work → _cleaned:_ **We  dress well for work** → _Nosotras vestimos bien para el trabajo_ `[noun_id=trabajo]`
  6. (auditory) They choose the best restaurant → _Ellos eligen el mejor restaurante_ `[noun_id=restaurante]`
  7. (written) You ask for the book → _Usted pide el libro_ `[noun_id=libro]`
  8. (auditory) We repeat the Spanish words → _Nosotros repetimos las palabras en español_ `[no noun_id]`
  9. (written) They (f) dress the children → _cleaned:_ **They  dress the children** → _Ellas visten a los niños_ `[no noun_id]`
  10. (auditory) You all choose the city → _Ustedes eligen la ciudad_ `[noun_id=ciudad]`

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | pedir, repetir | verb chart + 10 drills |
| 2 | **drill** | seguir, servir | verb chart + 10 drills |
| 3 | **chat** | pedir, repetir, seguir, servir | chat (10 possible conjugations, user does 5) |
| 4 | **drill** | vestir, elegir | verb chart + 10 drills |
| 5 | **chat** | vestir, elegir | chat (10 possible conjugations, user does 5) |

---

## Ir A + Infinitive (GL 9)

### Current lessons

**`grammar_ir_a_inf_1` — Ir A + Infinitive (1/3)** (lesson 1)

- **Verbs/rules:** hablar, comer, dormir, vivir, escribir, estudiar
- **Current anatomy:** video chart (0a) + 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip; 3 drills > 6 words — simplify (1 longer per lesson allowed)
- **Drill sentences (10):**
  1. (written) I am going to speak Spanish → _Voy a hablar español_ `[no noun_id]`
  2. (auditory) You are going to eat → _Vas a comer_ `[no noun_id]`
  3. (written) He is going to sleep → _Él va a dormir_ `[no noun_id]`
  4. (auditory) She is going to live here → _Ella va a vivir aquí_ `[no noun_id]`
  5. (written) You are going to write a letter → _Usted va a escribir una carta_ `[noun_id=carta]`
  6. (auditory) We are going to study → _Nosotros vamos a estudiar_ `[no noun_id]`
  7. (written) We (f) are going to speak Spanish → _cleaned:_ **We  are going to speak Spanish** → _Nosotras vamos a hablar español_ `[no noun_id]`
  8. (auditory) They are going to eat → _Ellos van a comer_ `[no noun_id]`
  9. (written) They (f) are going to sleep → _cleaned:_ **They  are going to sleep** → _Ellas van a dormir_ `[no noun_id]`
  10. (auditory) You all are going to live here → _Ustedes van a vivir aquí_ `[no noun_id]`

**`grammar_ir_a_inf_2` — Ir A + Infinitive (2/3)** (lesson 2)

- **Verbs/rules:** hablar, comer, dormir, vivir, escribir, estudiar
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip; 2 drills > 6 words — simplify (1 longer per lesson allowed)
- **Drill sentences (10):**
  1. (written) You are going to speak Spanish → _Tú vas a hablar español_ `[no noun_id]`
  2. (auditory) I am going to eat lunch → _Yo voy a comer_ `[no noun_id]`
  3. (written) She is going to sleep → _Ella va a dormir_ `[no noun_id]`
  4. (auditory) He is going to live here → _Él va a vivir aquí_ `[no noun_id]`
  5. (written) We are going to write a letter → _Nosotros vamos a escribir una carta_ `[noun_id=carta]`
  6. (auditory) You are going to study → _Usted va a estudiar_ `[no noun_id]`
  7. (written) They are going to speak Spanish → _Ellos van a hablar español_ `[no noun_id]`
  8. (auditory) We (f) are going to eat → _cleaned:_ **We  are going to eat** → _Nosotras vamos a comer_ `[no noun_id]`
  9. (written) You all are going to sleep → _Ustedes van a dormir_ `[no noun_id]`
  10. (auditory) They (f) are going to live here → _cleaned:_ **They  are going to live here** → _Ellas van a vivir aquí_ `[no noun_id]`

**`grammar_ir_a_inf_3` — Ir A + Infinitive (3/3)** (lesson 3)

- **Verbs/rules:** hablar, comer, dormir, vivir, escribir, estudiar
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 2/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) He is going to speak Spanish → _Él va a hablar español_ `[no noun_id]`
  2. (auditory) She is going to eat → _Ella va a comer_ `[no noun_id]`
  3. (written) I am going to sleep → _Yo voy a dormir_ `[no noun_id]`
  4. (auditory) You are going to live here → _Tú vas a vivir aquí_ `[no noun_id]`
  5. (written) We (f) are going to write a book → _cleaned:_ **We  are going to write a book** → _Nosotras vamos a escribir un libro_ `[noun_id=libro]`
  6. (auditory) They are going to study → _Ellos van a estudiar_ `[no noun_id]`
  7. (written) You are going to speak Spanish → _Usted va a hablar español_ `[no noun_id]`
  8. (auditory) We are going to eat → _Nosotros vamos a comer_ `[no noun_id]`
  9. (written) They (f) are going to write → _cleaned:_ **They  are going to write** → _Ellas van a escribir_ `[no noun_id]`
  10. (auditory) You all are going to study → _Ustedes van a estudiar_ `[no noun_id]`

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | hablar, comer | verb chart + 10 drills |
| 2 | **drill** | dormir, vivir | verb chart + 10 drills |
| 3 | **chat** | hablar, comer, dormir, vivir | chat (10 possible conjugations, user does 5) |
| 4 | **drill** | escribir, estudiar | verb chart + 10 drills |
| 5 | **chat** | escribir, estudiar | chat (10 possible conjugations, user does 5) |

---

## Gustar Part 1 (GL 10)

### Current lessons

**`grammar_gustar_1` — Gustar Part 1** (lesson 1)

- **Verbs/rules:** gusta
- **Current anatomy:** video chart (0a) + 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 1/10 drills have parenthetical clues — strip; missing noun_id for: música, plan
- **Drill sentences (10):**
  1. (written) I like the coffee → _Me gusta el café_ `[noun_id=café]`
  2. (auditory) You like the music → _Te gusta la música_ `[no noun_id]`
  3. (written) She likes the book → _Le gusta el libro_ `[noun_id=libro]`
  4. (auditory) He likes the water → _Le gusta el agua_ `[noun_id=agua]`
  5. (written) You (formal) like the food → _cleaned:_ **You  like the food** → _Le gusta la comida_ `[noun_id=comida]`
  6. (auditory) We like the plan → _Nos gusta el plan_ `[no noun_id]`
  7. (written) They like the park → _Les gusta el parque_ `[noun_id=parque]`
  8. (auditory) I like the dog → _Me gusta el perro_ `[noun_id=perro]`
  9. (written) You like the city → _Te gusta la ciudad_ `[noun_id=ciudad]`
  10. (auditory) She likes the house → _Le gusta la casa_ `[noun_id=casa]`

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | gusta | rule chart + 10 drills |
| 2 | **chat** | gusta | chat (10 possible conjugations, user does 5) |

---

## Gustar Part 2 (GL 10.3)

### Current lessons

**`grammar_gustar_2` — Gustar Part 2** (lesson 1)

- **Verbs/rules:** gustan
- **Current anatomy:** video chart (0a) + 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences (10):**
  1. (written) I like the cats → _Me gustan los gatos_ `[noun_id=gato]`
  2. (auditory) You like the books → _Te gustan los libros_ `[noun_id=libro]`
  3. (written) She likes the dogs → _Le gustan los perros_ `[noun_id=perro]`
  4. (auditory) He likes the cars → _Le gustan los carros_ `[noun_id=carro]`
  5. (written) We like the movies → _Nos gustan las películas_ `[no noun_id]`
  6. (auditory) They like the parks → _Les gustan los parques_ `[noun_id=parque]`
  7. (written) You all like the beaches → _Les gustan las playas_ `[noun_id=playa]`
  8. (auditory) I like the cities → _Me gustan las ciudades_ `[noun_id=ciudad]`
  9. (written) You like the colors → _Te gustan los colores_ `[noun_id=color]`
  10. (auditory) She likes the houses → _Le gustan las casas_ `[noun_id=casa]`

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | gustan | rule chart + 10 drills |
| 2 | **chat** | gustan | chat (10 possible conjugations, user does 5) |

---

## Gustar Part 3 (GL 10.6)

### Current lessons

**`grammar_gustar_3` — Gustar Part 3** (lesson 1)

- **Verbs/rules:** gusta, gustan
- **Current anatomy:** video chart (0a) + 10 drills (0b) + chat P2
- **Issues:** drill+chat in same lesson (chat should be its own lesson); 10/10 drills have parenthetical clues — strip; missing noun_id for: música
- **Drill sentences (10):**
  1. (written) I like the coffee (emphatic) → _cleaned:_ **I like the coffee** → _A mí me gusta el café_ `[noun_id=café]`
  2. (auditory) You like the music (emphatic) → _cleaned:_ **You like the music** → _A ti te gusta la música_ `[no noun_id]`
  3. (written) He likes the book (emphatic) → _cleaned:_ **He likes the book** → _A él le gusta el libro_ `[noun_id=libro]`
  4. (auditory) She likes the water (emphatic) → _cleaned:_ **She likes the water** → _A ella le gusta el agua_ `[noun_id=agua]`
  5. (written) You (formal) like the food (emphatic) → _cleaned:_ **You  like the food** → _A usted le gusta la comida_ `[noun_id=comida]`
  6. (auditory) We like the park (emphatic) → _cleaned:_ **We like the park** → _A nosotros nos gusta el parque_ `[noun_id=parque]`
  7. (written) They like the dog (emphatic) → _cleaned:_ **They like the dog** → _A ellos les gusta el perro_ `[noun_id=perro]`
  8. (auditory) You all like the city (emphatic) → _cleaned:_ **You all like the city** → _A ustedes les gusta la ciudad_ `[noun_id=ciudad]`
  9. (written) I like the house (emphatic) → _cleaned:_ **I like the house** → _A mí me gusta la casa_ `[noun_id=casa]`
  10. (auditory) She likes the car (emphatic) → _cleaned:_ **She likes the car** → _A ella le gusta el carro_ `[noun_id=carro]`

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | gusta, gustan | rule chart + 10 drills |
| 2 | **chat** | gusta, gustan | chat (10 possible conjugations, user does 5) |

---

## Tengo que / Me toca / Necesito (GL 11)

### Current lessons

**`grammar_modal_tengo_que` — Tengo Que + Inf (1/3)** (lesson 1)

- **Verbs/rules:** hablar, comer
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 4/10 drills have parenthetical clues — strip; 8 drills > 6 words — simplify (1 longer per lesson allowed)
- **Drill sentences (10):**
  1. (written) We (f) tengo que + verb the letter → _cleaned:_ **We  tengo que + verb the letter** → _Nosotras tenemos que comer la carta_ `[noun_id=carta]`
  2. (auditory) We (f) tengo que + verb Spanish → _cleaned:_ **We  tengo que + verb Spanish** → _Nosotras tenemos que hablar español_ `[no noun_id]`
  3. (written) You tengo que + verb water → _Tú tienes que comer agua_ `[noun_id=agua]`
  4. (auditory) They (f) tengo que + verb the bread → _cleaned:_ **They  tengo que + verb the bread** → _Ellas tienen que comer el pan_ `[noun_id=pan]`
  5. (written) You tengo que + verb the coffee → _Tú tienes que hablar el café_ `[noun_id=café]`
  6. (auditory) You (formal) tengo que + verb the music → _cleaned:_ **You  tengo que + verb the music** → _Usted tiene que hablar la música_ `[noun_id=música]`
  7. (written) I tengo que + verb the letter → _Yo tengo que comer la carta_ `[noun_id=carta]`
  8. (auditory) You all tengo que + verb the book → _Ustedes tienen que comer el libro_ `[noun_id=libro]`
  9. (written) She tengo que + verb water → _Ella tiene que comer agua_ `[noun_id=agua]`
  10. (auditory) I tengo que + verb at home → _Yo tengo que hablar en casa_ `[noun_id=casa]`

**`grammar_modal_me_toca` — Me Toca + Inf (2/3)** (lesson 2)

- **Verbs/rules:** vivir, estudiar
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 5/10 drills have parenthetical clues — strip; 9 drills > 6 words — simplify (1 longer per lesson allowed); missing noun_id for: canción, verdad
- **Drill sentences (10):**
  1. (written) You all me toca + verb the letter → _Ustedes les toca vivir la carta_ `[noun_id=carta]`
  2. (auditory) You all me toca + verb Spanish → _Ustedes les toca estudiar español_ `[no noun_id]`
  3. (written) She me toca + verb water → _Ella le toca vivir agua_ `[noun_id=agua]`
  4. (auditory) We (f) me toca + verb the bread → _cleaned:_ **We  me toca + verb the bread** → _Nosotras nos toca vivir el pan_ `[noun_id=pan]`
  5. (written) You me toca + verb the coffee → _Tú te toca estudiar el café_ `[noun_id=café]`
  6. (auditory) You (formal) me toca + verb the truth → _cleaned:_ **You  me toca + verb the truth** → _Usted le toca vivir la verdad_ `[no noun_id]`
  7. (written) We (f) me toca + verb the song → _cleaned:_ **We  me toca + verb the song** → _Nosotras nos toca estudiar la canción_ `[no noun_id]`
  8. (auditory) They (f) me toca + verb Spanish → _cleaned:_ **They  me toca + verb Spanish** → _Ellas les toca estudiar español_ `[no noun_id]`
  9. (written) You (formal) me toca + verb English → _cleaned:_ **You  me toca + verb English** → _Usted le toca estudiar inglés_ `[no noun_id]`
  10. (auditory) I me toca + verb the bread → _Yo me toca vivir el pan_ `[noun_id=pan]`

**`grammar_modal_necesito` — Necesito + Inf (3/3)** (lesson 3)

- **Verbs/rules:** dormir, escribir
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 5/10 drills have parenthetical clues — strip; 4 drills > 6 words — simplify (1 longer per lesson allowed); missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) They (f) necesito + verb the letter → _cleaned:_ **They  necesito + verb the letter** → _Ellas necesitan escribir la carta_ `[noun_id=carta]`
  2. (auditory) I necesito + verb the book → _Yo necesito dormir el libro_ `[noun_id=libro]`
  3. (written) They (f) necesito + verb water → _cleaned:_ **They  necesito + verb water** → _Ellas necesitan dormir agua_ `[noun_id=agua]`
  4. (auditory) You (formal) necesito + verb the bread → _cleaned:_ **You  necesito + verb the bread** → _Usted necesita dormir el pan_ `[noun_id=pan]`
  5. (written) She necesito + verb here → _Ella necesita escribir aquí_ `[no noun_id]`
  6. (auditory) You all necesito + verb the truth → _Ustedes necesitan escribir la verdad_ `[no noun_id]`
  7. (written) She necesito + verb the letter → _Ella necesita dormir la carta_ `[noun_id=carta]`
  8. (auditory) We (f) necesito + verb the book → _cleaned:_ **We  necesito + verb the book** → _Nosotras necesitamos escribir el libro_ `[noun_id=libro]`
  9. (written) You (formal) necesito + verb water → _cleaned:_ **You  necesito + verb water** → _Usted necesita escribir agua_ `[noun_id=agua]`
  10. (auditory) I necesito + verb the bread → _Yo necesito escribir el pan_ `[noun_id=pan]`

**`grammar_modal_chat_1` — Tengo Que / Me Toca — Voice Chat** (lesson 4)

- **Verbs/rules:** hablar, comer, vivir, estudiar
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

**`grammar_modal_chat_2` — Necesito — Voice Chat** (lesson 5)

- **Verbs/rules:** dormir, escribir
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | hablar, comer | verb chart + 10 drills |
| 2 | **drill** | vivir, estudiar | verb chart + 10 drills |
| 3 | **chat** | hablar, comer, vivir, estudiar | chat (10 possible conjugations, user does 5) |
| 4 | **drill** | dormir, escribir | verb chart + 10 drills |
| 5 | **chat** | dormir, escribir | chat (10 possible conjugations, user does 5) |

---

## Imperfect (GL 12)

### Current lessons

**`grammar_imperfect_1` — Imperfect (1)** (lesson 1)

- **Verbs/rules:** hablar, escuchar
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; 3 drills > 6 words — simplify (1 longer per lesson allowed); missing noun_id for: canción
- **Drill sentences (10):**
  1. (written) You all used to (imperfect) the song → _cleaned:_ **You all used to  the song** → _Ustedes hablaban la canción_ `[no noun_id]`
  2. (auditory) You (formal) used to (imperfect) Spanish → _cleaned:_ **You  used to  Spanish** → _Usted hablaba español_ `[no noun_id]`
  3. (written) We (f) used to (imperfect) English → _cleaned:_ **We  used to  English** → _Nosotras escuchábamos inglés_ `[no noun_id]`
  4. (auditory) We (f) used to (imperfect) at home → _cleaned:_ **We  used to  at home** → _Nosotras hablábamos en casa_ `[noun_id=casa]`
  5. (written) I used to (imperfect) the coffee → _cleaned:_ **I used to  the coffee** → _Yo hablaba el café_ `[noun_id=café]`
  6. (auditory) She used to (imperfect) the music → _cleaned:_ **She used to  the music** → _Ella escuchaba la música_ `[noun_id=música]`
  7. (written) I used to (imperfect) the song → _cleaned:_ **I used to  the song** → _Yo escuchaba la canción_ `[no noun_id]`
  8. (auditory) They (f) used to (imperfect) Spanish → _cleaned:_ **They  used to  Spanish** → _Ellas hablaban español_ `[no noun_id]`
  9. (written) You all used to (imperfect) English → _cleaned:_ **You all used to  English** → _Ustedes escuchaban inglés_ `[no noun_id]`
  10. (auditory) You (formal) used to (imperfect) at home → _cleaned:_ **You  used to  at home** → _Usted escuchaba en casa_ `[noun_id=casa]`

**`grammar_imperfect_2` — Imperfect (2)** (lesson 2)

- **Verbs/rules:** comer, vivir
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; 5 drills > 6 words — simplify (1 longer per lesson allowed); missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) You used to (imperfect) the letter → _cleaned:_ **You used to  the letter** → _Tú vivías la carta_ `[noun_id=carta]`
  2. (auditory) You all used to (imperfect) the book → _cleaned:_ **You all used to  the book** → _Ustedes vivían el libro_ `[noun_id=libro]`
  3. (written) She used to (imperfect) water → _cleaned:_ **She used to  water** → _Ella vivía agua_ `[noun_id=agua]`
  4. (auditory) We (f) used to (imperfect) the bread → _cleaned:_ **We  used to  the bread** → _Nosotras comíamos el pan_ `[noun_id=pan]`
  5. (written) She used to (imperfect) here → _cleaned:_ **She used to  here** → _Ella comía aquí_ `[no noun_id]`
  6. (auditory) They (f) used to (imperfect) the truth → _cleaned:_ **They  used to  the truth** → _Ellas comían la verdad_ `[no noun_id]`
  7. (written) They (f) used to (imperfect) the letter → _cleaned:_ **They  used to  the letter** → _Ellas vivían la carta_ `[noun_id=carta]`
  8. (auditory) You all used to (imperfect) the book → _cleaned:_ **You all used to  the book** → _Ustedes comían el libro_ `[noun_id=libro]`
  9. (written) We (f) used to (imperfect) water → _cleaned:_ **We  used to  water** → _Nosotras vivíamos agua_ `[noun_id=agua]`
  10. (auditory) You used to (imperfect) the bread → _cleaned:_ **You used to  the bread** → _Tú comías el pan_ `[noun_id=pan]`

**`grammar_imperfect_3` — Imperfect — Chat 1** (lesson 3)

- **Verbs/rules:** hablar, escuchar, comer, vivir
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

**`grammar_imperfect_4` — Imperfect (4)** (lesson 4)

- **Verbs/rules:** ir, ser
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; 3 drills > 6 words — simplify (1 longer per lesson allowed); missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) You used to (imperfect) the letter → _cleaned:_ **You used to  the letter** → _Tú eras la carta_ `[noun_id=carta]`
  2. (auditory) I used to (imperfect) the book → _cleaned:_ **I used to  the book** → _Yo iba el libro_ `[noun_id=libro]`
  3. (written) You (formal) used to (imperfect) water → _cleaned:_ **You  used to  water** → _Usted era agua_ `[noun_id=agua]`
  4. (auditory) You (formal) used to (imperfect) the bread → _cleaned:_ **You  used to  the bread** → _Usted iba el pan_ `[noun_id=pan]`
  5. (written) You used to (imperfect) here → _cleaned:_ **You used to  here** → _Tú ibas aquí_ `[no noun_id]`
  6. (auditory) I used to (imperfect) the truth → _cleaned:_ **I used to  the truth** → _Yo era la verdad_ `[no noun_id]`
  7. (written) You all used to (imperfect) the letter → _cleaned:_ **You all used to  the letter** → _Ustedes eran la carta_ `[noun_id=carta]`
  8. (auditory) She used to (imperfect) the book → _cleaned:_ **She used to  the book** → _Ella era el libro_ `[noun_id=libro]`
  9. (written) She used to (imperfect) water → _cleaned:_ **She used to  water** → _Ella iba agua_ `[noun_id=agua]`
  10. (auditory) They (f) used to (imperfect) the bread → _cleaned:_ **They  used to  the bread** → _Ellas eran el pan_ `[noun_id=pan]`

**`grammar_imperfect_5` — Imperfect (5)** (lesson 5)

- **Verbs/rules:** ver, escribir
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; 5 drills > 6 words — simplify (1 longer per lesson allowed); missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) They (f) used to (imperfect) the letter → _cleaned:_ **They  used to  the letter** → _Ellas escribían la carta_ `[noun_id=carta]`
  2. (auditory) You all used to (imperfect) the book → _cleaned:_ **You all used to  the book** → _Ustedes veían el libro_ `[noun_id=libro]`
  3. (written) You used to (imperfect) water → _cleaned:_ **You used to  water** → _Tú escribías agua_ `[noun_id=agua]`
  4. (auditory) You (formal) used to (imperfect) the bread → _cleaned:_ **You  used to  the bread** → _Usted escribía el pan_ `[noun_id=pan]`
  5. (written) We (f) used to (imperfect) here → _cleaned:_ **We  used to  here** → _Nosotras veíamos aquí_ `[no noun_id]`
  6. (auditory) You (formal) used to (imperfect) the truth → _cleaned:_ **You  used to  the truth** → _Usted veía la verdad_ `[no noun_id]`
  7. (written) She used to (imperfect) the letter → _cleaned:_ **She used to  the letter** → _Ella escribía la carta_ `[noun_id=carta]`
  8. (auditory) I used to (imperfect) the book → _cleaned:_ **I used to  the book** → _Yo veía el libro_ `[noun_id=libro]`
  9. (written) We (f) used to (imperfect) water → _cleaned:_ **We  used to  water** → _Nosotras escribíamos agua_ `[noun_id=agua]`
  10. (auditory) They (f) used to (imperfect) the bread → _cleaned:_ **They  used to  the bread** → _Ellas veían el pan_ `[noun_id=pan]`

**`grammar_imperfect_6` — Imperfect — Chat 2** (lesson 6)

- **Verbs/rules:** ir, ser, ver, escribir
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | hablar, escuchar | verb chart + 10 drills |
| 2 | **drill** | comer, vivir | verb chart + 10 drills |
| 3 | **chat** | hablar, escuchar, comer, vivir | chat (10 possible conjugations, user does 5) |
| 4 | **drill** | ir, ser | verb chart + 10 drills |
| 5 | **drill** | ver, escribir | verb chart + 10 drills |
| 6 | **chat** | ir, ser, ver, escribir | chat (10 possible conjugations, user does 5) |

---

## Reflexive (GL 13)

### Current lessons

**`grammar_reflexive_1` — Reflexive (1)** (lesson 1)

- **Verbs/rules:** lavarse, llamarse
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) We (f) (reflexive present) the letter → _cleaned:_ **We   the letter** → _Nosotras nos lavamos la carta_ `[noun_id=carta]`
  2. (auditory) We (f) (reflexive present) the book → _cleaned:_ **We   the book** → _Nosotras nos llamamos el libro_ `[noun_id=libro]`
  3. (written) They (f) (reflexive present) water → _cleaned:_ **They   water** → _Ellas se llaman agua_ `[noun_id=agua]`
  4. (auditory) You (reflexive present) the bread → _cleaned:_ **You  the bread** → _Tú te llamas el pan_ `[noun_id=pan]`
  5. (written) You (formal) (reflexive present) here → _cleaned:_ **You   here** → _Usted se llama aquí_ `[no noun_id]`
  6. (auditory) I (reflexive present) the truth → _cleaned:_ **I  the truth** → _Yo me llamo la verdad_ `[no noun_id]`
  7. (written) They (f) (reflexive present) the letter → _cleaned:_ **They   the letter** → _Ellas se lavan la carta_ `[noun_id=carta]`
  8. (auditory) You (reflexive present) the book → _cleaned:_ **You  the book** → _Tú te lavas el libro_ `[noun_id=libro]`
  9. (written) She (reflexive present) water → _cleaned:_ **She  water** → _Ella se lava agua_ `[noun_id=agua]`
  10. (auditory) You (formal) (reflexive present) the bread → _cleaned:_ **You   the bread** → _Usted se lava el pan_ `[noun_id=pan]`

**`grammar_reflexive_2` — Reflexive (2)** (lesson 2)

- **Verbs/rules:** levantarse, ducharse
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) You (reflexive present) the letter → _cleaned:_ **You  the letter** → _Tú te duchas la carta_ `[noun_id=carta]`
  2. (auditory) She (reflexive present) the book → _cleaned:_ **She  the book** → _Ella se ducha el libro_ `[noun_id=libro]`
  3. (written) You (formal) (reflexive present) water → _cleaned:_ **You   water** → _Usted se levanta agua_ `[noun_id=agua]`
  4. (auditory) They (f) (reflexive present) the bread → _cleaned:_ **They   the bread** → _Ellas se levantan el pan_ `[noun_id=pan]`
  5. (written) You all (reflexive present) here → _cleaned:_ **You all  here** → _Ustedes se duchan aquí_ `[no noun_id]`
  6. (auditory) We (f) (reflexive present) the truth → _cleaned:_ **We   the truth** → _Nosotras nos levantamos la verdad_ `[no noun_id]`
  7. (written) You (reflexive present) the letter → _cleaned:_ **You  the letter** → _Tú te levantas la carta_ `[noun_id=carta]`
  8. (auditory) She (reflexive present) the book → _cleaned:_ **She  the book** → _Ella se levanta el libro_ `[noun_id=libro]`
  9. (written) I (reflexive present) water → _cleaned:_ **I  water** → _Yo me levanto agua_ `[noun_id=agua]`
  10. (auditory) You (formal) (reflexive present) the bread → _cleaned:_ **You   the bread** → _Usted se ducha el pan_ `[noun_id=pan]`

**`grammar_reflexive_3` — Reflexive — Chat 1** (lesson 3)

- **Verbs/rules:** lavarse, llamarse, levantarse, ducharse
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

**`grammar_reflexive_4` — Reflexive (4)** (lesson 4)

- **Verbs/rules:** despertarse, acostarse
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) They (f) (reflexive present) the letter → _cleaned:_ **They   the letter** → _Ellas se despiertan la carta_ `[noun_id=carta]`
  2. (auditory) You (formal) (reflexive present) the book → _cleaned:_ **You   the book** → _Usted se acuesta el libro_ `[noun_id=libro]`
  3. (written) You (formal) (reflexive present) water → _cleaned:_ **You   water** → _Usted se despierta agua_ `[noun_id=agua]`
  4. (auditory) They (f) (reflexive present) the bread → _cleaned:_ **They   the bread** → _Ellas se acuestan el pan_ `[noun_id=pan]`
  5. (written) I (reflexive present) here → _cleaned:_ **I  here** → _Yo me acuesto aquí_ `[no noun_id]`
  6. (auditory) She (reflexive present) the truth → _cleaned:_ **She  the truth** → _Ella se despierta la verdad_ `[no noun_id]`
  7. (written) She (reflexive present) the letter → _cleaned:_ **She  the letter** → _Ella se acuesta la carta_ `[noun_id=carta]`
  8. (auditory) You (reflexive present) the book → _cleaned:_ **You  the book** → _Tú te acuestas el libro_ `[noun_id=libro]`
  9. (written) I (reflexive present) water → _cleaned:_ **I  water** → _Yo me despierto agua_ `[noun_id=agua]`
  10. (auditory) You all (reflexive present) the bread → _cleaned:_ **You all  the bread** → _Ustedes se despiertan el pan_ `[noun_id=pan]`

**`grammar_reflexive_5` — Reflexive (5)** (lesson 5)

- **Verbs/rules:** vestirse, sentarse
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) They (f) (reflexive present) the letter → _cleaned:_ **They   the letter** → _Ellas se sientan la carta_ `[noun_id=carta]`
  2. (auditory) I (reflexive present) the book → _cleaned:_ **I  the book** → _Yo me visto el libro_ `[noun_id=libro]`
  3. (written) You all (reflexive present) water → _cleaned:_ **You all  water** → _Ustedes se sientan agua_ `[noun_id=agua]`
  4. (auditory) You (reflexive present) the bread → _cleaned:_ **You  the bread** → _Tú te vistes el pan_ `[noun_id=pan]`
  5. (written) You (formal) (reflexive present) here → _cleaned:_ **You   here** → _Usted se sienta aquí_ `[no noun_id]`
  6. (auditory) They (f) (reflexive present) the truth → _cleaned:_ **They   the truth** → _Ellas se visten la verdad_ `[no noun_id]`
  7. (written) We (f) (reflexive present) the letter → _cleaned:_ **We   the letter** → _Nosotras nos vestemos la carta_ `[noun_id=carta]`
  8. (auditory) I (reflexive present) the book → _cleaned:_ **I  the book** → _Yo me siento el libro_ `[noun_id=libro]`
  9. (written) She (reflexive present) water → _cleaned:_ **She  water** → _Ella se sienta agua_ `[noun_id=agua]`
  10. (auditory) You all (reflexive present) the bread → _cleaned:_ **You all  the bread** → _Ustedes se visten el pan_ `[noun_id=pan]`

**`grammar_reflexive_6` — Reflexive — Chat 2** (lesson 6)

- **Verbs/rules:** despertarse, acostarse, vestirse, sentarse
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | lavarse, llamarse | verb chart + 10 drills |
| 2 | **drill** | levantarse, ducharse | verb chart + 10 drills |
| 3 | **chat** | lavarse, llamarse, levantarse, ducharse | chat (10 possible conjugations, user does 5) |
| 4 | **drill** | despertarse, acostarse | verb chart + 10 drills |
| 5 | **drill** | vestirse, sentarse | verb chart + 10 drills |
| 6 | **chat** | despertarse, acostarse, vestirse, sentarse | chat (10 possible conjugations, user does 5) |

---

## Imperatives (GL 13.5)

### Current lessons

**`grammar_imperatives_1` — Imperatives (1/2)** (lesson 1)

- **Verbs/rules:** hablar, comer, vivir
- **Current anatomy:** 10 drills (0b) + chat P3
- **Issues:** uses P3 (no-hints chat) — consolidate to single 'chat'; 10/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) Speak slowly (tú) → _cleaned:_ **Speak slowly** → _Habla despacio_ `[no noun_id]`
  2. (auditory) Speak here (usted) → _cleaned:_ **Speak here** → _Hable aquí_ `[no noun_id]`
  3. (written) Let's speak now (nosotros) → _cleaned:_ **Let's speak now** → _Hablemos ahora_ `[no noun_id]`
  4. (auditory) Eat the bread (tú) → _cleaned:_ **Eat the bread** → _Come el pan_ `[noun_id=pan]`
  5. (written) Eat the food (usted) → _cleaned:_ **Eat the food** → _Coma la comida_ `[noun_id=comida]`
  6. (auditory) Let's eat together (nosotros) → _cleaned:_ **Let's eat together** → _Comamos juntos_ `[no noun_id]`
  7. (written) You all eat now (ustedes) → _cleaned:_ **You all eat now** → _Coman ahora_ `[no noun_id]`
  8. (auditory) Live well (tú) → _cleaned:_ **Live well** → _Vive bien_ `[no noun_id]`
  9. (written) Live here (usted) → _cleaned:_ **Live here** → _Viva aquí_ `[no noun_id]`
  10. (auditory) Let's live well (nosotros) → _cleaned:_ **Let's live well** → _Vivamos bien_ `[no noun_id]`

**`grammar_imperatives_2` — Imperatives (2/2)** (lesson 2)

- **Verbs/rules:** ir, ser, tener
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 10/10 drills have parenthetical clues — strip; missing noun_id for: plan
- **Drill sentences (10):**
  1. (written) Go now (tú) → _cleaned:_ **Go now** → _Ve ahora_ `[no noun_id]`
  2. (auditory) Go to the park (usted) → _cleaned:_ **Go to the park** → _Vaya al parque_ `[noun_id=parque]`
  3. (written) Let's go (nosotros) → _cleaned:_ **Let's go** → _Vamos_ `[no noun_id]`
  4. (auditory) You all go now (ustedes) → _cleaned:_ **You all go now** → _Vayan ahora_ `[no noun_id]`
  5. (written) Be calm (tú) → _cleaned:_ **Be calm** → _Sé tranquilo_ `[no noun_id]`
  6. (auditory) Be here (usted) → _cleaned:_ **Be here** → _Sea aquí_ `[no noun_id]`
  7. (written) Let's be calm (nosotros) → _cleaned:_ **Let's be calm** → _Seamos tranquilos_ `[no noun_id]`
  8. (auditory) Have the book (tú) → _cleaned:_ **Have the book** → _Ten el libro_ `[noun_id=libro]`
  9. (written) Have patience (usted) → _cleaned:_ **Have patience** → _Tenga paciencia_ `[no noun_id]`
  10. (auditory) You all have the plan (ustedes) → _cleaned:_ **You all have the plan** → _Tengan el plan_ `[no noun_id]`

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | hablar, comer | verb chart + 10 drills |
| 2 | **drill** | vivir, ir | verb chart + 10 drills |
| 3 | **chat** | hablar, comer, vivir, ir | chat (10 possible conjugations, user does 5) |
| 4 | **drill** | ser, tener | verb chart + 10 drills |
| 5 | **chat** | ser, tener | chat (10 possible conjugations, user does 5) |

---

## Future Simple (GL 14)

### Current lessons

**`grammar_future_1` — Future Simple (1)** (lesson 1)

- **Verbs/rules:** hablar, comer
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 6/10 drills have parenthetical clues — strip; missing noun_id for: canción, verdad
- **Drill sentences (10):**
  1. (written) They (f) will the song → _cleaned:_ **They  will the song** → _Ellas hablarán la canción_ `[no noun_id]`
  2. (auditory) You (formal) will the book → _cleaned:_ **You  will the book** → _Usted comerá el libro_ `[noun_id=libro]`
  3. (written) We (f) will water → _cleaned:_ **We  will water** → _Nosotras comeremos agua_ `[noun_id=agua]`
  4. (auditory) You all will at home → _Ustedes hablarán en casa_ `[noun_id=casa]`
  5. (written) We (f) will the coffee → _cleaned:_ **We  will the coffee** → _Nosotras hablaremos el café_ `[noun_id=café]`
  6. (auditory) You will the truth → _Tú comerás la verdad_ `[no noun_id]`
  7. (written) You (formal) will the song → _cleaned:_ **You  will the song** → _Usted hablará la canción_ `[no noun_id]`
  8. (auditory) They (f) will the book → _cleaned:_ **They  will the book** → _Ellas comerán el libro_ `[noun_id=libro]`
  9. (written) You all will water → _Ustedes comerán agua_ `[noun_id=agua]`
  10. (auditory) I will the bread → _Yo comeré el pan_ `[noun_id=pan]`

**`grammar_future_2` — Future Simple (2)** (lesson 2)

- **Verbs/rules:** vivir, estudiar
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 4/10 drills have parenthetical clues — strip; missing noun_id for: canción, verdad
- **Drill sentences (10):**
  1. (written) You (formal) will the letter → _cleaned:_ **You  will the letter** → _Usted vivirá la carta_ `[noun_id=carta]`
  2. (auditory) You will Spanish → _Tú estudiarás español_ `[no noun_id]`
  3. (written) She will English → _Ella estudiará inglés_ `[no noun_id]`
  4. (auditory) You will the bread → _Tú vivirás el pan_ `[noun_id=pan]`
  5. (written) She will here → _Ella vivirá aquí_ `[no noun_id]`
  6. (auditory) We (f) will the truth → _cleaned:_ **We  will the truth** → _Nosotras viviremos la verdad_ `[no noun_id]`
  7. (written) We (f) will the song → _cleaned:_ **We  will the song** → _Nosotras estudiaremos la canción_ `[no noun_id]`
  8. (auditory) You all will the book → _Ustedes vivirán el libro_ `[noun_id=libro]`
  9. (written) You (formal) will English → _cleaned:_ **You  will English** → _Usted estudiará inglés_ `[no noun_id]`
  10. (auditory) You all will at home → _Ustedes estudiarán en casa_ `[noun_id=casa]`

**`grammar_future_3` — Future Simple — Chat 1** (lesson 3)

- **Verbs/rules:** hablar, comer, vivir, estudiar
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

**`grammar_future_4` — Future Simple (4)** (lesson 4)

- **Verbs/rules:** tener, hacer
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 5/10 drills have parenthetical clues — strip; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) You all will the letter → _Ustedes harán la carta_ `[noun_id=carta]`
  2. (auditory) We (f) will the book → _cleaned:_ **We  will the book** → _Nosotras haremos el libro_ `[noun_id=libro]`
  3. (written) They (f) will water → _cleaned:_ **They  will water** → _Ellas tendrán agua_ `[noun_id=agua]`
  4. (auditory) You (formal) will the bread → _cleaned:_ **You  will the bread** → _Usted tendrá el pan_ `[noun_id=pan]`
  5. (written) I will here → _Yo tendré aquí_ `[no noun_id]`
  6. (auditory) You (formal) will the truth → _cleaned:_ **You  will the truth** → _Usted hará la verdad_ `[no noun_id]`
  7. (written) She will the letter → _Ella tendrá la carta_ `[noun_id=carta]`
  8. (auditory) They (f) will the book → _cleaned:_ **They  will the book** → _Ellas harán el libro_ `[noun_id=libro]`
  9. (written) I will water → _Yo haré agua_ `[noun_id=agua]`
  10. (auditory) You will the bread → _Tú harás el pan_ `[noun_id=pan]`

**`grammar_future_5` — Future Simple (5)** (lesson 5)

- **Verbs/rules:** decir, poder
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 4/10 drills have parenthetical clues — strip; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) I will the letter → _Yo podré la carta_ `[noun_id=carta]`
  2. (auditory) You will the book → _Tú dirás el libro_ `[noun_id=libro]`
  3. (written) You (formal) will water → _cleaned:_ **You  will water** → _Usted dirá agua_ `[noun_id=agua]`
  4. (auditory) You (formal) will the bread → _cleaned:_ **You  will the bread** → _Usted podrá el pan_ `[noun_id=pan]`
  5. (written) She will here → _Ella dirá aquí_ `[no noun_id]`
  6. (auditory) They (f) will the truth → _cleaned:_ **They  will the truth** → _Ellas dirán la verdad_ `[no noun_id]`
  7. (written) I will the letter → _Yo diré la carta_ `[noun_id=carta]`
  8. (auditory) You all will the book → _Ustedes podrán el libro_ `[noun_id=libro]`
  9. (written) We (f) will water → _cleaned:_ **We  will water** → _Nosotras diremos agua_ `[noun_id=agua]`
  10. (auditory) She will the bread → _Ella podrá el pan_ `[noun_id=pan]`

**`grammar_future_6` — Future Simple — Chat 2** (lesson 6)

- **Verbs/rules:** tener, hacer, decir, poder
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

**`grammar_future_7` — Future Simple (7)** (lesson 7)

- **Verbs/rules:** saber, querer
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 4/10 drills have parenthetical clues — strip; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) You all will the letter → _Ustedes querrán la carta_ `[noun_id=carta]`
  2. (auditory) She will the book → _Ella sabrá el libro_ `[noun_id=libro]`
  3. (written) We (f) will water → _cleaned:_ **We  will water** → _Nosotras querremos agua_ `[noun_id=agua]`
  4. (auditory) They (f) will the bread → _cleaned:_ **They  will the bread** → _Ellas querrán el pan_ `[noun_id=pan]`
  5. (written) I will here → _Yo sabré aquí_ `[no noun_id]`
  6. (auditory) I will the truth → _Yo querré la verdad_ `[no noun_id]`
  7. (written) We (f) will the letter → _cleaned:_ **We  will the letter** → _Nosotras sabremos la carta_ `[noun_id=carta]`
  8. (auditory) You will the book → _Tú sabrás el libro_ `[noun_id=libro]`
  9. (written) They (f) will water → _cleaned:_ **They  will water** → _Ellas sabrán agua_ `[noun_id=agua]`
  10. (auditory) She will the bread → _Ella querrá el pan_ `[noun_id=pan]`

**`grammar_future_8` — Future Simple (8)** (lesson 8)

- **Verbs/rules:** venir, salir
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 4/10 drills have parenthetical clues — strip; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) You will the letter → _Tú saldrás la carta_ `[noun_id=carta]`
  2. (auditory) I will the book → _Yo vendré el libro_ `[noun_id=libro]`
  3. (written) We (f) will water → _cleaned:_ **We  will water** → _Nosotras vendremos agua_ `[noun_id=agua]`
  4. (auditory) She will the bread → _Ella saldrá el pan_ `[noun_id=pan]`
  5. (written) We (f) will here → _cleaned:_ **We  will here** → _Nosotras saldremos aquí_ `[no noun_id]`
  6. (auditory) You (formal) will the truth → _cleaned:_ **You  will the truth** → _Usted vendrá la verdad_ `[no noun_id]`
  7. (written) You (formal) will the letter → _cleaned:_ **You  will the letter** → _Usted saldrá la carta_ `[noun_id=carta]`
  8. (auditory) You all will the book → _Ustedes vendrán el libro_ `[noun_id=libro]`
  9. (written) She will water → _Ella vendrá agua_ `[noun_id=agua]`
  10. (auditory) You will the bread → _Tú vendrás el pan_ `[noun_id=pan]`

**`grammar_future_9` — Future Simple — Chat 3** (lesson 9)

- **Verbs/rules:** saber, querer, venir, salir
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | hablar, comer | verb chart + 10 drills |
| 2 | **drill** | vivir, estudiar | verb chart + 10 drills |
| 3 | **chat** | hablar, comer, vivir, estudiar | chat (10 possible conjugations, user does 5) |
| 4 | **drill** | tener, hacer | verb chart + 10 drills |
| 5 | **drill** | decir, poder | verb chart + 10 drills |
| 6 | **chat** | tener, hacer, decir, poder | chat (10 possible conjugations, user does 5) |
| 7 | **drill** | saber, querer | verb chart + 10 drills |
| 8 | **drill** | venir, salir | verb chart + 10 drills |
| 9 | **chat** | saber, querer, venir, salir | chat (10 possible conjugations, user does 5) |

---

## Conditional (GL 15)

### Current lessons

**`grammar_conditional_1` — Conditional (1)** (lesson 1)

- **Verbs/rules:** hablar, comer
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 4/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) You all would the letter → _Ustedes comerían la carta_ `[noun_id=carta]`
  2. (auditory) She would the book → _Ella comería el libro_ `[noun_id=libro]`
  3. (written) I would English → _Yo hablaría inglés_ `[no noun_id]`
  4. (auditory) She would at home → _Ella hablaría en casa_ `[noun_id=casa]`
  5. (written) We (f) would here → _cleaned:_ **We  would here** → _Nosotras comeríamos aquí_ `[no noun_id]`
  6. (auditory) You all would the music → _Ustedes hablarían la música_ `[noun_id=música]`
  7. (written) They (f) would the letter → _cleaned:_ **They  would the letter** → _Ellas comerían la carta_ `[noun_id=carta]`
  8. (auditory) You (formal) would the book → _cleaned:_ **You  would the book** → _Usted comería el libro_ `[noun_id=libro]`
  9. (written) They (f) would English → _cleaned:_ **They  would English** → _Ellas hablarían inglés_ `[no noun_id]`
  10. (auditory) You would at home → _Tú hablarías en casa_ `[noun_id=casa]`

**`grammar_conditional_2` — Conditional (2)** (lesson 2)

- **Verbs/rules:** vivir, estudiar
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 3/10 drills have parenthetical clues — strip; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) I would the letter → _Yo viviría la carta_ `[noun_id=carta]`
  2. (auditory) You all would Spanish → _Ustedes estudiarían español_ `[no noun_id]`
  3. (written) You would water → _Tú vivirías agua_ `[noun_id=agua]`
  4. (auditory) You (formal) would at home → _cleaned:_ **You  would at home** → _Usted estudiaría en casa_ `[noun_id=casa]`
  5. (written) You would the coffee → _Tú estudiarías el café_ `[noun_id=café]`
  6. (auditory) She would the truth → _Ella viviría la verdad_ `[no noun_id]`
  7. (written) They (f) would the letter → _cleaned:_ **They  would the letter** → _Ellas vivirían la carta_ `[noun_id=carta]`
  8. (auditory) You all would the book → _Ustedes vivirían el libro_ `[noun_id=libro]`
  9. (written) You (formal) would water → _cleaned:_ **You  would water** → _Usted viviría agua_ `[noun_id=agua]`
  10. (auditory) She would at home → _Ella estudiaría en casa_ `[noun_id=casa]`

**`grammar_conditional_3` — Conditional — Chat 1** (lesson 3)

- **Verbs/rules:** hablar, comer, vivir, estudiar
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

**`grammar_conditional_4` — Conditional (4)** (lesson 4)

- **Verbs/rules:** tener, hacer
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 3/10 drills have parenthetical clues — strip; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) They (f) would the letter → _cleaned:_ **They  would the letter** → _Ellas tendrían la carta_ `[noun_id=carta]`
  2. (auditory) You would the book → _Tú tendrías el libro_ `[noun_id=libro]`
  3. (written) She would water → _Ella haría agua_ `[noun_id=agua]`
  4. (auditory) They (f) would the bread → _cleaned:_ **They  would the bread** → _Ellas harían el pan_ `[noun_id=pan]`
  5. (written) You all would here → _Ustedes harían aquí_ `[no noun_id]`
  6. (auditory) I would the truth → _Yo tendría la verdad_ `[no noun_id]`
  7. (written) We (f) would the letter → _cleaned:_ **We  would the letter** → _Nosotras tendríamos la carta_ `[noun_id=carta]`
  8. (auditory) You would the book → _Tú harías el libro_ `[noun_id=libro]`
  9. (written) You all would water → _Ustedes tendrían agua_ `[noun_id=agua]`
  10. (auditory) I would the bread → _Yo haría el pan_ `[noun_id=pan]`

**`grammar_conditional_5` — Conditional (5)** (lesson 5)

- **Verbs/rules:** decir, poder
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 3/10 drills have parenthetical clues — strip; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) You would the letter → _Tú podrías la carta_ `[noun_id=carta]`
  2. (auditory) I would the book → _Yo podría el libro_ `[noun_id=libro]`
  3. (written) They (f) would water → _cleaned:_ **They  would water** → _Ellas dirían agua_ `[noun_id=agua]`
  4. (auditory) You all would the bread → _Ustedes dirían el pan_ `[noun_id=pan]`
  5. (written) She would here → _Ella diría aquí_ `[no noun_id]`
  6. (auditory) We (f) would the truth → _cleaned:_ **We  would the truth** → _Nosotras podríamos la verdad_ `[no noun_id]`
  7. (written) You all would the letter → _Ustedes podrían la carta_ `[noun_id=carta]`
  8. (auditory) You would the book → _Tú dirías el libro_ `[noun_id=libro]`
  9. (written) I would water → _Yo diría agua_ `[noun_id=agua]`
  10. (auditory) You (formal) would the bread → _cleaned:_ **You  would the bread** → _Usted podría el pan_ `[noun_id=pan]`

**`grammar_conditional_6` — Conditional — Chat 2** (lesson 6)

- **Verbs/rules:** tener, hacer, decir, poder
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | hablar, comer | verb chart + 10 drills |
| 2 | **drill** | vivir, estudiar | verb chart + 10 drills |
| 3 | **chat** | hablar, comer, vivir, estudiar | chat (10 possible conjugations, user does 5) |
| 4 | **drill** | tener, hacer | verb chart + 10 drills |
| 5 | **drill** | decir, poder | verb chart + 10 drills |
| 6 | **chat** | tener, hacer, decir, poder | chat (10 possible conjugations, user does 5) |

---

## Preterite vs Imperfect (GL 16)

### Current lessons

**`grammar_pret_vs_imperfect` — Preterite vs. Imperfect** (lesson 1)

- **Verbs/rules:** preterite, imperfect
- **Current anatomy:** chat P2
- **Issues:** CHAT-ONLY (no teaching before chat); 10 drill_sentences but 0b:off → dead data; 10/10 drills have parenthetical clues — strip; 6 drills > 6 words — simplify (1 longer per lesson allowed); missing noun_id for: hora
- **Drill sentences (10):**
  1. (written) I was reading when she arrived (background + completed) → _cleaned:_ **I was reading when she arrived** → _Yo leía cuando ella llegó_ `[no noun_id]`
  2. (auditory) We used to play every day (habitual) → _cleaned:_ **We used to play every day** → _Jugábamos todos los días_ `[no noun_id]`
  3. (written) He ate the bread (completed) → _cleaned:_ **He ate the bread** → _Él comió el pan_ `[noun_id=pan]`
  4. (auditory) She was eating when I called (background) → _cleaned:_ **She was eating when I called** → _Ella comía cuando yo llamé_ `[no noun_id]`
  5. (written) It was raining all morning (ongoing) → _cleaned:_ **It was raining all morning** → _Llovía toda la mañana_ `[no noun_id]`
  6. (auditory) It rained yesterday (completed) → _cleaned:_ **It rained yesterday** → _Llovió ayer_ `[no noun_id]`
  7. (written) I was tired (state) → _cleaned:_ **I was tired** → _Yo estaba cansado_ `[no noun_id]`
  8. (auditory) I was tired for an hour (delimited state → preterite) → _cleaned:_ **I was tired for an hour** → _Estuve cansado por una hora_ `[no noun_id]`
  9. (written) When I was a kid, I used to live in Mexico (habitual past) → _cleaned:_ **When I was a kid, I used to live in Mexico** → _Cuando era niño, vivía en México_ `[no noun_id]`
  10. (auditory) She lived in Mexico for five years (completed) → _cleaned:_ **She lived in Mexico for five years** → _Ella vivió en México por cinco años_ `[no noun_id]`

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | preterite, imperfect | rule chart + 10 drills |
| 2 | **chat** | preterite, imperfect | chat (10 possible conjugations, user does 5) |

---

## Preterite Regular (GL 17)

### Current lessons

**`grammar_preterite_regular_1` — Preterite Regular (1/3)** (lesson 1)

- **Verbs/rules:** hablar, encontrar, comer, unir, beber, salir
- **Current anatomy:** video chart (0a) + 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 3/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) I spoke Spanish → _Yo hablé español_ `[no noun_id]`
  2. (auditory) You found the book → _Tú encontraste el libro_ `[noun_id=libro]`
  3. (written) He ate the food → _Él comió la comida_ `[noun_id=comida]`
  4. (auditory) She united the group → _Ella unió al grupo_ `[no noun_id]`
  5. (written) You (formal) drank the water → _cleaned:_ **You  drank the water** → _Usted bebió el agua_ `[noun_id=agua]`
  6. (auditory) We left the house → _Nosotros salimos de la casa_ `[noun_id=casa]`
  7. (written) We (f) spoke a lot → _cleaned:_ **We  spoke a lot** → _Nosotras hablamos mucho_ `[no noun_id]`
  8. (auditory) They found the dog → _Ellos encontraron el perro_ `[noun_id=perro]`
  9. (written) They (f) ate the bread → _cleaned:_ **They  ate the bread** → _Ellas comieron el pan_ `[noun_id=pan]`
  10. (auditory) You all united here → _Ustedes unieron aquí_ `[no noun_id]`

**`grammar_preterite_regular_2` — Preterite Regular (2/3)** (lesson 2)

- **Verbs/rules:** hablar, encontrar, comer, unir, beber, salir
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 3/10 drills have parenthetical clues — strip; missing noun_id for: familia
- **Drill sentences (10):**
  1. (written) You spoke first → _Tú hablaste primero_ `[no noun_id]`
  2. (auditory) I found the letter → _Yo encontré la carta_ `[noun_id=carta]`
  3. (written) She ate the bread → _Ella comió el pan_ `[noun_id=pan]`
  4. (auditory) He united the family → _Él unió a la familia_ `[no noun_id]`
  5. (written) We drank the water → _Nosotros bebimos el agua_ `[noun_id=agua]`
  6. (auditory) You (formal) left the house → _cleaned:_ **You  left the house** → _Usted salió de la casa_ `[noun_id=casa]`
  7. (written) They spoke Spanish → _Ellos hablaron español_ `[no noun_id]`
  8. (auditory) We (f) found the dog → _cleaned:_ **We  found the dog** → _Nosotras encontramos el perro_ `[noun_id=perro]`
  9. (written) You all ate the food → _Ustedes comieron la comida_ `[noun_id=comida]`
  10. (auditory) They (f) united here → _cleaned:_ **They  united here** → _Ellas unieron aquí_ `[no noun_id]`

**`grammar_preterite_regular_3` — Preterite Regular (3/3)** (lesson 3)

- **Verbs/rules:** hablar, encontrar, comer, unir, beber, salir
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 3/10 drills have parenthetical clues — strip; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) He spoke the truth → _Él habló la verdad_ `[no noun_id]`
  2. (auditory) She found the book → _Ella encontró el libro_ `[noun_id=libro]`
  3. (written) I ate the bread → _Yo comí el pan_ `[noun_id=pan]`
  4. (auditory) You united the group → _Tú uniste al grupo_ `[no noun_id]`
  5. (written) We (f) drank the water → _cleaned:_ **We  drank the water** → _Nosotras bebimos el agua_ `[noun_id=agua]`
  6. (auditory) They left the house → _Ellos salieron de la casa_ `[noun_id=casa]`
  7. (written) You (formal) spoke a lot → _cleaned:_ **You  spoke a lot** → _Usted habló mucho_ `[no noun_id]`
  8. (auditory) We found the dog → _Nosotros encontramos el perro_ `[noun_id=perro]`
  9. (written) They (f) drank the coffee → _cleaned:_ **They  drank the coffee** → _Ellas bebieron el café_ `[noun_id=café]`
  10. (auditory) You all left the city → _Ustedes salieron de la ciudad_ `[noun_id=ciudad]`

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | hablar, encontrar | verb chart + 10 drills |
| 2 | **drill** | comer, unir | verb chart + 10 drills |
| 3 | **chat** | hablar, encontrar, comer, unir | chat (10 possible conjugations, user does 5) |
| 4 | **drill** | beber, salir | verb chart + 10 drills |
| 5 | **chat** | beber, salir | chat (10 possible conjugations, user does 5) |

---

## Preterite Highly Irregular (GL 17.1)

### Current lessons

**`grammar_preterite_irregular_1` — Preterite Highly Irregular (1/4)** (lesson 1)

- **Verbs/rules:** ser, ir, dar, ver, hacer, decir
- **Current anatomy:** video chart (0a) + 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 3/10 drills have parenthetical clues — strip; missing noun_id for: plan, verdad
- **Drill sentences (10):**
  1. (written) I was a student → _Yo fui estudiante_ `[no noun_id]`
  2. (auditory) She was at the park → _Ella fue al parque_ `[noun_id=parque]`
  3. (written) You went to the market → _Tú fuiste al mercado_ `[noun_id=mercado]`
  4. (auditory) We (f) gave the letter → _cleaned:_ **We  gave the letter** → _Nosotras dimos la carta_ `[noun_id=carta]`
  5. (written) He gave the book → _Él dio el libro_ `[noun_id=libro]`
  6. (auditory) You all saw the dog → _Ustedes vieron el perro_ `[noun_id=perro]`
  7. (written) You (formal) saw the house → _cleaned:_ **You  saw the house** → _Usted vio la casa_ `[noun_id=casa]`
  8. (auditory) We made the plan → _Nosotros hicimos el plan_ `[no noun_id]`
  9. (written) They (f) made the food → _cleaned:_ **They  made the food** → _Ellas hicieron la comida_ `[noun_id=comida]`
  10. (auditory) They said the truth → _Ellos dijeron la verdad_ `[no noun_id]`

**`grammar_preterite_irregular_2` — Preterite Highly Irregular (2/4)** (lesson 2)

- **Verbs/rules:** traer, dormir, morir, ser, hacer
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 3/10 drills have parenthetical clues — strip; missing noun_id for: plan
- **Drill sentences (10):**
  1. (written) I brought the food → _Yo traje la comida_ `[noun_id=comida]`
  2. (auditory) We brought the letter → _Nosotros trajimos la carta_ `[noun_id=carta]`
  3. (written) They (f) brought the bags → _cleaned:_ **They  brought the bags** → _Ellas trajeron las bolsas_ `[noun_id=bolsa]`
  4. (auditory) You slept well → _Tú dormiste bien_ `[no noun_id]`
  5. (written) She slept a lot → _Ella durmió mucho_ `[no noun_id]`
  6. (auditory) He died young → _Él murió joven_ `[no noun_id]`
  7. (written) You all died of fear → _Ustedes murieron de miedo_ `[no noun_id]`
  8. (auditory) You (formal) were a doctor → _cleaned:_ **You  were a doctor** → _Usted fue doctor_ `[no noun_id]`
  9. (written) We (f) were at the park → _cleaned:_ **We  were at the park** → _Nosotras fuimos al parque_ `[noun_id=parque]`
  10. (auditory) They made the plan → _Ellos hicieron el plan_ `[no noun_id]`

**`grammar_preterite_irregular_3` — Preterite Highly Irregular (3/4)** (lesson 3)

- **Verbs/rules:** ser, ir, dar, ver, hacer, decir
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 3/10 drills have parenthetical clues — strip; missing noun_id for: plan, verdad
- **Drill sentences (10):**
  1. (written) You were a teacher → _Tú fuiste profesor_ `[no noun_id]`
  2. (auditory) We went to the park → _Nosotros fuimos al parque_ `[noun_id=parque]`
  3. (written) They went to the city → _Ellos fueron a la ciudad_ `[noun_id=ciudad]`
  4. (auditory) You (formal) gave the book → _cleaned:_ **You  gave the book** → _Usted dio el libro_ `[noun_id=libro]`
  5. (written) I gave the letter → _Yo di la carta_ `[noun_id=carta]`
  6. (auditory) She saw the dog → _Ella vio el perro_ `[noun_id=perro]`
  7. (written) We (f) saw the house → _cleaned:_ **We  saw the house** → _Nosotras vimos la casa_ `[noun_id=casa]`
  8. (auditory) He made the plan → _Él hizo el plan_ `[no noun_id]`
  9. (written) You all made the food → _Ustedes hicieron la comida_ `[noun_id=comida]`
  10. (auditory) They (f) said the truth → _cleaned:_ **They  said the truth** → _Ellas dijeron la verdad_ `[no noun_id]`

**`grammar_preterite_irregular_4` — Preterite Highly Irregular (4/4)** (lesson 4)

- **Verbs/rules:** traer, dormir, morir, ir, decir
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 3/10 drills have parenthetical clues — strip; missing noun_id for: casa, verdad
- **Drill sentences (10):**
  1. (written) You brought the food → _Tú trajiste la comida_ `[noun_id=comida]`
  2. (auditory) You (formal) brought the letter → _cleaned:_ **You  brought the letter** → _Usted trajo la carta_ `[noun_id=carta]`
  3. (written) I slept eight hours → _Yo dormí ocho horas_ `[no noun_id]`
  4. (auditory) We (f) slept here → _cleaned:_ **We  slept here** → _Nosotras dormimos aquí_ `[no noun_id]`
  5. (written) They slept in the house → _Ellos durmieron en la casa_ `[noun_id=casa]`
  6. (auditory) She died at home → _Ella murió en casa_ `[no noun_id]`
  7. (written) We died of laughter → _Nosotros morimos de risa_ `[no noun_id]`
  8. (auditory) He went to the market → _Él fue al mercado_ `[noun_id=mercado]`
  9. (written) They (f) went to the park → _cleaned:_ **They  went to the park** → _Ellas fueron al parque_ `[noun_id=parque]`
  10. (auditory) You all said the truth → _Ustedes dijeron la verdad_ `[no noun_id]`

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | ser, ir | verb chart + 10 drills |
| 2 | **drill** | dar, ver | verb chart + 10 drills |
| 3 | **chat** | ser, ir, dar, ver | chat (10 possible conjugations, user does 5) |
| 4 | **drill** | hacer, decir | verb chart + 10 drills |
| 5 | **drill** | traer, dormir | verb chart + 10 drills |
| 6 | **chat** | hacer, decir, traer, dormir | chat (10 possible conjugations, user does 5) |
| 7 | **drill** | morir | verb chart + 10 drills |
| 8 | **chat** | morir | chat (10 possible conjugations, user does 5) |

---

## Preterite Weird Spelling Changes (GL 17.2)

### Current lessons

**`grammar_pret_spelling_1` — Preterite Spelling Changes (1)** (lesson 1)

- **Verbs/rules:** pagar, jugar
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; missing noun_id for: canción
- **Drill sentences (10):**
  1. (written) We (f) (preterite) the song → _cleaned:_ **We   the song** → _Nosotras jugamos la canción_ `[no noun_id]`
  2. (auditory) You (preterite) Spanish → _cleaned:_ **You  Spanish** → _Tú pagaste español_ `[no noun_id]`
  3. (written) You (preterite) English → _cleaned:_ **You  English** → _Tú jugaste inglés_ `[no noun_id]`
  4. (auditory) She (preterite) at home → _cleaned:_ **She  at home** → _Ella pagó en casa_ `[noun_id=casa]`
  5. (written) You (formal) (preterite) the coffee → _cleaned:_ **You   the coffee** → _Usted jugó el café_ `[noun_id=café]`
  6. (auditory) You all (preterite) the music → _cleaned:_ **You all  the music** → _Ustedes pagaron la música_ `[noun_id=música]`
  7. (written) They (f) (preterite) the song → _cleaned:_ **They   the song** → _Ellas pagaron la canción_ `[no noun_id]`
  8. (auditory) You (formal) (preterite) Spanish → _cleaned:_ **You   Spanish** → _Usted pagó español_ `[no noun_id]`
  9. (written) We (f) (preterite) English → _cleaned:_ **We   English** → _Nosotras pagamos inglés_ `[no noun_id]`
  10. (auditory) They (f) (preterite) at home → _cleaned:_ **They   at home** → _Ellas jugaron en casa_ `[noun_id=casa]`

**`grammar_pret_spelling_2` — Preterite Spelling Changes (2)** (lesson 2)

- **Verbs/rules:** buscar, tocar
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; missing noun_id for: canción
- **Drill sentences (10):**
  1. (written) We (f) (preterite) the song → _cleaned:_ **We   the song** → _Nosotras buscamos la canción_ `[no noun_id]`
  2. (auditory) You (preterite) Spanish → _cleaned:_ **You  Spanish** → _Tú buscaste español_ `[no noun_id]`
  3. (written) You (preterite) English → _cleaned:_ **You  English** → _Tú tocaste inglés_ `[no noun_id]`
  4. (auditory) I (preterite) at home → _cleaned:_ **I  at home** → _Yo toqué en casa_ `[noun_id=casa]`
  5. (written) They (f) (preterite) the coffee → _cleaned:_ **They   the coffee** → _Ellas buscaron el café_ `[noun_id=café]`
  6. (auditory) They (f) (preterite) the music → _cleaned:_ **They   the music** → _Ellas tocaron la música_ `[noun_id=música]`
  7. (written) You all (preterite) the song → _cleaned:_ **You all  the song** → _Ustedes tocaron la canción_ `[no noun_id]`
  8. (auditory) You (formal) (preterite) Spanish → _cleaned:_ **You   Spanish** → _Usted tocó español_ `[no noun_id]`
  9. (written) She (preterite) English → _cleaned:_ **She  English** → _Ella tocó inglés_ `[no noun_id]`
  10. (auditory) You all (preterite) at home → _cleaned:_ **You all  at home** → _Ustedes buscaron en casa_ `[noun_id=casa]`

**`grammar_pret_spelling_3` — Preterite Spelling Changes — Chat 1** (lesson 3)

- **Verbs/rules:** pagar, jugar, buscar, tocar
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

**`grammar_pret_spelling_4` — Preterite Spelling Changes (4)** (lesson 4)

- **Verbs/rules:** empezar, almorzar
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; missing noun_id for: canción
- **Drill sentences (10):**
  1. (written) They (f) (preterite) the song → _cleaned:_ **They   the song** → _Ellas empezaron la canción_ `[no noun_id]`
  2. (auditory) You (formal) (preterite) Spanish → _cleaned:_ **You   Spanish** → _Usted empezó español_ `[no noun_id]`
  3. (written) I (preterite) English → _cleaned:_ **I  English** → _Yo almorcé inglés_ `[no noun_id]`
  4. (auditory) She (preterite) at home → _cleaned:_ **She  at home** → _Ella empezó en casa_ `[noun_id=casa]`
  5. (written) I (preterite) the coffee → _cleaned:_ **I  the coffee** → _Yo empecé el café_ `[noun_id=café]`
  6. (auditory) They (f) (preterite) the music → _cleaned:_ **They   the music** → _Ellas almorzaron la música_ `[noun_id=música]`
  7. (written) You (preterite) the song → _cleaned:_ **You  the song** → _Tú almorzaste la canción_ `[no noun_id]`
  8. (auditory) We (f) (preterite) Spanish → _cleaned:_ **We   Spanish** → _Nosotras almorzamos español_ `[no noun_id]`
  9. (written) You (preterite) English → _cleaned:_ **You  English** → _Tú empezaste inglés_ `[no noun_id]`
  10. (auditory) We (f) (preterite) at home → _cleaned:_ **We   at home** → _Nosotras empezamos en casa_ `[noun_id=casa]`

**`grammar_pret_spelling_5` — Preterite Spelling Changes (5)** (lesson 5)

- **Verbs/rules:** creer, leer
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) You all (preterite) the letter → _cleaned:_ **You all  the letter** → _Ustedes leyeron la carta_ `[noun_id=carta]`
  2. (auditory) You all (preterite) the book → _cleaned:_ **You all  the book** → _Ustedes creyeron el libro_ `[noun_id=libro]`
  3. (written) You (formal) (preterite) water → _cleaned:_ **You   water** → _Usted leyó agua_ `[noun_id=agua]`
  4. (auditory) They (f) (preterite) the bread → _cleaned:_ **They   the bread** → _Ellas creyeron el pan_ `[noun_id=pan]`
  5. (written) We (f) (preterite) here → _cleaned:_ **We   here** → _Nosotras leímos aquí_ `[no noun_id]`
  6. (auditory) You (preterite) the truth → _cleaned:_ **You  the truth** → _Tú leíste la verdad_ `[no noun_id]`
  7. (written) She (preterite) the letter → _cleaned:_ **She  the letter** → _Ella leyó la carta_ `[noun_id=carta]`
  8. (auditory) We (f) (preterite) the book → _cleaned:_ **We   the book** → _Nosotras creímos el libro_ `[noun_id=libro]`
  9. (written) I (preterite) water → _cleaned:_ **I  water** → _Yo leí agua_ `[noun_id=agua]`
  10. (auditory) They (f) (preterite) the bread → _cleaned:_ **They   the bread** → _Ellas leyeron el pan_ `[noun_id=pan]`

**`grammar_pret_spelling_6` — Preterite Spelling Changes — Chat 2** (lesson 6)

- **Verbs/rules:** empezar, almorzar, creer, leer
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

**`grammar_pret_spelling_7` — Preterite Spelling Changes (7)** (lesson 7)

- **Verbs/rules:** caer, oír
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) You (preterite) the letter → _cleaned:_ **You  the letter** → _Tú oíste la carta_ `[noun_id=carta]`
  2. (auditory) We (f) (preterite) the book → _cleaned:_ **We   the book** → _Nosotras caímos el libro_ `[noun_id=libro]`
  3. (written) We (f) (preterite) water → _cleaned:_ **We   water** → _Nosotras oímos agua_ `[noun_id=agua]`
  4. (auditory) You (preterite) the bread → _cleaned:_ **You  the bread** → _Tú caíste el pan_ `[noun_id=pan]`
  5. (written) You all (preterite) here → _cleaned:_ **You all  here** → _Ustedes oyeron aquí_ `[no noun_id]`
  6. (auditory) You (formal) (preterite) the truth → _cleaned:_ **You   the truth** → _Usted cayó la verdad_ `[no noun_id]`
  7. (written) You (formal) (preterite) the letter → _cleaned:_ **You   the letter** → _Usted oyó la carta_ `[noun_id=carta]`
  8. (auditory) They (f) (preterite) the book → _cleaned:_ **They   the book** → _Ellas cayeron el libro_ `[noun_id=libro]`
  9. (written) You all (preterite) water → _cleaned:_ **You all  water** → _Ustedes cayeron agua_ `[noun_id=agua]`
  10. (auditory) I (preterite) the bread → _cleaned:_ **I  the bread** → _Yo oí el pan_ `[noun_id=pan]`

**`grammar_pret_spelling_8` — Preterite Spelling Changes (8)** (lesson 8)

- **Verbs/rules:** construir, fluir
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) She (preterite) the letter → _cleaned:_ **She  the letter** → _Ella construyó la carta_ `[noun_id=carta]`
  2. (auditory) You (preterite) the book → _cleaned:_ **You  the book** → _Tú fluiste el libro_ `[noun_id=libro]`
  3. (written) She (preterite) water → _cleaned:_ **She  water** → _Ella fluyó agua_ `[noun_id=agua]`
  4. (auditory) You (formal) (preterite) the bread → _cleaned:_ **You   the bread** → _Usted fluyó el pan_ `[noun_id=pan]`
  5. (written) I (preterite) here → _cleaned:_ **I  here** → _Yo fluí aquí_ `[no noun_id]`
  6. (auditory) You (preterite) the truth → _cleaned:_ **You  the truth** → _Tú construiste la verdad_ `[no noun_id]`
  7. (written) You all (preterite) the letter → _cleaned:_ **You all  the letter** → _Ustedes construyeron la carta_ `[noun_id=carta]`
  8. (auditory) We (f) (preterite) the book → _cleaned:_ **We   the book** → _Nosotras construimos el libro_ `[noun_id=libro]`
  9. (written) You all (preterite) water → _cleaned:_ **You all  water** → _Ustedes fluyeron agua_ `[noun_id=agua]`
  10. (auditory) You (formal) (preterite) the bread → _cleaned:_ **You   the bread** → _Usted construyó el pan_ `[noun_id=pan]`

**`grammar_pret_spelling_9` — Preterite Spelling Changes — Chat 3** (lesson 9)

- **Verbs/rules:** caer, oír, construir, fluir
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | pagar, jugar | verb chart + 10 drills |
| 2 | **drill** | buscar, tocar | verb chart + 10 drills |
| 3 | **chat** | pagar, jugar, buscar, tocar | chat (10 possible conjugations, user does 5) |
| 4 | **drill** | empezar, almorzar | verb chart + 10 drills |
| 5 | **drill** | creer, leer | verb chart + 10 drills |
| 6 | **chat** | empezar, almorzar, creer, leer | chat (10 possible conjugations, user does 5) |
| 7 | **drill** | caer, oír | verb chart + 10 drills |
| 8 | **drill** | construir, fluir | verb chart + 10 drills |
| 9 | **chat** | caer, oír, construir, fluir | chat (10 possible conjugations, user does 5) |

---

## Preterite Stem Changers (GL 17.3)

### Current lessons

**`grammar_pret_strong_1` — Preterite Strong-Stem (1)** (lesson 1)

- **Verbs/rules:** estar, tener
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; missing noun_id for: canción
- **Drill sentences (10):**
  1. (written) You all (preterite) the song → _cleaned:_ **You all  the song** → _Ustedes estuvieron la canción_ `[no noun_id]`
  2. (auditory) You (formal) (preterite) the book → _cleaned:_ **You   the book** → _Usted tuvo el libro_ `[noun_id=libro]`
  3. (written) They (f) (preterite) water → _cleaned:_ **They   water** → _Ellas tuvieron agua_ `[noun_id=agua]`
  4. (auditory) You (preterite) the bread → _cleaned:_ **You  the bread** → _Tú tuviste el pan_ `[noun_id=pan]`
  5. (written) We (f) (preterite) here → _cleaned:_ **We   here** → _Nosotras tuvimos aquí_ `[no noun_id]`
  6. (auditory) She (preterite) the music → _cleaned:_ **She  the music** → _Ella estuvo la música_ `[noun_id=música]`
  7. (written) I (preterite) the letter → _cleaned:_ **I  the letter** → _Yo tuve la carta_ `[noun_id=carta]`
  8. (auditory) You all (preterite) the book → _cleaned:_ **You all  the book** → _Ustedes tuvieron el libro_ `[noun_id=libro]`
  9. (written) We (f) (preterite) English → _cleaned:_ **We   English** → _Nosotras estuvimos inglés_ `[no noun_id]`
  10. (auditory) You (preterite) at home → _cleaned:_ **You  at home** → _Tú estuviste en casa_ `[noun_id=casa]`

**`grammar_pret_strong_2` — Preterite Strong-Stem (2)** (lesson 2)

- **Verbs/rules:** poder, poner
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) You all (preterite) the letter → _cleaned:_ **You all  the letter** → _Ustedes pudieron la carta_ `[noun_id=carta]`
  2. (auditory) She (preterite) the book → _cleaned:_ **She  the book** → _Ella puso el libro_ `[noun_id=libro]`
  3. (written) They (f) (preterite) water → _cleaned:_ **They   water** → _Ellas pudieron agua_ `[noun_id=agua]`
  4. (auditory) You all (preterite) the bread → _cleaned:_ **You all  the bread** → _Ustedes pusieron el pan_ `[noun_id=pan]`
  5. (written) They (f) (preterite) here → _cleaned:_ **They   here** → _Ellas pusieron aquí_ `[no noun_id]`
  6. (auditory) We (f) (preterite) the truth → _cleaned:_ **We   the truth** → _Nosotras pusimos la verdad_ `[no noun_id]`
  7. (written) I (preterite) the letter → _cleaned:_ **I  the letter** → _Yo pude la carta_ `[noun_id=carta]`
  8. (auditory) We (f) (preterite) the book → _cleaned:_ **We   the book** → _Nosotras pudimos el libro_ `[noun_id=libro]`
  9. (written) You (formal) (preterite) water → _cleaned:_ **You   water** → _Usted pudo agua_ `[noun_id=agua]`
  10. (auditory) I (preterite) the bread → _cleaned:_ **I  the bread** → _Yo puse el pan_ `[noun_id=pan]`

**`grammar_pret_strong_3` — Preterite Strong-Stem — Chat 1** (lesson 3)

- **Verbs/rules:** estar, tener, poder, poner
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

**`grammar_pret_strong_4` — Preterite Strong-Stem (4)** (lesson 4)

- **Verbs/rules:** saber, querer
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) You (preterite) the letter → _cleaned:_ **You  the letter** → _Tú supiste la carta_ `[noun_id=carta]`
  2. (auditory) They (f) (preterite) the book → _cleaned:_ **They   the book** → _Ellas quisieron el libro_ `[noun_id=libro]`
  3. (written) You all (preterite) water → _cleaned:_ **You all  water** → _Ustedes supieron agua_ `[noun_id=agua]`
  4. (auditory) I (preterite) the bread → _cleaned:_ **I  the bread** → _Yo supe el pan_ `[noun_id=pan]`
  5. (written) We (f) (preterite) here → _cleaned:_ **We   here** → _Nosotras supimos aquí_ `[no noun_id]`
  6. (auditory) She (preterite) the truth → _cleaned:_ **She  the truth** → _Ella quiso la verdad_ `[no noun_id]`
  7. (written) You (preterite) the letter → _cleaned:_ **You  the letter** → _Tú quisiste la carta_ `[noun_id=carta]`
  8. (auditory) They (f) (preterite) the book → _cleaned:_ **They   the book** → _Ellas supieron el libro_ `[noun_id=libro]`
  9. (written) You (formal) (preterite) water → _cleaned:_ **You   water** → _Usted quiso agua_ `[noun_id=agua]`
  10. (auditory) I (preterite) the bread → _cleaned:_ **I  the bread** → _Yo quise el pan_ `[noun_id=pan]`

**`grammar_pret_strong_5` — Preterite Strong-Stem (5)** (lesson 5)

- **Verbs/rules:** andar, venir
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; missing noun_id for: canción, verdad
- **Drill sentences (10):**
  1. (written) We (f) (preterite) the song → _cleaned:_ **We   the song** → _Nosotras anduvimos la canción_ `[no noun_id]`
  2. (auditory) We (f) (preterite) the book → _cleaned:_ **We   the book** → _Nosotras vinimos el libro_ `[noun_id=libro]`
  3. (written) She (preterite) English → _cleaned:_ **She  English** → _Ella anduvo inglés_ `[no noun_id]`
  4. (auditory) They (f) (preterite) the bread → _cleaned:_ **They   the bread** → _Ellas vinieron el pan_ `[noun_id=pan]`
  5. (written) They (f) (preterite) the coffee → _cleaned:_ **They   the coffee** → _Ellas anduvieron el café_ `[noun_id=café]`
  6. (auditory) She (preterite) the truth → _cleaned:_ **She  the truth** → _Ella vino la verdad_ `[no noun_id]`
  7. (written) You (preterite) the letter → _cleaned:_ **You  the letter** → _Tú viniste la carta_ `[noun_id=carta]`
  8. (auditory) I (preterite) the book → _cleaned:_ **I  the book** → _Yo vine el libro_ `[noun_id=libro]`
  9. (written) You (preterite) English → _cleaned:_ **You  English** → _Tú anduviste inglés_ `[no noun_id]`
  10. (auditory) You all (preterite) at home → _cleaned:_ **You all  at home** → _Ustedes anduvieron en casa_ `[noun_id=casa]`

**`grammar_pret_strong_6` — Preterite Strong-Stem — Chat 2** (lesson 6)

- **Verbs/rules:** saber, querer, andar, venir
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

**`grammar_pret_strong_7` — Preterite Strong-Stem (7)** (lesson 7)

- **Verbs/rules:** haber, caber
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) I (preterite) the letter → _cleaned:_ **I  the letter** → _Yo hube la carta_ `[noun_id=carta]`
  2. (auditory) She (preterite) the book → _cleaned:_ **She  the book** → _Ella cupo el libro_ `[noun_id=libro]`
  3. (written) We (f) (preterite) water → _cleaned:_ **We   water** → _Nosotras hubimos agua_ `[noun_id=agua]`
  4. (auditory) You all (preterite) the bread → _cleaned:_ **You all  the bread** → _Ustedes hubieron el pan_ `[noun_id=pan]`
  5. (written) They (f) (preterite) here → _cleaned:_ **They   here** → _Ellas hubieron aquí_ `[no noun_id]`
  6. (auditory) She (preterite) the truth → _cleaned:_ **She  the truth** → _Ella hubo la verdad_ `[no noun_id]`
  7. (written) You (preterite) the letter → _cleaned:_ **You  the letter** → _Tú cupiste la carta_ `[noun_id=carta]`
  8. (auditory) They (f) (preterite) the book → _cleaned:_ **They   the book** → _Ellas cupieron el libro_ `[noun_id=libro]`
  9. (written) You (formal) (preterite) water → _cleaned:_ **You   water** → _Usted hubo agua_ `[noun_id=agua]`
  10. (auditory) You (formal) (preterite) the bread → _cleaned:_ **You   the bread** → _Usted cupo el pan_ `[noun_id=pan]`

**`grammar_pret_strong_8` — Preterite Strong-Stem (8)** (lesson 8)

- **Verbs/rules:** mantener, obtener
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) They (f) (preterite) the letter → _cleaned:_ **They   the letter** → _Ellas mantuvieron la carta_ `[noun_id=carta]`
  2. (auditory) You all (preterite) the book → _cleaned:_ **You all  the book** → _Ustedes obtuvieron el libro_ `[noun_id=libro]`
  3. (written) We (f) (preterite) water → _cleaned:_ **We   water** → _Nosotras obtuvimos agua_ `[noun_id=agua]`
  4. (auditory) You (preterite) the bread → _cleaned:_ **You  the bread** → _Tú obtuviste el pan_ `[noun_id=pan]`
  5. (written) You all (preterite) here → _cleaned:_ **You all  here** → _Ustedes mantuvieron aquí_ `[no noun_id]`
  6. (auditory) You (preterite) the truth → _cleaned:_ **You  the truth** → _Tú mantuviste la verdad_ `[no noun_id]`
  7. (written) You (formal) (preterite) the letter → _cleaned:_ **You   the letter** → _Usted mantuvo la carta_ `[noun_id=carta]`
  8. (auditory) We (f) (preterite) the book → _cleaned:_ **We   the book** → _Nosotras mantuvimos el libro_ `[noun_id=libro]`
  9. (written) She (preterite) water → _cleaned:_ **She  water** → _Ella mantuvo agua_ `[noun_id=agua]`
  10. (auditory) I (preterite) the bread → _cleaned:_ **I  the bread** → _Yo mantuve el pan_ `[noun_id=pan]`

**`grammar_pret_strong_9` — Preterite Strong-Stem — Chat 3** (lesson 9)

- **Verbs/rules:** haber, caber, mantener, obtener
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | estar, tener | verb chart + 10 drills |
| 2 | **drill** | poder, poner | verb chart + 10 drills |
| 3 | **chat** | estar, tener, poder, poner | chat (10 possible conjugations, user does 5) |
| 4 | **drill** | saber, querer | verb chart + 10 drills |
| 5 | **drill** | andar, venir | verb chart + 10 drills |
| 6 | **chat** | saber, querer, andar, venir | chat (10 possible conjugations, user does 5) |
| 7 | **drill** | haber, caber | verb chart + 10 drills |
| 8 | **drill** | mantener, obtener | verb chart + 10 drills |
| 9 | **chat** | haber, caber, mantener, obtener | chat (10 possible conjugations, user does 5) |

---

## Preterite DUCIR (GL 17.4)

### Current lessons

**`grammar_pret_ducir_1` — Preterite DUCIR (1)** (lesson 1)

- **Verbs/rules:** traducir, conducir
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) They (f) (preterite) the letter → _cleaned:_ **They   the letter** → _Ellas condujeron la carta_ `[noun_id=carta]`
  2. (auditory) I (preterite) the book → _cleaned:_ **I  the book** → _Yo traduje el libro_ `[noun_id=libro]`
  3. (written) You (formal) (preterite) water → _cleaned:_ **You   water** → _Usted tradujo agua_ `[noun_id=agua]`
  4. (auditory) You (preterite) the bread → _cleaned:_ **You  the bread** → _Tú tradujiste el pan_ `[noun_id=pan]`
  5. (written) You (preterite) here → _cleaned:_ **You  here** → _Tú condujiste aquí_ `[no noun_id]`
  6. (auditory) You all (preterite) the truth → _cleaned:_ **You all  the truth** → _Ustedes tradujeron la verdad_ `[no noun_id]`
  7. (written) We (f) (preterite) the letter → _cleaned:_ **We   the letter** → _Nosotras condujimos la carta_ `[noun_id=carta]`
  8. (auditory) You all (preterite) the book → _cleaned:_ **You all  the book** → _Ustedes condujeron el libro_ `[noun_id=libro]`
  9. (written) You (formal) (preterite) water → _cleaned:_ **You   water** → _Usted condujo agua_ `[noun_id=agua]`
  10. (auditory) She (preterite) the bread → _cleaned:_ **She  the bread** → _Ella condujo el pan_ `[noun_id=pan]`

**`grammar_pret_ducir_2` — Preterite DUCIR (2)** (lesson 2)

- **Verbs/rules:** producir, introducir
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) You (preterite) the letter → _cleaned:_ **You  the letter** → _Tú produjiste la carta_ `[noun_id=carta]`
  2. (auditory) You (formal) (preterite) the book → _cleaned:_ **You   the book** → _Usted introdujo el libro_ `[noun_id=libro]`
  3. (written) You all (preterite) water → _cleaned:_ **You all  water** → _Ustedes introdujeron agua_ `[noun_id=agua]`
  4. (auditory) You (formal) (preterite) the bread → _cleaned:_ **You   the bread** → _Usted produjo el pan_ `[noun_id=pan]`
  5. (written) I (preterite) here → _cleaned:_ **I  here** → _Yo produje aquí_ `[no noun_id]`
  6. (auditory) We (f) (preterite) the truth → _cleaned:_ **We   the truth** → _Nosotras introdujimos la verdad_ `[no noun_id]`
  7. (written) They (f) (preterite) the letter → _cleaned:_ **They   the letter** → _Ellas introdujeron la carta_ `[noun_id=carta]`
  8. (auditory) She (preterite) the book → _cleaned:_ **She  the book** → _Ella produjo el libro_ `[noun_id=libro]`
  9. (written) I (preterite) water → _cleaned:_ **I  water** → _Yo introduje agua_ `[noun_id=agua]`
  10. (auditory) We (f) (preterite) the bread → _cleaned:_ **We   the bread** → _Nosotras produjimos el pan_ `[noun_id=pan]`

**`grammar_pret_ducir_3` — Preterite DUCIR — Chat 1** (lesson 3)

- **Verbs/rules:** traducir, conducir, producir, introducir
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | traducir, conducir | verb chart + 10 drills |
| 2 | **drill** | producir, introducir | verb chart + 10 drills |
| 3 | **chat** | traducir, conducir, producir, introducir | chat (10 possible conjugations, user does 5) |

---

## Preterite e-to-i Irregular (GL 17.5)

### Current lessons

**`grammar_pret_e_to_i_1` — Preterite e→i (1)** (lesson 1)

- **Verbs/rules:** pedir, sentir
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) We (f) (preterite) the letter → _cleaned:_ **We   the letter** → _Nosotras pedimos la carta_ `[noun_id=carta]`
  2. (auditory) I (preterite) the book → _cleaned:_ **I  the book** → _Yo sentí el libro_ `[noun_id=libro]`
  3. (written) She (preterite) water → _cleaned:_ **She  water** → _Ella sintió agua_ `[noun_id=agua]`
  4. (auditory) You all (preterite) the bread → _cleaned:_ **You all  the bread** → _Ustedes sintieron el pan_ `[noun_id=pan]`
  5. (written) You (preterite) here → _cleaned:_ **You  here** → _Tú sentiste aquí_ `[no noun_id]`
  6. (auditory) We (f) (preterite) the truth → _cleaned:_ **We   the truth** → _Nosotras sentimos la verdad_ `[no noun_id]`
  7. (written) You (formal) (preterite) the letter → _cleaned:_ **You   the letter** → _Usted pidió la carta_ `[noun_id=carta]`
  8. (auditory) You (preterite) the book → _cleaned:_ **You  the book** → _Tú pediste el libro_ `[noun_id=libro]`
  9. (written) I (preterite) water → _cleaned:_ **I  water** → _Yo pedí agua_ `[noun_id=agua]`
  10. (auditory) They (f) (preterite) the bread → _cleaned:_ **They   the bread** → _Ellas pidieron el pan_ `[noun_id=pan]`

**`grammar_pret_e_to_i_2` — Preterite e→i (2)** (lesson 2)

- **Verbs/rules:** repetir, servir
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) I (preterite) the letter → _cleaned:_ **I  the letter** → _Yo serví la carta_ `[noun_id=carta]`
  2. (auditory) You (preterite) the book → _cleaned:_ **You  the book** → _Tú serviste el libro_ `[noun_id=libro]`
  3. (written) They (f) (preterite) water → _cleaned:_ **They   water** → _Ellas repitieron agua_ `[noun_id=agua]`
  4. (auditory) They (f) (preterite) the bread → _cleaned:_ **They   the bread** → _Ellas sirvieron el pan_ `[noun_id=pan]`
  5. (written) You all (preterite) here → _cleaned:_ **You all  here** → _Ustedes repitieron aquí_ `[no noun_id]`
  6. (auditory) You (preterite) the truth → _cleaned:_ **You  the truth** → _Tú repetiste la verdad_ `[no noun_id]`
  7. (written) We (f) (preterite) the letter → _cleaned:_ **We   the letter** → _Nosotras servimos la carta_ `[noun_id=carta]`
  8. (auditory) I (preterite) the book → _cleaned:_ **I  the book** → _Yo repetí el libro_ `[noun_id=libro]`
  9. (written) You (formal) (preterite) water → _cleaned:_ **You   water** → _Usted repitió agua_ `[noun_id=agua]`
  10. (auditory) We (f) (preterite) the bread → _cleaned:_ **We   the bread** → _Nosotras repetimos el pan_ `[noun_id=pan]`

**`grammar_pret_e_to_i_3` — Preterite e→i — Chat 1** (lesson 3)

- **Verbs/rules:** pedir, sentir, repetir, servir
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | pedir, sentir | verb chart + 10 drills |
| 2 | **drill** | repetir, servir | verb chart + 10 drills |
| 3 | **chat** | pedir, sentir, repetir, servir | chat (10 possible conjugations, user does 5) |

---

## Gerund (GL 18)

### Current lessons

**`grammar_gerund_1` — Gerund (1/4)** (lesson 1)

- **Verbs/rules:** hablar, caminar, charlar, comer
- **Current anatomy:** video chart (0a) + 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 3/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) I am speaking Spanish → _Yo estoy hablando español_ `[no noun_id]`
  2. (auditory) She is speaking now → _Ella está hablando ahora_ `[no noun_id]`
  3. (written) You all are speaking → _Ustedes están hablando_ `[no noun_id]`
  4. (auditory) You are walking here → _Tú estás caminando aquí_ `[no noun_id]`
  5. (written) We (f) are walking a lot → _cleaned:_ **We  are walking a lot** → _Nosotras estamos caminando mucho_ `[no noun_id]`
  6. (auditory) He is chatting now → _Él está charlando ahora_ `[no noun_id]`
  7. (written) They are chatting here → _Ellos están charlando aquí_ `[no noun_id]`
  8. (auditory) You (formal) are eating the food → _cleaned:_ **You  are eating the food** → _Usted está comiendo la comida_ `[noun_id=comida]`
  9. (written) We are eating the bread → _Nosotros estamos comiendo el pan_ `[noun_id=pan]`
  10. (auditory) They (f) are eating a lot → _cleaned:_ **They  are eating a lot** → _Ellas están comiendo mucho_ `[no noun_id]`

**`grammar_gerund_2` — Gerund (2/4)** (lesson 2)

- **Verbs/rules:** beber, inhibir, prohibir, salir
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 3/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) I am drinking the water → _Yo estoy bebiendo el agua_ `[noun_id=agua]`
  2. (auditory) We are drinking the coffee → _Nosotros estamos bebiendo el café_ `[noun_id=café]`
  3. (written) They (f) are drinking a lot → _cleaned:_ **They  are drinking a lot** → _Ellas están bebiendo mucho_ `[no noun_id]`
  4. (auditory) You are inhibiting me → _Tú estás inhibiendo aquí_ `[no noun_id]`
  5. (written) She is inhibiting now → _Ella está inhibiendo ahora_ `[no noun_id]`
  6. (auditory) He is prohibiting the entry → _Él está prohibiendo la entrada_ `[no noun_id]`
  7. (written) You all are prohibiting it → _Ustedes están prohibiendo eso_ `[no noun_id]`
  8. (auditory) You (formal) are leaving now → _cleaned:_ **You  are leaving now** → _Usted está saliendo ahora_ `[no noun_id]`
  9. (written) We (f) are leaving the house → _cleaned:_ **We  are leaving the house** → _Nosotras estamos saliendo de la casa_ `[noun_id=casa]`
  10. (auditory) They are leaving the city → _Ellos están saliendo de la ciudad_ `[noun_id=ciudad]`

**`grammar_gerund_3` — Gerund (3/4)** (lesson 3)

- **Verbs/rules:** hablar, caminar, charlar, comer
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 3/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) You are speaking now → _Tú estás hablando ahora_ `[no noun_id]`
  2. (auditory) We are speaking Spanish → _Nosotros estamos hablando español_ `[no noun_id]`
  3. (written) You (formal) are walking here → _cleaned:_ **You  are walking here** → _Usted está caminando aquí_ `[no noun_id]`
  4. (auditory) They (f) are walking a lot → _cleaned:_ **They  are walking a lot** → _Ellas están caminando mucho_ `[no noun_id]`
  5. (written) I am chatting now → _Yo estoy charlando ahora_ `[no noun_id]`
  6. (auditory) We (f) are chatting here → _cleaned:_ **We  are chatting here** → _Nosotras estamos charlando aquí_ `[no noun_id]`
  7. (written) You all are chatting a lot → _Ustedes están charlando mucho_ `[no noun_id]`
  8. (auditory) He is eating the food → _Él está comiendo la comida_ `[noun_id=comida]`
  9. (written) She is eating the bread → _Ella está comiendo el pan_ `[noun_id=pan]`
  10. (auditory) They are eating now → _Ellos están comiendo ahora_ `[no noun_id]`

**`grammar_gerund_4` — Gerund (4/4)** (lesson 4)

- **Verbs/rules:** beber, inhibir, prohibir, salir
- **Current anatomy:** 10 drills (0b) + chat P2 + chat P3
- **Issues:** drill+chat in same lesson (chat should be its own lesson); uses P3 (no-hints chat) — consolidate to single 'chat'; 3/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) You are drinking the water → _Tú estás bebiendo el agua_ `[noun_id=agua]`
  2. (auditory) You (formal) are drinking the coffee → _cleaned:_ **You  are drinking the coffee** → _Usted está bebiendo el café_ `[noun_id=café]`
  3. (written) I am inhibiting it → _Yo estoy inhibiendo eso_ `[no noun_id]`
  4. (auditory) We (f) are inhibiting now → _cleaned:_ **We  are inhibiting now** → _Nosotras estamos inhibiendo ahora_ `[no noun_id]`
  5. (written) They are inhibiting here → _Ellos están inhibiendo aquí_ `[no noun_id]`
  6. (auditory) She is prohibiting the entry → _Ella está prohibiendo la entrada_ `[no noun_id]`
  7. (written) We are prohibiting it → _Nosotros estamos prohibiendo eso_ `[no noun_id]`
  8. (auditory) He is leaving now → _Él está saliendo ahora_ `[no noun_id]`
  9. (written) They (f) are leaving the house → _cleaned:_ **They  are leaving the house** → _Ellas están saliendo de la casa_ `[noun_id=casa]`
  10. (auditory) You all are leaving the city → _Ustedes están saliendo de la ciudad_ `[noun_id=ciudad]`

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | hablar, caminar | verb chart + 10 drills |
| 2 | **drill** | charlar, comer | verb chart + 10 drills |
| 3 | **chat** | hablar, caminar, charlar, comer | chat (10 possible conjugations, user does 5) |
| 4 | **drill** | beber, inhibir | verb chart + 10 drills |
| 5 | **drill** | prohibir, salir | verb chart + 10 drills |
| 6 | **chat** | beber, inhibir, prohibir, salir | chat (10 possible conjugations, user does 5) |

---

## Perfect Tenses (GL 18.5)

### Current lessons

**`grammar_perfect_tenses` — Perfect Tenses** (lesson 1)

- **Verbs/rules:** haber
- **Current anatomy:** 1 flashcards (1a) + written test (1b) + chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); 1a flashcards enabled (unusual); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | haber | verb chart + 10 drills |
| 2 | **chat** | haber | chat (10 possible conjugations, user does 5) |

---

## Direct + Indirect Object Pronouns (GL 19)

### Current lessons

**`grammar_obj_direct` — Direct Object Pronouns** (lesson 1)

- **Verbs/rules:** lo, la, los, las
- **Current anatomy:** chat P2
- **Issues:** CHAT-ONLY (no teaching before chat); 10 drill_sentences but 0b:off → dead data; 9/10 drills have parenthetical clues — strip
- **Drill sentences (10):**
  1. (written) I see it (the book) → _cleaned:_ **I see it** → _Lo veo_ `[noun_id=libro]`
  2. (auditory) She buys them (the apples) → _cleaned:_ **She buys them** → _Las compra_ `[no noun_id]`
  3. (written) We eat it (the bread) → _cleaned:_ **We eat it** → _Lo comemos_ `[noun_id=pan]`
  4. (auditory) They bring her (Maria) → _cleaned:_ **They bring her** → _La traen_ `[no noun_id]`
  5. (written) You hear them (the children) → _cleaned:_ **You hear them** → _Los oyes_ `[no noun_id]`
  6. (auditory) I read it (the letter) → _cleaned:_ **I read it** → _La leo_ `[noun_id=carta]`
  7. (written) He drinks it (the coffee) → _cleaned:_ **He drinks it** → _Lo bebe_ `[noun_id=café]`
  8. (auditory) We see them (the cars) → _cleaned:_ **We see them** → _Los vemos_ `[no noun_id]`
  9. (written) She wants it (the book) → _cleaned:_ **She wants it** → _Lo quiere_ `[noun_id=libro]`
  10. (auditory) I take her → _La llevo_ `[no noun_id]`

**`grammar_obj_indirect` — Indirect Object Pronouns** (lesson 2)

- **Verbs/rules:** le, les
- **Current anatomy:** chat P2
- **Issues:** CHAT-ONLY (no teaching before chat); 10 drill_sentences but 0b:off → dead data; missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) I give him the book → _Le doy el libro_ `[noun_id=libro]`
  2. (auditory) She tells them the truth → _Les dice la verdad_ `[no noun_id]`
  3. (written) We bring her the food → _Le traemos la comida_ `[noun_id=comida]`
  4. (auditory) They send him the letter → _Le mandan la carta_ `[noun_id=carta]`
  5. (written) I write him a message → _Le escribo un mensaje_ `[no noun_id]`
  6. (auditory) We pay them the money → _Les pagamos el dinero_ `[noun_id=dinero]`
  7. (written) You give them the gift → _Les das el regalo_ `[no noun_id]`
  8. (auditory) She buys him the shirt → _Le compra la camisa_ `[noun_id=camisa]`
  9. (written) I show him the photo → _Le muestro la foto_ `[no noun_id]`
  10. (auditory) We tell them everything → _Les decimos todo_ `[no noun_id]`

**`grammar_obj_chat_1` — Object Pronouns — Chat 1** (lesson 3)

- **Verbs/rules:** lo, la, los, las, le, les
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

**`grammar_obj_combined_a` — Combined Object Pronouns (1/2)** (lesson 4)

- **Verbs/rules:** se, lo, la, me, te
- **Current anatomy:** chat P2
- **Issues:** CHAT-ONLY (no teaching before chat); 10 drill_sentences but 0b:off → dead data
- **Drill sentences (10):**
  1. (written) She gives it to me → _Me lo da_ `[no noun_id]`
  2. (auditory) I give it to you → _Te lo doy_ `[no noun_id]`
  3. (written) She gives it to him → _Se lo da_ `[no noun_id]`
  4. (auditory) We bring it to her → _Se lo traemos_ `[no noun_id]`
  5. (written) I tell it to you → _Te lo digo_ `[no noun_id]`
  6. (auditory) He sends it to me → _Me lo manda_ `[no noun_id]`
  7. (written) She writes it to me → _Me la escribe_ `[no noun_id]`
  8. (auditory) We bring it to you → _Te la traemos_ `[no noun_id]`
  9. (written) They give it to him → _Se la dan_ `[no noun_id]`
  10. (auditory) I show it to her → _Se la muestro_ `[no noun_id]`

**`grammar_obj_combined_b` — Combined Object Pronouns (2/2)** (lesson 5)

- **Verbs/rules:** nos, los, las, se
- **Current anatomy:** chat P2
- **Issues:** CHAT-ONLY (no teaching before chat); 10 drill_sentences but 0b:off → dead data
- **Drill sentences (10):**
  1. (written) They bring them to us → _Nos los traen_ `[no noun_id]`
  2. (auditory) She tells them to us → _Nos los dice_ `[no noun_id]`
  3. (written) He gives them to them → _Se los da_ `[no noun_id]`
  4. (auditory) We send them to her → _Se las mandamos_ `[no noun_id]`
  5. (written) They show them to us → _Nos las muestran_ `[no noun_id]`
  6. (auditory) I write them to him → _Se las escribo_ `[no noun_id]`
  7. (written) We pay them to them → _Se los pagamos_ `[no noun_id]`
  8. (auditory) You give them to us → _Nos los das_ `[no noun_id]`
  9. (written) She brings them to me → _Me las trae_ `[no noun_id]`
  10. (auditory) I send them to you → _Te las mando_ `[no noun_id]`

**`grammar_obj_chat_2` — Object Pronouns — Chat 2** (lesson 6)

- **Verbs/rules:** se, me, te, nos, lo, la, los, las
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | lo, la | rule chart + 10 drills |
| 2 | **drill** | los, las | rule chart + 10 drills |
| 3 | **chat** | lo, la, los, las | chat (10 possible conjugations, user does 5) |
| 4 | **drill** | le, les | rule chart + 10 drills |
| 5 | **drill** | se, me | rule chart + 10 drills |
| 6 | **chat** | le, les, se, me | chat (10 possible conjugations, user does 5) |
| 7 | **drill** | te, nos | rule chart + 10 drills |
| 8 | **chat** | te, nos | chat (10 possible conjugations, user does 5) |

---

## Subjunctive (GL 20)

### Current lessons

**`grammar_subj_pres_1` — Present Subjunctive (1)** (lesson 1)

- **Verbs/rules:** hablar, comer
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; 10 drills > 6 words — simplify (1 longer per lesson allowed); missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) I (that ___ ) — present subj the letter → _cleaned:_ **I  — present subj the letter** → _Yo coma la carta_ `[noun_id=carta]`
  2. (auditory) You all (that ___ ) — present subj the book → _cleaned:_ **You all  — present subj the book** → _Ustedes coman el libro_ `[noun_id=libro]`
  3. (written) You (that ___ ) — present subj water → _cleaned:_ **You  — present subj water** → _Tú comas agua_ `[noun_id=agua]`
  4. (auditory) She (that ___ ) — present subj at home → _cleaned:_ **She  — present subj at home** → _Ella hable en casa_ `[noun_id=casa]`
  5. (written) They (f) (that ___ ) — present subj the coffee → _cleaned:_ **They   — present subj the coffee** → _Ellas hablen el café_ `[noun_id=café]`
  6. (auditory) They (f) (that ___ ) — present subj the truth → _cleaned:_ **They   — present subj the truth** → _Ellas coman la verdad_ `[no noun_id]`
  7. (written) You (formal) (that ___ ) — present subj the letter → _cleaned:_ **You   — present subj the letter** → _Usted coma la carta_ `[noun_id=carta]`
  8. (auditory) You (that ___ ) — present subj Spanish → _cleaned:_ **You  — present subj Spanish** → _Tú hables español_ `[no noun_id]`
  9. (written) We (f) (that ___ ) — present subj English → _cleaned:_ **We   — present subj English** → _Nosotras hablemos inglés_ `[no noun_id]`
  10. (auditory) You all (that ___ ) — present subj at home → _cleaned:_ **You all  — present subj at home** → _Ustedes hablen en casa_ `[noun_id=casa]`

**`grammar_subj_pres_2` — Present Subjunctive (2)** (lesson 2)

- **Verbs/rules:** vivir, estudiar
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; 10 drills > 6 words — simplify (1 longer per lesson allowed); missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) I (that ___ ) — present subj the letter → _cleaned:_ **I  — present subj the letter** → _Yo viva la carta_ `[noun_id=carta]`
  2. (auditory) You all (that ___ ) — present subj Spanish → _cleaned:_ **You all  — present subj Spanish** → _Ustedes estudien español_ `[no noun_id]`
  3. (written) I (that ___ ) — present subj English → _cleaned:_ **I  — present subj English** → _Yo estudie inglés_ `[no noun_id]`
  4. (auditory) You (formal) (that ___ ) — present subj the bread → _cleaned:_ **You   — present subj the bread** → _Usted viva el pan_ `[noun_id=pan]`
  5. (written) We (f) (that ___ ) — present subj here → _cleaned:_ **We   — present subj here** → _Nosotras vivamos aquí_ `[no noun_id]`
  6. (auditory) You (that ___ ) — present subj the truth → _cleaned:_ **You  — present subj the truth** → _Tú vivas la verdad_ `[no noun_id]`
  7. (written) She (that ___ ) — present subj the letter → _cleaned:_ **She  — present subj the letter** → _Ella viva la carta_ `[noun_id=carta]`
  8. (auditory) You all (that ___ ) — present subj the book → _cleaned:_ **You all  — present subj the book** → _Ustedes vivan el libro_ `[noun_id=libro]`
  9. (written) She (that ___ ) — present subj English → _cleaned:_ **She  — present subj English** → _Ella estudie inglés_ `[no noun_id]`
  10. (auditory) We (f) (that ___ ) — present subj at home → _cleaned:_ **We   — present subj at home** → _Nosotras estudiemos en casa_ `[noun_id=casa]`

**`grammar_subj_pres_3` — Present Subjunctive — Chat 1** (lesson 3)

- **Verbs/rules:** hablar, comer, vivir, estudiar
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

**`grammar_subj_pres_4` — Present Subjunctive (4)** (lesson 4)

- **Verbs/rules:** ser, ir
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; 10 drills > 6 words — simplify (1 longer per lesson allowed); missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) We (f) (that ___ ) — present subj the letter → _cleaned:_ **We   — present subj the letter** → _Nosotras seamos la carta_ `[noun_id=carta]`
  2. (auditory) She (that ___ ) — present subj the book → _cleaned:_ **She  — present subj the book** → _Ella sea el libro_ `[noun_id=libro]`
  3. (written) You (formal) (that ___ ) — present subj water → _cleaned:_ **You   — present subj water** → _Usted vaya agua_ `[noun_id=agua]`
  4. (auditory) You (that ___ ) — present subj the bread → _cleaned:_ **You  — present subj the bread** → _Tú seas el pan_ `[noun_id=pan]`
  5. (written) We (f) (that ___ ) — present subj here → _cleaned:_ **We   — present subj here** → _Nosotras vayamos aquí_ `[no noun_id]`
  6. (auditory) I (that ___ ) — present subj the truth → _cleaned:_ **I  — present subj the truth** → _Yo vaya la verdad_ `[no noun_id]`
  7. (written) I (that ___ ) — present subj the letter → _cleaned:_ **I  — present subj the letter** → _Yo sea la carta_ `[noun_id=carta]`
  8. (auditory) You (that ___ ) — present subj the book → _cleaned:_ **You  — present subj the book** → _Tú vayas el libro_ `[noun_id=libro]`
  9. (written) They (f) (that ___ ) — present subj water → _cleaned:_ **They   — present subj water** → _Ellas sean agua_ `[noun_id=agua]`
  10. (auditory) You (formal) (that ___ ) — present subj the bread → _cleaned:_ **You   — present subj the bread** → _Usted sea el pan_ `[noun_id=pan]`

**`grammar_subj_pres_5` — Present Subjunctive (5)** (lesson 5)

- **Verbs/rules:** estar, dar
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; 10 drills > 6 words — simplify (1 longer per lesson allowed); missing noun_id for: canción
- **Drill sentences (10):**
  1. (written) She (that ___ ) — present subj the song → _cleaned:_ **She  — present subj the song** → _Ella esté la canción_ `[no noun_id]`
  2. (auditory) We (f) (that ___ ) — present subj Spanish → _cleaned:_ **We   — present subj Spanish** → _Nosotras estemos español_ `[no noun_id]`
  3. (written) You all (that ___ ) — present subj English → _cleaned:_ **You all  — present subj English** → _Ustedes estén inglés_ `[no noun_id]`
  4. (auditory) They (f) (that ___ ) — present subj at home → _cleaned:_ **They   — present subj at home** → _Ellas den en casa_ `[noun_id=casa]`
  5. (written) You (formal) (that ___ ) — present subj the coffee → _cleaned:_ **You   — present subj the coffee** → _Usted esté el café_ `[noun_id=café]`
  6. (auditory) I (that ___ ) — present subj the music → _cleaned:_ **I  — present subj the music** → _Yo dé la música_ `[noun_id=música]`
  7. (written) You (that ___ ) — present subj the song → _cleaned:_ **You  — present subj the song** → _Tú estés la canción_ `[no noun_id]`
  8. (auditory) We (f) (that ___ ) — present subj Spanish → _cleaned:_ **We   — present subj Spanish** → _Nosotras demos español_ `[no noun_id]`
  9. (written) You all (that ___ ) — present subj English → _cleaned:_ **You all  — present subj English** → _Ustedes den inglés_ `[no noun_id]`
  10. (auditory) They (f) (that ___ ) — present subj at home → _cleaned:_ **They   — present subj at home** → _Ellas estén en casa_ `[noun_id=casa]`

**`grammar_subj_pres_6` — Present Subjunctive — Chat 2** (lesson 6)

- **Verbs/rules:** ser, ir, estar, dar
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

**`grammar_subj_pres_7` — Present Subjunctive (7)** (lesson 7)

- **Verbs/rules:** saber, haber
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; 10 drills > 6 words — simplify (1 longer per lesson allowed); missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) We (f) (that ___ ) — present subj the letter → _cleaned:_ **We   — present subj the letter** → _Nosotras sepamos la carta_ `[noun_id=carta]`
  2. (auditory) You (formal) (that ___ ) — present subj the book → _cleaned:_ **You   — present subj the book** → _Usted haya el libro_ `[noun_id=libro]`
  3. (written) We (f) (that ___ ) — present subj water → _cleaned:_ **We   — present subj water** → _Nosotras hayamos agua_ `[noun_id=agua]`
  4. (auditory) You (that ___ ) — present subj the bread → _cleaned:_ **You  — present subj the bread** → _Tú sepas el pan_ `[noun_id=pan]`
  5. (written) They (f) (that ___ ) — present subj here → _cleaned:_ **They   — present subj here** → _Ellas hayan aquí_ `[no noun_id]`
  6. (auditory) She (that ___ ) — present subj the truth → _cleaned:_ **She  — present subj the truth** → _Ella haya la verdad_ `[no noun_id]`
  7. (written) I (that ___ ) — present subj the letter → _cleaned:_ **I  — present subj the letter** → _Yo sepa la carta_ `[noun_id=carta]`
  8. (auditory) You all (that ___ ) — present subj the book → _cleaned:_ **You all  — present subj the book** → _Ustedes sepan el libro_ `[noun_id=libro]`
  9. (written) She (that ___ ) — present subj water → _cleaned:_ **She  — present subj water** → _Ella sepa agua_ `[noun_id=agua]`
  10. (auditory) They (f) (that ___ ) — present subj the bread → _cleaned:_ **They   — present subj the bread** → _Ellas sepan el pan_ `[noun_id=pan]`

**`grammar_subj_pres_8` — Present Subjunctive — Chat 3** (lesson 8)

- **Verbs/rules:** saber, haber
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

**`grammar_subj_impf_1` — Imperfect Subjunctive (1)** (lesson 9)

- **Verbs/rules:** hablar, comer
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; 10 drills > 6 words — simplify (1 longer per lesson allowed); missing noun_id for: canción, verdad
- **Drill sentences (10):**
  1. (written) You (if ___ ) — imperfect subj the song → _cleaned:_ **You  — imperfect subj the song** → _Tú hablaras la canción_ `[no noun_id]`
  2. (auditory) I (if ___ ) — imperfect subj Spanish → _cleaned:_ **I  — imperfect subj Spanish** → _Yo hablara español_ `[no noun_id]`
  3. (written) We (f) (if ___ ) — imperfect subj English → _cleaned:_ **We   — imperfect subj English** → _Nosotras habláramos inglés_ `[no noun_id]`
  4. (auditory) We (f) (if ___ ) — imperfect subj the bread → _cleaned:_ **We   — imperfect subj the bread** → _Nosotras comiéramos el pan_ `[noun_id=pan]`
  5. (written) She (if ___ ) — imperfect subj the coffee → _cleaned:_ **She  — imperfect subj the coffee** → _Ella hablara el café_ `[noun_id=café]`
  6. (auditory) She (if ___ ) — imperfect subj the truth → _cleaned:_ **She  — imperfect subj the truth** → _Ella comiera la verdad_ `[no noun_id]`
  7. (written) You all (if ___ ) — imperfect subj the song → _cleaned:_ **You all  — imperfect subj the song** → _Ustedes hablaran la canción_ `[no noun_id]`
  8. (auditory) You (formal) (if ___ ) — imperfect subj Spanish → _cleaned:_ **You   — imperfect subj Spanish** → _Usted hablara español_ `[no noun_id]`
  9. (written) You (if ___ ) — imperfect subj water → _cleaned:_ **You  — imperfect subj water** → _Tú comieras agua_ `[noun_id=agua]`
  10. (auditory) You all (if ___ ) — imperfect subj the bread → _cleaned:_ **You all  — imperfect subj the bread** → _Ustedes comieran el pan_ `[noun_id=pan]`

**`grammar_subj_impf_2` — Imperfect Subjunctive (2)** (lesson 10)

- **Verbs/rules:** vivir, estudiar
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; 10 drills > 6 words — simplify (1 longer per lesson allowed); missing noun_id for: canción
- **Drill sentences (10):**
  1. (written) We (f) (if ___ ) — imperfect subj the song → _cleaned:_ **We   — imperfect subj the song** → _Nosotras estudiáramos la canción_ `[no noun_id]`
  2. (auditory) You (if ___ ) — imperfect subj the book → _cleaned:_ **You  — imperfect subj the book** → _Tú vivieras el libro_ `[noun_id=libro]`
  3. (written) We (f) (if ___ ) — imperfect subj water → _cleaned:_ **We   — imperfect subj water** → _Nosotras viviéramos agua_ `[noun_id=agua]`
  4. (auditory) You (if ___ ) — imperfect subj at home → _cleaned:_ **You  — imperfect subj at home** → _Tú estudiaras en casa_ `[noun_id=casa]`
  5. (written) You all (if ___ ) — imperfect subj here → _cleaned:_ **You all  — imperfect subj here** → _Ustedes vivieran aquí_ `[no noun_id]`
  6. (auditory) They (f) (if ___ ) — imperfect subj the music → _cleaned:_ **They   — imperfect subj the music** → _Ellas estudiaran la música_ `[noun_id=música]`
  7. (written) You (formal) (if ___ ) — imperfect subj the song → _cleaned:_ **You   — imperfect subj the song** → _Usted estudiara la canción_ `[no noun_id]`
  8. (auditory) I (if ___ ) — imperfect subj the book → _cleaned:_ **I  — imperfect subj the book** → _Yo viviera el libro_ `[noun_id=libro]`
  9. (written) She (if ___ ) — imperfect subj English → _cleaned:_ **She  — imperfect subj English** → _Ella estudiara inglés_ `[no noun_id]`
  10. (auditory) I (if ___ ) — imperfect subj at home → _cleaned:_ **I  — imperfect subj at home** → _Yo estudiara en casa_ `[noun_id=casa]`

**`grammar_subj_impf_3` — Imperfect Subjunctive — Chat 1** (lesson 11)

- **Verbs/rules:** hablar, comer, vivir, estudiar
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

**`grammar_subj_impf_4` — Imperfect Subjunctive (4)** (lesson 12)

- **Verbs/rules:** ser, tener
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; 10 drills > 6 words — simplify (1 longer per lesson allowed); missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) You (if ___ ) — imperfect subj the letter → _cleaned:_ **You  — imperfect subj the letter** → _Tú fueras la carta_ `[noun_id=carta]`
  2. (auditory) You all (if ___ ) — imperfect subj the book → _cleaned:_ **You all  — imperfect subj the book** → _Ustedes fueran el libro_ `[noun_id=libro]`
  3. (written) You all (if ___ ) — imperfect subj water → _cleaned:_ **You all  — imperfect subj water** → _Ustedes tuvieran agua_ `[noun_id=agua]`
  4. (auditory) She (if ___ ) — imperfect subj the bread → _cleaned:_ **She  — imperfect subj the bread** → _Ella fuera el pan_ `[noun_id=pan]`
  5. (written) We (f) (if ___ ) — imperfect subj here → _cleaned:_ **We   — imperfect subj here** → _Nosotras tuviéramos aquí_ `[no noun_id]`
  6. (auditory) I (if ___ ) — imperfect subj the truth → _cleaned:_ **I  — imperfect subj the truth** → _Yo tuviera la verdad_ `[no noun_id]`
  7. (written) She (if ___ ) — imperfect subj the letter → _cleaned:_ **She  — imperfect subj the letter** → _Ella tuviera la carta_ `[noun_id=carta]`
  8. (auditory) You (if ___ ) — imperfect subj the book → _cleaned:_ **You  — imperfect subj the book** → _Tú tuvieras el libro_ `[noun_id=libro]`
  9. (written) They (f) (if ___ ) — imperfect subj water → _cleaned:_ **They   — imperfect subj water** → _Ellas fueran agua_ `[noun_id=agua]`
  10. (auditory) You (formal) (if ___ ) — imperfect subj the bread → _cleaned:_ **You   — imperfect subj the bread** → _Usted fuera el pan_ `[noun_id=pan]`

**`grammar_subj_impf_5` — Imperfect Subjunctive (5)** (lesson 13)

- **Verbs/rules:** hacer, querer
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; 10 drills > 6 words — simplify (1 longer per lesson allowed); missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) You all (if ___ ) — imperfect subj the letter → _cleaned:_ **You all  — imperfect subj the letter** → _Ustedes hicieran la carta_ `[noun_id=carta]`
  2. (auditory) You (if ___ ) — imperfect subj the book → _cleaned:_ **You  — imperfect subj the book** → _Tú hicieras el libro_ `[noun_id=libro]`
  3. (written) I (if ___ ) — imperfect subj water → _cleaned:_ **I  — imperfect subj water** → _Yo hiciera agua_ `[noun_id=agua]`
  4. (auditory) You (formal) (if ___ ) — imperfect subj the bread → _cleaned:_ **You   — imperfect subj the bread** → _Usted hiciera el pan_ `[noun_id=pan]`
  5. (written) She (if ___ ) — imperfect subj here → _cleaned:_ **She  — imperfect subj here** → _Ella quisiera aquí_ `[no noun_id]`
  6. (auditory) You (formal) (if ___ ) — imperfect subj the truth → _cleaned:_ **You   — imperfect subj the truth** → _Usted quisiera la verdad_ `[no noun_id]`
  7. (written) They (f) (if ___ ) — imperfect subj the letter → _cleaned:_ **They   — imperfect subj the letter** → _Ellas quisieran la carta_ `[noun_id=carta]`
  8. (auditory) You all (if ___ ) — imperfect subj the book → _cleaned:_ **You all  — imperfect subj the book** → _Ustedes quisieran el libro_ `[noun_id=libro]`
  9. (written) I (if ___ ) — imperfect subj water → _cleaned:_ **I  — imperfect subj water** → _Yo quisiera agua_ `[noun_id=agua]`
  10. (auditory) We (f) (if ___ ) — imperfect subj the bread → _cleaned:_ **We   — imperfect subj the bread** → _Nosotras hiciéramos el pan_ `[noun_id=pan]`

**`grammar_subj_impf_6` — Imperfect Subjunctive — Chat 2** (lesson 14)

- **Verbs/rules:** ser, tener, hacer, querer
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

**`grammar_subj_impf_7` — Imperfect Subjunctive (7)** (lesson 15)

- **Verbs/rules:** decir, poder
- **Current anatomy:** 0a:on but no video + 10 drills (0b)
- **Issues:** 0a:on but no video → renders empty; 10/10 drills have parenthetical clues — strip; 10 drills > 6 words — simplify (1 longer per lesson allowed); missing noun_id for: verdad
- **Drill sentences (10):**
  1. (written) We (f) (if ___ ) — imperfect subj the letter → _cleaned:_ **We   — imperfect subj the letter** → _Nosotras pudiéramos la carta_ `[noun_id=carta]`
  2. (auditory) You (if ___ ) — imperfect subj the book → _cleaned:_ **You  — imperfect subj the book** → _Tú dijeras el libro_ `[noun_id=libro]`
  3. (written) You (formal) (if ___ ) — imperfect subj water → _cleaned:_ **You   — imperfect subj water** → _Usted dijera agua_ `[noun_id=agua]`
  4. (auditory) I (if ___ ) — imperfect subj the bread → _cleaned:_ **I  — imperfect subj the bread** → _Yo pudiera el pan_ `[noun_id=pan]`
  5. (written) She (if ___ ) — imperfect subj here → _cleaned:_ **She  — imperfect subj here** → _Ella pudiera aquí_ `[no noun_id]`
  6. (auditory) You all (if ___ ) — imperfect subj the truth → _cleaned:_ **You all  — imperfect subj the truth** → _Ustedes pudieran la verdad_ `[no noun_id]`
  7. (written) You (if ___ ) — imperfect subj the letter → _cleaned:_ **You  — imperfect subj the letter** → _Tú pudieras la carta_ `[noun_id=carta]`
  8. (auditory) They (f) (if ___ ) — imperfect subj the book → _cleaned:_ **They   — imperfect subj the book** → _Ellas dijeran el libro_ `[noun_id=libro]`
  9. (written) We (f) (if ___ ) — imperfect subj water → _cleaned:_ **We   — imperfect subj water** → _Nosotras dijéramos agua_ `[noun_id=agua]`
  10. (auditory) She (if ___ ) — imperfect subj the bread → _cleaned:_ **She  — imperfect subj the bread** → _Ella dijera el pan_ `[noun_id=pan]`

**`grammar_subj_impf_8` — Imperfect Subjunctive — Chat 3** (lesson 16)

- **Verbs/rules:** decir, poder
- **Current anatomy:** chat P2 + chat P3
- **Issues:** CHAT-ONLY (no teaching before chat); uses P3 (no-hints chat) — consolidate to single 'chat'
- **Drill sentences:** _none in source_

### Ideal lessons

| # | Kind | Verbs / rules | Anatomy |
|---|---|---|---|
| 1 | **drill** | hablar, comer | verb chart + 10 drills |
| 2 | **drill** | vivir, estudiar | verb chart + 10 drills |
| 3 | **chat** | hablar, comer, vivir, estudiar | chat (10 possible conjugations, user does 5) |
| 4 | **drill** | ser, ir | verb chart + 10 drills |
| 5 | **drill** | estar, dar | verb chart + 10 drills |
| 6 | **chat** | ser, ir, estar, dar | chat (10 possible conjugations, user does 5) |
| 7 | **drill** | saber, haber | verb chart + 10 drills |
| 8 | **drill** | tener, hacer | verb chart + 10 drills |
| 9 | **chat** | saber, haber, tener, hacer | chat (10 possible conjugations, user does 5) |
| 10 | **drill** | querer, decir | verb chart + 10 drills |
| 11 | **drill** | poder | verb chart + 10 drills |
| 12 | **chat** | querer, decir, poder | chat (10 possible conjugations, user does 5) |

---

## Summary counts

- Total lessons: **130** across **36** grammar levels.
- Lessons mixing drill + chat in one (need to be split): **42**.
- Chat-only lessons today: **38**.
- Lessons with `0a:on` but no video: **47** (will use a `RuleChart` instead in Phase 3).
- Lessons with ≥5 `drill_sentences` but `0b:off` (dead data — flip on in Phase 1): **12**.
- Lessons using `1a` flashcards: **2**.
- Total drill sentences in source: **1020**.
  - With parenthetical clues to strip: **564**.
  - Over 6 words (need simplification, 1 longer per lesson allowed): **159**.
  - Recognizable noun in `es` but `noun_id: null` (need to set): **110**.
- Cross-lesson duplicate drill sentences detected within a module: **0**.
