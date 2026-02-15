---
name: thought.FORBIDDEN
alias: "Thought: Forbidden"
type: THOUGHT
parent: "topic.EVIL"
en_content: "What attracts us to the forbidden? It's forbidden!"
tags:
- prohibited
- restricted
- banned
- outlawed
- taboo
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
---

```Cypher
// 11-Mar-2010a
CREATE (t:THOUGHT {
    name: "thought.FORBIDDEN",
    alias: "Thought: Forbidden",
    parent: "topic.EVIL",
    tags: ["prohibited", "restricted", "banned", "outlawed", "taboo"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FORBIDDEN",
    en_title: "Forbidden",
    en_content: "What attracts us to the forbidden? It's forbidden!",
    es_title: "Prohibido",
    es_content: "¿Qué nos atrae de lo prohibido? ¡Está prohibido!",
    fr_title: "Interdit",
    fr_content: "Pourquoi est-ce que l'interdit nous attire ? Parce que c'est interdit !",
    hi_title: "मना किया हुआ",
    hi_content: "हमें मना की हुई चीज़ों की तरफ़ क्या आकर्षित करता है? यह मना है!",
    zh_title:"Jìnjì",
    zh_content: "shì shénme xīyǐn wǒmen qù zhuīqiú jìnjì? Yīnwèi tā jìnjì!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FORBIDDEN" AND c.name = "content.FORBIDDEN"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.FORBIDDEN"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.FORBIDDEN"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.EVIL->FORBIDDEN"}]->(child);
```