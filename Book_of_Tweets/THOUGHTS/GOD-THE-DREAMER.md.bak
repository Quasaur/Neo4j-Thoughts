---
name: "thought.GOD THE DREAMER"
alias: "Thought: God The Dreamer"
type: THOUGHT
en_content: "Existence is a Dream--but we're not the dreamers...God is!"
parent: "topic.PHILOSOPHY"
tags:
- reality
- dream
- existence
- philosophy
- creator
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 11-Oct-2010)
CREATE (t:THOUGHT {
    name: "thought.GOD THE DREAMER",
    alias: "Thought: God The Dreamer",
    parent: "topic.PHILOSOPHY",
    tags: ['reality', 'dream', 'existence', 'philosophy', 'creator'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.GOD THE DREAMER",
    en_title: "God The Dreamer",
    en_content: "Existence is a Dream--but we're not the dreamers...God is!",
    es_title: "dios el soñador",
    es_content: "La existencia es un sueño, pero nosotros no somos los soñadores... ¡Dios sí lo es!",
    fr_title: "Dieu le rêveur",
    fr_content: "L'existence est un rêve, mais nous ne sommes pas des rêveurs... Dieu l'est !",
    hi_title: "सपने देखने वाला भगवान",
    hi_content: "अस्तित्व एक सपना है--लेकिन हम सपने देखने वाले नहीं हैं...ईश्वर है!",
    zh_title: "梦想家上帝",
    zh_content: "存在是一个梦想——但我们不是梦想家……上帝才是！"
});

MATCH (t:THOUGHT {name: "thought.GOD THE DREAMER"})
MATCH (c:CONTENT {name: "content.GOD THE DREAMER"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD THE DREAMER" }]->(c);

MATCH (parent:TOPIC {name: "topic.PHILOSOPHY"})
MATCH (child:THOUGHT {name: "thought.GOD THE DREAMER"})
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY->GOD THE DREAMER" }]->(child);
```
