---
name: "thought.THE_BIBLE"
alias: "Thought: THE BIBLE"
type: THOUGHT
parent: topic.HISTORY
tags:
- apocalypse
- bible
- rock
- spirituality
- delusion
neo4j: true
ptopic: "[[topic-HISTORY]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.THE_BIBLE",
    alias: "Thought: THE BIBLE",
    parent: "topic.HISTORY",
    tags: ["apocalypse", "bible", "rock", "spirituality", "delusion"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.THE_BIBLE",
    en_title: "THE BIBLE",
    en_content: "As time draws closer to the Return of Jesus and The Great Delusion begins to tighten its grip on the minds of the unsaved, the Role of the Bible as the Divinely-appointed Rule of Faith and Practice will suffer an increasingly vicious assault not only from outside the Assembly of Believers, but also increasingly from within!",
    es_title: "LA BIBLIA",
    es_content: "A medida que el tiempo se acerca al Retorno de Jesús y el Gran Engaño comienza a afianzarse en las mentes de los no salvos, el papel de la Biblia como Regla de fe y práctica divinamente designada sufrirá un ataque cada vez más cruel no sólo desde fuera de la Asamblea de Creyentes, ¡sino también cada vez más desde dentro!",
    fr_title: "LA BIBLE",
    fr_content: "À mesure que le temps se rapproche du retour de Jésus et que la Grande Illusion commence à resserrer son emprise sur l’esprit de ceux qui ne sont pas sauvés, le rôle de la Bible en tant que règle de foi et de pratique divinement désignée subira une agression de plus en plus vicieuse, non seulement de l’extérieur de l’Assemblée des croyants, mais aussi de plus en plus de l’intérieur !",
    hi_title: "बाइबिल",
    hi_content: "जैसे-जैसे समय यीशु की वापसी के करीब आता है और महान भ्रम ने बचाए नहीं गए लोगों के दिमाग पर अपनी पकड़ मजबूत करना शुरू कर दिया है, आस्था और अभ्यास के दैवीय रूप से नियुक्त नियम के रूप में बाइबिल की भूमिका पर न केवल विश्वासियों की सभा के बाहर से, बल्कि अंदर से भी तेजी से खतरनाक हमला होगा!",
    zh_title: "shèng jīng",
    zh_content: "suí zhe yē sū zài lái de shí jiān yuè lái yuè jìn ， dà wàng xiǎng kāi shǐ jiā qiáng duì wèi dé jiù zhī rén de kòng zhì ， shèng jīng zuò wéi shén suǒ zhǐ dìng de xìn yǎng hé shí jiàn guī zé de zuò yòng jiāng zāo shòu yuè lái yuè è dú de gōng jī ， bù jǐn lái zì xìn tú dà huì zhī wài ， ér qiě yě yuè lái yuè lái zì nèi bù ！"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.THE_BIBLE" AND c.name = "content.THE_BIBLE"
MERGE (t)-[:HAS_CONTENT {name: "edge.THE_BIBLE"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HISTORY" AND child.name = "thought.THE_BIBLE"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.HISTORY->THE_BIBLE"}]->(child);
```
