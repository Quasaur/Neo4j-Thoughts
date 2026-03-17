---
type: THOUGHT
name: "thought.INVITE OR COMMAND?"
alias: "Thought: Invite or Command"
parent: "topic.THE-GOSPEL"
en_content: |
  In American churches people are INVITED to receive the Gospel; this is a un-Biblical heresy.
  God COMMANDS all people to repent and believe the Gospel.
  Acts 17:30,31"
tags: ["repent", "invite", "command", "gospel", "judgment"]
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
neo4j: true
verified: false
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.INVITE OR COMMAND?",
    alias: "Thought: Invite or Command",
    parent: "topic.THE-GOSPEL",
    tags: ["repent", "invite", "command", "gospel", "judgment"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.INVITE OR COMMAND?",
    ctype: "THOUGHT",
    en_title: "Invite or Command",
    en_content: "In American churches people are INVITED to receive the Gospel; this is a un-Biblical heresy.
God COMMANDS all people to repent and believe the Gospel.
Acts 17:30,31",
    es_title: "INVITA O COMANDO",
    es_content: "En las iglesias americanas la gente está INVITADA a recibir el Evangelio; Esta es una herejía no bíblica.
Dios ORDENA a todas las personas que se arrepientan y crean en el Evangelio.
Hechos 17:30,31",
    fr_title: "INVITER OU COMMANDER",
    fr_content: "Dans les églises américaines, les gens sont INVITÉS à recevoir l’Évangile ; c'est une hérésie non biblique.
Dieu COMMANDE à tous les hommes de se repentir et de croire à l’Évangile.
Actes 17:30,31",
    hi_title: "आमंत्रित करें या आदेश दें",
    hi_content: "अमेरिकी चर्चों में लोगों को सुसमाचार प्राप्त करने के लिए आमंत्रित किया जाता है; यह एक गैर-बाइबिल विधर्म है।
भगवान सभी लोगों को पश्चाताप करने और सुसमाचार पर विश्वास करने का आदेश देते हैं।
अधिनियम 17:30,31",
    zh_title: "yāo qǐng huò mìng lìng",
    zh_content: "zài měi guó jiào huì zhōng ， rén men bèi yāo qǐng jiē shòu fú yīn ； zhè shì bù fú hé shèng jīng de yì duān 。
 shén mìng lìng suǒ yǒu rén huǐ gǎi bìng xiāng xìn fú yīn 。
 shǐ tú xíng chuán  17:30,31"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.INVITE OR COMMAND?"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.THE-GOSPEL"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.THE-GOSPEL->INVITE OR COMMAND?"
RETURN t, parent;
```
