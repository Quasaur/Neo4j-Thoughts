---
name: "thought.ATTRACTION TO FORBIDDEN"
alias: "Thought: Attraction To Forbidden"
type: THOUGHT
en_content: "What attracts us to the forbidden? Sin."
parent: "topic.MORALITY"
tags:
- sin
- attraction
- forbidden
- morality
- temptation
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Oct-2011d)
CREATE (t:THOUGHT {
    name: "thought.ATTRACTION TO FORBIDDEN",
    alias: "Thought: Attraction To Forbidden",
    parent: "topic.MORALITY",
    tags: ['sin', 'attraction', 'forbidden', 'morality', 'temptation'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ATTRACTION TO FORBIDDEN",
    en_title: "Attraction To Forbidden",
    en_content: "What attracts us to the forbidden? Sin.",
    es_title: "Atracción a lo Prohibido",
    es_content: "¿Qué nos atrae a lo prohibido? El pecado.",
    fr_title: "Attraction pour l'Interdit",
    fr_content: "Qu'est-ce qui nous attire vers l'interdit ? Le péché.",
    hi_title: "वर्जित की ओर आकर्षण",
    hi_content: "वर्जित की ओर हमें क्या आकर्षित करता है? पाप।",
    zh_title: "Duì jìnjì de xīyǐn lì 对禁忌的吸引力",
    zh_content: "Shì shénme xīyǐn wǒmen bèi jìnjì zhī wù? Zuìzhèng. 是什么吸引我们被禁忌之物？罪政。"
});

MATCH (t:THOUGHT {name: "thought.ATTRACTION TO FORBIDDEN"})
MATCH (c:CONTENT {name: "content.ATTRACTION TO FORBIDDEN"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.ATTRACTION TO FORBIDDEN" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.ATTRACTION TO FORBIDDEN"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >ATTRACTION TO FORBIDDEN" }]->(child);
```
