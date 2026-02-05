---
name: "thought.RECOGNIZE OPPORTUNITY"
alias: "Thought: Recognize Opportunity"
type: THOUGHT
en_content: "The tragedy is that African American men do not recognize opportunity when they see it."
parent: "topic.WISDOM"
tags:
- opportunity
- wisdom
- tragedy
- recognition
- race
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Mar-2012a)
CREATE (t:THOUGHT {
    name: "thought.RECOGNIZE OPPORTUNITY",
    alias: "Thought: Recognize Opportunity",
    parent: "topic.WISDOM",
    tags: ['opportunity', 'wisdom', 'tragedy', 'recognition', 'race'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.RECOGNIZE OPPORTUNITY",
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

MATCH (t:THOUGHT {name: "thought.RECOGNIZE OPPORTUNITY"})
MATCH (c:CONTENT {name: "content.RECOGNIZE OPPORTUNITY"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.RECOGNIZE OPPORTUNITY" }]->(c);

MATCH (parent:TOPIC {name: "topic.WISDOM"})
MATCH (child:THOUGHT {name: "thought.RECOGNIZE OPPORTUNITY"})
MERGE (parent)-[:HAS_THOUGHT { "name": "WISDOM->RECOGNIZE OPPORTUNITY" }]->(child);
```
