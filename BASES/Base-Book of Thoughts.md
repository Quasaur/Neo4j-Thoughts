```base
view: View-Thoughts
folder: Book_of_Thoughts/
columns:
views:
  - type: table
    name: Book of Thoughts
    filters:
      and:
        - file.folder == "Book_of_Tweets/cypher"
    order:
      - file.name
      - name
      - insert
      - level
      - ptopic
      - parent
      - en_content
    sort:
      - property: name
        direction: ASC
    columnSize:
      file.name: 285
      note.name: 372
      note.ptopic: 153
      note.parent: 243
