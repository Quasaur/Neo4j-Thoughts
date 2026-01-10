---
name: topic.GRACE
alias: "Topic Gospel of Grace"
type: TOPIC
parent: topic.CREATION
tags:
- kindness
- blessing
- benevolence
- empower
- anointing
neo4j: true
ptopic: "[[topic-CREATION]]"
level: 3
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.GRACE",
    alias: "Topic Gospel of Grace",
    parent: "topic.CREATION",
    tags: ["kindness", "blessing", "benevolence", "empower", "anointing"],
    level: 3
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.GRACE",
    en_title: "GRACE",
    en_content: "Unmerited Divine Favor given to humans for their sanctification and regeneration; the same Favor God the Father bestows on His Only-Begotten Son Jesus Christ.",
    es_title: "GRACIA",
    es_content: "Favor Divino inmerecido dado a los humanos para su santificación y regeneración; el mismo Favor que Dios Padre otorga a Su Hijo Unigénito Jesucristo.",
    fr_title: "GRÂCE",
    fr_content: "Faveur divine imméritée accordée aux humains pour leur sanctification et leur régénération ; la même faveur que Dieu le Père accorde à son Fils unique Jésus-Christ.",
    hi_title: "कृपा",
    hi_content: "मनुष्यों को उनके पवित्रीकरण और पुनर्जन्म के लिए दिया गया अप्रतिभुत ईश्वरीय अनुग्रह; वही अनुग्रह जो पिता परमेश्वर ने अपने एकलौते पुत्र यीशु मसीह को प्रदान किया।",
    zh_title: "Ēndiǎn",
    zh_content: "Shàngdì wèile shǐ rénlèi chéng shèng hé chóngshēng ér cìyǔ rénlèi wúcháng de ēnhuì; tiānfù yě jiāng tóngyàng de ēnhuì cìyǔle tā de dúshēngzǐ yēsū jīdū."
});

// LINK DESCRIPTION
MATCH (t:TOPIC), (d:DESCRIPTION)
WHERE t.name = "topic.GRACE" AND d.name = "desc.GRACE"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.GRACE"}]->(d);

// LINK PARENT
MATCH (p:TOPIC), (c:TOPIC)
WHERE p.name = "topic.CREATION" AND c.name = "topic.GRACE"
MERGE (p)-[:HAS_CHILD {name: "edge.CREATION->GRACE"}]->(c);

```
