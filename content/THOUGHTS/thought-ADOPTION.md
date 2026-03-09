---
type: THOUGHT
name: "thought.ADOPTION"
alias: "Thought: Adoption"
parent: "topic.THE-GOSPEL"
tags: ["adoption", "abba", "father", "child_of_god", "everlasting"]
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.ADOPTION",
    alias: "Thought: Adoption",
    parent: "topic.THE-GOSPEL",
    tags: ["adoption", "abba", "father", "child_of_god", "everlasting"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.ADOPTION",
    ctype: "THOUGHT",
    en_title: "Adoption",
 es_title: "ADOPCIÓN",
 fr_title: "ADOPTION",
 hi_title: "दत्तक ग्रहण",
 zh_title: "cǎi yòng",
    en_content: "",
 es_content: "Él es el Arquitecto del Cosmos y la Sede del Poder Absoluto... ¡y mi Papá!",
 fr_content: "Il est l'architecte du cosmos et le siège du pouvoir absolu... et mon papa !",
 hi_content: "वह ब्रह्मांड के वास्तुकार और पूर्ण शक्ति के केंद्र हैं...और मेरे पिताजी!",
 zh_content: "tā shì yǔ zhòu de jiàn zhù shī hé jué duì quán lì de bǎo zuò …… hái yǒu wǒ de bà bà ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ADOPTION" AND c.name = "content.ADOPTION"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.ADOPTION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "thought.ADOPTION"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.THE-GOSPEL->ADOPTION"}]->(child);
```