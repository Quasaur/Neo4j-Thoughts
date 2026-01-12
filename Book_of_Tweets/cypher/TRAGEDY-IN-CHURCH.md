---
name: "thought.TRAGEDY IN CHURCH"
alias: "Thought: Tragedy In Church"
type: THOUGHT
en_content: "To be in church all one's life, and still go to Hell...what a tragedy!"
parent: "topic.RELIGION"
tags:
- religion
- church
- salvation
- tragedy
- deception
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Nov-2011)
CREATE (t:THOUGHT {
    name: "thought.TRAGEDY IN CHURCH",
    alias: "Thought: Tragedy In Church",
    parent: "topic.RELIGION",
    tags: ['religion', 'church', 'salvation', 'tragedy', 'deception'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.TRAGEDY IN CHURCH",
    en_title: "Tragedy In Church",
    en_content: "To be in church all one's life, and still go to Hell...what a tragedy!",
    es_title: "Tragedia En La Iglesia",
    es_content: "Estar en la iglesia toda la vida, y aún así ir al Infierno...¡qué tragedia!",
    fr_title: "Tragédie Dans L'Église",
    fr_content: "Être à l'église toute sa vie, et aller quand même en Enfer...quelle tragédie !",
    hi_title: "चर्च में त्रासदी",
    hi_content: "जीवन भर चर्च में रहना, और फिर भी नरक में जाना...कितनी त्रासदी है!",
    zh_title: "Jiaohui Li De Beiju",
    zh_content: "Yisheng dou zai jiaohui li, que reng ran qu diyu...zhe shi duome da de beiju!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.TRAGEDY IN CHURCH" AND c.name = "content.TRAGEDY IN CHURCH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TRAGEDY IN CHURCH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.TRAGEDY IN CHURCH"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >TRAGEDY IN CHURCH" }]->(child);
```
