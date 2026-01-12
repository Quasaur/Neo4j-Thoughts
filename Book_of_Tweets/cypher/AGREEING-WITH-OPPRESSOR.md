---
name: "thought.AGREEING WITH OPPRESSOR"
alias: "Thought: Agreeing With Oppressor"
type: THOUGHT
en_content: "Every day we do things to let the Opressor know that we AGREE that his money is worth more than justice, dignity, equity and honor."
parent: "topic.MORALITY"
tags:
- oppression
- dignity
- money
- morality
- society
level: 3
neo4j: true
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 12-Oct-2012e)
CREATE (t:THOUGHT {
    name: "thought.AGREEING WITH OPPRESSOR",
    alias: "Thought: Agreeing With Oppressor",
    parent: "topic.MORALITY",
    tags: ['oppression', 'dignity', 'money', 'morality', 'society'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.AGREEING WITH OPPRESSOR",
    en_title: "Agreeing With Oppressor",
    en_content: "Every day we do things to let the Opressor know that we AGREE that his money is worth more than justice, dignity, equity and honor.",
    es_title: "De Acuerdo con el Opresor",
    es_content: "Cada día hacemos cosas para hacerle saber al Opresor que ESTAMOS DE ACUERDO en que su dinero vale más que la justicia, la dignidad, la equidad y el honor.",
    fr_title: "Accord avec l'Oppresseur",
    fr_content: "Chaque jour, nous faisons des choses pour faire savoir à l'Oppresseur que nous ACCEPTONS que son argent vaut plus que la justice, la dignité, l'équité et l'honneur.",
    hi_title: "उत्पीड़क से सहमति",
    hi_content: "हर दिन हम ऐसे काम करते हैं जिससे उत्पीड़क को पता चल जाए कि हम सहमत हैं कि उसका पैसा न्याय, सम्मान, समानता और मर्यादा से अधिक मूल्यवान है।",
    zh_title: "Yǔ yāpòzhě yīzhì",
    zh_content: "Měitiān wǒmen dōu zài zuò yīxiē shìqíng, ràng yāpòzhě zhīdào wǒmen tóngyì tā de jīnqián bǐ zhèngyì, zūnyán, gōngpíng hé róngyù gèng yǒu jiàzhí."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.AGREEING WITH OPPRESSOR" AND c.name = "content.AGREEING WITH OPPRESSOR"
MERGE (t)-[:HAS_CONTENT { "name": "edge.AGREEING WITH OPPRESSOR" }]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.AGREEING WITH OPPRESSOR"
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >AGREEING WITH OPPRESSOR" }]->(child);
```
