---
name: passage.REMOVING ALL THINGS
alias: "Passage: Removing All Things"
type: PASSAGE
en_content: '"I will completely remove all things from the face of the earth."'
parent: topic.DIVINE SOVEREIGNTY
tags:
  - judgment
  - sovereignty
  - bible
  - earth
  - prophecy
level: 2
neo4j: true
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Nov-2011c)
CREATE (t:THOUGHT {
    name: "thought.REMOVING ALL THINGS",
    alias: "Thought: Removing All Things",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['judgment', 'sovereignty', 'bible', 'earth', 'prophecy'],
    source: "Zephania 1:2'",
    sortedsource: "'Zephaniah 01:02'",
    biblelink: "((https://www.biblegateway.com/passage/?search=Zephaniah%201%3A2&version=NASB)",
    level: 2                   
});

CREATE (c:CONTENT {
    name: "content.REMOVING ALL THINGS",
    en_title: "Removing All Things",
    en_content: "\"I will completely remove all things from the face of the earth,"\ -- God",
    es_title: "Eliminando todas las cosas",
    es_content: "«Eliminaré por completo todas las cosas de la faz de la tierra», — Dios",
    fr_title: "Suppression de toutes choses",
    fr_content: "« Je supprimerai complètement toutes choses de la surface de la terre », — Dieu",
    hi_title: "सभी चीज़ों को हटाना",
    hi_content: ""\मैं धरती की सतह से सभी चीज़ों को पूरी तरह हटा दूँगा,"\ -- ईश्वर",
    zh_title: "Qīngchú wànwù",
    zh_content: "“\wǒ bì jiāng dìshàng de yīqiè chèdǐ qīngchú.”\——Shàngdì"
});

MATCH (t:THOUGHT {name: "thought.REMOVING ALL THINGS"})
MATCH (c:CONTENT {name: "content.REMOVING ALL THINGS"})
MERGE (t)-[:HAS_CONTENT { "name": "b.edge.REMOVING ALL THINGS" }]->(c);

MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MATCH (child:THOUGHT {name: "thought.REMOVING ALL THINGS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "b.edge.DIVINE SOVEREIGNTY->REMOVING ALL THINGS" }]->(child);
```
