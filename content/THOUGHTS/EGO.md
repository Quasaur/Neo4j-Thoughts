---
title: "Thought: EGO"
draft: false
type: THOUGHT
mling: false
tags:
  - god
  - sun
  - earth
  - humility
  - myself
neo4j: true
ptopic: "[[topic-THE-GODHEAD]]"
level: 1
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.EGO",
    alias: "Thought: The Greatness of God",
    parent: "topic.THE GODHEAD",
    tags: ["god", "sun", "earth", "myself", "humility"],
    level: 1
});

CREATE (c:CONTENT {
    name: "content.EGO",
    en_title: "EGO",
    en_content: "The Earth is 3.5 million times bigger than me...
..the Sun is a million times bigger than the Earth...
...that means the Sun is 176 SEPTILLION (176 followed by 24 zeros) times larger than myself...
...GOD is great...I am pathetic.",
    es_title: "EGO",
    es_content: "La Tierra es 3,5 millones de veces más grande que yo...
..el Sol es un millón de veces más grande que la Tierra...
...eso significa que el Sol es 176 SEPTILLONES (176 seguido de 24 ceros) veces más grande que yo...
...DIOS es grande...Soy patético.",
    fr_title: "EGO",
    fr_content: "La Terre est 3,5 millions de fois plus grande que moi...
..le Soleil est un million de fois plus gros que la Terre...
...cela signifie que le Soleil est 176 SEPTILLIONS (176 suivis de 24 zéros) fois plus grand que moi...
... DIEU est grand... Je suis pathétique.",
    hi_title: "अहंकार",
    hi_content: "पृथ्वी मुझसे 35 लाख गुना बड़ी है...
..सूर्य पृथ्वी से लाखों गुना बड़ा है...
...इसका मतलब है कि सूर्य मुझसे 176 सेप्टिलियन (176 के बाद 24 शून्य) गुना बड़ा है...
...भगवान महान हैं...मैं दयनीय हूं।",
    zh_title: "zì wǒ",
    zh_content: "dì qiú bǐ wǒ dà 350 wàn bèi ……
.. tài yáng bǐ dì qiú dà yī bǎi wàn bèi ......
... zhè yì wèi zhe tài yáng bǐ wǒ dà  176 SEPTILLION（176  hòu miàn gēn zhe  24  gè líng ） bèi ...
... shàng dì shì wěi dà de ... wǒ hěn kě lián 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.EGO" AND c.name = "content.EGO"
MERGE (t)-[:HAS_CONTENT {name: "edge.EGO"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.EGO"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE GODHEAD->EGO"}]->(child);
```
