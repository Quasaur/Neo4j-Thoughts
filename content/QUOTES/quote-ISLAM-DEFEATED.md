---
type: QUOTE
name: "quote.ISLAM DEFEATED"
alias: "Quote: Islam Defeated"
parent: "topic.RELIGION"
source: "Letters from God: A Work of Fiction"
en_content: "Biblical Christianity will defeat Islam by the same means it defeated paganism: through the Truth of the Holy Bible, the Love of Jesus Christ, and the Life of Christ lived through His followers."
tags: ["islam", "christianity", "biblical", "bible", "jesus_christ"]
ptopic: "[[topic-RELIGION]]"
level: 4
neo4j: true
verified: true
---

```Cypher
// CREATE QUOTE
CREATE (q:QUOTE {
    name: "quote.ISLAM DEFEATED",
    alias: "Quote: Islam Defeated",
    parent: "topic.RELIGION",
    tags: ["islam", "christianity", "biblical", "bible", "jesus_christ"],
    source: "Letters from God: A Work of Fiction",
    booklink: "https://www.amazon.com/Letters-God-Fiction-Calvin-Mitchell-ebook/dp/B01M255OZX",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.ISLAM DEFEATED",
    ctype: "QUOTE",
    en_title: "Quote: Islam Defeated",
    en_content: "Biblical Christianity will defeat Islam by the same means it defeated paganism: through the Truth of the Holy Bible, the Love of Jesus Christ, and the Life of Christ lived through His followers.",
 es_title: "Cita: Islam derrotado",
 es_content: "El cristianismo bíblico derrotará al Islam por los mismos medios que derrotó al paganismo: a través de la Verdad de la Santa Biblia, el Amor de Jesucristo y la Vida de Cristo vivida a través de Sus seguidores.",
 fr_title: "Citation : L'Islam vaincu",
 fr_content: "Le christianisme biblique vaincra l’islam de la même manière qu’il a vaincu le paganisme : par la vérité de la Sainte Bible, l’amour de Jésus-Christ et la vie du Christ vécue à travers ses disciples.",
 hi_title: "उद्धरण: इस्लाम हार गया",
 hi_content: "बाइबिल आधारित ईसाइयत इस्लाम को उसी तरीके से हरा देगी, जिस तरह से उसने बुतपरस्ती को हराया था: पवित्र बाइबिल की सच्चाई, यीशु मसीह के प्रेम और उनके अनुयायियों के माध्यम से जीए गए मसीह के जीवन के माध्यम से।",
 zh_title: "yǐn yòng ：yī sī lán bèi jī bài",
 zh_content: "fú hé shèng jīng de jī dū jiào jiāng yǐ jī bài yì jiào de tóng yàng fāng shì jī bài yī sī lán jiào ： tōng guò shèng jīng de zhēn lǐ 、 yē sū jī dū de ài yǐ jí jī dū de zhuī suí zhě suǒ jīng lì de shēng huó 。"
});

// LINK CONTENT
MATCH (q:QUOTE {name: "quote.ISLAM DEFEATED"})
MATCH (c:CONTENT {name: "content.ISLAM DEFEATED"})
MERGE (q)-[:HAS_CONTENT {name: "q.edge.ISLAM DEFEATED"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.RELIGION"})
MATCH (child:QUOTE {name: "quote.ISLAM DEFEATED"})
MERGE (parent)-[:HAS_QUOTE {name: "q.edge.RELIGION->ISLAM DEFEATED"}]->(child);

```
