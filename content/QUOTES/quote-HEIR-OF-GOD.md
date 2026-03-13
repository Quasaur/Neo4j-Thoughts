---
type: QUOTE
name: "quote.HEIR OF GOD!"
alias: "Quote: Heir of God!"
parent: "topic.THE GOSPEL"
source: "The Narrow Way"
en_content: "Thankfully, GOD has looked upon your situation with compassion and is not only offering you an escape from His Wrath, but a priceless opportunity TO BECOME HIS HEIR!!! All the 'heavy lifting' has been done for you, yet you must set your heart to follow Your Creator (GOD The Word, incarnated as Jesus the Messiah) back to the Father of all spirits and NOT LOOK BACK on the familiar life you were born into."
tags: ["heir", "adoption", "son", "daughter", "jesus_christ"]
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
neo4j: true
verified: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.HEIR OF GOD!",
    alias: "Quote: Heir of God!",
    parent: "topic.THE GOSPEL",
    tags: ["heir", "adoption", "son", "daughter", "jesus_christ"],
    source: "The Narrow Way",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.HEIR OF GOD!",
    ctype: "QUOTE",
    en_title: "Quote: Heir of God!",
    en_content: "Thankfully, GOD has looked upon your situation with compassion and is not only offering you an escape from His Wrath, but a priceless opportunity TO BECOME HIS HEIR!!! All the 'heavy lifting' has been done for you, yet you must set your heart to follow Your Creator (GOD The Word, incarnated as Jesus the Messiah) back to the Father of all spirits and NOT LOOK BACK on the familiar life you were born into.",
 es_title: "Cita: ¡Heredero de Dios!",
 es_content: "¡¡¡Afortunadamente, DIOS ha mirado tu situación con compasión y no solo te ofrece un escape de Su ira, sino también una oportunidad invaluable DE CONVERTIRTE EN SU HEREDERO!!! Todo el 'trabajo pesado' ya se ha hecho por ti, pero debes establecer tu corazón para seguir a Tu Creador (DIOS, la Palabra, encarnado como Jesús el Mesías) de regreso al Padre de todos los espíritus y NO MIRAR ATRÁS a la vida familiar en la que naciste.",
 fr_title: "Citation : Héritier de Dieu !",
 fr_content: "Heureusement, DIEU a regardé votre situation avec compassion et vous offre non seulement une évasion de sa colère, mais une opportunité inestimable de DEVENIR SON HÉRITIER !!! Tout le « gros du travail » a été fait pour vous, mais vous devez décider à cœur de suivre votre Créateur (DIEU la Parole, incarné en Jésus le Messie) jusqu'au Père de tous les esprits et de NE PAS REGARDER EN RETOUR sur la vie familière dans laquelle vous êtes né.",
 hi_title: "उद्धरण: भगवान का वारिस!",
 hi_content: "शुक्र है, भगवान ने आपकी स्थिति पर दया की है और वह आपको न केवल अपने क्रोध से बचने की पेशकश कर रहा है, बल्कि उसका उत्तराधिकारी बनने का एक अमूल्य अवसर भी दे रहा है!!! आपके लिए सारा 'भारी भार' उठाया जा चुका है, फिर भी आपको सभी आत्माओं के पिता के पास अपने निर्माता (ईश्वर शब्द, यीशु मसीहा के रूप में अवतरित) का अनुसरण करने के लिए अपना दिल लगाना चाहिए और उस परिचित जीवन को पीछे मुड़कर नहीं देखना चाहिए जिसमें आप पैदा हुए थे।",
 zh_title: "yǐn yòng ：shén de jì chéng rén ！",
 zh_content: "zhí de qìng xìng de shì ， shàng dì lián mǐn dì kàn dài nǐ de chǔ jìng ， bù jǐn wèi nǐ tí gōng le táo bì tā fèn nù de jī huì ， ér qiě wèi nǐ tí gōng le chéng wéi tā de jì chéng rén de wú jià jī huì ！ suǒ yǒu de “ zhòng dàn ” dōu yǐ jīng wèi nǐ wán chéng le ， dàn nǐ bì xū xià dìng jué xīn gēn suí nǐ de chuàng zào zhě （ shén dào ， huà shēn wèi mí sài yà yē sū ） huí dào wàn líng zhī fù nà lǐ ， ér bú shì huí tóu kàn nǐ chū shēng shí shú xī de shēng huó 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.HEIR OF GOD!"})
MATCH (c:CONTENT {name: "content.HEIR OF GOD!"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.HEIR OF GOD!"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.THE GOSPEL"})
MATCH (child:QUOTE {name: "quote.HEIR OF GOD!"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE GOSPEL->HEIR OF GOD!"}]->(child);

```
