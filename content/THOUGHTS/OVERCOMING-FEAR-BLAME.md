---
name: "thought.OVERCOMING FEAR BLAME"
alias: "Thought: Overcoming Fear Blame"
type: THOUGHT
en_content: If you keep blaming others for your fears, you'll never overcome them.
parent: topic.ATTITUDE
tags:
  - fear
  - blame
  - attitude
  - courage
  - character
level: 3
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 14-Sep-2012)
CREATE (t:THOUGHT {
    name: "thought.OVERCOMING FEAR BLAME",
    alias: "Thought: Overcoming Fear Blame",
    parent: "topic.ATTITUDE",
    tags: ['fear', 'blame', 'attitude', 'courage', 'character'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.OVERCOMING FEAR BLAME",
    en_title: "Overcoming Fear Blame",
    en_content: "If you keep blaming others for your fears, you'll never overcome them.",
    es_title: "Superando la Culpa del Miedo",
    es_content: "Si sigues culpando a otros por tus miedos, nunca los superarás.",
    fr_title: "Surmonter le Blâme de la Peur",
    fr_content: "Si tu continues à blâmer les autres pour tes peurs, tu ne les surmonteras jamais.",
    hi_title: "भय के दोषारोपण पर विजय",
    hi_content: "यदि तुम अपने भय के लिए दूसरों को दोष देते रहोगे, तो तुम कभी भी उन पर विजय नहीं पा सकोगे।",
    zh_title: "Kèfú Kǒngjù Zhǐzé",
    zh_content: "Rúguǒ nǐ yīzhí wèi nǐ de kǒngjù zérèn biérén, nǐ jiāng yǒngyuǎn wúfǎ kèfú tāmen."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.OVERCOMING FEAR BLAME" AND c.name = "content.OVERCOMING FEAR BLAME"
MERGE (t)-[:HAS_CONTENT { "name": "edge.OVERCOMING FEAR BLAME" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.OVERCOMING FEAR BLAME"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE->OVERCOMING FEAR BLAME" }]->(child);
```
