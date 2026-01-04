---
name: topic.PHILOSOPHY
alias: "Topic: The Science of Ideology"
type: TOPIC
parent: topic.HUMANITY
tags:
- fundamentals
- humanities
- existence
- reason
- knowledge
neo4j: true
level: 4
---

```Cypher
// CREATE TOPIC
CREATE (t:TOPIC {
    name: "topic.PHILOSOPHY",
    alias: "Topic: The Science of Ideology",
    parent: "topic.HUMANITY",
    tags: ["fundamentals", "humanities", "existence", "reason", "knowledge"],
    level: 4
});

// CREATE DESCRIPTION
CREATE (d:DESCRIPTION {
    name: "desc.PHILOSOPHY",
    en_title: "PHILOSOPHY",
    en_content: "A foundational discipline within the Humanities. It explores fundamental questions about existence, knowledge, values, reason, mind, and language. As such, it provides a framework for understanding other humanities fields like literature, history, art, and religion. While philosophy can be considered a standalone discipline, it also intersects and informs many other areas of study within the humanities.",
    es_title: "FILOSOFÍA",
    es_content: "Disciplina fundamental dentro de las humanidades. Explora cuestiones fundamentales sobre la existencia, el conocimiento, los valores, la razón, la mente y el lenguaje. Como tal, proporciona un marco para comprender otros campos de las humanidades, como la literatura, la historia, el arte y la religión. Si bien la filosofía puede considerarse una disciplina independiente, también se relaciona con muchas otras áreas de estudio dentro de las humanidades y las orienta.",
    fr_title: "PHILOSOPHIE",
    fr_content: "Une discipline fondamentale au sein des sciences humaines. Elle explore des questions fondamentales sur l'existence, la connaissance, les valeurs, la raison, l'esprit et le langage. En tant que telle, elle fournit un cadre pour comprendre d'autres domaines des sciences humaines comme la littérature, l'histoire, l'art et la religion. Si la philosophie peut être considérée comme une discipline autonome, elle recoupe et informe également de nombreux autres domaines d'étude des sciences humaines.",
    hi_title: "दर्शन",
    hi_content: "मानविकी के भीतर एक आधारभूत अनुशासन। यह अस्तित्व, ज्ञान, मूल्यों, तर्क, मन और भाषा के बारे में मौलिक प्रश्नों की खोज करता है। इस प्रकार, यह साहित्य, इतिहास, कला और धर्म जैसे अन्य मानविकी क्षेत्रों को समझने के लिए एक रूपरेखा प्रदान करता है। जबकि दर्शन को एक स्वतंत्र अनुशासन माना जा सकता है, यह मानविकी के भीतर अध्ययन के कई अन्य क्षेत्रों को भी जोड़ता है और सूचित करता है।",
    zh_title: "Zhéxué",
    zh_content: "Rénwén xuékē zhōng de yī mén jīchǔ xuékē. Tā tànsuǒ yǒuguān cúnzài, zhīshì, jiàzhíguān, lǐxìng, sīxiǎng hé yǔyán de jīběn wèntí. Yīncǐ, tā wèi lǐjiě wénxué, lìshǐ, yìshù hé zōngjiào děng qítā rénwén xuékē lǐngyù tígōngle yīgè kuàngjià. suīrán zhéxué kěyǐ bèi shì wéi yī mén dúlì de xuékē, dàn tā yě yǔ rénwén xuékē zhōng de xǔduō qítā yánjiū lǐngyù xiāng jiāochā bìng wéi qí tígōng xìnxī."
});

// LINK DESCRIPTION
MATCH (t:TOPIC), (d:DESCRIPTION)
WHERE t.name = "topic.PHILOSOPHY" AND d.name = "desc.PHILOSOPHY"
MERGE (t)-[:HAS_DESCRIPTION {name: "edge.PHILOSOPHY"}]->(d);

// LINK PARENT
MATCH (p:TOPIC), (c:TOPIC)
WHERE p.name = "topic.HUMANITY" AND c.name = "topic.PHILOSOPHY"
MERGE (p)-[:HAS_CHILD {name: "edge.HUMANITY->PHILOSOPHY"}]->(c);

```
