---
name: "thought.FUTURE FOR ATHEISTS"
alias: "Thought: Future For Atheists"
type: THOUGHT
en_content: "Is there any future for a species that so despises its Creator as to announce that He doesn't exist?"
parent: "topic.PHILOSOPHY"
tags:
- future
- creator
- atheism
- philosophy
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Nov-2013)
CREATE (t:THOUGHT {
    name: "thought.FUTURE FOR ATHEISTS",
    alias: "Thought: Future For Atheists",
    parent: "topic.PHILOSOPHY",
    tags: ['future', 'creator', 'atheism', 'philosophy'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FUTURE FOR ATHEISTS",
    en_title: "Future For Atheists",
    en_content: "Is there any future for a species that so despises its Creator as to announce that He doesn't exist?",
    es_title: "Futuro Para Los Ateos",
    es_content: "¿Hay algún futuro para una especie que tanto desprecia a su Creador como para anunciar que Él no existe?",
    fr_title: "Avenir Pour Les Athées",
    fr_content: "Y a-t-il un avenir pour une espèce qui méprise tant son Créateur au point d'annoncer qu'Il n'existe pas ?",
    hi_title: "नास्तिकों के लिए भविष्य",
    hi_content: "क्या उस प्रजाति का कोई भविष्य है जो अपने सृष्टिकर्ता से इतनी घृणा करती है कि वह घोषणा करती है कि वह अस्तित्व में नहीं है?",
    zh_title: "Wu shen lun zhe de wei lai",
    zh_content: "Yi ge wu shi qi zao wu zhu zhi shen zhi xuan bu ta bu cun zai de wu zhong, hai you shen me wei lai ma?"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FUTURE FOR ATHEISTS" AND c.name = "content.FUTURE FOR ATHEISTS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FUTURE FOR ATHEISTS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.FUTURE FOR ATHEISTS"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >FUTURE FOR ATHEISTS" }]->(child);
```
