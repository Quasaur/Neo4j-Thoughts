---
name: "thought.SAUL WASTING LIFE"
alias: "Thought: Saul Wasting Life"
type: THOUGHT
en_content: "Saul wasted a large portion of his life trying to kill David while neglecting weightier matters...like his relationship with God."
parent: "topic.RELIGION"
tags:
- saul
- david
- relationship
- god
- waste
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 09-Oct-2013)
CREATE (t:THOUGHT {
    name: "thought.SAUL WASTING LIFE",
    alias: "Thought: Saul Wasting Life",
    parent: "topic.RELIGION",
    tags: ['saul', 'david', 'relationship', 'god', 'waste'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.SAUL WASTING LIFE",
    en_title: "Saul Wasting Life",
    en_content: "Saul wasted a large portion of his life trying to kill David while neglecting weightier matters...like his relationship with God.",
    es_title: "Saúl Desperdiciando la Vida",
    es_content: "Saúl desperdició una gran parte de su vida tratando de matar a David mientras descuidaba asuntos de mayor peso...como su relación con Dios.",
    fr_title: "Saül Gaspillant sa Vie",
    fr_content: "Saül a gaspillé une grande partie de sa vie à essayer de tuer David tout en négligeant des questions plus importantes...comme sa relation avec Dieu.",
    hi_title: "शाऊल का जीवन की बर्बादी",
    hi_content: "शाऊल ने अपने जीवन का एक बड़ा हिस्सा दाऊद को मारने की कोशिश में बर्बाद किया जबकि वह अधिक महत्वपूर्ण बातों की उपेक्षा कर रहा था...जैसे परमेश्वर के साथ अपना रिश्ता।",
    zh_title: "Sǎo'ěr Làngfèi Shēngmìng",
    zh_content: "Sǎo'ěr bǎ tā shēngmìng de hěn dà yī bùfen làngfèi zài shìtú shā sǐ Dàwèi shàng, ér hūlüè le gèng zhòngyào de shìqíng...bǐrú tā yǔ Shàngdì de guānxì."
});

MATCH (t:THOUGHT {name: "thought.SAUL WASTING LIFE"})
MATCH (c:CONTENT {name: "content.SAUL WASTING LIFE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.SAUL WASTING LIFE" }]->(c);

MATCH (parent:TOPIC {name: "topic.RELIGION"})
MATCH (child:THOUGHT {name: "thought.SAUL WASTING LIFE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION->SAUL WASTING LIFE" }]->(child);
```
