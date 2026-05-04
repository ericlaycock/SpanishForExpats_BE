"""Dump the lesson metadata that the FE PDF generator consumes.

Writes /tmp/grammar_lessons.json with one entry per lesson: identifying
fields (sid/title/level/etc.), intro card count, and — crucially — the
intro_chart's recall list, so the PDF script can fill recall inputs and
walk every step.
"""
import json
import sys

sys.path.insert(0, '.')
from app.data.grammar_situations import GRAMMAR_SITUATIONS, GL_TITLES


def recall_steps(intro_chart):
    """Return [{verb, answers: {pronoun: form_without_pipe}}, …] for the FE."""
    if not intro_chart:
        return []
    recall = intro_chart.get('recall')
    if not recall:
        return []
    if isinstance(recall, dict):
        recall = [recall]
    out = []
    for r in recall:
        verb = r.get('verb')
        ans = r.get('answers') or {}
        if not verb:
            continue
        out.append({
            'verb': verb,
            'answers': {p: (form or '').replace('|', '') for p, form in ans.items()},
        })
    return out


def main():
    lessons = []
    for sid, cfg in GRAMMAR_SITUATIONS.items():
        intro = cfg.get('intro_chart') or {}
        cards = intro.get('cards') or []
        lessons.append({
            'sid': sid,
            'title': cfg.get('title', sid),
            'grammar_level': cfg.get('grammar_level'),
            'gl_title': GL_TITLES.get(cfg.get('grammar_level'), str(cfg.get('grammar_level'))),
            'lesson_number': cfg.get('lesson_number'),
            'lesson_type': cfg.get('lesson_type'),
            'drill_type': cfg.get('drill_type'),
            'tense': cfg.get('tense'),
            'word_workload': cfg.get('word_workload', []),
            'has_intro': bool(intro),
            'intro_card_count': len(cards) if cards else (1 if intro else 0),
            'intro_recall_steps': recall_steps(intro),
            'phases': cfg.get('phases', {}),
        })
    lessons.sort(key=lambda L: (L['grammar_level'] or 0, L['lesson_number'] or 0))
    with open('/tmp/grammar_lessons.json', 'w') as f:
        json.dump(lessons, f, ensure_ascii=False, indent=2)
    print(f'Dumped {len(lessons)} lessons')


if __name__ == '__main__':
    main()
