---
name: "thought.DEFINING PORNOGRAPHY"
alias: "Thought: Defining Pornography"
type: THOUGHT
en_content: "Matthew 5:27-30: Porn is adultery to a married man and fornication to a bachelor."
parent: "topic.MORALITY"
tags:
- morality
- purity
- adultery
- bible
- sin
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Sep-2011a)
CREATE (t:THOUGHT {
    name: "thought.DEFINING PORNOGRAPHY",
    alias: "Thought: Defining Pornography",
    parent: "topic.MORALITY",
    tags: ['morality', 'purity', 'adultery', 'bible', 'sin'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DEFINING PORNOGRAPHY",
    en_title: "Defining Pornography",
    en_content: "Matthew 5:27-30: Porn is adultery to a married man and fornication to a bachelor.",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DEFINING PORNOGRAPHY" AND c.name = "content.DEFINING PORNOGRAPHY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINING PORNOGRAPHY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.DEFINING PORNOGRAPHY"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >DEFINING PORNOGRAPHY" }]->(child);
```
