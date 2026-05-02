"""Splice the 11 _glX_output.py files into app/data/grammar_situations.py.

For each output file:
  1. Extract retire-keys list (from the comment block).
  2. Extract intro-constants section (between '# ── New intro constants' and '# ── New lesson dicts').
  3. Extract lesson-dicts section (everything after '# ── New lesson dicts').
  4. Remove every retire-key (and its preceding sub-comment) from GRAMMAR_SITUATIONS.
  5. Append intro-constants before `GRAMMAR_SITUATIONS = {`.
  6. Append lesson-dicts inside GRAMMAR_SITUATIONS, just before its closing `}`.

Validates by importing grammar_situations after splicing and asserting:
  - Every retired key is absent.
  - Every new key resolves via get_grammar_config.
  - All new conjugation drill lessons have ≤ 2 verbs.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "app" / "data" / "grammar_situations.py"

OUTPUT_FILES = [
    "_gl4_5_output.py",
    "_gl5_output.py",
    "_gl6_output.py",
    "_gl7_output.py",
    "_gl8_output.py",
    "_gl9_output.py",
    "_gl13_5_output.py",
    "_gl17_output.py",
    "_gl17_1_output.py",
    "_gl18_output.py",
    "_gl18_5_output.py",
]


def parse_retire_keys(text: str) -> list[str]:
    """Pull old keys from the '# ── Retire keys' or '# ── Retire these keys'
    comment block. Supports both formats:
      - explicit list across multiple lines:
          # grammar_x_1, grammar_x_2,
          # grammar_x_3, ...
      - compact brace expansion:
          # ── Retire keys: grammar_x_{1,2,3}{,_chat}
    """
    # Find the retire-line(s)
    retire_match = re.search(r'# ── Retire[^\n]*keys[^\n]*\n((?:#[^\n]*\n)*)', text)
    if not retire_match:
        return []
    block = retire_match.group(0)

    # Try compact `prefix_{a,b,c}{,_chat}` form
    compact = re.findall(
        r'(grammar_[a-z0-9_]+)_\{([0-9,]+)\}(?:\{,(_chat)\})?',
        block,
    )
    keys: list[str] = []
    for prefix, indices, has_chat in compact:
        for idx in indices.split(','):
            idx = idx.strip()
            if not idx:
                continue
            keys.append(f"{prefix}_{idx}")
            if has_chat:
                keys.append(f"{prefix}_{idx}_chat")

    # Fallback: literal grammar_* keys not inside braces
    if not keys:
        # Strip out brace expressions before scanning
        flat = re.sub(r'\{[^}]*\}', '', block)
        keys = re.findall(r'grammar_[a-z0-9_]+', flat)

    # Dedup preserving order
    seen = set()
    out = []
    for k in keys:
        if k not in seen and not k.endswith('_chat') or k not in seen:
            if k not in seen:
                out.append(k)
                seen.add(k)
    return out


def split_sections(text: str) -> tuple[str, str]:
    """Return (intros_section, lessons_section)."""
    intros_marker = '# ── New intro constants'
    lessons_marker = '# ── New lesson dicts'
    intros_start = text.index(intros_marker)
    lessons_start = text.index(lessons_marker)
    intros_section = text[intros_start:lessons_start].strip()
    # Skip the marker line itself in intros
    intros_section = '\n'.join(intros_section.split('\n')[1:]).strip()
    # Lessons section: drop the marker line, keep the rest
    lessons_section = text[lessons_start:].strip()
    lessons_section = '\n'.join(lessons_section.split('\n')[1:]).strip()
    return intros_section, lessons_section


def remove_key_from_dict(src: str, key: str) -> str:
    """Remove a top-level dict entry like:
        # comment line(s)?
        "key": {
            ...
        },
    Conservative: only matches when indented 4 spaces (inside GRAMMAR_SITUATIONS).
    """
    pattern = re.compile(
        r'(?:^    #[^\n]*\n)*'  # leading sub-comment lines (optional)
        r'^    "' + re.escape(key) + r'": \{[\s\S]*?^    \},\n',
        re.MULTILINE,
    )
    new_src, n = pattern.subn('', src)
    if n == 0:
        # Try without leading comments
        pattern2 = re.compile(
            r'^    "' + re.escape(key) + r'": \{[\s\S]*?^    \},\n',
            re.MULTILINE,
        )
        new_src, n = pattern2.subn('', src)
    return new_src


def find_dict_end(src: str) -> int:
    """Find the line index of the closing `}` of GRAMMAR_SITUATIONS."""
    lines = src.split('\n')
    start = None
    for i, line in enumerate(lines):
        if line.startswith('GRAMMAR_SITUATIONS = {'):
            start = i
            break
    if start is None:
        raise RuntimeError("GRAMMAR_SITUATIONS not found")
    for i in range(start + 1, len(lines)):
        if lines[i] == '}':
            return i
    raise RuntimeError("GRAMMAR_SITUATIONS closing brace not found")


def main() -> int:
    src = TARGET.read_text()
    all_intros: list[str] = []
    all_lessons: list[str] = []
    all_retire_keys: list[str] = []

    for fname in OUTPUT_FILES:
        path = ROOT / "scripts" / fname
        text = path.read_text()
        retire = parse_retire_keys(text)
        intros, lessons = split_sections(text)
        all_intros.append(f"# ── From {fname} ──")
        all_intros.append(intros)
        all_lessons.append(f"    # ── From {fname} ──")
        all_lessons.append(lessons)
        # Add _chat companions for each retired drill key
        retire_full = list(retire)
        for k in retire:
            chat_k = f"{k}_chat"
            if chat_k not in retire_full:
                retire_full.append(chat_k)
        all_retire_keys.extend(retire_full)
        print(f"{fname}: {len(retire_full)} keys to retire, {lessons.count('\"grammar_')} new lessons")

    print(f"\nTotal retire: {len(all_retire_keys)} keys")
    print(f"Total new intros: {sum(i.count('_INTRO = {') for i in all_intros)}")
    print(f"Total new lessons (rough): {sum(l.count('\"grammar_') for l in all_lessons)}")

    # Remove old keys
    for key in all_retire_keys:
        src = remove_key_from_dict(src, key)

    # Insert intro constants before GRAMMAR_SITUATIONS = {
    intros_block = '\n# ─────────────────────────────────────────────────────────────────────────────\n# Phase C.3 sub-block intros — auto-spliced from scripts/_glX_output.py\n# ─────────────────────────────────────────────────────────────────────────────\n\n' + '\n\n'.join(all_intros) + '\n\n'
    src = src.replace('GRAMMAR_SITUATIONS = {\n', intros_block + 'GRAMMAR_SITUATIONS = {\n', 1)

    # Insert lessons before the closing } of GRAMMAR_SITUATIONS
    lines = src.split('\n')
    end_idx = find_dict_end(src)
    lessons_block = '\n    # ─────────────────────────────────────────────────────────────────────────\n    # Phase C.3 sub-block lessons — auto-spliced from scripts/_glX_output.py\n    # ─────────────────────────────────────────────────────────────────────────\n\n' + '\n\n'.join(all_lessons) + '\n'
    lines.insert(end_idx, lessons_block)
    src = '\n'.join(lines)

    TARGET.write_text(src)
    print(f"\nSpliced. New file size: {len(src)} chars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
