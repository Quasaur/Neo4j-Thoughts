#!/usr/bin/env python3
"""
Insert THOUGHT nodes with ptopic data into Neo4j AuraDB.

This script processes the 43 validated files from Book_of_Tweets/THOUGHTS/ 
that have ptopic values set.

Validates each file before insertion:
- Checks parent/ptopic consistency
- Ensures Cypher block parent matches YAML parent
- Prevents insertion if mismatches found

After successful insertion, updates neo4j: false to neo4j: true
"""

import os
import re
import sys
from pathlib import Path
from neo4j import GraphDatabase

# AuraDB connection credentials
URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")

# Base path for thought files
BASE_PATH = Path("/Users/quasaur/Developer/WISDOM/Neo4j-Thoughts/Book_of_Tweets/THOUGHTS")

# 43 validated files with ptopic data
VALIDATED_FILES = [
    "ARGUING-WITH-CREATOR.md",
    "ARROGANCE-VS-DIGNITY.md",
    "BAG-OF-CHEMICALS-DUPED.md",
    "DEVIL-THE-ACCUSER.md",
    "DIVINE-MERCY-HOPE.md",
    "BUNYANS-MASTERPIECE.md",
    "CHRISTS-AMNESTY.md",
    "COST-OF-HEAVEN.md",
    "DAILY-DIVINE-LOVE.md",
    "DEFINE-GRACE.md",
    "DONT-KNOW-DOING.md",
    "FACING-TRUTH-LOVE.md",
    "FAILURE-TO-SUCCESS.md",
    "FORGIVE-AND-SANCTIFY.md",
    "FORGIVING-OTHERS-PROBLEM.md",
    "FORGIVING-THE-FUTURE.md",
    "GLORY-THROUGH-LOSERS.md",
    "GOD-SAVES-BREAKING.md",
    "GODS-FORGETFULNESS.md",
    "GRACE-STRONGER-SIN.md",
    "GRACE-TO-HUMBLE.md",
    "GRACE-VS-MERIT.md",
    "GRACE-VS-SATAN.md",
    "HEAVEN-BY-GRACE.md",
    "HEAVEN-WITHIN-SALVATION.md",
    "HUMANITY-TOO-FAR-GONE.md",
    "HUMANITYS-FINAL-VIRTUE.md",
    "LEGALITY-OF-ATONEMENT.md",
    "LIMITS-OF-FORGIVENESS.md",
    "LIVING-IN-CHRISTS-RIGHTEOUSNESS.md",
    "LOVE-CHANGES-SINNER.md",
    "LOVE-HATER-GRACE.md",
    "LOVE-SEVERING-SIN.md",
    "MIRACLE-OF-SALVATION.md",
    "PENALTY-VS-SIN.md",
    "RECREATING-INTENT.md",
    "SALVATION-FOR-ANYBODY.md",
    "SIN-MAKES-IDIOTS.md",
    "SPITTING-ON-THE-CROSS.md",
    "TREATED-AS-FAMILY.md",
    "UNFORGIVABLE-SIN.md",
    "UNIVERSAL-MERCY-REQUIREMENT.md",
    "WORK-TO-BE-SAVED.md",
]

# Files excluded due to parent mismatches (none currently)
EXCLUDED_FILES = []


def extract_frontmatter(content: str) -> str:
    """Extract YAML frontmatter from markdown content."""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[1].strip()
    return None


def parse_yaml_value(line: str) -> str:
    """Parse a YAML value, removing quotes if present."""
    line = line.strip()
    # Handle quoted values
    if (line.startswith('"') and line.endswith('"')) or \
       (line.startswith("'") and line.endswith("'")):
        return line[1:-1]
    return line


def extract_yaml_parent(frontmatter: str) -> str:
    """Extract the parent value from YAML frontmatter."""
    for line in frontmatter.split('\n'):
        if line.strip().startswith('parent:'):
            value = line.split(':', 1)[1].strip()
            return parse_yaml_value(value)
    return None


def extract_cypher_parent(content: str) -> str:
    """Extract the parent topic from the Cypher MATCH statement."""
    # Look for: MATCH (parent:TOPIC {name: "topic.XXX"})
    match = re.search(r'MATCH\s*\(parent:\s*\w+\s*\{\s*name:\s*"([^"]+)"\s*\}\)', content, re.IGNORECASE)
    if match:
        return match.group(1)
    return None


def clean_cypher_syntax(cypher: str) -> str:
    """Fix common Cypher syntax errors in the generated queries."""
    # Fix 1: Remove quotes around property keys: { "name": ... } -> { name: ... }
    cypher = re.sub(r'\{\s*"(\w+)":', r'{ \1:', cypher)
    
    # Fix 2: Add missing comma before zh_title if hi_content is followed by zh_title without comma
    # Pattern: "hi_content": "..." zh_title: -> "hi_content": "...", zh_title:
    cypher = re.sub(r'(hi_content:\s*"[^"]*")\s+(zh_title:)', r'\1, \2', cypher)
    
    return cypher


def convert_create_to_merge(cypher: str) -> str:
    """Convert CREATE statements to MERGE for idempotent insertion."""
    # Convert CREATE (n:Label { ... }) to MERGE (n:Label { ... })
    # This handles the pattern: CREATE (var:TYPE { props });
    cypher = re.sub(
        r'CREATE\s*\((\w+):(\w+)\s*\{',
        r'MERGE (\1:\2 {',
        cypher,
        flags=re.IGNORECASE
    )
    return cypher


def extract_cypher_block(content: str) -> str:
    """Extract and clean the Cypher code block from markdown."""
    match = re.search(r'```Cypher\s*(.*?)\s*```', content, re.DOTALL | re.IGNORECASE)
    if match:
        cypher = match.group(1).strip()
        # Remove comment lines
        lines = [line for line in cypher.split('\n') if not line.strip().startswith('//')]
        cypher = '\n'.join(lines).strip()
        # Clean up syntax errors
        cypher = clean_cypher_syntax(cypher)
        # Convert CREATE to MERGE for idempotent insertion
        cypher = convert_create_to_merge(cypher)
        return cypher
    return None


def split_cypher_statements(cypher: str) -> list:
    """Split Cypher block into individual statements."""
    # Split on semicolons followed by newline or end
    statements = []
    current = []
    
    for line in cypher.split('\n'):
        line = line.strip()
        if not line:
            continue
        current.append(line)
        if line.endswith(';'):
            stmt = ' '.join(current).strip()
            if stmt:
                statements.append(stmt)
            current = []
    
    # Handle any remaining content
    if current:
        stmt = ' '.join(current).strip()
        if stmt:
            statements.append(stmt)
    
    return statements


def validate_file(file_path: Path) -> tuple[bool, str]:
    """
    Validate a file for parent consistency.
    Returns (is_valid, error_message)
    """
    content = file_path.read_text(encoding='utf-8')
    
    # Extract frontmatter and get YAML parent
    frontmatter = extract_frontmatter(content)
    if not frontmatter:
        return False, "No frontmatter found"
    
    yaml_parent = extract_yaml_parent(frontmatter)
    if not yaml_parent:
        return False, "No parent found in frontmatter"
    
    # Extract Cypher parent
    cypher_parent = extract_cypher_parent(content)
    if not cypher_parent:
        return False, "No parent found in Cypher block"
    
    # Compare parents
    if yaml_parent != cypher_parent:
        return False, f"Parent mismatch: YAML='{yaml_parent}' vs Cypher='{cypher_parent}'"
    
    # Check Cypher block exists
    cypher = extract_cypher_block(content)
    if not cypher:
        return False, "No Cypher block found"
    
    return True, None


def execute_cypher_statements(statements: list, filename: str) -> tuple[bool, str]:
    """
    Execute Cypher statements against AuraDB.
    Returns (success, error_message)
    """
    driver = GraphDatabase.driver(URI, auth=AUTH)
    
    try:
        with driver.session() as session:
            for i, stmt in enumerate(statements):
                if not stmt.strip():
                    continue
                try:
                    session.run(stmt)
                except Exception as e:
                    return False, f"Statement {i+1} failed: {str(e)}"
        return True, None
    except Exception as e:
        return False, f"Database connection error: {str(e)}"
    finally:
        driver.close()


def update_neo4j_status(file_path: Path, status: bool) -> bool:
    """Update the neo4j property in the file's frontmatter."""
    try:
        content = file_path.read_text(encoding='utf-8')
        # Replace neo4j: false with neo4j: true (or neo4j: <status>)
        updated = re.sub(r'neo4j:\s*false', f'neo4j: {str(status).lower()}', content)
        updated = re.sub(r'neo4j:\s*true', f'neo4j: {str(status).lower()}', updated)
        file_path.write_text(updated, encoding='utf-8')
        return True
    except Exception as e:
        print(f"  ⚠️  Warning: Could not update neo4j status: {e}")
        return False


def main():
    """Main execution function."""
    print("=" * 70)
    print("Neo4j AuraDB Insertion Script for ptopic THOUGHTS")
    print("=" * 70)
    print(f"\nProcessing {len(VALIDATED_FILES)} validated files")
    if EXCLUDED_FILES:
        print(f"Excluded {len(EXCLUDED_FILES)} files with errors:\n  - " + "\n  - ".join(EXCLUDED_FILES))
    print()
    
    # Statistics
    stats = {
        'validated': 0,
        'passed': 0,
        'failed_validation': 0,
        'inserted': 0,
        'failed_insertion': 0,
    }
    
    failed_files = []
    
    for i, filename in enumerate(VALIDATED_FILES, 1):
        file_path = BASE_PATH / filename
        print(f"[{i}/{len(VALIDATED_FILES)}] Processing: {filename}")
        
        # Validate file
        stats['validated'] += 1
        is_valid, error = validate_file(file_path)
        
        if not is_valid:
            stats['failed_validation'] += 1
            print(f"  ❌ VALIDATION FAILED: {error}")
            failed_files.append((filename, f"Validation: {error}"))
            continue
        
        stats['passed'] += 1
        print(f"  ✅ Validation passed")
        
        # Extract and execute Cypher
        content = file_path.read_text(encoding='utf-8')
        cypher = extract_cypher_block(content)
        statements = split_cypher_statements(cypher)
        
        print(f"  📊 Executing {len(statements)} Cypher statements...")
        success, error = execute_cypher_statements(statements, filename)
        
        if success:
            stats['inserted'] += 1
            print(f"  ✅ Inserted successfully")
            # Update neo4j status
            if update_neo4j_status(file_path, True):
                print(f"  📝 Updated neo4j status to true")
        else:
            stats['failed_insertion'] += 1
            print(f"  ❌ INSERTION FAILED: {error}")
            failed_files.append((filename, f"Insertion: {error}"))
    
    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total files validated:     {stats['validated']}")
    print(f"Passed validation:         {stats['passed']}")
    print(f"Failed validation:         {stats['failed_validation']}")
    print(f"Successfully inserted:     {stats['inserted']}")
    print(f"Failed insertion:          {stats['failed_insertion']}")
    
    if failed_files:
        print("\n" + "-" * 70)
        print("FAILED FILES:")
        print("-" * 70)
        for filename, error in failed_files:
            print(f"  {filename}: {error}")
    
    print("\n" + "=" * 70)
    
    return 0 if stats['failed_validation'] == 0 and stats['failed_insertion'] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
