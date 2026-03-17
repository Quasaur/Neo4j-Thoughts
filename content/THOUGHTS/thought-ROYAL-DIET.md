---
type: THOUGHT
name: "thought.ROYAL DIET"
alias: "Thought: Diet01"
parent: "topic.HEALTH"
en_content: "Eat breakfast like a king | queen; eat lunch like a prince | princess; eat dinner like a pauper. - Brian Tracy"
tags: ["breakfast", "lunch", "dinner", "king", "prince"]
ptopic: "[[topic-HEALTH]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.ROYAL DIET",
    alias: "Thought: Diet01",
    parent: "topic.HEALTH",
    tags: ["breakfast", "lunch", "dinner", "king", "prince"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ROYAL DIET",
    ctype: "THOUGHT",
    en_title: "Diet01",
    en_content: "Eat breakfast like a king | queen; eat lunch like a prince | princess; eat dinner like a pauper. - Brian Tracy",
    es_title: "DIETA01",
    es_content: "Desayuna como un rey | reina; almorzar como un príncipe | princesa; cenar como un pobre. -Brian Tracy",
    fr_title: "RÉGIME01",
    fr_content: "Prenez votre petit-déjeuner comme un roi | reine; déjeuner comme un prince | princesse; dîne comme un pauvre. -Brian Tracy",
    hi_title: "DIET01",
    hi_content: "राजा की तरह नाश्ता करें | रानी; दोपहर का खाना राजकुमार की तरह खाओ | राजकुमारी; रात का खाना एक कंगाल की तरह खाओ. -ब्रायन ट्रेसी",
    zh_title: "yǐn shí 01",
    zh_content: "xiàng guó wáng yī yàng chī zǎo cān  | nǚ wáng ; xiàng wáng zǐ yī yàng chī wǔ cān | gōng zhǔ ; xiàng qǐ gài yī yàng chī wǎn fàn 。 —— bù lái ēn · tè léi xī"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.ROYAL DIET"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HEALTH"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HEALTH->ROYAL DIET"
RETURN t, parent;
```
