---
name: thought.FAITH AND SCIENCE
alias: "Thought: Faith And Science"
type: THOUGHT
en_content: The Standard Model (Inflation, Dark Matter/Energy/Flow) takes more FAITH than to believe God holds the universe together by His Word.
parent: topic.PHYSICS
tags:
  - faith
  - science
  - standard_model
  - creation
  - belief
level: 6
neo4j: true
ptopic: "[[topic-PHYSICS]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 27-Jul-2010)
CREATE (t:THOUGHT {
    name: "thought.FAITH AND SCIENCE",
    alias: "Thought: Faith And Science",
    parent: "topic.PHYSICS",
    tags: ['faith', 'science', 'standard_model', 'creation', 'belief'],
    level: 6
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
    zh_title: "xìn yǎng yǔ kē xué",
    zh_content: "biāo zhǔn mó xíng （ bào zhàng 、 àn wù zhì / néng liàng / liú dòng ） xū yào gèng duō de xìn xīn ， ér bú shì xiāng xìn shàng dì tōng guò tā de huà yǔ jiāng yǔ zhòu jié hé zài yì qǐ 。"
});

MATCH (t:THOUGHT {name: "thought.FAITH AND SCIENCE"})
MATCH (c:CONTENT {name: "content.FAITH AND SCIENCE"})
MERGE (t)-[:HAS_CONTENT { "name": "t.edge.FAITH AND SCIENCE" }]->(c);

MATCH (parent:TOPIC {name: "topic.PHYSICS"})
MATCH (child:THOUGHT {name: "thought.FAITH AND SCIENCE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "t.edge.PHYSICS->FAITH AND SCIENCE" }]->(child);
```
