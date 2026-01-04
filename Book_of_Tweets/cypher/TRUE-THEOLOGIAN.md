---
name: "thought.TRUE THEOLOGIAN"
alias: "Thought: Knowing God Personally"
type: THOUGHT
tags:
- theology
- encounter
- personal_relation
- knowing_god
- spirituality
en_content: "Can a theologian who has not had a personal encounter with God be truly called a theologian?"
parent: topic.SPIRITUALITY
level: 2
neo4j: true
insert: true
---

```Cypher
// Generated from Book6E-FINAL.md
CREATE (t:THOUGHT {
    name: "thought.TRUE THEOLOGIAN",
    alias: "Thought: TRUE THEOLOGIAN",
    parent: "topic.SPIRITUALITY",
    tags: ["theology", "encounter", "personal_relation", "knowing_god", "spirituality"],
    notes: "",
    level: 2
});

CREATE (c:CONTENT {
    name: "content.TRUE THEOLOGIAN",
    en_title: "TRUE THEOLOGIAN",
    en_content: "Can a theologian who has not had a personal encounter with God be truly called a theologian?",
    es_title: "VERDADERO TEÓLOGO",
    es_content: "¿Puede un teólogo que no ha tenido un encuentro personal con Dios ser llamado verdaderamente teólogo?",
    fr_title: "VRAI THÉOLOGIEN",
    fr_content: "Un théologien qui n'a pas eu de rencontre personnelle avec Dieu peut-il être vraiment appelé théologien ?",
    hi_title: "सच्चा धर्मशास्त्री",
    hi_content: "क्या वह धर्मशास्त्री जिसने ईश्वर के साथ व्यक्तिगत मुलाकात नहीं की है, वास्तव में धर्मशास्त्री कहला सकता है?"
    zh_title: "zhēn shén xué jiā",
    zh_content: "yī gè méi yǒu yǔ shàng dì jìn xíng guò gè rén jiē chù de shén xué jiā ， zhēn de néng bèi chēng wéi shén xué jiā ma ？"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.TRUE THEOLOGIAN" AND c.name = "content.TRUE THEOLOGIAN"
MERGE (t)-[:HAS_CONTENT {name: "edge.TRUE THEOLOGIAN"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITUALITY" AND child.name = "thought.TRUE THEOLOGIAN"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.SPIRITUALITY >TRUE THEOLOGIAN"}]->(child);
```
