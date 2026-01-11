---
title: "Thought: THE ULTIMATE (2)"
draft: false
type: THOUGHT
mling: true
tags:
  - deity
  - wrath
  - grace
  - judgment
  - acquittal
neo4j: true
ptopic: "[[topic-THE-GODHEAD]]"
level: 1
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.THE_ULTIMATE2",
    alias: "Thought: THE ULTIMATE (2)",
    parent: "topic.THE-GODHEAD",
    tags: ["deity", "wrath", "grace", "judgment", "acquittal"],
    level: 1
});

CREATE (c:CONTENT {
    name: "content.THE_ULTIMATE2",
    en_title: "THE ULTIMATE (2)",
    en_content: "Every human that has ever lived will soon face either the Greatest Terror (God's Wrath) or the Greatest Pleasure (God's Grace).",
    es_title: "LO ÚLTIMO (2)",
    es_content: "Todo ser humano que alguna vez haya vivido pronto enfrentará el Mayor Terror (la Ira de Dios) o el Mayor Placer (la Gracia de Dios).",
    fr_title: "L'ULTIME (2)",
    fr_content: "Tout être humain ayant jamais vécu sera bientôt confronté soit à la plus grande terreur (la colère de Dieu), soit au plus grand plaisir (la grâce de Dieu).",
    hi_title: "परम (2)",
    hi_content: "प्रत्येक मानव जो कभी जीवित रहा है उसे जल्द ही सबसे बड़े आतंक (भगवान का क्रोध) या सबसे बड़ी खुशी (भगवान की कृपा) का सामना करना पड़ेगा।",
    zh_title: "zhōng jí  (2)",
    zh_content: "měi gè céng jīng shēng huó guò de rén lèi hěn kuài jiù huì miàn lín zuì dà de kǒng jù （ shàng dì de fèn nù ） huò zuì dà de kuài lè （ shàng dì de ēn diǎn ）。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE_ULTIMATE2" AND c.name = "content.THE_ULTIMATE2"
MERGE (t)-[:HAS_CONTENT {name: "edge.THE_ULTIMATE2"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-GODHEAD" AND child.name = "thought.THE_ULTIMATE2"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE-GODHEAD->THE_ULTIMATE2"}]->(child);
```
