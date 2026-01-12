---
name: "thought.HEAVY DIVINE WILL"
alias: "Thought: Heavy Divine Will"
type: THOUGHT
en_content: "The Will of God is far too heavy for frail human hands to budge it in any direction; answered prayer is ALWAYS an Act of Divine Mercy."
parent: "topic.DIVINE SOVEREIGNTY"
tags:
- will
- prayer
- mercy
- sovereignty
- power
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Jul-2011d)
CREATE (t:THOUGHT {
    name: "thought.HEAVY DIVINE WILL",
    alias: "Thought: Heavy Divine Will",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ['will', 'prayer', 'mercy', 'sovereignty', 'power'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.HEAVY DIVINE WILL",
    en_title: "Heavy Divine Will",
    en_content: "The Will of God is far too heavy for frail human hands to budge it in any direction; answered prayer is ALWAYS an Act of Divine Mercy.",
    es_title: "Voluntad Divina Pesada",
    es_content: "La Voluntad de Dios es demasiado pesada para que las frágiles manos humanas la muevan en cualquier dirección; la oración respondida es SIEMPRE un Acto de Misericordia Divina.",
    fr_title: "Volonté Divine Pesante",
    fr_content: "La Volonté de Dieu est bien trop lourde pour que de frêles mains humaines puissent la déplacer dans quelque direction que ce soit ; la prière exaucée est TOUJOURS un Acte de Miséricorde Divine.",
    hi_title: "भारी दिव्य इच्छा",
    hi_content: "परमेश्वर की इच्छा कमज़ोर मानवीय हाथों के लिए बहुत भारी है कि वे इसे किसी भी दिशा में हिला सकें; उत्तर दिया गया प्रार्थना हमेशा दिव्य कृपा का एक कार्य होता है।",
    zh_title: "Chénzhòng de Shénshèng Yìzhì",
    zh_content: "Shàngdì de yìzhì duì cuìruò de rénlèi shuāngshǒu lái shuō tài guò chénzhòng, wúfǎ jiāng qí tuīdòng dào rènhé fāngxiàng; déi dào huídá de qídǎo ZǑNGSHÌ Shénshèng Cíbēi de Xíngwéi."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HEAVY DIVINE WILL" AND c.name = "content.HEAVY DIVINE WILL"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HEAVY DIVINE WILL" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.DIVINE SOVEREIGNTY" AND child.name = "thought.HEAVY DIVINE WILL"
MERGE (parent)-[:HAS_THOUGHT { "name": "DIVINE SOVEREIGNTY >HEAVY DIVINE WILL" }]->(child);
```
