---
title: "Thought: EMPTINESS"
draft: false
type: THOUGHT
mling: false
tags:
  - emptiness
  - void
  - hunger
  - addiction
  - spirituality
neo4j: true
ptopic: "[[topic-THE-GODHEAD]]"
level: 1
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.EMPTINESS",
    alias: "Thought: The Void Within",
    parent: "topic.THE GODHEAD",
    tags: ["emptiness", "void", "hunger", "addiction", "spirituality"],
    level: 1
});

CREATE (c:CONTENT {
    name: "content.EMPTINESS",
    en_title: "EMPTINESS",
    en_content: "It’s why we eat when we’re not hungry.
It’s why we watch hours of mindless television and play with ouija boards and horoscopes.
It’s why we pursue one addiction after another, and there’s only One Cure that will fill that black hole in the core of our being: The Lord Jesus Christ. 
How insane it is, then, to attend Church for years and NEVER meet Jesus!!!",
    es_title: "VACÍO",
    es_content: "Por eso comemos cuando no tenemos hambre.
Es por eso que miramos horas de televisión sin sentido y jugamos con tablas ouija y horóscopos.
Es por eso que perseguimos una adicción tras otra, y solo hay una cura que llenará ese agujero negro en el centro de nuestro ser: el Señor Jesucristo. 
¡¡¡Qué locura es, entonces, asistir a la Iglesia durante años y NUNCA conocer a Jesús!!!",
    fr_title: "VIDE",
    fr_content: "C’est pour cela que nous mangeons quand nous n’avons pas faim.
C’est pourquoi nous regardons des heures de télévision stupide et jouons avec des planches ouija et des horoscopes.
C’est pourquoi nous poursuivons une dépendance après l’autre, et il n’y a qu’un seul remède qui comblera ce trou noir au cœur de notre être : le Seigneur Jésus-Christ. 
Comme il est donc insensé d'aller à l'église pendant des années et de ne JAMAIS rencontrer Jésus !!!",
    hi_title: "शून्यता",
    hi_content: "यही कारण है कि जब हमें भूख नहीं होती तो हम खाते हैं।
यही कारण है कि हम घंटों बिना सोचे-समझे टेलीविजन देखते हैं और ओइजा बोर्ड और राशिफल के साथ खेलते हैं।
यही कारण है कि हम एक के बाद एक लत का पीछा करते हैं, और केवल एक ही इलाज है जो हमारे अस्तित्व के मूल में उस काले छेद को भर देगा: प्रभु यीशु मसीह। 
तो फिर, यह कितना पागलपन है कि वर्षों तक चर्च जाते रहें और कभी यीशु से न मिलें!!!",
    zh_title: "kōng xū",
    zh_content: "zhè jiù shì wèi shén me wǒ men bù è de shí hòu jiù chī dōng xī 。
 zhè jiù shì wèi shén me wǒ men huì huā jǐ gè xiǎo shí wú yì shí dì kàn diàn shì 、 wán xiǎn líng bǎn hé zhān xīng shù 。
 zhè jiù shì wèi shén me wǒ men chén mí yú yī zhǒng yòu yī zhǒng de yuán yīn ， ér zhǐ yǒu yī zhǒng zhì liáo fāng fǎ kě yǐ tián bǔ wǒ men cún zài hé xīn de hēi dòng ： zhǔ yē sū jī dū 。 
 nà me ， duō nián lái qù jiào huì què cóng wèi jiàn guò yē sū ， zhè shì duō me fēng kuáng a ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.EMPTINESS" AND c.name = "content.EMPTINESS"
MERGE (t)-[:HAS_CONTENT {name: "edge.EMPTINESS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.THE GODHEAD" AND child.name = "thought.EMPTINESS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.THE GODHEAD->EMPTINESS"}]->(child);
```
