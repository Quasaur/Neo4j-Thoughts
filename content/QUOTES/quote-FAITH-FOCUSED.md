---
type: QUOTE
name: "quote.FAITH FOCUSED"
alias: "Quote: Faith Focused"
parent: "topic.FAITH"
source: "The Narrow Way"
en_content: "Here's a hint: if you're stuck in doubt, it's because YOU'RE FOCUSED ON THE WRONG PERSON. If you're looking inward at yourself the only conclusion you can come to is 'impossible.' But if you turn your attention to Jesus and His Unconditional Love for you, your confidence in His Word (in this case Romans Chapter Six) will grow and meet the challenge of your past with the glory of your future in Christ."
tags: ["faith", "focus", "word_of_faith", "jesus_christ", "self"]
ptopic: "[[topic-FAITH]]"
level: 4
neo4j: true
verified: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.FAITH FOCUSED",
    alias: "Quote: Faith Focused",
    parent: "topic.FAITH",
    tags: ["faith", "focus", "word_of_faith", "jesus_christ", "self"],
    source: "The Narrow Way",
    booklink: "https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.FAITH FOCUSED",
    ctype: "QUOTE",
    en_title: "Quote: Faith Focused",
    en_content: "Here's a hint: if you're stuck in doubt, it's because YOU'RE FOCUSED ON THE WRONG PERSON. If you're looking inward at yourself the only conclusion you can come to is 'impossible.' But if you turn your attention to Jesus and His Unconditional Love for you, your confidence in His Word (in this case Romans Chapter Six) will grow and meet the challenge of your past with the glory of your future in Christ.",
 es_title: "Cita: Centrado en la fe",
 es_content: "Aquí tienes una pista: si tienes dudas, es porque ESTÁS ENFOCADO EN LA PERSONA EQUIVOCADA. Si miras hacia adentro, la única conclusión a la que puedes llegar es \"imposible\". Pero si diriges tu atención a Jesús y Su amor incondicional por ti, tu confianza en Su Palabra (en este caso Romanos Capítulo Seis) crecerá y enfrentará el desafío de tu pasado con la gloria de tu futuro en Cristo.",
 fr_title: "Citation : Centrado en la fe",
 fr_content: "Voici un indice : si vous êtes coincé dans le doute, c'est que VOUS ÊTES CONCENTRÉ SUR LA MAUVAISE PERSONNE. Si vous regardez à l’intérieur de vous-même, la seule conclusion à laquelle vous pouvez arriver est « impossible ». Mais si vous tournez votre attention vers Jésus et son amour inconditionnel pour vous, votre confiance en sa Parole (dans ce cas Romains chapitre six) grandira et relèvera le défi de votre passé avec la gloire de votre avenir en Christ.",
 hi_title: "उद्धरण: आस्था केंद्रित",
 hi_content: "यहां एक संकेत है: यदि आप संदेह में फंस गए हैं, तो इसका कारण यह है कि आपका ध्यान गलत व्यक्ति पर केंद्रित है। यदि आप अपने अंदर झाँक रहे हैं तो आप केवल यही निष्कर्ष निकाल सकते हैं कि 'असंभव' है। लेकिन यदि आप अपना ध्यान यीशु और आपके प्रति उनके बिना शर्त प्रेम की ओर लगाते हैं, तो उनके वचन (इस मामले में रोमियों अध्याय छह) में आपका विश्वास बढ़ेगा और मसीह में अपने भविष्य की महिमा के साथ अपने अतीत की चुनौती का सामना करेंगे।",
 zh_title: "yǐn yòng : zhuān zhù yú xìn yǎng",
 zh_content: "zhè lǐ yǒu yí gè tí shì ： rú guǒ nǐ yóu yù bù jué ， nà shì yīn wèi nǐ kàn cuò le rén 。 rú guǒ nǐ xiàng nèi shěn shì zì jǐ ， nǐ néng dé chū de wéi yī jié lùn jiù shì “ bù kě néng ”。 dàn shì ， rú guǒ nín jiāng zhù yì lì zhuǎn xiàng yē sū hé tā duì nín wú tiáo jiàn de ài ， nín duì tā de huà yǔ （ zài běn lì zhōng wèi luó mǎ shū dì liù zhāng ） de xìn xīn jiù huì zēng qiáng ， bìng yǐ nín zài jī dū lǐ de wèi lái de róng yào yíng jiē guò qù de tiǎo zhàn 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.FAITH FOCUSED"})
MATCH (c:CONTENT {name: "content.FAITH FOCUSED"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.FAITH FOCUSED"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.FAITH"})
MATCH (child:QUOTE {name: "quote.FAITH FOCUSED"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.FAITH->FAITH FOCUSED"}]->(child);
```