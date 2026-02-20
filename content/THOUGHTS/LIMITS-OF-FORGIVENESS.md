---
name: "thought.LIMITS OF FORGIVENESS"
alias: "Thought: Limits Of Forgiveness"
type: THOUGHT
parent: "topic.GRACE"
en_content: "The only people God doesn't forgive are those who don't want to be forgiven."
tags:
- forgiveness
- grace
- repentance
- will
- mercy
level: 3
neo4j: true
ptopic: "[[topic-GRACE]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 25-Aug-2010)
CREATE (t:THOUGHT {
    name: "thought.LIMITS OF FORGIVENESS",
    alias: "Thought: Limits Of Forgiveness",
    parent: "topic.GRACE",
    tags: ['forgiveness', 'grace', 'repentance', 'will', 'mercy'],
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
    zh_title: "kuān shù de xiàn dù",
    zh_content: "shén wéi yī bù ráo shù de rén shì nà xiē bù xiǎng bèi ráo shù de rén 。"
});

MATCH (t:THOUGHT {name: "thought.LIMITS OF FORGIVENESS"})
MATCH (c:CONTENT {name: "content.LIMITS OF FORGIVENESS"})
MERGE (t)-[:HAS_CONTENT { "name": "t.edge.LIMITS OF FORGIVENESS" }]->(c);

MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:THOUGHT {name: "thought.LIMITS OF FORGIVENESS"})
MERGE (parent)-[:HAS_THOUGHT { "name": "t.edge.GRACE->LIMITS OF FORGIVENESS" }]->(child);
```
