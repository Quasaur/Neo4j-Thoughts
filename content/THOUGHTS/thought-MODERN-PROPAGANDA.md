---
type: THOUGHT
name: "thought.MODERN PROPAGANDA"
alias: "Thought: Modern Propaganda"
parent: "topic.EVIL"
en_content: "Modern Propaganda (good vampires, pious werewolves, virtuous mediums) has perpetuated humanity's slide into Satan's occult domain."
tags: ["evil", "propaganda", "occult", "deception", "discernment"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.MODERN PROPAGANDA",
    alias: "Thought: Modern Propaganda",
    parent: "topic.EVIL",
    tags: ['evil', 'propaganda', 'occult', 'deception', 'discernment'],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.MODERN PROPAGANDA",
    ctype: "THOUGHT",
    en_title: "Modern Propaganda",
    en_content: "Modern Propaganda (good vampires, pious werewolves, virtuous mediums) has perpetuated humanity's slide into Satan's occult domain.",
    es_title: "Publicidad moderna",
    es_content: "La propaganda moderna (buenos vampiros, hombres lobo piadosos, médiums virtuosos) ha perpetuado el deslizamiento de la humanidad hacia el dominio oculto de Satanás.",
    fr_title: "Publicité moderne",
    fr_content: "La propagande moderne (bons vampires, loups-garous pieux, médiums vertueux) a perpétué le glissement de l'humanité vers le domaine occulte de Satan.",
    hi_title: "आधुनिक विज्ञापन",
    hi_content: "आधुनिक प्रचार (अच्छे पिशाच, पवित्र वेयरवोल्स, अच्छे माध्यम) ने मानवता को शैतान के गुप्त क्षेत्र में धकेल दिया है।",
    zh_title: "xiàn dài guǎng gào",
    zh_content: "xiàn dài xuān chuán （ shàn liáng de xī xuè guǐ 、 qián chéng de láng rén 、 shàn liáng de méi jiè ） shǐ rén lèi yǒng yuǎn huá rù sā dàn de shén mì lǐng yù 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.MODERN PROPAGANDA"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.EVIL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.EVIL->MODERN PROPAGANDA"
RETURN t, parent;
```
