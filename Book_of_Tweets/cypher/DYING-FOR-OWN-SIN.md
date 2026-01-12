---
name: "thought.DYING FOR OWN SIN"
alias: "Thought: Dying For Own Sin"
type: THOUGHT
en_content: "I die--not for Adam's sin but for my own; for I was in Adam when he sinned and therefore sinned with him!"
parent: "topic.HUMANITY"
tags:
- sin
- death
- responsibility
- adam
- humanity
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Sep-2011)
CREATE (t:THOUGHT {
    name: "thought.DYING FOR OWN SIN",
    alias: "Thought: Dying For Own Sin",
    parent: "topic.HUMANITY",
    tags: ['sin', 'death', 'responsibility', 'adam', 'humanity'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DYING FOR OWN SIN",
    en_title: "Dying For Own Sin",
    en_content: "I die--not for Adam's sin but for my own; for I was in Adam when he sinned and therefore sinned with him!",
    es_title: "Morir Por Mi Propio Pecado",
    es_content: "Yo muero--no por el pecado de Adán sino por el mío propio; ¡porque yo estaba en Adán cuando él pecó y por lo tanto pequé con él!",
    fr_title: "Mourir Pour Mon Propre Péché",
    fr_content: "Je meurs--non pour le péché d'Adam mais pour le mien; car j'étais en Adam quand il a péché et donc j'ai péché avec lui!",
    hi_title: "अपने पाप के लिए मरना",
    hi_content: "मैं मरता हूँ--आदम के पाप के लिए नहीं बल्कि अपने पाप के लिए; क्योंकि जब आदम ने पाप किया था तब मैं आदम में था और इसलिए मैंने उसके साथ पाप किया था!",
    zh_title: "Wei Zi Ji De Zui Er Si",
    zh_content: "Wo si--bu shi wei le Ya Dang de zui er shi wei le wo zi ji de zui; yin wei dang Ya Dang fan zui shi wo zai Ya Dang li mian, suo yi wo he ta yi qi fan zui le!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DYING FOR OWN SIN" AND c.name = "content.DYING FOR OWN SIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DYING FOR OWN SIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.DYING FOR OWN SIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >DYING FOR OWN SIN" }]->(child);
```
