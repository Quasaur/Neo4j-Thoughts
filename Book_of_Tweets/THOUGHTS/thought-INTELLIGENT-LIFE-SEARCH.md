---
type: THOUGHT
name: "thought.INTELLIGENT LIFE SEARCH"
alias: "Thought: Intelligent Life Search"
parent: "topic.PHILOSOPHY"
en_content: "Why is it that all of the instruments seeking intelligent life in the universe are pointed away from Earth?"
tags: ["intelligence", "universe", "earth", "search", "philosophy"]
ptopic:
level: 4
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Mar-2012)
CREATE (t:THOUGHT {    name: "thought.INTELLIGENT LIFE SEARCH",
    alias: "Thought: Intelligent Life Search",
    parent: "topic.PHILOSOPHY",
    tags: ['intelligence', 'universe', 'earth', 'search', 'philosophy'],
    level: 4});

CREATE (c:CONTENT {
    name: "content.INTELLIGENT LIFE SEARCH",
    ctype: "THOUGHT",
    en_title: "Intelligent Life Search",
    en_content: "Why is it that all of the instruments seeking intelligent life in the universe are pointed away from Earth?",
    es_title: "Búsqueda de Vida Inteligente",
    es_content: "¿Por qué es que todos los instrumentos que buscan vida inteligente en el universo están apuntados lejos de la Tierra?",
    fr_title: "Recherche de Vie Intelligente",
    fr_content: "Pourquoi est-ce que tous les instruments cherchant la vie intelligente dans l'univers sont pointés loin de la Terre ?",
    hi_title: "बुद्धिमान जीवन की खोज",
    hi_content: "ऐसा क्यों है कि ब्रह्मांड में बुद्धिमान जीवन की खोज करने वाले सभी उपकरण पृथ्वी से दूर की ओर निर्देशित हैं?",
    zh_title: "Zhìnéng Shēngmìng Sōusuǒ",
    zh_content: "Wèishénme suǒyǒu zài yǔzhòu zhōng xúnzhǎo zhìnéng shēngmìng de yíqì dōu zhǐxiàng yuǎnlí dìqiú de dìfāng?"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.INTELLIGENT LIFE SEARCH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PHILOSOPHY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PHILOSOPHY->INTELLIGENT LIFE SEARCH"
RETURN t, parent;
```
