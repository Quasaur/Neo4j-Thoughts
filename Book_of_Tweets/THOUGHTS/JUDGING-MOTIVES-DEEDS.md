---
name: "thought.JUDGING MOTIVES DEEDS"
alias: "Thought: Judging Motives Deeds"
type: THOUGHT
en_content: "While your neighbor is looking at your deeds to judge your motives, God is looking at your motives to judge your deeds!"
parent: "topic.THE GODHEAD"
tags:
- motives
- deeds
- judgment
- god
- perspective
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Jul-2012)
CREATE (t:THOUGHT {
    name: "thought.JUDGING MOTIVES DEEDS",
    alias: "Thought: Judging Motives Deeds",
    parent: "topic.THE GODHEAD",
    tags: ['motives', 'deeds', 'judgment', 'god', 'perspective'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.JUDGING MOTIVES DEEDS",
    en_title: "Judging Motives Deeds",
    en_content: "While your neighbor is looking at your deeds to judge your motives, God is looking at your motives to judge your deeds!",
    es_title: "Juzgando Motivos y Obras",
    es_content: "¡Mientras tu prójimo está mirando tus obras para juzgar tus motivos, Dios está mirando tus motivos para juzgar tus obras!",
    fr_title: "Juger les Motifs et les Actions",
    fr_content: "Alors que votre prochain regarde vos actions pour juger vos motifs, Dieu regarde vos motifs pour juger vos actions !",
    hi_title: "प्रेरणाओं और कर्मों का न्याय",
    hi_content: "जब आपका पड़ोसी आपकी प्रेरणाओं को परखने के लिए आपके कर्मों को देख रहा है, तब परमेश्वर आपके कर्मों को परखने के लिए आपकी प्रेरणाओं को देख रहा है!",
    zh_title: "Pànduàn Dòngjī Xíngwéi",
    zh_content: "Dāng nǐ de línjū zhèngzài kàn nǐ de xíngwéi lái pànduàn nǐ de dòngjī shí, Shàngdì què zài kàn nǐ de dòngjī lái pànduàn nǐ de xíngwéi!"
});

MATCH (t:THOUGHT {name: "thought.JUDGING MOTIVES DEEDS"})
MATCH (c:CONTENT {name: "content.JUDGING MOTIVES DEEDS"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.JUDGING MOTIVES DEEDS" }]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.JUDGING MOTIVES DEEDS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD->JUDGING MOTIVES DEEDS" }]->(child);
```
