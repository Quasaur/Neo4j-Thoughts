---
name: "thought.SPIRIT OF CHRIST ENCOUNTER"
alias: "Thought: Spirit Of Christ Encounter"
type: THOUGHT
en_content: "The greatest moment of my existence was being swallowed up by the Spirit of Christ...all I want is to go back (or forward) to that moment."
parent: "topic.SPIRITUALITY"
tags:
- spirit
- encounter
- christ
- joy
- presence
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Nov-2011b)
CREATE (t:THOUGHT {
    name: "thought.SPIRIT OF CHRIST ENCOUNTER",
    alias: "Thought: Spirit Of Christ Encounter",
    parent: "topic.SPIRITUALITY",
    tags: ['spirit', 'encounter', 'christ', 'joy', 'presence'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SPIRIT OF CHRIST ENCOUNTER",
    en_title: "Spirit Of Christ Encounter",
    en_content: "The greatest moment of my existence was being swallowed up by the Spirit of Christ...all I want is to go back (or forward) to that moment.",
    es_title: "Encuentro con el Espíritu de Cristo",
    es_content: "El momento más grandioso de mi existencia fue ser absorbido por el Espíritu de Cristo...todo lo que quiero es regresar (o avanzar) a ese momento.",
    fr_title: "Rencontre avec l'Esprit du Christ",
    fr_content: "Le plus grand moment de mon existence fut d'être englouti par l'Esprit du Christ...tout ce que je veux c'est retourner (ou avancer) vers ce moment.",
    hi_title: "मसीह की आत्मा से मुलाकात",
    hi_content: "मेरे अस्तित्व का सबसे महान क्षण था मसीह की आत्मा में समा जाना...मैं केवल उस क्षण में वापस जाना (या आगे बढ़ना) चाहता हूँ।",
    zh_title: "Jīdū zhī Líng xiāng yù",
    zh_content: "Wǒ cúnzài zhōng zuì wěidà de shíkè jiùshì bèi Jīdū zhī Líng tūnmò...wǒ suǒ xiǎng de jiùshì huí dào (huò qiánjìn dào) nàgè shíkè."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SPIRIT OF CHRIST ENCOUNTER" AND c.name = "content.SPIRIT OF CHRIST ENCOUNTER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SPIRIT OF CHRIST ENCOUNTER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.SPIRIT OF CHRIST ENCOUNTER"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >SPIRIT OF CHRIST ENCOUNTER" }]->(child);
```
