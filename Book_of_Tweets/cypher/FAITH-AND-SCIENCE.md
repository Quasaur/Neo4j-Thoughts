---
name: "thought.FAITH AND SCIENCE"
alias: "Thought: Faith And Science"
type: THOUGHT
en_content: "The Standard Model (Inflation, Dark Matter/Energy/Flow) takes more FAITH than to believe God holds the universe together by His Word."
parent: "topic.FAITH"
tags:
- faith
- science
- standard_model
- creation
- belief
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Jul-2010)
CREATE (t:THOUGHT {
    name: "thought.FAITH AND SCIENCE",
    alias: "Thought: Faith And Science",
    parent: "topic.FAITH",
    tags: ['faith', 'science', 'standard_model', 'creation', 'belief'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FAITH AND SCIENCE",
    en_title: "Faith And Science",
    en_content: "The Standard Model (Inflation, Dark Matter/Energy/Flow) takes more FAITH than to believe God holds the universe together by His Word.",
    es_title: "Fe y ciencia",
    es_content: "El Modelo Estándar (Inflación, Materia Oscura/Energía/Flujo) requiere más FE que creer que Dios mantiene unido el universo mediante Su Palabra.",
    fr_title: "Foi et science",
    fr_content: "Le modèle standard (inflation, matière noire/énergie/flux) demande plus de FOI que de croire que Dieu maintient l’univers ensemble par sa Parole.",
    hi_title: "आस्था और विज्ञान",
    hi_content: "मानक मॉडल (मुद्रास्फीति, डार्क मैटर/ऊर्जा/प्रवाह) में इस विश्वास की तुलना में अधिक विश्वास की आवश्यकता है कि ईश्वर अपने वचन द्वारा ब्रह्मांड को एक साथ रखता है।",
    zh_title: "信仰与科学",
    zh_content: "标准模型（暴胀、暗物质/能量/流动）需要更多的信心，而不是相信上帝通过他的话语将宇宙结合在一起。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FAITH AND SCIENCE" AND c.name = "content.FAITH AND SCIENCE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.FAITH AND SCIENCE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.FAITH AND SCIENCE"
MERGE (parent)-[:HAS_THOUGHT { "name": "FAITH >FAITH AND SCIENCE" }]->(child);
```
