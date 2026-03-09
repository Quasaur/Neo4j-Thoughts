---
type: QUOTE
name: "quote.ONE WILL"
alias: "Quote: One Will"
parent: "topic.DIVINE-SOVEREIGNTY"
source: "'Once Saved, Always Saved: The Assurance of Our Father's LOVE'"
en_content: "Precious Reader, I have experienced The Light of Eternity saturating my being (The Traveler's Oasis: Book One, Chapter 18) and i can tell you that THERE IS ONLY ONE WILL THAT HAS EVER AND WILL EVER EXIST!",
 es_title: "Cita: UNA VOLUNTAD",
 es_content: "Precioso Lector, he experimentado La Luz de la Eternidad saturando mi ser (El Oasis del Viajero: Libro Uno, Capítulo 18) y puedo decirte que ¡SOLO HAY UNA VOLUNTAD QUE SIEMPRE HA EXISTIDO Y SIEMPRE EXISTIRÁ!",
 fr_title: "Citation : UNE VOLONTÉ",
 fr_content: "Précieux Lecteur, j'ai fait l'expérience de la Lumière de l'Éternité saturant mon être (L'Oasis du Voyageur : Livre Un, Chapitre 18) et je peux vous dire qu'IL N'Y A QU'UNE SEULE VOLONTÉ QUI A JAMAIS EXISTÉ ET EXISTERA JAMAIS !",
 hi_title: "उद्धरण: एक होगा",
 hi_content: "प्रिय पाठक, मैंने अपने अस्तित्व को संतृप्त करने वाले अनंत काल के प्रकाश का अनुभव किया है (द ट्रैवेलर्स ओएसिस: बुक वन, चैप्टर 18) और मैं आपको बता सकता हूं कि केवल एक ही इच्छा है जो कभी अस्तित्व में थी और हमेशा रहेगी!",
 zh_title: "yǐn yòng ： yí gè yì zhì",
 zh_content: "qīn ài de dú zhě ， wǒ jīng lì guò yǒng héng zhī guāng jìn tòu wǒ de cún zài （ lǚ xíng zhě de lǜ zhōu ： dì yī běn shū ， dì  18  zhāng ）， wǒ kě yǐ gào sù nǐ ， zhǐ yǒu yí gè yì zhì céng jīng bìng qiě jiāng yǒng yuǎn cún zài ！"
tags: ["light", "eternity", "onewill", "deity", "sovereignty"]
ptopic: "[[topic-DIVINE-SOVEREIGNTY]]"
level: 2
neo4j: true
verified: false
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.ONE WILL",
    alias: "Quote: One Will",
    parent: "topic.DIVINE-SOVEREIGNTY",
    tags: ["light", "eternity", "onewill", "deity", "sovereignty"],
    source: "'Once Saved, Always Saved: The Assurance of Our Father's LOVE'",
    booklink: "(https://www.amazon.com/Once-Saved-Always-Assurance-Fathers-ebook/dp/B0132UEB68)",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.ONE WILL",
    ctype: "QUOTE",
    en_title: "One Will",
    en_content: "Precious Reader, I have experienced The Light of Eternity saturating my being (The Traveler's Oasis: Book One, Chapter 18) and i can tell you that THERE IS ONLY ONE WILL THAT HAS EVER AND WILL EVER EXIST!",
 es_title: "Cita: UNA VOLUNTAD",
 es_content: "Precioso Lector, he experimentado La Luz de la Eternidad saturando mi ser (El Oasis del Viajero: Libro Uno, Capítulo 18) y puedo decirte que ¡SOLO HAY UNA VOLUNTAD QUE SIEMPRE HA EXISTIDO Y SIEMPRE EXISTIRÁ!",
 fr_title: "Citation : UNE VOLONTÉ",
 fr_content: "Précieux Lecteur, j'ai fait l'expérience de la Lumière de l'Éternité saturant mon être (L'Oasis du Voyageur : Livre Un, Chapitre 18) et je peux vous dire qu'IL N'Y A QU'UNE SEULE VOLONTÉ QUI A JAMAIS EXISTÉ ET EXISTERA JAMAIS !",
 hi_title: "उद्धरण: एक होगा",
 hi_content: "प्रिय पाठक, मैंने अपने अस्तित्व को संतृप्त करने वाले अनंत काल के प्रकाश का अनुभव किया है (द ट्रैवेलर्स ओएसिस: बुक वन, चैप्टर 18) और मैं आपको बता सकता हूं कि केवल एक ही इच्छा है जो कभी अस्तित्व में थी और हमेशा रहेगी!",
 zh_title: "yǐn yòng ： yí gè yì zhì",
 zh_content: "qīn ài de dú zhě ， wǒ jīng lì guò yǒng héng zhī guāng jìn tòu wǒ de cún zài （ lǚ xíng zhě de lǜ zhōu ： dì yī běn shū ， dì  18  zhāng ）， wǒ kě yǐ gào sù nǐ ， zhǐ yǒu yí gè yì zhì céng jīng bìng qiě jiāng yǒng yuǎn cún zài ！"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.ONE WILL"})
MATCH (c:CONTENT {name: "content.ONE WILL"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.ONE WILL"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.DIVINE-SOVEREIGNTY"})
MATCH (child:QUOTE {name: "quote.ONE WILL"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.DIVINE-SOVEREIGNTY->ONE WILL"}]->(child);

```
