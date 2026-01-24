---
name: "thought.PRAYER BEFORE SPEECH"
alias: "Thought: Prayer Before Speech"
type: THOUGHT
en_content: "It is inappropriate to speak out on what we don't pray out."
parent: "topic.SPIRITUALITY"
tags:
- prayer
- speech
- spirituality
- integrity
- character
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Aug-2012a)
CREATE (t:THOUGHT {
    name: "thought.PRAYER BEFORE SPEECH",
    alias: "Thought: Prayer Before Speech",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'speech', 'spirituality', 'integrity', 'character'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.PRAYER BEFORE SPEECH",
    en_title: "Prayer Before Speech",
    en_content: "It is inappropriate to speak out on what we don't pray out.",
    es_title: "Oración Antes de Hablar",
    es_content: "Es inapropiado hablar sobre lo que no oramos.",
    fr_title: "Prière Avant la Parole",
    fr_content: "Il est inapproprié de s'exprimer sur ce pour quoi nous ne prions pas.",
    hi_title: "वाणी से पूर्व प्रार्थना",
    hi_content: "जिस विषय पर हम प्रार्थना नहीं करते, उस पर बोलना अनुचित है।",
    zh_title: "Yán Qián Qí Dǎo",
    zh_content: "Duì yú wǒmen méiyǒu qídǎo guò de shìqíng, bùyí gōngkāi fāyán."
});

MATCH (t:THOUGHT {name: "thought.PRAYER BEFORE SPEECH"})
MATCH (c:CONTENT {name: "content.PRAYER BEFORE SPEECH"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.PRAYER BEFORE SPEECH" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.PRAYER BEFORE SPEECH"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY->PRAYER BEFORE SPEECH" }]->(child);
```
