---
name: "thought.CRY OF POOR"
alias: "Thought: Cry Of Poor"
type: THOUGHT
en_content: "Whoever closes his ear to the cry of the poor will himself call out and not be answered. Proverbs 21:13, ESV"
parent: "topic.MORALITY"
tags:
- poor
- justice
- bible
- morality
- consequences
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 16-Oct-2012a)
CREATE (t:THOUGHT {
    name: "thought.CRY OF POOR",
    alias: "Thought: Cry Of Poor",
    parent: "topic.MORALITY",
    tags: ['poor', 'justice', 'bible', 'morality', 'consequences'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CRY OF POOR",
    en_title: "Cry Of Poor",
    en_content: "Whoever closes his ear to the cry of the poor will himself call out and not be answered. Proverbs 21:13, ESV",
    es_title: "Grito de los Pobres",
    es_content: "El que cierra su oído al clamor del pobre, él mismo clamará y no será oído. Proverbios 21:13, NVI",
    fr_title: "Cri des Pauvres",
    fr_content: "Celui qui ferme son oreille au cri du pauvre criera lui-même et ne sera pas exaucé. Proverbes 21:13, LSG",
    hi_title: "गरीबों की पुकार",
    hi_content: "जो गरीब की पुकार से अपना कान बंद करता है, वह स्वयं पुकारेगा और उत्तर नहीं पाएगा। नीतिवचन 21:13, ESV",
    zh_title: "Qiángrén de Hǎnjiào",
    zh_content: "Shéi duì qióngrén de hǎnjiào bīsè ěrduo, tā zìjǐ jiāng hǎnjiào què bùdé yìngdá. Zhēnyán 21:13, ESV"
});

MATCH (t:THOUGHT {name: "thought.CRY OF POOR"})
MATCH (c:CONTENT {name: "content.CRY OF POOR"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.CRY OF POOR" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.CRY OF POOR"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >CRY OF POOR" }]->(child);
```
