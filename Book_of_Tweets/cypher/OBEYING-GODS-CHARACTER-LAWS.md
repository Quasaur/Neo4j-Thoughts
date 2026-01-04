---
name: "thought.OBEYING GODS CHARACTER LAWS"
alias: "Thought: Obeying Gods Character Laws"
type: THOUGHT
en_content: "Just because it's legal, doesn't mean it's ethical or just or fair. God doesn't expect us to obey laws that violate His Character."
parent: "topic.MORALITY"
tags:
- law
- character
- god
- ethics
- morality
level: 3
neo4j: true
insert: true
---
# Obeying Gods Character Laws

> [!Thought-en]
> Just because it's legal, doesn't mean it's ethical or just or fair. God doesn't expect us to obey laws that violate His Character.

```Cypher
// Generated from Book6E-FINAL.md (ID: 20-Sep-2013a)
CREATE (t:THOUGHT {
    name: "thought.OBEYING GODS CHARACTER LAWS",
    alias: "Thought: Obeying Gods Character Laws",
    parent: "topic.MORALITY",
    tags: ['law', 'character', 'god', 'ethics', 'morality'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.OBEYING GODS CHARACTER LAWS",
    en_title: "Obeying Gods Character Laws",
    en_content: "Just because it's legal, doesn't mean it's ethical or just or fair. God doesn't expect us to obey laws that violate His Character.",
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
WHERE t.name = "thought.OBEYING GODS CHARACTER LAWS" AND c.name = "content.OBEYING GODS CHARACTER LAWS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.OBEYING GODS CHARACTER LAWS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.OBEYING GODS CHARACTER LAWS"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >OBEYING GODS CHARACTER LAWS" }]->(child);
```