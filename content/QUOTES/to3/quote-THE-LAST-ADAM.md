---
type: QUOTE
name: "quote.THE_LAST_ADAM"
alias: "Quote: Quote: THE LAST ADAM"
parent: "topic.HUMANITY"
en_content: "Jesus is the most powerful human in the universe! And having in His Body exalted humanity beyond the reach of sin and affliction, He became the Last Adam of a new race of humanity, and has poured out His Divine Holy Spirit upon all who in faith call upon Him.",
 es_title: "Cita: EL ÚLTIMO ADÁN",
 es_content: "¡Jesús es el ser humano más poderoso del universo! Y habiendo exaltado en Su Cuerpo a la humanidad más allá del alcance del pecado y de la aflicción, se convirtió en el Último Adán de una nueva raza de humanidad, y ha derramado Su Divino Espíritu Santo sobre todos los que con fe lo invocan.",
 fr_title: "Citation : LE DERNIER ADAM",
 fr_content: "Jésus est l'humain le plus puissant de l'univers ! Et ayant dans son corps exalté l’humanité au-delà de la portée du péché et de l’affliction, il est devenu le dernier Adam d’une nouvelle race humaine et a répandu son divin Saint-Esprit sur tous ceux qui, avec foi, l’invoquent.",
 hi_title: "उद्धरण: अंतिम एडम",
 hi_content: "यीशु ब्रह्मांड में सबसे शक्तिशाली इंसान हैं! और अपने शरीर में मानवता को पाप और पीड़ा की पहुंच से परे ऊंचा करके, वह मानवता की एक नई जाति का अंतिम आदम बन गया, और उसने उन सभी पर अपनी दिव्य पवित्र आत्मा उंडेली जो विश्वास में उसे बुलाते हैं।",
 zh_title: "yǐn yòng ： zuì hòu de yà dāng",
 zh_content: "yē sū shì yǔ zhòu zhōng zuì qiáng dà de rén ！ tā zài zì jǐ de shēn tǐ zhōng jiàng rén lèi tí shēng dào le chāo yuè zuì è hé kǔ nàn de chéng dù ， chéng wéi rén lèi xīn zhǒng zú de mò hòu yà dāng ， bìng jiāng shén shèng de shèng líng qīng dǎo zài suǒ yǒu píng zhe xìn xīn hū qiú tā de rén shēn shàng 。"
tags: ["jesus_christ", "lastadam", "humanity", "exalted", "holy_spirit"]
ptopic: "[[topic-HUMANITY]]"
level: 3
neo4j: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.THE_LAST_ADAM",
    alias: "Quote: Quote: THE LAST ADAM",
    parent: "topic.HUMANITY",
    tags: ["jesus_christ", "lastadam", "humanity", "exalted", "holy_spirit"],
    source: "'The Traveler's Oasis, Book Three'",
    booklink: "(https://www.amazon.com/Travelers-Oasis-Book-Three-ebook/dp/B00YRKX8E4)",
    level: 3
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.THE_LAST_ADAM",
    ctype: "QUOTE",
    en_title: "Quote: THE LAST ADAM",
    en_content: "Jesus is the most powerful human in the universe! And having in His Body exalted humanity beyond the reach of sin and affliction, He became the Last Adam of a new race of humanity, and has poured out His Divine Holy Spirit upon all who in faith call upon Him.",
 es_title: "Cita: EL ÚLTIMO ADÁN",
 es_content: "¡Jesús es el ser humano más poderoso del universo! Y habiendo exaltado en Su Cuerpo a la humanidad más allá del alcance del pecado y de la aflicción, se convirtió en el Último Adán de una nueva raza de humanidad, y ha derramado Su Divino Espíritu Santo sobre todos los que con fe lo invocan.",
 fr_title: "Citation : LE DERNIER ADAM",
 fr_content: "Jésus est l'humain le plus puissant de l'univers ! Et ayant dans son corps exalté l’humanité au-delà de la portée du péché et de l’affliction, il est devenu le dernier Adam d’une nouvelle race humaine et a répandu son divin Saint-Esprit sur tous ceux qui, avec foi, l’invoquent.",
 hi_title: "उद्धरण: अंतिम एडम",
 hi_content: "यीशु ब्रह्मांड में सबसे शक्तिशाली इंसान हैं! और अपने शरीर में मानवता को पाप और पीड़ा की पहुंच से परे ऊंचा करके, वह मानवता की एक नई जाति का अंतिम आदम बन गया, और उसने उन सभी पर अपनी दिव्य पवित्र आत्मा उंडेली जो विश्वास में उसे बुलाते हैं।",
 zh_title: "yǐn yòng ： zuì hòu de yà dāng",
 zh_content: "yē sū shì yǔ zhòu zhōng zuì qiáng dà de rén ！ tā zài zì jǐ de shēn tǐ zhōng jiàng rén lèi tí shēng dào le chāo yuè zuì è hé kǔ nàn de chéng dù ， chéng wéi rén lèi xīn zhǒng zú de mò hòu yà dāng ， bìng jiāng shén shèng de shèng líng qīng dǎo zài suǒ yǒu píng zhe xìn xīn hū qiú tā de rén shēn shàng 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.THE_LAST_ADAM"})
MATCH (c:CONTENT {name: "content.THE_LAST_ADAM"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.THE_LAST_ADAM"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.HUMANITY"})
MATCH (child:QUOTE {name: "quote.THE_LAST_ADAM"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.HUMANITY->THE_LAST_ADAM"}]->(child);

```
