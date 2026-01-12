---
name: "thought.SCIENCE AND SCRIPTURE"
alias: "Thought: Science And Scripture"
type: THOUGHT
en_content: "No discrepancy exists between Science and Scripture; the discrepancy is between scientists and God."
parent: "topic.TRUTH"
tags:
- science
- scripture
- truth
- creation
- reconciliation
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Sep-2011b)
CREATE (t:THOUGHT {
    name: "thought.SCIENCE AND SCRIPTURE",
    alias: "Thought: Science And Scripture",
    parent: "topic.TRUTH",
    tags: ['science', 'scripture', 'truth', 'creation', 'reconciliation'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SCIENCE AND SCRIPTURE",
    en_title: "Science And Scripture",
    en_content: "No discrepancy exists between Science and Scripture; the discrepancy is between scientists and God.",
    es_title: "Ciencia Y Escritura",
    es_content: "No existe discrepancia entre la Ciencia y la Escritura; la discrepancia está entre los científicos y Dios.",
    fr_title: "Science Et Écriture",
    fr_content: "Aucune discordance n'existe entre la Science et l'Écriture ; la discordance est entre les scientifiques et Dieu.",
    hi_title: "विज्ञान और धर्मग्रंथ",
    hi_content: "विज्ञान और धर्मग्रंथ के बीच कोई विसंगति नहीं है; विसंगति वैज्ञानिकों और परमेश्वर के बीच है।",
    zh_title: "Kē Xué Yǔ Shèng Jīng",
    zh_content: "Kē xué hé Shèng jīng zhī jiān méi yǒu máo dùn; máo dùn zài yú kē xué jiā hé Shàng dì zhī jiān."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SCIENCE AND SCRIPTURE" AND c.name = "content.SCIENCE AND SCRIPTURE"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SCIENCE AND SCRIPTURE" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.SCIENCE AND SCRIPTURE"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >SCIENCE AND SCRIPTURE" }]->(child);
```
