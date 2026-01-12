---
name: "thought.KNOWLEDGE PROPERTY GOD"
alias: "Thought: Knowledge Property God"
type: THOUGHT
en_content: "Genesis 2:15, 16: Knowledge is not a right; knowledge is the property of God."
parent: "topic.TRUTH"
tags:
- knowledge
- ownership
- property
- god
- truth
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Mar-2013b)
CREATE (t:THOUGHT {
    name: "thought.KNOWLEDGE PROPERTY GOD",
    alias: "Thought: Knowledge Property God",
    parent: "topic.TRUTH",
    tags: ['knowledge', 'ownership', 'property', 'god', 'truth'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.KNOWLEDGE PROPERTY GOD",
    en_title: "Knowledge Property God",
    en_content: "Genesis 2:15, 16: Knowledge is not a right; knowledge is the property of God.",
    es_title: "El Conocimiento Propiedad de Dios",
    es_content: "Génesis 2:15, 16: El conocimiento no es un derecho; el conocimiento es propiedad de Dios.",
    fr_title: "La Connaissance Propriété de Dieu",
    fr_content: "Genèse 2:15, 16: La connaissance n'est pas un droit; la connaissance est la propriété de Dieu.",
    hi_title: "ज्ञान परमेश्वर की संपत्ति",
    hi_content: "उत्पत्ति 2:15, 16: ज्ञान कोई अधिकार नहीं है; ज्ञान परमेश्वर की संपत्ति है।",
    zh_title: "Zhishi Shu Shen De Caichan",
    zh_content: "Chuangshiji 2:15, 16: Zhishi bushi yizhong quanli; zhishi shi Shen de caichan."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.KNOWLEDGE PROPERTY GOD" AND c.name = "content.KNOWLEDGE PROPERTY GOD"
MERGE (t)-[:HAS_CONTENT { "name": "edge.KNOWLEDGE PROPERTY GOD" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.KNOWLEDGE PROPERTY GOD"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >KNOWLEDGE PROPERTY GOD" }]->(child);
```
