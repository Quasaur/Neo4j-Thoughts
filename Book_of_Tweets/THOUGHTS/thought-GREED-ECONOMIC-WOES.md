---
type: THOUGHT
name: "thought.GREED ECONOMIC WOES"
alias: "Thought: Greed Economic Woes"
parent: "topic.MORALITY"
en_content: "The true source of our economic woes is GREED; therefore no recovery will ever be permanent until Christ returns."
tags: ["greed", "economy", "morality", "recovery", "society"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 19-Feb-2012d)
CREATE (t:THOUGHT {    name: "thought.GREED ECONOMIC WOES",
    alias: "Thought: Greed Economic Woes",
    parent: "topic.MORALITY",
    tags: ['greed', 'economy', 'morality', 'recovery', 'society'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.GREED ECONOMIC WOES",
    ctype: "THOUGHT",
    en_title: "Greed Economic Woes",
    en_content: "The true source of our economic woes is GREED; therefore no recovery will ever be permanent until Christ returns.",
    es_title: "Problemas Económicos por Codicia",
    es_content: "La verdadera fuente de nuestros problemas económicos es la CODICIA; por lo tanto, ninguna recuperación será permanente hasta que Cristo regrese.",
    fr_title: "Maux Économiques de l'Avarice",
    fr_content: "La véritable source de nos maux économiques est l'AVARICE ; par conséquent, aucune reprise ne sera jamais permanente jusqu'à ce que le Christ revienne.",
    hi_title: "लालच की आर्थिक समस्याएं",
    hi_content: "हमारी आर्थिक समस्याओं का वास्तविक स्रोत लालच है; इसलिए जब तक मसीह वापस नहीं आता, कोई भी सुधार कभी स्थायी नहीं होगा।",
    zh_title: "Tānlán Jīngjì Kùnnán",
    zh_content: "Wǒmen jīngjì kùnnán de zhēnzhèng gēnyuán shì TĀNLÁN; yīncǐ zài Jīdū zàilín zhīqián, rènhé fùsū dōu bù huì shì yǒngjiǔ de."
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.GREED ECONOMIC WOES"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.MORALITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.MORALITY->GREED ECONOMIC WOES"
RETURN t, parent;
```
