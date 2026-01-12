---
name: "thought.SCIENCE ON ORIGIN"
alias: "Thought: Science On Origin"
type: THOUGHT
en_content: "If I can't trust science to explain origin, why is it so infallible on development??"
parent: "topic.TRUTH"
tags:
- science
- origin
- development
- truth
- evolution
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Oct-2011e)
CREATE (t:THOUGHT {
    name: "thought.SCIENCE ON ORIGIN",
    alias: "Thought: Science On Origin",
    parent: "topic.TRUTH",
    tags: ['science', 'origin', 'development', 'truth', 'evolution'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SCIENCE ON ORIGIN",
    en_title: "Science On Origin",
    en_content: "If I can't trust science to explain origin, why is it so infallible on development??",
    es_title: "La Ciencia Sobre el Origen",
    es_content: "Si no puedo confiar en la ciencia para explicar el origen, ¿por qué es tan infalible en el desarrollo?",
    fr_title: "La Science sur l'Origine",
    fr_content: "Si je ne peux pas faire confiance à la science pour expliquer l'origine, pourquoi est-elle si infaillible sur le développement ?",
    hi_title: "उत्पत्ति पर विज्ञान",
    hi_content: "यदि मैं उत्पत्ति की व्याख्या के लिए विज्ञान पर भरोसा नहीं कर सकता, तो यह विकास पर इतना अचूक क्यों है?",
    zh_title: "Guānyú Qǐyuán de Kēxué",
    zh_content: "Rúguǒ wǒ bùnéng xiāngxìn kēxué lái jiěshì qǐyuán, wèishéme tā zài fāzhǎn shàng què rúcǐ wúwù?"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SCIENCE ON ORIGIN" AND c.name = "content.SCIENCE ON ORIGIN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SCIENCE ON ORIGIN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.SCIENCE ON ORIGIN"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >SCIENCE ON ORIGIN" }]->(child);
```
