---
type: QUOTE
name: "quote.GOD_IS_GENEROUS"
alias: "Quote: Quote: GOD IS GENEROUS"
parent: "topic.GRACE"
en_content: "GOD IS GENEROUS! He is generous to angel and demon…saint and sinner. He is not only more generous than anyone else, He was generous before anyone else! Look at the size of your planet, your solar system, your galaxy, your local group of galaxies—your universe! Look at the size of your family, your clan, your tribe, your nation! For the Love of GOD…YOU EXIST!!! Forever dismiss from your mind the idea that GOD is stingy…YOU are stingy; GOD is immeasurably magnanimous!",
 es_title: "Cita: DIOS ES GENEROSO",
 es_content: "¡DIOS ES GENEROSO! Es generoso con los ángeles y los demonios... con los santos y los pecadores. ¡Él no sólo es más generoso que nadie, sino que fue generoso antes que nadie! Mire el tamaño de su planeta, su sistema solar, su galaxia, su grupo local de galaxias: ¡su universo! ¡Mira el tamaño de tu familia, tu clan, tu tribu, tu nación! Por el Amor de DIOS… ¡¡¡TÚ EXISTES!!! Descarta para siempre de tu mente la idea de que DIOS es tacaño… TÚ eres tacaño; ¡DIOS es inmensamente magnánimo!",
 fr_title: "Citation : DIEU EST GÉNÉREUX",
 fr_content: "DIEU EST GÉNÉREUX ! Il est généreux envers les anges et les démons… les saints et les pécheurs. Non seulement il est plus généreux que quiconque, mais il l’a été avant tout le monde ! Regardez la taille de votre planète, de votre système solaire, de votre galaxie, de votre groupe local de galaxies – de votre univers ! Regardez la taille de votre famille, de votre clan, de votre tribu, de votre nation ! Pour l’Amour de DIEU… VOUS EXISTEZ !!! Éliminez à jamais de votre esprit l’idée que DIEU est avare… VOUS êtes avare ; DIEU est infiniment magnanime !",
 hi_title: "उद्धरण: ईश्वर उदार है",
 hi_content: "भगवान उदार है! वह देवदूत और दानव...संत और पापी के प्रति उदार है। वह न केवल किसी और से अधिक उदार है, बल्कि वह किसी और से भी पहले उदार था! अपने ग्रह, अपने सौर मंडल, अपनी आकाशगंगा, अपने स्थानीय आकाशगंगा समूह-अपने ब्रह्मांड के आकार को देखें! अपने परिवार, अपने कुल, अपने गोत्र, अपने राष्ट्र के आकार को देखो! ईश्वर के प्रेम के लिए...आपका अस्तित्व है!!! अपने मन से यह विचार हमेशा के लिए निकाल दें कि ईश्वर कंजूस है...आप कंजूस हैं; ईश्वर अत्यंत उदार है!",
 zh_title: "yǐn yòng ： shàng dì shì kāng kǎi de",
 zh_content: "shàng dì shì kāng kǎi de ！ tā duì tiān shǐ hé è mó …… shèng rén hé zuì rén dōu hěn kāng kǎi 。 tā bù jǐn bǐ rèn hé rén dōu kāng kǎi ， ér qiě bǐ rèn hé rén dōu kāng kǎi ！ kàn kàn nǐ de xīng qiú 、 nǐ de tài yáng xì 、 nǐ de xīng xì 、 nǐ de běn dì xīng xì qún —— nǐ de yǔ zhòu de dà xiǎo ！ kàn kàn nǐ de jiā tíng 、 nǐ de shì zú 、 nǐ de bù luò 、 nǐ de guó jiā yǒu duō dà ！ wèi le shàng dì de ài …… nǐ cún zài ！！！ yǒng yuǎn cóng nǐ de nǎo hǎi zhōng xiāo chú shàng dì shì xiǎo qì de xiǎng fǎ …… nǐ shì xiǎo qì de ； nǐ shì xiǎo qì de ； nǐ shì xiǎo qì de ； nǐ shì xiǎo qì de ； nǐ shì xiǎo qì de 。 shàng dì shì wú bǐ kuān hóng de ！"
tags: ["god", "generous", "magnanimous", "gracious", "stingy"]
ptopic: "[[topic-GRACE]]"
level: 3
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.GOD_IS_GENEROUS",
    alias: "Quote: Quote: GOD IS GENEROUS",
    parent: "topic.GRACE",
    tags: ["god", "generous", "magnanimous", "gracious", "stingy"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.GOD_IS_GENEROUS",
    ctype: "QUOTE",
    en_title: "Quote: GOD IS GENEROUS",
    en_content: "GOD IS GENEROUS! He is generous to angel and demon…saint and sinner. He is not only more generous than anyone else, He was generous before anyone else! Look at the size of your planet, your solar system, your galaxy, your local group of galaxies—your universe! Look at the size of your family, your clan, your tribe, your nation! For the Love of GOD…YOU EXIST!!! Forever dismiss from your mind the idea that GOD is stingy…YOU are stingy; GOD is immeasurably magnanimous!",
 es_title: "Cita: DIOS ES GENEROSO",
 es_content: "¡DIOS ES GENEROSO! Es generoso con los ángeles y los demonios... con los santos y los pecadores. ¡Él no sólo es más generoso que nadie, sino que fue generoso antes que nadie! Mire el tamaño de su planeta, su sistema solar, su galaxia, su grupo local de galaxias: ¡su universo! ¡Mira el tamaño de tu familia, tu clan, tu tribu, tu nación! Por el Amor de DIOS… ¡¡¡TÚ EXISTES!!! Descarta para siempre de tu mente la idea de que DIOS es tacaño… TÚ eres tacaño; ¡DIOS es inmensamente magnánimo!",
 fr_title: "Citation : DIEU EST GÉNÉREUX",
 fr_content: "DIEU EST GÉNÉREUX ! Il est généreux envers les anges et les démons… les saints et les pécheurs. Non seulement il est plus généreux que quiconque, mais il l’a été avant tout le monde ! Regardez la taille de votre planète, de votre système solaire, de votre galaxie, de votre groupe local de galaxies – de votre univers ! Regardez la taille de votre famille, de votre clan, de votre tribu, de votre nation ! Pour l’Amour de DIEU… VOUS EXISTEZ !!! Éliminez à jamais de votre esprit l’idée que DIEU est avare… VOUS êtes avare ; DIEU est infiniment magnanime !",
 hi_title: "उद्धरण: ईश्वर उदार है",
 hi_content: "भगवान उदार है! वह देवदूत और दानव...संत और पापी के प्रति उदार है। वह न केवल किसी और से अधिक उदार है, बल्कि वह किसी और से भी पहले उदार था! अपने ग्रह, अपने सौर मंडल, अपनी आकाशगंगा, अपने स्थानीय आकाशगंगा समूह-अपने ब्रह्मांड के आकार को देखें! अपने परिवार, अपने कुल, अपने गोत्र, अपने राष्ट्र के आकार को देखो! ईश्वर के प्रेम के लिए...आपका अस्तित्व है!!! अपने मन से यह विचार हमेशा के लिए निकाल दें कि ईश्वर कंजूस है...आप कंजूस हैं; ईश्वर अत्यंत उदार है!",
 zh_title: "yǐn yòng ： shàng dì shì kāng kǎi de",
 zh_content: "shàng dì shì kāng kǎi de ！ tā duì tiān shǐ hé è mó …… shèng rén hé zuì rén dōu hěn kāng kǎi 。 tā bù jǐn bǐ rèn hé rén dōu kāng kǎi ， ér qiě bǐ rèn hé rén dōu kāng kǎi ！ kàn kàn nǐ de xīng qiú 、 nǐ de tài yáng xì 、 nǐ de xīng xì 、 nǐ de běn dì xīng xì qún —— nǐ de yǔ zhòu de dà xiǎo ！ kàn kàn nǐ de jiā tíng 、 nǐ de shì zú 、 nǐ de bù luò 、 nǐ de guó jiā yǒu duō dà ！ wèi le shàng dì de ài …… nǐ cún zài ！！！ yǒng yuǎn cóng nǐ de nǎo hǎi zhōng xiāo chú shàng dì shì xiǎo qì de xiǎng fǎ …… nǐ shì xiǎo qì de ； nǐ shì xiǎo qì de ； nǐ shì xiǎo qì de ； nǐ shì xiǎo qì de ； nǐ shì xiǎo qì de 。 shàng dì shì wú bǐ kuān hóng de ！"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.GOD_IS_GENEROUS"})
MATCH (c:CONTENT {name: "content.GOD_IS_GENEROUS"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.GOD_IS_GENEROUS"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.GRACE"})
MATCH (child:QUOTE {name: "quote.GOD_IS_GENEROUS"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.GRACE->GOD_IS_GENEROUS"}]->(child);

```
