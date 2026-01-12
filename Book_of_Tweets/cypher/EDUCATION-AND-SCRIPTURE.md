---
name: "thought.EDUCATION AND SCRIPTURE"
alias: "Thought: Education And Scripture"
type: THOUGHT
en_content: "How can anyone be considered educated without having surveyed the Holy Scriptures?"
parent: "topic.TRUTH"
tags:
- education
- scripture
- bible
- survey
- truth
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Jul-2013a)
CREATE (t:THOUGHT {
    name: "thought.EDUCATION AND SCRIPTURE",
    alias: "Thought: Education And Scripture",
    parent: "topic.TRUTH",
    tags: ['education', 'scripture', 'bible', 'survey', 'truth'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.EDUCATION AND SCRIPTURE",
    en_title: "Education And Scripture",
    en_content: "How can anyone be considered educated without having surveyed the Holy Scriptures?",
    es_title: "Educación y Escritura",
    es_content: "¿Cómo puede alguien ser considerado educado sin haber estudiado las Sagradas Escrituras?",
    fr_title: "Éducation et Écriture",
    fr_content: "Comment peut-on être considéré comme éduqué sans avoir étudié les Saintes Écritures ?",
    hi_title: "शिक्षा और धर्मग्रंथ",
    hi_content: "पवित्र शास्त्रों का अध्ययन किए बिना किसी को शिक्षित कैसे माना जा सकता है?",
    zh_title: "Jiàoyù yǔ shèngjīng 教育与圣经",
    zh_content: "Rúguǒ méiyǒu dàochá shèngjīng, zěnme néng bèi shì wéi shòu jiàoyù ne? 如果没有导察圣经，怎么能被视为受教育呢？"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.EDUCATION AND SCRIPTURE" AND c.name = "content.EDUCATION AND SCRIPTURE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.EDUCATION AND SCRIPTURE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.EDUCATION AND SCRIPTURE"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >EDUCATION AND SCRIPTURE" }]->(child);
```
