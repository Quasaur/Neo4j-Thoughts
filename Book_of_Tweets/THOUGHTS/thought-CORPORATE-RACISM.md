---
type: THOUGHT
name: "thought.CORPORATE RACISM"
alias: "Thought: Corporate Racism"
parent: "topic.MORALITY"
en_content: "Racism, Discrimination and Prejudice are alive and well in Corporate America."
tags: ["racism", "discrimination", "morality", "corporations", "justice"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Oct-2011c)
CREATE (t:THOUGHT {    name: "thought.CORPORATE RACISM",
    alias: "Thought: Corporate Racism",
    parent: "topic.MORALITY",
    tags: ['racism', 'discrimination', 'morality', 'corporations', 'justice'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.CORPORATE RACISM",
    ctype: "THOUGHT",
    en_title: "Corporate Racism",
    en_content: "Racism, Discrimination and Prejudice are alive and well in Corporate America.",
    es_title: "Racismo Corporativo",
    es_content: "El racismo, la discriminación y los prejuicios están vivos y bien en la América Corporativa.",
    fr_title: "Racisme Corporatif",
    fr_content: "Le racisme, la discrimination et les préjugés sont bien vivants dans l'Amérique corporative.",
    hi_title: "निगम नस्लवाद",
    hi_content: "नस्लवाद, भेदभाव और पूर्वाग्रह कॉर्पोरेट अमेरिका में जीवित और स्वस्थ हैं।",
    zh_title: "Gōngsī Zhǒngzú Zhǔyì",
    zh_content: "Zhǒngzú zhǔyì, qíshì hé piānjiàn zài gōngsī Měiguó zhōng shēngcún de hěn hǎo."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.CORPORATE RACISM"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->CORPORATE RACISM"
RETURN t, parent;
```
