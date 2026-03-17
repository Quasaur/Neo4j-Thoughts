---
type: THOUGHT
name: "thought.UNFAIR"
alias: "Thought: Unfair"
parent: "topic.DIVINE-SOVEREIGNTY"
en_content: "You may call God unfair, yet your life is still in His Hand; perhaps it would be wiser to bow and worship than to provoke."
tags: ["god", "unfair", "wise", "bow", "submit"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
es_content: "Puedes llamar a Dios injusto, pero tu vida aún está en Sus manos; tal vez sea más sabio inclinarse y adorar que provocar."
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.UNFAIR",
    alias: "Thought: Unfair",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["god", "unfair", "wise", "bow", "submit"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.UNFAIR",
    ctype: "THOUGHT",
    en_title: "Unfair",
    en_content: "You may call God unfair, yet your life is still in His Hand; perhaps it would be wiser to bow and worship than to provoke.",
    es_title: "Injusto",
    es_content: "Puedes llamar a Dios injusto, pero tu vida aún está en Sus manos; tal vez sea más sabio inclinarse y adorar que provocar.",
    fr_title: "Injuste",
    fr_content: "Vous pouvez qualifier Dieu d'injuste, mais votre vie reste entre ses mains ; il serait peut-être plus sage de s'incliner et de l'adorer que de le provoquer.",
    hi_title: "अन्याय",
    hi_content: "आप भगवान को अन्यायी कह सकते हैं, फिर भी आपकी ज़िंदगी उनके हाथ में है; शायद गुस्सा दिलाने के बजाय झुकना और पूजा करना ज़्यादा समझदारी होगी।",
    zh_title: "",
    zh_content: "nǐ huòxǔ huì shuō shàngdì bù gōngpíng, dàn nǐ de shēngmìng réngrán zhǎngwò zài tā shǒuzhōng; huòxǔ fǔshǒu jìng bài bǐ jīnù tā gèng míngzhì."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.UNFAIR"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.DIVINE-SOVEREIGNTY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.DIVINE-SOVEREIGNTY->UNFAIR"
RETURN t, parent;
```
