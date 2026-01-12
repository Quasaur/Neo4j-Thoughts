#!/usr/bin/env python3
"""
Batch translate markdown files using Claude AI for proper translations.
Process in small batches to ensure accurate, contextual translations.
"""

import os
import re
from pathlib import Path
import json

# Files that already have complete translations (skip these)
COMPLETE_FILES = {
    "ACCOUNTABILITY.md", "AGREEING-WITH-OPPRESSOR.md", "ALIGNING-THROUGH-PRAYER.md",
    "ALL-TRUTH-GODS.md", "ALONZO-CHURCH-FAITH.md", "AMERICA-ACCOUNTABLE-FREEDOMS.md",
    "AMERICAN-POVERTY-LINE.md", "ANGER-AND-PAIN.md", "ANGER-AS-CONTAGION.md",
    "APOCALYPSE-BETTER-WORLD.md", "APOSTLES-AS-VISION.md", "ARROGANCE-VS-DIGNITY.md",
    "ASK-GOD-PERFECTION.md", "ATROCITIES-OF-RELIGION.md", "ATTENTIONS-DESIRE.md",
    "AWESOME-GOD.md", "DEFINITION-OF-SIN.md", "DUST-AND-DIVINE.md",
    "FRIENDS-AND-ENEMIES.md", "GOD-AND-EVIL.md", "JESUS-IN-DISGUISE.md",
    "LIFE-AS-DREAM.md", "SUBMITTING-OUR-PLANS.md", "ABORTION-AND-GOLDEN-RULE.md",
    "ACCURATE-THEOLOGY.md", "ALL-OF-GOD-JESUS.md", "ALL-THINGS-FOR-HIM.md"
}

CYPHER_DIR = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/cypher")

def get_files_to_process():
    """Get list of files that need translation."""
    all_files = list(CYPHER_DIR.glob("*.md"))
    to_process = [f for f in all_files if f.name not in COMPLETE_FILES]
    return sorted(to_process)

def extract_english_content(file_path):
    """Extract en_title and en_content from file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    en_title_match = re.search(r'en_title:\s*"([^"]*)"', content)
    en_content_match = re.search(r'en_content:\s*"([^"]*)"', content)
    
    if en_title_match and en_content_match:
        return {
            'en_title': en_title_match.group(1),
            'en_content': en_content_match.group(1),
            'full_content': content
        }
    return None

def main():
    """Main function to display files needing translation."""
    files = get_files_to_process()
    
    print("="*70)
    print(f"TRANSLATION BATCH PROCESSING")
    print("="*70)
    print(f"\nTotal files to translate: {len(files)}")
    print(f"Files already complete: {len(COMPLETE_FILES)}")
    print(f"\nFirst 20 files to process:")
    print("-"*70)
    
    for i, file_path in enumerate(files[:20], 1):
        data = extract_english_content(file_path)
        if data:
            print(f"\n{i}. {file_path.name}")
            print(f"   Title: {data['en_title']}")
            print(f"   Content: {data['en_content'][:80]}...")
        else:
            print(f"\n{i}. {file_path.name} - ERROR: Could not extract content")
    
    print("\n" + "="*70)
    print(f"Ready to process {len(files)} files in total.")
    print("="*70)

if __name__ == "__main__":
    main()
