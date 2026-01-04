---
title: Topics-Level
draft: true
type: hiddentable
---
# Table: TOPICS (hidden)
```dataview
TABLE WITHOUT ID
   file.link AS "File*",
   level AS "Level",
   ptopic AS "Parent Topic",
ptopic.level AS "Parent Level"
   FROM "content/TOPICS"
   SORT level ASC
```


## Dataview
parent:: [[content/index|index]]