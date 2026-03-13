---
type: QUOTE
name: "quote.FEELINGS"
alias: "Quote: Feelings"
parent: "topic.FAITH"
source: "IMMUNITY to the Lake of Fire: A No-Nonsense Guide"
en_content: "Your personal neuroses (guilt, shame, depression, bipolar disorder, etc.) notwithstanding, when you pray GOD STOPS WHAT HE’S DOING AND LISTENS! Your perception of His Presence (or lack thereof) is irrelevant; what matters is the truth and your faith in the truth…not your feelings."
tags: ["feelings", "emotions", "faith", "word_of_god", "believe"]
ptopic: "[[topic-FAITH]]"
level: 4
neo4j: true
verified: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.FEELINGS",
    alias: "Quote: Feelings",
    parent: "topic.FAITH",
    tags: ["feelings", "emotions", "faith", "word_of_god", "believe"],
    source: "IMMUNITY to the Lake of Fire: A No-Nonsense Guide",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.FEELINGS",
    ctype: "QUOTE",
    en_title: "Quote: Feelings",
    en_content: "Your personal neuroses (guilt, shame, depression, bipolar disorder, etc.) notwithstanding, when you pray GOD STOPS WHAT HE’S DOING AND LISTENS! Your perception of His Presence (or lack thereof) is irrelevant; what matters is the truth and your faith in the truth…not your feelings.",
 es_title: "Cita: Sentimientos",
 es_content: "A pesar de tus neurosis personales (culpa, vergüenza, depresión, trastorno bipolar, etc.), cuando oras, ¡DIOS DEJA LO QUE ESTÁ HACIENDO Y ESCUCHA! Tu percepción de Su Presencia (o falta de ella) es irrelevante; lo que importa es la verdad y tu fe en la verdad... no tus sentimientos.",
 fr_title: "Citation : Sentiments",
 fr_content: "Malgré vos névroses personnelles (culpabilité, honte, dépression, trouble bipolaire, etc.), lorsque vous priez, DIEU ARRÊTE CE IL FAIT ET ÉCOUTE ! Votre perception de Sa Présence (ou de son absence) n’a pas d’importance ; ce qui compte, c'est la vérité et votre foi en la vérité… pas vos sentiments.",
 hi_title: "उद्धरण: भावनाएँ",
 hi_content: "आपकी व्यक्तिगत न्यूरोसिस (अपराध, शर्म, अवसाद, द्विध्रुवी विकार, आदि) के बावजूद, जब आप प्रार्थना करते हैं कि भगवान जो कर रहा है उसे रोक देता है और सुनता है! उसकी उपस्थिति (या उसकी कमी) के बारे में आपकी धारणा अप्रासंगिक है; जो मायने रखता है वह है सत्य और सत्य में आपका विश्वास...आपकी भावनाएँ नहीं।",
 zh_title: "yǐn yòng ：gǎn shòu",
 zh_content: "jǐn guǎn nǐ yǒu gè rén de shén jīng zhèng （ nèi jiù 、 xiū chǐ 、 yì yù 、 shuāng xiàng qíng gǎn zhàng ài děng ）， dàn dāng nǐ qí dǎo shàng dì tíng zhǐ tā zhèng zài zuò de shì qíng bìng qīng tīng shí ！ nǐ duì tā de cún zài （ huò quē fá ） de gǎn zhī shì wú guān ​​ jǐn yào de ； zhòng yào de shì zhēn xiàng hé nǐ duì zhēn xiàng de xìn niàn …… ér bú shì nǐ de gǎn shòu 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.FEELINGS"})
MATCH (c:CONTENT {name: "content.FEELINGS"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.FEELINGS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.FAITH"})
MATCH (child:QUOTE {name: "quote.FEELINGS"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.FAITH->FEELINGS"}]->(child);

```
