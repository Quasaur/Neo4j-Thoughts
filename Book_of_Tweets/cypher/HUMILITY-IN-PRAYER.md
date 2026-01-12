---
name: "thought.HUMILITY IN PRAYER"
alias: "Thought: Humility In Prayer"
type: THOUGHT
en_content: "Prayer needs no Humility to be spoken, but no prayer is heard without it."
parent: "topic.SPIRITUALITY"
tags:
- prayer
- humility
- spirituality
- connection
- truth
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-May-2012)
CREATE (t:THOUGHT {
    name: "thought.HUMILITY IN PRAYER",
    alias: "Thought: Humility In Prayer",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'humility', 'spirituality', 'connection', 'truth'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HUMILITY IN PRAYER",
    en_title: "Humility In Prayer",
    en_content: "Prayer needs no Humility to be spoken, but no prayer is heard without it.",
    es_title: "Humildad en la Oración",
    es_content: "La oración no necesita humildad para ser pronunciada, pero ninguna oración es escuchada sin ella.",
    fr_title: "Humilité dans la Prière",
    fr_content: "La prière n'a pas besoin d'humilité pour être prononcée, mais aucune prière n'est entendue sans elle.",
    hi_title: "प्रार्थना में विनम्रता",
    hi_content: "प्रार्थना को बोलने के लिए विनम्रता की आवश्यकता नहीं है, परंतु इसके बिना कोई प्रार्थना सुनी नहीं जाती।",
    zh_title: "Qídǎo Zhōng de Qiānbēi",
    zh_content: "Qídǎo bù xūyào qiānbēi jiù néng shuōchū, dàn méiyǒu qiānbēi jiù méiyǒu qídǎo bèi tīngjiàn."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HUMILITY IN PRAYER" AND c.name = "content.HUMILITY IN PRAYER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HUMILITY IN PRAYER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.HUMILITY IN PRAYER"
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >HUMILITY IN PRAYER" }]->(child);
```
