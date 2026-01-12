---
name: "thought.CARDBOARD BOX DIGNITY"
alias: "Thought: Cardboard Box Dignity"
type: THOUGHT
en_content: "I'd rather live in a cardboard box than to earn 6 figures and be treated like a pet!"
parent: "topic.HUMANITY"
tags:
- dignity
- wealth
- humanity
- character
- choice
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Oct-2012d)
CREATE (t:THOUGHT {
    name: "thought.CARDBOARD BOX DIGNITY",
    alias: "Thought: Cardboard Box Dignity",
    parent: "topic.HUMANITY",
    tags: ['dignity', 'wealth', 'humanity', 'character', 'choice'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.CARDBOARD BOX DIGNITY",
    en_title: "Cardboard Box Dignity",
    en_content: "I'd rather live in a cardboard box than to earn 6 figures and be treated like a pet!",
    es_title: "Dignidad en una Caja de Cartón",
    es_content: "¡Preferiría vivir en una caja de cartón que ganar seis cifras y ser tratado como una mascota!",
    fr_title: "Dignité dans une Boîte en Carton",
    fr_content: "Je préférerais vivre dans une boîte en carton plutôt que de gagner six chiffres et d'être traité comme un animal de compagnie !",
    hi_title: "गत्ते के डिब्बे में गरिमा",
    hi_content: "मैं छह अंकों की कमाई करने और पालतू जानवर की तरह व्यवहार किए जाने की तुलना में गत्ते के डिब्बे में रहना पसंद करूंगा!",
    zh_title: "Zhǐbǎn Xiāng Zūnyán",
    zh_content: "Wǒ nìngyuàn zhù zài zhǐbǎn xiāng lǐ, yě bù yuànyì zhuàn liùwèi shù de gōngzī rán'hòu bèi dàng zuò chǒngwù duìdài!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CARDBOARD BOX DIGNITY" AND c.name = "content.CARDBOARD BOX DIGNITY"
MERGE (t)-[:HAS_CONTENT { "name": "edge.CARDBOARD BOX DIGNITY" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMANITY" AND child.name = "thought.CARDBOARD BOX DIGNITY"
MERGE (parent)-[:HAS_THOUGHT { "name": "HUMANITY >CARDBOARD BOX DIGNITY" }]->(child);
```
