---
name: "thought.DESPISING_THE_CROSS"
alias: "Thought: DESPISING THE CROSS"
type: THOUGHT
parent: topic.EVIL
tags:
- cross
- salvation
- gospel
- lakeoffire
- jesuschrist
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DESPISING_THE_CROSS",
    alias: "Thought: DESPISING THE CROSS",
    parent: "topic.EVIL",
    tags: ["cross", "salvation", "gospel", "lakeoffire", "jesuschrist"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.DESPISING_THE_CROSS",
    en_title: "DESPISING THE CROSS",
    en_content: "A myriad excuses are offered for the most heinous of crimes…yet beyond any reasonable doubt, the one who despises The Cross of Jesus Christ deserves to burn in the Lake of Fire FOREVER.
John 16:7-9",
    es_title: "DESpreciando la cruz",
    es_content: "Se ofrecen innumerables excusas para los crímenes más atroces... sin embargo, más allá de cualquier duda razonable, aquel que desprecia la Cruz de Jesucristo merece arder en el Lago de Fuego PARA SIEMPRE.
Juan 16:7-9",
    fr_title: "MÉPRISER LA CROIX",
    fr_content: "Une myriade d’excuses sont offertes pour les crimes les plus odieux… pourtant, au-delà de tout doute raisonnable, celui qui méprise la Croix de Jésus-Christ mérite de brûler dans l’étang de feu POUR TOUJOURS.
Jean 16 : 7-9",
    hi_title: "क्रूस का तिरस्कार करना",
    hi_content: "सबसे जघन्य अपराधों के लिए असंख्य बहाने पेश किए जाते हैं... फिर भी किसी भी उचित संदेह से परे, जो यीशु मसीह के क्रॉस का तिरस्कार करता है वह हमेशा के लिए आग की झील में जलने का हकदार है।
यूहन्ना 16:7-9",
    zh_title: "miǎo shì shí zì jià",
    zh_content: "rén men wèi zuì lìng rén fà zhǐ de zuì xíng tí gōng liǎo wú shù de jiè kǒu …… dàn háo wú yí wèn ， miè shì yē sū jī dū shí zì jià de rén yīng gāi yǒng yuǎn zài huǒ hú zhōng rán shāo 。
 yuē hàn fú yīn  16:7-9"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DESPISING_THE_CROSS" AND c.name = "content.DESPISING_THE_CROSS"
MERGE (t)-[:HAS_CONTENT {name: "edge.DESPISING_THE_CROSS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.EVIL" AND child.name = "thought.DESPISING_THE_CROSS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.EVIL->DESPISING_THE_CROSS"}]->(child);
```
