---
type: THOUGHT
name: "thought.RECOGNIZE OPPORTUNITY"
alias: "Thought: Recognize Opportunity"
parent: "topic.WISDOM"
en_content: "The tragedy is that African American men do not recognize opportunity when they see it."
tags: ["opportunity", "wisdom", "tragedy", "recognition", "race"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Mar-2012a)
CREATE (t:THOUGHT {    name: "thought.RECOGNIZE OPPORTUNITY",
    alias: "Thought: Recognize Opportunity",
    parent: "topic.WISDOM",
    tags: ['opportunity', 'wisdom', 'tragedy', 'recognition', 'race'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.RECOGNIZE OPPORTUNITY",
    ctype: "THOUGHT",
    en_title: "Recognize Opportunity",
    en_content: "The tragedy is that African American men do not recognize opportunity when they see it.",
    es_title: "Reconocer la Oportunidad",
    es_content: "La tragedia es que los hombres afroamericanos no reconocen la oportunidad cuando la ven.",
    fr_title: "Reconnaître l'Opportunité",
    fr_content: "La tragédie est que les hommes afro-américains ne reconnaissent pas l'opportunité quand ils la voient.",
    hi_title: "अवसर को पहचानना",
    hi_content: "दुर्भाग्य यह है कि अफ्रीकी अमेरिकी पुरुष अवसर को देखते समय पहचान नहीं पाते।",
    zh_title: "Rènshí jīhuì  rèn shí jī huì",
    zh_content: "Bēijù shì Fēizhōu měiguó nánxìng zài kàndào jīhuì shí wúfǎ rènshí tā.  bēi jù shì fēi zhōu měi guó nán xìng zài kàn dào jī huì shí wú fǎ rèn shí tā 。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.RECOGNIZE OPPORTUNITY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.WISDOM"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.WISDOM->RECOGNIZE OPPORTUNITY"
RETURN t, parent;
```
