> **HISTORICAL — superseded.** The monothematic standard was confirmed and the database has been restructured to comply. See `docs/decisions/monothematic-encounters.md` for the authoritative record. This document is preserved for context, not as an active requirement.

# Monothematic Situation Requirement

## Standard
**EVERY ENCOUNTER FOR A GIVEN SITUATION MUST BE ABOUT THE EXACT SAME THING.**

This means:
- Each situation should have 50 encounters (encounter numbers 1-50)
- All 50 encounters within a situation must be about the same theme/topic
- If encounters 1-25 are about "checking in" but 26-50 are about "security", that's a failure
- Instead, create separate situations: "Checking in at the Airport" and "Going Through Security at the Airport"

## Current Database Status

### ❌ ISSUE: Database is NOT Monothematic

The current database structure has situations that mix multiple themes within the same category. For example:

**Airport Category (50 situations):**
- 14 different themes detected:
  - "Checking in at the Airport": 10 situations
  - "Going Through Security": 5 situations
  - "Customs Declaration": 5 situations
  - "On the Plane": 4 situations
  - "Collecting Baggage": 4 situations
  - And 9 more themes...

**All Categories Have This Issue:**
- Banking: 32 different themes
- Clothing: 38 different themes
- Contractor: 25 different themes
- Groceries: 25 different themes
- Internet: 23 different themes
- Mechanic: 25 different themes
- Police: 16 different themes
- Restaurant: 25 different themes
- Small Talk: 21 different themes

## Required Fix

### Option 1: Restructure Database (Recommended)
Split each theme into its own situation with 50 encounters:

**Example for Airport:**
- Situation: "Checking in at the Airport" → 50 encounters (1-50)
- Situation: "Going Through Security" → 50 encounters (1-50)
- Situation: "Customs Declaration" → 50 encounters (1-50)
- etc.

### Option 2: Group by Theme
Group existing situations by theme and ensure each theme has exactly 50 encounters.

## Animation Prompts CSV

The file `scenario_animation_prompt.csv` has been generated with:
- **25,000 encounters** (500 situations × 50 encounters each)
- Each situation uses the same animation prompt for all 50 encounters
- Animation prompts are theme-specific where possible

**CSV Structure:**
- `situation_id`: The situation ID (e.g., "airport_1")
- `encounter_number`: Encounter number within situation (1-50)
- `encounter_id`: Full encounter ID (e.g., "airport_1_1", "airport_1_2", etc.)
- `animation_prompt`: The animation description for this encounter

## Next Steps

1. **Review the monothematic violations** - Each category needs to be split into separate situations by theme
2. **Update database schema** - Ensure each situation has exactly 50 encounters
3. **Update application code** - Ensure code handles encounters correctly (1-50 per situation)
4. **Regenerate CSV** - Once database is restructured, regenerate the animation prompts CSV

## Verification Script

Run the monothematic check:
```bash
cd SpanishForExpats_BE
source venv/bin/activate
python scripts/list_situations.py
```

This will show which categories have multiple themes and need to be split.


