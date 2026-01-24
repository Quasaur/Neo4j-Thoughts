---
name: "thought.QUIET_THE_FLESH"
alias: "Thought: QUIET THE FLESH"
type: THOUGHT
parent: topic.GRACE
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
    en_content: "# Thought: QUIET THE FLESH
[!Thought-en]
Only the Holy Spirit of Christ can truly quiet the flesh, providing fertile ground for discipline, self-control, and love towards others.

[!Pensamiento-es]
Sólo el Espíritu Santo de Cristo puede verdaderamente aquietar la carne, proporcionando terreno fértil para la disciplina, el autocontrol y el amor hacia los demás.

[!Pensée-fr]
Sólo el Espíritu Santo de Cristo puede verdaderamente aquietar la carne, proporcionando terreno fértil para la disciplina, el autocontrol y el amor hacia los demás.

[!सोचा-hi]
केवल मसीह की पवित्र आत्मा ही वास्तव में शरीर को शांत कर सकती है, तथा अनुशासन, आत्म-नियंत्रण और दूसरों के प्रति प्रेम के लिए उपजाऊ भूमि प्रदान कर सकती है।

[!思考-zh]
只有基督的圣灵才能真正平静肉体，为纪律、自制和对他人的爱提供沃土。",
    es_title: "CALLAR LA CARNE",
    es_content: "#Pensamiento: CALLAR LA CARNE
[!pensamiento-es]
Sólo el Espíritu Santo de Cristo puede verdaderamente aquietar la carne, proporcionando un terreno fértil para la disciplina, el autocontrol y el amor hacia los demás.

[!Pensamiento-es]
Sólo el Espíritu Santo de Cristo puede verdaderamente aquietar la carne, proporcionando un terreno fértil para la disciplina, el autocontrol y el amor hacia los demás.

[!Pensée-fr]
Sólo el Espíritu Santo de Cristo puede verdaderamente aquietar la carne, proporcionando un terreno fértil para la disciplina, el autocontrol y el amor hacia los demás.

[!pensamiento-hola]
Sólo el Espíritu Santo de Cristo puede verdaderamente calmar la carne y proporcionar un terreno fértil para la disciplina, el autocontrol y el amor por los demás.

[!pensando-zh]
Sólo el Espíritu Santo de Cristo puede proporcionar el terreno para la verdadera paz mental, la disciplina, el autocontrol y el amor por los demás.",
    fr_title: "CALMER LA CHAIR",
    fr_content: "#Pensée : CALMER LA CHAIR
[!pensé-fr]
Seul le Saint-Esprit du Christ peut vraiment apaiser la chair, fournissant un terrain fertile pour la discipline, la maîtrise de soi et l’amour envers les autres.

[!Pensamiento-es]
Seul le Saint-Esprit du Christ peut véritablement apaiser la chair, fournissant un terrain fertile pour la discipline, la maîtrise de soi et l’amour envers les autres.

[!Pensée-fr]
Seul le Saint-Esprit du Christ peut véritablement apaiser la chair, fournissant un terrain fertile pour la discipline, la maîtrise de soi et l’amour envers les autres.

[!pensé-salut]
Seul le Saint-Esprit du Christ peut vraiment calmer la chair et fournir un terrain fertile pour la discipline, la maîtrise de soi et l’amour des autres.

[!thinking-zh]
Seul le Saint-Esprit du Christ peut fournir le terrain propice à une véritable tranquillité d’esprit, à la discipline, à la maîtrise de soi et à l’amour des autres.",
    hi_title: "मांस को शांत करो",
    hi_content: "# Thought: QUIET THE FLESH
[!Thought-en]
Only the Holy Spirit of Christ can truly quiet the flesh, providing fertile ground for discipline, self-control, and love towards others.

[!Pensamiento-es]
Sólo el Espíritu Santo de Cristo puede verdaderamente aquietar la carne, proporcionando terreno fértil para la disciplina, el autocontrol y el amor hacia los demás.

[!Pensée-fr]
Sólo el Espíritu Santo de Cristo puede verdaderamente aquietar la carne, proporcionando terreno fértil para la disciplina, el autocontrol y el amor hacia los demás.

[!सोचा-hi]
केवल मसीह की पवित्र आत्मा ही वास्तव में शरीर को शांत कर सकती है, तथा अनुशासन, आत्म-नियंत्रण और दूसरों के प्रति प्रेम के लिए उपजाऊ भूमि प्रदान कर सकती है।

[!思考-zh]
只有基督的圣灵才能真正平静肉体，为纪律、自制和对他人的爱提供沃土。",
    zh_title: "ràng ròu tǐ ān jìng xià lái",
    zh_content: "# xiǎng fǎ ： ràng ròu tǐ ān jìng xià lái 
[!thought-en]
 zhǐ yǒu jī dū de shèng líng cái néng zhēn zhèng píng jìng ròu tǐ ， wèi jì lǜ 、 zì wǒ kòng zhì hé ài tā rén tí gōng féi wò de tǔ rǎng 。

[!Pensamiento-es]
 zhǐ yǒu jī dū de shèng líng cái néng zhēn zhèng píng jìng ròu tǐ ， wèi jì lǜ 、 zì wǒ kòng zhì hé ài tā rén tí gōng féi wò de tǔ rǎng 。

[!Pensée-fr]
 zhǐ yǒu jī dū de shèng líng cái néng zhēn zhèng píng jìng ròu tǐ ， wèi jì lǜ 、 zì wǒ kòng zhì hé ài tā rén tí gōng féi wò de tǔ rǎng 。

[！ sī xiǎng hāi ]
 zhǐ yǒu jī dū de shèng líng cái néng zhēn zhèng píng jìng ròu tǐ ， bìng wèi zì lǜ 、 zì zhì hé ài tā rén tí gōng féi wò de tǔ rǎng 。

[! sī kǎo -zh]
 zhǐ yǒu jī dū de shèng líng cái néng wèi zhēn zhèng de xīn líng píng ān 、 zì lǜ 、 zì zhì hé ài tā rén tí gōng tǔ rǎng 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.QUIET_THE_FLESH" AND c.name = "content.QUIET_THE_FLESH"
MERGE (t)-[:HAS_CONTENT {name: "edge.QUIET_THE_FLESH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.QUIET_THE_FLESH"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.GRACE->QUIET_THE_FLESH"}]->(child);
```
