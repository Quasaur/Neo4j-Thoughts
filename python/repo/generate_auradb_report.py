#!/usr/bin/env python3
"""
Compare content folder with Neo4j AuraDB and generate discrepancy report.
This script scans the content folder and compares it with the Neo4j AuraDB instance.
"""

import os
import re
import yaml
from datetime import datetime
from collections import defaultdict
from neo4j import GraphDatabase

# Configuration
CONTENT_ROOT = "/Users/quasaur/Developer/Neo4j-Thoughts/content"
URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

REPORT_PATH = "/Users/quasaur/Developer/Neo4j-Thoughts/dos/reports/neo4j_auradb_descripancies.md"


def extract_frontmatter(file_path):
    """Extract YAML frontmatter from a markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Match frontmatter between --- markers
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if match:
            frontmatter = yaml.safe_load(match.group(1))
            return frontmatter if isinstance(frontmatter, dict) else {}
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return {}


def scan_content_folder():
    """Scan content folder and categorize all nodes."""
    local_nodes = {
        'THOUGHT': {},
        'QUOTE': {},
        'PASSAGE': {},
        'TOPIC': {}
    }
    
    # Scan THOUGHTS
    thoughts_dir = os.path.join(CONTENT_ROOT, 'THOUGHTS')
    if os.path.exists(thoughts_dir):
        for filename in os.listdir(thoughts_dir):
            if filename.endswith('.md'):
                file_path = os.path.join(thoughts_dir, filename)
                fm = extract_frontmatter(file_path)
                if fm and 'name' in fm:
                    node_name = fm['name']
                    local_nodes['THOUGHT'][node_name] = {
                        'alias': fm.get('alias', ''),
                        'parent': fm.get('parent', ''),
                        'file': f'THOUGHTS/{filename}',
                        'neo4j': fm.get('neo4j', False)
                    }
    
    # Scan QUOTES
    quotes_dir = os.path.join(CONTENT_ROOT, 'QUOTES')
    if os.path.exists(quotes_dir):
        for root, _, files in os.walk(quotes_dir):
            for filename in files:
                if filename.endswith('.md'):
                    file_path = os.path.join(root, filename)
                    rel_path = os.path.relpath(file_path, CONTENT_ROOT)
                    fm = extract_frontmatter(file_path)
                    if fm and 'name' in fm:
                        node_name = fm['name']
                        local_nodes['QUOTE'][node_name] = {
                            'alias': fm.get('alias', ''),
                            'parent': fm.get('parent', ''),
                            'file': rel_path,
                            'neo4j': fm.get('neo4j', False)
                        }
    
    # Scan PASSAGES
    passages_dir = os.path.join(CONTENT_ROOT, 'PASSAGES')
    if os.path.exists(passages_dir):
        for root, _, files in os.walk(passages_dir):
            for filename in files:
                if filename.endswith('.md'):
                    file_path = os.path.join(root, filename)
                    rel_path = os.path.relpath(file_path, CONTENT_ROOT)
                    fm = extract_frontmatter(file_path)
                    if fm and 'name' in fm:
                        node_name = fm['name']
                        local_nodes['PASSAGE'][node_name] = {
                            'alias': fm.get('alias', ''),
                            'parent': fm.get('parent', ''),
                            'file': rel_path,
                            'neo4j': fm.get('neo4j', False)
                        }
    
    # Scan TOPICS
    topics_dir = os.path.join(CONTENT_ROOT, 'TOPICS')
    if os.path.exists(topics_dir):
        for filename in os.listdir(topics_dir):
            if filename.endswith('.md'):
                file_path = os.path.join(topics_dir, filename)
                fm = extract_frontmatter(file_path)
                if fm and 'name' in fm:
                    node_name = fm['name']
                    local_nodes['TOPIC'][node_name] = {
                        'alias': fm.get('alias', ''),
                        'parent': fm.get('parent', ''),
                        'file': f'TOPICS/{filename}',
                        'neo4j': fm.get('neo4j', False)
                    }
    
    return local_nodes


def query_auradb():
    """Query Neo4j AuraDB for all nodes."""
    auradb_nodes = {
        'THOUGHT': {},
        'QUOTE': {},
        'PASSAGE': {},
        'TOPIC': {}
    }
    
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    try:
        with driver.session() as session:
            # Query THOUGHT nodes
            result = session.run("""
                MATCH (t:THOUGHT)
                RETURN t.name as name, t.alias as alias, t.parent as parent
            """)
            for record in result:
                auradb_nodes['THOUGHT'][record['name']] = {
                    'alias': record['alias'],
                    'parent': record['parent']
                }
            
            # Query QUOTE nodes
            result = session.run("""
                MATCH (q:QUOTE)
                RETURN q.name as name, q.alias as alias, q.parent as parent
            """)
            for record in result:
                auradb_nodes['QUOTE'][record['name']] = {
                    'alias': record['alias'],
                    'parent': record['parent']
                }
            
            # Query PASSAGE nodes
            result = session.run("""
                MATCH (p:PASSAGE)
                RETURN p.name as name, p.alias as alias, p.parent as parent
            """)
            for record in result:
                auradb_nodes['PASSAGE'][record['name']] = {
                    'alias': record['alias'],
                    'parent': record['parent']
                }
            
            # Query TOPIC nodes
            result = session.run("""
                MATCH (t:TOPIC)
                RETURN t.name as name, t.alias as alias, t.parent as parent
            """)
            for record in result:
                auradb_nodes['TOPIC'][record['name']] = {
                    'alias': record['alias'],
                    'parent': record['parent']
                }
                
    finally:
        driver.close()
    
    return auradb_nodes


def compare_nodes(local_nodes, auradb_nodes):
    """Compare local content with AuraDB and find discrepancies."""
    discrepancies = {
        'missing_in_auradb': defaultdict(list),  # In local but not in AuraDB
        'missing_in_local': defaultdict(list),   # In AuraDB but not in local
        'mismatched': defaultdict(list),         # In both but with differences
        'in_sync': defaultdict(list)             # In both and matching
    }
    
    for node_type in ['THOUGHT', 'QUOTE', 'PASSAGE', 'TOPIC']:
        local = local_nodes[node_type]
        auradb = auradb_nodes[node_type]
        
        # Find missing in AuraDB (in local but not in AuraDB)
        for name, data in local.items():
            if name not in auradb:
                discrepancies['missing_in_auradb'][node_type].append({
                    'name': name,
                    'local_data': data
                })
            else:
                # Check for mismatches
                auradb_data = auradb[name]
                mismatches = []
                
                if data.get('alias') != auradb_data.get('alias'):
                    mismatches.append(f"alias: local='{data.get('alias')}' vs auradb='{auradb_data.get('alias')}'")
                if data.get('parent') != auradb_data.get('parent'):
                    mismatches.append(f"parent: local='{data.get('parent')}' vs auradb='{auradb_data.get('parent')}'")
                
                if mismatches:
                    discrepancies['mismatched'][node_type].append({
                        'name': name,
                        'mismatches': mismatches,
                        'local_data': data,
                        'auradb_data': auradb_data
                    })
                else:
                    discrepancies['in_sync'][node_type].append({
                        'name': name,
                        'data': data
                    })
        
        # Find missing in local (in AuraDB but not in local)
        for name, data in auradb.items():
            if name not in local:
                discrepancies['missing_in_local'][node_type].append({
                    'name': name,
                    'auradb_data': data
                })
    
    return discrepancies


def generate_report(discrepancies, local_nodes, auradb_nodes):
    """Generate the markdown report."""
    report_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    report = f"""# Neo4j AuraDB vs Content Folder Discrepancy Report

**Generated:** {report_date}

## Executive Summary

| Node Type | Local Files | AuraDB Nodes | Missing in AuraDB | Missing in Local | Mismatched | In Sync |
|-----------|-------------|--------------|-------------------|------------------|------------|----------|
"""
    
    for node_type in ['THOUGHT', 'QUOTE', 'PASSAGE', 'TOPIC']:
        local_count = len(local_nodes[node_type])
        auradb_count = len(auradb_nodes[node_type])
        missing_auradb = len(discrepancies['missing_in_auradb'][node_type])
        missing_local = len(discrepancies['missing_in_local'][node_type])
        mismatched = len(discrepancies['mismatched'][node_type])
        in_sync = len(discrepancies['in_sync'][node_type])
        
        report += f"| {node_type} | {local_count} | {auradb_count} | {missing_auradb} | {missing_local} | {mismatched} | {in_sync} |\n"
    
    report += """
---

## 1. Nodes Missing in AuraDB (Present in Local, Missing in AuraDB)

These nodes exist in the content folder but are not present in the Neo4j AuraDB instance.

"""
    
    for node_type in ['THOUGHT', 'QUOTE', 'PASSAGE', 'TOPIC']:
        items = discrepancies['missing_in_auradb'][node_type]
        if items:
            report += f"### {node_type} Nodes Missing in AuraDB ({len(items)} total)\n\n"
            report += "| Name | Alias | Parent | File | neo4j flag |\n"
            report += "|------|-------|--------|------|------------|\n"
            for item in items:
                data = item['local_data']
                report += f"| `{item['name']}` | {data.get('alias', '')} | {data.get('parent', '')} | {data.get('file', '')} | {data.get('neo4j', False)} |\n"
            report += "\n"
    
    if not any(discrepancies['missing_in_auradb'].values()):
        report += "**No nodes are missing in AuraDB.** All local content folder nodes exist in the database.\n\n"
    
    report += """---

## 2. Nodes Missing in Local Content (Present in AuraDB, Missing in Local)

These nodes exist in Neo4j AuraDB but are not present in the content folder.

"""
    
    for node_type in ['THOUGHT', 'QUOTE', 'PASSAGE', 'TOPIC']:
        items = discrepancies['missing_in_local'][node_type]
        if items:
            report += f"### {node_type} Nodes Missing in Local ({len(items)} total)\n\n"
            report += "| Name | Alias | Parent |\n"
            report += "|------|-------|--------|\n"
            for item in items:
                data = item['auradb_data']
                report += f"| `{item['name']}` | {data.get('alias', '')} | {data.get('parent', '')} |\n"
            report += "\n"
    
    if not any(discrepancies['missing_in_local'].values()):
        report += "**No nodes are missing in local content.** All AuraDB nodes exist in the content folder.\n\n"
    
    report += """---

## 3. Mismatched Nodes (Present in Both, But with Differences)

These nodes exist in both locations but have differing properties.

"""
    
    for node_type in ['THOUGHT', 'QUOTE', 'PASSAGE', 'TOPIC']:
        items = discrepancies['mismatched'][node_type]
        if items:
            report += f"### {node_type} Mismatched Nodes ({len(items)} total)\n\n"
            for item in items:
                report += f"**`{item['name']}`**\n"
                report += f"- File: {item['local_data'].get('file', 'N/A')}\n"
                for mismatch in item['mismatches']:
                    report += f"- {mismatch}\n"
                report += "\n"
    
    if not any(discrepancies['mismatched'].values()):
        report += "**No mismatched nodes found.** All nodes that exist in both locations have matching properties.\n\n"
    
    report += """---

## 4. Detailed Node Lists

### 4.1 THOUGHT Nodes
"""
    
    report += f"\n**Local THOUGHT nodes:** {len(local_nodes['THOUGHT'])}\n"
    report += f"**AuraDB THOUGHT nodes:** {len(auradb_nodes['THOUGHT'])}\n\n"
    
    report += "### 4.2 QUOTE Nodes\n"
    report += f"\n**Local QUOTE nodes:** {len(local_nodes['QUOTE'])}\n"
    report += f"**AuraDB QUOTE nodes:** {len(auradb_nodes['QUOTE'])}\n\n"
    
    report += "### 4.3 PASSAGE Nodes\n"
    report += f"\n**Local PASSAGE nodes:** {len(local_nodes['PASSAGE'])}\n"
    report += f"**AuraDB PASSAGE nodes:** {len(auradb_nodes['PASSAGE'])}\n\n"
    
    report += "### 4.4 TOPIC Nodes\n"
    report += f"\n**Local TOPIC nodes:** {len(local_nodes['TOPIC'])}\n"
    report += f"**AuraDB TOPIC nodes:** {len(auradb_nodes['TOPIC'])}\n\n"
    
    report += """---

## Recommendations

Based on the discrepancy analysis:

"""
    
    total_missing_auradb = sum(len(v) for v in discrepancies['missing_in_auradb'].values())
    total_missing_local = sum(len(v) for v in discrepancies['missing_in_local'].values())
    total_mismatched = sum(len(v) for v in discrepancies['mismatched'].values())
    
    if total_missing_auradb > 0:
        report += f"1. **Sync to AuraDB:** {total_missing_auradb} node(s) need to be inserted into Neo4j AuraDB.\n"
    
    if total_missing_local > 0:
        report += f"2. **Create Local Files:** {total_missing_local} node(s) exist only in AuraDB and need local markdown files.\n"
    
    if total_mismatched > 0:
        report += f"3. **Resolve Mismatches:** {total_mismatched} node(s) have property differences that need reconciliation.\n"
    
    if total_missing_auradb == 0 and total_missing_local == 0 and total_mismatched == 0:
        report += "**All nodes are in sync!** No action required.\n"
    
    report += "\n---\n\n*Report generated by generate_auradb_report.py*\n"
    
    return report


def main():
    """Main function to run the comparison and generate report."""
    print("Scanning content folder...")
    local_nodes = scan_content_folder()
    print(f"  Found {len(local_nodes['THOUGHT'])} THOUGHTS")
    print(f"  Found {len(local_nodes['QUOTE'])} QUOTES")
    print(f"  Found {len(local_nodes['PASSAGE'])} PASSAGES")
    print(f"  Found {len(local_nodes['TOPIC'])} TOPICS")
    
    print("\nQuerying Neo4j AuraDB...")
    auradb_nodes = query_auradb()
    print(f"  Found {len(auradb_nodes['THOUGHT'])} THOUGHTS")
    print(f"  Found {len(auradb_nodes['QUOTE'])} QUOTES")
    print(f"  Found {len(auradb_nodes['PASSAGE'])} PASSAGES")
    print(f"  Found {len(auradb_nodes['TOPIC'])} TOPICS")
    
    print("\nComparing nodes...")
    discrepancies = compare_nodes(local_nodes, auradb_nodes)
    
    print("\nGenerating report...")
    report = generate_report(discrepancies, local_nodes, auradb_nodes)
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(REPORT_PATH), exist_ok=True)
    
    # Write report
    with open(REPORT_PATH, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n✅ Report saved to: {REPORT_PATH}")
    
    # Print summary
    total_missing_auradb = sum(len(v) for v in discrepancies['missing_in_auradb'].values())
    total_missing_local = sum(len(v) for v in discrepancies['missing_in_local'].values())
    total_mismatched = sum(len(v) for v in discrepancies['mismatched'].values())
    total_in_sync = sum(len(v) for v in discrepancies['in_sync'].values())
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Missing in AuraDB:  {total_missing_auradb}")
    print(f"Missing in Local:   {total_missing_local}")
    print(f"Mismatched:         {total_mismatched}")
    print(f"In Sync:            {total_in_sync}")
    print("=" * 60)


if __name__ == "__main__":
    main()
