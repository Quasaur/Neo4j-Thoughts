---
type: QUOTE
name: "quote.ADOPTION2"
alias: "Quote: Adoption2"
parent: "topic.GRACE"
source: "'The Narrow Way'"
en_content: "No doubt you can appreciate how important Conversion is to your Salvation. GOD does not exist to the world (or the religious) because, as unredeemed sinners, they do not have the Holy Spirit of GOD dwelling in them, as true Christians do.",
 es_title: "Cita: ADOPCIÓN2",
 es_content: "Sin duda podrás apreciar lo importante que es la Conversión para tu Salvación. DIOS no existe para el mundo (ni para los religiosos) porque, como pecadores no redimidos, no tienen el Espíritu Santo de DIOS morando en ellos, como lo hacen los verdaderos cristianos.",
 fr_title: "Citation : ADOPTION2",
 fr_content: "Vous pouvez sans aucun doute comprendre à quel point la conversion est importante pour votre salut. DIEU n’existe pas pour le monde (ni pour les religieux) parce que, en tant que pécheurs non rachetés, ils n’ont pas le Saint-Esprit de DIEU habitant en eux, comme le font les vrais chrétiens.",
 hi_title: "उद्धरण: दत्तक ग्रहण2",
 hi_content: "इसमें कोई संदेह नहीं कि आप समझ सकते हैं कि रूपांतरण आपके उद्धार के लिए कितना महत्वपूर्ण है। दुनिया (या धार्मिक) के लिए ईश्वर का कोई अस्तित्व नहीं है, क्योंकि, मुक्ति न पाए पापियों के रूप में, उनमें ईश्वर की पवित्र आत्मा का वास नहीं है, जैसा कि सच्चे ईसाइयों में होता है।",
 zh_title: "yǐn yòng ： cǎi yòng 2",
 zh_content: "háo wú yí wèn ， nǐ kě yǐ tǐ huì dào guī yī duì nǐ de jiù shú yǒu duō me zhòng yào 。 duì yú shì jiè （ huò zōng jiào ） lái shuō ， shàng dì bìng bù cún zài ， yīn wèi zuò wéi wèi dé jiù shú de zuì rén ， tā men méi yǒu xiàng zhēn zhèng de jī dū tú nà yàng yǒu shàng dì de shèng líng zhù zài tā men lǐ miàn 。"
tags: ["born_again", "rebirth", "holy_spirit", "child_of_god", "holy_spirit"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
verified: false
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.ADOPTION2",
    alias: "Quote: Adoption2",
    parent: "topic.GRACE",
    tags: ["born_again", "rebirth", "holy_spirit", "child_of_god", "holy_spirit"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.ADOPTION2",
    ctype: "QUOTE",
    en_title: "Adoption2",
    en_content: "No doubt you can appreciate how important Conversion is to your Salvation. GOD does not exist to the world (or the religious) because, as unredeemed sinners, they do not have the Holy Spirit of GOD dwelling in them, as true Christians do.",
 es_title: "Cita: ADOPCIÓN2",
 es_content: "Sin duda podrás apreciar lo importante que es la Conversión para tu Salvación. DIOS no existe para el mundo (ni para los religiosos) porque, como pecadores no redimidos, no tienen el Espíritu Santo de DIOS morando en ellos, como lo hacen los verdaderos cristianos.",
 fr_title: "Citation : ADOPTION2",
 fr_content: "Vous pouvez sans aucun doute comprendre à quel point la conversion est importante pour votre salut. DIEU n’existe pas pour le monde (ni pour les religieux) parce que, en tant que pécheurs non rachetés, ils n’ont pas le Saint-Esprit de DIEU habitant en eux, comme le font les vrais chrétiens.",
 hi_title: "उद्धरण: दत्तक ग्रहण2",
 hi_content: "इसमें कोई संदेह नहीं कि आप समझ सकते हैं कि रूपांतरण आपके उद्धार के लिए कितना महत्वपूर्ण है। दुनिया (या धार्मिक) के लिए ईश्वर का कोई अस्तित्व नहीं है, क्योंकि, मुक्ति न पाए पापियों के रूप में, उनमें ईश्वर की पवित्र आत्मा का वास नहीं है, जैसा कि सच्चे ईसाइयों में होता है।",
 zh_title: "yǐn yòng ： cǎi yòng 2",
 zh_content: "háo wú yí wèn ， nǐ kě yǐ tǐ huì dào guī yī duì nǐ de jiù shú yǒu duō me zhòng yào 。 duì yú shì jiè （ huò zōng jiào ） lái shuō ， shàng dì bìng bù cún zài ， yīn wèi zuò wéi wèi dé jiù shú de zuì rén ， tā men méi yǒu xiàng zhēn zhèng de jī dū tú nà yàng yǒu shàng dì de shèng líng zhù zài tā men lǐ miàn 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.ADOPTION2"})
MATCH (c:CONTENT {name: "content.ADOPTION2"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.ADOPTION2"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:QUOTE {name: "quote.ADOPTION2"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->ADOPTION2"}]->(child);

```
