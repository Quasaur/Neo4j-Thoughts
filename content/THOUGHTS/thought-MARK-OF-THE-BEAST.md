---
type: THOUGHT
name: "thought.MARK OF THE BEAST"
alias: "Thought: Mark of the Beast"
parent: "topic.THE-GOSPEL"
en_content: |
  Do you not see...
  ...that by making the observance of Sunday the "Mark of the Beast" you are perverting the True Gospel and condemning all of Christendom to Eternal Damnation?!?!?
  Romans 14"
tags: ["gospel", "sunday", "sabbath", "faith", "works"]
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
neo4j: true
verified: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "\"thought.MARK OF THE BEAST\"",
    alias: "Thought: Mark of the Beast",
    parent: "\"topic.THE-GOSPEL\"",
    tags: ["gospel", "sunday", "sabbath", "faith", "works"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.MARK OF THE BEAST",
    ctype: "THOUGHT",
    en_title: "Mark of the Beast",
    en_content: "Do you not see...
...that by making the observance of Sunday the \\\"Mark of the Beast\\\" you are perverting the True Gospel and condemning all of Christendom to Eternal Damnation?!?!?
Romans 14",
    es_title: "MARCA DE LA BESTIA",
    es_content: "¿No ves...?
...que al hacer de la observancia del domingo la \\\"Marca de la Bestia\\\" estás pervirtiendo el Verdadero Evangelio y condenando a toda la cristiandad a la condenación eterna?!?!?
Romanos 14",
    fr_title: "",
    fr_content: "Ne vois-tu pas...
...qu'en faisant de l'observance du dimanche la « Marque de la Bête », vous pervertissez le véritable Évangile et condamnez toute la chrétienté à la damnation éternelle ?!?!?
Romains 14",
    hi_title: "जानवर का निशान",
    hi_content: "क्या तुम नहीं देखते...
...कि रविवार को \\\"जानवर का निशान\\\" बनाकर आप सच्चे सुसमाचार को विकृत कर रहे हैं और पूरे ईसाईजगत को शाश्वत विनाश की निंदा कर रहे हैं?!?!?
रोमियों 14",
    zh_title: "",
    zh_content: "nán dào nǐ méi kàn dào ...
... tōng guò jiāng xīng qī rì de zūn shǒu shì wèi “ yě shòu de yìn jì ”， nín zhèng zài wāi qū zhēn zhèng de fú yīn bìng qiǎn zé zhěng gè jī dū jiào shì jiè yǒng héng de zǔ zhòu ？！？！？
 luó mǎ shū  14"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.'"thought.MARK OF THE BEAST"'"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE-GOSPEL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE GOSPEL->MARK OF THE BEAST"thought.MARK OF THE BEAST"'"
RETURN t, parent;
```
