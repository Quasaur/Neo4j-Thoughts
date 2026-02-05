---
name: "thought.DISABILITY OF SPIRIT"
alias: "Thought: Disability Of Spirit"
type: THOUGHT
en_content: "The inability to perceive God's Immediate Presence is a greater disability than not being able to walk or see."
parent: "topic.SPIRITUALITY"
tags:
- presence
- perception
- disability
- spirituality
- god
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 11-Oct-2013)
CREATE (t:THOUGHT {
    name: "thought.DISABILITY OF SPIRIT",
    alias: "Thought: Disability Of Spirit",
    parent: "topic.SPIRITUALITY",
    tags: ['presence', 'perception', 'disability', 'spirituality', 'god'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DISABILITY OF SPIRIT",
    en_title: "Disability Of Spirit",
    en_content: "The inability to perceive God's Immediate Presence is a greater disability than not being able to walk or see.",
    es_title: "Discapacidad del Espíritu",
    es_content: "La incapacidad de percibir la Presencia Inmediata de Dios es una discapacidad mayor que no poder caminar o ver.",
    fr_title: "Handicap de l'Esprit",
    fr_content: "L'incapacité de percevoir la Présence Immédiate de Dieu est un handicap plus grand que de ne pas pouvoir marcher ou voir.",
    hi_title: "आत्मा की अशक्तता",
    hi_content: "परमेश्वर की तत्काल उपस्थिति को महसूस न कर पाना चलने या देखने में असमर्थ होने से बड़ी अशक्तता है।",
    zh_title: "Líng de cánjí  líng de cán jí",
    zh_content: "Wúfǎ gǎnshòu Shàngdì jítǐ línzài shì bǐ bù néng zǒulù huò kànjiàn gèng dà de cánjí.  wú fǎ gǎn shòu shàng dì jí shí lín zài shì bǐ bù néng zǒu lù huò kàn jiàn gèng dà de cán jí 。"
});

MATCH (t:THOUGHT {name: "thought.DISABILITY OF SPIRIT"})
MATCH (c:CONTENT {name: "content.DISABILITY OF SPIRIT"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.DISABILITY OF SPIRIT" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.DISABILITY OF SPIRIT"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY->DISABILITY OF SPIRIT" }]->(child);
```
