---
name: "thought.LOVE ABUSER HATE ABUSE"
alias: "Thought: Love Abuser Hate Abuse"
type: THOUGHT
en_content: "God loves abusers (it's the act of abuse He has a problem with)."
parent: "topic.THE GODHEAD"
tags:
- love
- abuse
- character
- god
- justice
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Feb-2012a)
CREATE (t:THOUGHT {
    name: "thought.LOVE ABUSER HATE ABUSE",
    alias: "Thought: Love Abuser Hate Abuse",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'abuse', 'character', 'god', 'justice'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.LOVE ABUSER HATE ABUSE",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.LOVE ABUSER HATE ABUSE" AND c.name = "content.LOVE ABUSER HATE ABUSE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LOVE ABUSER HATE ABUSE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.LOVE ABUSER HATE ABUSE"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >LOVE ABUSER HATE ABUSE" }]->(child);
```
