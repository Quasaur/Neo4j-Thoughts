---
name: "thought.HORDES OF THE ABYSS"
alias: "Thought: Hordes Of The Abyss"
type: THOUGHT
en_content: "Humanity will be visited by the hordes of the Abyss because that is what it, by its deeds, asked for."
parent: "topic.EVIL"
tags:
- abyss
- hordes
- deeds
- judgment
- evil
level: 4
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Sep-2013d)
CREATE (t:THOUGHT {
    name: "thought.HORDES OF THE ABYSS",
    alias: "Thought: Hordes Of The Abyss",
    parent: "topic.EVIL",
    tags: ['abyss', 'hordes', 'deeds', 'judgment', 'evil'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.HORDES OF THE ABYSS",
    en_title: "Hordes Of The Abyss",
    en_content: "Humanity will be visited by the hordes of the Abyss because that is what it, by its deeds, asked for.",
    es_title: "Hordas del Abismo",
    es_content: "La humanidad será visitada por las hordas del Abismo porque eso es lo que, por sus actos, pidió.",
    fr_title: "Hordes de l'Abîme",
    fr_content: "L'humanité sera visitée par les hordes de l'Abîme parce que c'est ce qu'elle a demandé par ses actes.",
    hi_title: "अगाध गर्त की सेनाएं",
    hi_content: "मानवता पर अगाध गर्त की सेनाओं का आगमन होगा क्योंकि उसने अपने कर्मों द्वारा इसी की मांग की है।",
    zh_title: "Shenyuan Zhong Jun",
    zh_content: "Renlei jiang bei shenyuan zhong jun suofang, yinwei zhengshi renlei yi qi suowei suoyaoqiu de."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.HORDES OF THE ABYSS" AND c.name = "content.HORDES OF THE ABYSS"
MERGE (t)-[:HAS_CONTENT { "name": "edge.HORDES OF THE ABYSS" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.HORDES OF THE ABYSS"
MERGE (parent)-[:HAS_THOUGHT { "name": "EVIL >HORDES OF THE ABYSS" }]->(child);
```
