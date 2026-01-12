---
name: "thought.CAT ON KNEE"
alias: "Thought: Cat On Knee"
type: THOUGHT
en_content: "My cat will jump up on my knee, and from there knock things off the table so he can play with them on the floor...God is great!"
parent: "topic.CREATION"
tags:
- creation
- nature
- design
- cat
- humor
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Oct-2011)
CREATE (t:THOUGHT {
    name: "thought.CAT ON KNEE",
    alias: "Thought: Cat On Knee",
    parent: "topic.CREATION",
    tags: ['creation', 'nature', 'design', 'cat', 'humor'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.CAT ON KNEE",
    en_title: "Cat On Knee",
    en_content: "My cat will jump up on my knee, and from there knock things off the table so he can play with them on the floor...God is great!",
    es_title: "Gato en la Rodilla",
    es_content: "Mi gato saltará sobre mi rodilla, y desde allí tirará cosas de la mesa para poder jugar con ellas en el suelo... ¡Dios es grande!",
    fr_title: "Chat sur le Genou",
    fr_content: "Mon chat va sauter sur mon genou, et de là faire tomber des choses de la table pour pouvoir jouer avec elles par terre... Dieu est grand !",
    hi_title: "घुटने पर बिल्ली",
    hi_content: "मेरी बिल्ली मेरे घुटने पर कूदेगी, और वहां से मेज से चीज़ें गिरा देगी ताकि वह फर्श पर उनके साथ खेल सके... भगवान महान हैं!",
    zh_title: "Māo zài Xīgài shàng",
    zh_content: "Wǒ de māo huì tiào dào wǒ de xīgài shàng, ránhòu cóng nàlǐ bǎ zhuōzi shàng de dōngxī nòng diào, zhèyàng tā jiù kěyǐ zài dìbǎn shàng wán le... Shàngdì shì wěidà de!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CAT ON KNEE" AND c.name = "content.CAT ON KNEE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CAT ON KNEE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.CAT ON KNEE"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >CAT ON KNEE" }]->(child);
```
