---
type: THOUGHT
name: "thought.GNOSIS"
alias: "Thought: GNOSIS"
parent: "topic.FAITH"
tags: ["gnosis", "faith", "immortality", "knowledge", "believe"]
ptopic: "[[topic-FAITH]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.GNOSIS",
    alias: "Thought: GNOSIS",
    parent: "topic.FAITH",
    tags: ["gnosis", "faith", "immortality", "knowledge", "believe"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.GNOSIS",
    ctype: "THOUGHT",
    en_title: "GNOSIS",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.GNOSIS" AND c.name = "content.GNOSIS"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.GNOSIS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FAITH" AND child.name = "thought.GNOSIS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.FAITH->GNOSIS"}]->(child);
```