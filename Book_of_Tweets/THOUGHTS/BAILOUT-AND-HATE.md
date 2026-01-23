---
name: "thought.BAILOUT AND HATE"
alias: "Thought: Bailout And Hate"
type: THOUGHT
en_content: "Obama bailed out the Republicans...which made them hate him all the more."
parent: "topic.MORALITY"
tags:
- politics
- gratitude
- hate
- morality
- society
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Oct-2011c)
CREATE (t:THOUGHT {
    name: "thought.BAILOUT AND HATE",
    alias: "Thought: Bailout And Hate",
    parent: "topic.MORALITY",
    tags: ['politics', 'gratitude', 'hate', 'morality', 'society'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.BAILOUT AND HATE",
    en_title: "Bailout And Hate",
    en_content: "Obama bailed out the Republicans...which made them hate him all the more.",
    es_title: "Rescate y Odio",
    es_content: "Obama rescató a los republicanos... lo cual los hizo odiarlo aún más.",
    fr_title: "Renflouement et Haine",
    fr_content: "Obama a renflouer les républicains... ce qui les a fait le haïr encore plus.",
    hi_title: "सहायता और नफरत",
    hi_content: "ओबामा ने रिपब्लिकनों को बचाया... जिससे वे उनसे और अधिक नफरत करने लगे।",
    zh_title: "Jiùzhù hé chóuhèn 救助和仇恨",
    zh_content: "Àobāmǎ jiùzhù le Gònghédǎng rén... zhè shǐ tāmen gèng jiā chóuhèn tā. 奥巴马救助了共和党人...这使他们更加仇恨他。"
});

MATCH (t:THOUGHT {name: "thought.BAILOUT AND HATE"})
MATCH (c:CONTENT {name: "content.BAILOUT AND HATE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.BAILOUT AND HATE" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.BAILOUT AND HATE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >BAILOUT AND HATE" }]->(child);
```
