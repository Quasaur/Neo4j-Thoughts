---
type: THOUGHT
name: "thought.MEETING UNCREATED BEING"
alias: "Thought: Meeting Uncreated Being"
parent: "topic.THE GODHEAD"
en_content: "You haven't lived till you've met An Uncreated Being!"
tags: ["encounter", "uncreated", "life", "god", "divinity"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 29-Nov-2012)
CREATE (t:THOUGHT {    name: "thought.MEETING UNCREATED BEING",
    alias: "Thought: Meeting Uncreated Being",
    parent: "topic.THE GODHEAD",
    tags: ['encounter', 'uncreated', 'life', 'god', 'divinity'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.MEETING UNCREATED BEING",
    ctype: "THOUGHT",
    en_title: "Meeting Uncreated Being",
    en_content: "You haven't lived till you've met An Uncreated Being!",
    es_title: "Encuentro con el Ser Increado",
    es_content: "¡No has vivido hasta que has conocido a un Ser Increado!",
    fr_title: "Rencontrer l'Être Incréé",
    fr_content: "Tu n'as pas vécu tant que tu n'as pas rencontré un Être Incréé !",
    hi_title: "अनुत्पन्न सत्ता से मिलना",
    hi_content: "जब तक आपने अनुत्पन्न सत्ता से भेंट नहीं की है, तब तक आपने जीवन जिया ही नहीं है!",
    zh_title: "Yù jiàn wú chuàng zào zhě",
    zh_content: "Zhǐ yǒu yù jiàn le wú chuàng zào zhě, nǐ cái zhēn zhèng dì huó guò!"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.MEETING UNCREATED BEING"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->MEETING UNCREATED BEING"
RETURN t, parent;
```
