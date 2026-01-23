---
name: "thought.EVERYTHING FROM NOTHING"
alias: "Thought: Everything From Nothing"
type: THOUGHT
en_content: "Saying that everything came from nothing makes no sense."
parent: "topic.TRUTH"
tags:
- truth
- origin
- science
- creation
- logic
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 15-Oct-2011b)
CREATE (t:THOUGHT {
    name: "thought.EVERYTHING FROM NOTHING",
    alias: "Thought: Everything From Nothing",
    parent: "topic.TRUTH",
    tags: ['truth', 'origin', 'science', 'creation', 'logic'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.EVERYTHING FROM NOTHING",
    en_title: "Everything From Nothing",
    en_content: "Saying that everything came from nothing makes no sense.",
    es_title: "Todo De La Nada",
    es_content: "Decir que todo vino de la nada no tiene sentido.",
    fr_title: "Tout À Partir De Rien",
    fr_content: "Dire que tout est venu de rien n'a aucun sens.",
    hi_title: "शून्य से सब कुछ",
    hi_content: "यह कहना कि सब कुछ शून्य से आया है, इसका कोई अर्थ नहीं है।",
    zh_title: "Cong Wu Zhong Lai De Yiqie",
    zh_content: "Shuo yiqie dou cong wu zhong lai shi meiyou yiyi de."
});

MATCH (t:THOUGHT {name: "thought.EVERYTHING FROM NOTHING"})
MATCH (c:CONTENT {name: "content.EVERYTHING FROM NOTHING"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.EVERYTHING FROM NOTHING" }]->(c);

MATCH (parent:TOPIC {name: "topic.TRUTH"})
MATCH (child:THOUGHT {name: "thought.EVERYTHING FROM NOTHING"})
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >EVERYTHING FROM NOTHING" }]->(child);
```
