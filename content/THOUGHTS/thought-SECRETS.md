---
type: THOUGHT
name: "thought.SECRETS"
alias: "Thought: Secrets"
parent: "topic.PSYCHOLOGY"
tags: ["secrets", "distractions", "eternity", "immortality", "transcendence"]
ptopic: "[[topic-PSYCHOLOGY]]"
level: 4
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SECRETS",
    alias: "Thought: Secrets",
    parent: "topic.PSYCHOLOGY",
    tags: ["secrets", "distractions", "eternity", "immortality", "transcendence"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.SECRETS",
    ctype: "THOUGHT",
    en_title: "Secrets",
 es_title: "MISTERIOS",
 fr_title: "SECRETS",
 hi_title: "रहस्य",
 zh_title: "mì mì",
    en_content: "",
 es_content: "Los SECRETOS DEL UNIVERSO, incluyendo la inmortalidad y la trascendencia, están a tu alrededor… justo debajo de tus narices; pero sin OJOS para ver y OÍDOS para oír, los extrañarás en la cacofonía que te distrae de la “vida” terrenal y eventualmente te encontrarás en una ETERNIDAD de miseria indescriptible porque estabas demasiado ocupado “haciéndote a ti mismo”.
Mateo 7:13,14",
 fr_content: "Les SECRETS DE L'UNIVERS, y compris l'immortalité et la transcendance, sont tout autour de vous… juste sous votre nez ; mais sans YEUX pour voir et sans OREILLES pour entendre, vous les manquerez dans la cacophonie distrayante de la « vie » terrestre et vous finirez par vous retrouver dans une ÉTERNITÉ de misère indescriptible parce que vous étiez trop occupé à « vous faire ».
Matthieu 7:13,14",
 hi_content: "ब्रह्मांड के रहस्य, अमरता और उत्कृष्टता सहित, आपके चारों ओर हैं... ठीक आपकी नाक के नीचे; लेकिन देखने के लिए आँखों और सुनने के लिए कानों के बिना, आप सांसारिक \"जीवन\" के विचलित करने वाले शोर में उन्हें याद करेंगे और अंततः अपने आप को अवर्णनीय दुख की अनंत काल में पाएंगे क्योंकि आप \"अपने काम\" में बहुत व्यस्त थे।
मत्ती 7:13,14"जीवन\" के विचलित करने वाले शोर में उन्हें याद करेंगे और अंततः अपने आप को अवर्णनीय दुख की अनंत काल में पाएंगे क्योंकि आप \"अपने काम\" में बहुत व्यस्त थे।
मत्ती 7:13,14"जीवन\" के विचलित करने वाले शोर में उन्हें याद करेंगे और अंततः अपने आप को अवर्णनीय दुख की अनंत काल में पाएंगे क्योंकि आप \"अपने काम\" में बहुत व्यस्त थे।
मत्ती 7:13,14"जीवन\" के विचलित करने वाले शोर में उन्हें याद करेंगे और अंततः अपने आप को अवर्णनीय दुख की अनंत काल में पाएंगे क्योंकि आप \"अपने काम\" में बहुत व्यस्त थे।
मत्ती 7:13,14",
 zh_content: "yǔ zhòu de mì mì ， bāo kuò yǒng shēng hé chāo yuè ， jiù zài nǐ zhōu wéi …… jiù zài nǐ yǎn pí dǐ xià ； dàn rú guǒ méi yǒu yǎn jīng qù kàn ， méi yǒu ěr duǒ qù tīng ， nǐ jiù huì zài chén shì “ shēng huó ” de xuān xiāo zhōng cuò guò tā men ， bìng zuì zhōng fā xiàn zì jǐ xiàn rù liǎo wú fǎ xíng róng de tòng kǔ zhī zhōng ， yīn wèi nǐ tài máng yú “ zuò nǐ zì jǐ ”。
 mǎ tài fú yīn  7:13,14"जीवन\" के विचलित करने वाले शोर में उन्हें याद करेंगे और अंततः अपने आप को अवर्णनीय दुख की अनंत काल में पाएंगे क्योंकि आप \"अपने काम\" में बहुत व्यस्त थे।\nमत्ती 7:13,14"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SECRETS" AND c.name = "content.SECRETS"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.SECRETS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.PSYCHOLOGY" AND child.name = "thought.SECRETS"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.PSYCHOLOGY->SECRETS"}]->(child);
```