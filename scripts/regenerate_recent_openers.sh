#!/usr/bin/env bash
# Regenerate R2 audio for every encounter opener whose Spanish text
# was rewritten in PR #31 (airport, 32 sids) and PR #35 (the other 9
# topics, 257 sids). Total: 289 sids.
#
# Why a script: production R2 holds the OLD audio for these sids
# (the file is keyed by `initial_msg_<sid>.mp3`, no version suffix).
# After merging the text PRs the avatar would still play the old
# dead-end audio until somebody runs `pregenerate_initial_audio.py
# --force` for each rewritten sid. This script is the canonical
# `force-everything-the-text-PRs-touched` runner.
#
# Usage:
#   ./scripts/regenerate_recent_openers.sh
#
# Run from the repo root. Requires Railway CLI logged in to the
# project so `railway run` injects R2_* and OPENAI_API_KEY env vars.
# `--force` makes the script overwrite even if the R2 file exists,
# which is what we want — re-runs after a partial failure are safe.
#
# Cost: ~$1-2 in OpenAI Realtime + a handful of MB to R2.
# Time: ~10 min on a stable connection (script logs every 50 sids).
#
# After this script finishes you can delete it; it's meant to be
# one-off cleanup tied to the two PRs above.

set -euo pipefail

cd "$(dirname "$0")/.."

railway run .venv/bin/python scripts/pregenerate_initial_audio.py \
  air_4 air_9 air_11 air_12 air_13 air_15 air_16 air_17 air_21 air_22 \
  air_25 air_26 air_27 air_28 air_29 air_30 air_31 air_32 air_33 air_35 \
  air_37 air_38 air_39 air_40 air_41 air_42 air_43 air_44 air_46 air_48 \
  air_49 air_50 \
  bank_9 bank_13 bank_15 bank_19 bank_23 bank_24 bank_25 bank_26 bank_27 \
  bank_29 bank_30 bank_31 bank_32 bank_33 bank_34 bank_35 bank_37 bank_40 \
  bank_41 bank_43 bank_44 bank_47 bank_49 bank_50 \
  cloth_7 cloth_10 cloth_11 cloth_12 cloth_15 cloth_16 cloth_17 cloth_18 \
  cloth_19 cloth_20 cloth_21 cloth_22 cloth_23 cloth_25 cloth_26 cloth_27 \
  cloth_28 cloth_29 cloth_30 cloth_31 cloth_33 cloth_34 cloth_35 cloth_36 \
  cloth_37 cloth_38 cloth_39 cloth_40 cloth_41 cloth_42 cloth_43 cloth_44 \
  cloth_45 cloth_47 cloth_48 cloth_49 cloth_50 \
  contr_1 contr_2 contr_4 contr_5 contr_6 contr_7 contr_8 contr_9 contr_10 \
  contr_11 contr_12 contr_13 contr_14 contr_15 contr_17 contr_18 contr_19 \
  contr_20 contr_21 contr_22 contr_23 contr_24 contr_25 contr_26 contr_27 \
  contr_28 contr_29 contr_30 contr_31 contr_32 contr_33 contr_34 contr_35 \
  contr_36 contr_37 contr_38 contr_39 contr_40 contr_41 contr_42 contr_43 \
  contr_44 contr_45 contr_46 contr_47 contr_48 contr_49 contr_50 \
  groc_1 groc_2 groc_3 groc_4 groc_5 groc_6 groc_7 groc_8 groc_9 groc_10 \
  groc_11 groc_12 groc_13 groc_14 groc_15 groc_16 groc_18 groc_20 groc_21 \
  groc_22 groc_23 groc_24 groc_25 groc_26 groc_27 groc_28 groc_29 groc_30 \
  groc_31 groc_32 groc_35 groc_36 groc_37 groc_38 groc_40 groc_41 groc_42 \
  groc_43 groc_44 groc_45 groc_46 groc_47 groc_48 groc_49 groc_50 \
  inet_13 inet_43 inet_46 \
  mech_10 mech_11 mech_12 mech_13 mech_15 mech_17 mech_18 mech_19 mech_20 \
  mech_21 mech_23 mech_24 mech_25 mech_26 mech_27 mech_28 mech_30 mech_31 \
  mech_32 mech_33 mech_34 mech_35 mech_36 mech_37 mech_39 mech_43 mech_44 \
  mech_45 mech_46 mech_47 mech_48 mech_49 mech_50 \
  pol_1 pol_7 pol_8 pol_9 pol_10 pol_11 pol_12 pol_14 pol_15 pol_16 \
  pol_17 pol_18 pol_19 pol_20 pol_25 pol_26 pol_27 pol_28 pol_29 pol_30 \
  pol_31 pol_32 pol_33 pol_34 pol_35 pol_40 pol_41 pol_43 pol_44 pol_45 \
  pol_46 pol_48 pol_49 pol_50 \
  rest_1 rest_4 rest_19 rest_20 rest_22 rest_23 rest_25 rest_26 rest_29 \
  rest_30 rest_32 rest_35 rest_36 rest_38 rest_42 rest_43 rest_44 rest_45 \
  rest_48 rest_50 \
  talk_4 talk_5 talk_7 talk_8 talk_11 talk_12 talk_14 talk_15 talk_22 \
  talk_23 talk_24 talk_31 talk_36 \
  --force
