---
name: "thought.THE_END_OF_EVIL"
alias: "Thought: THE END OF EVIL"
type: THOUGHT
parent: "topic.EVIL"
en_content: "The Day is coming when evil will no longer exist."
tags:
- day
- evil
- cessation
- hope
- future
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.THE_END_OF_EVIL",
    alias: "Thought: The End of Evil",
    parent: "topic.EVIL",
    tags: ["day", "evil", "cessation", "hope", "future"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.THE_END_OF_EVIL",
    en_title: "The End of Evil",
    en_content: "The Day is coming when evil will no longer exist.",
	es_title: "EL FIN DEL MAL",
    es_content: "Se acerca el día en que el mal ya no existirá.",
	fr_title: "LA FIN DU MAL",
    fr_content: "Le jour vient où le mal n’existera plus.",
	hi_title: "बुराई का अंत",
    hi_content: "वह दिन आ रहा है जब बुराई का अस्तित्व नहीं रहेगा।",
	zh_title: "xié è de zhōng jié",
    zh_content: "The Day is coming when evil will no longer exist."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE_END_OF_EVIL" AND c.name = "content.THE_END_OF_EVIL"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.THE_END_OF_EVIL"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.THE_END_OF_EVIL"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.EVIL->THE_END_OF_EVIL"}]->(child);
```
