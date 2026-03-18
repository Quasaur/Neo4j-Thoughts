---
type: THOUGHT
name: "thought.PRIDE VS DIGNITY RACE"
alias: "Thought: Pride Vs Dignity Race"
parent: "topic.HUMANITY"
en_content: "Why do African American men confuse pride with dignity?"
tags: ["pride", "dignity", "race", "character", "confusion"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Mar-2012c)
CREATE (t:THOUGHT {    name: "thought.PRIDE VS DIGNITY RACE",
    alias: "Thought: Pride Vs Dignity Race",
    parent: "topic.HUMANITY",
    tags: ['pride', 'dignity', 'race', 'character', 'confusion'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.PRIDE VS DIGNITY RACE",
    ctype: "THOUGHT",
    en_title: "Pride Vs Dignity Race",
    en_content: "Why do African American men confuse pride with dignity?",
    es_title: "Carrera Orgullo Vs Dignidad",
    es_content: "¿Por qué los hombres afroamericanos confunden orgullo con dignidad?",
    fr_title: "Course fierté contre dignité",
    fr_content: "Pourquoi les hommes afro-américains confondent-ils fierté et dignité ?",
    hi_title: "गौरव बनाम गरिमा की दौड़",
    hi_content: "अफ़्रीकी अमेरिकी पुरुष गर्व को गरिमा के साथ भ्रमित क्यों करते हैं?",
    zh_title: "jiāo ào yǔ zūn yán jìng sài",
    zh_content: "wèi shén me fēi yì měi guó nán xìng huì jiāng jiāo ào yǔ zūn yán hùn wéi yī tán ？"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PRIDE VS DIGNITY RACE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMANITY->PRIDE VS DIGNITY RACE"
RETURN t, parent;
```
