#!/usr/bin/env python3.11
"""
Neo4j AuraDB Sync Script
- Part 1: PASSAGE Node Sync
- Part 2: QUOTE Node Cleanup
"""

import os
import re
from neo4j import GraphDatabase
from collections import defaultdict

# Configuration
URI = "neo4j+s://cf81ef03.databases.neo4j.io"
AUTH = ("neo4j", "BfLateGN_PldIlF7nd60M1m2v088QJelp9y9nuY9Y-s")
PASSAGES_DIR = "/Users/quasaur/Developer/Neo4j-Thoughts/content/PASSAGES"
QUOTES_DIR = "/Users/quasaur/Developer/Neo4j-Thoughts/content/QUOTES"

class Neo4jSync:
    def __init__(self):
        self.driver = GraphDatabase.driver(URI, auth=AUTH)
        self.report = {
            'passages_created': [],
            'passages_updated': [],
            'passages_in_sync': [],
            'quotes_deleted': [],
            'errors': []
        }
    
    def close(self):
        self.driver.close()
    
    def verify_connection(self):
        """Verify connection to AuraDB"""
        try:
            with self.driver.session() as session:
                result = session.run("RETURN 1 as test")
                record = result.single()
                print(f"✓ Connected to Neo4j AuraDB successfully")
                return True
        except Exception as e:
            print(f"✗ Failed to connect to Neo4j: {e}")
            return False
    
    def extract_cypher_from_markdown(self, filepath):
        """Extract Cypher block from markdown file"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find Cypher block (case insensitive)
        match = re.search(r'```[Cc]ypher\s*\n(.*?)```', content, re.DOTALL)
        if not match:
            return None
        
        return match.group(1).strip()
    
    def extract_name_from_cypher(self, cypher_content):
        """Extract the PASSAGE/QUOTE name from the CREATE statement"""
        # Look for name property in CREATE statement
        match = re.search(r'name:\s*"([^"]+)"', cypher_content)
        if match:
            return match.group(1)
        return None
    
    def extract_passage_properties_simple(self, cypher_content):
        """Extract PASSAGE properties using simpler regex approach"""
        # Find the PASSAGE node definition
        passage_match = re.search(
            r'CREATE\s*\(\s*(\w+)\s*:\s*PASSAGE\s*\{([^}]+)\}',
            cypher_content,
            re.DOTALL | re.IGNORECASE
        )
        
        if not passage_match:
            return None
        
        props_str = passage_match.group(2)
        
        # Parse simple properties
        props = {}
        
        # Extract name
        name_match = re.search(r'name:\s*"([^"]+)"', props_str)
        if name_match:
            props['name'] = name_match.group(1)
        
        # Extract parent
        parent_match = re.search(r'parent:\s*"([^"]+)"', props_str)
        if parent_match:
            props['parent'] = parent_match.group(1)
        
        # Extract alias
        alias_match = re.search(r'alias:\s*"([^"]+)"', props_str)
        if alias_match:
            props['alias'] = alias_match.group(1)
        
        # Extract source
        source_match = re.search(r'source:\s*"([^"]+)"', props_str)
        if source_match:
            props['source'] = source_match.group(1)
        
        # Extract sortedsource
        sortedsource_match = re.search(r'sortedsource:\s*"([^"]+)"', props_str)
        if sortedsource_match:
            props['sortedsource'] = sortedsource_match.group(1)
        
        # Extract biblelink
        biblelink_match = re.search(r'biblelink:\s*"([^"]+)"', props_str)
        if biblelink_match:
            props['biblelink'] = biblelink_match.group(1)
        
        # Extract level
        level_match = re.search(r'level:\s*(\d+)', props_str)
        if level_match:
            props['level'] = int(level_match.group(1))
        
        # Extract tags - handle array format
        tags_match = re.search(r'tags:\s*(\[[^\]]*\])', props_str, re.DOTALL)
        if tags_match:
            tags_str = tags_match.group(1)
            # Extract individual tag strings
            tags = re.findall(r'"([^"]*)"', tags_str)
            props['tags'] = tags
        
        return props
    
    def get_all_passages_from_files(self):
        """Get all PASSAGE data from markdown files"""
        passages = {}
        for filename in sorted(os.listdir(PASSAGES_DIR)):
            if filename.endswith('.md'):
                filepath = os.path.join(PASSAGES_DIR, filename)
                cypher = self.extract_cypher_from_markdown(filepath)
                if cypher:
                    props = self.extract_passage_properties_simple(cypher)
                    if props and 'name' in props:
                        passages[props['name']] = {
                            'props': props,
                            'cypher': cypher,
                            'filepath': filepath
                        }
        return passages
    
    def get_all_passages_from_db(self):
        """Get all PASSAGE nodes from Neo4j"""
        with self.driver.session() as session:
            result = session.run("""
                MATCH (p:PASSAGE)
                RETURN p.name as name, p
            """)
            passages = {}
            for record in result:
                name = record["name"]
                node = record["p"]
                passages[name] = dict(node)
            return passages
    
    def create_passage(self, name, passage_data):
        """Create a new PASSAGE node with its CONTENT and relationships"""
        cypher = passage_data['cypher']
        try:
            with self.driver.session() as session:
                session.run(cypher)
                self.report['passages_created'].append(name)
                print(f"  ✓ Created PASSAGE: {name}")
                return True
        except Exception as e:
            self.report['errors'].append(f"Error creating {name}: {e}")
            print(f"  ✗ Error creating PASSAGE {name}: {e}")
            return False
    
    def update_passage(self, name, file_props, db_props):
        """Update existing PASSAGE node if properties differ"""
        changes = []
        
        # Compare all properties
        for key, file_value in file_props.items():
            db_value = db_props.get(key)
            
            # Normalize for comparison
            if isinstance(file_value, list) and isinstance(db_value, list):
                if sorted(file_value) != sorted(db_value):
                    changes.append(f"{key}: {db_value} -> {file_value}")
            elif file_value != db_value:
                changes.append(f"{key}: {db_value} -> {file_value}")
        
        if not changes:
            return False
        
        # Perform update
        try:
            with self.driver.session() as session:
                # Update PASSAGE properties
                set_clause = ', '.join([f"p.{k} = ${k}" for k in file_props.keys()])
                query = f"""
                    MATCH (p:PASSAGE {{name: $name}})
                    SET {set_clause}
                """
                params = {'name': name, **file_props}
                session.run(query, params)
                
                self.report['passages_updated'].append({'name': name, 'changes': changes})
                print(f"  ✓ Updated PASSAGE: {name}")
                for change in changes:
                    print(f"    - {change}")
                return True
        except Exception as e:
            self.report['errors'].append(f"Error updating {name}: {e}")
            print(f"  ✗ Error updating PASSAGE {name}: {e}")
            return False
    
    def sync_passages(self):
        """Part 1: Sync PASSAGE nodes"""
        print("\n" + "="*60)
        print("PART 1: PASSAGE NODE SYNC")
        print("="*60)
        
        # Get data from files and DB
        print("\n📁 Loading PASSAGE data from markdown files...")
        file_passages = self.get_all_passages_from_files()
        print(f"   Found {len(file_passages)} PASSAGE files")
        
        print("\n🗄️  Loading PASSAGE data from Neo4j AuraDB...")
        db_passages = self.get_all_passages_from_db()
        print(f"   Found {len(db_passages)} PASSAGE nodes in DB")
        
        # Process each passage from files
        print("\n🔄 Syncing PASSAGE nodes...")
        for name, data in file_passages.items():
            if name not in db_passages:
                # Create new passage
                self.create_passage(name, data)
            else:
                # Check for updates
                updated = self.update_passage(name, data['props'], db_passages[name])
                if not updated:
                    self.report['passages_in_sync'].append(name)
        
        # Verify final count
        print("\n📊 Verifying final count...")
        final_count = len(self.get_all_passages_from_db())
        print(f"   Total PASSAGE nodes in AuraDB: {final_count}")
        if final_count == 28:
            print("   ✓ Count matches expected (28)")
        else:
            print(f"   ✗ Expected 28, got {final_count}")
        
        return final_count
    
    def get_quote_names_from_files(self):
        """Get QUOTE names from files"""
        names = set()
        for filename in os.listdir(QUOTES_DIR):
            if filename.startswith('quote-') and filename.endswith('.md'):
                # Convert filename to name format
                # quote-THE-CALL.md -> quote.THE CALL
                name_part = filename[6:-3]  # Remove 'quote-' and '.md'
                name = "quote." + name_part.replace('-', ' ')
                names.add(name)
        return names
    
    def get_all_quotes_from_db(self):
        """Get all QUOTE names from Neo4j"""
        with self.driver.session() as session:
            result = session.run("MATCH (q:QUOTE) RETURN q.name as name")
            return {record["name"] for record in result if record["name"]}
    
    def delete_orphaned_quote(self, name):
        """Delete an orphaned QUOTE node and its connections"""
        try:
            with self.driver.session() as session:
                # Delete QUOTE, its CONTENT, and all relationships
                session.run("""
                    MATCH (q:QUOTE {name: $name})
                    OPTIONAL MATCH (q)-[r1:HAS_CONTENT]->(c:CONTENT)
                    OPTIONAL MATCH (t:TOPIC)-[r2:HAS_QUOTE]->(q)
                    DELETE r1, r2, c, q
                """, {'name': name})
                self.report['quotes_deleted'].append(name)
                print(f"  ✓ Deleted orphaned QUOTE: {name}")
                return True
        except Exception as e:
            self.report['errors'].append(f"Error deleting quote {name}: {e}")
            print(f"  ✗ Error deleting QUOTE {name}: {e}")
            return False
    
    def cleanup_quotes(self):
        """Part 2: Clean up orphaned QUOTE nodes"""
        print("\n" + "="*60)
        print("PART 2: QUOTE NODE CLEANUP")
        print("="*60)
        
        # Get QUOTE names from files and DB
        print("\n📁 Loading QUOTE names from files...")
        file_quotes = self.get_quote_names_from_files()
        print(f"   Found {len(file_quotes)} QUOTE files")
        
        print("\n🗄️  Loading QUOTE names from Neo4j AuraDB...")
        db_quotes = self.get_all_quotes_from_db()
        print(f"   Found {len(db_quotes)} QUOTE nodes in DB")
        
        # Find orphaned quotes
        orphaned = db_quotes - file_quotes
        print(f"\n🗑️  Found {len(orphaned)} orphaned QUOTE nodes")
        
        if orphaned:
            print("\n🔄 Deleting orphaned QUOTE nodes...")
            for name in sorted(orphaned):
                self.delete_orphaned_quote(name)
        else:
            print("   No orphaned QUOTE nodes to delete")
        
        # Return final count
        final_count = len(self.get_all_quotes_from_db())
        print(f"\n   Final QUOTE count in AuraDB: {final_count}")
        return final_count
    
    def print_report(self):
        """Print final report"""
        print("\n" + "="*60)
        print("SYNC REPORT")
        print("="*60)
        
        print("\n📊 PASSAGE NODES:")
        print(f"   Created: {len(self.report['passages_created'])}")
        if self.report['passages_created']:
            for name in self.report['passages_created']:
                print(f"      - {name}")
        
        print(f"\n   Updated: {len(self.report['passages_updated'])}")
        if self.report['passages_updated']:
            for item in self.report['passages_updated']:
                print(f"      - {item['name']}")
                for change in item['changes']:
                    print(f"        * {change}")
        
        print(f"\n   In Sync: {len(self.report['passages_in_sync'])}")
        
        print("\n📊 QUOTE NODES:")
        print(f"   Deleted: {len(self.report['quotes_deleted'])}")
        if self.report['quotes_deleted']:
            for name in self.report['quotes_deleted']:
                print(f"      - {name}")
        
        if self.report['errors']:
            print("\n❌ ERRORS:")
            for error in self.report['errors']:
                print(f"   - {error}")
        
        print("\n" + "="*60)


def main():
    sync = Neo4jSync()
    
    try:
        # Verify connection
        if not sync.verify_connection():
            return
        
        # Part 1: Sync PASSAGE nodes
        passage_count = sync.sync_passages()
        
        # Part 2: Clean up orphaned QUOTE nodes
        quote_count = sync.cleanup_quotes()
        
        # Print final report
        sync.print_report()
        
        print(f"\n✅ Final Counts:")
        print(f"   PASSAGE nodes: {passage_count}")
        print(f"   QUOTE nodes: {quote_count}")
        
    finally:
        sync.close()


if __name__ == "__main__":
    main()
