---
title: "Table: Thoughts - Level"
draft: true
type: hiddentable
---
# Table: THOUGHTS - Level (hidden)
```dataview
TABLE
	level AS "Level*",
	ptopic AS "Topic",
	ptopic.level AS "Topic Level"
   FROM "content/THOUGHTS"
   SORT level ASC, file.link ASC
```


## Dataview
parent:: [[content/index]]

## Snippets

```dataview
 WHERE type != THOUGHT

tags AS "Social Tags"
```