---
name: "topic.MUSICOLOGY"
alias: "Topic: Musicology"
type: TOPIC
parent: "topic.HUMANITY"
tags:
- musicology
- music
- study
- research
- history
- theory
neo4j: true
ptopic: "[[topic-HUMANITY]]"
level: 4
insert: true
---
# Topic: Musicology

```Cypher
CREATE (t:TOPIC {
    name: "topic.MUSICOLOGY",
    alias: "Topic: Musicology",
    parent: "topic.HUMANITY",
    tags: ["musicology", "music", "study", "research", "history", "theory"],
    notes: "",
    level: 4
});

CREATE (d:DESCRIPTION {
    name: "description.MUSICOLOGY",
    en_title: "Musicology",
    en_content: "The scholarly study of music, encompassing the historical, cultural, theoretical, and scientific aspects of music and its role in human society.",
    es_title: "Musicología",
    es_content: "El estudio académico de la música, que abarca los aspectos históricos, culturales, teóricos y científicos de la música y su papel en la sociedad humana.",
    fr_title: "Musicologie",
    fr_content: "L'étude savante de la musique, englobant les aspects historiques, culturels, théoriques et scientifiques de la musique et son rôle dans la société humaine.",
    hi_title: "संगीत विज्ञान",
    hi_content: "संगीत का विद्वतापूर्ण अध्ययन, जिसमें संगीत के ऐतिहासिक, सांस्कृतिक, सैद्धांतिक और वैज्ञानिक पहलुओं और मानव समाज में इसकी भूमिका को शामिल किया गया है।",
    zh_title: "yīn yuè xué",
    zh_content: "yīn yuè de xué shù yán jiū ， bāo kuò yīn yuè de lì shǐ 、 wén huà 、 lǐ lùn hé kē xué fāng miàn jí qí zài rén lèi shè huì zhōng de zuò yòng 。"
});

MATCH (t:TOPIC)
MATCH (d:DESCRIPTION)
WHERE t.name = "topic.MUSICOLOGY" AND d.name = "description.MUSICOLOGY"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.MUSICOLOGY"}]->(d);

MATCH (parent:TOPIC)
MATCH (child:TOPIC)
WHERE parent.name = "topic.HUMANITY" AND child.name = "topic.MUSICOLOGY"
MERGE (parent)-[:HAS_CHILD {name: "edge.HUMANITY->MUSICOLOGY"}]->(child);
```
