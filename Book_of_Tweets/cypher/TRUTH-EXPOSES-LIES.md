---
name: "thought.TRUTH EXPOSES LIES"
alias: "Thought: Truth Exposes Lies"
type: THOUGHT
en_content: "Truth is dangerous because it exposes lies that people believe to be true; and many would rather kill Truth than abandon their lies."
parent: "topic.TRUTH"
tags:
- truth
- lie
- deception
- danger
- reality
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 21-Oct-2012)
CREATE (t:THOUGHT {
    name: "thought.TRUTH EXPOSES LIES",
    alias: "Thought: Truth Exposes Lies",
    parent: "topic.TRUTH",
    tags: ['truth', 'lie', 'deception', 'danger', 'reality'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.TRUTH EXPOSES LIES",
    en_title: "Truth Exposes Lies",
    en_content: "Truth is dangerous because it exposes lies that people believe to be true; and many would rather kill Truth than abandon their lies.",
    es_title: "La Verdad Expone las Mentiras",
    es_content: "La Verdad es peligrosa porque expone las mentiras que las personas creen que son verdaderas; y muchos preferirían matar a la Verdad antes que abandonar sus mentiras.",
    fr_title: "La Vérité Expose les Mensonges",
    fr_content: "La Vérité est dangereuse parce qu'elle expose les mensonges que les gens croient être vrais ; et beaucoup préféreraient tuer la Vérité plutôt que d'abandonner leurs mensonges.",
    hi_title: "सत्य झूठ को उजागर करता है",
    hi_content: "सत्य खतरनाक है क्योंकि यह उन झूठों को उजागर करता है जिन्हें लोग सच मानते हैं; और कई लोग अपने झूठ छोड़ने के बजाय सत्य को मार देना पसंद करेंगे।",
    zh_title: "Zhēnlǐ Jiēlù Huǎngyán",
    zh_content: "Zhēnlǐ shì wēixiǎn de, yīnwèi tā jiēlù le rénmen xiāngxìn shì zhēnshí de huǎngyán; érqiě xǔduō rén nìngyuàn shāsǐ Zhēnlǐ yě bùyuàn fàngqì tāmen de huǎngyán."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.TRUTH EXPOSES LIES" AND c.name = "content.TRUTH EXPOSES LIES"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TRUTH EXPOSES LIES" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.TRUTH EXPOSES LIES"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >TRUTH EXPOSES LIES" }]->(child);
```
