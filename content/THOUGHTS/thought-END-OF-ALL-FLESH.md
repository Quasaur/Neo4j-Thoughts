---
type: THOUGHT
name: "thought.END OF ALL FLESH"
alias: "Thought: End Of All Flesh"
parent: "topic.DIVINE SOVEREIGNTY"
en_content: "\"
 es_title: "Fin de toda carne"
 es_content: ""
 fr_title: "Fin de toute chair"
 fr_content: ""
 hi_title: "सभी मांस का अंत"
 hi_content: ""
 zh_title: "suǒ yǒu ròu tǐ de zhōng jié"
 zh_content: ""
tags: ["judgment", "sovereignty", "end_times", "justice", "divinity"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.END OF ALL FLESH",
    alias: "Thought: End Of All Flesh",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ["judgment", "sovereignty", "end_times", "justice", "divinity"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.END",
    ctype: "THOUGHT",
    en_title: "End Of All Flesh",
    en_content: "\",
 es_title: "Fin de toda carne",
 es_content: "",
 fr_title: "Fin de toute chair",
 fr_content: "",
 hi_title: "सभी मांस का अंत",
 hi_content: "",
 zh_title: "suǒ yǒu ròu tǐ de zhōng jié",
 zh_content: ""
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.END OF ALL FLESH" AND c.name = "content.END"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.END OF ALL FLESH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.END OF ALL FLESH"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.DIVINE SOVEREIGNTY->END OF ALL FLESH"}]->(child);