---
name: "thought.NO DIVINE EXCUSES"
alias: "Thought: No Divine Excuses"
type: THOUGHT
en_content: "God can and will forgive anything...but He will not excuse anything."
parent: "topic.THE GODHEAD"
tags:
- forgiveness
- excuse
- character
- god
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 28-Nov-2012)
CREATE (t:THOUGHT {
    name: "thought.NO DIVINE EXCUSES",
    alias: "Thought: No Divine Excuses",
    parent: "topic.THE GODHEAD",
    tags: ['forgiveness', 'excuse', 'character', 'god', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.NO DIVINE EXCUSES",
    en_title: "No Divine Excuses",
    en_content: "God can and will forgive anything...but He will not excuse anything.",
    es_title: "Sin Excusas Divinas",
    es_content: "Dios puede y perdonará cualquier cosa...pero Él no excusará nada.",
    fr_title: "Aucune Excuse Divine",
    fr_content: "Dieu peut et pardonnera tout...mais Il n'excusera rien.",
    hi_title: "कोई दिव्य बहाने नहीं",
    hi_content: "परमेश्वर कुछ भी क्षमा कर सकता है और करेगा...लेकिन वह किसी चीज़ को बहाना नहीं बनाएगा।",
    zh_title: "méi yǒu shén shèng jiè kǒu",
    zh_content: "shàng dì néng gòu bìng qiě huì kuān shù yī qiè...dàn shì tā bù huì wèi rèn hé shì qíng zhǎo jiè kǒu."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.NO DIVINE EXCUSES" AND c.name = "content.NO DIVINE EXCUSES"
MERGE (t)-[:HAS_CONTENT { "name": "edge.NO DIVINE EXCUSES" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.NO DIVINE EXCUSES"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >NO DIVINE EXCUSES" }]->(child);
```
