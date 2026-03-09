---
type: QUOTE
name: "quote.NO OBLIGATION"
alias: "Quote: No Obligation"
parent: "topic.MERCY"
source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'"
en_content: "GOD is under no obligation to be merciful to evil. Sinners are evil, and every human is a sinner. By the definitions of the terms “mercy” and “forgiveness,” these virtues can never be owed to the sinner. GOD would’ve been perfectly righteous and just to annihilate Adam and Eve before their offspring could permeate the surface of the Earth with the wretchedness and horror you see today. Even more so: GOD would’ve been just to shut Lucifer down before anyone else was affected."
 es_title: "Cotización: SIN COMPROMISO"
 es_content: "DIOS no tiene ninguna obligación de ser misericordioso con el mal. Los pecadores son malos y todo ser humano es un pecador. Según las definiciones de los términos “misericordia” y “perdón”, estas virtudes nunca se pueden deber al pecador. DIOS habría sido perfectamente recto y justo al aniquilar a Adán y Eva antes de que su descendencia pudiera impregnar la superficie de la Tierra con la miseria y el horror que vemos hoy. Aún más: DIOS habría sido justo si hubiera cerrado a Lucifer antes de que alguien más se viera afectado."
 fr_title: "Citation : AUCUNE OBLIGATION"
 fr_content: "DIEU n’a aucune obligation d’être miséricordieux envers le mal. Les pécheurs sont mauvais et tout être humain est pécheur. Par les définitions des termes « miséricorde » et « pardon », ces vertus ne peuvent jamais être dues au pécheur. DIEU aurait été parfaitement juste et aurait juste anéanti Adam et Ève avant que leur progéniture ne puisse imprégner la surface de la Terre de la misère et de l’horreur que vous voyez aujourd’hui. Plus encore : DIEU aurait simplement arrêté Lucifer avant que quelqu’un d’autre ne soit affecté."
 hi_title: "उद्धरण: कोई बाध्यता नहीं"
 hi_content: "ईश्वर बुराई के प्रति दयालु होने के लिए बाध्य नहीं है। पापी दुष्ट हैं, और प्रत्येक मनुष्य पापी है। \"दया\" और \"क्षमा\" शब्दों की परिभाषा के अनुसार, ये गुण कभी भी पापी पर बकाया नहीं हो सकते। ईश्वर पूरी तरह से धर्मी होता और आदम और हव्वा को नष्ट कर देता, इससे पहले कि उनकी संतानें पृथ्वी की सतह पर उस दुष्टता और भयावहता को व्याप्त कर पातीं जो आप आज देख रहे हैं। इससे भी अधिक: इससे पहले कि कोई और प्रभावित होता, भगवान ने लूसिफ़ेर को बंद कर दिया होता।"
 zh_title: "bào jià ： wú yì wù"
 zh_content: "shàng dì méi yǒu yì wù duì xié è rén cí 。 zuì rén dōu shì xié è de ， měi gè rén dōu shì zuì rén 。 gēn jù “ rén cí ” hé “ kuān shù ” zhè liǎng gè cí de dìng yì ， zhè xiē měi dé yǒng yuǎn bù néng guī gōng yú zuì rén 。 shàng dì huì shì wán quán zhèng yì de ， huì zài yà dāng hé xià wá de hòu dài ràng nǐ men jīn tiān kàn dào de bēi cǎn hé kǒng bù biàn bù dì qiú biǎo miàn zhī qián xiāo miè tā men 。 gèng zhòng yào de shì ： shàng dì huì zài qí tā rén shòu dào yǐng xiǎng zhī qián guān bì lù xī fǎ 。"
tags: ["god", "sovereignty", "unowed", "leniency", "evil"]
ptopic: "[[topic-MERCY]]"
level: 5
neo4j: true
verified: false
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.NO OBLIGATION",
    alias: "Quote: No Obligation",
    parent: "topic.MERCY",
    tags: ["god", "sovereignty", "unowed", "leniency", "evil"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "()",
    level: 5
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.NO OBLIGATION",
    ctype: "QUOTE",
    en_title: "No Obligation",
    en_content: "GOD is under no obligation to be merciful to evil. Sinners are evil, and every human is a sinner. By the definitions of the terms “mercy” and “forgiveness,” these virtues can never be owed to the sinner. GOD would’ve been perfectly righteous and just to annihilate Adam and Eve before their offspring could permeate the surface of the Earth with the wretchedness and horror you see today. Even more so: GOD would’ve been just to shut Lucifer down before anyone else was affected.",
 es_title: "Cotización: SIN COMPROMISO",
 es_content: "DIOS no tiene ninguna obligación de ser misericordioso con el mal. Los pecadores son malos y todo ser humano es un pecador. Según las definiciones de los términos “misericordia” y “perdón”, estas virtudes nunca se pueden deber al pecador. DIOS habría sido perfectamente recto y justo al aniquilar a Adán y Eva antes de que su descendencia pudiera impregnar la superficie de la Tierra con la miseria y el horror que vemos hoy. Aún más: DIOS habría sido justo si hubiera cerrado a Lucifer antes de que alguien más se viera afectado.",
 fr_title: "Citation : AUCUNE OBLIGATION",
 fr_content: "DIEU n’a aucune obligation d’être miséricordieux envers le mal. Les pécheurs sont mauvais et tout être humain est pécheur. Par les définitions des termes « miséricorde » et « pardon », ces vertus ne peuvent jamais être dues au pécheur. DIEU aurait été parfaitement juste et aurait juste anéanti Adam et Ève avant que leur progéniture ne puisse imprégner la surface de la Terre de la misère et de l’horreur que vous voyez aujourd’hui. Plus encore : DIEU aurait simplement arrêté Lucifer avant que quelqu’un d’autre ne soit affecté.",
 hi_title: "उद्धरण: कोई बाध्यता नहीं",
 hi_content: "ईश्वर बुराई के प्रति दयालु होने के लिए बाध्य नहीं है। पापी दुष्ट हैं, और प्रत्येक मनुष्य पापी है। \"दया\" और \"क्षमा\" शब्दों की परिभाषा के अनुसार, ये गुण कभी भी पापी पर बकाया नहीं हो सकते। ईश्वर पूरी तरह से धर्मी होता और आदम और हव्वा को नष्ट कर देता, इससे पहले कि उनकी संतानें पृथ्वी की सतह पर उस दुष्टता और भयावहता को व्याप्त कर पातीं जो आप आज देख रहे हैं। इससे भी अधिक: इससे पहले कि कोई और प्रभावित होता, भगवान ने लूसिफ़ेर को बंद कर दिया होता।",
 zh_title: "bào jià ： wú yì wù",
 zh_content: "shàng dì méi yǒu yì wù duì xié è rén cí 。 zuì rén dōu shì xié è de ， měi gè rén dōu shì zuì rén 。 gēn jù “ rén cí ” hé “ kuān shù ” zhè liǎng gè cí de dìng yì ， zhè xiē měi dé yǒng yuǎn bù néng guī gōng yú zuì rén 。 shàng dì huì shì wán quán zhèng yì de ， huì zài yà dāng hé xià wá de hòu dài ràng nǐ men jīn tiān kàn dào de bēi cǎn hé kǒng bù biàn bù dì qiú biǎo miàn zhī qián xiāo miè tā men 。 gèng zhòng yào de shì ： shàng dì huì zài qí tā rén shòu dào yǐng xiǎng zhī qián guān bì lù xī fǎ 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.NO OBLIGATION"})
MATCH (c:CONTENT {name: "content.NO OBLIGATION"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.NO OBLIGATION"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.MERCY"})
MATCH (child:QUOTE {name: "quote.NO OBLIGATION"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.MERCY->NO OBLIGATION"}]->(child);
```