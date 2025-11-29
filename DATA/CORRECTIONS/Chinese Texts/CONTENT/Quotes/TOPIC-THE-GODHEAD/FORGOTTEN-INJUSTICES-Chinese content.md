```Cypher
MATCH (c:CONTENT {en_title: "FORGOTTEN INJUSTICES"})
SET c.zh_title = 'Bèi yíwàng de bùgōng'
SET c.zh_content = "'rénlèi duì zìjǐ fàn xià de suǒyǒu zuì yánzhòng de bùgōng, zài shénshèng shànliáng de miànqián dōu bù huì bèi jì qǐ.";
```