```base
view: View-Thoughts
folder: content/THOUGHTS
columns:
views:
  - type: table
    name: Table
    filters:
      and:
        - type == "THOUGHT"
    groupBy:
      property: level
      direction: ASC
    order:
      - file.name
      - type
      - level
      - ptopic
      - file.folder
      - neo4j
    sort:
      - property: level
        direction: ASC
      - property: neo4j
        direction: ASC
    columnSize:
      file.name: 285
      note.type: 164
      note.ptopic: 363
      file.folder: 265
