---
title: "Thought: MIRACLES"
draft: false
type: THOUGHT
mling: false
tags:
  - miracles
  - diine_power
  - acts_of_god
  - glory_of_god
  - signs
neo4j: true
ptopic: "[[topic-THE-GODHEAD]]"
level: 1
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.MIRACLES",
    alias: "Thought: Acts of God",
    parent: "topic.THE GODHEAD",
    tags: ["miracles", "acts_of_god", "divine_power", "glory_of_god", "signs"],
    level: 1
});

CREATE (c:CONTENT {
    name: "content.MIRACLES",
    en_title: "MIRACLES",
    en_content: "Miracles are...
...the only Acts God has ever done,
the only Acts God is doing,
and the only Acts God will ever do!",
    es_title: "MILAGROS",
    es_content: "Los milagros son...
...los únicos actos que Dios ha hecho jamás,
los únicos actos que Dios está haciendo,
¡Y los únicos actos que Dios jamás hará!",
    fr_title: "MIRACLES",
    fr_content: "Les miracles sont...
...les seuls actes que Dieu ait jamais accomplis,
les seuls actes que Dieu fait,
et les seuls actes que Dieu fera jamais !",
    hi_title: "चमत्कार",
    hi_content: "चमत्कार हैं...
...परमेश्वर ने अब तक जो एकमात्र कार्य किया है,
एकमात्र कार्य जो ईश्वर कर रहा है,
और एकमात्र कार्य जो परमेश्वर कभी करेगा!",
    zh_title: "qí jì",
    zh_content: "qí jì shì ...
…… zhè shì shàng dì wéi yī zuò guò de shì ，
 shén wéi yī suǒ zuò de shì ，
 zhè shì shén wéi yī huì zuò de shì ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MIRACLES" AND c.name = "content.MIRACLES"
MERGE (t)-[:HAS_CONTENT {name: "edge.MIRACLES"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.MIRACLES"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.THE GODHEAD->MIRACLES"}]->(child);
```
