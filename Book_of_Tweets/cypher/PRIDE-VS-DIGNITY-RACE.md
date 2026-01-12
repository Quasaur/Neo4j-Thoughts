---
name: "thought.PRIDE VS DIGNITY RACE"
alias: "Thought: Pride Vs Dignity Race"
type: THOUGHT
en_content: "Why do African American men confuse pride with dignity?"
parent: "topic.HUMANITY"
tags:
- pride
- dignity
- race
- character
- confusion
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Mar-2012c)
CREATE (t:THOUGHT {
    name: "thought.PRIDE VS DIGNITY RACE",
    alias: "Thought: Pride Vs Dignity Race",
    parent: "topic.HUMANITY",
    tags: ['pride', 'dignity', 'race', 'character', 'confusion'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.PRIDE VS DIGNITY RACE",
    en_title: "Pride Vs Dignity Race",
    en_content: "Why do African American men confuse pride with dignity?",
    es_title: "Carrera Orgullo Vs Dignidad",
    es_content: "¿Por qué los hombres afroamericanos confunden orgullo con dignidad?",
    fr_title: "Course fierté contre dignité",
    fr_content: "Pourquoi les hommes afro-américains confondent-ils fierté et dignité ?",
    hi_title: "गौरव बनाम गरिमा की दौड़",
    hi_content: "अफ़्रीकी अमेरिकी पुरुष गर्व को गरिमा के साथ भ्रमित क्यों करते हैं?",
    zh_title: "骄傲与尊严竞赛",
    zh_content: "为什么非裔美国男性会将骄傲与尊严混为一谈？"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PRIDE VS DIGNITY RACE" AND c.name = "content.PRIDE VS DIGNITY RACE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRIDE VS DIGNITY RACE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.PRIDE VS DIGNITY RACE"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >PRIDE VS DIGNITY RACE" }]->(child);
```
