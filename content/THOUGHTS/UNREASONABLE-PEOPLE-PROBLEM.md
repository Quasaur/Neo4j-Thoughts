---
name: "thought.UNREASONABLE PEOPLE PROBLEM"
alias: "Thought: Unreasonable People Problem"
type: THOUGHT
en_content: Life would be perfect but for the presence of unreasonable people.
parent: topic.WISDOM
tags:
  - people
  - reason
  - life
  - attitude
  - problem
level: 3
neo4j: true
ptopic: "[[topic-WISDOM]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Oct-2013a)
CREATE (t:THOUGHT {
    name: "thought.UNREASONABLE PEOPLE PROBLEM",
    alias: "Thought: Unreasonable People Problem",
    parent: "topic.ATTITUDE",
    tags: ['people', 'reason', 'life', 'attitude', 'problem'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.UNREASONABLE PEOPLE PROBLEM",
    en_title: "Unreasonable People Problem",
    en_content: "Life would be perfect but for the presence of unreasonable people.",
    es_title: "El Problema de la Gente Irrazonable",
    es_content: "La vida sería perfecta si no fuera por la presencia de personas irrazonables.",
    fr_title: "Le Problème des Gens Déraisonnables",
    fr_content: "La vie serait parfaite sans la présence de personnes déraisonnables.",
    hi_title: "अतार्किक लोगों की समस्या",
    hi_content: "जीवन संपूर्ण होता लेकिन अतार्किक लोगों की उपस्थिति इसे बिगाड़ देती है।",
    zh_title: "Bù lǐxìng zhī rén de wèntí 不理性之人的问题",
    zh_content: "Rúguǒ bù shì yīnwèi bù lǐxìng zhī rén de cúnzài, shēnghuó jiàng shì wánměi de. 如果不是因为不理性之人的存在，生活将是完美的。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.UNREASONABLE PEOPLE PROBLEM" AND c.name = "content.UNREASONABLE PEOPLE PROBLEM"
MERGE (t)-[:HAS_CONTENT { "name": "edge.UNREASONABLE PEOPLE PROBLEM" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.UNREASONABLE PEOPLE PROBLEM"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE->UNREASONABLE PEOPLE PROBLEM" }]->(child);
```
