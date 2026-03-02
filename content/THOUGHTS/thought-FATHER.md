---
type: THOUGHT
name: "thought.FATHER"
alias: "Thought: FATHER"
parent: "topic.GRACE"
tags: ["father", "flesh", "spirit", "knowledgeimmortality"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.FATHER",
    alias: "Thought: FATHER",
    parent: "topic.GRACE",
    tags: ["father", "flesh", "spirit", "knowledgeimmortality"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.FATHER",
    ctype: "THOUGHT",
    en_title: "FATHER",
    en_content: "I never got to know the father of my flesh; yet perhaps the greater tragedy is not getting to know the Father of my spirit.",
 es_title: "PADRE",
 es_content: "Nunca llegué a conocer al padre de mi carne; sin embargo, tal vez la mayor tragedia sea no conocer al Padre de mi espíritu.",
 fr_title: "PÈRE",
 fr_content: "Je n’ai jamais connu le père de ma chair ; mais peut-être que la plus grande tragédie est de ne pas connaître le Père de mon esprit.",
 hi_title: "पिता",
 hi_content: "मैं अपने शरीर के पिता को कभी नहीं जान पाया; फिर भी शायद सबसे बड़ी त्रासदी मेरी आत्मा के पिता को न जान पाना है।",
 zh_title: "fù qīn",
 zh_content: "wǒ cóng wèi rèn shí guò wǒ de qīn shēng fù qīn ； rán ér ， yě xǔ gèng dà de bēi jù shì wú fǎ rèn shí wǒ jīng shén zhī fù 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FATHER" AND c.name = "content.FATHER"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.FATHER"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.FATHER"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.GRACE->FATHER"}]->(child);
```