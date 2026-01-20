---
name: "thought.ALIGNING THROUGH PRAYER"
alias: "Thought: Aligning Through Prayer"
type: THOUGHT
en_content: "The purpose of prayer is not just to get God to do stuff, but to align myself with what God is doing!"
parent: "topic.SPIRITUALITY"
tags:
- prayer
- alignment
- will
- purpose
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 11-Mar-2014)
CREATE (t:THOUGHT {
    name: "thought.ALIGNING THROUGH PRAYER",
    alias: "Thought: Aligning Through Prayer",
    parent: "topic.SPIRITUALITY",
    tags: ['prayer', 'alignment', 'will', 'purpose'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.ALIGNING THROUGH PRAYER",
    en_title: "Aligning Through Prayer",
    en_content: "The purpose of prayer is not just to get God to do stuff, but to align myself with what God is doing!",
    es_title: "Alinearse Mediante la Oración",
    es_content: "El propósito de la oración no es solo conseguir que Dios haga cosas, ¡sino alinearme con lo que Dios está haciendo!",
    fr_title: "S'Aligner par la Prière",
    fr_content: "Le but de la prière n'est pas seulement d'obtenir que Dieu fasse des choses, mais de m'aligner sur ce que Dieu fait !",
    hi_title: "प्रार्थना के माध्यम से संरेखण",
    hi_content: "प्रार्थना का उद्देश्य केवल भगवान से चीजें करवाना नहीं है, बल्कि स्वयं को उस काम के साथ संरेखित करना है जो भगवान कर रहे हैं!",
    zh_title: "Tōngguò dǎogào duìqí",
    zh_content: "Dǎogào de mùdì bùjǐn jǐn shì ràng shàngdì zuòshì, ér shì ràng zìjǐ yǔ shàngdì zhèngzài zuò de shì duìqí!"
});

MATCH (t:THOUGHT {name: "thought.ALIGNING THROUGH PRAYER"})
MATCH (c:CONTENT {name: "content.ALIGNING THROUGH PRAYER"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.ALIGNING THROUGH PRAYER" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.ALIGNING THROUGH PRAYER"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >ALIGNING THROUGH PRAYER" }]->(child);
```
