---
type: QUOTE
name: "quote.TRUTH_AND_FAITH"
alias: "Quote: Quote: TRUTH AND FAITH"
parent: "topic.THE-GOSPEL"
en_content: "GOD lovingly provides both the Truth that saves us from the Lake of Fire as well as the Saving Faith necessary to believe on (from the heart) and live by that Saving Truth.",
 es_title: "Cita: VERDAD Y FE",
 es_content: "DIOS amorosamente proporciona tanto la Verdad que nos salva del Lago de Fuego como también la Fe Salvadora necesaria para creer (desde el corazón) y vivir según esa Verdad Salvadora.",
 fr_title: "Citation : VÉRITÉ ET FOI",
 fr_content: "DIEU fournit avec amour à la fois la Vérité qui nous sauve de l’étang de feu ainsi que la foi salvatrice nécessaire pour croire (du cœur) et vivre selon cette Vérité salvatrice.",
 hi_title: "उद्धरण: सत्य और विश्वास",
 hi_content: "भगवान प्रेमपूर्वक सत्य प्रदान करते हैं जो हमें आग की झील से बचाता है और साथ ही बचाने वाला विश्वास भी प्रदान करता है जिस पर (हृदय से) विश्वास करना और उस बचाने वाले सत्य के अनुसार जीना आवश्यक है।",
 zh_title: "yǐn yòng ： zhēn lǐ yǔ xìn yǎng",
 zh_content: "shàng dì cí ài dì tí gōng le jiāng wǒ men cóng huǒ hú zhōng zhěng jiù chū lái de zhēn lǐ ， yǐ jí （ cóng nèi xīn ） xiāng xìn bìng àn zhào gāi zhěng jiù zhēn lǐ shēng huó suǒ bì xū de zhěng jiù xìn yǎng 。"
tags: ["faith", "truth", "salvation", "lake_of_fire", "love"]
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.TRUTH_AND_FAITH",
    alias: "Quote: Quote: TRUTH AND FAITH",
    parent: "topic.THE-GOSPEL",
    tags: ["faith", "truth", "salvation", "lake_of_fire", "love"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.TRUTH_AND_FAITH",
    ctype: "QUOTE",
    en_title: "Quote: TRUTH AND FAITH",
    en_content: "GOD lovingly provides both the Truth that saves us from the Lake of Fire as well as the Saving Faith necessary to believe on (from the heart) and live by that Saving Truth.",
 es_title: "Cita: VERDAD Y FE",
 es_content: "DIOS amorosamente proporciona tanto la Verdad que nos salva del Lago de Fuego como también la Fe Salvadora necesaria para creer (desde el corazón) y vivir según esa Verdad Salvadora.",
 fr_title: "Citation : VÉRITÉ ET FOI",
 fr_content: "DIEU fournit avec amour à la fois la Vérité qui nous sauve de l’étang de feu ainsi que la foi salvatrice nécessaire pour croire (du cœur) et vivre selon cette Vérité salvatrice.",
 hi_title: "उद्धरण: सत्य और विश्वास",
 hi_content: "भगवान प्रेमपूर्वक सत्य प्रदान करते हैं जो हमें आग की झील से बचाता है और साथ ही बचाने वाला विश्वास भी प्रदान करता है जिस पर (हृदय से) विश्वास करना और उस बचाने वाले सत्य के अनुसार जीना आवश्यक है।",
 zh_title: "yǐn yòng ： zhēn lǐ yǔ xìn yǎng",
 zh_content: "shàng dì cí ài dì tí gōng le jiāng wǒ men cóng huǒ hú zhōng zhěng jiù chū lái de zhēn lǐ ， yǐ jí （ cóng nèi xīn ） xiāng xìn bìng àn zhào gāi zhěng jiù zhēn lǐ shēng huó suǒ bì xū de zhěng jiù xìn yǎng 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.TRUTH_AND_FAITH"})
MATCH (c:CONTENT {name: "content.TRUTH_AND_FAITH"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.TRUTH_AND_FAITH"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.THE-GOSPEL"})
MATCH (child:QUOTE {name: "quote.TRUTH_AND_FAITH"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE-GOSPEL->TRUTH_AND_FAITH"}]->(child);

```
