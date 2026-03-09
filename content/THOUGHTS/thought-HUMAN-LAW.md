---
type: THOUGHT
name: "thought.HUMAN LAW"
alias: "Thought: Human Law"
parent: "topic.LAW"
en_content: "Without accountability, there is no foundation for human law or human hope."
tags: ["humanity", "god", "accountable", "law", "hope"]
ptopic: "[[topic-LAW]]"
level: 4
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.HUMAN LAW",
    alias: "Thought: Human Law",
    parent: "topic.LAW",
    tags: ["humanity", "god", "accountable", "law", "hope"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.HUMAN LAW",
    ctype: "THOUGHT",
    en_title: "Human Law",
    en_content: "Without accountability, there is no foundation for human law or human hope.",
    es_title: "LEY HUMANA",
    es_content: "Sin rendición de cuentas, no hay fundamento para la ley humana ni para la esperanza humana.",
    fr_title: "DROIT HUMAIN",
    fr_content: "Sans responsabilité, il n’y a pas de fondement à la loi humaine ni à l’espoir humain.",
    hi_title: "मानव कानून",
    hi_content: "जवाबदेही के बिना, मानव कानून या मानवीय आशा का कोई आधार नहीं है।",
    zh_title: "rén lèi fǎ",
    zh_content: "méi yǒu wèn zé zhì ， rén lèi fǎ lǜ huò rén lèi xī wàng jiù méi yǒu jī chǔ 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HUMAN LAW" AND c.name = "content.HUMAN LAW"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.HUMAN LAW"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.LAW" AND child.name = "thought.HUMAN LAW"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.LAW->HUMAN LAW"}]->(child);
```
