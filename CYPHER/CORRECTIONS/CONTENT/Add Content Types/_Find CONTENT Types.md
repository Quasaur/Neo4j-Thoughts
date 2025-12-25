```Cypher
//find all content nodes that have a ctype promperty
MATCH (c:CONTENT) WHERE c.ctype IS NOT NULL RETURN c;
//Search for content type thought
MATCH (c:CONTENT) WHERE c.ctype = 1 RETURN c;
//Search for content type quote
MATCH (c:CONTENT) WHERE c.ctype = 2 RETURN c;
//Search for content type passage
MATCH (c:CONTENT) WHERE c.ctype = 3 RETURN c;

// find any nodes of type PASSAGE that have relationship of the HAS_CONTENT type.
MATCH (p:PASSAGE)-[:HAS_CONTENT]-() RETURN p;

// find any nodes of type PASSAGE that have relationship of the HAS_CONTENT type; include the CONTENT nodes.
MATCH (p:PASSAGE)-[:HAS_CONTENT]->(c:CONTENT) RETURN p, c;

//  find any nodes of type PASSAGE that have relationships of the HAS_CONTENT type; include the CONTENT nodes. and their relationships to the PASSAGE nodes.
MATCH (p:PASSAGE)-[r:HAS_CONTENT]->(c:CONTENT) RETURN p, r, c;
```