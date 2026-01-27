---
name: passage.PROTECTION_FROM_EVIL
alias: "Passage: PROTECTION FROM EVIL"
type: PASSAGE
parent: topic.EVIL
tags:
- wisdom
- knowledge
- discretion
- understanding
- rescue
neo4j: true
ptopic: "[[topic-EVIL]]"
level: 4
---
```Cypher
// CREATE PASSAGE
CREATE (b:PASSAGE {
    name: "passage.PROTECTION_FROM_EVIL",
    alias: "Passage: PROTECTION FROM EVIL",
    parent: "topic.EVIL",
    tags: ["wisdom", "knowledge", "discretion", "understanding", "rescue"],
    source: "'Proverbs 2:10-12'",
    sortedsource: "'Proverbs 02:10-12'",
    biblelink: "(https://www.biblegateway.com/passage/?search=proverbs+2%3A10-12&version=NASB)",
    level: 4
});

// CREATE CONTENT
CREATE (c:CONTENT {
    name: "content.PROTECTION_FROM_EVIL",
    en_title: "PROTECTION FROM EVIL",
    en_content: "For wisdom will enter your heart, And knowledge will be delightful to your soul; Discretion will watch over you, Understanding will guard you, To rescue you from the way of evil, From a person who speaks perverse things;",
 es_title: "PROTECCIÓN CONTRA EL MAL",
 es_content: "Porque la sabiduría entrará en tu corazón, y el conocimiento será delicia para tu alma; La discreción te guardará, el entendimiento te guardará, para librarte del camino del mal, del que habla cosas perversas;",
 fr_title: "PROTECTION CONTRE LE MAL",
 fr_content: "Car la sagesse entrera dans ton cœur, et la connaissance sera délicieuse à ton âme ; La discrétion veillera sur toi, L'intelligence te gardera, Pour te délivrer de la voie du mal, De celui qui dit des choses perverses ;",
 hi_title: "बुराई से सुरक्षा",
 hi_content: "क्योंकि बुद्धि तेरे हृदय में प्रवेश करेगी, और ज्ञान से तेरा मन प्रसन्न होगा; विवेक तेरी रक्षा करेगा, समझ तेरी रक्षा करेगी, और तुझे बुराई के मार्ग से बचाएगा, और टेढ़ी-मेढ़ी बातें बोलनेवाले से बचाएगा;",
 zh_title: "bǎo hù miǎn shòu xié è qīn hài",
 zh_content: "yīn wèi zhì huì jiāng jìn rù nǐ de nèi xīn ， zhī shí jiàng lìng nǐ de líng hún yú yuè ； míng biàn huì bǎo hù nǐ ， cōng míng huì bǎo hù nǐ ， jiù nǐ tuō lí è dào ， tuō lí shuō guāi huà de rén 。",
});

// LINK CONTENT
MATCH (b:PASSAGE {name: "passage.PROTECTION_FROM_EVIL"})
MATCH (c:CONTENT {name: "content.PROTECTION_FROM_EVIL"})
MERGE (b)-[:HAS_CONTENT {name: "b.edge.PROTECTION_FROM_EVIL"}]->(c);

// LINK PARENT
MATCH (parent:TOPIC {name: "topic.EVIL"})
MATCH (child:PASSAGE {name: "passage.PROTECTION_FROM_EVIL"})
MERGE (parent)-[:HAS_PASSAGE {name: "p.edge.b.EVIL->PROTECTION_FROM_EVIL"}]->(child);

```
