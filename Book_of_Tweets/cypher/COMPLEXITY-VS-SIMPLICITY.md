---
name: "thought.COMPLEXITY VS SIMPLICITY"
alias: "Thought: Complexity Vs Simplicity"
type: THOUGHT
en_content: "There is no \"natural law\" that would bring complexity out of simplicity!"
parent: "topic.TRUTH"
tags:
- complexity
- simplicity
- science
- law
- truth
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Oct-2011b)
CREATE (t:THOUGHT {
    name: "thought.COMPLEXITY VS SIMPLICITY",
    alias: "Thought: Complexity Vs Simplicity",
    parent: "topic.TRUTH",
    tags: ['complexity', 'simplicity', 'science', 'law', 'truth'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.COMPLEXITY VS SIMPLICITY",
    en_title: "Complexity Vs Simplicity",
    en_content: "There is no \"natural law\" that would bring complexity out of simplicity!",
    es_title: "Complejidad Versus Simplicidad",
    es_content: "¡No existe ninguna \"ley natural\" que pueda traer complejidad de la simplicidad!",
    fr_title: "Complexité Contre Simplicité",
    fr_content: "Il n'existe aucune \"loi naturelle\" qui ferait naître la complexité de la simplicité !",
    hi_title: "जटिलता बनाम सरलता",
    hi_content: "कोई \"प्राकृतिक नियम\" नहीं है जो सरलता से जटिलता ला सके!",
    zh_title: "Fùzá Duìbǐ Jiǎndān",
    zh_content: "Méiyǒu shénme \"zìrán fǎzé\" huì cóng jiǎndān zhōng chǎnshēng fùzá!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.COMPLEXITY VS SIMPLICITY" AND c.name = "content.COMPLEXITY VS SIMPLICITY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.COMPLEXITY VS SIMPLICITY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.TRUTH" AND child.name = "thought.COMPLEXITY VS SIMPLICITY"
MERGE (parent)-[:HAS_THOUGHT { "name": "TRUTH >COMPLEXITY VS SIMPLICITY" }]->(child);
```
