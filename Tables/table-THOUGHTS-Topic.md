---
title: "Table: Thoughts - Topic"
draft: true
type: hiddentable
---
# Table: Thoughts - Topic (hidden)
```dataview
TABLE
	level AS "Level",
	ptopic AS "Topic*",
	ptopic.level AS "Topic Level"
   FROM "content/THOUGHTS"
   SORT ptopic ASC
```


## Dataview
parent:: [[content/index|index]]

## Snippets

```dataview
 WHERE type != THOUGHT

tags AS "Social Tags"
```