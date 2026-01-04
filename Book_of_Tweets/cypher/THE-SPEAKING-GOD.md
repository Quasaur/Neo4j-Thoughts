---
name: "thought.THE SPEAKING GOD"
alias: "Thought: Divine Word"
parent: "topic.THE GODHEAD"
tags:
- divine_word
- divine_speech
- creation_act
- sovereignty
- revelation
level: 1
neo4j: true
insert: true
---
# The Speaking God

> [!Thought-en]
> It's been said that the only thing God has ever done is talk...what do you think?

```Cypher
CREATE (t:THOUGHT {
    name: "thought.THE SPEAKING GOD",
    alias: "Thought: Divine Word",
    parent: "topic.THE GODHEAD",
    tags: ["divine_word", "divine_speech", "creation_act", "sovereignty", "revelation"],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.THE SPEAKING GOD",
    en_title: "The Speaking God",
    en_content: "It's been said that the only thing God has ever done is talk...what do you think?",
    es_title: "El Dios habla",
    es_content: "Se ha dicho que lo único que Dios ha hecho es hablar... ¿qué piensas tú?",
    fr_title: "Le Dieu parle",
    fr_content: "On a dit que la seule chose que Dieu ait jamais faite, c'est parler... qu'en penses-tu ?",
    hi_title: "bolane vaala bhagavaan",
    hi_content: "कहा गया है कि भगवान ने जो एकमात्र काम किया है वह है बात करना... आप क्या सोचते हैं?",
    zh_title: "shuō huà de shèng",
    zh_content: "yǒu rén shuō shàng dì zuò guò de wéi yī de shì jiù shì shuō huà... nǐ zěn me kàn ?"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE SPEAKING GOD" AND c.name = "content.THE SPEAKING GOD"
MERGE (t)-[:HAS_CONTENT {name: "edge.THE SPEAKING GOD"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.THE SPEAKING GOD"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE GODHEAD >THE SPEAKING GOD"}]->(child);
```
