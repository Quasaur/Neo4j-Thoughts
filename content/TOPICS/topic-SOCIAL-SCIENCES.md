---
name: "topic.SOCIAL SCIENCES"
alias: "Topic: Human Interaction in Social Systems"
type: TOPIC
parent: topic.HUMANITY
en_content: "The group of academic disciplines that systematically study human behavior, social relationships, institutions, and societies using empirical, analytical, and interpretive methods to explain how people interact and how social systems function."
tags:
- society
- behavior
- institutions
- culture
- analysis
neo4j: true
ptopic: "[[topic-HUMANITY]]"
level: 4
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.SOCIAL SCIENCES",
    alias: "Topic: Human Interaction in Social Systems",
    parent: "topic.HUMANITY",
    tags: ["society", "behavior", "interactions", "culture", "analysis"],
    level: 4
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.SOCIAL SCIENCES",
    en_title: "Social Sciences",
    en_content: "The group of academic disciplines that systematically study human behavior, social relationships, institutions, and societies using empirical, analytical, and interpretive methods to explain how people interact and how social systems function.",
    es_title: "Ciencias Sociales",
    es_content: "Conjunto de disciplinas académicas que estudian sistemáticamente el comportamiento humano, las relaciones sociales, las instituciones y las sociedades, utilizando métodos empíricos, analíticos e interpretativos para explicar cómo interactúan las personas y cómo funcionan los sistemas sociales.",
    fr_title: "Sciences sociales",
    fr_content: "L'ensemble des disciplines universitaires qui étudient systématiquement le comportement humain, les relations sociales, les institutions et les sociétés en utilisant des méthodes empiriques, analytiques et interprétatives afin d'expliquer comment les individus interagissent et comment fonctionnent les systèmes sociaux.",
    hi_title: "सामाजिक विज्ञान",
    hi_content: "शैक्षणिक विषयों का वह समूह जो लोगों के व्यवहार, सामाजिक संबंधों, संस्थानों और समाजों का व्यवस्थित रूप से अध्ययन करता है, जिसमें अनुभवजन्य, विश्लेषणात्मक और व्याख्यात्मक तरीकों का उपयोग करके यह समझाया जाता है कि लोग कैसे बातचीत करते हैं और सामाजिक प्रणालियाँ कैसे काम करती हैं।",
    zh_title: "Shèhuì kēxué",
    zh_content: "zhè shì yī zǔ xuéshù xuékē, tāmen yùnyòng shízhèng, fēnxī hé jiěshì xìng fāngfǎ, xìtǒng de yánjiū rénlèi xíngwéi, shèhuì guānxì, shèhuì zhìdù hé shèhuì, yǐ jiěshì rénmen rúhé hùdòng yǐjí shèhuì xìtǒng rúhé yùnzuò."
});

// LINK DESCRIPTION
MATCH (t:TOPIC {name: "topic.SOCIAL SCIENCES"})
MATCH (d:DESCRIPTION {name: "desc.SOCIAL SCIENCES"})
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.SOCIAL SCIENCES"}]->(d);

// LINK PARENT
MATCH (p:TOPIC)
WHERE p.name = "topic.HUMANITY"
MATCH (c:TOPIC)
WHERE c.name = "topic.SOCIAL SCIENCES"
MERGE (p)-[:HAS_CHILD {name: "edge.HUMANITY->SOCIAL SCIENCES"}]->(c);

```
