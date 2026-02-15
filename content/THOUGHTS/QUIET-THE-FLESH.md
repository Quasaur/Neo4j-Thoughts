---
name: "thought.QUIET_THE_FLESH"
alias: "Thought: QUIET THE FLESH"
type: THOUGHT
parent: "topic.GRACE"
en_content: "Only the Holy Spirit of Christ can truly quiet the flesh, providing fertile ground for discipline, self-control, and love towards others."
tags:
- flesh
- mortify
- crucify
- spirit
- holy
neo4j: true
ptopic: "[[topic-GRACE]]"
level: 3
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.QUIET_THE_FLESH",
    alias: "Thought: QUIET THE FLESH",
    parent: "topic.GRACE",
    tags: ["flesh", "mortify", "crucify", "spirit", "holy"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.QUIET_THE_FLESH",
    en_title: "QUIET THE FLESH",
    en_content: "Only the Holy Spirit of Christ can truly quiet the flesh, providing fertile ground for discipline, self-control, and love towards others.",
    es_title: "CALLAR LA CARNE",
    es_content: "Sólo el Espíritu Santo de Cristo puede verdaderamente aquietar la carne, proporcionando un terreno fértil para la disciplina, el autocontrol y el amor hacia los demás.",
	fr_title: "CALMER LA CHAIR",
    fr_content: "Seul le Saint-Esprit du Christ peut vraiment apaiser la chair, fournissant un terrain fertile pour la discipline, la maîtrise de soi et l’amour envers les autres.",
	hi_title: "मांस को शांत करो",
    hi_content: "केवल मसीह की पवित्र आत्मा ही वास्तव में शरीर को शांत कर सकती है, तथा अनुशासन, आत्म-नियंत्रण और दूसरों के प्रति प्रेम के लिए उपजाऊ भूमि प्रदान कर सकती है।",
	zh_title: "ràng ròu tǐ ān jìng xià lái",
    zh_content: "zhǐ yǒu jī dū de shèng líng cái néng zhēn zhèng píng jìng ròu tǐ ， wèi jì lǜ 、 zì wǒ kòng zhì hé ài tā rén tí gōng féi wò de tǔ rǎng 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.QUIET_THE_FLESH" AND c.name = "content.QUIET_THE_FLESH"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.QUIET_THE_FLESH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.QUIET_THE_FLESH"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.GRACE->QUIET_THE_FLESH"}]->(child);
```
