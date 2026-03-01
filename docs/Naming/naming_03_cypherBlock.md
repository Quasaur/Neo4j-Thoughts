---
type: agent
typeDesc: Instructions for aritificial intelligence LLMs, agents and models.
creation: 27-Feb-2026@0942
title: "Part 3 - Cypher Block Naming Conventions"
series: "Neo4j-Thoughts: Naming Conventions"
docStatus: COMPLETE
---
**# Part 3 - The Cypher Block**

**## Introduction**

This document defines the standard for what goes into the Cypher block of the markdown file for each node type.

  

The Cypher block consists of four queries; the first two queries are run together. After a brief pause the next two queries are run separately...one after the other.

  

The first query creates the primary node as one of the four types (TOPIC, THOUGHT, QUOTE or PASSAGE).

  

The second query creates the secondary node. The secondary node is defined as either the DESCRIPTION node (if the primary node is a TOPIC) or the CONTENT node (if the primary node is a THOUGHT, QUOTE or PASSAGE).

  

The third query creates the relationship between the primary and secondary nodes.

  

The fourth query creates the relationship between the primary node and its parent node. The Developer ensures that the primary node's parent node already exists in the AuraDB instance before the queries in the Cypher block are executed against the AuraDB.

  

The following rules define the values of the primary and secondary nodes as well as the properties of both the relationship between the primary and secondary nodes as well as the relationship between the primary node and its parent node.

  

## Primary Node

  

## Secondary Node

  

## First Relationship 

  

## Second Relationship