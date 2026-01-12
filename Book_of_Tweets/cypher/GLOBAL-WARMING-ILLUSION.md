---
name: "thought.GLOBAL WARMING ILLUSION"
alias: "Thought: Global Warming Illusion"
type: THOUGHT
en_content: "Do you still believe global warming is an illusion?"
parent: "topic.CREATION"
tags:
- creation
- environment
- climate
- earth
- stewardship
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Aug-2011b)
CREATE (t:THOUGHT {
    name: "thought.GLOBAL WARMING ILLUSION",
    alias: "Thought: Global Warming Illusion",
    parent: "topic.CREATION",
    tags: ['creation', 'environment', 'climate', 'earth', 'stewardship'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GLOBAL WARMING ILLUSION",
    en_title: "Global Warming Illusion",
    en_content: "Do you still believe global warming is an illusion?",
    es_title: "Ilusión del calentamiento global",
    es_content: "¿Sigues creyendo que el calentamiento global es una ilusión?",
    fr_title: "Illusion du réchauffement climatique",
    fr_content: "Pensez-vous toujours que le réchauffement climatique est une illusion ?",
    hi_title: "ग्लोबल वार्मिंग भ्रम",
    hi_content: "क्या आप अब भी मानते हैं कि ग्लोबल वार्मिंग एक भ्रम है?",
    zh_title: "全球变暖错觉",
    zh_content: "您仍然相信全球变暖只是一种幻觉吗？"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GLOBAL WARMING ILLUSION" AND c.name = "content.GLOBAL WARMING ILLUSION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GLOBAL WARMING ILLUSION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.GLOBAL WARMING ILLUSION"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >GLOBAL WARMING ILLUSION" }]->(child);
```
