#!/usr/bin/env python3
"""
Direct Translation Updater - Uses inline AI translations
This script directly translates and updates files with proper translations.
"""

import re
from pathlib import Path
from typing import Dict, Tuple

CYPHER_DIR = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/cypher")

# Translation dictionary - We'll use AI to generate these
TRANSLATIONS = {
    # File: ABORTION-AND-GOLDEN-RULE.md
    "Abortion And Golden Rule": {
        "content": "Abortion is a violation of the Golden Rule: \"Do unto others as you would have them do into you.\"",
        "es_title": "El Aborto y la Regla de Oro",
        "es_content": "El aborto es una violación de la Regla de Oro: \\\"Haz a los demás lo que quieras que te hagan a ti.\\\"",
        "fr_title": "L'avortement et la Règle d'Or",
        "fr_content": "L'avortement est une violation de la Règle d'Or : \\\"Fais aux autres ce que tu voudrais qu'ils te fassent.\\\"",
        "hi_title": "गर्भपात और स्वर्णिम नियम",
        "hi_content": "गर्भपात स्वर्णिम नियम का उल्लंघन है: \\\"दूसरों के साथ वैसा ही करो जैसा तुम चाहते हो कि तुम्हारे साथ किया जाए।\\\"",
        "zh_title": "堕胎与黄金法则",
        "zh_content": "堕胎违反了黄金法则：\\\"己所不欲，勿施于人。\\\""
    },
    # We'll add more as we process them
}


def update_single_file(file_path: Path, en_title: str, translations: Dict[str, str]) -> bool:
    """Update a single file with translations."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace placeholders
        updated = content
        updated = updated.replace(
            'es_title: "TITULO DEL PENSAMIENTO"',
            f'es_title: "{translations["es_title"]}"'
        )
        updated = updated.replace(
            'es_content: "CONTENIDO DEL PENSAMIENTO"',
            f'es_content: "{translations["es_content"]}"'
        )
        updated = updated.replace(
            'fr_title: "TITRE DE LA PENSÉE"',
            f'fr_title: "{translations["fr_title"]}"'
        )
        updated = updated.replace(
            'fr_content: "CONTENU DE LA PENSÉE"',
            f'fr_content: "{translations["fr_content"]}"'
        )
        updated = updated.replace(
            'hi_title: "शिखा"',
            f'hi_title: "{translations["hi_title"]}"'
        )
        updated = updated.replace(
            'hi_content: "सामग्री"',
            f'hi_content: "{translations["hi_content"]}"'
        )
        updated = updated.replace(
            'zh_title: "biāo tí"',
            f'zh_title: "{translations["zh_title"]}"'
        )
        updated = updated.replace(
            'zh_content: "nèi róng"',
            f'zh_content: "{translations["zh_content"]}"'
        )
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated)
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def main():
    """Update files with translations."""
    # Start with first file
    file_path = CYPHER_DIR / "ABORTION-AND-GOLDEN-RULE.md"
    en_title = "Abortion And Golden Rule"
    
    if en_title in TRANSLATIONS:
        print(f"Updating {file_path.name}...")
        if update_single_file(file_path, en_title, TRANSLATIONS[en_title]):
            print(f"✅ Successfully updated!")
        else:
            print(f"❌ Failed to update")
    else:
        print(f"No translation found for {en_title}")


if __name__ == "__main__":
    main()
