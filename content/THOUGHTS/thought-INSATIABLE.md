---
type: THOUGHT
name: "thought.INSATIABLE"
alias: "Thought: Insatiable"
parent: "topic.EVIL"
en_content: "The human flesh nature is never satisfied. Thus humanity is plunged into every kind of addiction to satiate the unforgiving beast."
tags: ["flesh", "carnal", "animalistic", "impetuous", "instinctual"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.INSATIABLE",
    alias: "Thought: Insatiable",
    parent: "topic.EVIL",
    tags: ["flesh", "carnal", "animalistic", "impetuous", "instinctual"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.INSATIABLE",
    ctype: "THOUGHT",
    en_title: "Insatiable",
    en_content: "The human flesh nature is never satisfied. Thus humanity is plunged into every kind of addiction to satiate the unforgiving beast.",
    es_title: "Insaciable",
    es_content: "La naturaleza humana nunca se satisface. Por ello, la humanidad se ve inmersa en todo tipo de adicciones para saciar a la bestia implacable.",
    fr_title: "Insatiable",
    fr_content: "La nature humaine est insatiable. C'est pourquoi l'humanité sombre dans toutes sortes d'addictions pour assouvir sa soif insatiable.",
    hi_title: "",
    hi_content: "",
    zh_title: "Yǒng bù mǎnzú",
    zh_content: "rénlèi de ròutǐ běnxìng yǒng bù mǎnzú. Yīncǐ, rénlèi chénnì yú gè zhǒng gè yàng de shìhào, yǐ qiú mǎnzú zhè wúqíng de yěshòu."
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.INSATIABLE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.EVIL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.EVIL->INSATIABLE"
RETURN t, parent;
```
