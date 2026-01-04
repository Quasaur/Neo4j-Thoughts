---
title: "Table: Thoughts - File"
draft: true
type: hiddentable
---
# Table: THOUGHTS - File (hidden)
```dataview
TABLE WITHOUT ID
	file.link AS "File*",
	level AS "Level",
	ptopic AS "Topic",
	ptopic.level AS "Topic Level"
   FROM "content/THOUGHTS"
   SORT file.link ASC
```


## Dataview
parent:: [[content/index]]

## Snippets

```dataview
 WHERE type != THOUGHT

tags AS "Social Tags"
```