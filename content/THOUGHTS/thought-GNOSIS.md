---
type: THOUGHT
name: "thought.GNOSIS"
alias: "Thought: Gnosis"
parent: "topic.FAITH"
tags: ["gnosis", "faith", "immortality", "knowledge", "believe"]
ptopic: "[[topic-FAITH]]"
level: 4
neo4j: true
verified: false
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.GNOSIS",
    alias: "Thought: Gnosis",
    parent: "topic.FAITH",
    tags: ["gnosis", "faith", "immortality", "knowledge", "believe"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.GNOSIS",
    ctype: "THOUGHT",
    en_title: "Gnosis",
    en_content: "The Knowledge that brings IMMORTALITY is not hidden…it's just incredibly difficult to BELIEVE (in the Biblical sense)!",
    es_title: "GNOSIS",
    es_content: "El Conocimiento que trae la INMORTALIDAD no está oculto... ¡es simplemente increíblemente difícil de CREER (en el sentido bíblico)!",
    fr_title: "GNOSE",
    fr_content: "La Connaissance qui apporte l'IMMORTALITÉ n'est pas cachée… c'est juste incroyablement difficile à CROIRE (au sens biblique) !",
    hi_title: "ज्ञान की",
    hi_content: "वह ज्ञान जो अमरता लाता है, छिपा नहीं है...इस पर विश्वास करना अविश्वसनीय रूप से कठिन है (बाइबिल के अर्थ में)!",
    zh_title: "nuò xī sī",
    zh_content: "dài lái bù xiǔ de zhī shí bìng bú shì yǐn cáng de …… zhǐ shì nán yǐ zhì xìn dì nán yǐ xiāng xìn （ zài shèng jīng yì yì shàng ）！"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GNOSIS"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.FAITH"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.FAITH->GNOSIS"
RETURN t, parent;
```
