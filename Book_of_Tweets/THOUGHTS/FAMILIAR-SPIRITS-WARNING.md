---
name: "thought.FAMILIAR SPIRITS WARNING"
alias: "Thought: Familiar Spirits Warning"
type: THOUGHT
en_content: "\"You do not turn nor seek to those having familiar spirits nor necromancers to be unclean by them; I am YHWH your God.\" -- Leviticus 19:31"
parent: "topic.EVIL"
tags:
- occult
- spirits
- evil
- law
- bible
level: 4
neo4j: false
ptopic: 
---

```Cypher
// Generated from Book6E-FINAL.md (ID: 26-Sep-2011)
CREATE (t:THOUGHT {
    name: "thought.FAMILIAR SPIRITS WARNING",
    alias: "Thought: Familiar Spirits Warning",
    parent: "topic.EVIL",
    tags: ['occult', 'spirits', 'evil', 'law', 'bible'],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.FAMILIAR SPIRITS WARNING",
    en_title: "Familiar Spirits Warning",
    en_content: "\"You do not turn nor seek to those having familiar spirits nor necromancers to be unclean by them; I am YHWH your God.\" -- Leviticus 19:31",
    es_title: "Advertencia sobre Espíritus Familiares",
    es_content: "Los espíritus familiares son entidades demoniacas que se disfrazan como seres queridos fallecidos o guías espirituales benevolentes. La Escritura advierte claramente contra buscar comunicación con los muertos (Deuteronomio 18:10-12). Estos espíritus engañosos explotan nuestro dolor y curiosidad, llevándonos lejos de la verdad de Cristo. Como creyentes, debemos discernir espiritualmente y rechazar cualquier práctica que abra puertas a estos engaños, confiando en cambio en la guía del Espíritu Santo y la Palabra de Dios.",
    fr_title: "Avertissement sur les Esprits Familiers",
    fr_content: "Les esprits familiers sont des entités démoniaques qui se déguisent en proches décédés ou en guides spirituels bienveillants. L'Écriture met clairement en garde contre la recherche de communication avec les morts (Deutéronome 18:10-12). Ces esprits trompeurs exploitent notre chagrin et notre curiosité, nous éloignant de la vérité du Christ. En tant que croyants, nous devons faire preuve de discernement spirituel et rejeter toute pratique qui ouvre des portes à ces tromperies, nous appuyant plutôt sur la guidance du Saint-Esprit et la Parole de Dieu.",
    hi_title: "परिचित आत्माओं की चेतावनी",
    hi_content: "परिचित आत्माएं दुष्ट आत्माएं हैं जो मृत प्रियजनों या कृपालु आध्यात्मिक मार्गदर्शकों का भेष धारण करती हैं। शास्त्र स्पष्ट रूप से मृतकों के साथ संवाद स्थापित करने के विरुद्ध चेतावनी देता है (व्यवस्थाविवरण 18:10-12)। ये धोखेबाज आत्माएं हमारे दुःख और जिज्ञासा का फायदा उठाकर हमें मसीह के सत्य से दूर ले जाती हैं। विश्वासियों के रूप में, हमें आध्यात्मिक विवेक रखना चाहिए और ऐसी किसी भी प्रथा को अस्वीकार करना चाहिए जो इन धोखों के लिए द्वार खोलती है, बल्कि पवित्र आत्मा के मार्गदर्शन और परमेश्वर के वचन पर भरोसा करना चाहिए।",
    zh_title: "Shu Xi Ling Hun Jing Gao",
    zh_content: "Shu xi ling hun shi e mo shi ti, ta men wei zhuang cheng yi shi de qin ren huo shan liang de shen ling dao shi. Sheng jing ming que jing gao fan dui xun qiu yu si zhe gou tong (Shen ming ji 18:10-12). Zhe xie qi pian xing de ling hun li yong wo men de tong ku he hao qi xin, yin dao wo men yuan li Ji du de zhen li. Zuo wei xin tu, wo men bi xu you shu ling fen bian li, ju jue ren he wei zhe xie qi pian da kai men hu de zuo fa, er shi yi kao Sheng Ling de yin dao he Shen de Hua Yu."
});

MATCH (t:THOUGHT {name: "thought.FAMILIAR SPIRITS WARNING"})
MATCH (c:CONTENT {name: "content.FAMILIAR SPIRITS WARNING"})
MERGE (t)-[:HAS_CONTENT { "name": "edge.FAMILIAR SPIRITS WARNING" }]->(c);

MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:THOUGHT {name: "thought.FAMILIAR SPIRITS WARNING"})
MERGE (parent)-[:HAS_THOUGHT { "name": "EVIL->FAMILIAR SPIRITS WARNING" }]->(child);
```
