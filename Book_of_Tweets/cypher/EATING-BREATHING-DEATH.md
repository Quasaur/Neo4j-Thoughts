---
name: "thought.EATING BREATHING DEATH"
alias: "Thought: Eating Breathing Death"
type: THOUGHT
parent: "topic.MORALITY"
tags:
- health
- body
- death
- morality
- healthcare
level: 3
neo4j: true
insert: true
---
# Eating Breathing Death

> [!Thought-en]
> We insist on eating and breathing death (meat and cigarettes) and then wonder why we get sick and die so fast and why healthcare costs are so high!

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Sep-2013a)
CREATE (t:THOUGHT {
    name: "thought.EATING BREATHING DEATH",
    alias: "Thought: Eating Breathing Death",
    parent: "topic.MORALITY",
    tags: ['health', 'body', 'death', 'morality', 'healthcare'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.EATING BREATHING DEATH",
    en_title: "Eating Breathing Death",
    en_content: "We insist on eating and breathing death (meat and cigarettes) and then wonder why we get sick and die so fast and why healthcare costs are so high!",
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
WHERE t.name = "thought.EATING BREATHING DEATH" AND c.name = "content.EATING BREATHING DEATH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.EATING BREATHING DEATH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.EATING BREATHING DEATH"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >EATING BREATHING DEATH" }]->(child);
```