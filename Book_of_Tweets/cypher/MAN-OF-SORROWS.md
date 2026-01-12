---
name: "thought.MAN OF SORROWS"
alias: "Thought: Man Of Sorrows"
type: THOUGHT
en_content: "Jesus was a Man of sorrows...acquainted with grief--not because of what they did to Him, but what they did to each other!"
parent: "topic.THE GODHEAD"
tags:
- jesus
- sorrow
- grief
- humanity
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Oct-2012a)
CREATE (t:THOUGHT {
    name: "thought.MAN OF SORROWS",
    alias: "Thought: Man Of Sorrows",
    parent: "topic.THE GODHEAD",
    tags: ['jesus', 'sorrow', 'grief', 'humanity', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.MAN OF SORROWS",
    en_title: "Man Of Sorrows",
    en_content: "Jesus was a Man of sorrows...acquainted with grief--not because of what they did to Him, but what they did to each other!",
    es_title: "Varón de Dolores",
    es_content: "Jesús era un Varón de dolores... familiarizado con el sufrimiento--no por lo que le hicieron a Él, sino por lo que se hicieron unos a otros!",
    fr_title: "Homme de Douleurs",
    fr_content: "Jésus était un Homme de douleurs... familier avec le chagrin--non pas à cause de ce qu'ils Lui ont fait, mais de ce qu'ils se sont fait les uns aux autres !",
    hi_title: "दुःख का पुरुष",
    hi_content: "यीशु दुःख का पुरुष था... शोक से परिचित--इसलिए नहीं कि उन्होंने उनके साथ क्या किया, बल्कि इसलिए कि उन्होंने एक दूसरे के साथ क्या किया!",
    zh_title: "Bēiāi zhī rén 悲哀之人",
    zh_content: "Yēsū shì bēiāi zhī rén... shì xī tòngkǔ de--bù shì yīnwèi tāmen duì tā zuò le shénme, ér shì yīnwèi tāmen bǐcǐ zuò le shénme! 耶穣是悲哀之人...熟悉痛苦的--不是因为他们对他做了什么，而是因为他们彼此做了什么！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MAN OF SORROWS" AND c.name = "content.MAN OF SORROWS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.MAN OF SORROWS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.MAN OF SORROWS"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >MAN OF SORROWS" }]->(child);
```
