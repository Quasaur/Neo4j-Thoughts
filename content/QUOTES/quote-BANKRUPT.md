---
type: QUOTE
name: "quote.BANKRUPT"
alias: "Quote: Bankrupt"
parent: "topic.GRACE"
en_content: "We can never be allowed to experience the Power of GOD’s Holy Spirit until we fully understand that we are absolutely bankrupt (both morally and spiritually), with nothing to offer GOD except our sin, our shame and our failure.",
 es_title: "Cita: BANCARROTA",
 es_content: "Nunca se nos permitirá experimentar el poder del Espíritu Santo de DIOS hasta que entendamos completamente que estamos absolutamente en bancarrota (tanto moral como espiritualmente), sin nada que ofrecer a DIOS excepto nuestro pecado, nuestra vergüenza y nuestro fracaso.",
 fr_title: "Citation : FAILLITE",
 fr_content: "Nous ne pourrons jamais expérimenter la puissance du Saint-Esprit de DIEU tant que nous n’aurons pas pleinement compris que nous sommes absolument en faillite (à la fois moralement et spirituellement), sans rien à offrir à DIEU à part notre péché, notre honte et notre échec.",
 hi_title: "उद्धरण: दिवालिया",
 hi_content: "हमें कभी भी भगवान की पवित्र आत्मा की शक्ति का अनुभव करने की अनुमति नहीं दी जा सकती जब तक कि हम पूरी तरह से यह नहीं समझ लेते कि हम पूरी तरह से दिवालिया हैं (नैतिक और आध्यात्मिक रूप से), हमारे पाप, हमारी शर्म और हमारी विफलता के अलावा भगवान को देने के लिए हमारे पास कुछ भी नहीं है।",
 zh_title: "yǐn yòng ： pò chǎn",
 zh_content: "chú fēi wǒ men wán quán míng bái ， wǒ men jué duì pò chǎn le （ wú lùn shì zài dào dé shàng hái shì zài jīng shén shàng ）， chú le wǒ men de zuì 、 wǒ men de xiū chǐ hé wǒ men de shī bài zhī wài ， wǒ men méi yǒu rèn hé dōng xī kě yǐ xiàn gěi shàng dì ， fǒu zé wǒ men yǒng yuǎn bú huì bèi yǔn xǔ tǐ yàn shàng dì shèng líng de lì liàng 。"
tags: ["offering", "sin", "shame", "failure", "holy_spirit"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.BANKRUPT",
    alias: "Quote: Bankrupt",
    parent: "topic.GRACE",
    tags: ["offering", "sin", "shame", "failure", "holy_spirit"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.BANKRUPT",
    ctype: "QUOTE",
    en_title: "Bankrupt",
    en_content: "We can never be allowed to experience the Power of GOD’s Holy Spirit until we fully understand that we are absolutely bankrupt (both morally and spiritually), with nothing to offer GOD except our sin, our shame and our failure.",
 es_title: "Cita: BANCARROTA",
 es_content: "Nunca se nos permitirá experimentar el poder del Espíritu Santo de DIOS hasta que entendamos completamente que estamos absolutamente en bancarrota (tanto moral como espiritualmente), sin nada que ofrecer a DIOS excepto nuestro pecado, nuestra vergüenza y nuestro fracaso.",
 fr_title: "Citation : FAILLITE",
 fr_content: "Nous ne pourrons jamais expérimenter la puissance du Saint-Esprit de DIEU tant que nous n’aurons pas pleinement compris que nous sommes absolument en faillite (à la fois moralement et spirituellement), sans rien à offrir à DIEU à part notre péché, notre honte et notre échec.",
 hi_title: "उद्धरण: दिवालिया",
 hi_content: "हमें कभी भी भगवान की पवित्र आत्मा की शक्ति का अनुभव करने की अनुमति नहीं दी जा सकती जब तक कि हम पूरी तरह से यह नहीं समझ लेते कि हम पूरी तरह से दिवालिया हैं (नैतिक और आध्यात्मिक रूप से), हमारे पाप, हमारी शर्म और हमारी विफलता के अलावा भगवान को देने के लिए हमारे पास कुछ भी नहीं है।",
 zh_title: "yǐn yòng ： pò chǎn",
 zh_content: "chú fēi wǒ men wán quán míng bái ， wǒ men jué duì pò chǎn le （ wú lùn shì zài dào dé shàng hái shì zài jīng shén shàng ）， chú le wǒ men de zuì 、 wǒ men de xiū chǐ hé wǒ men de shī bài zhī wài ， wǒ men méi yǒu rèn hé dōng xī kě yǐ xiàn gěi shàng dì ， fǒu zé wǒ men yǒng yuǎn bú huì bèi yǔn xǔ tǐ yàn shàng dì shèng líng de lì liàng 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.BANKRUPT"})
MATCH (c:CONTENT {name: "content.BANKRUPT"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.BANKRUPT"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:QUOTE {name: "quote.BANKRUPT"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->BANKRUPT"}]->(child);

```
