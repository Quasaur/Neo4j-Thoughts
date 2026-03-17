---
type: THOUGHT
name: "thought.HUMAN MERCY"
alias: "Thought: Human Mercy"
parent: "topic.ATTITUDE"
en_content: "Oh Most Holy Father of spirits, please grant me the Grace to be merciful to Your Feelings through my submission and faithful obedience to Your Only-Begotten Son The Messiah!"
tags: ["mercy", "submission", "faithfulness", "obedience", "jesus_christ"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.HUMAN MERCY",
    alias: "Thought: Human Mercy",
    parent: "topic.ATTITUDE",
    tags: ["mercy", "submission", "faithfulness", "obedience", "jesus_christ"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HUMAN MERCY",
    ctype: "THOUGHT",
    en_title: "Human Mercy",
    en_content: "Oh Most Holy Father of spirits, please grant me the Grace to be merciful to Your Feelings through my submission and faithful obedience to Your Only-Begotten Son The Messiah!",
    es_title: "MISERICORDIA HUMANA",
    es_content: "¡Oh Santísimo Padre de los espíritus, por favor concédeme la Gracia de ser misericordioso con Tus Sentimientos a través de mi sumisión y fiel obediencia a Tu Unigénito Hijo El Mesías!",
    fr_title: "MISÉRICORDE HUMAINE",
    fr_content: "Oh Très Saint Père des esprits, accorde-moi s'il te plaît la Grâce d'être miséricordieux envers Tes Sentiments par ma soumission et ma fidèle obéissance à Ton Fils Unique, le Messie !",
    hi_title: "मानव दया",
    hi_content: "हे आत्माओं के परम पवित्र पिता, कृपया मुझे आपके इकलौते पुत्र मसीहा के प्रति समर्पण और वफ़ादार आज्ञाकारिता के माध्यम से आपकी भावनाओं के प्रति दयालु होने की कृपा प्रदान करें!",
    zh_title: "rén xìng de lián mǐn",
    zh_content: "ō ， zhì shèng wàn líng zhī fù ， qǐng cì yǔ wǒ ēn diǎn ， tōng guò wǒ duì nín dú shēng zi mí sài yà de shùn fú hé zhōng shí fú cóng ， lái lián mǐn nín de gǎn shòu ！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.HUMAN MERCY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->HUMAN MERCY"
RETURN t, parent;
```
