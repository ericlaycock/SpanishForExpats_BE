# Trial "First Perfect Word" + Memory-Bar Loop

> **Status:** Proposal (design approved 2026-06-11, pending spec review). Not yet built.
> **Surface:** Free-trial **Memory Miracle** flow (`/freetrial/mm`). Replaces the current
> single long-phrase opener with a repeating *one-word → use-it-in-sentences* loop.
> **Why:** The trial's first memorization moment is the conversion lever (free-trial
> north-star). Today it opens by encoding a whole curated/LLM-picked phrase. We replace
> that with a single, perfectly-chosen first **word** so the "I memorized it!" beat lands
> hard, then deploy that word in sentences, then repeat.

---

## 1. The four criteria for a "perfect first word"

The very first word a user is asked to memorize must be:

1. **New** — not a recognizable cognate, not a word they already half-know. If it's
   familiar, memorizing it isn't impressive ("I already knew it").
2. **Obviously useful** — something a learner feels powerful deploying immediately
   (`quisiera` "I would like" ✓; `aprender` "to learn" ✗ — useless to a raw beginner).
3. **Easy to memorize** — a quick win. Hard first words cause churn.
4. **For intermediates: a past-tense verb conjugation** — intermediates aren't impressed
   by learning a noun; they're impressed by *mastering a conjugation*.

Criterion #1 is enforced at runtime by the **"I recognize this word"** button (§4).

---

## 2. Core loop

Replaces the "encode one long phrase" opener with a repeating beat:

1. **Level gate** (3 buttons) → sets the starting **tier** (§3).
2. **Show ONE candidate word** (Spanish + English) with two buttons:
   **"Memorize this word"** and **"I recognize this word."**
3. **"I recognize this word"** → the word fails criterion #1 → **jump up one tier**
   (capped at the top tier) and show that tier's first word. Repeat until the user hits a
   genuinely-new word.
4. **"Memorize this word"** → run the **memory-bar encoding loop** (§5). On completion,
   **deploy the word in 3 sentences** (§6).
5. **Next cycle** → advance to the **next word in the current tier**; memorize → sentences.
6. After **N cycles** (default **3**) → the conversion moment (value before the ask).

**Key asymmetry:**
- **"I recognize"** ⇒ the user is *under-leveled* ⇒ **jump tier** (capped).
- **"Memorize"** ⇒ the user is at the *right* level ⇒ **advance within the tier**.

---

## 3. Tiers and word banks

Stored server-side in a new data module `app/data/trial_first_words.py` (sibling of
`app/data/trial_phrases.py`). Each tier is an **ordered** list; index 0 is the word shown
first when a user lands on that tier.

| Tier | Label (button copy) | Ordered words (first → later) | Rationale |
|---|---|---|---|
| **0 · Absolute** | "I'm new" | `quisiera` (I'd like) · `busco` (I'm looking for) · `pido` (I'll order / ask for) · `hay` (there is / are) | High-utility, near-zero chance an absolute beginner already knows them. `quisiera` leads: maximally useful, non-cognate, still an easy win. |
| **1 · Mid-beginner** | "Not new to Spanish but I can't make sentences yet" | `consigo` (I get / manage) · `suelo` (I usually…) · `quieren` (they want) · `pueden` (they can) | 1st-person irregulars + a 3rd-person-plural stretch (conjugation that's a notch harder). |
| **2 · Intermediate** | "Can make sentences but verbs need work" | `quiso` (he/she wanted) · `pudo` (could) · `tuvo` (had) · `dijo` (said) · `hizo` (did / made) | 3rd-person **preterite irregulars** — the conjugation flex that impresses (criterion #4). |

Word-bank rules:
- **LATAM Spanish only** — no `vosotros`, no `os` reflexive, no `-áis/-éis/-ís`. (All words
  above comply.)
- Each entry carries `{ es, en }` and may carry an optional `note`/syllable hint for the
  encoding screen.
- Banks are hand-vetted and **reorderable** without code changes (data, not logic).

---

## 4. Tiering logic ("hybrid")

> ⚠️ **Spec-review confirmation needed:** the reading below treats the explicit button tap
> as the primary tier signal and the recognize-button as the upward correction. Confirm
> this is the intended "hybrid" (vs. the LLM auto-setting the tier from intake with no tap).

- **Primary signal — explicit 3-button self-rating** sets the starting tier (floor), using
  the exact copy in §3's "Label" column.
- **Self-correction — "I recognize this word"** bumps the user **up one tier in real time**,
  **capped at Tier 2**. If they recognize the top-tier word too, they land on a hard word
  and attempt it regardless (no infinite climb).
- **LLM (light, optional)** — read the user's free-text intake and *pre-highlight* the
  button it infers fits. The user's tap is always authoritative.

Worked tier path: user taps "I'm new" → sees `quisiera` → taps "I recognize this word" →
jumps to Tier 1, sees `consigo` → taps "I recognize this word" → jumps to Tier 2, sees
`quiso` → taps "Memorize this word" (genuinely new) → encoding loop.

---

## 5. The memory-bar loop (one stable screen per word)

The single most important UX change: from the moment a user starts memorizing a word to the
moment they finish, **the frame does not change**.

### Layout (invariant)
- The **word stays centered** on screen.
- A **memorized bar** is pinned on the **left**.
- Only the **instruction area beneath the word** swaps between activities. There is **no
  route/screen transition** mid-word — the same frame hosts every activity and gut-check.

### The bar = felt progress
The bar blends two inputs:
- **Auto-fill** (time-on-task): **+1% every 5 seconds** while an activity's timer runs.
- **Gut-check jumps** (self-reported confidence, 0–100): set between activities.

### Auto-fill rules
- **Per-activity cap decays each round** so it "auto-fills less and less":
  - Activity 1: up to **+12%** (~60s at 1%/5s)
  - Activity 2: up to **+6%** (~30s)
  - Activity 3: up to **+3%**, then **+1.5%**, … (**halving** each activity)
- **Freeze rule:** auto-fill **never moves the bar when current value is > 80%.** Past 80%,
  only gut-checks advance it.

### Gut checks
- Between activities, ask: **"How well do you know it now? (0–100)"**
- The bar **jumps up** to their answer. **Monotonic** — it never decreases:
  `bar = max(bar, reported)`.

### Completion
- Because auto-fill caps at 80%, **only a gut check can reach 100%.**
- Reaching **100%** ends the word → advance to the 3-sentence deploy (§6).

### Activity script (cycles until 100%)
1. **Air-trace + say aloud** (trace the word in the air while repeating it out loud).
2. **Sensory encoding** (color → landscape → eyes-closed, connecting an image to the
   "coldest"/most-foreign syllable).
3. **Eyes-closed full recall** (reconstruct the whole word from memory).
4. Repeat (2)/(3) variants until a gut check closes the loop at 100%.

> Implementation note: today these activities live as **separate screens** —
> `GuidedMemorize.tsx` (air-trace, 60s fade) and `MemoryActivity2.tsx` (syllable → color →
> landscape → eyes-closed). This proposal **refactors them under one persistent frame +
> bar**, interleaved with gut checks. `segmentWord()` (syllable splitting) and the color
> palette are reused as-is.

### Worked example
```
0%
  → [air-trace + say aloud]            auto-fill +12%  → 12%
  → gut check: "50"                    jump           → 50%
  → [color / landscape / eyes-closed]  auto-fill +6%   → 56%
  → gut check: "80"                    jump           → 80%
  → [eyes-closed full recall]          auto-fill FROZEN (>80%)  → 80%
  → gut check: "100"                   jump           → 100%  ✅ done → sentences
```

---

## 6. Deploy beat — "use it in a sentence" (reuse existing drill)

After a word hits 100%, the user uses it in **3 fill-in-the-blank sentences** — the
established free-trial application phase. **Reuse the existing pattern as-is:**

- **Component:** `app/[locale]/freetrial/memorize/SentencePractice.tsx` — 3 sentences,
  alternating **typed → spoken → typed**.
- **Endpoint:** `POST /v1/memorize/sentences` (`app/api/v1/memorize.py:248`) — given
  `{ es, en }`, GPT-4.1 returns 3 short LATAM sentences, each with the target replaced by
  `_____`. Shape: `{ sentences: [{ en, blank }] }`.
- **Checking:** `answersMatch()` / `sentenceMatches()` (`components/tensequest/lib.ts:38`) —
  accent/case/punctuation-tolerant, accepts leading-pronoun variants, accepts just the
  blanked word.
- The **target word is the single memorized word** (`es`/`en` from the tier bank), not a
  phrase.

> Optional extension (flag for review): the endpoint currently takes only `{ es, en }`.
> We *could* pass the user's intake goal so the 3 sentences are themed to their real-life
> context. Default: leave the endpoint unchanged for v1.

---

## 7. Components & endpoints

**Backend**
- `app/data/trial_first_words.py` *(new)* — the three ordered tier banks.
- `app/api/v1/trial.py` *(extend)* — endpoint to serve the next word given
  `{ tier, index, recognized }` (keep selection server-side for control over ordering and
  the tier-jump cap). Returns `{ es, en, tier, note? }`.
- `app/api/v1/memorize.py` — **reused unchanged** (`/sentences`).

**Frontend** (`app/[locale]/freetrial/mm/` + `app/[locale]/freetrial/memorize/`)
- **LevelGate** *(new)* — the 3-button tier question (§3 copy).
- **WordCard** *(new)* — centered word + "Memorize this word" / "I recognize this word".
- **MemoryBarFrame** *(new)* — the invariant frame (word + left bar) hosting the activity
  script and gut checks; absorbs/refactors `GuidedMemorize` + `MemoryActivity2`.
- **SentencePractice** — **reused** for the 3-sentence deploy.
- Orchestrator: extend `MemoryMiracleFlow.tsx` (or a new sibling) with the state machine:
  `tier`, `wordIndex`, `recognizedCount`, `barValue`, `cycleCount`.

---

## 8. Tunable parameters (defaults)

| Parameter | Default | Notes |
|---|---|---|
| Auto-fill rate | +1% / 5s | |
| Per-activity cap decay | halving (12 → 6 → 3 → 1.5…) | |
| Auto-fill freeze threshold | > 80% | above this, only gut checks move the bar |
| Completion threshold | 100% (gut check only) | |
| Cycles before conversion ask | 3 | one cycle = one word memorized + its 3 sentences |
| Tier-jump cap | top tier (Tier 2) | no infinite climb |

---

## 9. Out of scope (v1) / later

- The conversion-ask content/placement after N cycles (separate flow).
- Full LLM auto-tiering from intake (we ship only the *light pre-highlight*).
- Goal-themed sentence generation (the §6 optional extension).
- Analytics/event instrumentation for the loop.

## 10. Open questions for spec review

1. **Hybrid tiering (§4):** confirm explicit-button-primary + recognize-correction is the
   intended read (vs. LLM auto-setting the tier with no tap).
2. **Within-tier ordering:** deterministic fixed order (default) vs. adapt the next word to
   the user's goal?
3. **Sentence theming (§6):** keep `/sentences` as `{es, en}` only, or pass goal context?
