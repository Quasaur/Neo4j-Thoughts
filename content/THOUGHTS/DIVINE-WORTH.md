---
name: "thought.DIVINE_WORTH"
alias: "Thought: DIVINE WORTH"
type: THOUGHT
parent: "topic.HOLINESS"

tags:
- deity
- holy
- worth
- value
- diine
neo4j: true
ptopic: "[[topic-HOLINESS]]"
level: 2
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DIVINE_WORTH",
    alias: "Thought: DIVINE WORTH",
    parent: "topic.HOLINESS",
    tags: ["deity", "holy", "worth", "value", "diine"],
    level: 2
});

CREATE (c:CONTENT {
    name: "content.DIVINE_WORTH",
    en_title: "Divine Worth",
    en_content: "God is holy. Which means that God is worth more than you or I...more than all the life in the cosmos put together.",
	es_title: "VALOR DIVINO",
    es_content: "Dios es santo. Lo que significa que Dios vale más que tú o que yo... más que toda la vida en el cosmos junta.",
	fr_title: "VALEUR DIVINE",
    fr_content: "Dieu est saint. Ce qui signifie que Dieu vaut plus que vous ou moi... plus que toute la vie du cosmos réunie.",
	hi_title: "दिव्य मूल्य",
    hi_content: "भगवान पवित्र है. जिसका अर्थ यह है कि ईश्वर आपसे या मुझसे अधिक मूल्यवान है...ब्रह्मांड के समस्त जीवन से अधिक मूल्यवान है।",
    zh_title: "shén shèng de jià zhí",
    zh_content: "shàng dì shì shén shèng de 。 zhè yì wèi zhe shàng dì bǐ nǐ huò wǒ gèng yǒu jià zhí …… bǐ yǔ zhòu zhōng suǒ yǒu shēng mìng de zǒng hé gèng yǒu jià zhí 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DIVINE_WORTH" AND c.name = "content.DIVINE_WORTH"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.DIVINE_WORTH"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HOLINESS" AND child.name = "thought.DIVINE_WORTH"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.HOLINESS->DIVINE_WORTH"}]->(child);
```
