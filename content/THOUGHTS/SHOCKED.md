---
name: "thought.SHOCKED"
alias: "Thought: Shocked"
type: THOUGHT
parent: "topic.EVIL"
en_content: "It's a strange thing: we are all sinners, but we are \"shocked\" and \"appalled\" when one of us sins!"
tags:
- hypocrisy
- shocked
- appalled
- sinner
- sinning
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SHOCKED",
    alias: "Thought: SHOCKED",
    parent: "topic.EVIL",
    tags: ["hypocrisy", "shocked", "appalled", "sinner", "sinning"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.SHOCKED",
    en_title: "Shocked",
    en_content: "It's a strange thing: we are all sinners, but we are \"shocked\" and \"appalled\" when one of us sins!",
    es_title: "Conmocionado",
    es_content: "Es extraño: todos somos pecadores, pero nos sentimos “conmocionados” y “horrorizados” cuando alguno de nosotros peca.",
	fr_title: "Choqués",
    fr_content: "C'est étrange : nous sommes tous pécheurs, mais nous sommes « choqués » et « consternés » quand l'un d'entre nous pèche !",
	hi_title: "हैरान",
    hi_content: "यह एक अजीब बात है: हम सभी पापी हैं, लेकिन जब हममें से कोई पाप करता है तो हम \"हैरान\" और \"हैरान\" हो जाते हैं!",
	zh_title: "Zhènjīng",
    zh_content: "zhè hěn qíguài: Wǒmen dōu shì zuìrén, dàn dāng wǒmen zhōng yǒurén fànzuì shí, wǒmen què gǎndào \“zhènjīng\” hé \“fènkǎi\”!",
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SHOCKED" AND c.name = "content.SHOCKED"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.SHOCKED"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.SHOCKED"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.EVIL->SHOCKED"}]->(child);
```