---
name: "thought.GOD HAS SENSE"
alias: "Thought: God Has Sense"
type: THOUGHT
en_content: "God has sense: if you talk to Him He'll talk to you; if you listen to Him He'll listen to you; if you'll honor Him He'll honor you."
parent: "topic.SPIRITUALITY"
tags:
- relationship
- communication
- honor
- spirituality
- god
level: 2
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Nov-2011a)
CREATE (t:THOUGHT {
    name: "thought.GOD HAS SENSE",
    alias: "Thought: God Has Sense",
    parent: "topic.SPIRITUALITY",
    tags: ['relationship', 'communication', 'honor', 'spirituality', 'god'],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.GOD HAS SENSE",
    en_title: "God Has Sense",
    en_content: "God has sense: if you talk to Him He'll talk to you; if you listen to Him He'll listen to you; if you'll honor Him He'll honor you.",
    es_title: "Dios Tiene Sentido",
    es_content: "Dios tiene sentido: si le hablas, Él te hablará; si le escuchas, Él te escuchará; si le honras, Él te honrará.",
    fr_title: "Dieu a du Sens",
    fr_content: "Dieu a du sens : si tu lui parles, Il te parlera ; si tu l'écoutes, Il t'écoutera ; si tu l'honores, Il t'honorera.",
    hi_title: "परमेश्वर के पास समझ है",
    hi_content: "परमेश्वर के पास समझ है: यदि तुम उससे बात करोगे तो वह तुमसे बात करेगा; यदि तुम उसकी सुनोगे तो वह तुम्हारी सुनेगा; यदि तुम उसका सम्मान करोगे तो वह तुम्हारा सम्मान करेगा।",
    zh_title: "Shàngdì yǒu dàolǐ",
    zh_content: "Shàngdì yǒu dàolǐ: rúguǒ nǐ gēn Tā shuōhuà, Tā jiù huì gēn nǐ shuōhuà; rúguǒ nǐ tīng Tā de huà, Tā jiù huì tīng nǐ de huà; rúguǒ nǐ zūnjìng Tā, Tā jiù huì zūnjìng nǐ."
});

MATCH (t:THOUGHT {name: "thought.GOD HAS SENSE"})
MATCH (c:CONTENT {name: "content.GOD HAS SENSE"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.GOD HAS SENSE" }]->(c);

MATCH (parent:TOPIC {name: "topic.SPIRITUALITY"})
MATCH (child:THOUGHT {name: "thought.GOD HAS SENSE"})
MERGE (parent)-[:HAS_THOUGHT { "name": "SPIRITUALITY >GOD HAS SENSE" }]->(child);
```
