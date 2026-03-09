---
type: THOUGHT
name: "thought.CITIZENSHIP"
alias: "Thought: Citizenship"
parent: "topic.ECONOMICS"
tags: ["citizenship", "kingdom", "reign_of_god", "freedom", "jesus_christ"]
ptopic: "[[topic-ECONOMICS]]"
level: 4
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.CITIZENSHIP",
    alias: "Thought: Citizenship",
    parent: "topic.ECONOMICS",
    tags: ["citizenship", "kingdom", "reign_of_god", "freedom", "jesus_christ"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.CITIZENSHIP",
    ctype: "THOUGHT",
    en_title: "Citizenship",
    en_content: "REMEMBER: there is no 'cost of living' in the Kingdom of the Heavens. Change your citizenship IMMEDIATELY!!!",
 es_title: "CIUDADANÍA",
 es_content: "RECUERDA: no hay 'costo de vida' en el Reino de los Cielos. ¡¡¡Cambia tu ciudadanía INMEDIATAMENTE!!!",
 fr_title: "CITOYENNETÉ",
 fr_content: "RAPPELEZ-VOUS : il n'y a pas de « coût de la vie » dans le Royaume des Cieux. Changez de citoyenneté IMMÉDIATEMENT !!!",
 hi_title: "सिटिज़नशिप",
 hi_content: "याद रखें: स्वर्ग के राज्य में 'जीवनयापन की कोई कीमत' नहीं है। तुरंत अपनी नागरिकता बदलें!!!",
 zh_title: "guó jí",
 zh_content: "qǐng jì zhù ： tiān guó lǐ méi yǒu “ shēng huó fèi yòng ”。 lì jí gēng gǎi nín de guó jí ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CITIZENSHIP" AND c.name = "content.CITIZENSHIP"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.CITIZENSHIP"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.ECONOMICS" AND child.name = "thought.CITIZENSHIP"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.ECONOMICS->CITIZENSHIP"}]->(child);
```