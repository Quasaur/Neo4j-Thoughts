In Neo4j does an node's Primary ID have to start with a letter? Please provide examples, including backticks.

Let's clarify the concept of a "Primary ID" in Neo4j and how it relates to naming conventions and data values.
In Neo4j, there are two main "IDs" to consider for a node:
 * Neo4j's Internal ID (id() or elementId()):
   * Every node (and relationship) automatically gets a unique internal ID assigned by Neo4j.
   * This is always a numerical value (an integer). It never starts with a letter.
   * Example: MATCH (n:Person) RETURN id(n) might return 0, 1, 2, 100, etc.
   * Crucially, you should never use this internal ID as your primary key for application logic. These IDs can be reused, change during database operations (like import/export), and are not stable across different Neo4j instances or even major version upgrades.
 * User-Defined "Primary ID" (A Property on the Node):
   * This is the common understanding of a "primary ID" in Neo4j. It's a property that you define on your nodes to uniquely identify them within your domain.
   * You enforce uniqueness on this property by creating a unique constraint.
   * For these user-defined "Primary IDs," there are two aspects to consider:
     * The Property Name: The name you give to this property (e.g., userId, customerID, isbn).
     * The Property Value: The actual data stored in that property (e.g., 'alice123', 'CUST-001', 978-3-16-148410-0).
Let's break down the rules for each:
1. Rules for the Property Name of your User-Defined "Primary ID"
Cypher has naming rules for identifiers (like property names).
 * Standard Naming: Property names should ideally start with a letter (a-z, A-Z). They can then contain letters, numbers, and underscores (_).
   * Example:
     CREATE CONSTRAINT FOR (p:Product) REQUIRE p.productCode IS UNIQUE;
CREATE (p:Product {productCode: 'PROD-A001', name: 'Laptop'});

     Here, productCode is the property name, and it starts with a letter.
 * Using Backticks (`): If you need to use a property name that doesn't follow the standard naming rules (e.g., it starts with a number, contains spaces, or other special characters), you must enclose the property name in backticks.
   * Example 1 (Property Name Starting with a Number):
     CREATE CONSTRAINT FOR (c:Customer) REQUIRE c.`1st_id` IS UNIQUE;
CREATE (c:Customer {`1st_id`: 'CUST-XYZ', name: 'Jane Doe'});

     Here, `1st_id` is the property name, and it starts with a number, so backticks are required.
   * Example 2 (Property Name with Spaces):
     CREATE CONSTRAINT FOR (b:Book) REQUIRE b.`ISBN Number` IS UNIQUE;
CREATE (b:Book {`ISBN Number`: '978-0321765723', title: 'The Martian'});

     Here, `ISBN Number` is the property name, and it contains a space, so backticks are required.
2. Rules for the Property Value of your User-Defined "Primary ID"
The value stored in your "primary ID" property has no such restriction on starting with a letter. It can be a string that starts with a number, a number itself, or any other valid Cypher data type.
 * Example (String Value Starting with a Number):
   CREATE CONSTRAINT FOR (e:Employee) REQUIRE e.employeeId IS UNIQUE;
CREATE (e:Employee {employeeId: '789ABC', firstName: 'John'}); // Value starts with a number

   Here, employeeId is the property name (starts with a letter), but its value '789ABC' starts with a number. This is perfectly valid.
 * Example (Integer Value):
   CREATE CONSTRAINT FOR (o:Order) REQUIRE o.orderNumber IS UNIQUE;
CREATE (o:Order {orderNumber: 1001, status: 'Pending'}); // Value is a number

   Here, orderNumber is the property name, and its value 1001 is an integer. This is also perfectly valid.
In summary:
 * Neo4j's internal node IDs are always numbers and never start with a letter. Don't use them as your primary keys.
 * For your user-defined "primary ID" properties:
   * The property name itself (e.g., myId) should ideally start with a letter unless you use backticks (e.g., `123id`).
   * The value of that property (e.g., 'ABC123', '123XYZ', 456) can start with anything (letters, numbers) or be any valid data type.
