#!/usr/bin/env python3
"""Build new seed_bank _SUB_SITUATIONS data from cleaned_triplets.json.

Outputs Python code to paste into seed_bank.py.

Usage: .venv/bin/python scripts/build_seed_bank.py > /tmp/new_sub_situations.py
"""

import json
import os
import sys

CLEANED = os.path.join(os.path.dirname(__file__), "cleaned_triplets.json")

# Mapping from master file category → seed_bank config
CATEGORY_CONFIG = {
    "Clothing": {
        "animation_type": "clothing",
        "word_prefix": "cloth",
        "title": "Clothing Shopping",
        "goal": "Navigate a clothing store, find your size, make a purchase, and handle returns",
    },
    "Groceries": {
        "animation_type": "groceries",
        "word_prefix": "groc",
        "title": "At the Supermarket",
        "goal": "Check out at the supermarket, handle pricing issues, and bag your groceries",
    },
    "Banking": {
        "animation_type": "banking",
        "word_prefix": "bank",
        "title": "Banking",
        "goal": "Handle banking tasks including accounts, transfers, cards, and loans",
    },
    "Airport": {
        "animation_type": "airport",
        "word_prefix": "air",
        "title": "Checking In",
        "goal": "Complete the airport check-in process with the airline agent",
    },
    "Restaurant": {
        "animation_type": "restaurant",
        "word_prefix": "rest",
        "title": "Eating Out",
        "goal": "Order food, interact with the server, and pay for your meal",
    },
    "Small Talk with a Neighbour": {
        "animation_type": "small_talk",
        "word_prefix": "talk",
        "title": "Meeting a Neighbor",
        "goal": "Have a friendly conversation with your neighbor about building life",
    },
    "Construction Contractor": {
        "animation_type": "contractor",
        "word_prefix": "contr",
        "title": "Hiring a Contractor",
        "goal": "Manage a construction project, discuss plans, costs, and quality with your contractor",
    },
    "Mechanic": {
        "animation_type": "mechanic",
        "word_prefix": "mech",
        "title": "At the Mechanic",
        "goal": "Describe car problems, get a diagnosis, and handle repairs and payment",
    },
    "Police Traffic Stop": {
        "animation_type": "police",
        "word_prefix": "pol",
        "title": "Traffic Stop",
        "goal": "Handle a traffic stop calmly by providing documents and following instructions",
    },
}


def main():
    with open(CLEANED) as f:
        categories = json.load(f)

    # Generate _SUB_SITUATIONS
    print("_SUB_SITUATIONS = {")
    for cat_name, config in CATEGORY_CONFIG.items():
        triplets = categories[cat_name]
        anim = config["animation_type"]
        prefix = config["word_prefix"]
        title = config["title"]
        goal = config["goal"]

        # Build words list: 150 tuples (spanish, english, catalan)
        # Catalan set to "" for now
        words_tuples = []
        for t in triplets:
            for w in t["words"]:
                words_tuples.append(f'("{w}", "", "")')

        words_str = ",\n            ".join(words_tuples)

        print(f'    "{anim}": [')
        print(f"        {{")
        print(f'            "word_prefix": "{prefix}",')
        print(f'            "title": "{title}",')
        print(f'            "goal": "{goal}",')
        print(f'            "words": [')
        print(f"            {words_str},")
        print(f"            ],")
        print(f"        }},")
        print(f"    ],")

    print("}")

    # Generate openers dict
    print("\n\n# --- Openers ---")
    print("ENCOUNTER_OPENERS = {")
    for cat_name, config in CATEGORY_CONFIG.items():
        triplets = categories[cat_name]
        prefix = config["word_prefix"]
        for i, t in enumerate(triplets):
            sid = f"{prefix}_{i+1}"
            opener = t["opener"].replace('"', '\\"')
            print(f'    "{sid}": "{opener}",')
    print("}")


if __name__ == "__main__":
    main()
