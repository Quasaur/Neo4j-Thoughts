---
name: "thought.OPPORTUNITY FOR ANGER"
alias: "Thought: Opportunity For Anger"
type: THOUGHT
parent: "topic.ATTITUDE"
tags:
- anger
- attitude
- character
- human_nature
- emotion
level: 2
neo4j: true
insert: true
---
# Opportunity For Anger

> [!Thought-en]
> People don't need a reason to be angry...just an opportunity.

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Dec-2011)
CREATE (t:THOUGHT {
    name: "thought.OPPORTUNITY FOR ANGER",
    alias: "Thought: Opportunity For Anger",
    parent: "topic.ATTITUDE",
    tags: ['anger', 'attitude', 'character', 'human_nature', 'emotion'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.OPPORTUNITY FOR ANGER",
    en_title: "Opportunity For Anger",
    en_content: "People don't need a reason to be angry...just an opportunity.",
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
WHERE t.name = "thought.OPPORTUNITY FOR ANGER" AND c.name = "content.OPPORTUNITY FOR ANGER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.OPPORTUNITY FOR ANGER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.OPPORTUNITY FOR ANGER"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >OPPORTUNITY FOR ANGER" }]->(child);
```