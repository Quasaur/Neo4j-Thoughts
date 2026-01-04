---
name: "thought.CHURCH AS LOVE GROUP"
alias: "Thought: Church As Love Group"
type: THOUGHT
en_content: "The number of hate groups has doubled the last 10 years. Where's the love groups? Oh yeah: that's what the CHURCH's supposed to be!"
parent: "topic.RELIGION"
tags:
- church
- love
- hate
- society
- religion
level: 3
neo4j: true
insert: true
---
# Church As Love Group

> [!Thought-en]
> The number of hate groups has doubled the last 10 years. Where's the love groups? Oh yeah: that's what the CHURCH's supposed to be!

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Aug-2012)
CREATE (t:THOUGHT {
    name: "thought.CHURCH AS LOVE GROUP",
    alias: "Thought: Church As Love Group",
    parent: "topic.RELIGION",
    tags: ['church', 'love', 'hate', 'society', 'religion'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CHURCH AS LOVE GROUP",
    en_title: "Church As Love Group",
    en_content: "The number of hate groups has doubled the last 10 years. Where's the love groups? Oh yeah: that's what the CHURCH's supposed to be!",
    es_title: "TITULO DEL PENSAMIENTO",
    es_content: "CONTENIDO DEL PENSAMIENTO",
    fr_title: "TITRE DE LA PENSÉE",
    fr_content: "CONTENU DE LA PENSÉE",
    hi_title: "शिखा",
    hi_content: "सामग्री",
    zh_title: "biāo tí",
    zh_content: "nèi róng"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CHURCH AS LOVE GROUP" AND c.name = "content.CHURCH AS LOVE GROUP"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHURCH AS LOVE GROUP" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.RELIGION" AND child.name = "thought.CHURCH AS LOVE GROUP"
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >CHURCH AS LOVE GROUP" }]->(child);
```