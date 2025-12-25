```Cypher
MATCH ()-[r:RELATIONSHIP_TYPE {property_name: 'value'}]->() DELETE r ;
```

Apply to the first edge labeled "HAS_DESCRIPTION":

```Cypher
MATCH ()-[r:HAS_DESCRIPTION {property_name: 'value'}]->() DELETE r 
```