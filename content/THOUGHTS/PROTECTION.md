---
title: "Thought: PROTECTION"
draft: false
type: THOUGHT
mling: false
tags:
  - holy_spirit
  - spirit_of_truth
  - standard
  - defense
  - jesus_christ
neo4j: true
ptopic: "[[topic-THE-GODHEAD]]"
level: 1
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.PROTECTION",
    alias: "Thought: Strong Tower",
    parent: "topic.THE GODHEAD",
    tags: ["holy_spirit", "spirit_of_truth", "standard", "defense", "jesus_christ"],
    level: 1
});

CREATE (c:CONTENT {
    name: "content.PROTECTION",
    en_title: "PROTECTION",
    en_content: "# PROTECTION
Without the Holy Spirit of Christ humanity has no defense against the Devil, those who rule the world or even our own lower natures.",
    es_title: "PROTECCIÓN",
    es_content: "# PROTECCIÓN
Sin el Espíritu Santo de Cristo, la humanidad no tiene defensa contra el Diablo, aquellos que gobiernan el mundo o incluso nuestra propia naturaleza inferior.",
    fr_title: "PROTECTION",
    fr_content: "#PROTECTION
Sans le Saint-Esprit du Christ, l’humanité n’a aucune défense contre le Diable, contre ceux qui dirigent le monde ou même contre notre propre nature inférieure.",
    hi_title: "सुरक्षा",
    hi_content: "# सुरक्षा
मसीह की पवित्र आत्मा के बिना मानवता के पास शैतान से, दुनिया पर शासन करने वालों से या यहां तक कि हमारे अपने निम्न स्वभावों से कोई बचाव नहीं है।",
    zh_title: "bǎo hù",
    zh_content: "#  bǎo hù 
 méi yǒu jī dū de shèng líng ， rén lèi jiù wú fǎ dǐ yù mó guǐ 、 tǒng zhì shì jiè de rén ， shèn zhì wǒ men zì jǐ de dī děng běn xìng 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.PROTECTION" AND c.name = "content.PROTECTION"
MERGE (t)-[:HAS_CONTENT {name: "edge.PROTECTION"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.PROTECTION"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.THE GODHEAD->PROTECTION"}]->(child);
```
