---
type: THOUGHT
name: "thought.EDUCATION AND SCRIPTURE"
alias: "Thought: Education And Scripture"
parent: "topic.TRUTH"
en_content: "How can anyone be considered educated without having surveyed the Holy Scriptures?"
tags: ["education", "scripture", "bible", "survey", "truth"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Jul-2013a)
CREATE (t:THOUGHT {    name: "thought.EDUCATION AND SCRIPTURE",
    alias: "Thought: Education And Scripture",
    parent: "topic.TRUTH",
    tags: ['education', 'scripture', 'bible', 'survey', 'truth'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.EDUCATION AND SCRIPTURE",
    ctype: "THOUGHT",
    en_title: "Education And Scripture",
    en_content: "How can anyone be considered educated without having surveyed the Holy Scriptures?",
    es_title: "Educación y Escritura",
    es_content: "¿Cómo puede alguien ser considerado educado sin haber estudiado las Sagradas Escrituras?",
    fr_title: "Éducation et Écriture",
    fr_content: "Comment peut-on être considéré comme éduqué sans avoir étudié les Saintes Écritures ?",
    hi_title: "शिक्षा और धर्मग्रंथ",
    hi_content: "पवित्र शास्त्रों का अध्ययन किए बिना किसी को शिक्षित कैसे माना जा सकता है?",
    zh_title: "Jiàoyù yǔ shèngjīng  jiào yù yǔ shèng jīng",
    zh_content: "Rúguǒ méiyǒu dàochá shèngjīng, zěnme néng bèi shì wéi shòu jiàoyù ne?  rú guǒ méi yǒu dǎo chá shèng jīng ， zěn me néng bèi shì wéi shòu jiào yù ne ？"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.EDUCATION AND SCRIPTURE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.TRUTH"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.TRUTH->EDUCATION AND SCRIPTURE"
RETURN t, parent;
```
