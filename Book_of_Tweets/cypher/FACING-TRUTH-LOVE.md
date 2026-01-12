---
name: "thought.FACING TRUTH LOVE"
alias: "Thought: Facing Truth Love"
type: THOUGHT
en_content: "It's God's Love for us that enables us to face the truth about ourselves."
parent: "topic.GRACE"
tags:
- love
- truth
- grace
- self_examination
- transformation
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Sep-2012)
CREATE (t:THOUGHT {
    name: "thought.FACING TRUTH LOVE",
    alias: "Thought: Facing Truth Love",
    parent: "topic.GRACE",
    tags: ['love', 'truth', 'grace', 'self_examination', 'transformation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FACING TRUTH LOVE",
    en_title: "Facing Truth Love",
    en_content: "It's God's Love for us that enables us to face the truth about ourselves.",
    es_title: "Amor que Enfrenta la Verdad",
    es_content: "Es el Amor de Dios por nosotros lo que nos permite enfrentar la verdad sobre nosotros mismos.",
    fr_title: "L'Amour qui Affronte la Vérité",
    fr_content: "C'est l'Amour de Dieu pour nous qui nous permet de faire face à la vérité sur nous-mêmes.",
    hi_title: "सत्य का सामना करने वाला प्रेम",
    hi_content: "यह परमेश्वर का हमारे लिए प्रेम है जो हमें अपने बारे में सत्य का सामना करने में सक्षम बनाता है।",
    zh_title: "Mian Dui Zhen Li De Ai",
    zh_content: "Zheng Shi Shang Di Dui Wo Men De Ai Shi Wo Men Neng Gou Mian Dui Guan Yu Zi Ji De Zhen Li."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FACING TRUTH LOVE" AND c.name = "content.FACING TRUTH LOVE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FACING TRUTH LOVE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.FACING TRUTH LOVE"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >FACING TRUTH LOVE" }]->(child);
```
