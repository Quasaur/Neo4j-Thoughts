---
name: "thought.THE_END_OF_EVIL"
alias: "Thought: THE END OF EVIL"
type: THOUGHT
parent: topic.EVIL
tags:
- day
- evil
- cessation
- hope
- future
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.THE_END_OF_EVIL",
    alias: "Thought: THE END OF EVIL",
    parent: "topic.EVIL",
    tags: ["day", "evil", "cessation", "hope", "future"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.THE_END_OF_EVIL",
    en_title: "THE END OF EVIL",
    en_content: "# Thought: TNE END OF EVIL
[!Thought-en]
The Day is coming when evil will no longer exist.

[!Pensamiento-es]
Llegará el día en que el mal ya no existirá.

[!Pensée-fr]
Le jour viendra où le mal n’existera plus.

[!सोचा-hi]
वह दिन आ रहा है जब बुराई का अस्तित्व नहीं रहेगा।

[!思考-zh]
邪恶不再存在的那一天即将到来。",
    es_title: "EL FIN DEL MAL",
    es_content: "#Pensamiento: TNE FIN DEL MAL
[!Pensamiento-es]
Se acerca el día en que el mal ya no existirá.

[!Pensamiento-es]
Llegará el día en que el mal ya no existirá.

[!Pensée-fr]
Le jour viendra où le mal n'existera plus.

[!सोचा-hola]
वह दिन आ रहरहै जब बुररई कर ्तित्व नहीं रहेग।

[!Piensa-zh]
Se acerca el día en que el mal ya no existirá.",
    fr_title: "LA FIN DU MAL",
    fr_content: "#Pensée : LA FIN DU MAL
[!Pensée-fr]
Le jour vient où le mal n’existera plus.

[!Pensamiento-es]
Llegará el día en que el mal ya no existirá.

[!Pensée-fr]
Le jour viendra où le mal n’existera plus.

[!सोचा-salut]
वह दिन आ रहरहै जब बुररई कर अस्तित्व नहीं रहेग।

[!Think-zh]
Le jour vient où le mal n’existera plus.",
    hi_title: "बुराई का अंत",
    hi_content: "#विचार: बुराई का अंत
[!विचार-एन]
वह दिन आ रहा है जब बुराई का अस्तित्व नहीं रहेगा।

[!पेन्सामिएंटो-एस]
मुझे लगता है कि मेरा कोई अस्तित्व नहीं है.

[!पेन्सी-fr]
ले पत्रिकाएँ विन्द्रा ओउ ले माल नेक्सिस्टेरा प्लस।

[!सोचा-हाय]
वह दिन आ रहरहै जब बुरा करै अनुभव नहीं रहैग।

[!सोचें-zh]
वह दिन आ रहा है जब बुराई का अस्तित्व नहीं रहेगा।",
    zh_title: "xié è de zhōng jié",
    zh_content: "# Thought: TNE END OF EVIL
[!Thought-en]
The Day is coming when evil will no longer exist.

[!Pensamiento-es]
Llegará el día en que el mal ya no existirá.

[!Pensée-fr]
Le jour viendra où le mal n’existera plus.

[!सोचा-hi]
वह दिन आ रहा है जब बुराई का अस्तित्व नहीं रहेगा।

[! sī kǎo -zh]
 xié è bù zài cún zài de nà yī tiān jí jiāng dào lái 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE_END_OF_EVIL" AND c.name = "content.THE_END_OF_EVIL"
MERGE (t)-[:HAS_CONTENT {name: "edge.THE_END_OF_EVIL"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.THE_END_OF_EVIL"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.EVIL->THE_END_OF_EVIL"}]->(child);
```
