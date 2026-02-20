---
name: "thought.DIGNITY OR DEATH"
alias: "Thought: Dignity Or Death"
type: THOUGHT
en_content: "Give me DIGNITY or give me death!"
parent: "topic.HUMANITY"
tags:
- dignity
- freedom
- humanity
- character
- sacrifice
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Oct-2012b)
CREATE (t:THOUGHT {
    name: "thought.DIGNITY OR DEATH",
    alias: "Thought: Dignity Or Death",
    parent: "topic.HUMANITY",
    tags: ['dignity', 'freedom', 'humanity', 'character', 'sacrifice'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DIGNITY OR DEATH",
    en_title: "Dignity Or Death",
    en_content: "Give me DIGNITY or give me death!",
    es_title: "Dignidad o Muerte",
    es_content: "¡Dame DIGNIDAD o dame muerte!",
    fr_title: "Dignité ou Mort",
    fr_content: "Donnez-moi la DIGNITÉ ou donnez-moi la mort !",
    hi_title: "सम्मान या मृत्यु",
    hi_content: "मुझे सम्मान दो या मुझे मृत्यु दो!",
    zh_title: "Zūnyán huò sǐwáng 尊严或死亡",
    zh_content: "Gěi wǒ zūnyán, fǒuzé jiù gěi wǒ sǐwáng! 给我尊严，否则就给我死亡！"
});

MATCH (t:THOUGHT {name: "thought.DIGNITY OR DEATH"})
MATCH (c:CONTENT {name: "content.DIGNITY OR DEATH"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.DIGNITY OR DEATH" }]->(c);

MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MATCH (child:THOUGHT {name: "thought.DIGNITY OR DEATH"})
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY->DIGNITY OR DEATH" }]->(child);
```
