---
name: "thought.MODERN PROPAGANDA"
alias: "Thought: Modern Propaganda"
type: THOUGHT
en_content: "Modern Propaganda (good vampires, pious werewolves, virtuous mediums) has perpetuated humanity's slide into Satan's occult domain."
parent: "topic.EVIL"
tags:
- evil
- propaganda
- occult
- deception
- discernment
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 03-Sep-2010a)
CREATE (t:THOUGHT {
    name: "thought.MODERN PROPAGANDA",
    alias: "Thought: Modern Propaganda",
    parent: "topic.EVIL",
    tags: ['evil', 'propaganda', 'occult', 'deception', 'discernment'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.MODERN PROPAGANDA",
    en_title: "Modern Propaganda",
    en_content: "Modern Propaganda (good vampires, pious werewolves, virtuous mediums) has perpetuated humanity's slide into Satan's occult domain.",
    es_title: "Publicidad moderna",
    es_content: "La propaganda moderna (buenos vampiros, hombres lobo piadosos, médiums virtuosos) ha perpetuado el deslizamiento de la humanidad hacia el dominio oculto de Satanás.",
    fr_title: "Publicité moderne",
    fr_content: "La propagande moderne (bons vampires, loups-garous pieux, médiums vertueux) a perpétué le glissement de l'humanité vers le domaine occulte de Satan.",
    hi_title: "आधुनिक विज्ञापन",
    hi_content: "आधुनिक प्रचार (अच्छे पिशाच, पवित्र वेयरवोल्स, अच्छे माध्यम) ने मानवता को शैतान के गुप्त क्षेत्र में धकेल दिया है।",
    zh_title: "现代广告",
    zh_content: "现代宣传（善良的吸血鬼、虔诚的狼人、善良的媒介）使人类永远滑入撒旦的神秘领域。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.MODERN PROPAGANDA" AND c.name = "content.MODERN PROPAGANDA"
MERGE (t)-[:HAS_CONTENT { "name": "edge.MODERN PROPAGANDA" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.MODERN PROPAGANDA"
MERGE (parent)-[:HAS_THOUGHT { "name": "EVIL >MODERN PROPAGANDA" }]->(child);
```
