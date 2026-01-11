---
name: "thought.THE_REAL_YOU"
alias: "Thought: THE REAL YOU"
type: THOUGHT
parent: topic.GRACE
tags:
- identity
- selfimage
- imageofgod
- christian
- jesuschrist
neo4j: true
ptopic: "[[topic-GRACE]]"
level: 3
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.THE_REAL_YOU",
    alias: "Thought: THE REAL YOU",
    parent: "topic.GRACE",
    tags: ["identity", "selfimage", "imageofgod", "christian", "jesuschrist"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.THE_REAL_YOU",
    en_title: "THE REAL YOU",
    en_content: "Dear Christian: your earthly self is just an avatar.
Your Real Self is hid with Christ in GOD; that’s why Jesus MUST return: so that you (and everyone else) can behold who you really are! 
Colossians 3:1-4",
    es_title: "EL VERDADERO TÚ",
    es_content: "Querido cristiano: tu yo terrenal es sólo un avatar.
Tu Ser Real está escondido con Cristo en DIOS; es por eso que Jesús DEBE regresar: ¡para que tú (y todos los demás) puedas contemplar quién eres realmente! 
Colosenses 3:1-4",
    fr_title: "LE VRAI VOUS",
    fr_content: "Cher chrétien : votre moi terrestre n’est qu’un avatar.
Votre Soi Réel est caché avec Christ en DIEU ; c’est pourquoi Jésus DOIT revenir : pour que vous (et tous les autres) puissiez voir qui vous êtes vraiment ! 
Colossiens 3:1-4",
    hi_title: "असली आप",
    hi_content: "प्रिय ईसाई: आपका सांसारिक स्वंय सिर्फ एक अवतार है।
आपका वास्तविक स्वंय मसीह के साथ ईश्वर में छिपा हुआ है; इसीलिए यीशु को अवश्य लौटना चाहिए: ताकि आप (और बाकी सभी) देख सकें कि आप वास्तव में कौन हैं! 
कुलुस्सियों 3:1-4",
    zh_title: "zhēn shí de nǐ",
    zh_content: "qīn ài de jī dū tú ： nǐ chén shì de zì wǒ zhǐ shì yí gè huà shēn 。
 nǐ de zhēn shí zì wǒ yǔ jī dū yì qǐ yǐn cáng zài shàng dì zhī zhōng ； zhè jiù shì wèi shén me yē sū bì xū huí lái ： zhè yàng nǐ （ hé qí tā rén ） cái néng kàn dào nǐ dào dǐ shì shuí ！ 
 gē luó xī shū  3:1-4"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE_REAL_YOU" AND c.name = "content.THE_REAL_YOU"
MERGE (t)-[:HAS_CONTENT {name: "edge.THE_REAL_YOU"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.GRACE" AND child.name = "thought.THE_REAL_YOU"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.GRACE->THE_REAL_YOU"}]->(child);
```
