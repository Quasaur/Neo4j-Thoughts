---
type: agent
typeDesc: Instructions for artificial intelligence LLMs, agents and models.
creation: 02-Mar-2026@2005
title: Part 1 - Neo4j CYPHER Language Specifications
version: 1
series: "Neo4j-Thoughts: Naming Conventions"
docStatus: COMPLETE
---
# Neo4j Property Name Specs
## CYPHER: Node Property Names
### Q:
According to Neo4j & its CYPHER language specs, what are the rules for node property names?

### A:
In Neo4j, property names (also known as keys) follow specific lexical rules defined by the Cypher query language. Think of them like variable names in most programming languages: they are case-sensitive and generally prefer alphanumeric characters.

#### Naming Conventions (The "Standard" Way)

To keep your queries clean and readable without extra punctuation, you should follow the rules for unquoted identifiers:

 * **Characters:** Must begin with an alphabetic character (A–Z, a–z) or an underscore (_). Subsequent characters can include numbers.

 * **Case Sensitivity:** Property names are case-sensitive. firstName, firstname, and FirstName are treated as three distinct properties.

 * **Recommendation:** The industry standard for Neo4j property names is camelCase (e.g., dateOfBirth), while labels usually use PascalCase (e.g., :Person).

#### Using Escaped Names (The "Anything Goes" Way)

If you need to use spaces, special characters, or reserved keywords as a property name, you must wrap the name in backticks (`).

 * Example: MATCH (n) RETURN n.`First Name`

 * Allowed: With backticks, you can use almost any Unicode character, including emojis or names starting with numbers.

 * Reserved Keywords: If you want to use a Cypher keyword (like MATCH or CREATE) as a property name, backticks are mandatory to prevent syntax errors.

#### Prohibited & Restricted Names

While Cypher is flexible, there are a few hard boundaries to keep in mind:

 * **Leading Underscores:** While technically allowed, Neo4j often uses internal properties starting with underscores (like _id in some contexts). It’s best to avoid these to prevent future conflicts.

 * **Null Values:** You cannot have a property with a null value. In Neo4j, "setting a property to null" is semantically equivalent to deleting the property from that specific node.

 * **Empty Strings:** You can use an empty string as a property name if you escape it (` `), but this is considered extremely poor practice and makes debugging a nightmare.

## CYPHER: Arrays
### Q:
I know the Cypher query language supports arrays; give me an example of a "tags" property which consist of an array of five keywords...at least one of which contains two words separated by an underscore and at least one of which consists of three words separated by two undersocres.

### A:
In Cypher, arrays (officially called **Lists**) are defined using square brackets `[]`. They are ordered collections, and in the case of node properties, they must contain elements of the same basic type (e.g., all strings).

Here is an example of a `Person` node where the `tags` property contains five keywords following your specific formatting requirements:
```cypher
CREATE (p:Person {
  name: "Alex",
  tags: [
    "developer",
    "neo4j_expert",
    "graph_database_fan",
    "remote_work",
    "open_source"
  ]
})
RETURN p
```

#### Breakdown of the Array

In this example, the `tags` property satisfies your criteria:
- **Two words, one underscore:** `neo4j_expert` and `open_source`.
- **Three words, two underscores:** `graph_database_fan`.
- **Total count:** 5 string elements.

#### Important Rules for Property Arrays

If you're planning to work with these lists extensively, keep these Neo4j-specific behaviors in mind:
- **Homogeneity:** Unlike general Cypher lists used in memory, **property** arrays stored on a node must be homogeneous (you can't mix strings and integers in the same array on a node).
- **No Nested Arrays:** You cannot store an array inside another array as a node property (e.g., `[[1,2], [3,4]]` is invalid for storage).
- **Querying:** To find nodes containing a specific tag within that array, you use the `IN` operator:
    ```cypher
    MATCH (p:Person)
    WHERE "neo4j_expert" IN p.tags
    RETURN p.name
    ```
    
## CYPHER: Integers
### Q:
If a CYPHER property value is an integer, must it be enclosed in backticks, single quotes or double quotes?
### A:
The short answer is: **None of the above.**

In Cypher, if you enclose a number in quotes or backticks, you change its **data type**, which can lead to unexpected results during math operations or sorting.

#### The Rule for Integers

Integers should be written as **plain literals** without any surrounding characters.

- **Correct (Integer):** `SET n.age = 25`
    
- **Incorrect (String):** `SET n.age = "25"` — This stores the text characters "2" and "5", not the mathematical value.
    
- **Incorrect (Identifier):** `SET n.age =` `25` — This tells Neo4j to look for a property or variable _named_ "25", which will likely cause an error.
    
#### Comparison of Syntax

To keep your data types clean, here is how Cypher distinguishes between them:

|**Data Type**|**Syntax Example**|**When to use**|
|---|---|---|
|**Integer**|`42`|For ages, counts, timestamps, or IDs.|
|**String**|`"42"` or `'42'`|For names, descriptions, or codes (like Zip Codes).|
|**Identifier**|`` `42` ``|Only if you (bravely) named a property "42".|

---

#### Why it matters: Type Safety

Neo4j is a "schemaless-friendly" database, but it is strict about types. If you store an age as a string `"25"`, the following query will **fail** or return no results because you cannot perform greater-than comparisons on strings and integers simultaneously:

```
// This works only if 'age' is a raw integer
MATCH (p:Person) 
WHERE p.age > 21 
RETURN p.name
```

If you accidentally stored them as strings, you would have to use the `toInteger()` function to fix it on the fly, which is slower: `WHERE toInteger(p.age) > 21`.

## CYPHER: URLS
### Q:
Are there any special rules in the Neo4j CYPHER specs for properties with values that are web address URLs (i.e., https://www.amazon.com/Basics-More-Years-Sermons-ebook/dp/B00XLMBDR8)?

### A:
Technically, the Neo4j Cypher specification treats a URL exactly like any other **String**. There are no specialized "URL" data types or specific "web address" syntax rules, but because URLs contain special characters like `:`, `/`, `.`, and `?`, there are three practical rules you must follow to handle them correctly.

#### The Quote Rule
Since a URL is a String, it **must** be enclosed in either single quotes (`'`) or double quotes (`"`).

- **Correct:** `SET n.url = "https://www.amazon.com/..."`
- **Incorrect:** `SET n.url = https://www.amazon.com/...` (This will throw a syntax error because Cypher will try to interpret the `:` and `/` as operators or relationship markers).

**Pro Tip:** If your URL contains single quotes (rare but possible in query strings), use double quotes to wrap the whole thing, or vice-versa.

#### The Escaping Rule (Backslashes)
Cypher uses the backslash (`\`) as an escape character. If your URL contains a backslash (sometimes seen in tracking parameters or Windows-based file paths converted to URLs), you must double it: `\\`.

However, for standard web URLs like the Amazon link you provided, you generally don't need to escape the forward slashes (`/`).

#### Case Sensitivity in Comparisons
While domain names (like `amazon.com`) are case-insensitive in a web browser, **Cypher strings are case-sensitive**.

If you store `https://www.Amazon.com` and then search for `https://www.amazon.com`, Neo4j will **not** find a match.

**The Solution:** Use the `toLower()` function when querying if you aren't sure of the casing:

```cypher
MATCH (b:Book)
WHERE toLower(b.source_url) = "https://www.amazon.com/..."
RETURN b
```

### Comparison: URL vs. Standard String

|**Feature**|**Standard String**|**URL Property**|
|---|---|---|
|**Enclosure**|Required (`'` or `"`)|Required (`'` or `"`)|
|**Special Characters**|Allowed|Allowed (slashes, dots, etc.)|
|**Indexing**|Supported|Supported (highly recommended)|
|**Validation**|None by default|Use `WHERE n.url STARTS WITH "https://"`|



### Bonus: Searching with URLs

Since URLs are long and complex, using `STARTS WITH` or `CONTAINS` is often more efficient than matching the entire string, especially for Amazon links that have long "ref" tags at the end:

Cypher

```
MATCH (n:Product)
WHERE n.url CONTAINS "B00XLMBDR8" // Searching by the ASIN/ID within the URL
RETURN n
```

**Would you like me to write a Cypher query that extracts just the domain name (e.g., "amazon.com") from a list of URL properties?**


## CYPHER: Special Characters
Look at the following Cypher query:
```cypher
CREATE (t:THOUGHT {
	name: "thought.692, 189",
	alias: "Thought: 692, 189",
	parent: "topic.PSYCHOLOGY",
	tags: ["massshootings", "gunviolence", "guns", "church", "prayer"],
	level: 4
});
```
This query is **syntactically perfect!** You nailed the distinction between the property names (keys) and the string values (literals).

By using **double quotes** for the strings and keeping the **integer** as a raw number, Neo4j will execute this without any issues.

### Why this works:

- **Property Names:** `name`, `alias`, `parent`, `tags`, and `level` are all standard identifiers (no spaces or special characters), so they don't need backticks.
- **String Values:** Even though `name` contains a period, a space, and a comma (`"thought.692, 189"`), wrapping it in quotes tells Cypher to treat the entire thing as a single piece of text.
- **Arrays:** Your `tags` array is correctly formatted with square brackets and comma-separated strings.
- **Integers:** `level: 4` is a proper numerical value, which is great for future filtering (e.g., `WHERE t.level > 2`).
    
### A Small Optimization Tip

In Neo4j, if you find yourself frequently using the `parent` property to reference another node (like `topic.PSYCHOLOGY`), you might eventually want to transform that into a **Relationship**.

In a graph database, connecting two nodes with a line (edge) is much faster for querying than matching text strings. It would look like this:

Cypher

```
// Instead of a 'parent' property, you use a relationship:
MATCH (parent:TOPIC {name: "topic.PSYCHOLOGY"})
CREATE (t:THOUGHT {
    name: "thought.692, 189",
    alias: "Thought: 692, 189",
    tags: ["massshootings", "gunviolence", "guns", "church", "prayer"],
    level: 4
})
CREATE (t)-[:CHILD_OF]->(parent)
```

---

**Would you like me to explain how to write a "MERGE" query so you don't accidentally create duplicate nodes if you run this script twice?**
## Summary Table

| Feature | Unquoted (Standard) | Quoted (Backticks) |
|---|---|---|
| Starts with | Letter or Underscore | Any character |
| Contains | Letters, Numbers, _ | Any Unicode character |
| Case Sensitive | Yes | Yes 
| Example | user_age | `User Age` |

