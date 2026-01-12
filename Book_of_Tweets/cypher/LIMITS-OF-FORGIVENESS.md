---
name: "thought.LIMITS OF FORGIVENESS"
alias: "Thought: Limits Of Forgiveness"
type: THOUGHT
en_content: "The only people God doesn't forgive are those who don't want to be forgiven."
parent: "topic.GRACE"
tags:
- forgiveness
- grace
- repentance
- will
- mercy
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Aug-2010)
CREATE (t:THOUGHT {
    name: "thought.LIMITS OF FORGIVENESS",
    alias: "Thought: Limits Of Forgiveness",
    parent: "topic.GRACE",
    tags: ['forgiveness', 'grace', 'repentance', 'will', 'mercy'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.LIMITS OF FORGIVENESS",
    en_title: "Limits Of Forgiveness",
    en_content: "The only people God doesn't forgive are those who don't want to be forgiven.",
    es_title: "Límites del perdón",
    es_content: "Las únicas personas que Dios no perdona son aquellas que no quieren ser perdonadas.",
    fr_title: "Limites du pardon",
    fr_content: "Les seules personnes que Dieu ne pardonne pas sont celles qui ne veulent pas être pardonnées.",
    hi_title: "क्षमा की सीमा",
    hi_content: "केवल उन्हीं लोगों को ईश्वर क्षमा नहीं करता है जो क्षमा नहीं चाहते हैं।",
    zh_title: "宽恕的限度",
    zh_content: "神唯一不饶恕的人是那些不想被饶恕的人。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.LIMITS OF FORGIVENESS" AND c.name = "content.LIMITS OF FORGIVENESS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LIMITS OF FORGIVENESS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.LIMITS OF FORGIVENESS"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >LIMITS OF FORGIVENESS" }]->(child);
```
