---
name: "thought.EDUCATION AS SELLING OUT"
alias: "Thought: Education As Selling Out"
type: THOUGHT
en_content: "At what point in history did African American men decide that being educated was selling out??"
parent: "topic.TRUTH"
tags:
- education
- truth
- selling_out
- race
- history
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Mar-2012d)
CREATE (t:THOUGHT {
    name: "thought.EDUCATION AS SELLING OUT",
    alias: "Thought: Education As Selling Out",
    parent: "topic.TRUTH",
    tags: ['education', 'truth', 'selling_out', 'race', 'history'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.EDUCATION AS SELLING OUT",
    en_title: "Education As Selling Out",
    en_content: "At what point in history did African American men decide that being educated was selling out??",
    es_title: "La educación como venta",
    es_content: "¿En qué momento de la historia los hombres afroamericanos decidieron que recibir educación era venderse?",
    fr_title: "L’éducation comme vente",
    fr_content: "À quel moment de l’histoire les hommes afro-américains ont-ils décidé qu’être instruit revenait à se vendre ?",
    hi_title: "शिक्षा बिक रही है",
    hi_content: "इतिहास के किस मोड़ पर अफ्रीकी अमेरिकी पुरुषों ने निर्णय लिया कि शिक्षित होना बिकाऊ है??",
    zh_title: "jiào yù chū mài",
    zh_content: "lì shǐ shàng de nǎ ge shí kè ， fēi yì měi guó nán xìng jué dìng jiē shòu jiào yù jiù shì chū mài zì jǐ ？"
});

MATCH (t:THOUGHT {name: "thought.EDUCATION AS SELLING OUT"})
MATCH (c:CONTENT {name: "content.EDUCATION AS SELLING OUT"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.EDUCATION AS SELLING OUT" }]->(c);

MATCH (parent:TOPIC {name: "topic.TRUTH"})
MATCH (child:THOUGHT {name: "thought.EDUCATION AS SELLING OUT"})
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH->EDUCATION AS SELLING OUT" }]->(child);
```
