---
type: THOUGHT
name: "thought.TIME"
alias: "Thought: Time"
parent: "topic.JUSTICE"
tags: ["spirituality", "damnation", "soul", "lake_of_fire", "judgment"]
ptopic: "[[topic-JUSTICE]]"
level: 5
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.TIME",
    alias: "Thought: Time",
    parent: "topic.JUSTICE",
    tags: ["spirituality", "damnation", "soul", "lake_of_fire", "judgment"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.TIME",
    ctype: "THOUGHT",
    en_title: "Time",
 es_title: "TIEMPO",
 fr_title: "TEMPS",
 hi_title: "समय",
 zh_title: "shí jiān",
    en_content: "",
 es_content: "Pasarás más tiempo en la Eternidad que en esta vida (o en vidas “anteriores”)… ¡¿y NO te preocupas por el destino de tu alma?!",
 fr_content: "Vous passerez plus de temps dans l’Éternité que vous ne l’avez jamais fait dans cette vie (ou dans vos vies « précédentes »)… et vous n’avez AUCUNE préoccupation concernant le sort de votre âme ?!",
 hi_content: "आप अनंत काल में इस जीवन (या \"पिछले\" जीवन) की तुलना में अधिक समय व्यतीत करेंगे...और आपको अपनी आत्मा के भाग्य के बारे में कोई चिंता नहीं है?!"पिछले\" जीवन) की तुलना में अधिक समय व्यतीत करेंगे...और आपको अपनी आत्मा के भाग्य के बारे में कोई चिंता नहीं है?!"पिछले\" जीवन) की तुलना में अधिक समय व्यतीत करेंगे...और आपको अपनी आत्मा के भाग्य के बारे में कोई चिंता नहीं है?!"पिछले\" जीवन) की तुलना में अधिक समय व्यतीत करेंगे...और आपको अपनी आत्मा के भाग्य के बारे में कोई चिंता नहीं है?!",
 zh_content: "nǐ jiāng zài yǒng héng zhōng dù guò bǐ jīn shēng （ huò “ qián shì ”） gèng duō de shí jiān …… ér qiě nǐ bù guān xīn nǐ líng hún de mìng yùn ？！"पिछले\" जीवन) की तुलना में अधिक समय व्यतीत करेंगे...और आपको अपनी आत्मा के भाग्य के बारे में कोई चिंता नहीं है?!"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.TIME" AND c.name = "content.TIME"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.TIME"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.JUSTICE" AND child.name = "thought.TIME"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.JUSTICE->TIME"}]->(child);
```