---
type: QUOTE
name: "quote.THE_SALVATION"
alias: "Quote: Quote: THE SALVATION"
parent: "topic.THE-GOSPEL"
en_content: "THERE IS NO SALVATION APART FROM JESUS. Let me put this another way: JESUS **IS** THE SALVATION GOD THE FATHER IS OFFERING YOU, as opposed to a set of deeds you must accomplish or words you must say to 'receive' Salvation from Jesus.",
 es_title: "Cita: LA SALVACIÓN",
 es_content: "NO HAY SALVACIÓN APARTE DE JESÚS. Permíteme decirlo de otra manera: JESÚS **ES** LA SALVACIÓN QUE DIOS EL PADRE TE OFRECE, a diferencia de un conjunto de hechos que debes realizar o palabras que debes decir para 'recibir' la Salvación de Jesús.",
 fr_title: "Citation : LE SALUT",
 fr_content: "IL N'Y A PAS DE SALUT EN DEHORS DE JÉSUS. Permettez-moi de formuler cela autrement : JÉSUS **EST** LE SALUT DIEU LE PÈRE VOUS OFFRE, par opposition à un ensemble d'actes que vous devez accomplir ou de paroles que vous devez dire pour « recevoir » le salut de Jésus.",
 hi_title: "उद्धरण: मोक्ष",
 hi_content: "यीशु के अलावा कोई मुक्ति नहीं है। मैं इसे दूसरे तरीके से कहना चाहता हूं: यीशु वह मुक्तिदाता ईश्वर है जो पिता आपको प्रदान कर रहा है, यह उन कार्यों के सेट के विपरीत है जिन्हें आपको पूरा करना होगा या जो शब्द आपको यीशु से मुक्ति 'प्राप्त करने' के लिए कहने होंगे।",
 zh_title: "yǐn yòng ： jiù shú",
 zh_content: "chú le yē sū zhī wài ， bié wú zhěng jiù 。 ràng wǒ huàn jù huà shuō ： yē sū ** shì ** tiān fù shén tí gōng gěi nǐ de jiù ēn ， ér bú shì nǐ bì xū wán chéng de yī xì liè xíng wéi huò nǐ bì xū shuō de huà cái néng “ jiē shòu ” lái zì yē sū de jiù ēn 。"
tags: ["salvation", "divine", "gift", "free", "unearned"]
ptopic: "[[topic-THE-GOSPEL]]"
level: 2
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE_SALVATION",
    alias: "Quote: Quote: THE SALVATION",
    parent: "topic.THE-GOSPEL",
    tags: ["salvation", "divine", "gift", "free", "unearned"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE_SALVATION",
    ctype: "QUOTE",
    en_title: "Quote: THE SALVATION",
    en_content: "THERE IS NO SALVATION APART FROM JESUS. Let me put this another way: JESUS **IS** THE SALVATION GOD THE FATHER IS OFFERING YOU, as opposed to a set of deeds you must accomplish or words you must say to 'receive' Salvation from Jesus.",
 es_title: "Cita: LA SALVACIÓN",
 es_content: "NO HAY SALVACIÓN APARTE DE JESÚS. Permíteme decirlo de otra manera: JESÚS **ES** LA SALVACIÓN QUE DIOS EL PADRE TE OFRECE, a diferencia de un conjunto de hechos que debes realizar o palabras que debes decir para 'recibir' la Salvación de Jesús.",
 fr_title: "Citation : LE SALUT",
 fr_content: "IL N'Y A PAS DE SALUT EN DEHORS DE JÉSUS. Permettez-moi de formuler cela autrement : JÉSUS **EST** LE SALUT DIEU LE PÈRE VOUS OFFRE, par opposition à un ensemble d'actes que vous devez accomplir ou de paroles que vous devez dire pour « recevoir » le salut de Jésus.",
 hi_title: "उद्धरण: मोक्ष",
 hi_content: "यीशु के अलावा कोई मुक्ति नहीं है। मैं इसे दूसरे तरीके से कहना चाहता हूं: यीशु वह मुक्तिदाता ईश्वर है जो पिता आपको प्रदान कर रहा है, यह उन कार्यों के सेट के विपरीत है जिन्हें आपको पूरा करना होगा या जो शब्द आपको यीशु से मुक्ति 'प्राप्त करने' के लिए कहने होंगे।",
 zh_title: "yǐn yòng ： jiù shú",
 zh_content: "chú le yē sū zhī wài ， bié wú zhěng jiù 。 ràng wǒ huàn jù huà shuō ： yē sū ** shì ** tiān fù shén tí gōng gěi nǐ de jiù ēn ， ér bú shì nǐ bì xū wán chéng de yī xì liè xíng wéi huò nǐ bì xū shuō de huà cái néng “ jiē shòu ” lái zì yē sū de jiù ēn 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.THE_SALVATION"})
MATCH (c:CONTENT {name: "content.THE_SALVATION"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE_SALVATION"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.THE-GOSPEL"})
MATCH (child:QUOTE {name: "quote.THE_SALVATION"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.THE-GOSPEL->THE_SALVATION"}]->(child);

```
