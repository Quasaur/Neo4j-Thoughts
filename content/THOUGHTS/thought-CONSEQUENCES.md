---
type: THOUGHT
name: "thought.CONSEQUENCES"
alias: "Thought: Consequences"
parent: "topic.MERCY"
tags: ["consequences", "mercy", "sovereignty", "sin", "suffering"]
ptopic: "[[topic-MERCY]]"
level: 4
neo4j: true
verified: false
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.CONSEQUENCES",
    alias: "Thought: Consequences",
    parent: "topic.MERCY",
    tags: ["consequences", "mercy", "sovereignty", "sin", "suffering"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.CONSEQUENCES",
    ctype: "THOUGHT",
    en_title: "Consequences",
 es_title: "CONSECUENCIAS",
 fr_title: "CONSÉQUENCES",
 hi_title: "नतीजे",
 zh_title: "jié guǒ",
    en_content: "",
 es_content: "La misericordia misma tiene consecuencias que nunca ocurren en la mente del pecador egoísta y obsesionado con sí mismo. 
Misericordia significa que Lucifer se convierte en Satanás. 
Misericordia significa que Satanás seduce a un tercio de los ángeles del Cielo, condenándolos a la vergüenza eterna. 
Misericordia significa permitir que Satanás tiente al puro e inocente Adán y a su esposa Eva. 
Misericordia significa miles de años de muerte, abuso, violación, tortura, hambre, desastres naturales y provocados por el hombre, plagas, enfermedades, guerra, desintegración de familias, lo oculto, oscuridad profunda, engaño y ceguera.",
 fr_content: "La miséricorde elle-même a des conséquences qui ne viennent jamais à l’esprit du pécheur égoïste et obsédé par lui-même. 
La miséricorde signifie que Lucifer devient Satan. 
La miséricorde signifie que Satan séduit un tiers des anges du Ciel, les condamnant à une honte éternelle. 
La miséricorde signifie permettre à Satan de tenter Adam, pur et innocent, et sa femme Ève. 
La miséricorde signifie des milliers d'années de mort, d'abus, de viols, de torture, de famine, de catastrophes naturelles et d'origine humaine, de peste, de maladie, de guerre, de déchirement des familles, d'occultisme, d'obscurité profonde, de tromperie et d'aveuglement.",
 hi_content: "दया के स्वयं ऐसे परिणाम होते हैं जो स्वार्थी, आत्म-मुग्ध पापी के दिमाग में कभी नहीं आते हैं। 
दया का अर्थ है लूसिफ़ेर शैतान बन जाता है। 
दया का अर्थ है कि शैतान स्वर्ग के एक तिहाई स्वर्गदूतों को बहकाता है, और उन्हें शाश्वत शर्मिंदगी का शिकार बनाता है। 
दया का अर्थ है शैतान को शुद्ध और निर्दोष आदम और उसकी पत्नी हव्वा को प्रलोभित करने की अनुमति देना। 
दया का अर्थ है हजारों वर्षों की मृत्यु, दुर्व्यवहार, बलात्कार, यातना, भुखमरी, अकाल, प्राकृतिक और मानव निर्मित आपदाएँ, प्लेग, बीमारी, युद्ध, परिवारों का टूटना, जादू-टोना, गहरा अंधकार, धोखा और अंधापन।",
 zh_content: "lián mǐn běn shēn suǒ dài lái de hòu guǒ shì zì sī 、 zì liàn de zuì rén yǒng yuǎn bú huì xiǎng dào de 。 
 lián mǐn yì wèi zhe lù xī fǎ biàn chéng sā dàn 。 
 lián mǐn yì wèi zhe sā dàn yǐn yòu le sān fēn zhī yī de tiān táng tiān shǐ ， ràng tā men zāo shòu yǒng yuǎn de chǐ rǔ 。 
 lián mǐn yì wèi zhe yǔn xǔ sā dàn yòu huò chún jié wú zuì de yà dāng hé tā de qī zǐ xià wá 。 
 cí bēi yì wèi zhe shù qiān nián de sǐ wáng 、 nüè dài 、 qiáng jiān 、 kù xíng 、 jī è 、 jī huāng 、 tiān zāi rén huò 、 wēn yì 、 jí bìng 、 zhàn zhēng 、 jiā tíng pò liè 、 shén mì 、 hēi àn 、 qī piàn hé shī míng 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.CONSEQUENCES" AND c.name = "content.CONSEQUENCES"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.CONSEQUENCES"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MERCY" AND child.name = "thought.CONSEQUENCES"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.MERCY->CONSEQUENCES"}]->(child);
```