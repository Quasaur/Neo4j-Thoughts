In Neo4j what is the format of a script file written in Cypher?

In Neo4j, a script file written in Cypher is typically a plain text file containing a sequence of Cypher statements. There isn't a strict, single "format" beyond that, but there are common conventions and important considerations:
Key Characteristics and Conventions:
 * File Extension: The most common and recommended file extension for Cypher scripts is .cypher. However, you might also see .cql (for Cypher Query Language) or simply .txt.
 * Plain Text: The file should be a plain text file encoded in UTF-8.
 * One Statement Per Line (Often, but not strictly required): While Cypher statements can span multiple lines, it's a common practice to put each complete statement on its own line for readability.
 * Semicolon (;) as Statement Terminator: Each Cypher statement must be terminated by a semicolon (;). This is crucial for Neo4j to parse and execute multiple statements within a single script.
 * Comments:
   * Single-line comments: Start with // (double forward slash). Everything from // to the end of the line is a comment.
   * Multi-line comments: Enclosed between /* and */. These can span multiple lines.
 * Whitespace: Whitespace (spaces, tabs, newlines) is generally ignored by Cypher, except within string literals. You can use it freely to format your queries for readability.
 * Order of Execution: Statements in the script are executed sequentially from top to bottom.
 * Transactions (Implicit and Explicit):
   * When you run a Cypher script, Neo4j will often execute it within an implicit transaction. If any statement fails, the entire transaction might be rolled back (depending on how you execute the script and the Neo4j version/configuration).
   * For more complex operations, especially those involving multiple writes that need to be atomic, you might explicitly define transactions within your script using BEGIN, COMMIT, and ROLLBACK (though these are less common in simple scripts and more often handled by drivers).
Example of a Cypher Script File (my_script.cypher):
// This is a single-line comment

// Create some nodes
CREATE (p1:Person {name: 'Alice', age: 30});
CREATE (p2:Person {name: 'Bob', age: 25});
CREATE (p3:Person {name: 'Charlie', age: 35});

/*
This is a multi-line comment.
We are now creating some relationships.
*/
MATCH (p1:Person {name: 'Alice'}), (p2:Person {name: 'Bob'})
CREATE (p1)-[:KNOWS]->(p2);

MATCH (p2:Person {name: 'Bob'}), (p3:Person {name: 'Charlie'})
CREATE (p2)-[:FRIENDS_WITH]->(p3);

// Retrieve all people
MATCH (p:Person)
RETURN p.name, p.age;

// Clean up (optional: useful for development)
// MATCH (n) DETACH DELETE n;

How to Execute Cypher Script Files:
 * cypher-shell: This is the most common way. You can run cypher-shell -f /path/to/your/script.cypher.
 * Neo4j Browser: While the browser typically takes individual queries, you can paste multiple semicolon-separated queries into the query editor and execute them.
 * Neo4j Drivers: When using a programming language driver (Java, Python, Node.js, etc.), you would typically read the script file's content into a string and then execute it via the driver's session/transaction methods.
In summary, a Cypher script file is essentially a sequence of valid Cypher statements, each terminated by a semicolon, and often accompanied by comments for clarity. The .cypher extension is the best practice.
