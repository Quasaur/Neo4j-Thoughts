#!/usr/bin/env python3
"""
Generate Cypher script to update edge name properties in Neo4j AuraDB.
This script reads the corrections log and generates the necessary MATCH/SET statements.
"""

import re
from pathlib import Path

def parse_correction_log(log_path):
    """Parse the corrections log to extract relationship name changes."""
    corrections = []
    
    with open(log_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all before/after pairs
    pattern = r'BEFORE: MERGE.*?name:\s*"([^"]+)".*?\n\s*AFTER:\s*MERGE.*?name:\s*"([^"]+)"'
    matches = re.findall(pattern, content, re.DOTALL)
    
    for old_name, new_name in matches:
        corrections.append({
            'old': old_name,
            'new': new_name
        })
    
    return corrections

def generate_neo4j_script(corrections):
    """Generate Cypher script to update relationship name properties."""
    
    # Group corrections by old -> new
    unique_corrections = {}
    for corr in corrections:
        key = (corr['old'], corr['new'])
        unique_corrections[key] = corr
    
    script_lines = []
    script_lines.append("// Neo4j AuraDB Edge Name Property Corrections")
    script_lines.append("// Generated automatically from edge_corrections_log.txt")
    script_lines.append("// Total corrections: " + str(len(unique_corrections)))
    script_lines.append("")
    script_lines.append("// NOTE: This script updates relationship `name` properties")
    script_lines.append("// to fix spacing errors (' >' -> '->') and add missing prefixes")
    script_lines.append("")
    script_lines.append("// Execute in Neo4j Browser or via Python driver")
    script_lines.append("")
    
    # Group by relationship type
    has_child_corrections = []
    has_thought_corrections = []
    has_quote_corrections = []
    has_passage_corrections = []
    
    for (old_name, new_name), corr in sorted(unique_corrections.items()):
        # Determine relationship type based on prefix
        if new_name.startswith('edge.') and not new_name.startswith(('t.edge.', 'q.edge.', 'p.edge.')):
            has_child_corrections.append(corr)
        elif new_name.startswith('t.edge.'):
            has_thought_corrections.append(corr)
        elif new_name.startswith('q.edge.'):
            has_quote_corrections.append(corr)
        elif new_name.startswith('p.edge.'):
            has_passage_corrections.append(corr)
    
    # Generate corrections for HAS_CHILD (TOPIC->TOPIC)
    if has_child_corrections:
        script_lines.append("// ============================================================")
        script_lines.append(f"// HAS_CHILD Relationship Corrections ({len(has_child_corrections)} total)")
        script_lines.append("// ============================================================")
        script_lines.append("")
        
        for corr in has_child_corrections:
            script_lines.append(f"// Fix: '{corr['old']}' -> '{corr['new']}'")
            script_lines.append(f"MATCH ()-[r:HAS_CHILD]->() WHERE r.name = \"{corr['old']}\"")
            script_lines.append(f"SET r.name = \"{corr['new']}\";")
            script_lines.append("")
    
    # Generate corrections for HAS_THOUGHT (TOPIC->THOUGHT)
    if has_thought_corrections:
        script_lines.append("// ============================================================")
        script_lines.append(f"// HAS_THOUGHT Relationship Corrections ({len(has_thought_corrections)} total)")
        script_lines.append("// ============================================================")
        script_lines.append("")
        
        for corr in has_thought_corrections:
            script_lines.append(f"// Fix: '{corr['old']}' -> '{corr['new']}'")
            script_lines.append(f"MATCH ()-[r:HAS_THOUGHT]->() WHERE r.name = \"{corr['old']}\"")
            script_lines.append(f"SET r.name = \"{corr['new']}\";")
            script_lines.append("")
    
    # Generate corrections for HAS_QUOTE (TOPIC->QUOTE)
    if has_quote_corrections:
        script_lines.append("// ============================================================")
        script_lines.append(f"// HAS_QUOTE Relationship Corrections ({len(has_quote_corrections)} total)")
        script_lines.append("// ============================================================")
        script_lines.append("")
        
        for corr in has_quote_corrections:
            script_lines.append(f"// Fix: '{corr['old']}' -> '{corr['new']}'")
            script_lines.append(f"MATCH ()-[r:HAS_QUOTE]->() WHERE r.name = \"{corr['old']}\"")
            script_lines.append(f"SET r.name = \"{corr['new']}\";")
            script_lines.append("")
    
    # Generate corrections for HAS_PASSAGE (TOPIC->PASSAGE)
    if has_passage_corrections:
        script_lines.append("// ============================================================")
        script_lines.append(f"// HAS_PASSAGE Relationship Corrections ({len(has_passage_corrections)} total)")
        script_lines.append("// ============================================================")
        script_lines.append("")
        
        for corr in has_passage_corrections:
            script_lines.append(f"// Fix: '{corr['old']}' -> '{corr['new']}'")
            script_lines.append(f"MATCH ()-[r:HAS_PASSAGE]->() WHERE r.name = \"{corr['old']}\"")
            script_lines.append(f"SET r.name = \"{corr['new']}\";")
            script_lines.append("")
    
    return '\n'.join(script_lines)

def main():
    base_dir = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts")
    log_path = base_dir / "CYPHER" / "CORRECTIONS" / "edge_corrections_log.txt"
    output_path = base_dir / "CYPHER" / "CORRECTIONS" / "neo4j_edge_corrections.cypher"
    
    print("=" * 80)
    print("GENERATING NEO4J CORRECTION SCRIPT")
    print("=" * 80)
    
    # Parse log
    print(f"\n📖 Reading corrections log: {log_path.name}")
    corrections = parse_correction_log(log_path)
    print(f"   Found {len(corrections)} total corrections")
    
    # Remove duplicates
    unique_corrections = {}
    for corr in corrections:
        key = (corr['old'], corr['new'])
        unique_corrections[key] = corr
    
    print(f"   Unique corrections: {len(unique_corrections)}")
    
    # Generate script
    print(f"\n🔧 Generating Cypher script...")
    script_content = generate_neo4j_script(corrections)
    
    # Write output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    print(f"   ✅ Script saved to: {output_path}")
    print(f"   📊 Total statements: {len(unique_corrections)}")
    print("\n" + "=" * 80)
    print("Next step: Review and execute the Cypher script in Neo4j AuraDB")
    print("=" * 80)

if __name__ == '__main__':
    main()
