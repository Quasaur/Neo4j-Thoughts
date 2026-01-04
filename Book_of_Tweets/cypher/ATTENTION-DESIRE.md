---
name: "thought.ATTENTION DESIRE"
alias: "Thought: Attention Desire"
type: THOUGHT
parent: "topic.ATTITUDE"
tags:
- attitude
- attention
- human_nature
- desire
- pride
level: 2
neo4j: true
insert: true
---
# Attention Desire

> [!Thought-en]
> I only want your attention when you don't want to give it to me.

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Aug-2011a)
CREATE (t:THOUGHT {
    name: "thought.ATTENTION DESIRE",
    alias: "Thought: Attention Desire",
    parent: "topic.ATTITUDE",
    tags: ['attitude', 'attention', 'human_nature', 'desire', 'pride'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.ATTENTION DESIRE",
    en_title: "Attention Desire",
    en_content: "I only want your attention when you don't want to give it to me.",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "विट्गेन्स्टाइन की खोज",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ATTENTION DESIRE" AND c.name = "content.ATTENTION DESIRE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ATTENTION DESIRE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.ATTENTION DESIRE"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >ATTENTION DESIRE" }]->(child);
```