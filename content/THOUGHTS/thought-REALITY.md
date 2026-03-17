---
type: THOUGHT
name: "thought.REALITY"
alias: "Thought: Reality"
parent: "topic.TRUTH"
tags: ["cosmology", "relativity", "geocentricity", "michelson", "intelligentdesign"]
ptopic: "[[topic-TRUTH]]"
level: 2
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.REALITY",
    alias: "Thought: Reality",
    parent: "topic.TRUTH",
    tags: ["cosmology", "relativity", "geocentricity", "michelson", "intelligentdesign"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.REALITY",
    ctype: "THOUGHT",
    en_title: "Reality",
    en_content: "",
    es_title: "REALIDAD",
    es_content: "Los científicos honestos están empezando a admitir públicamente que, basándose en todos los datos disponibles, la crisis actual que afecta al Modelo Estándar (materia oscura, etc.) se RESUELVE cuando se coloca nuestro sistema solar (y la Tierra en particular) en el CENTRO del Universo.",
    fr_title: "RÉALITÉ",
    fr_content: "Des scientifiques honnêtes commencent à admettre publiquement que, sur la base de toutes les données disponibles, la crise actuelle impliquant le modèle standard (matière noire, etc.) est RÉSOLU lorsque l’on place notre système solaire (et la Terre en particulier) au CENTRE de l’Univers.",
    hi_title: "वास्तविकता",
    hi_content: "ईमानदार वैज्ञानिक सार्वजनिक रूप से यह स्वीकार करना शुरू कर रहे हैं कि, सभी उपलब्ध आंकड़ों के आधार पर, मानक मॉडल (डार्क मैटर इत्यादि) से जुड़ा मौजूदा संकट तब हल हो जाता है जब आप हमारे सौर मंडल (और विशेष रूप से पृथ्वी) को ब्रह्मांड के केंद्र में रखते हैं।",
    zh_title: "xiàn shí",
    zh_content: "chéng shí de kē xué jiā kāi shǐ gōng kāi chéng rèn ， gēn jù suǒ yǒu kě yòng shù jù ， dāng nín jiāng wǒ men de tài yáng xì （ tè bié shì dì qiú ） zhì yú yǔ zhòu zhōng xīn shí ， dāng qián shè jí biāo zhǔn mó xíng （ àn wù zhì děng ） de wēi jī jiù dé dào le jiě jué 。"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.REALITY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.TRUTH"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.TRUTH->REALITY"
RETURN t, parent;
```
