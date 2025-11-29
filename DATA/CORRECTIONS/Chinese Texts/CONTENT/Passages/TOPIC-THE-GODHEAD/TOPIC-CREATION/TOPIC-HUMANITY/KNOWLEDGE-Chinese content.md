```Cypher
MATCH (C:CONTENT {en_title: "KNOWLEDGE"})
SET c.zh_title = 'Zhīshì'
SET c.zh_content = "jìngwèi yēhéhuá shì zhīshì de kāiduān; yúwàng rén miǎoshì zhìhuì hé xùnhuì.";
```