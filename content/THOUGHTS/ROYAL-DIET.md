---
name: "thought.ROYAL_DIET"
alias: "Thought: DIET01"
type: THOUGHT
parent: topic.HEALTH
tags:
- breakfast
- lunch
- dinner
- king
- prince
neo4j: true
ptopic: "[[topic-HEALTH]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.ROYAL_DIET",
    alias: "Thought: DIET01",
    parent: "topic.HEALTH",
    tags: ["breakfast", "lunch", "dinner", "king", "prince"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ROYAL_DIET",
    en_title: "DIET01",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ROYAL_DIET" AND c.name = "content.ROYAL_DIET"
MERGE (t)-[:HAS_CONTENT {name: "edge.ROYAL_DIET"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HEALTH" AND child.name = "thought.ROYAL_DIET"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.HEALTH->ROYAL_DIET"}]->(child);
```
