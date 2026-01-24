---
name: "thought.SCIENCE_CONSPIRACY"
alias: "Thought: SCIENCE CONSPIRACY"
type: THOUGHT
parent: topic.COSMOLOGY
tags:
- science
- cosmology
- geocentricity
- michelson
- creationism
neo4j: true
ptopic: "[[topic-COSMOLOGY]]"
level: 4
inserted: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SCIENCE_CONSPIRACY",
    alias: "Thought: SCIENCE CONSPIRACY",
    parent: "topic.COSMOLOGY",
    tags: ["science", "cosmology", "geocentricity", "michelson", "creationism"],
    level: 4
});

CREATE (c:CONTENT {
    name: "content.SCIENCE_CONSPIRACY",
    en_title: "SCIENCE CONSPIRACY",
    en_content: "The gods of the scientific community have deceived us: Einstein’s special and general theories of relativity CONTRADICT each other: either the speed of light is unchangeable or the Earth is, in fact, the center of the known universe!
Michelson’s two experiments verify the existence of the ETHER…nullifying special relativity entirely!
A standard model based on a geocentric universe is less complicated, makes more sense and eliminates the need for “dark” matter & energy. “NOTHING”, BY DEFINITION, DOES NOT EXIST.",
    es_title: "CONSPIRACIÓN CIENTÍFICA",
    es_content: "Los dioses de la comunidad científica nos han engañado: las teorías de la relatividad especial y general de Einstein se CONTRADICTAN entre sí: ¡o la velocidad de la luz es inmutable o la Tierra es, de hecho, el centro del universo conocido!
Los dos experimentos de Michelson verifican la existencia del ÉTER… ¡anulando por completo la relatividad especial!
Un modelo estándar basado en un universo geocéntrico es menos complicado, tiene más sentido y elimina la necesidad de materia y energía \"oscuras\". “NADA”, POR DEFINICIÓN, NO EXISTE.",
    fr_title: "CONSPIRATION SCIENTIFIQUE",
    fr_content: "Les dieux de la communauté scientifique nous ont trompés : les théories de la relativité restreinte et générale d’Einstein se CONTRADIVENT : soit la vitesse de la lumière est immuable, soit la Terre est, en fait, le centre de l’univers connu !
Les deux expériences de Michelson vérifient l’existence de l’ETHER… annulant complètement la relativité restreinte !
Un modèle standard basé sur un univers géocentrique est moins compliqué, a plus de sens et élimine le besoin de matière et d’énergie « sombres ». « RIEN », PAR DÉFINITION, N’EXISTE PAS.",
    hi_title: "विज्ञान षडयंत्र",
    hi_content: "वैज्ञानिक समुदाय के देवताओं ने हमें धोखा दिया है: आइंस्टीन के सापेक्षता के विशेष और सामान्य सिद्धांत एक-दूसरे के विपरीत हैं: या तो प्रकाश की गति अपरिवर्तनीय है या पृथ्वी, वास्तव में, ज्ञात ब्रह्मांड का केंद्र है!
माइकलसन के दो प्रयोग ईथर के अस्तित्व की पुष्टि करते हैं... विशेष सापेक्षता को पूरी तरह से समाप्त कर देते हैं!
भूकेंद्रिक ब्रह्मांड पर आधारित एक मानक मॉडल कम जटिल है, अधिक अर्थपूर्ण है और \"अंधेरे\" पदार्थ और ऊर्जा की आवश्यकता को समाप्त करता है। परिभाषा के अनुसार, \"कुछ भी नहीं\", अस्तित्व में नहीं है।",
    zh_title: "kē xué yīn móu",
    zh_content: "kē xué jiè de zhū shén qī piàn le wǒ men ： ài yīn sī tǎn de xiá yì xiāng duì lùn hé guǎng yì xiāng duì lùn xiāng hù máo dùn ： yào me guāng sù bù biàn ， yào me dì qiú shí jì shàng shì yǐ zhī yǔ zhòu de zhōng xīn ！
 mài kè ěr xùn de liǎng gè shí yàn zhèng shí le yǐ tài de cún zài …… wán quán fǒu dìng le xiá yì xiāng duì lùn ！
 jī yú dì xīn yǔ zhòu de biāo zhǔn mó xíng bù tài fù zá ， gèng yǒu yì yì ， bìng qiě xiāo chú le duì “ àn ” wù zhì hé néng liàng de xū qiú 。 gēn jù dìng yì ，“ wú ” shì bù cún zài de 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SCIENCE_CONSPIRACY" AND c.name = "content.SCIENCE_CONSPIRACY"
MERGE (t)-[:HAS_CONTENT {name: "edge.SCIENCE_CONSPIRACY"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.COSMOLOGY" AND child.name = "thought.SCIENCE_CONSPIRACY"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.COSMOLOGY->SCIENCE_CONSPIRACY"}]->(child);
```
