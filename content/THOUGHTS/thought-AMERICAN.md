---
type: THOUGHT
name: "thought.AMERICAN"
alias: "Thought: American"
parent: "topic.POLITICAL-SCIENCE"
tags: ["nationalism", "american", "addiction", "dependency", "codependency"]
ptopic: "[[topic-POLITICAL-SCIENCE]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.AMERICAN",
    alias: "Thought: American",
    parent: "topic.POLITICAL-SCIENCE",
    tags: ["nationalism", "american", "addiction", "dependency", "codependency"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.AMERICAN",
    ctype: "THOUGHT",
    en_title: "American",
 es_title: "AMERICANO",
 fr_title: "AMÉRICAIN",
 hi_title: "अमेरिकी",
 zh_title: "měi guó rén",
    en_content: "",
 es_content: "No eres realmente estadounidense a menos que seas adicto a algo.",
 fr_content: "Vous n’êtes pas vraiment américain à moins d’être accro à quelque chose.",
 hi_content: "आप वास्तव में अमेरिकी नहीं हैं जब तक कि आप किसी चीज़ के आदी न हों।",
 zh_content: "chú fēi nǐ duì mǒu jiàn shì shàng yǐn ， fǒu zé nǐ jiù bú shì zhēn zhèng de měi guó rén 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.AMERICAN" AND c.name = "content.AMERICAN"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.AMERICAN"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.POLITICAL-SCIENCE" AND child.name = "thought.AMERICAN"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.POLITICAL-SCIENCE->AMERICAN"}]->(child);
```