Show me an example of nested properties in a Neo4j Cypher CREATE statement.

Certainly! Here's an example of a Neo4j Cypher `CREATE` statement that demonstrates nested properties. In this example, we'll create a `Person` node with nested properties for contact information and address details.

```Cypher
CREATE (p:Person {
    name: "John Doe",
    age: 30,
    contactInfo: {
        email: "john.doe@example.com",
        phone: {
            home: "123-456-7890",
            mobile: "987-654-3210"
        }
    },
    address: {
        street: "123 Elm Street",
        city: "Springfield",
        state: "IL",
        postalCode: "62701"
    }
})
```

### Breakdown of the Example:
- The `Person` node has a `name` and `age` property.
- The `contactInfo` property is an object containing `email` and another nested object `phone`.
- The `phone` object has `home` and `mobile` properties.
- The `address` property contains another nested object with `street`, `city`, `state`, and `postalCode`.

This structure allows you to store complex data in a single node, making it easy to access related information.