---
name: "thought.ABORTION AND GOLDEN RULE"
alias: "Thought: Abortion And Golden Rule"
type: THOUGHT
parent: "topic.MORALITY"
tags:
- morality
- abortion
- golden_rule
- justice
- ethics
level: 3
neo4j: true
insert: true
---
# Abortion And Golden Rule

> [!Thought-en]
> Abortion is a violation of the Golden Rule: "Do unto others as you would have them do into you."

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Oct-2011b)
CREATE (t:THOUGHT {
    name: "thought.ABORTION AND GOLDEN RULE",
    alias: "Thought: Abortion And Golden Rule",
    parent: "topic.MORALITY",
    tags: ['morality', 'abortion', 'golden_rule', 'justice', 'ethics'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ABORTION AND GOLDEN RULE",
    en_title: "Abortion And Golden Rule",
    en_content: "Abortion is a violation of the Golden Rule: \"Do unto others as you would have them do into you.\"",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "शिखा",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ABORTION AND GOLDEN RULE" AND c.name = "content.ABORTION AND GOLDEN RULE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ABORTION AND GOLDEN RULE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.ABORTION AND GOLDEN RULE"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >ABORTION AND GOLDEN RULE" }]->(child);
```