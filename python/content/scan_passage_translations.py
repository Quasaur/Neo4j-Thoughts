#!/usr/bin/env python3
"""
Scan all PASSAGE files to identify missing translations.
Expected translations: en, es, fr, hi, zh
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Set

def extract_content_fields(cypher_content: str) -> Set[str]:
    """Extract all content field names from Cypher CREATE CONTENT block."""
    fields = set()
    
    # Pattern to match field names like en_title, es_content, etc.
    pattern = r'\b(en|es|fr|hi|zh)_(title|content)\b'
    matches = re.findall(pattern, cypher_content)
    
    for lang, field_type in matches:
        fields.add(f"{lang}_{field_type}")
    
    return fields

def scan_passage_file(file_path: Path) -> Dict:
    """Scan a single PASSAGE file for translation completeness."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract YAML frontmatter
    yaml_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not yaml_match:
        return None
    
    yaml_content = yaml_match.group(1)
    
    # Extract name from YAML
    name_match = re.search(r'^name:\s*["\']?(.+?)["\']?$', yaml_content, re.MULTILINE)
    passage_name = name_match.group(1) if name_match else "UNKNOWN"
    
    # Extract Cypher block
    cypher_match = re.search(r'```Cypher\n(.*?)\n```', content, re.DOTALL | re.IGNORECASE)
    if not cypher_match:
        return {
            'file': str(file_path),
            'name': passage_name,
            'error': 'No Cypher block found'
        }
    
    cypher_content = cypher_match.group(1)
    
    # Find all translation fields
    found_fields = extract_content_fields(cypher_content)
    
    # Expected fields for complete translations
    expected_langs = {'en', 'es', 'fr', 'hi', 'zh'}
    expected_fields = {f"{lang}_{field}" for lang in expected_langs for field in ['title', 'content']}
    
    missing_fields = expected_fields - found_fields
    
    # Determine which languages are missing
    missing_langs = set()
    for field in missing_fields:
        lang = field.split('_')[0]
        missing_langs.add(lang)
    
    return {
        'file': str(file_path),
        'name': passage_name,
        'found_fields': sorted(found_fields),
        'missing_fields': sorted(missing_fields),
        'missing_languages': sorted(missing_langs),
        'is_complete': len(missing_fields) == 0
    }

def main():
    """Main function to scan all PASSAGE files."""
    passages_dir = Path('content/PASSAGES')
    
    if not passages_dir.exists():
        print(f"Error: {passages_dir} does not exist")
        return
    
    # Find all .md files
    passage_files = list(passages_dir.rglob('*.md'))
    
    print(f"Found {len(passage_files)} PASSAGE files\n")
    print("=" * 80)
    
    results = []
    incomplete_count = 0
    
    for file_path in sorted(passage_files):
        result = scan_passage_file(file_path)
        if result:
            results.append(result)
            
            if not result.get('is_complete', False):
                incomplete_count += 1
                print(f"\n❌ INCOMPLETE: {result['name']}")
                print(f"   File: {result['file']}")
                if 'error' in result:
                    print(f"   Error: {result['error']}")
                else:
                    print(f"   Missing languages: {', '.join(result['missing_languages'])}")
                    print(f"   Missing fields: {', '.join(result['missing_fields'])}")
    
    print("\n" + "=" * 80)
    print(f"\nSUMMARY:")
    print(f"  Total PASSAGE files: {len(results)}")
    print(f"  Complete: {len(results) - incomplete_count}")
    print(f"  Incomplete: {incomplete_count}")
    
    if incomplete_count > 0:
        print(f"\n⚠️  {incomplete_count} PASSAGE file(s) are missing translations!")
        
        # Group by missing languages
        lang_summary = {}
        for result in results:
            if not result.get('is_complete', False) and 'missing_languages' in result:
                for lang in result['missing_languages']:
                    if lang not in lang_summary:
                        lang_summary[lang] = []
                    lang_summary[lang].append(result['name'])
        
        print("\nMissing translations by language:")
        for lang in sorted(lang_summary.keys()):
            print(f"  {lang}: {len(lang_summary[lang])} files")
            for name in lang_summary[lang]:
                print(f"    - {name}")
    else:
        print("\n✅ All PASSAGE files have complete translations!")
    
    # Save detailed report
    report_path = Path('ANALYSIS/passage_translation_report.txt')
    report_path.parent.mkdir(exist_ok=True)
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("PASSAGE Translation Completeness Report\n")
        f.write("=" * 80 + "\n\n")
        
        for result in results:
            f.write(f"File: {result['file']}\n")
            f.write(f"Name: {result['name']}\n")
            
            if 'error' in result:
                f.write(f"Error: {result['error']}\n")
            else:
                f.write(f"Complete: {'Yes' if result['is_complete'] else 'No'}\n")
                if not result['is_complete']:
                    f.write(f"Missing languages: {', '.join(result['missing_languages'])}\n")
                    f.write(f"Missing fields: {', '.join(result['missing_fields'])}\n")
            
            f.write("\n" + "-" * 80 + "\n\n")
        
        f.write(f"\nSUMMARY:\n")
        f.write(f"Total: {len(results)}\n")
        f.write(f"Complete: {len(results) - incomplete_count}\n")
        f.write(f"Incomplete: {incomplete_count}\n")
    
    print(f"\n📄 Detailed report saved to: {report_path}")

if __name__ == '__main__':
    main()
