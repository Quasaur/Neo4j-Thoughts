---
name: "thought.LIVELIER LIVING"
alias: "Thought: Livelier Living"
type: THOUGHT
en_content: "Soap makes water wetter; Jesus Christ makes living livelier!"
parent: "topic.SPIRITUALITY"
tags:
- jesus
- life
- joy
- spirituality
- character
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Feb-2012h)
CREATE (t:THOUGHT {
    name: "thought.LIVELIER LIVING",
    alias: "Thought: Livelier Living",
    parent: "topic.SPIRITUALITY",
    tags: ['jesus', 'life', 'joy', 'spirituality', 'character'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.LIVELIER LIVING",
    en_title: "Livelier Living",
    en_content: "Soap makes water wetter; Jesus Christ makes living livelier!",
    es_title: "Vivir Más Vivo",
    es_content: "El jabón hace el agua más húmeda; ¡Jesucristo hace el vivir más vivo!",
    fr_title: "Vivre Plus Vivant",
    fr_content: "Le savon rend l'eau plus mouillante ; Jésus-Christ rend la vie plus vivante !",
    hi_title: "जीवंत जीवन",
    hi_content: "साबुन पानी को और गीला बनाता है; यीशु मसीह जीवन को और जीवंत बनाते हैं!",
    zh_title: "Geng Huo Yue De Sheng Huo",
    zh_content: "Fei Zao Shi Shui Geng Shi Run; Ye Su Ji Du Shi Sheng Huo Geng Huo Yue!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.LIVELIER LIVING" AND c.name = "content.LIVELIER LIVING"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LIVELIER LIVING" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.LIVELIER LIVING"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >LIVELIER LIVING" }]->(child);
```
