#!/usr/bin/env python3
"""One-off: seed opener text for `core_1`..`core_47` into encounter_messages_generated.py.

Spanish is the canonical authored text — grounded in each encounter's
3-word workload from `seed_bank.py` so that a natural learner reply
deploys those words. en/ca/sv are produced once via gpt-4.1-mini, with
Spanish kept exactly as authored.

Usage:
    OPENAI_API_KEY=... python scripts/seed_core_openers.py [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import httpx

from app.config import settings
from app.services.encounter_messages_generated import ENCOUNTER_MESSAGES

OUT_PATH = Path(__file__).resolve().parents[1] / "app" / "services" / "encounter_messages_generated.py"

# Hand-authored Spanish openers, grounded in each encounter's word workload
# (see seed_bank.py _SUB_SITUATIONS["core"]). Each invites a reply that
# naturally uses one of the encounter's 3 target phrases. Casual `tú`
# register matches the "casual, friendly male voice" assigned to `core`.
CORE_OPENERS_ES: dict[str, str] = {
    "core_1":  "Estás muy callado, ¿qué quieres hacer ahora?",
    "core_2":  "Te ves agotado, ¿qué necesitas hacer primero?",
    "core_3":  "Hola, ¿qué puedes hacer en esta sala?",
    "core_4":  "Te veo frustrado, ¿qué cosa no puedes hacer?",
    "core_5":  "¿Qué vas a hacer ahorita, vas a quedarte o moverte?",
    "core_6":  "Hola, ¿qué estás haciendo aquí parado?",
    "core_7":  "¿Tienes mucho que hacer hoy o estás libre?",
    "core_8":  "Pareces aliviado, ¿qué cosa ya no tienes que hacer?",
    "core_9":  "¿Qué debes hacer antes de que termine el día?",
    "core_10": "Te veo concentrado, ¿qué tratas de hacer ahorita?",
    "core_11": "Oye, ¿qué necesitas de mí ahora mismo?",
    "core_12": "Aquí tengo de todo, ¿qué puedes pedirme?",
    "core_13": "Te veo apurado, ¿en qué te puedo ayudar?",
    "core_14": "Dime, ¿qué necesitas que yo haga ahora?",
    "core_15": "Te veo serio, ¿qué quieres preguntarme?",
    "core_16": "Estás confundido, ¿qué quieres que te explique?",
    "core_17": "Aquí está todo nuevo para ti, ¿qué quieres que te muestre?",
    "core_18": "¿Qué quieres que te deje hacer?",
    "core_19": "Cuéntame, ¿con qué quieres que te ayude?",
    "core_20": "Tengo un chisme raro, pero antes dime qué no quieres oír.",
    "core_21": "¿Dónde estás ahora mismo?",
    "core_22": "Te veo con prisa, ¿adónde vas?",
    "core_23": "Hola, ¿de dónde vienes a esta hora?",
    "core_24": "¿Estás cerca o lejos del lugar de la cita?",
    "core_25": "Te llamo porque te necesito, ¿qué tan lejos estás?",
    "core_26": "¿Hacia dónde te diriges en este momento?",
    "core_27": "Si quieres te recojo, ¿por dónde paso?",
    "core_28": "Estoy llegando, ¿a dónde entro primero?",
    "core_29": "¿De dónde sales para venir aquí?",
    "core_30": "Hace mal tiempo, ¿dónde te quedas hoy?",
    "core_31": "¿Ya hiciste lo que tenías pendiente?",
    "core_32": "Pasaron varias horas, ¿qué sigues haciendo?",
    "core_33": "¿Cómo va tu plan? ¿Ya empezó algo?",
    "core_34": "Te necesitamos aquí, ¿qué haces ahora mismo?",
    "core_35": "¿Cuándo nos vemos? ¿Después de qué?",
    "core_36": "Tengo varias cosas pendientes, ¿qué hago antes de qué?",
    "core_37": "¿Desde cuándo te sientes así?",
    "core_38": "¿Por cuánto tiempo te vas a quedar?",
    "core_39": "¿En cuánto tiempo llegas?",
    "core_40": "Avísame, pero ¿cuándo te paso a buscar?",
    "core_41": "Te veo incómodo, ¿qué tienes?",
    "core_42": "¿Cómo estás de ánimo y de cuerpo hoy?",
    "core_43": "Llegamos a este sitio, ¿qué te parece?",
    "core_44": "Te muestro varias opciones, ¿cuál te llama la atención?",
    "core_45": "Veo que no estás cómodo, ¿qué cosa no te gusta?",
    "core_46": "Dime con confianza, ¿qué te hace falta?",
    "core_47": "Te veo perdido, ¿qué buscas?",
}

assert len(CORE_OPENERS_ES) == 47, f"Expected 47 openers, got {len(CORE_OPENERS_ES)}"


TRANSLATE_SYSTEM = (
    "You translate Spanish (Mexican) chat openers into English (US), "
    "Catalan, and Swedish. Each input is one short conversational line. "
    "Preserve register (casual `tú`), tone, and length. Keep questions as "
    "questions. Do NOT paraphrase, expand, or moralize. Return ONLY a "
    "JSON object: {\"<id>\": {\"en\": \"...\", \"ca\": \"...\", \"sv\": \"...\"}}."
)


def translate_all(es_by_id: dict[str, str]) -> dict[str, dict[str, str]]:
    """One call to gpt-4.1-mini that returns en/ca/sv for every id."""
    user_payload = json.dumps(es_by_id, ensure_ascii=False, indent=2)
    user_msg = (
        "Translate each Spanish opener below to en, ca, sv. Return JSON "
        "keyed by the same id, with each value being an object with keys "
        "`en`, `ca`, `sv`. Do not include `es` in the output.\n\n"
        f"{user_payload}"
    )
    resp = httpx.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {settings.openai_api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": "gpt-4.1-mini",
            "response_format": {"type": "json_object"},
            "messages": [
                {"role": "system", "content": TRANSLATE_SYSTEM},
                {"role": "user", "content": user_msg},
            ],
            "temperature": 0,
        },
        timeout=120,
    )
    resp.raise_for_status()
    content = resp.json()["choices"][0]["message"]["content"]
    parsed = json.loads(content)

    missing = set(es_by_id) - set(parsed)
    if missing:
        raise RuntimeError(f"Translation missing ids: {sorted(missing)}")
    for sid, langs in parsed.items():
        if not all(k in langs for k in ("en", "ca", "sv")):
            raise RuntimeError(f"Translation for {sid} missing langs: {langs}")
    return parsed


def render_python_source(messages: dict[str, dict[str, str]]) -> str:
    lines: list[str] = [
        '"""Auto-generated per-encounter initial messages (multi-language).',
        "",
        "Generated by scripts/translate_openers.py using GPT-4.1-mini.",
        f"Total: {len(messages)} situations x 4 languages.",
        '"""',
        "",
        "ENCOUNTER_MESSAGES: dict[str, dict[str, str]] = {",
    ]
    # Preserve insertion order; new keys (added via dict.update) appear at end.
    for sid, langs in messages.items():
        lines.append(f'    "{sid}": {{')
        for lang in ("en", "es", "ca", "sv"):
            if lang in langs:
                v = langs[lang]
                # JSON-style escaping handles quotes/backslashes/control chars.
                escaped = json.dumps(v, ensure_ascii=False)
                lines.append(f'        "{lang}": {escaped},')
        lines.append("    },")
    lines.append("}")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true", help="Print result; don't write the file.")
    args = p.parse_args()

    if not settings.openai_api_key:
        sys.exit("OPENAI_API_KEY not set")

    print(f"Translating {len(CORE_OPENERS_ES)} core openers (es → en/ca/sv)…")
    translations = translate_all(CORE_OPENERS_ES)

    # Build full per-id entries: keep our authored ES, fold in translations.
    new_entries = {
        sid: {
            "en": translations[sid]["en"],
            "es": CORE_OPENERS_ES[sid],
            "ca": translations[sid]["ca"],
            "sv": translations[sid]["sv"],
        }
        for sid in CORE_OPENERS_ES
    }

    # Existing dict order is preserved; new core_* keys append at the end.
    merged: dict[str, dict[str, str]] = dict(ENCOUNTER_MESSAGES)
    overwritten = [sid for sid in new_entries if sid in merged]
    if overwritten:
        print(f"  ({len(overwritten)} core_* keys already existed and will be overwritten)")
    merged.update(new_entries)

    src = render_python_source(merged)

    if args.dry_run:
        # Show the new entries' rendered form
        sample_lines: list[str] = []
        in_section = False
        for line in src.splitlines():
            if any(f'"{sid}"' in line for sid in ("core_1", "core_2", "core_47")) and ":" in line:
                in_section = True
            if in_section:
                sample_lines.append(line)
                if line.strip() == "}," and "core_47" in src.splitlines()[len(sample_lines) - 1 - 5 : len(sample_lines)][0:1]:
                    break
        print("\n--- sample of new entries ---")
        # Simpler: just show first 20 lines mentioning core
        printed = 0
        for line in src.splitlines():
            if "core_" in line or printed > 0 and printed < 25:
                print(line)
                printed += 1
                if printed > 30:
                    break
        return

    OUT_PATH.write_text(src, encoding="utf-8")
    print(f"Wrote {OUT_PATH}  ({len(merged)} total entries; +{len(new_entries)})")


if __name__ == "__main__":
    main()
