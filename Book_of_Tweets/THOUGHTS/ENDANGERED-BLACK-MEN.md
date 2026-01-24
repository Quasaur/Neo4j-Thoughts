---
name: "thought.ENDANGERED BLACK MEN"
alias: "Thought: Endangered Black Men"
type: THOUGHT
en_content: "African American men have ALWAYS been the targets of genocide...we are an ENDANGERED SPECIES."
parent: "topic.HUMANITY"
tags:
- race
- genocide
- target
- humanity
- justice
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 23-Mar-2012)
CREATE (t:THOUGHT {
    name: "thought.ENDANGERED BLACK MEN",
    alias: "Thought: Endangered Black Men",
    parent: "topic.HUMANITY",
    tags: ['race', 'genocide', 'target', 'humanity', 'justice'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.ENDANGERED BLACK MEN",
    en_title: "Endangered Black Men",
    en_content: "African American men have ALWAYS been the targets of genocide...we are an ENDANGERED SPECIES.",
    es_title: "Hombres Negros en Peligro de Extinción",
    es_content: "Los hombres afroamericanos SIEMPRE han sido objetivos de genocidio...somos una ESPECIE EN PELIGRO DE EXTINCIÓN.",
    fr_title: "Hommes Noirs en Danger",
    fr_content: "Les hommes afro-américains ont TOUJOURS été les cibles de génocide...nous sommes une ESPÈCE EN VOIE DE DISPARITION.",
    hi_title: "संकटग्रस्त अश्वेत पुरुष",
    hi_content: "अफ्रीकी अमेरिकी पुरुष हमेशा से नरसंहार के निशाने पर रहे हैं...हम एक संकटग्रस्त प्रजाति हैं।",
    zh_title: "Binwei Heiren Nanxing",
    zh_content: "Feizhou Yixi Meiguoren nanxing YIZHI dou shi zhongzu miesha de mubiao...women shi BINWEI WUZHONG."
});

MATCH (t:THOUGHT {name: "thought.ENDANGERED BLACK MEN"})
MATCH (c:CONTENT {name: "content.ENDANGERED BLACK MEN"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.ENDANGERED BLACK MEN" }]->(c);

MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MATCH (child:THOUGHT {name: "thought.ENDANGERED BLACK MEN"})
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY->ENDANGERED BLACK MEN" }]->(child);
```
