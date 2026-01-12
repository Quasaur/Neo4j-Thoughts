---
name: "thought.OPPORTUNITY FOR ANGER"
alias: "Thought: Opportunity For Anger"
type: THOUGHT
en_content: People don't need a reason to be angry...just an opportunity.
parent: topic.ATTITUDE
tags:
  - anger
  - attitude
  - character
  - human_nature
  - emotion
level: 3
neo4j: false
ptopic: "[[topic-ATTITUDE]]"
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 18-Dec-2011)
CREATE (t:THOUGHT {
    name: "thought.OPPORTUNITY FOR ANGER",
    alias: "Thought: Opportunity For Anger",
    parent: "topic.ATTITUDE",
    tags: ['anger', 'attitude', 'character', 'human_nature', 'emotion'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.OPPORTUNITY FOR ANGER",
    en_title: "Opportunity For Anger",
    en_content: "People don't need a reason to be angry...just an opportunity.",
    es_title: "Oportunidad Para La Ira",
    es_content: "Las personas no necesitan una razón para estar enojadas...solo una oportunidad.",
    fr_title: "Opportunité Pour La Colère",
    fr_content: "Les gens n'ont pas besoin d'une raison pour être en colère...juste d'une opportunité.",
    hi_title: "क्रोध के लिए अवसर",
    hi_content: "लोगों को गुस्सा होने के लिए किसी कारण की जरूरत नहीं...बस एक अवसर की।",
    zh_title: "Fen Nu De Ji Hui",
    zh_content: "Ren men bu xu yao sheng qi de li you...zhi xu yao yi ge ji hui."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.OPPORTUNITY FOR ANGER" AND c.name = "content.OPPORTUNITY FOR ANGER"
MERGE (t)-[:HAS_CONTENT { "name": "edge.OPPORTUNITY FOR ANGER" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ATTITUDE" AND child.name = "thought.OPPORTUNITY FOR ANGER"
MERGE (parent)-[:HAS_THOUGHT { "name": "ATTITUDE >OPPORTUNITY FOR ANGER" }]->(child);
```
