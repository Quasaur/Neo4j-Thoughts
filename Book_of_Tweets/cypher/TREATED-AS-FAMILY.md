---
name: "thought.TREATED AS FAMILY"
alias: "Thought: Treated As Family"
type: THOUGHT
en_content: "God has always treated me as family, whether I deserved it or not."
parent: "topic.GRACE"
tags:
- family
- grace
- identity
- god
- love
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-May-2012)
CREATE (t:THOUGHT {
    name: "thought.TREATED AS FAMILY",
    alias: "Thought: Treated As Family",
    parent: "topic.GRACE",
    tags: ['family', 'grace', 'identity', 'god', 'love'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.TREATED AS FAMILY",
    en_title: "Treated As Family",
    en_content: "God has always treated me as family, whether I deserved it or not.",
    es_title: "Tratado Como Familia",
    es_content: "Dios siempre me ha tratado como familia, ya sea que lo mereciera o no.",
    fr_title: "Traité Comme un Membre de la Famille",
    fr_content: "Dieu m'a toujours traité comme un membre de la famille, que je le mérite ou non.",
    hi_title: "परिवार की तरह व्यवहार",
    hi_content: "परमेश्वर ने हमेशा मेरे साथ परिवार की तरह व्यवहार किया है, चाहे मैं इसके योग्य था या नहीं।",
    zh_title: "Bèi dàng zuò jiā rén",
    zh_content: "Wú lùn wǒ shì fǒu zhí dé, Shàng dì zǒng shì bǎ wǒ dàng zuò jiā rén duì dài."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.TREATED AS FAMILY" AND c.name = "content.TREATED AS FAMILY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.TREATED AS FAMILY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.TREATED AS FAMILY"
MERGE (parent)-[:HAS_THOUGHT { "name": "GRACE >TREATED AS FAMILY" }]->(child);
```
