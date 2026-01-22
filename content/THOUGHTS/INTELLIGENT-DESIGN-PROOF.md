---
name: "thought.INTELLIGENT DESIGN PROOF"
alias: "Thought: Intelligent Design Proof"
type: THOUGHT
en_content: "There are TONS of evidence for Intelligent Design evolutionists don't want you to know."
parent: "topic.CREATION"
tags:
- creation
- design
- evolution
- evidence
- truth
level: 2
neo4j: true
ptopic: "[[topic-CREATION]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Oct-2011g)
CREATE (t:THOUGHT {
    name: "thought.INTELLIGENT DESIGN PROOF",
    alias: "Thought: Intelligent Design Proof",
    parent: "topic.CREATION",
    tags: ['creation', 'design', 'evolution', 'evidence', 'truth'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.INTELLIGENT DESIGN PROOF",
    en_title: "Intelligent Design Proof",
    en_content: "There are TONS of evidence for Intelligent Design evolutionists don't want you to know.",
    es_title: "Prueba del Diseño Inteligente",
    es_content: "Hay TONELADAS de evidencia para el Diseño Inteligente que los evolucionistas no quieren que sepas.",
    fr_title: "Preuve du Dessein Intelligent",
    fr_content: "Il y a ÉNORMÉMENT de preuves pour le Dessein Intelligent que les évolutionnistes ne veulent pas que vous sachiez.",
    hi_title: "बुद्धिमान डिज़ाइन का प्रमाण",
    hi_content: "बुद्धिमान डिज़ाइन के लिए बहुत सारे सबूत हैं जिन्हें विकासवादी नहीं चाहते कि आप जानें।",
    zh_title: "Zhi Neng She Ji Zheng Ming",
    zh_content: "You DA LIANG de zheng ju zheng ming Zhi Neng She Ji, jin hua lun zhe bu xi wang ni zhi dao."
});

MATCH (t:THOUGHT {name: "thought.INTELLIGENT DESIGN PROOF"})
MATCH (c:CONTENT {name: "content.INTELLIGENT DESIGN PROOF"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.INTELLIGENT DESIGN PROOF" }]->(c);

MATCH (parent:TOPIC {name: "topic.CREATION"})
MATCH (child:THOUGHT {name: "thought.INTELLIGENT DESIGN PROOF"})
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION->INTELLIGENT DESIGN PROOF" }]->(child);
```
