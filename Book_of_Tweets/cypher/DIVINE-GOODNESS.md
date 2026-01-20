---
name: "thought.DIVINE GOODNESS"
alias: "Thought: Divine Goodness"
en_content: "It blows my mind how good God is to a person as wicked as I am."
parent: topic.THE GODHEAD
tags:
  - divine_goodness
  - divine_nature
  - holiness
  - worship
  - grace
level: 1
neo4j: false
ptopic: 
type: THOUGHT
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DIVINE GOODNESS",
    alias: "Thought: Divine Goodness",
    parent: "topic.THE GODHEAD",
    tags: ["divine_goodness", "divine_nature", "holiness", "worship", "grace"],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.DIVINE GOODNESS",
    en_title: "God is Good",
    en_content: "It blows my mind how good God is to a person as wicked as I am.",
    es_title: "Dios es bueno",
    es_content: "Me asombra lo bueno que es Dios con una persona tan malvada como yo.",
    fr_title: "Dieu est bon",
    fr_content: "Cela me dépasse de voir à quel point Dieu est bon envers une personne aussi méchante que moi.",
    hi_title: "bhagavaan achchha hai",
    hi_content: "यह मेरे होश उड़ा देता है कि भगवान मेरे जैसा दुष्ट व्यक्ति के लिए कितना अच्छा है।",
    zh_title: "shàng dì hǎo",
    zh_content: "shàng dì duì wǒ zhè yàng de è rén jìng rán rú cǐ zhī hǎo, zhēn shì lìng wǒ jīng tàn bú yǐ!"
});

MATCH (t:THOUGHT {name: "thought.DIVINE GOODNESS"})
MATCH (c:CONTENT {name: "content.DIVINE GOODNESS"})
MERGE (t)-[:HAS_CONTENT {name: "edge.DIVINE GOODNESS"}]->(c);

MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MATCH (child:THOUGHT {name: "thought.DIVINE GOODNESS"})
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE GODHEAD >DIVINE GOODNESS"}]->(child);
```
