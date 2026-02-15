---
name: "thought.UNFAIR"
alias: "Thought: Unfair"
type: THOUGHT
parent: "topic.DIVINE-SOVEREIGNTY"
es_content: "You may call God unfair, yet your life is still in His Hand; perhaps it would be wiser to bow and worship than to provoke."
tags:
- god
- unfair
- wise
- bow
- submit
neo4j: true
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
---

```Cypher
// 18-Mar-2010a
CREATE (t:THOUGHT {
    name: "thought.UNFAIR",
    alias: "Thought: Unfair",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["god", "unfair", "wise", "bow", "submit"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.UNFAIR",
    en_title: "Unfair",
    en_content: "You may call God unfair, yet your life is still in His Hand; perhaps it would be wiser to bow and worship than to provoke.",
    es_title: "Injusto",
    es_content: "Puedes llamar a Dios injusto, pero tu vida aún está en Sus manos; tal vez sea más sabio inclinarse y adorar que provocar.",
    fr_title: "Injuste",
    fr_content: "Vous pouvez qualifier Dieu d'injuste, mais votre vie reste entre ses mains ; il serait peut-être plus sage de s'incliner et de l'adorer que de le provoquer.",
    hi_title: "अन्याय",
    hi_content: "आप भगवान को अन्यायी कह सकते हैं, फिर भी आपकी ज़िंदगी उनके हाथ में है; शायद गुस्सा दिलाने के बजाय झुकना और पूजा करना ज़्यादा समझदारी होगी।"",
    zh_title: "Bù gōngpíng",
    zh_content: "nǐ huòxǔ huì shuō shàngdì bù gōngpíng, dàn nǐ de shēngmìng réngrán zhǎngwò zài tā shǒuzhōng; huòxǔ fǔshǒu jìng bài bǐ jīnù tā gèng míngzhì."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.UNFAIR" AND c.name = "content.UNFAIR"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.UNFAIR"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE-SOVEREIGNTY" AND child.name = "thought.UNFAIR"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.DIVINE-SOVEREIGNTY->UNFAIR"}]->(child);
```