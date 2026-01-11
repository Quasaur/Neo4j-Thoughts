---
name: "thought.INVITE_OR_COMMAND?"
alias: "Thought: INVITE OR COMMAND"
type: THOUGHT
parent: topic.THE-GOSPEL
tags:
- repent
- invite
- command
- gospel
- judgment
neo4j: true
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.INVITE_OR_COMMAND?",
    alias: "Thought: INVITE OR COMMAND",
    parent: "topic.THE-GOSPEL",
    tags: ["repent", "invite", "command", "gospel", "judgment"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.INVITE_OR_COMMAND?",
    en_title: "INVITE OR COMMAND",
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

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.INVITE_OR_COMMAND?" AND c.name = "content.INVITE_OR_COMMAND?"
MERGE (t)-[:HAS_CONTENT {name: "edge.INVITE_OR_COMMAND?"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE-GOSPEL" AND child.name = "thought.INVITE_OR_COMMAND?"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE-GOSPEL->INVITE_OR_COMMAND?"}]->(child);
```
