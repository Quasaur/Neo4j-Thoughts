---
name: "thought.PURPOSELESS EXISTENCE"
alias: "Thought: Purposeless Existence"
type: THOUGHT
en_content: "What is so scientific about saying that Existence has no purpose?"
parent: "topic.PHILOSOPHY"
tags:
- purpose
- science
- existence
- philosophy
- meaning
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Oct-2011a)
CREATE (t:THOUGHT {
    name: "thought.PURPOSELESS EXISTENCE",
    alias: "Thought: Purposeless Existence",
    parent: "topic.PHILOSOPHY",
    tags: ['purpose', 'science', 'existence', 'philosophy', 'meaning'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.PURPOSELESS EXISTENCE",
    en_title: "Purposeless Existence",
    en_content: "What is so scientific about saying that Existence has no purpose?",
    es_title: "Existencia Sin Propósito",
    es_content: "¿Qué tiene de científico decir que la Existencia no tiene propósito?",
    fr_title: "Existence Sans But",
    fr_content: "Qu'y a-t-il de si scientifique à dire que l'Existence n'a pas de but ?",
    hi_title: "उद्देश्यहीन अस्तित्व",
    hi_content: "यह कहने में क्या वैज्ञानिक बात है कि अस्तित्व का कोई उद्देश्य नहीं है?",
    zh_title: "Wu mu di de cun zai",
    zh_content: "Shuo cun zai mei you mu di you shen me ke xue xing ne?"
});

MATCH (t:THOUGHT {name: "thought.PURPOSELESS EXISTENCE"})
MATCH (c:CONTENT {name: "content.PURPOSELESS EXISTENCE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.PURPOSELESS EXISTENCE" }]->(c);

MATCH (parent:TOPIC {name: "topic.PHILOSOPHY"})
MATCH (child:THOUGHT {name: "thought.PURPOSELESS EXISTENCE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY->PURPOSELESS EXISTENCE" }]->(child);
```
