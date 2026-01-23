---
name: "thought.INCARCERATION SLAVERY PARALLEL"
alias: "Thought: Incarceration Slavery Parallel"
type: THOUGHT
en_content: "Today in the USA there are more black people incarcerated than there were black slaves in 1850. Thank you, America!"
parent: "topic.MORALITY"
tags:
- incarceration
- slavery
- america
- race
- justice
level: 3
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Aug-2013)
CREATE (t:THOUGHT {
    name: "thought.INCARCERATION SLAVERY PARALLEL",
    alias: "Thought: Incarceration Slavery Parallel",
    parent: "topic.MORALITY",
    tags: ['incarceration', 'slavery', 'america', 'race', 'justice'],
    notes: "",
    level: 3
});

CREATE (c:CONTENT {
    name: "content.INCARCERATION SLAVERY PARALLEL",
    en_title: "Incarceration Slavery Parallel",
    en_content: "Today in the USA there are more black people incarcerated than there were black slaves in 1850. Thank you, America!",
    es_title: "Paralelo entre Encarcelamiento y Esclavitud",
    es_content: "Hoy en los EE.UU. hay más personas negras encarceladas que esclavos negros en 1850. ¡Gracias, América!",
    fr_title: "Parallèle entre Incarcération et Esclavage",
    fr_content: "Aujourd'hui aux États-Unis, il y a plus de personnes noires incarcérées qu'il n'y avait d'esclaves noirs en 1850. Merci, Amérique !",
    hi_title: "कारावास और गुलामी की समानता",
    hi_content: "आज संयुक्त राज्य अमेरिका में 1850 में काले गुलामों की तुलना में अधिक काले लोग कैद में हैं। धन्यवाद, अमेरिका!",
    zh_title: "Jiānjìn yǔ núlì de lèibǐ 监秦与奴隶的类比",
    zh_content: "Jīntiān zài Měiguó, jīnyù de hēirén bǐ 1850 nián de hēirén núlì hái duō. Xièxiè nǐ, Měiguó! 今天在美国，监禦的黑人比1850年的黑人奴隶还多。谢谢你，美国！"
});

MATCH (t:THOUGHT {name: "thought.INCARCERATION SLAVERY PARALLEL"})
MATCH (c:CONTENT {name: "content.INCARCERATION SLAVERY PARALLEL"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.INCARCERATION SLAVERY PARALLEL" }]->(c);

MATCH (parent:TOPIC {name: "topic.MORALITY"})
MATCH (child:THOUGHT {name: "thought.INCARCERATION SLAVERY PARALLEL"})
MERGE (parent)-[:HAS_THOUGHT { "name": "MORALITY >INCARCERATION SLAVERY PARALLEL" }]->(child);
```
