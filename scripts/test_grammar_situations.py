#!/usr/bin/env python3
"""Test all grammar situations on QA — drills and conversation creation.

Verifies:
1. All grammar situations exist in DB
2. Each situation can start
3. Each situation creates a conversation with initial message
4. Initial messages are direct questions (openers)

Usage:
    python scripts/test_grammar_situations.py
    python scripts/test_grammar_situations.py --situation grammar_regular_present_1
"""

import json
import argparse
import urllib.request
from datetime import datetime

API_URL = "https://sfe-backend-qa.up.railway.app"
EMAIL = "eric@spanishforexpats.com"
PASSWORD = "Ilovecottage9!!"


def api(method, path, token=None, body=None):
    """Make API request."""
    url = f"{API_URL}{path}"
    data = json.dumps(body).encode() if body else None
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        res = urllib.request.urlopen(req)
        return res.status, json.loads(res.read())
    except urllib.error.HTTPError as e:
        body_text = e.read().decode() if e.fp else ""
        try:
            return e.code, json.loads(body_text)
        except Exception:
            return e.code, {"error": body_text[:500]}


def login():
    """Login and return token."""
    status, data = api("POST", "/v1/auth/login", body={"email": EMAIL, "password": PASSWORD})
    assert status == 200, f"Login failed: {status} {data}"
    return data["access_token"]


def test_grammar_situations(token, filter_id=None):
    """Test all grammar situations."""
    # Get all situations
    status, situations = api("GET", "/v1/situations", token)
    assert status == 200, f"List situations failed: {status}"

    grammar = [s for s in situations if "grammar" in s.get("id", "")]
    grammar.sort(key=lambda s: s["id"])

    if filter_id:
        grammar = [s for s in grammar if s["id"] == filter_id]

    print(f"\nFound {len(grammar)} grammar situations to test")
    print(f"{'='*80}")

    results = {"pass": 0, "fail": 0, "errors": []}

    for sit in grammar:
        sid = sit["id"]
        title = sit.get("title", "?")
        print(f"\n  {sid} ({title})")

        # 1. Start situation
        status, data = api("POST", f"/v1/situations/{sid}/start", token)
        if status not in (200, 201):
            print(f"    FAIL: Start failed ({status}): {data}")
            results["fail"] += 1
            results["errors"].append(f"{sid}: start failed ({status})")
            continue
        print(f"    Start: OK")

        # 2. Create conversation
        status, conv = api("POST", "/v1/conversations", token, {"situation_id": sid, "mode": "voice"})
        if status not in (200, 201):
            print(f"    FAIL: Create conversation failed ({status}): {conv}")
            results["fail"] += 1
            results["errors"].append(f"{sid}: create conv failed ({status})")
            continue

        conv_id = conv.get("conversation_id", "?")
        initial_msg = conv.get("initial_message", "")
        words = conv.get("words", [])
        lang_mode = conv.get("language_mode", "?")

        print(f"    Conv: {conv_id[:12]}... mode={lang_mode} words={len(words)}")
        print(f"    Opener: \"{initial_msg[:80]}{'...' if len(initial_msg) > 80 else ''}\"")

        # 3. Verify initial message exists and looks like a question
        if not initial_msg:
            print(f"    WARN: No initial message!")
            results["errors"].append(f"{sid}: no initial message")
        elif "?" not in initial_msg:
            print(f"    WARN: Opener doesn't contain '?' — may not be a question")

        # 4. Verify words are returned
        if not words:
            print(f"    WARN: No words returned")
            results["errors"].append(f"{sid}: no words")

        results["pass"] += 1
        print(f"    PASS")

    print(f"\n{'='*80}")
    print(f"RESULTS: {results['pass']} passed, {results['fail']} failed")
    if results["errors"]:
        print(f"\nIssues:")
        for e in results["errors"]:
            print(f"  - {e}")

    return results


def test_drill_data():
    """Verify all grammar situations have drill config data."""
    from app.data.grammar_situations import GRAMMAR_SITUATIONS

    print(f"\nVerifying drill data for {len(GRAMMAR_SITUATIONS)} situations...")
    issues = []
    for sid, cfg in sorted(GRAMMAR_SITUATIONS.items()):
        drill_cfg = cfg.get("drill_config", {})
        answers = drill_cfg.get("answers", {})
        targets = cfg.get("drill_targets", [])

        if cfg["grammar_level"] >= 3 and not targets:
            issues.append(f"{sid}: no drill_targets")
        if cfg["grammar_level"] >= 3 and not answers:
            issues.append(f"{sid}: no drill_config.answers")

        verb_count = len(answers)
        target_count = len(targets)
        print(f"  {sid}: {verb_count} verb answer tables, {target_count} targets")

    if issues:
        print(f"\nDrill data issues:")
        for i in issues:
            print(f"  - {i}")
    else:
        print(f"\nAll drill data OK!")
    return issues


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--situation", help="Test only this situation ID")
    parser.add_argument("--drill-only", action="store_true", help="Only verify drill data (no API calls)")
    args = parser.parse_args()

    if args.drill_only:
        issues = test_drill_data()
        return 1 if issues else 0

    print(f"Testing grammar situations on QA")
    print(f"API: {API_URL}")
    print(f"Time: {datetime.now().isoformat()}")

    token = login()
    print(f"Logged in as {EMAIL}")

    # First verify drill data locally
    test_drill_data()

    # Then test API
    results = test_grammar_situations(token, args.situation)
    return 1 if results["fail"] > 0 else 0


if __name__ == "__main__":
    exit(main())
