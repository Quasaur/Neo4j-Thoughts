---
name: "thought.KNOWING JESUS NAME"
alias: "Thought: Knowing Jesus Name"
type: THOUGHT
en_content: "Matthew 7:22, 23 -- Using Jesus' Name doesn't mean you know Jesus."
parent: "topic.THE GODHEAD"
tags:
- jesus
- identity
- knowledge
- lord
- relationship
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Nov-2011a)
CREATE (t:THOUGHT {
    name: "thought.KNOWING JESUS NAME",
    alias: "Thought: Knowing Jesus Name",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'identity', 'knowledge', 'lord', 'relationship'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.KNOWING JESUS NAME",
    en_title: "Knowing Jesus Name",
    en_content: "Matthew 7:22, 23 -- Using Jesus' Name doesn't mean you know Jesus.",
    es_title: "Conocer el Nombre de Jesús",
    es_content: "Mateo 7:22, 23 -- Usar el Nombre de Jesús no significa que conozcas a Jesús.",
    fr_title: "Connaître le Nom de Jésus",
    fr_content: "Matthieu 7:22, 23 -- Utiliser le Nom de Jésus ne signifie pas que vous connaissez Jésus.",
    hi_title: "यीशु का नाम जानना",
    hi_content: "मत्ती 7:22, 23 -- यीशु का नाम लेने का मतलब यह नहीं है कि आप यीशु को जानते हैं।",
    zh_title: "Rènshí Yēsū de míng 认识耶稣的名",
    zh_content: "Mǎdù fùyīn 7:22, 23 -- Shǐyòng Yēsū de míng bù dàibiǎo nǐ rènshi Yēsū. 马太福音 7:22, 23 --使用耶稣的名不代表你认识耶稣。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.KNOWING JESUS NAME" AND c.name = "content.KNOWING JESUS NAME"
MERGE (t)-[:HAS_CONTENT { "name": "edge.KNOWING JESUS NAME" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.KNOWING JESUS NAME"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >KNOWING JESUS NAME" }]->(child);
```
