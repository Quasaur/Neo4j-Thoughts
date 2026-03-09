---
type: QUOTE
name: "quote.MY PROGRAMMING"
alias: "Quote: My Programming"
parent: "topic.PSYCHOLOGY"
source: "'The Traveler's Oasis, Book Two'"
en_content: "In contrast, my programming was virtually complete. When my controller raised his firearm to his son's face, the well-honed logic that had so faithfully enabled me to survive numerous assignments kicked into gear with machine-like precision.",
 es_title: "Cita: MI PROGRAMACIÓN",
 es_content: "Por el contrario, mi programación estaba prácticamente completa. Cuando mi controlador levantó su arma de fuego hacia la cara de su hijo, la lógica perfeccionada que tan fielmente me había permitido sobrevivir a numerosas tareas se puso en marcha con precisión similar a la de una máquina.",
 fr_title: "Citation : MA PROGRAMMATION",
 fr_content: "En revanche, ma programmation était pratiquement terminée. Lorsque mon contrôleur a levé son arme à feu vers le visage de son fils, la logique bien rodée qui m'avait si fidèlement permis de survivre à de nombreuses missions s'est mise en marche avec une précision semblable à celle d'une machine.",
 hi_title: "उद्धरण: मेरी प्रोग्रामिंग",
 hi_content: "इसके विपरीत, मेरी प्रोग्रामिंग वस्तुतः पूर्ण थी। जब मेरे नियंत्रक ने अपने बेटे के चेहरे पर अपनी बन्दूक उठाई, तो अच्छी तरह से परिष्कृत तर्क जिसने मुझे इतनी ईमानदारी से कई कार्यों को जीवित रहने में सक्षम बनाया था, मशीन जैसी सटीकता के साथ गियर में डाल दिया गया।",
 zh_title: "yǐn yòng ： wǒ de biān chéng",
 zh_content: "xiāng bǐ zhī xià ， wǒ de biān chéng shí jì shàng yǐ jīng wán chéng le 。 dāng wǒ de guǎn zhì yuán jiāng qiāng jǔ dào tā ér zi de liǎn shàng shí ， céng jīng ràng wǒ zhōng shí dì zài wú shù cì rèn wù zhōng xìng cún xià lái de jīng xīn mó liàn de luó jí kāi shǐ yǐ jī qì bān de jīng què dù qǐ dòng 。"
tags: ["programming", "brain_washing", "training", "dream", "fiction"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
verified: false
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.MY PROGRAMMING",
    alias: "Quote: My Programming",
    parent: "topic.PSYCHOLOGY",
    tags: ["programming", "brain_washing", "training", "dream", "fiction"],
    source: "'The Traveler's Oasis, Book Two'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-Two-ebook/dp/B00YIT5O9Q)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.MY PROGRAMMING",
    ctype: "QUOTE",
    en_title: "My Programming",
    en_content: "In contrast, my programming was virtually complete. When my controller raised his firearm to his son's face, the well-honed logic that had so faithfully enabled me to survive numerous assignments kicked into gear with machine-like precision.",
 es_title: "Cita: MI PROGRAMACIÓN",
 es_content: "Por el contrario, mi programación estaba prácticamente completa. Cuando mi controlador levantó su arma de fuego hacia la cara de su hijo, la lógica perfeccionada que tan fielmente me había permitido sobrevivir a numerosas tareas se puso en marcha con precisión similar a la de una máquina.",
 fr_title: "Citation : MA PROGRAMMATION",
 fr_content: "En revanche, ma programmation était pratiquement terminée. Lorsque mon contrôleur a levé son arme à feu vers le visage de son fils, la logique bien rodée qui m'avait si fidèlement permis de survivre à de nombreuses missions s'est mise en marche avec une précision semblable à celle d'une machine.",
 hi_title: "उद्धरण: मेरी प्रोग्रामिंग",
 hi_content: "इसके विपरीत, मेरी प्रोग्रामिंग वस्तुतः पूर्ण थी। जब मेरे नियंत्रक ने अपने बेटे के चेहरे पर अपनी बन्दूक उठाई, तो अच्छी तरह से परिष्कृत तर्क जिसने मुझे इतनी ईमानदारी से कई कार्यों को जीवित रहने में सक्षम बनाया था, मशीन जैसी सटीकता के साथ गियर में डाल दिया गया।",
 zh_title: "yǐn yòng ： wǒ de biān chéng",
 zh_content: "xiāng bǐ zhī xià ， wǒ de biān chéng shí jì shàng yǐ jīng wán chéng le 。 dāng wǒ de guǎn zhì yuán jiāng qiāng jǔ dào tā ér zi de liǎn shàng shí ， céng jīng ràng wǒ zhōng shí dì zài wú shù cì rèn wù zhōng xìng cún xià lái de jīng xīn mó liàn de luó jí kāi shǐ yǐ jī qì bān de jīng què dù qǐ dòng 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.MY PROGRAMMING"})
MATCH (c:CONTENT {name: "content.MY PROGRAMMING"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.MY PROGRAMMING"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
MATCH (child:QUOTE {name: "quote.MY PROGRAMMING"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.PSYCHOLOGY->MY PROGRAMMING"}]->(child);

```
