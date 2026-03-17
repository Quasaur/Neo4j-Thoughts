# Prompts
## Prompt 1
dos/reports/neo4j_auradb_descripancies.md contains a report you produced for me yesterday; I need you to run the report again (comparing the Neo4j AuraDB online instance with the content folder in this repo). For this report i need you to review the content folder exclusively. you may access the python folder recursively for access to existing scripts used to access the Neo4j AuraDB instance, along with any python environment resources you require. You may edit the current report markdown file with the new results.

## Prompt 2
docs/Naming/naming_01_file_names.md is finished; check all node markdown file names in both the content and Book_of_Tweets folder against that markdown file and make any necessary corrections in the file names. When you're done place the report in the docs/reports/filename_[corrections_27-Feb-2026@1505.md](mailto:corrections_27-Feb-2026@1505.md) and report to me.

## Prompt 3
In the document docs/reports/edge_case_issues.md i have added responses to the remaining edge case issues. Search the content folder recursively for every markdown file that contains a Cypher block. Audit and make corrections in every qualified file based on the material in the docs/Naming folder. Make a report of discrepancies found and how they were corrected, along a list of discrepancies that could not be corrected, and add them to a markdown file in the docs/reports folder; Make sure the file name containing the report includes a date & time stamp.

## Prompt 4
Compare the content folder (recursively) against the documents in the docs/Naming folder and identify discrepan
cies or violatiions of the standards established in the docs/Naming folder, and document those discrepancies in a
new markdown document in the docs/reports folder, including the file creation timestampt in its file name.

## Prompt 5
Compare the content/QUOTES folder against the documents in the docs/Naming folder and identify any errors, discrepancies or violations of the standards established by the markdown files in the docs/Naming folder, and document those discrepancies in a
new markdown document in the docs/reports folder, including the file creation timestamp in its file name.

## Prompt 6
The markdown files in the content/QUOTES folder are considered source of truth. Connect to the Neo4j AuraDB online instance and compare all of the QUOTE nodes and their connected CONTENT nodes against the Cypher blocks in the markdown files of the content/QUOTES folder and refactor or replace any AuraDB QUOTE node property or the QUOTE node's connected CONTENT node properties with those in the Cypher blocks of the markdown files in the content/QUOTES folder.

## Prompt 7
Whatever nodes that exist in the content/QUOTES folder that are missing in the AuraDB online instance you must upload to the AuraDB. When all is done, there should be 80 QUOTE nodes in the AuraDB; any QUOTE nodes in the AuraDB that do not exist in the content/QUOTES folder you must delete along with their relationships and child nodes.

## Prompt 8
Review the contents of the content/PASSAGES folder. I have discovered a more efficient set of queries for the PASSAGE node type Cypher block: the three markdown files which contain the YAML property "verified" with a value of "true" are the three examples of the new Cypher query format; refactor all other markdown files in the content/PASSAGES folder (recursively) to use the new query. Be sure not to alter any property values!

## Prompt 9
Compare the number of PASSAGE markdown files in the ANALYSIS/PASSAGES-2 folder (recursively) against those in the content/PASSAGES folder (recursively) and give me a count of each.

## Prompt 9a
Move all markdown files that are in the content/PASSAGES folder (recursively) and move them to the content/PASSAGES folder itself, then delete all of the empty sub-folders under content/PASSAGES.

## Prompt 9b
Check the markdown files in content/PASSAGES recursively against the markdown files in docs/Naming for consistency and give me a report; dd not change the contents of any markdown file!!!!!

## Prompt 10
The markdown files in the content/PASSAGES folder are considered source of truth. 

Connect to the Neo4j AuraDB online instance and compare all of the PASSAGE nodes and their connected CONTENT nodes in the AuraDB instance against the Cypher blocks in the markdown files of the content/PASSAGES folder and refactor or replace any AuraDB QUOTE node property or the PASSAGE node's connected CONTENT node properties with those in the Cypher blocks of the markdown files in the content/PASSAGE folder.

Whatever nodes that exist in the content/PASSAGES folder that are missing in the AuraDB online instance you must upload to the AuraDB. When all is done, there should be 28 PASSAGE nodes in the AuraDB; any QUOTE nodes in the AuraDB that do not exist in the content/QUOTES folder you must delete along with their relationships and child nodes.

## Prompt 11
This prompt contains instructions regarding the contents of the content/THOUGHTS folder. I have discovered a more efficient set of queries for the THOUGHT node type Cypher block: the markdown file at content/THOUGHTS/thought-BETTER-WORLD.md is the example of the new Cypher query format; refactor the Cypher blocks of all other markdown files in the content/THOUGHTS folder to use the new query format. Be sure not to alter any property values in the Cypher blocks!

## Prompt 12
Create the docs/reports/thoughts_uploaded.md markdown file. 

As i give you files in the content/THOUGHTS folder with the YAML property "verified: true" to use in the refactoring and replacing of THOUGHT nodes in the Neo4j AuraDB online instance, add the names of those files to the docs/reports/thoughts_uploaded.md file. 

Starting now, i'm ordering you to connect to the Neo4j AuraDB online instance and compare the first batch of files in the content/THOUGHTS folder with the YAML property "verified: true" against the corresponding THOUGHT nodes in the AuraDB and refactor or replace their properties. 

If for some reason there is a THOUGHT in content/THOUGHTS with the YAML property "verified: true" that does not exist in the AuraDB, you are ordered to use the Cypher block of that file to insert the THOUGHT node, its CONTENT node as well as its parent relationship into the AuraDB. 

If for some reason the required parent TOPIC of the THOUGHT does not exist in the AuraDB, find the parent TOPIC in the content/TOPICS folder, insert the parent TOPIC using its Cypher block, and then proceed with the THOUGHT insertion.

Commands to run THOUGHT refactor process:
```zsh
 cd /Users/quasaur/Developer/Neo4j-Thoughts
  source .venv/bin/activate
  python3 python/AuraDB/sync_verified_thoughts.py
```

## Python 13
Take the markdown file /Book_of_Tweets/BIBLE/passage-END-OF-ALL-FLESH.md and compare its contents against the Neo4j AuraDB online instance.

If the PASSAGE node contained in the aforementioned markdown file exists in the AuraDB instance, refactor the AuraDB PASSAGE node to match the nodes & properties in the Cypher block of the aforementioned markdown file.

If the PASSAGE node doesn't exist in the AuraDB run the aforementioned node's Cypher block queries to add the node to the AuraDB.

When the aforementioned markdown file's contents are completely synced against the AuraDB, move the aforementioned markdown file to the content/PASSAGES folder.



