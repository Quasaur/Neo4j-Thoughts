---
type: THOUGHT
name: "thought.DIFFICULTY"
alias: "Thought: Difficulty"
parent: "topic.ATTITUDE"
en_content: "There is nothing harder in life than being a Christian—but it is NOT because Christianity is difficult! It is because I am hard: hard-hearted, hard-headed, and hard of hearing! I need to ask Jesus to soften me!"
tags: ["difficulty", "challenge", "struggle", "humility", "confession"]
ptopic: "[[topic-ATTITUDE]]"
level: 3
neo4j: true
verified: true
---


```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Dec-2013)
CREATE (t:THOUGHT {
    name: "thought.DIFFICULTY",
    alias: "Thought: Difficulty",
    parent: "topic.ATTITUDE",
    tags: ["difficulty", "challenge", "struggle", "humility", "confession"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.DIFFICULTY",
    ctype: "THOUGHT",
    en_title: "Thought: Difficulty",
    en_content: "There is nothing harder in life than being a Christian—but it is NOT because Christianity is difficult! It is because I am hard: hard-hearted, hard-headed, and hard of hearing! I need to ask Jesus to soften me!",
    es_title: "Pensamiento: Dificultad",
    es_content: "No hay nada más difícil en la vida que ser cristiano, ¡pero NO es porque el cristianismo sea difícil! Es porque soy duro: ¡de corazón duro, testarudo y sordo! ¡Necesito pedirle a Jesús que me ablande!",
    fr_title: "Pensée : Difficulté",
    fr_content: "Il n’y a rien de plus difficile dans la vie que d’être chrétien, mais ce n’est PAS parce que le christianisme est difficile ! C'est parce que je suis dur : dur de cœur, dur de tête et malentendant ! Je dois demander à Jésus de m'adoucir !",
    hi_title: "सोचा: कठिनाई",
    hi_content: "जीवन में ईसाई होने से कठिन कुछ भी नहीं है—लेकिन ऐसा इसलिए नहीं है क्योंकि ईसाई धर्म कठिन है! ऐसा इसलिए है क्योंकि मैं कठोर हूं: कठोर हृदय वाला, कठोर दिमाग वाला और सुनने में कठोर! मुझे यीशु से मुझे नरम करने के लिए कहने की ज़रूरत है!",
    zh_title: "xiǎng fǎ : kùn nán",
    zh_content: "shēng huó zhōng méi yǒu shén me bǐ chéng wéi yī míng jī dū tú gèng kùn nán de le -- dàn zhè bìng bú shì yīn wèi jī dū jiào hěn nán ! yīn wèi wǒ yìng : xīn yìng 、 nǎo zi yìng 、 ěr lóng ! wǒ xū yào qiú yē sū ruǎn huà wǒ !"
});

// 2. Link Content to Thought using the variables 't' and 'c'
MERGE (t)-[r:HAS_CONTENT]->(c)
ON CREATE SET r.name = "t.edge.DIFFICULTY"
// 3. Pass 't' forward, find the Parent Topic, and link them
WITH t
MATCH (parent:TOPIC {name: "topic.ATTITUDE"})
MERGE (parent)-[r2:HAS_THOUGHT]->(t)
ON CREATE SET r2.name = "t.edge.ATTITUDE->DIFFICULTY"
RETURN t, parent;
```
