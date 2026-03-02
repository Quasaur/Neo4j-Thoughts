---
type: THOUGHT
name: "thought.REPARATIONS"
alias: "Thought: REPARATIONS"
parent: "topic.JUSTICE"
tags: ["reparations", "slavery", "blackamericans", "compensation", "justice"]
ptopic: "[[topic-JUSTICE]]"
level: 5
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.REPARATIONS",
    alias: "Thought: REPARATIONS",
    parent: "topic.JUSTICE",
    tags: ["reparations", "slavery", "blackamericans", "compensation", "justice"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.REPARATIONS",
    ctype: "THOUGHT",
    en_title: "REPARATIONS",
 es_title: "INDEMNIZACIÓN",
 fr_title: "RÉPARATIONS",
 hi_title: "मुआवज़ा",
 zh_title: "péi cháng",
    en_content: "",
 es_content: "Reparaciones razonables a los descendientes de esclavos negros: esos descendientes deben estar EXENTOS DE IMPUESTOS FEDERALES Y ESTATALES.",
 fr_content: "Réparations raisonnables aux descendants d’esclaves noirs : ces descendants devraient être EXEMPTÉS D’IMPÔTS FÉDÉRAUX ET D’ÉTAT.",
 hi_content: "काले दासों के वंशजों को उचित मुआवज़ा: उन वंशजों को संघीय और राज्य कर-मुक्त होना चाहिए।",
 zh_content: "duì hēi rén nú lì de hòu dài de hé lǐ péi cháng ： zhè xiē hòu dài yīng gāi xiǎng shòu lián bāng hé zhōu miǎn shuì 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.REPARATIONS" AND c.name = "content.REPARATIONS"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.REPARATIONS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.JUSTICE" AND child.name = "thought.REPARATIONS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.JUSTICE->REPARATIONS"}]->(child);
```