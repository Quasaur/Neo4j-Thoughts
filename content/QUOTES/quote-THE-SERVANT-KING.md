---
type: QUOTE
name: "quote.THE SERVANT KING"
alias: "Quote: The Servant King"
parent: "topic.ATTITUDE"
source: "'The Narrow Way'"
en_content: "OH MY GOD!!! Here the Lord Jesus Christ distinguishes Himself from all the great men (and great thinkers) of history who have either preceded Him or came after Him! If the Claims Jesus made about Himself are true, He had at His disposal enough absolute power to bend all human society to His Will... Yet, in His First Advent, He refuses to exert a single iota of His Divine Sovereignty to shape human will or human hearts! Rather, by the Spirit of Humility, He calls, teaches and persuades us by means of deeds the lowliest of slaves would be hesitant to perform!",
 es_title: "Cita: EL REY SIERVO",
 es_content: "¡¡¡AY DIOS MÍO!!! ¡Aquí el Señor Jesucristo se distingue de todos los grandes hombres (y grandes pensadores) de la historia que lo precedieron o vinieron después de Él! Si las afirmaciones que Jesús hizo sobre sí mismo son ciertas, Él tenía a Su disposición suficiente poder absoluto para someter a toda la sociedad humana a Su Voluntad... ¡Sin embargo, en Su Primera Venida, Él se niega a ejercer un solo ápice de Su Divina Soberanía para moldear la voluntad humana o los corazones humanos! Más bien, por el Espíritu de Humildad, Él nos llama, nos enseña y persuade por medio de obras que el más humilde de los esclavos dudaría en realizar.",
 fr_title: "Citation : LE ROI SERVITEUR",
 fr_content: "OH MON DIEU!!! Ici, le Seigneur Jésus-Christ se distingue de tous les grands hommes (et grands penseurs) de l’histoire qui l’ont précédé ou suivi ! Si les affirmations de Jésus sur lui-même sont vraies, il avait à sa disposition suffisamment de pouvoir absolu pour plier toute la société humaine à sa volonté... Pourtant, lors de son premier avènement, il refuse d'exercer un seul iota de sa souveraineté divine pour façonner la volonté humaine ou les cœurs humains ! Au contraire, par l’Esprit d’humilité, Il nous appelle, nous enseigne et nous persuade au moyen d’actes que le plus humble des esclaves hésiterait à accomplir !",
 hi_title: "उद्धरण: सेवक राजा",
 hi_content: "अरे बाप रे!!! यहाँ प्रभु यीशु मसीह स्वयं को इतिहास के उन सभी महान व्यक्तियों (और महान विचारकों) से अलग करते हैं जो या तो उनसे पहले आए थे या उनके बाद आए थे! यदि यीशु ने अपने बारे में जो दावा किया है वह सच है, तो उसके पास पूरे मानव समाज को अपनी इच्छा के अनुसार झुकाने के लिए पर्याप्त पूर्ण शक्ति थी... फिर भी, अपने पहले आगमन में, उसने मानव इच्छा या मानव हृदय को आकार देने के लिए अपनी दिव्य संप्रभुता का एक कण भी प्रयोग करने से इनकार कर दिया! बल्कि, विनम्रता की भावना से, वह हमें उन कार्यों के माध्यम से बुलाता है, सिखाता है और मनाता है जिन्हें करने में सबसे तुच्छ दास भी झिझकेंगे!",
 zh_title: "yǐn yòng ： pú rén zhī wáng",
 zh_content: "wǒ de tiān a ！！！ zài zhè lǐ ， zhǔ yē sū jī dū jiāng zì jǐ yǔ lì shǐ shàng suǒ yǒu zài tā zhī qián huò zhī hòu de wěi rén （ hé wěi dà de sī xiǎng jiā ） qū fēn kāi lái ！ rú guǒ yē sū duì zì jǐ de xuān chēng shì zhēn shí de ， nà me tā jiù yōng yǒu zú gòu de jué duì quán lì ， kě yǐ shǐ zhěng gè rén lèi shè huì qū fú yú tā de yì zhì …… rán ér ， zài tā de dì yī cì jiàng lín zhōng ， tā jù jué fā huī tā de shén shèng zhǔ quán de yī dīng diǎn lái sù zào rén lèi de yì zhì huò rén xīn ！ xiāng fǎn ， tā yǐ qiān bēi de jīng shén ， tōng guò lián zuì bēi wēi de nú lì dōu yóu yù bù jué de xíng wéi lái hū zhào 、 jiào dǎo hé shuō fú wǒ men ！"
tags: ["greatest", "servant", "burdenbearer", "foundation", "jesus_christ"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: false
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE SERVANT KING",
    alias: "Quote: The Servant King",
    parent: "topic.ATTITUDE",
    tags: ["greatest", "servant", "burdenbearer", "foundation", "jesus_christ"],
    source: "'The Narrow Way'",
    booklink: "(https://www.amazon.com/Narrow-Way-Calvin-Mitchell-ebook/dp/B0CRYC8WY7)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE SERVANT KING",
    ctype: "QUOTE",
    en_title: "The Servant King",
    en_content: "OH MY GOD!!! Here the Lord Jesus Christ distinguishes Himself from all the great men (and great thinkers) of history who have either preceded Him or came after Him! If the Claims Jesus made about Himself are true, He had at His disposal enough absolute power to bend all human society to His Will... Yet, in His First Advent, He refuses to exert a single iota of His Divine Sovereignty to shape human will or human hearts! Rather, by the Spirit of Humility, He calls, teaches and persuades us by means of deeds the lowliest of slaves would be hesitant to perform!",
 es_title: "Cita: EL REY SIERVO",
 es_content: "¡¡¡AY DIOS MÍO!!! ¡Aquí el Señor Jesucristo se distingue de todos los grandes hombres (y grandes pensadores) de la historia que lo precedieron o vinieron después de Él! Si las afirmaciones que Jesús hizo sobre sí mismo son ciertas, Él tenía a Su disposición suficiente poder absoluto para someter a toda la sociedad humana a Su Voluntad... ¡Sin embargo, en Su Primera Venida, Él se niega a ejercer un solo ápice de Su Divina Soberanía para moldear la voluntad humana o los corazones humanos! Más bien, por el Espíritu de Humildad, Él nos llama, nos enseña y persuade por medio de obras que el más humilde de los esclavos dudaría en realizar.",
 fr_title: "Citation : LE ROI SERVITEUR",
 fr_content: "OH MON DIEU!!! Ici, le Seigneur Jésus-Christ se distingue de tous les grands hommes (et grands penseurs) de l’histoire qui l’ont précédé ou suivi ! Si les affirmations de Jésus sur lui-même sont vraies, il avait à sa disposition suffisamment de pouvoir absolu pour plier toute la société humaine à sa volonté... Pourtant, lors de son premier avènement, il refuse d'exercer un seul iota de sa souveraineté divine pour façonner la volonté humaine ou les cœurs humains ! Au contraire, par l’Esprit d’humilité, Il nous appelle, nous enseigne et nous persuade au moyen d’actes que le plus humble des esclaves hésiterait à accomplir !",
 hi_title: "उद्धरण: सेवक राजा",
 hi_content: "अरे बाप रे!!! यहाँ प्रभु यीशु मसीह स्वयं को इतिहास के उन सभी महान व्यक्तियों (और महान विचारकों) से अलग करते हैं जो या तो उनसे पहले आए थे या उनके बाद आए थे! यदि यीशु ने अपने बारे में जो दावा किया है वह सच है, तो उसके पास पूरे मानव समाज को अपनी इच्छा के अनुसार झुकाने के लिए पर्याप्त पूर्ण शक्ति थी... फिर भी, अपने पहले आगमन में, उसने मानव इच्छा या मानव हृदय को आकार देने के लिए अपनी दिव्य संप्रभुता का एक कण भी प्रयोग करने से इनकार कर दिया! बल्कि, विनम्रता की भावना से, वह हमें उन कार्यों के माध्यम से बुलाता है, सिखाता है और मनाता है जिन्हें करने में सबसे तुच्छ दास भी झिझकेंगे!",
 zh_title: "yǐn yòng ： pú rén zhī wáng",
 zh_content: "wǒ de tiān a ！！！ zài zhè lǐ ， zhǔ yē sū jī dū jiāng zì jǐ yǔ lì shǐ shàng suǒ yǒu zài tā zhī qián huò zhī hòu de wěi rén （ hé wěi dà de sī xiǎng jiā ） qū fēn kāi lái ！ rú guǒ yē sū duì zì jǐ de xuān chēng shì zhēn shí de ， nà me tā jiù yōng yǒu zú gòu de jué duì quán lì ， kě yǐ shǐ zhěng gè rén lèi shè huì qū fú yú tā de yì zhì …… rán ér ， zài tā de dì yī cì jiàng lín zhōng ， tā jù jué fā huī tā de shén shèng zhǔ quán de yī dīng diǎn lái sù zào rén lèi de yì zhì huò rén xīn ！ xiāng fǎn ， tā yǐ qiān bēi de jīng shén ， tōng guò lián zuì bēi wēi de nú lì dōu yóu yù bù jué de xíng wéi lái hū zhào 、 jiào dǎo hé shuō fú wǒ men ！"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.THE SERVANT KING"})
MATCH (c:CONTENT {name: "content.THE SERVANT KING"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE SERVANT KING"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MATCH (child:QUOTE {name: "quote.THE SERVANT KING"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.ATTITUDE->THE SERVANT KING"}]->(child);

```
