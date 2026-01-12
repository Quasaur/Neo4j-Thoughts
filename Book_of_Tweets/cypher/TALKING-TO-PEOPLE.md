---
name: "thought.TALKING TO PEOPLE"
alias: "Thought: Talking To People"
type: THOUGHT
en_content: "If you don't know how to talk to people, you probably shouldn't talk to people."
parent: "topic.WISDOM"
tags:
- communication
- wisdom
- social_skills
- discernment
- relationships
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Aug-2013a)
CREATE (t:THOUGHT {
    name: "thought.TALKING TO PEOPLE",
    alias: "Thought: Talking To People",
    parent: "topic.WISDOM",
    tags: ["communication", "wisdom", "social_skills", "discernment", "relationships"],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.TALKING TO PEOPLE",
    en_title: "Talking To People",
    en_content: "If you don't know how to talk to people, you probably shouldn't talk to people.",
    es_title: "Hablando con las Personas",
    es_content: "Si no sabes cómo hablar con las personas, probablemente no deberías hablar con las personas.",
    fr_title: "Parler aux Gens",
    fr_content: "Si vous ne savez pas comment parler aux gens, vous ne devriez probablement pas parler aux gens.",
    hi_title: "लोगों से बात करना",
    hi_content: "यदि आप नहीं जानते कि लोगों से कैसे बात करनी है, तो आपको शायद लोगों से बात नहीं करनी चाहिए।",
    zh_title: "Yu Ren Tan Hua",
    zh_content: "Ru Guo Ni Bu Zhi Dao Zen Yang Yu Ren Tan Hua, Ni Ke Neng Bu Ying Gai Yu Ren Tan Hua."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.TALKING TO PEOPLE" AND c.name = "content.TALKING TO PEOPLE"
MERGE (t)-[:HAS_CONTENT {name: "edge.TALKING TO PEOPLE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.WISDOM" AND child.name = "thought.TALKING TO PEOPLE"
MERGE (parent)-[:HAS_THOUGHT {name: "WISDOM >TALKING TO PEOPLE"}]->(child);
```
