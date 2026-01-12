---
name: "thought.BEGINNING OF MISERY"
alias: "Thought: Beginning Of Misery"
type: THOUGHT
en_content: "Misery began when some idiot decided he was more important than God."
parent: "topic.HUMANITY"
tags:
- misery
- pride
- humanity
- origin
- god
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Jan-2012)
CREATE (t:THOUGHT {
    name: "thought.BEGINNING OF MISERY",
    alias: "Thought: Beginning Of Misery",
    parent: "topic.HUMANITY",
    tags: ['misery', 'pride', 'humanity', 'origin', 'god'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.BEGINNING OF MISERY",
    en_title: "Beginning Of Misery",
    en_content: "Misery began when some idiot decided he was more important than God.",
    es_title: "El Comienzo de la Miseria",
    es_content: "La miseria comenzó cuando algún idiota decidió que era más importante que Dios.",
    fr_title: "Le Début de la Misère",
    fr_content: "La misère a commencé quand un idiot a décidé qu'il était plus important que Dieu.",
    hi_title: "दुख की शुरुआत",
    hi_content: "दुख तब शुरू हुआ जब किसी मूर्ख ने यह तय किया कि वह परमेश्वर से अधिक महत्वपूर्ण था।",
    zh_title: "Kǔnàn de kāishǐ 苦难的开始",
    zh_content: "Dāng mǒu gè báichī juédìng tā bǐ Shàngdì gèng zhòngyào shí, kǔnàn jiù kāishǐ le. 当某个白痴决定他比上帝更重要时，苦难就开始了。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.BEGINNING OF MISERY" AND c.name = "content.BEGINNING OF MISERY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.BEGINNING OF MISERY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.BEGINNING OF MISERY"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >BEGINNING OF MISERY" }]->(child);
```
