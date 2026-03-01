---
type: PASSAGE
name: "passage.REMOVING ALL THINGS"
alias: "Passage: Removing All Things"
parent: "topic.DIVINE SOVEREIGNTY"
en_content: "\"I will completely remove all things from the face of the earth.\""
tags: ["judgment", "sovereignty", "bible", "earth", "prophecy"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
---





```Cypher
CREATE (t:PASSAGE {
    name: "passage.REMOVING ALL THINGS",
    alias: "Passage: Removing All Things",
    parent: "topic.DIVINE SOVEREIGNTY",
    tags: ["judgment", "sovereignty", "bible", "earth", "prophecy"],

    level: 2                   
});

CREATE (c:CONTENT {
    name: "content.REMOVING ALL THINGS",
    en_title: "Removing All Things",
    en_content: "\"I will completely remove all things from the face of the earth.\"",
    es_title: "Eliminando todas las cosas",
    es_content: "«Eliminaré por completo todas las cosas de la faz de la tierra», — Dios",
    fr_title: "Suppression de toutes choses",
    fr_content: "« Je supprimerai complètement toutes choses de la surface de la terre », — Dieu",
    hi_title: "सभी चीज़ों को हटाना",
    hi_content: ""\मैं धरती की सतह से सभी चीज़ों को पूरी तरह हटा दूँगा,"\ -- ईश्वर",
    zh_title: "Qīngchú wànwù",
    zh_content: "“\wǒ bì jiāng dìshàng de yīqiè chèdǐ qīngchú.”\——Shàngdì"
});

MATCH (t:PASSAGE {name: "passage.REMOVING ALL THINGS"})
MATCH (c:CONTENT {name: "content.REMOVING ALL THINGS"})
MERGE (t)-[:HAS_CONTENT {name: "p.edge.REMOVING ALL THINGS"}]->(c);

MATCH (parent:TOPIC {name: "topic.DIVINE SOVEREIGNTY"})
MATCH (child:PASSAGE {name: "passage.REMOVING ALL THINGS"})
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.DIVINE SOVEREIGNTY->REMOVING ALL THINGS"}]->(child);
```
