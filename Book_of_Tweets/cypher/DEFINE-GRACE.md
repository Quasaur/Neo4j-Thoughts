---
name: "thought.DEFINE GRACE"
alias: "Thought: Define Grace"
type: THOUGHT
en_content: "GRACE is God saying \"I like you! I'm gonna cut you a break!\""
parent: "topic.GRACE"
tags:
- grace
- mercy
- love
- salvation
- favor
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Apr-2011)
CREATE (t:THOUGHT {
    name: "thought.DEFINE GRACE",
    alias: "Thought: Define Grace",
    parent: "topic.GRACE",
    tags: ['grace', 'mercy', 'love', 'salvation', 'favor'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DEFINE GRACE",
    en_title: "Define Grace",
    en_content: "GRACE is God saying \"I like you! I'm gonna cut you a break!\"",
    es_title: "Definir Gracia",
    es_content: "La GRACIA es Dios diciendo \"¡Me gustas! ¡Voy a darte un respiro!\"",
    fr_title: "Définir la Grâce",
    fr_content: "La GRÂCE est Dieu disant \"Je t'aime bien ! Je vais te donner une chance !\"",
    hi_title: "अनुग्रह को परिभाषित करें",
    hi_content: "अनुग्रह भगवान का कहना है \"मुझे तुम पसंद हो! मैं तुम्हें एक मौका दूंगा!\"",
    zh_title: "Dìngyì ēnhuì",
    zh_content: "Ēnhuì shì shàngdì shuō \"Wǒ xǐhuān nǐ! Wǒ yào gěi nǐ yīgè jīhuì!\""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DEFINE GRACE" AND c.name = "content.DEFINE GRACE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DEFINE GRACE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.DEFINE GRACE"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >DEFINE GRACE" }]->(child);
```
