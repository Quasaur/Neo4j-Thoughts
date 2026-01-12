---
name: "thought.SELF DESTRUCTIVE NATURE"
alias: "Thought: Self Destructive Nature"
type: THOUGHT
en_content: "We are self-destructive by nature and teach our children to be self-destructive."
parent: "topic.HUMANITY"
tags:
- humanity
- children
- destruction
- nature
- character
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Sep-2013c)
CREATE (t:THOUGHT {
    name: "thought.SELF DESTRUCTIVE NATURE",
    alias: "Thought: Self Destructive Nature",
    parent: "topic.HUMANITY",
    tags: ['humanity', 'children', 'destruction', 'nature', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SELF DESTRUCTIVE NATURE",
    en_title: "Self Destructive Nature",
    en_content: "We are self-destructive by nature and teach our children to be self-destructive.",
    es_title: "Naturaleza Autodestructiva",
    es_content: "Somos autodestructivos por naturaleza y enseñamos a nuestros hijos a ser autodestructivos.",
    fr_title: "Nature Autodestructrice",
    fr_content: "Nous sommes autodestructeurs par nature et nous enseignons à nos enfants à être autodestructeurs.",
    hi_title: "आत्म-विनाशकारी प्रकृति",
    hi_content: "हम प्रकृति से आत्म-विनाशकारी हैं और अपने बच्चों को आत्म-विनाशकारी होना सिखाते हैं।",
    zh_title: "Zi Wo Hui Mie De Ben Xing",
    zh_content: "Wo Men Ben Xing Shang Shi Zi Wo Hui Mie De, Bing Qie Jiao Dao Wo Men De Hai Zi Ye Bian De Zi Wo Hui Mie."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SELF DESTRUCTIVE NATURE" AND c.name = "content.SELF DESTRUCTIVE NATURE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SELF DESTRUCTIVE NATURE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.SELF DESTRUCTIVE NATURE"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >SELF DESTRUCTIVE NATURE" }]->(child);
```
