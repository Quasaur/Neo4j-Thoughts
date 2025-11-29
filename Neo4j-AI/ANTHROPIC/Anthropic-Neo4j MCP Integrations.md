i know that Antropic has integrations; is there an integration for/with Neo4j's AuraDB ([https://console-preview.neo4j.io/)?](https://console-preview.neo4j.io/\)?)

I don't have specific information about Anthropic's current integrations with Neo4j AuraDB in my knowledge base. Since integrations and partnerships can change frequently, I'd recommend checking a few sources for the most up-to-date information:Great! I found some excellent information. There is indeed a Neo4j integration with Anthropic's Claude through the Model Context Protocol (MCP). Let me get more details about this integration:Yes! There are several excellent integrations between Anthropic's Claude and Neo4j AuraDB through the **Model Context Protocol (MCP)**. Here's what's available:

## **Direct Neo4j-Claude Integrations via MCP**

Anthropic published the Model Context Protocol (MCP) in November 2024 to enable LLMs like Claude to communicate with external data sources, and Neo4j has developed several MCP servers specifically for this integration.

### **Available Neo4j MCP Servers:**

1. **mcp-neo4j-cypher** - Allows extracting the graph database schema so Claude can generate Cypher queries to query and update the database
    
    - Tools: `get-neo4j-schema`, `read-neo4j-cypher`, `write-neo4j-cypher`
2. **mcp-neo4j-memory** - Stores and updates entities with observations and relationships between them in Neo4j and can search and retrieve subgraphs of relevance
    
3. **mcp-neo4j-aura-manager** - Provides access to the Neo4j Aura API for managing databases, tenants, projects
    

### **How It Works:**

Claude can fetch data from Neo4j to render visualizations, charts, and answer questions using the database schema to figure out where and how data is stored. The MCP allows Claude to use tools during extended thinking, alternating between reasoning and tool use to improve responses.

### **Setup Example:**

You can configure Claude Desktop to connect to a Neo4j database by adding this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "movies-neo4j": {
      "command": "uvx",
      "args": [
        "mcp-neo4j-cypher",
        "--db-url", "neo4j+s://your-instance.databases.neo4j.io",
        "--user", "your-username",
        "--password", "your-password"
      ]
    }
  }
}
```

### **Latest Development:**

Anthropic recently announced "Integrations" which expands MCP support beyond local servers to remote MCP servers across the web and desktop apps, and developers can create their own Integrations in as little as 30 minutes.

For the most current information about these integrations and setup instructions, I'd recommend checking:

1. **Neo4j's MCP documentation**: https://neo4j.com/developer/genai-ecosystem/model-context-protocol-mcp/
2. **Neo4j MCP GitHub repository**: https://github.com/neo4j-contrib/mcp-neo4j
3. **Anthropic's MCP documentation**: https://modelcontextprotocol.io/

This integration allows you to leverage Claude's conversational AI with the full power of Neo4j's graph database capabilities, making it much easier than building a custom adapter like the Wix example I provided earlier!