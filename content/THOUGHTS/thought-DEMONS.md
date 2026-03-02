---
type: THOUGHT
name: "thought.DEMONS"
alias: "Thought: DEMONS"
parent: "topic.SPIRITS"
tags: ["demons", "hardhearted", "grace", "divine", "jesus_christ"]
ptopic: "[[topic-SPIRITS]]"
level: 3
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.DEMONS",
    alias: "Thought: DEMONS",
    parent: "topic.SPIRITS",
    tags: ["demons", "hardhearted", "grace", "divine", "jesus_christ"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DEMONS",
    ctype: "THOUGHT",
    en_title: "DEMONS",
 es_title: "DEMONIOS",
 fr_title: "DÉMONS",
 hi_title: "राक्षसों",
 zh_title: "è mó",
    en_content: "",
 es_content: "Lo que pasó con los ángeles caídos será el destino inevitable de toda alma humana que rechace la Gracia de Cristo.
 Rechazar la Gracia Divina es eventualmente volverse completamente descortés, totalmente descortés, absolutamente despiadado, terriblemente antinatural, incorregiblemente abusivo, abismalmente loco y espantosamente demoníaco.
 HOY…SI ESCUCHAS SU VOZ ETERNA…¡NO ENDURECES TU CORAZÓN!",
 fr_content: "Ce qui est arrivé aux anges déchus sera le sort inévitable de toute âme humaine qui rejette la Grâce du Christ.
 Rejeter la Grâce Divine, c’est finalement devenir complètement sans grâce, totalement impitoyable, absolument impitoyable, terriblement contre nature, incorrigiblement abusif, épouvantablement fou et horriblement démoniaque.
 AUJOURD'HUI… SI VOUS ENTENDEZ SA VOIX ÉTERNELLE… N'ENDURCISSEZ PAS VOTRE COEUR !",
 hi_content: "गिरे हुए स्वर्गदूतों के साथ जो हुआ वह प्रत्येक मानव आत्मा का अपरिहार्य भाग्य होगा जो मसीह की कृपा को अस्वीकार करता है।
 दैवीय कृपा को अस्वीकार करना अंततः पूरी तरह से अनुग्रहहीन, पूरी तरह से कृतघ्न, बिल्कुल निर्दयी, भयावह रूप से अप्राकृतिक, बेहद अपमानजनक, बेहद पागल और भयानक राक्षसी बन जाना है।
 आज...यदि आप उनकी शाश्वत आवाज सुनते हैं...अपना दिल कठोर मत करो!",
 zh_content: "duò luò tiān shǐ de zāo yù jiāng shì měi gè jù jué jī dū ēn diǎn de rén lèi líng hún bù kě bì miǎn de mìng yùn 。
  jù jué shén shèng ēn diǎn zuì zhōng huì biàn dé wán quán méi yǒu ēn diǎn 、 wán quán bù rén cí 、 jué duì bù rén cí 、 lìng rén kǒng jù dì bù zì rán 、 wú kě jiù yào dì nüè dài 、 jí dù fēng kuáng hé kě pà de è mó 。
  jīn tiān …… rú guǒ nín tīng dào tā yǒng héng de shēng yīn …… qǐng bú yào yìng qǐ xīn lái ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.DEMONS" AND c.name = "content.DEMONS"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.DEMONS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.SPIRITS" AND child.name = "thought.DEMONS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.SPIRITS->DEMONS"}]->(child);
```