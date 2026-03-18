---
type: THOUGHT
name: "thought.DIGNITY OR DEATH"
alias: "Thought: Dignity Or Death"
parent: "topic.HUMANITY"
en_content: "Give me DIGNITY or give me death!"
tags: ["dignity", "freedom", "humanity", "character", "sacrifice"]
ptopic:
level: 3
neo4j: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Oct-2012b)
CREATE (t:THOUGHT {    name: "thought.DIGNITY OR DEATH",
    alias: "Thought: Dignity Or Death",
    parent: "topic.HUMANITY",
    tags: ['dignity', 'freedom', 'humanity', 'character', 'sacrifice'],
    level: 3});

CREATE (c:CONTENT {
    name: "content.DIGNITY OR DEATH",
    ctype: "THOUGHT",
    en_title: "Dignity Or Death",
    en_content: "Give me DIGNITY or give me death!",
    es_title: "Dignidad o Muerte",
    es_content: "¡Dame DIGNIDAD o dame muerte!",
    fr_title: "Dignité ou Mort",
    fr_content: "Donnez-moi la DIGNITÉ ou donnez-moi la mort !",
    hi_title: "सम्मान या मृत्यु",
    hi_content: "मुझे सम्मान दो या मुझे मृत्यु दो!",
    zh_title: "Zūnyán huò sǐwáng  zūn yán huò sǐ wáng",
    zh_content: "Gěi wǒ zūnyán, fǒuzé jiù gěi wǒ sǐwáng!  gěi wǒ zūn yán ， fǒu zé jiù gěi wǒ sǐ wáng ！"
});

MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DIGNITY OR DEATH"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.HUMANITY->DIGNITY OR DEATH"
RETURN t, parent;
```
