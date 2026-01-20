---
name: "thought.DNA MEMORY VS REINCARNATION"
alias: "Thought: Dna Memory Vs Reincarnation"
type: THOUGHT
en_content: "Reincarnation: what if these memories are not of previous lives, but of the lives of our ancestors engraved on our spirits/DNA?"
parent: "topic.PHILOSOPHY"
tags:
- philosophy
- reincarnation
- dna
- memory
- biology
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 07-Sep-2011a)
CREATE (t:THOUGHT {
    name: "thought.DNA MEMORY VS REINCARNATION",
    alias: "Thought: Dna Memory Vs Reincarnation",
    parent: "topic.PHILOSOPHY",
    tags: ['philosophy', 'reincarnation', 'dna', 'memory', 'biology'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DNA MEMORY VS REINCARNATION",
    en_title: "Dna Memory Vs Reincarnation",
    en_content: "Reincarnation: what if these memories are not of previous lives, but of the lives of our ancestors engraved on our spirits/DNA?",
    es_title: "Memoria del ADN Vs Reencarnación",
    es_content: "Reencarnación: ¿qué tal si estos recuerdos no son de vidas anteriores, sino de las vidas de nuestros ancestros grabadas en nuestros espíritus/ADN?",
    fr_title: "Mémoire de l'ADN Vs Réincarnation",
    fr_content: "Réincarnation : et si ces souvenirs n'étaient pas de vies antérieures, mais des vies de nos ancêtres gravées sur nos esprits/ADN ?",
    hi_title: "डीएनए स्मृति बनाम पुनर्जन्म",
    hi_content: "पुनर्जन्म: क्या होगा अगर ये यादें पूर्व जन्मों की नहीं, बल्कि हमारे पूर्वजों के जीवन की हैं जो हमारी आत्मा/डीएनए पर अंकित हैं?",
    zh_title: "DNA Ji Yi Dui Bi Lun Hui",
    zh_content: "Lun hui: ru guo zhei xie ji yi bu shi qian shi de, er shi wo men zu xian de sheng huo ke zai wo men ling hun/DNA shang de ne?"
});

MATCH (t:THOUGHT {name: "thought.DNA MEMORY VS REINCARNATION"})
MATCH (c:CONTENT {name: "content.DNA MEMORY VS REINCARNATION"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.DNA MEMORY VS REINCARNATION" }]->(c);

MATCH (parent:TOPIC {name: "topic.PHILOSOPHY"})
MATCH (child:THOUGHT {name: "thought.DNA MEMORY VS REINCARNATION"})
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >DNA MEMORY VS REINCARNATION" }]->(child);
```
