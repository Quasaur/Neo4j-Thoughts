---
type: QUOTE
name: "quote.HEADING_HOME"
alias: "Quote: Quote: HEADING HOME"
parent: "topic.TRUTH"
en_content: "Most people focus on the 'deny himself' clause, yet that is NOT the central idea of this statement. To be a disciple of Jesus you must FOLLOW Jesus...but WHERE IS JESUS GOING? In connection to what i said in [Part Fourteen](https://www.clmjournal.com/post/the-narrow-way-part-fourteen-discipleship) regarding Reality, Jesus is RETURNING TO THE FATHER where sin, death and affliction do not exist...and HE IS INVITING YOU TO RETURN THERE WITH HIM!!! This is the HEART of what being 'saved' means, with the added benefit of NEVER BEING CAPABLE OF SINNING AGAIN!!!!"
 es_title: "Cita: RUMBO A CASA"
 es_content: "La mayoría de la gente se centra en la cláusula de \"negarse a sí mismo\", pero esa NO es la idea central de esta declaración. Para ser discípulo de Jesús debes SEGUIR a Jesús...pero ¿A DÓNDE VA JESÚS? En conexión con lo que dije en [Parte Catorce](https://www.clmjournal.com/post/the-narrow-way-part-fourteen-discipleship) con respecto a la Realidad, Jesús está REGRESANDO AL PADRE donde el pecado, la muerte y la aflicción no existen... ¡¡¡Y TE ESTÁ INVITANDO A REGRESAR ALLÍ CON ÉL!!! ¡¡¡Este es el CORAZÓN de lo que significa ser 'salvo', con el beneficio adicional de NUNCA SER CAPAZ DE PECAR OTRA VEZ!!!!"
 fr_title: "Citation : Rentrer à la maison"
 fr_content: "La plupart des gens se concentrent sur la clause « renier lui-même », mais ce n'est PAS l'idée centrale de cette déclaration. Pour être disciple de Jésus, vous devez SUIVRE Jésus... mais OÙ VA JÉSUS ? En lien avec ce que j'ai dit dans la [Partie Quatorze](https://www.clmjournal.com/post/the-narrow-way-part-fourteen-discipleship) concernant la Réalité, Jésus RETOURNE AU PÈRE là où le péché, la mort et l'affliction n'existent pas... et IL VOUS INVITE À Y RETOURNER AVEC LUI !!! C'est le CŒUR de ce que signifie être « sauvé », avec l'avantage supplémentaire de NE JAMAIS ÊTRE CAPABLE DE PÉCHER ENCORE !!!!"
 hi_title: "उद्धरण: घर जा रहा हूँ"
 hi_content: "अधिकांश लोग 'खुद को नकारें' खंड पर ध्यान केंद्रित करते हैं, फिर भी यह इस कथन का केंद्रीय विचार नहीं है। यीशु का शिष्य बनने के लिए आपको यीशु का अनुसरण करना होगा...लेकिन यीशु कहाँ जा रहे हैं? वास्तविकता के संबंध में मैंने [भाग चौदह] (https://www.clmjournal.com/post/the-nrow-way-part-fourteen-discipleship) में जो कहा, उसके संबंध में, यीशु पिता के पास लौट रहे हैं जहां पाप, मृत्यु और दुःख मौजूद नहीं हैं... और वह आपको अपने साथ वहां लौटने के लिए आमंत्रित कर रहे हैं!!! 'बचाए जाने' का यही मूल अर्थ है, साथ ही दोबारा पाप करने में कभी सक्षम न होने का अतिरिक्त लाभ भी!!!!"
 zh_title: "yǐn yòng ： huí jiā"
 zh_content: "dà duō shù rén guān zhù “ fǒu dìng zì jǐ ” tiáo kuǎn ， dàn zhè bìng bú shì zhè jù huà de zhōng xīn sī xiǎng 。 yào chéng wéi yē sū de mén tú ， nǐ bì xū gēn suí yē sū …… dàn shì yē sū yào qù nǎ lǐ ？ guān yú wǒ zài [ dì shí sì bù fèn ](https://www.clmjournal.com/post/the-narrow-way-part-fourteen-discipleship) zhōng suǒ shuō de guān yú xiàn shí de nèi róng ， yē sū zhèng zài huí dào tiān fù nà lǐ ， nà lǐ bù cún zài zuì 、 sǐ wáng hé kǔ nàn …… tā yāo qǐng nǐ hé tā yì qǐ huí dào nà lǐ ！ zhè jiù shì “ dé jiù ” de hé xīn yì yì ， hái yǒu yí gè é wài de hǎo chù ， nà jiù shì yǒng yuǎn bù zài fàn zuì ！！！！"
tags: ["home", "safety", "joy", "rest", "godhead"]
ptopic: "[[topic-TRUTH]]"
level: 2
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.HEADING_HOME",
    alias: "Quote: Quote: HEADING HOME",
    parent: "topic.TRUTH",
    tags: ["home", "safety", "joy", "rest", "godhead"],
    source: "'The Narrow Way'",
    booklink: "()",
    level: 2
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.HEADING_HOME",
    ctype: "QUOTE",
    en_title: "Quote: HEADING HOME",
    en_content: "Most people focus on the 'deny himself' clause, yet that is NOT the central idea of this statement. To be a disciple of Jesus you must FOLLOW Jesus...but WHERE IS JESUS GOING? In connection to what i said in [Part Fourteen](https://www.clmjournal.com/post/the-narrow-way-part-fourteen-discipleship) regarding Reality, Jesus is RETURNING TO THE FATHER where sin, death and affliction do not exist...and HE IS INVITING YOU TO RETURN THERE WITH HIM!!! This is the HEART of what being 'saved' means, with the added benefit of NEVER BEING CAPABLE OF SINNING AGAIN!!!!",
 es_title: "Cita: RUMBO A CASA",
 es_content: "La mayoría de la gente se centra en la cláusula de \"negarse a sí mismo\", pero esa NO es la idea central de esta declaración. Para ser discípulo de Jesús debes SEGUIR a Jesús...pero ¿A DÓNDE VA JESÚS? En conexión con lo que dije en [Parte Catorce](https://www.clmjournal.com/post/the-narrow-way-part-fourteen-discipleship) con respecto a la Realidad, Jesús está REGRESANDO AL PADRE donde el pecado, la muerte y la aflicción no existen... ¡¡¡Y TE ESTÁ INVITANDO A REGRESAR ALLÍ CON ÉL!!! ¡¡¡Este es el CORAZÓN de lo que significa ser 'salvo', con el beneficio adicional de NUNCA SER CAPAZ DE PECAR OTRA VEZ!!!!",
 fr_title: "Citation : Rentrer à la maison",
 fr_content: "La plupart des gens se concentrent sur la clause « renier lui-même », mais ce n'est PAS l'idée centrale de cette déclaration. Pour être disciple de Jésus, vous devez SUIVRE Jésus... mais OÙ VA JÉSUS ? En lien avec ce que j'ai dit dans la [Partie Quatorze](https://www.clmjournal.com/post/the-narrow-way-part-fourteen-discipleship) concernant la Réalité, Jésus RETOURNE AU PÈRE là où le péché, la mort et l'affliction n'existent pas... et IL VOUS INVITE À Y RETOURNER AVEC LUI !!! C'est le CŒUR de ce que signifie être « sauvé », avec l'avantage supplémentaire de NE JAMAIS ÊTRE CAPABLE DE PÉCHER ENCORE !!!!",
 hi_title: "उद्धरण: घर जा रहा हूँ",
 hi_content: "अधिकांश लोग 'खुद को नकारें' खंड पर ध्यान केंद्रित करते हैं, फिर भी यह इस कथन का केंद्रीय विचार नहीं है। यीशु का शिष्य बनने के लिए आपको यीशु का अनुसरण करना होगा...लेकिन यीशु कहाँ जा रहे हैं? वास्तविकता के संबंध में मैंने [भाग चौदह] (https://www.clmjournal.com/post/the-nrow-way-part-fourteen-discipleship) में जो कहा, उसके संबंध में, यीशु पिता के पास लौट रहे हैं जहां पाप, मृत्यु और दुःख मौजूद नहीं हैं... और वह आपको अपने साथ वहां लौटने के लिए आमंत्रित कर रहे हैं!!! 'बचाए जाने' का यही मूल अर्थ है, साथ ही दोबारा पाप करने में कभी सक्षम न होने का अतिरिक्त लाभ भी!!!!",
 zh_title: "yǐn yòng ： huí jiā",
 zh_content: "dà duō shù rén guān zhù “ fǒu dìng zì jǐ ” tiáo kuǎn ， dàn zhè bìng bú shì zhè jù huà de zhōng xīn sī xiǎng 。 yào chéng wéi yē sū de mén tú ， nǐ bì xū gēn suí yē sū …… dàn shì yē sū yào qù nǎ lǐ ？ guān yú wǒ zài [ dì shí sì bù fèn ](https://www.clmjournal.com/post/the-narrow-way-part-fourteen-discipleship) zhōng suǒ shuō de guān yú xiàn shí de nèi róng ， yē sū zhèng zài huí dào tiān fù nà lǐ ， nà lǐ bù cún zài zuì 、 sǐ wáng hé kǔ nàn …… tā yāo qǐng nǐ hé tā yì qǐ huí dào nà lǐ ！ zhè jiù shì “ dé jiù ” de hé xīn yì yì ， hái yǒu yí gè é wài de hǎo chù ， nà jiù shì yǒng yuǎn bù zài fàn zuì ！！！！"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.HEADING_HOME"})
MATCH (c:CONTENT {name: "content.HEADING_HOME"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.HEADING_HOME"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.TRUTH"})
MATCH (child:QUOTE {name: "quote.HEADING_HOME"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.TRUTH->HEADING_HOME"}]->(child);
```