---
type: THOUGHT
name: "thought.SECRETS"
alias: "Thought: Secrets"
parent: "topic.PSYCHOLOGY"
tags: ["secrets", "distractions", "eternity", "immortality", "transcendence"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.SECRETS",
    alias: "Thought: Secrets",
    parent: "topic.PSYCHOLOGY",
    tags: ["secrets", "distractions", "eternity", "immortality", "transcendence"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.SECRETS",
    ctype: "THOUGHT",
    en_title: "Secrets",
    en_content: "",
    es_title: "MISTERIOS",
    es_content: "Los SECRETOS DEL UNIVERSO, incluyendo la inmortalidad y la trascendencia, están a tu alrededor… justo debajo de tus narices; pero sin OJOS para ver y OÍDOS para oír, los extrañarás en la cacofonía que te distrae de la “vida” terrenal y eventualmente te encontrarás en una ETERNIDAD de miseria indescriptible porque estabas demasiado ocupado “haciéndote a ti mismo”.
Mateo 7:13,14",
    fr_title: "SECRETS",
    fr_content: "Les SECRETS DE L'UNIVERS, y compris l'immortalité et la transcendance, sont tout autour de vous… juste sous votre nez ; mais sans YEUX pour voir et sans OREILLES pour entendre, vous les manquerez dans la cacophonie distrayante de la « vie » terrestre et vous finirez par vous retrouver dans une ÉTERNITÉ de misère indescriptible parce que vous étiez trop occupé à « vous faire ».
Matthieu 7:13,14",
    hi_title: "रहस्य",
    hi_content: "ब्रह्मांड के रहस्य, अमरता और उत्कृष्टता सहित, आपके चारों ओर हैं... ठीक आपकी नाक के नीचे; लेकिन देखने के लिए आँखों और सुनने के लिए कानों के बिना, आप सांसारिक \\\"जीवन\\\" के विचलित करने वाले शोर में उन्हें याद करेंगे और अंततः अपने आप को अवर्णनीय दुख की अनंत काल में पाएंगे क्योंकि आप \\\"अपने काम\\\" में बहुत व्यस्त थे।
मत्ती 7:13,14",
    zh_title: "mì mì",
    zh_content: ""
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.SECRETS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.PSYCHOLOGY->SECRETS"
RETURN t, parent;
```
