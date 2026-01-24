---
name: "thought.HUMAN_MERCY"
alias: "Thought: HUMAN MERCY"
type: THOUGHT
parent: topic.ATTITUDE
tags:
- mercy
- submission
- faithfulness
- obedience
- jesuschrist
neo4j: true
ptopic: "[[topic-ATTITUDE]]"
level: 3
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.HUMAN_MERCY",
    alias: "Thought: HUMAN MERCY",
    parent: "topic.ATTITUDE",
    tags: ["mercy", "submission", "faithfulness", "obedience", "jesuschrist"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.HUMAN_MERCY",
    en_title: "HUMAN MERCY",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HUMAN_MERCY" AND c.name = "content.HUMAN_MERCY"
MERGE (t)-[:HAS_CONTENT {name: "edge.HUMAN_MERCY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.HUMAN_MERCY"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ATTITUDE->HUMAN_MERCY"}]->(child);
```
