---
name: "thought.THE_IRC"
alias: "Thought: THE IRC"
type: THOUGHT
parent: "topic.FIN-GOV"
en_content: "The United States tax code, otherwise know as the Internal Revenue Code (IRC), was written by The Devil; his paw prints are all over it."
tags:
- government
- finance
- code
- usa
- tax
neo4j: true
ptopic: "[[topic-FIN-GOV]]"
level: 5
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.THE_IRC",
    alias: "Thought: THE IRC",
    parent: "topic.FIN-GOV",
    tags: ["government", "finance", "code", "usa", "tax"],
    level: 5
});

CREATE (c:CONTENT {
    name: "content.THE_IRC",
    en_title: "THE IRC",
    en_content: "The United States tax code, otherwise know as the Internal Revenue Code (IRC), was written by The Devil; his paw prints are all over it.",
	es_title: "EL IRC",
    es_content: "El código tributario de los Estados Unidos, también conocido como Código de Rentas Internas (IRC), fue escrito por El Diablo; sus huellas están por todas partes.",
	fr_title: "LE IRC",
    fr_content: "Le code fiscal des États-Unis, également connu sous le nom d’Internal Revenue Code (IRC), a été rédigé par le Diable ; ses empreintes de pattes sont partout.",
	hi_title: "आईआरसी",
    hi_content: "संयुक्त राज्य कर कोड, जिसे अन्यथा आंतरिक राजस्व कोड (आईआरसी) के रूप में जाना जाता है, द डेविल द्वारा लिखा गया था; उसके पंजे के निशान इस पर हैं।",
	zh_title: "IRC",
    zh_content: "měi guó shuì fǎ ， yě chēng wéi 《 guó nèi shuì shōu fǎ diǎn 》（IRC）， shì yóu mó guǐ zhì dìng de ； shàng miàn dào chù dōu shì tā de zhǎo yìn 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE_IRC" AND c.name = "content.THE_IRC"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.THE_IRC"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.FIN-GOV" AND child.name = "thought.THE_IRC"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.FIN-GOV->THE_IRC"}]->(child);
```
