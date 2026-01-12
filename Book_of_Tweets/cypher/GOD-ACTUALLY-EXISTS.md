---
name: "thought.GOD ACTUALLY EXISTS"
alias: "Thought: God Actually Exists"
type: THOUGHT
en_content: "The idea that a Being such as That described in the Bible (God) actually exists should frighten us all...and it will."
parent: "topic.THE GODHEAD"
tags:
- existence
- god
- fear
- truth
- divinity
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Oct-2013)
CREATE (t:THOUGHT {
    name: "thought.GOD ACTUALLY EXISTS",
    alias: "Thought: God Actually Exists",
    parent: "topic.THE GODHEAD",
    tags: ['existence', 'god', 'fear', 'truth', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD ACTUALLY EXISTS",
    en_title: "God Actually Exists",
    en_content: "The idea that a Being such as That described in the Bible (God) actually exists should frighten us all...and it will.",
    es_title: "Dios Realmente Existe",
    es_content: "La idea de que un Ser como Aquel descrito en la Biblia (Dios) realmente existe debería asustarnos a todos... y lo hará.",
    fr_title: "Dieu Existe Réellement",
    fr_content: "L'idée qu'un Être tel que Celui décrit dans la Bible (Dieu) existe réellement devrait nous effrayer tous... et cela arrivera.",
    hi_title: "परमेश्वर वास्तव में अस्तित्व में है",
    hi_content: "यह विचार कि बाइबल में वर्णित एक ऐसा अस्तित्व (परमेश्वर) वास्तव में है, हम सभी को डराना चाहिए... और यह होगा।",
    zh_title: "Shén què shí cún zài",
    zh_content: "Xiàng Shèng jīng zhōng miáo shù de nà yàng yī gè cún zài (Shén) què shí cún zài de xiǎng fǎ yīng gāi ràng wǒ men suǒ yǒu rén dōu gǎn dào kǒng jù... ér qiě huì de."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GOD ACTUALLY EXISTS" AND c.name = "content.GOD ACTUALLY EXISTS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD ACTUALLY EXISTS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD ACTUALLY EXISTS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >GOD ACTUALLY EXISTS" }]->(child);
```
