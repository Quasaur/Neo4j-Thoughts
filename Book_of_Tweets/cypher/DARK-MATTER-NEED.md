---
name: "thought.DARK MATTER NEED"
alias: "Thought: Dark Matter Need"
type: THOUGHT
en_content: "If the Standard Model was doing its job, there'd be no need for \"dark matter\", \"dark energy\" or \"dark flow\"!"
parent: "topic.PHILOSOPHY"
tags:
- science
- dark_matter
- philosophy
- energy
- truth
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Oct-2011d)
CREATE (t:THOUGHT {
    name: "thought.DARK MATTER NEED",
    alias: "Thought: Dark Matter Need",
    parent: "topic.PHILOSOPHY",
    tags: ['science', 'dark_matter', 'philosophy', 'energy', 'truth'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DARK MATTER NEED",
    en_title: "Dark Matter Need",
    en_content: "If the Standard Model was doing its job, there'd be no need for \"dark matter\", \"dark energy\" or \"dark flow\"!",
    es_title: "Necesidad de Materia Oscura",
    es_content: "¡Si el Modelo Estándar estuviera haciendo su trabajo, no habría necesidad de \"materia oscura\", \"energía oscura\" o \"flujo oscuro\"!",
    fr_title: "Besoin de Matière Sombre",
    fr_content: "Si le Modèle Standard faisait son travail, il n'y aurait pas besoin de \"matière sombre\", \"énergie sombre\" ou \"flux sombre\" !",
    hi_title: "गहरी पदार्थ की आवश्यकता",
    hi_content: "यदि मानक मॉडल अपना काम कर रहा होता, तो \"गहरे पदार्थ\", \"गहरी ऊर्जा\" या \"गहरे प्रवाह\" की कोई आवश्यकता नहीं होती!",
    zh_title: "Hēi Wùzhí de Xūyào",
    zh_content: "Rúguǒ Biāozhǔn Móxíng zài zuò tā de gōngzuò, Jiù bù xūyào \"hēi wùzhí\", \"hēi néngliàng\" huò \"hēi liú\"le!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DARK MATTER NEED" AND c.name = "content.DARK MATTER NEED"
MERGE (t)-[:HAS_CONTENT { "name": "edge.DARK MATTER NEED" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PHILOSOPHY" AND child.name = "thought.DARK MATTER NEED"
MERGE (parent)-[:HAS_THOUGHT { "name": "PHILOSOPHY >DARK MATTER NEED" }]->(child);
```
