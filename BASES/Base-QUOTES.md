```base
view: View-Quotes
folder: content/QUOTES
columns:
views:
  - type: table
    name: Table
    filters:
      and:
        - type == "QUOTE"
    order:
      - file.name
      - file.folder
      - neo4j
      - type
    sort:
      - property: file.folder
        direction: ASC
    columnSize:
      file.name: 285
      file.folder: 265
