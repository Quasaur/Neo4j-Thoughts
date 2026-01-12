# Batch 1: Metadata Review (First 10 Tweets)

| Date ID | Title Suggestion | Suggested Topic | Parent Topic (if new) | Tags |
| :--- | :--- | :--- | :--- | :--- |
| 08-Apr-2010a | SUBMITTING OUR PLANS | topic.HUMILITY | - | ego, submission, plans, gods_plan, humility |
| 08-Apr-2010b | LIFE AS DREAM | topic.PHILOSOPHY | - | dream, reality, presence_god, awakening, consciousness |
| 13-Apr-2010 | BACH AND GENIUS | topic.MUSIC | topic.BEAUTY | bach, genius, music, gift, transcendence |
| 17-Apr-2010a | TRUE THEOLOGIAN | topic.SPIRITUALITY | - | theology, encounter, personal_relation, knowing_god, spirituality |
| 17-Apr-2010b | BROKEN RELATIONSHIP | topic.WORSHIP | - | obedience, submission, spirit_fruit, commitment, worship |
| 19-Apr-2010 | GIFT OR GIVER | topic.WORSHIP | - | gift, giver, priorities, gratitude, worship |
| 20-Apr-2010 | DIVINE CONSISTENCY | topic.THE-GODHEAD | - | divine_character, consistency, truth, divinity, godhead |
| 21-Apr-2010 | DIVINE WILL | topic.DIVINE-SOVEREIGNTY | - | sovereignty, gods_will, omnipotence, authority, providence |
| 22-Apr-2010a | SURVIVING JUDGMENT | topic.THE-GOSPEL | - | salvation, judgment, sinner, survival, gospel |
| 22-Apr-2010b | BUNYANS MASTERPIECE | topic.GRACE | - | john_bunyan, law, grace, literature, revelation |

---

## Sample File Content (Draft for 08-Apr-2010a)

```markdown
---
name: "thought.SUBMITTING OUR PLANS"
alias: "Thought: Ego and Submission"
type: THOUGHT
tags:
- ego
- submission
- plans
- gods plan
- humility
parent: topic.HUMILITY
level: 4
neo4j: true
ptopic: 
---
# Thought: SUBMITTING OUR PLANS
> [!Thought-en]
> Our egos are so massive...we're always trying to fit God into our plans rather than submitting ourselves to His Plan.

```Cypher
// Generated from Book6E-FINAL.md
CREATE (t:THOUGHT {
    name: "thought.SUBMITTING OUR PLANS",
    alias: "Thought: SUBMITTING OUR PLANS",
    parent: "topic.HUMILITY",
    tags: ["ego", "submission", "plans", "gods_plan", "humility"],
    notes: "",
    level: 4
});

CREATE (c:CONTENT {
    name: "content.SUBMITTING OUR PLANS",
    en_title: "SUBMITTING OUR PLANS",
    en_content: "Our egos are so massive...we're always trying to fit God into our plans rather than submitting ourselves to His Plan.",
    es_title: "SOMETIENDO NUESTROS PLANES",
    es_content: "Nuestros egos son tan masivos... siempre estamos tratando de encajar a Dios en nuestros planes en lugar de someternos a Su Plan.",
    fr_title: "SOUMETTRE NOS PLANS",
    fr_content: "Nos egos sont si massifs... nous essayons toujours de faire entrer Dieu dans nos plans plutôt que de nous soumettre à Son Plan.",
    hi_title: "योजनाएं समर्पित करना",
    hi_content: "हमारे अहंकार इतने विशाल हैं... हम हमेशा भगवान को अपनी योजनाओं में फिट करने की कोशिश करते हैं बजाय इसके कि हम खुद को उनकी योजना के प्रति समर्पित कर दें।"
    zh_title: "fú cóng jì huà",
    zh_content: "wǒ men de zì wǒ shì rú cǐ bàng dà …… wǒ men zǒng shì shì tú ràng shàng dì fú hé wǒ men de jì huà ， ér bù shì ràng wǒ men zì jǐ fú cóng tā de jì huà 。"
});

MATCH (t:THOUGHT)
MATCH (c:CONTENT)
WHERE t.name = "thought.SUBMITTING OUR PLANS" AND c.name = "content.SUBMITTING OUR PLANS"
MERGE (t)-[:HAS_CONTENT {name: "edge.SUBMITTING OUR PLANS"}]->(c);

MATCH (parent:TOPIC)
MATCH (child:THOUGHT)
WHERE parent.name = "topic.HUMILITY" AND child.name = "thought.SUBMITTING OUR PLANS"
MERGE (parent)-[:HAS_THOUGHT {name: "edge.HUMILITY >SUBMITTING OUR PLANS"}]->(child);
```
```
