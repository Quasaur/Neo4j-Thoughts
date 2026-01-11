---
name: "thought.FIRST_RULE"
alias: "Thought: FIRST RULE"
type: THOUGHT
parent: topic.HUMOR
tags:
- humor
- comedy
- social
- media
- movie
neo4j: true
ptopic: "[[topic-HUMOR]]"
level: 5
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.FIRST_RULE",
    alias: "Thought: FIRST RULE",
    parent: "topic.HUMOR",
    tags: ["humor", "comedy", "social", "media", "movie"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.FIRST_RULE",
    en_title: "FIRST RULE",
    en_content: "# Thought: FIRST RULE
[!Thought-en]
First rule of Twitter: you do not talk about FaceBook. (dying of laughter).

[!Pensamiento-es]
Primera regla de Twitter: no hables de FaceBook. (muerto de risa).

[!Pensée-fr]
Première règle de Twitter : on ne parle pas de FaceBook. (mort de rire).

[!सोचा-hi]
ट्विटर का पहला नियम: आप फेसबुक के बारे में बात नहीं करते। (हंसते-हंसते लोटपोट हो जाते हैं)।

[!思考-zh]
Twitter 的第一条规则：不要谈论 FaceBook。（笑死我了）。",
    es_title: "PRIMERA REGLA",
    es_content: "# Pensamiento: PRIMERA REGLA
[!pensamiento-es]
Primera regla de Twitter: no se habla de Facebook. Morir de risa.

[!Pensamiento-es]
Primera regla de Twitter: nada de hábitos de Facebook. (arroz muerto).

[!Pensée-fr]
Primera regla de Twitter: nunca hables de Facebook. (muerte del llanto).

[!pensamiento-hola]
La primera regla de Twitter: no se habla de Facebook. (Rodando de risa).

[!pensando-zh]
Primera regla de Twitter: no hables de Facebook.",
    fr_title: "PREMIÈRE RÈGLE",
    fr_content: "# Pensée : PREMIÈRE RÈGLE
[!pensé-fr]
Première règle de Twitter : on ne parle pas de Facebook. Mourir de rire.

[!Pensamiento-es]
Première règle de Twitter : pas d'habitudes de Facebook. (riz mort).

[!Pensée-fr]
Première règle de Twitter : ne jamais parler de Facebook. (mort des pleurs).

[!pensé-salut]
La première règle de Twitter : on ne parle pas de Facebook. (Roulant de rire).

[!thinking-zh]
Première règle de Twitter : ne parlez pas de Facebook.",
    hi_title: "पहला नियम",
    hi_content: "# Thought: FIRST RULE
[!Thought-en]
First rule of Twitter: you do not talk about FaceBook. (dying of laughter).

[!Pensamiento-es]
Primera regla de Twitter: no hables de FaceBook. (muerto de risa).

[!Pensée-fr]
Première règle de Twitter : on ne parle pas de FaceBook. (mort de rire).

[!सोचा-hi]
ट्विटर का पहला नियम: आप फेसबुक के बारे में बात नहीं करते। (हंसते-हंसते लोटपोट हो जाते हैं)।

[!思考-zh]
Twitter 的第一条规则：不要谈论 FaceBook。（笑死我了）。",
    zh_title: "dì yī tiáo guī zé",
    zh_content: "#  xiǎng fǎ ： dì yī tiáo guī zé 
[!thought-en]
Twitter  de dì yī tiáo guī zé ： nǐ bù néng tán lùn  Facebook。 xiào sǐ le 。

[!Pensamiento-es]
Twitter  de dì yī tiáo guī zé ： méi yǒu  Facebook  de xí guàn 。 （ sǐ mǐ ）。

[!Pensée-fr]
Twitter  de dì yī tiáo guī zé ： yǒng yuǎn bú yào tán lùn  Facebook。 （ kū sǐ ）。

[！ sī xiǎng hāi ]
Twitter  de dì yī tiáo guī zé ： nǐ bù néng tán lùn  Facebook。 （ xiào dé dǎ gǔn ）。

[! sī kǎo -zh]
Twitter  de dì yī tiáo guī zé ： bú yào tán lùn  Facebook。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.FIRST_RULE" AND c.name = "content.FIRST_RULE"
MERGE (t)-[:HAS_CONTENT {name: "edge.FIRST_RULE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMOR" AND child.name = "thought.FIRST_RULE"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.HUMOR->FIRST_RULE"}]->(child);
```
