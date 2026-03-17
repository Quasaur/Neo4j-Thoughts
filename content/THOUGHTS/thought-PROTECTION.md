---
type: THOUGHT
name: "thought.PROTECTION"
alias: "Thought: Protection"
en_content: |
  # PROTECTION
  Without the Holy Spirit of Christ humanity has no defense against the Devil, those who rule the world or even our own lower natures."
tags: ["holy_spirit", "spirit_of_truth", "standard", "defense", "jesus_christ"]
ptopic: "[[topic-THE-GODHEAD]]"
level: 1
neo4j: true
verified: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.PROTECTION",
    alias: "Thought: Protection",
    parent: "topic.THE GODHEAD",
    tags: ["holy_spirit", "spirit_of_truth", "standard", "defense", "jesus_christ"],
    level: 1
});

CREATE (c:CONTENT {
    name: "content.PROTECTION",
    ctype: "THOUGHT",
    en_title: "Protection",
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

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.PROTECTION"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE GODHEAD"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GODHEAD->PROTECTION"
RETURN t, parent;
```
