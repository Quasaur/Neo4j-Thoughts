---
type: QUOTE
name: "quote.WEALTH AND FAITH"
alias: "Quote: Wealth and Faith"
parent: "topic.WEALTH"
source: "IMMUNITY to the Lake of Fire: A No-Nonsense Guide"
en_content: "Wealth and Faith are mutually exclusive: having one, it does not necessarily follow that you will have the other in this life. When it comes to His Own, GOD determines the economic station of His Children. In perspective, however, there are no poor people in Heaven: you may have to wait till Eternity to receive your wealth (Matthew 6:19,20)."
tags: ["wealth", "faith", "exclusivity", "sovereignty", "heaven"]
ptopic: "[[topic-WEALTH]]"
level: 3
neo4j: true
verified: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.WEALTH AND FAITH",
    alias: "Quote: Wealth and Faith",
    parent: "topic.WEALTH",
    tags: ["wealth", "faith", "exclusivity", "sovereignty", "heaven"],
    source: "'IMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.WEALTH AND FAITH",
    ctype: "QUOTE",
    en_title: "Quote: Wealth and Faith",
    en_content: "Wealth and Faith are mutually exclusive: having one, it does not necessarily follow that you will have the other in this life. When it comes to His Own, GOD determines the economic station of His Children. In perspective, however, there are no poor people in Heaven: you may have to wait till Eternity to receive your wealth (Matthew 6:19,20).",
 es_title: "Cita: Riqueza y fe",
 es_content: "La riqueza y la fe son mutuamente excluyentes: teniendo una, no necesariamente se sigue que tendrás la otra en esta vida. Cuando se trata de los Suyos, DIOS determina la posición económica de Sus Hijos. En perspectiva, sin embargo, no hay pobres en el Cielo: es posible que tengas que esperar hasta la Eternidad para recibir tus riquezas (Mateo 6:19,20).",
 fr_title: "Citation : Richesse et foi",
 fr_content: "La richesse et la foi s’excluent mutuellement : avoir l’une ne signifie pas nécessairement que vous aurez l’autre dans cette vie. En ce qui concerne les Siens, DIEU détermine la situation économique de Ses Enfants. En perspective, cependant, il n’y a pas de pauvres au Ciel : vous devrez peut-être attendre l’éternité pour recevoir votre richesse (Matthieu 6 : 19,20).",
 hi_title: "उद्धरण: धन और विश्वास",
 hi_content: "धन और आस्था परस्पर अनन्य हैं: एक होने पर, यह आवश्यक नहीं है कि आपके पास इस जीवन में दूसरा भी होगा। जब अपनी खुद की बात आती है, तो भगवान अपने बच्चों की आर्थिक स्थिति निर्धारित करते हैं। हालाँकि, परिप्रेक्ष्य में, स्वर्ग में कोई गरीब लोग नहीं हैं: आपको अपना धन प्राप्त करने के लिए अनंत काल तक इंतजार करना पड़ सकता है (मैथ्यू 6:19,20)।",
 zh_title: "yǐn yòng ： cái fù yǔ xìn yǎng",
 zh_content: "cái fù hé xìn yǎng shì xiāng hù pái chì de ： yōng yǒu yí gè ， bìng bù yí dìng yì wèi zhe nǐ jīn shēng jiù huì yōng yǒu lìng yí gè 。 dāng tán dào tā zì jǐ de rén shí ， shàng dì jué dìng tā hái zi men de jīng jì dì wèi 。 rán ér ， cóng cháng yuǎn lái kàn ， tiān táng lǐ méi yǒu qióng rén ： nǐ kě néng bì xū děng dào yǒng héng cái néng huò dé nǐ de cái fù （ mǎ tài fú yīn 6:19,20）。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.WEALTH AND FAITH"})
MATCH (c:CONTENT {name: "content.WEALTH AND FAITH"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.WEALTH AND FAITH"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.WEALTH"})
MATCH (child:QUOTE {name: "quote.WEALTH AND FAITH"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.WEALTH->WEALTH AND FAITH"}]->(child);

```
