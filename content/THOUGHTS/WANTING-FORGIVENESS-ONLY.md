---
name: "thought.WANTING FORGIVENESS ONLY"
alias: "Thought: Wanting Forgiveness Only"
type: THOUGHT
en_content: We want to be forgiven, but we don't want to forgive...how disgusting.
parent: topic.LOVE
tags:
  - forgiveness
  - hypocrisy
  - attitude
  - character
  - disgusting
level: 3
neo4j: true
ptopic: "[[topic-LOVE]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jul-2013c)
CREATE (t:THOUGHT {
    name: "thought.WANTING FORGIVENESS ONLY",
    alias: "Thought: Wanting Forgiveness Only",
    parent: "topic.ATTITUDE",
    tags: ['forgiveness', 'hypocrisy', 'attitude', 'character', 'disgusting'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.WANTING FORGIVENESS ONLY",
    en_title: "Wanting Forgiveness Only",
    en_content: "We want to be forgiven, but we don't want to forgive...how disgusting.",
    es_title: "Queriendo Solo el Perdón",
    es_content: "Queremos ser perdonados, pero no queremos perdonar...qué repugnante.",
    fr_title: "Vouloir Seulement le Pardon",
    fr_content: "Nous voulons être pardonnés, mais nous ne voulons pas pardonner...comme c'est dégoûtant.",
    hi_title: "केवल क्षमा चाहना",
    hi_content: "हम क्षमा पाना चाहते हैं, लेकिन हम क्षमा करना नहीं चाहते...कितना घिनौना।",
    zh_title: "Zhi Xiang Yao Kuanshu",
    zh_content: "Women xiang bei kuanshu, dan women bu xiang kuanshu bieren...duo me eling."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.WANTING FORGIVENESS ONLY" AND c.name = "content.WANTING FORGIVENESS ONLY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.WANTING FORGIVENESS ONLY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.WANTING FORGIVENESS ONLY"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE->WANTING FORGIVENESS ONLY" }]->(child);
```
