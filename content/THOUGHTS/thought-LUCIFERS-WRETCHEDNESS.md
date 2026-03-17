---
type: THOUGHT
name: "thought.LUCIFERS WRETCHEDNESS"
alias: "Thought: Lucifers Wretchedness"
parent: "topic.EVIL"
en_content: "What a wretch Lucifer must be, to despise his most ardent Supporter!"
tags: ["lucifer", "pride", "evil", "supporter", "character"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.LUCIFERS WRETCHEDNESS",
    alias: "Thought: Lucifers Wretchedness",
    parent: "topic.EVIL",
    tags: ['lucifer', 'pride', 'evil', 'supporter', 'character'],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.LUCIFERS WRETCHEDNESS",
    ctype: "THOUGHT",
    en_title: "Lucifers Wretchedness",
    en_content: "What a wretch Lucifer must be, to despise his most ardent Supporter!",
    es_title: "La Miseria de Lucifer",
    es_content: "¡Qué miserable debe ser Lucifer, para despreciar a su más ferviente Defensor!",
    fr_title: "La Misère de Lucifer",
    fr_content: "Quel misérable Lucifer doit être, pour mépriser son plus ardent Soutien !",
    hi_title: "लूसिफर की दुर्दशा",
    hi_content: "लूसिफर कितना दयनीय होगा, अपने सबसे उत्कट समर्थक को तुच्छ समझने के लिए!",
    zh_title: "Lùxīfèi de bēicǎn  lù xī fú de bēi niè",
    zh_content: "Lùxīfèi dàgài shì duōme bēibiǐ, jìnrán qī shì tā zuì rèchéng de zhīchí zhě!  lù xī fú dà gài shì duō me bēi bǐ ， jìng rán qī shì tā zuì rè chéng de zhī chí zhě ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LUCIFERS WRETCHEDNESS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: ""})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.->LUCIFERS WRETCHEDNESS"
RETURN t, parent;
```
