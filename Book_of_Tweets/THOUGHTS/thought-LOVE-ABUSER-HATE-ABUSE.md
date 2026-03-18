---
type: THOUGHT
name: "thought.LOVE ABUSER HATE ABUSE"
alias: "Thought: Love Abuser Hate Abuse"
parent: "topic.THE GODHEAD"
en_content: "God loves abusers (it's the act of abuse He has a problem with)."
tags: ["love", "abuse", "character", "god", "justice"]
ptopic:
level: 1
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Feb-2012a)
CREATE (t:THOUGHT {    name: "thought.LOVE ABUSER HATE ABUSE",
    alias: "Thought: Love Abuser Hate Abuse",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'abuse', 'character', 'god', 'justice'],
    level: 1});

CREATE (c:CONTENT {
    name: "content.LOVE ABUSER HATE ABUSE",
    ctype: "THOUGHT",
    en_title: "Love Abuser Hate Abuse",
    en_content: "God loves abusers (it's the act of abuse He has a problem with).",
    es_title: "Ama al Abusador Odia el Abuso",
    es_content: "Dios ama a los abusadores (es el acto del abuso con lo que Él tiene un problema).",
    fr_title: "Aime l'Abuseur Déteste l'Abus",
    fr_content: "Dieu aime les abuseurs (c'est l'acte d'abus qu'Il condamne).",
    hi_title: "दुर्व्यवहारी से प्रेम करो दुर्व्यवहार से घृणा करो",
    hi_content: "परमेश्वर दुर्व्यवहारियों से प्रेम करता है (यह दुर्व्यवहार का कार्य है जिससे उसे समस्या है)।",
    zh_title: "Ai Shi Nue Zhe Hen E Nue Dai",
    zh_content: "Shang Di ai shi nue zhe (Ta dui shi nue xing wei you yi jian)."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.LOVE ABUSER HATE ABUSE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->LOVE ABUSER HATE ABUSE"
RETURN t, parent;
```
