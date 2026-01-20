---
name: topic.THE-BIBLE
alias: "Topic: The Story of Redemption"
type: TOPIC
parent: topic.ANTHROPOLOGY
tags:
- literature
- scriptures
- hebrew
- greek
- linquistic
neo4j: true
ptopic: "[[topic-ANTHROPOLOGY]]"
level: 5
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.THE-BIBLE",
    alias: "Topic: The Story of Redemption",
    parent: "topic.ANTHROPOLOGY",
    tags: ["literature", "scriptures", "hebrew", "greek", "linquistic"],
    level: 5
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.THE-BIBLE",
    en_title: "THE BIBLE",
    en_content: "The Sacred Scriptures of Christians comprising the Old Testament and the New Testament.",
    es_title: "LA BIBLIA",
    es_content: "Las Sagradas Escrituras de los cristianos que comprenden el Antiguo Testamento y el Nuevo Testamento.",
    fr_title: "LA BIBLE",
    fr_content: "Les Saintes Écritures des chrétiens comprenant l'Ancien Testament et le Nouveau Testament.",
    hi_title: "बाइबिल",
    hi_content: "ईसाईयों के पवित्र शास्त्र जिसमें पुराना नियम और नया नियम शामिल है।",
    zh_title: "Shèngjīng",
    zh_content: "Jīdū tú de shèngjīng, bāokuò jiù yuē hé xīn yuē."
});

// LINK DESCRIPTION
MATCH (t:TOPIC {name: "topic.THE-BIBLE"})
MATCH (d:DESCRIPTION {name: "desc.THE-BIBLE"})
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.THE-BIBLE"}]->(d);

// LINK PARENT
MATCH (p:TOPIC)
WHERE p.name = "topic.ANTHROPOLOGY"
MATCH (c:TOPIC)
WHERE c.name = "topic.THE-BIBLE"
MERGE (p)-[:HAS_CHILD {name: "edge.ANTHROPOLOGY->THE-BIBLE"}]->(c);

```
