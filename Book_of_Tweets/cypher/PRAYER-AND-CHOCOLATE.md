---
name: "thought.PRAYER AND CHOCOLATE"
alias: "Thought: Prayer And Chocolate"
type: THOUGHT
en_content: "Is there a better way to start a day than with prayer and chocolate? I think not!"
parent: "topic.SPIRITUALITY"
tags:
- prayer
- chocolate
- joy
- spirituality
- humor
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Jul-2013)
CREATE (t:THOUGHT {
    name: "thought.PRAYER AND CHOCOLATE",
    alias: "Thought: Prayer And Chocolate",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'chocolate', 'joy', 'spirituality', 'humor'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PRAYER AND CHOCOLATE",
    en_title: "Prayer And Chocolate",
    en_content: "Is there a better way to start a day than with prayer and chocolate? I think not!",
    es_title: "Oración Y Chocolate",
    es_content: "¿Hay una mejor manera de comenzar el día que con oración y chocolate? ¡Creo que no!",
    fr_title: "Prière Et Chocolat",
    fr_content: "Y a-t-il une meilleure façon de commencer une journée qu'avec la prière et le chocolat ? Je ne le pense pas !",
    hi_title: "प्रार्थना और चॉकलेट",
    hi_content: "क्या दिन की शुरुआत प्रार्थना और चॉकलेट के साथ करने से बेहतर कोई तरीका है? मुझे नहीं लगता!",
    zh_title: "Qídǎo Hé Qiǎokèlì",
    zh_content: "Yǒu shénme bǐ yòng qídǎo hé qiǎokèlì kāishǐ yītiān gèng hǎo de fāngfǎ ma? Wǒ rènwéi méiyǒu!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PRAYER AND CHOCOLATE" AND c.name = "content.PRAYER AND CHOCOLATE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRAYER AND CHOCOLATE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.PRAYER AND CHOCOLATE"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >PRAYER AND CHOCOLATE" }]->(child);
```
