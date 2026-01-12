---
name: "thought.REJECTED TRUTH WEIGHT"
alias: "Thought: Rejected Truth Weight"
type: THOUGHT
en_content: "The World will perish...crushed under the weight of the Truth it has rejected."
parent: "topic.TRUTH"
tags:
- truth
- rejection
- judgment
- world
- weight
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 30-May-2012c)
CREATE (t:THOUGHT {
    name: "thought.REJECTED TRUTH WEIGHT",
    alias: "Thought: Rejected Truth Weight",
    parent: "topic.TRUTH",
    tags: ['truth', 'rejection', 'judgment', 'world', 'weight'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.REJECTED TRUTH WEIGHT",
    en_title: "Rejected Truth Weight",
    en_content: "The World will perish...crushed under the weight of the Truth it has rejected.",
    es_title: "Peso de la Verdad Rechazada",
    es_content: "El Mundo perecerá...aplastado bajo el peso de la Verdad que ha rechazado.",
    fr_title: "Poids de la Vérité Rejetée",
    fr_content: "Le Monde périra...écrasé sous le poids de la Vérité qu'il a rejetée.",
    hi_title: "अस्वीकृत सत्य का भार",
    hi_content: "संसार नष्ट हो जाएगा...उस सत्य के भार तले दबकर जिसे उसने अस्वीकार किया है।",
    zh_title: "Bèi Jùjué Zhēnlǐ de Zhòngliàng",
    zh_content: "Shìjiè jiāng miè wáng...bèi tā suǒ jùjué de Zhēnlǐ zhòngliàng suǒ yāsuì."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.REJECTED TRUTH WEIGHT" AND c.name = "content.REJECTED TRUTH WEIGHT"
MERGE (t)-[:HAS_CONTENT { "name": "edge.REJECTED TRUTH WEIGHT" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.REJECTED TRUTH WEIGHT"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >REJECTED TRUTH WEIGHT" }]->(child);
```
