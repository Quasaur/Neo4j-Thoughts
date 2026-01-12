---
name: "thought.FORGIVING THE FUTURE"
alias: "Thought: Forgiving The Future"
type: THOUGHT
en_content: "We're so busy struggling to forgive the past we never consider the necessity of forgiving the future."
parent: "topic.GRACE"
tags:
- forgiveness
- future
- past
- grace
- healing
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Apr-2011)
CREATE (t:THOUGHT {
    name: "thought.FORGIVING THE FUTURE",
    alias: "Thought: Forgiving The Future",
    parent: "topic.GRACE",
    tags: ['forgiveness', 'future', 'past', 'grace', 'healing'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FORGIVING THE FUTURE",
    en_title: "Forgiving The Future",
    en_content: "We're so busy struggling to forgive the past we never consider the necessity of forgiving the future.",
    es_title: "Perdonando el Futuro",
    es_content: "Estamos tan ocupados luchando por perdonar el pasado que nunca consideramos la necesidad de perdonar el futuro.",
    fr_title: "Pardonner l'Avenir",
    fr_content: "Nous sommes si occupés à lutter pour pardonner le passé que nous n'envisageons jamais la nécessité de pardonner l'avenir.",
    hi_title: "भविष्य को क्षमा करना",
    hi_content: "हम अतीत को क्षमा करने के संघर्ष में इतने व्यस्त हैं कि हम भविष्य को क्षमा करने की आवश्यकता पर कभी विचार नहीं करते।",
    zh_title: "Kuanshu Weilai",
    zh_content: "Women mangyu zhengzha kuanshu guoqu, que conglai meiyou kaolü kuanshu weilai de biyaoxing."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FORGIVING THE FUTURE" AND c.name = "content.FORGIVING THE FUTURE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FORGIVING THE FUTURE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.FORGIVING THE FUTURE"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >FORGIVING THE FUTURE" }]->(child);
```
