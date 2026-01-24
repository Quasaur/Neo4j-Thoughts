---
name: "thought.INTELLIGENT LIFE SEARCH"
alias: "Thought: Intelligent Life Search"
type: THOUGHT
en_content: "Why is it that all of the instruments seeking intelligent life in the universe are pointed away from Earth?"
parent: "topic.PHILOSOPHY"
tags:
- intelligence
- universe
- earth
- search
- philosophy
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 01-Mar-2012)
CREATE (t:THOUGHT {
    name: "thought.INTELLIGENT LIFE SEARCH",
    alias: "Thought: Intelligent Life Search",
    parent: "topic.PHILOSOPHY",
    tags: ['intelligence', 'universe', 'earth', 'search', 'philosophy'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.INTELLIGENT LIFE SEARCH",
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

MATCH (t:THOUGHT {name: "thought.INTELLIGENT LIFE SEARCH"})
MATCH (c:CONTENT {name: "content.INTELLIGENT LIFE SEARCH"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.INTELLIGENT LIFE SEARCH" }]->(c);

MATCH (parent:TOPIC {name: "topic.PHILOSOPHY"})
MATCH (child:THOUGHT {name: "thought.INTELLIGENT LIFE SEARCH"})
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY->INTELLIGENT LIFE SEARCH" }]->(child);
```
