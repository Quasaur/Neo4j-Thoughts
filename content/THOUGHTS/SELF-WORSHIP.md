---
name: "thought.SELF_WORSHIP"
alias: "Thought: SELF WORSHIP"
type: THOUGHT
parent: topic.RELIGION
tags:
- narcissism
- selfworship
- religion
- humanitarian
- evolution
neo4j: true
ptopic: "[[topic-RELIGION]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SELF_WORSHIP",
    alias: "Thought: SELF WORSHIP",
    parent: "topic.RELIGION",
    tags: ["narcissism", "selfworship", "religion", "humanitarian", "evolution"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.SELF_WORSHIP",
    en_title: "SELF WORSHIP",
    en_content: "Self-awareness without God-awareness is just self-worship, from which comes humanitarianism and evolutionary theory.",
    es_title: "AUTOADORACIÓN",
    es_content: "La autoconciencia sin conciencia de Dios es sólo adoración a uno mismo, de la que proviene el humanitarismo y la teoría de la evolución.",
    fr_title: "ADORATION DE SOI",
    fr_content: "La conscience de soi sans la conscience de Dieu n’est qu’un culte de soi, d’où découlent l’humanitarisme et la théorie évolutionniste.",
    hi_title: "आत्म पूजा",
    hi_content: "ईश्वर-जागरूकता के बिना आत्म-जागरूकता सिर्फ आत्म-पूजा है, जिससे मानवतावाद और विकासवादी सिद्धांत आता है।",
    zh_title: "zì wǒ chóng bài",
    zh_content: "méi yǒu shàng dì yì shí de zì wǒ yì shí zhǐ shì zì wǒ chóng bài ， yóu cǐ chǎn shēng rén dào zhǔ yì hé jìn huà lùn 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SELF_WORSHIP" AND c.name = "content.SELF_WORSHIP"
MERGE (t)-[:HAS_CONTENT {name: "edge.SELF_WORSHIP"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.SELF_WORSHIP"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.RELIGION->SELF_WORSHIP"}]->(child);
```
