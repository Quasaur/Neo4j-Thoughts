---
type: THOUGHT
name: "thought.SHOULD"
alias: "Thought: Should"
parent: "topic.MORALITY"
tags: ["law", "order", "discipline", "principle", "god"]
ptopic: "[[topic-MORALITY]]"
level: 3
neo4j: true
---

```Cypher
CREATE (t:THOUGHT {
    name: "thought.SHOULD",
    alias: "Thought: Should",
    parent: "topic.MORALITY",
    tags: ["law", "order", "discipline", "principle", "god"],
    level: 3
});

CREATE (c:CONTENT {
    name: "content.SHOULD",
    ctype: "THOUGHT",
    en_title: "Should",
 es_title: "DEBERÍA",
 fr_title: "DEVRAIT",
 hi_title: "चाहिए",
 zh_title: "yīng gāi",
    en_content: "",
 es_content: "La palabra \"debería\" prueba la Existencia de Dios... nos señala un Ideal que no estamos a la altura y nos da un Estándar por el cual debemos juzgarnos a nosotros mismos."debería\" prueba la Existencia de Dios... nos señala un Ideal que no estamos a la altura y nos da un Estándar por el cual debemos juzgarnos a nosotros mismos."debería\" prueba la Existencia de Dios... nos señala un Ideal que no estamos a la altura y nos da un Estándar por el cual debemos juzgarnos a nosotros mismos."debería\" prueba la Existencia de Dios... nos señala un Ideal que no estamos a la altura y nos da un Estándar por el cual debemos juzgarnos a nosotros mismos.",
 fr_content: "Le mot « devrait » prouve l’existence de Dieu… nous indique un idéal auquel nous ne sommes pas tout à fait à la hauteur et nous donne une norme par laquelle nous devons nous juger nous-mêmes.",
 hi_content: "शब्द \"चाहिए\" ईश्वर के अस्तित्व को सिद्ध करता है... हमें एक ऐसे आदर्श की ओर इंगित करता है जिस पर हम खरे नहीं उतरते हैं और हमें एक मानक देता है जिसके द्वारा हमें स्वयं का मूल्यांकन करना चाहिए।"चाहिए\" ईश्वर के अस्तित्व को सिद्ध करता है... हमें एक ऐसे आदर्श की ओर इंगित करता है जिस पर हम खरे नहीं उतरते हैं और हमें एक मानक देता है जिसके द्वारा हमें स्वयं का मूल्यांकन करना चाहिए।"चाहिए\" ईश्वर के अस्तित्व को सिद्ध करता है... हमें एक ऐसे आदर्श की ओर इंगित करता है जिस पर हम खरे नहीं उतरते हैं और हमें एक मानक देता है जिसके द्वारा हमें स्वयं का मूल्यांकन करना चाहिए।"चाहिए\" ईश्वर के अस्तित्व को सिद्ध करता है... हमें एक ऐसे आदर्श की ओर इंगित करता है जिस पर हम खरे नहीं उतरते हैं और हमें एक मानक देता है जिसके द्वारा हमें स्वयं का मूल्यांकन करना चाहिए।",
 zh_content: "“ yīng gāi ” zhè ge cí zhèng míng liǎo shàng dì de cún zài …… xiàng wǒ men zhǐ chū le yí gè wǒ men wú fǎ wán quán dá dào de lǐ xiǎng ， bìng gěi le wǒ men yí gè wǒ men bì xū yòng lái pàn duàn zì jǐ de biāo zhǔn 。"चाहिए\" ईश्वर के अस्तित्व को सिद्ध करता है... हमें एक ऐसे आदर्श की ओर इंगित करता है जिस पर हम खरे नहीं उतरते हैं और हमें एक मानक देता है जिसके द्वारा हमें स्वयं का मूल्यांकन करना चाहिए।"debería\" prueba la Existencia de Dios... nos señala un Ideal que no estamos a la altura y nos da un Estándar por el cual debemos juzgarnos a nosotros mismos."
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SHOULD" AND c.name = "content.SHOULD"
MERGE (t)-[:HAS_CONTENT {name: "t.edge.SHOULD"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.MORALITY" AND child.name = "thought.SHOULD"
MERGE (parent)-[:HAS_THOUGHT {name: "t.edge.MORALITY->SHOULD"}]->(child);
```