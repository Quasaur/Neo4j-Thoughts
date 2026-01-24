---
name: "thought.ANOTHER_SINNER"
alias: "Thought: ANOTHER SINNER"
type: THOUGHT
parent: topic.EVIL
tags:
- satan
- sinner
- inferior
- god
- christ
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.ANOTHER_SINNER",
    alias: "Thought: ANOTHER SINNER",
    parent: "topic.EVIL",
    tags: ["satan", "sinner", "inferior", "god", "christ"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.ANOTHER_SINNER",
    en_title: "ANOTHER SINNER",
    en_content: "# Thought: TITLE
[!Thought-en]
Satan is just another sinner.

[!Pensamiento-es]
Satanás es sólo otro pecador.

[!Pensée-fr]
Satan n’est qu’un autre pécheur.

[!सोचा-hi]
शैतान भी एक पापी है।

[!思考-zh]
撒旦只不过是另一个罪人。",
    es_title: "OTRO PECADOR",
    es_content: "# Pensamiento: TÍTULO
[!Pensamiento-es]
Satanás es simplemente otro pecador.

[!Pensamiento-es]
Satanás es solo otro pecador.

[!Pensée-fr]
Satan n'est qu'un autre pécheur.

[!सोचा-hola]
शैतरन भी एक परपी है।

[!Piensa-zh]
Satanás es simplemente otro pecador.",
    fr_title: "UN AUTRE PÉCHEUR",
    fr_content: "# Pensée : TITRE
[!Pensée-fr]
Satan n'est qu'un autre pécheur.

[!Pensamiento-es]
Satanás est seul ou un autre pécheur.

[!Pensée-fr]
Satan n’est qu’un autre pêcheur.

[!सोचा-salut]
शैतरन भी एक परपी है।

[!Think-zh]
Satan n'est qu'un autre pécheur.",
    hi_title: "एक और पापी",
    hi_content: "# विचार: शीर्षक
[!विचार-एन]
शैतान एक और पापी है.

[!पेन्सामिएंटो-एस]
सतानास एकल ओट्रो पेकाडोर है।

[!पेन्सी-fr]
शैतान ने एक घंटे से भी कम समय बिताया है।

[!सोचा-हाय]
शैतान भी एक परपी है।

[!सोचें-zh]
शैतान एक और पापी है.",
    zh_title: "lìng yí gè zuì rén",
    zh_content: "# Thought: TITLE
[!Thought-en]
Satan is just another sinner.

[!Pensamiento-es]
Satanás es sólo otro pecador.

[!Pensée-fr]
Satan n’est qu’un autre pécheur.

[!सोचा-hi]
शैतान भी एक पापी है।

[! sī kǎo -zh]
 sā dàn zhǐ bù guò shì lìng yí gè zuì rén 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.ANOTHER_SINNER" AND c.name = "content.ANOTHER_SINNER"
MERGE (t)-[:HAS_CONTENT {name: "edge.ANOTHER_SINNER"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.ANOTHER_SINNER"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.EVIL->ANOTHER_SINNER"}]->(child);
```
