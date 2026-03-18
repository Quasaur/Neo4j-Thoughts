---
type: THOUGHT
name: "thought.BAILOUT AND HATE"
alias: "Thought: Bailout And Hate"
parent: "topic.MORALITY"
en_content: "Obama bailed out the Republicans...which made them hate him all the more."
tags: ["politics", "gratitude", "hate", "morality", "society"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 06-Oct-2011c)
CREATE (t:THOUGHT {    name: "thought.BAILOUT AND HATE",
    alias: "Thought: Bailout And Hate",
    parent: "topic.MORALITY",
    tags: ['politics', 'gratitude', 'hate', 'morality', 'society'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.BAILOUT AND HATE",
    ctype: "THOUGHT",
    en_title: "Bailout And Hate",
    en_content: "Obama bailed out the Republicans...which made them hate him all the more.",
    es_title: "Rescate y Odio",
    es_content: "Obama rescató a los republicanos... lo cual los hizo odiarlo aún más.",
    fr_title: "Renflouement et Haine",
    fr_content: "Obama a renflouer les républicains... ce qui les a fait le haïr encore plus.",
    hi_title: "सहायता और नफरत",
    hi_content: "ओबामा ने रिपब्लिकनों को बचाया... जिससे वे उनसे और अधिक नफरत करने लगे।",
    zh_title: "Jiùzhù hé chóuhèn  jiù zhù hé chóu hèn",
    zh_content: "Àobāmǎ jiùzhù le Gònghédǎng rén... zhè shǐ tāmen gèng jiā chóuhèn tā.  ào bā mǎ jiù zhù le gòng hé dǎng rén ... zhè shǐ tā men gèng jiā chóu hèn tā 。"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.BAILOUT AND HATE"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->BAILOUT AND HATE"
RETURN t, parent;
```
