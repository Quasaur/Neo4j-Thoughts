---
type: QUOTE
name: "quote.THE DESIRE TO RETURN"
alias: "Quote: The Desire to Return"
parent: "topic.EVIL"
en_content: "While any sinner would DO EVERYTHING POSSIBLE to avoid the Lake of Fire, no sinner has ANY DESIRE IN THEIR HEART WHATSOEVER to return to God (repentance).",
 es_title: "Cita: EL DESEO DE VOLVER",
 es_content: "Si bien cualquier pecador haría TODO LO POSIBLE para evitar el Lago de Fuego, ningún pecador tiene NINGÚN DESEO EN SU CORAZÓN de regresar a Dios (arrepentimiento).",
 fr_title: "Citation : LE DÉSIR DE RETOUR",
 fr_content: "Alors que n'importe quel pécheur ferait TOUT POSSIBLE pour éviter l'étang de feu, aucun pécheur n'a AUCUN DÉSIR DANS SON CŒUR QUE CE SOIT de retourner à Dieu (repentir).",
 hi_title: "उद्धरण: लौटने की इच्छा",
 hi_content: "जबकि कोई भी पापी आग की झील से बचने के लिए हर संभव प्रयास करेगा, किसी भी पापी के दिल में भगवान के पास लौटने (पश्चाताप) की कोई इच्छा नहीं है।",
 zh_title: "yǐn yòng ： huí guī de yuàn wàng",
 zh_content: "suī rán rèn hé zuì rén dū huì jǐn yī qiè kě néng bì miǎn huǒ hú ， dàn méi yǒu zuì rén nèi xīn yǒu rèn hé kě wàng huí dào shàng dì shēn biān （ huǐ gǎi ）。"
tags: ["survival", "lake_of_fire", "repentance", "sinner", "god"]
ptopic: "[[topic-EVIL]]"
level: 4
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE DESIRE TO RETURN",
    alias: "Quote: The Desire to Return",
    parent: "topic.EVIL",
    tags: ["survival", "lake_of_fire", "repentance", "sinner", "god"],
    source: "'IMMMUNITY to the Lake of Fire: A No-Nonsense Guide'",
    booklink: "(https://www.amazon.com/IMMUNITY-LAKE-FIRE-No-Nonsense-Guide-ebook/dp/B08B5J9V8J)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE DESIRE TO RETURN",
    ctype: "QUOTE",
    en_title: "The Desire to Return",
    en_content: "While any sinner would DO EVERYTHING POSSIBLE to avoid the Lake of Fire, no sinner has ANY DESIRE IN THEIR HEART WHATSOEVER to return to God (repentance).",
 es_title: "Cita: EL DESEO DE VOLVER",
 es_content: "Si bien cualquier pecador haría TODO LO POSIBLE para evitar el Lago de Fuego, ningún pecador tiene NINGÚN DESEO EN SU CORAZÓN de regresar a Dios (arrepentimiento).",
 fr_title: "Citation : LE DÉSIR DE RETOUR",
 fr_content: "Alors que n'importe quel pécheur ferait TOUT POSSIBLE pour éviter l'étang de feu, aucun pécheur n'a AUCUN DÉSIR DANS SON CŒUR QUE CE SOIT de retourner à Dieu (repentir).",
 hi_title: "उद्धरण: लौटने की इच्छा",
 hi_content: "जबकि कोई भी पापी आग की झील से बचने के लिए हर संभव प्रयास करेगा, किसी भी पापी के दिल में भगवान के पास लौटने (पश्चाताप) की कोई इच्छा नहीं है।",
 zh_title: "yǐn yòng ： huí guī de yuàn wàng",
 zh_content: "suī rán rèn hé zuì rén dū huì jǐn yī qiè kě néng bì miǎn huǒ hú ， dàn méi yǒu zuì rén nèi xīn yǒu rèn hé kě wàng huí dào shàng dì shēn biān （ huǐ gǎi ）。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.THE DESIRE TO RETURN"})
MATCH (c:CONTENT {name: "content.THE DESIRE TO RETURN"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE DESIRE TO RETURN"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:QUOTE {name: "quote.THE DESIRE TO RETURN"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.EVIL->THE DESIRE TO RETURN"}]->(child);

```
