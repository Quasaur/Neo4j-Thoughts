---
type: THOUGHT
name: "thought.FULLNESS"
alias: "Thought: Fullness"
parent: "topic.GRACE"
tags: ["spirituality", "fullness", "overflow", "immunity", "life"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.FULLNESS",
    alias: "Thought: Fullness",
    parent: "topic.GRACE",
    tags: ["spirituality", "fullness", "overflow", "immunity", "life"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FULLNESS",
    ctype: "THOUGHT",
    en_title: "Fullness",
    en_content: "",
    es_title: "PLENITUD",
    es_content: "Por Su DIVINA PLENITUD, Los Miembros de La DIVINIDAD son COMPLETAMENTE INMUNE a la tentación, la corrupción y el pecado.
A través de Jesucristo, ESA MISMA INMUNIDAD está disponible para el desdichado pecador... siempre que él o ella esté dispuesto a ABANDONAR su propia “plenitud” (justicia propia, bondad, orgullo).",
    fr_title: "PLÉNITUDE",
    fr_content: "En raison de leur PLEINITÉ DIVINE, les membres de The DIVIN sont COMPLÈTEMENT IMMUNIS contre la tentation, la corruption et le péché.
Par Jésus-Christ, CETTE MÊME IMMUNITÉ est mise à la disposition du misérable pécheur… à condition qu'il soit prêt à ABANDONNER sa propre « plénitude » (autosatisfaction, bonté, orgueil).",
    hi_title: "परिपूर्णता",
    hi_content: "अपनी दिव्य परिपूर्णता के कारण, ईश्वर के सदस्य प्रलोभन, भ्रष्टाचार और पाप के प्रति पूरी तरह से प्रतिरक्षित हैं।
यीशु मसीह के माध्यम से वही प्रतिरक्षा दुष्ट पापी को उपलब्ध कराई जाती है...बशर्ते वह अपनी \\\"संपूर्णता\\\" (स्वयं-धार्मिकता, अच्छाई, गर्व) को त्यागने के लिए तैयार हो।",
    zh_title: "bǎo mǎn dù",
    zh_content: ""
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.FULLNESS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.GRACE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.GRACE->FULLNESS"
RETURN t, parent;
```
