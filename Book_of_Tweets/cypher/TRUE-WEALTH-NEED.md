---
name: "thought.TRUE WEALTH NEED"
alias: "Thought: True Wealth Need"
type: THOUGHT
en_content: "Matthew 10:34-39: One is not truly wealthy until they've lost their need for everything!"
parent: "topic.PHILOSOPHY"
tags:
- wealth
- need
- philosophy
- character
- independence
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Oct-2012b)
CREATE (t:THOUGHT {
    name: "thought.TRUE WEALTH NEED",
    alias: "Thought: True Wealth Need",
    parent: "topic.PHILOSOPHY",
    tags: ['wealth', 'need', 'philosophy', 'character', 'independence'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.TRUE WEALTH NEED",
    en_title: "True Wealth Need",
    en_content: "Matthew 10:34-39: One is not truly wealthy until they've lost their need for everything!",
    es_title: "Necesidad de Verdadera Riqueza",
    es_content: "Mateo 10:34-39: ¡Uno no es verdaderamente rico hasta que ha perdido su necesidad de todo!",
    fr_title: "Besoin de Vraie Richesse",
    fr_content: "Matthieu 10:34-39: On n'est pas vraiment riche tant qu'on n'a pas perdu son besoin de tout!",
    hi_title: "सच्ची संपत्ति की आवश्यकता",
    hi_content: "मत्ती 10:34-39: व्यक्ति तब तक सच्चा धनवान नहीं है जब तक वह सब कुछ की अपनी आवश्यकता को खो नहीं देता!",
    zh_title: "Zhen Zheng Cai Fu De Xu Yao",
    zh_content: "Ma Tai Fu Yin 10:34-39: Yi ge ren zhi you dang ta shi qu le dui yi qie de xu yao shi, cai zhen zheng fu you!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.TRUE WEALTH NEED" AND c.name = "content.TRUE WEALTH NEED"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TRUE WEALTH NEED" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.TRUE WEALTH NEED"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >TRUE WEALTH NEED" }]->(child);
```
