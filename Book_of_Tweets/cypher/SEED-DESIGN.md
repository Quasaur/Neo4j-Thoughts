---
name: "thought.SEED DESIGN"
alias: "Thought: Seed Design"
type: THOUGHT
en_content: "Seeds are designed to know when their environment is appropriate for germination...God is Great!"
parent: "topic.CREATION"
tags:
- design
- seeds
- nature
- creation
- life
level: 2
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 22-Apr-2011e)
CREATE (t:THOUGHT {
    name: "thought.SEED DESIGN",
    alias: "Thought: Seed Design",
    parent: "topic.CREATION",
    tags: ['design', 'seeds', 'nature', 'creation', 'life'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.SEED DESIGN",
    en_title: "Seed Design",
    en_content: "Seeds are designed to know when their environment is appropriate for germination...God is Great!",
    es_title: "Diseño de las Semillas",
    es_content: "Las semillas están diseñadas para saber cuándo su ambiente es apropiado para la germinación...¡Dios es Grande!",
    fr_title: "Conception des Graines",
    fr_content: "Les graines sont conçues pour savoir quand leur environnement est approprié pour la germination...Dieu est Grand !",
    hi_title: "बीज की रचना",
    hi_content: "बीज इस प्रकार रचे गए हैं कि वे जान सकें कि उनका वातावरण अंकुरण के लिए उपयुक्त है...परमेश्वर महान है!",
    zh_title: "Zhǒngzi Shèjì",
    zh_content: "Zhǒngzi bèi shèjì dé zhīdào tāmen de huánjìng héshí shìhé fāyá...Shén shì wěidà de!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SEED DESIGN" AND c.name = "content.SEED DESIGN"
MERGE (t)-[:HAS_CONTENT { "name": "edge.SEED DESIGN" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.CREATION" AND child.name = "thought.SEED DESIGN"
MERGE (parent)-[:HAS_THOUGHT { "name": "CREATION >SEED DESIGN" }]->(child);
```
