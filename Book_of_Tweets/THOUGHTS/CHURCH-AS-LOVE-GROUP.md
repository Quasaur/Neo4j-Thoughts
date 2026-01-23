---
name: "thought.CHURCH AS LOVE GROUP"
alias: "Thought: Church As Love Group"
type: THOUGHT
en_content: "The number of hate groups has doubled the last 10 years. Where's the love groups? Oh yeah: that's what the CHURCH's supposed to be!"
parent: "topic.RELIGION"
tags:
- church
- love
- hate
- society
- religion
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 08-Aug-2012)
CREATE (t:THOUGHT {
    name: "thought.CHURCH AS LOVE GROUP",
    alias: "Thought: Church As Love Group",
    parent: "topic.RELIGION",
    tags: ['church', 'love', 'hate', 'society', 'religion'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.CHURCH AS LOVE GROUP",
    en_title: "Church As Love Group",
    en_content: "The number of hate groups has doubled the last 10 years. Where's the love groups? Oh yeah: that's what the CHURCH's supposed to be!",
    es_title: "La Iglesia como Grupo de Amor",
    es_content: "El número de grupos de odio se ha duplicado en los últimos 10 años. ¿Dónde están los grupos de amor? Ah sí: ¡eso es lo que se supone que debe ser la IGLESIA!",
    fr_title: "L'Église comme Groupe d'Amour",
    fr_content: "Le nombre de groupes haineux a doublé ces 10 dernières années. Où sont les groupes d'amour ? Ah oui : c'est ce que l'ÉGLISE est censée être !",
    hi_title: "प्रेम समूह के रूप में चर्च",
    hi_content: "घृणा समूहों की संख्या पिछले 10 वर्षों में दोगुनी हो गई है। प्रेम समूह कहाँ हैं? ओह हाँ: चर्च को यही होना चाहिए था!",
    zh_title: "Jiàotáng Zuòwéi Ài de Qúntǐ",
    zh_content: "Chóuhèn qúntǐ de shùliàng zài guòqù 10 nián zhōng fānle yī bèi. Ài de qúntǐ nǎ? Ō duì: Nà jiù shì JIÀOTÁNG yīnggāi chéngwéi de!"
});

MATCH (t:THOUGHT {name: "thought.CHURCH AS LOVE GROUP"})
MATCH (c:CONTENT {name: "content.CHURCH AS LOVE GROUP"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.CHURCH AS LOVE GROUP" }]->(c);

MATCH (parent:TOPIC {name: "topic.RELIGION"})
MATCH (child:THOUGHT {name: "thought.CHURCH AS LOVE GROUP"})
MERGE (parent)-[:HAS_THOUGHT { "name": "RELIGION >CHURCH AS LOVE GROUP" }]->(child);
```
