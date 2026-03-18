---
type: THOUGHT
name: "thought.TRUTH CONFIRMS GOD"
alias: "Thought: Truth Confirms God"
parent: "topic.TRUTH"
en_content: "There is no truth that denies God's Existence."
tags: ["truth", "existence", "god", "denial", "philosophy"]
ptopic:
level: 2
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Oct-2013)
CREATE (t:THOUGHT {    name: "thought.TRUTH CONFIRMS GOD",
    alias: "Thought: Truth Confirms God",
    parent: "topic.TRUTH",
    tags: ['truth', 'existence', 'god', 'denial', 'philosophy'],
    level: 2});

CREATE (c:CONTENT {
    name: "content.TRUTH CONFIRMS GOD",
    ctype: "THOUGHT",
    en_title: "Truth Confirms God",
    en_content: "There is no truth that denies God's Existence.",
    es_title: "La Verdad Confirma a Dios",
    es_content: "No hay verdad que niegue la Existencia de Dios.",
    fr_title: "La Vérité Confirme Dieu",
    fr_content: "Il n'y a aucune vérité qui nie l'Existence de Dieu.",
    hi_title: "सत्य परमेश्वर की पुष्टि करता है",
    hi_content: "कोई भी सत्य परमेश्वर के अस्तित्व से इनकार नहीं करता।",
    zh_title: "Zhen Li Zheng Shi Shang Di",
    zh_content: "Mei You Ren He Zhen Li Fou Ren Shang Di De Cun Zai."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.TRUTH CONFIRMS GOD"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.TRUTH"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.TRUTH->TRUTH CONFIRMS GOD"
RETURN t, parent;
```
