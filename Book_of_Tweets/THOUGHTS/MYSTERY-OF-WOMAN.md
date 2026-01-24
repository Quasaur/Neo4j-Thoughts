---
name: "thought.MYSTERY OF WOMAN"
alias: "Thought: Mystery Of Woman"
type: THOUGHT
en_content: "Adam did not see Eve being created; therefore Woman will always be a Mystery to Man."
parent: "topic.HUMANITY"
tags:
- woman
- man
- mystery
- creation
- adam
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 17-Jul-2012)
CREATE (t:THOUGHT {
    name: "thought.MYSTERY OF WOMAN",
    alias: "Thought: Mystery Of Woman",
    parent: "topic.HUMANITY",
    tags: ['woman', 'man', 'mystery', 'creation', 'adam'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.MYSTERY OF WOMAN",
    en_title: "Mystery Of Woman",
    en_content: "Adam did not see Eve being created; therefore Woman will always be a Mystery to Man.",
    es_title: "El Misterio de la Mujer",
    es_content: "Adán no vio a Eva ser creada; por lo tanto, la Mujer siempre será un Misterio para el Hombre.",
    fr_title: "Le Mystère de la Femme",
    fr_content: "Adam n'a pas vu Ève être créée ; par conséquent, la Femme sera toujours un Mystère pour l'Homme.",
    hi_title: "स्त्री का रहस्य",
    hi_content: "आदम ने हव्वा को बनाए जाते नहीं देखा; इसलिए स्त्री हमेशा पुरुष के लिए एक रहस्य रहेगी।",
    zh_title: "Nǚrén de àomì 女人的奥秘",
    zh_content: "Yàdāng méiyǒu kànjiàn Xiàwá de chuàngzào; yīncǐ nǚrén jiāng yǒngyuǎn shì nánrén de àomì. 亚当没有看见夏娃的创造；因此女人将永远是男人的奥秘。"
});

MATCH (t:THOUGHT {name: "thought.MYSTERY OF WOMAN"})
MATCH (c:CONTENT {name: "content.MYSTERY OF WOMAN"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.MYSTERY OF WOMAN" }]->(c);

MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MATCH (child:THOUGHT {name: "thought.MYSTERY OF WOMAN"})
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY->MYSTERY OF WOMAN" }]->(child);
```
