---
name: "thought.WAY TO MANS EGO"
alias: "Thought: Way To Mans Ego"
type: THOUGHT
en_content: "The fastest way to a man's heart is not through his stomach, but his ego."
parent: "topic.HUMANITY"
tags:
- man
- heart
- ego
- humanity
- irony
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Jul-2013)
CREATE (t:THOUGHT {
    name: "thought.WAY TO MANS EGO",
    alias: "Thought: Way To Mans Ego",
    parent: "topic.HUMANITY",
    tags: ['man', 'heart', 'ego', 'humanity', 'irony'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.WAY TO MANS EGO",
    en_title: "Way To Mans Ego",
    en_content: "The fastest way to a man's heart is not through his stomach, but his ego.",
    es_title: "Camino Al Ego Del Hombre",
    es_content: "El camino más rápido al corazón de un hombre no es a través de su estómago, sino de su ego.",
    fr_title: "Chemin Vers L'Ego De L'Homme",
    fr_content: "Le chemin le plus rapide vers le cœur d'un homme ne passe pas par son estomac, mais par son ego.",
    hi_title: "मनुष्य के अहंकार का मार्ग",
    hi_content: "किसी पुरुष के हृदय तक पहुँचने का सबसे तेज़ रास्ता उसके पेट से नहीं, बल्कि उसके अहंकार से होकर जाता है।",
    zh_title: "tong xiang nan ren zi wo de dao lu",
    zh_content: "tong wang nan ren xin ling de zui kuai tu jing bu shi tong guo ta de wei, er shi ta de zi wo."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.WAY TO MANS EGO" AND c.name = "content.WAY TO MANS EGO"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WAY TO MANS EGO" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.WAY TO MANS EGO"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >WAY TO MANS EGO" }]->(child);
```
