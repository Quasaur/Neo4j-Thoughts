```Cypher
MATCH (n {en_title: "LOVE"})
SET n.zh_title = 'Ài'
SET n.zh_content = "yīn qīnshǔ guānxì huò gèrén guānxì ér duì tārén de qiángliè gǎnqíng; jīyú àimù hé wēnróu de xīyǐn; jīyú qīnpèi, réncí huò gòngtóng lìyì de gǎnqíng; gǎnqíng de bǎozhèng; rèliè de yīliàn, rèqíng huò zhōngchéng; yīliàn, zhōngchéng huò qīnpèi de duìxiàng.";
```