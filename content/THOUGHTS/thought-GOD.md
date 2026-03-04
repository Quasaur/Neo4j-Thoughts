---
type: THOUGHT
name: "thought.GOD"
alias: "Thought: Impersonal God"
en_content: "An impersonal god is not God at all; that is why the God of the Hebrews named Himself 'I AM'\"."
tags: ["god", "personal", "impersonal", "sentience", "self_aware"]
ptopic: "[[topic-THE-GODHEAD]]"
level: 1
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.GOD",
    alias: "Thought: Impersonal God",
    parent: "topic.THE GODHEAD",
    tags: ["god", "personal", "impersonal", "sentience", "self_aware"],
    level: 1
});

CREATE (c:CONTENT {
    name: "content.GOD",
    ctype: "THOUGHT",
    en_title: "God",
    en_content: "An impersonal god is not God at all; that is why the God of the Hebrews named Himself 'I AM'\".",
    es_title: "DIOS IMPERSONAL",
    es_content: "Un dios impersonal no es Dios en absoluto; por eso el Dios de los hebreos se llamó 'YO SOY'\".",
    fr_title: "DIEU IMPERSONNEL",
    fr_content: "Un dieu impersonnel n’est pas Dieu du tout ; c'est pourquoi le Dieu des Hébreux s'est nommé \"JE SUIS\"\".",
    hi_title: "अवैयक्तिक भगवान",
    hi_content: "एक अवैयक्तिक ईश्वर बिल्कुल भी ईश्वर नहीं है; इसीलिए इब्रानियों के परमेश्वर ने अपना नाम 'मैं हूँ' रखा।",
    zh_title: "fēi rén gé de shàng dì",
    zh_content: "yí gè fēi rén gé de shén gēn běn jiù bú shì shén ； tā shì yí gè shén 。 zhè jiù shì wèi shén me xī bó lái rén de shén chēng zì jǐ wèi ‘ zì yǒu yǒng yǒu ’”。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GOD" AND c.name = "content.GOD"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.GOD"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.GOD"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.THE GODHEAD->GOD"}]->(child);
```
