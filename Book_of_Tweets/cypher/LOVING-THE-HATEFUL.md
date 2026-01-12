---
name: "thought.LOVING THE HATEFUL"
alias: "Thought: Loving The Hateful"
type: THOUGHT
en_content: "Loving the hateful... how does God do it? How can I do it?"
parent: "topic.THE GODHEAD"
tags:
- love
- hate
- character
- god
- divinity
level: 1
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 24-Oct-2013b)
CREATE (t:THOUGHT {
    name: "thought.LOVING THE HATEFUL",
    alias: "Thought: Loving The Hateful",
    parent: "topic.THE GODHEAD",
    tags: ['love', 'hate', 'character', 'god', 'divinity'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.LOVING THE HATEFUL",
    en_title: "Loving The Hateful",
    en_content: "Loving the hateful... how does God do it? How can I do it?",
    es_title: "Amar a los Aborrecibles",
    es_content: "Amar a los aborrecibles... ¿cómo lo hace Dios? ¿Cómo puedo hacerlo yo?",
    fr_title: "Aimer Ceux Qui Haïssent",
    fr_content: "Aimer ceux qui haïssent... comment Dieu fait-il cela ? Comment puis-je le faire ?",
    hi_title: "घृणा करने वालों से प्रेम करना",
    hi_content: "घृणा करने वालों से प्रेम करना... परमेश्वर यह कैसे करता है? मैं यह कैसे कर सकता हूँ?",
    zh_title: "Ai Na Xie Ke Wu De Ren",
    zh_content: "Ai na xie ke wu de ren... Shen shi zenme zuo dao de? Wo zenme neng zuo dao?"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.LOVING THE HATEFUL" AND c.name = "content.LOVING THE HATEFUL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.LOVING THE HATEFUL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.LOVING THE HATEFUL"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >LOVING THE HATEFUL" }]->(child);
```
