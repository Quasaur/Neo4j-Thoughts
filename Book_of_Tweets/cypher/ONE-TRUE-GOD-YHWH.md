---
name: "thought.ONE TRUE GOD YHWH"
alias: "Thought: One True God Yhwh"
type: THOUGHT
en_content: "I believe there is One True God -- YHWH; and Jesus Christ is His Living Word! Hebrews 1:1-4"
parent: "topic.THE GODHEAD"
tags:
- god
- jesus
- word
- trinity
- truth
level: 1
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 11-Sep-2011)
CREATE (t:THOUGHT {
    name: "thought.ONE TRUE GOD YHWH",
    alias: "Thought: One True God Yhwh",
    parent: "topic.THE GODHEAD",
    tags: ['god', 'jesus', 'word', 'trinity', 'truth'],
    notes: "",
    level: 1
});

CREATE (c:CONTENT {
    name: "content.ONE TRUE GOD YHWH",
    en_title: "One True God Yhwh",
    en_content: "I believe there is One True God -- YHWH; and Jesus Christ is His Living Word! Hebrews 1:1-4",
    es_title: "Un Dios Verdadero Yhwh",
    es_content: "Creo que hay Un Dios Verdadero -- YHWH; y Jesucristo es Su Palabra Viviente! Hebreos 1:1-4",
    fr_title: "Un Seul Vrai Dieu Yhwh",
    fr_content: "Je crois qu'il y a Un Seul Vrai Dieu -- YHWH; et Jésus-Christ est Sa Parole Vivante! Hébreux 1:1-4",
    hi_title: "एक सच्चा परमेश्वर यहवा",
    hi_content: "मैं विश्वास करता हूँ कि एक सच्चा परमेश्वर है -- यहवा; और यीशु मसीह उसका जीवित वचन है! इब्रानियों 1:1-4",
    zh_title: "Wei Yi Zhen Shen Ye He Hua",
    zh_content: "Wo xiang xin you Yi Wei Zhen Shen -- YE HE HUA; Ye Su Ji Du shi Ta de Huo Po de Dao! Xi Bo Lai Shu 1:1-4"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ONE TRUE GOD YHWH" AND c.name = "content.ONE TRUE GOD YHWH"
MERGE (t)-[:HAS_CONTENT { "name": "edge.ONE TRUE GOD YHWH" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.ONE TRUE GOD YHWH"
MERGE (parent)-[:HAS_THOUGHT { "name": "THE GODHEAD >ONE TRUE GOD YHWH" }]->(child);
```
