---
name: "thought.CHRONIC SELF DESTRUCTION"
alias: "Thought: Chronic Self Destruction"
type: THOUGHT
en_content: "As a species the homosapien is chronically self-destructive and IT CANNOT STOP ITSELF...therefore God must judge it."
parent: "topic.HUMANITY"
tags:
- humanity
- destruction
- judgment
- failure
- species
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 10-Sep-2011c)
CREATE (t:THOUGHT {
    name: "thought.CHRONIC SELF DESTRUCTION",
    alias: "Thought: Chronic Self Destruction",
    parent: "topic.HUMANITY",
    tags: ['humanity', 'destruction', 'judgment', 'failure', 'species'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CHRONIC SELF DESTRUCTION",
    en_title: "Chronic Self Destruction",
    en_content: "As a species the homosapien is chronically self-destructive and IT CANNOT STOP ITSELF...therefore God must judge it.",
    es_title: "Autodestrucción Crónica",
    es_content: "Como especie, el homosapiens es crónicamente autodestructivo y NO PUEDE DETENERSE... por lo tanto, Dios debe juzgarlo.",
    fr_title: "Auto-Destruction Chronique",
    fr_content: "En tant qu'espèce, l'homo sapiens est chroniquement autodestructeur et IL NE PEUT S'ARRÊTER... par conséquent, Dieu doit le juger.",
    hi_title: "दीर्घकालिक आत्म-विनाश",
    hi_content: "एक प्रजाति के रूप में मानव दीर्घकालिक रूप से आत्म-विनाशकारी है और यह खुद को रोक नहीं सकता... इसलिए परमेश्वर को इसका न्याय करना होगा।",
    zh_title: "Mànxìng Zìwǒ Huǐmiè",
    zh_content: "Zuòwéi yī gè wùzhǒng, Zhìrén mànxìng de zìwǒ huǐmiè, Érqiě TĀ WÚFǍ ZÌJǏ TÍNGZHǏ... Yīncǐ Shàngdì bìxū shěnpàn tā."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CHRONIC SELF DESTRUCTION" AND c.name = "content.CHRONIC SELF DESTRUCTION"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHRONIC SELF DESTRUCTION" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.CHRONIC SELF DESTRUCTION"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >CHRONIC SELF DESTRUCTION" }]->(child);
```
