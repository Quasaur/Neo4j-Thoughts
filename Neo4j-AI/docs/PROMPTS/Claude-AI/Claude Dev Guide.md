# Claude 3.5 Development Guide for Django & React (TypeScript) with SuperClaude Configuration (CLAUDE.md)

This document outlines how to effectively leverage Claude 3.5, integrated with the SuperClaude configuration system, for full-stack web development using Django (Python) for the backend and React with TypeScript for the frontend.

SuperClaude provides a sophisticated AI assistant framework with specialized personas, MCP servers, and commands designed for evidence-based development, focusing on security, performance, and quality.

## 1. Core System Components & Configuration

The SuperClaude system relies on specific configuration files to define its behavior and capabilities:

- **`.claude/settings.local.json`**: Basic Claude permissions and local settings.
    
- **`.claude/shared/superclaude-core.yml`**: Core philosophy, standards, and workflows.
    
- **`.claude/shared/superclaude-mcp.yml`**: MCP server integration details.
    
- **`.claude/shared/superclaude-rules.yml`**: Development practices and rules.
    
- **`.claude/shared/superclaude-personas.yml`**: Definitions for 9 specialized personas.
    

## 2. Personas: When & Where to Use for Web Development

Personas allow Claude to adopt a specialized role, providing more targeted and expert assistance.

### Development Personas

- **`--persona-frontend`**:
    
    - **Focus**: UI/UX, accessibility, React/Vue components.
        
    - **When**: Building user interfaces, design systems, accessibility work in React/TypeScript.
        
    - **Use with**: `Magic MCP`, `Puppeteer testing`, `--magic` flag.
        
    - **Example Prompt**: "Using `--persona-frontend --magic`, build a responsive React `ProductGrid` component in TypeScript using Tailwind CSS. It should display `ProductCard` components."
        
- **`--persona-backend`**:
    
    - **Focus**: API design, scalability, reliability engineering.
        
    - **When**: Building Django REST APIs, database interactions, server architecture.
        
    - **Use with**: `Context7` for patterns, `--seq` for complex analysis.
        
    - **Example Prompt**: "With `--persona-backend --seq`, design a scalable Django REST API for user authentication, including registration, login, and token management."
        
- **`--persona-architect`**:
    
    - **Focus**: System design, scalability, long-term thinking.
        
    - **When**: Designing overall Django/React application architecture, making technology decisions, microservices.
        
    - **Use with**: `Sequential MCP`, `--ultrathink` for complex systems.
        
    - **Example Prompt**: "Using `--persona-architect --ultrathink`, propose a microservices architecture for an e-commerce platform using Django for services and React for the frontend, considering inter-service communication and data consistency."
        

### Quality Personas

- **`--persona-analyzer`**:
    
    - **Focus**: Root cause analysis, evidence-based investigation.
        
    - **When**: Debugging complex issues in Django views, React components, or API interactions.
        
    - **Use with**: `All MCPs` for comprehensive analysis.
        
    - **Example Prompt**: "With `--persona-analyzer --all-mcp`, investigate this traceback from my Django application: `[PASTE TRACEBACK]`. Provide the root cause and a solution."
        
- **`--persona-security`**:
    
    - **Focus**: Threat modeling, vulnerability assessment.
        
    - **When**: Security audits of Django APIs, React authentication flows, data handling.
        
    - **Use with**: `--scan --security`, `Sequential` for threat analysis.
        
    - **Example Prompt**: "Using `--persona-security --scan --owasp`, identify potential security vulnerabilities in this Django REST Framework view code: `[PASTE VIEW CODE]`."
        
- **`--persona-qa`**:
    
    - **Focus**: Testing, quality assurance, edge cases.
        
    - **When**: Writing unit/integration/E2E tests for Django models/views or React components.
        
    - **Use with**: `Puppeteer` for E2E testing, `--coverage` flag.
        
    - **Example Prompt**: "With `--persona-qa --pup`, generate Playwright (or Cypress) E2E tests for a React login form, covering valid login, invalid credentials, and forgotten password link."
        
- **`--persona-performance`**:
    
    - **Focus**: Optimization, profiling, bottlenecks.
        
    - **When**: Optimizing Django ORM queries, React rendering performance, API response times.
        
    - **Use with**: `Puppeteer metrics`, `--profile` flag.
        
    - **Example Prompt**: "Using `--persona-performance --profile`, analyze this Django ORM query `[PASTE QUERY]` and suggest optimizations for better performance on large datasets."
        

### Improvement Personas

- **`--persona-refactorer`**:
    
    - **Focus**: Code quality, technical debt, maintainability.
        
    - **When**: Refactoring monolithic Django views, large React components, or improving TypeScript type definitions.
        
    - **Use with**: `--improve --quality`, `Sequential` analysis.
        
    - **Example Prompt**: "With `--persona-refactorer --improve --quality`, refactor this large React component `[PASTE COMPONENT CODE]` into smaller, more manageable functional components with clear responsibilities and improved TypeScript typings."
        
- **`--persona-mentor`**:
    
    - **Focus**: Teaching, documentation, knowledge transfer.
        
    - **When**: Explaining complex Django concepts (e.g., custom middleware), React hooks, or TypeScript advanced types.
        
    - **Use with**: `Context7` for official docs, `--depth` flag.
        
    - **Example Prompt**: "Using `--persona-mentor --depth`, explain the concept of Django's `select_related` and `prefetch_related` with practical examples involving `Product` and `Category` models, and when to use each."
        

## 3. MCP Servers: Capabilities & Usage for Web Development

SuperClaude's Modular Computing Processors (MCPs) provide specialized capabilities.

- **Context7 (Library Documentation) `--c7`**:
    
    - **Purpose**: Official library documentation & examples.
        
    - **When to Use**: External library integration (e.g., Django packages, React libraries like `react-query`), API documentation lookup, framework pattern research.
        
    - **Example**: `/build --react --c7` (React with official docs).
        
    - **Web Dev Use**: "Explain how to integrate `django-rest-framework-simplejwt` for token authentication using `--c7`."
        
- **Sequential (Complex Analysis) `--seq`**:
    
    - **Purpose**: Multi-step problem solving & architectural thinking.
        
    - **When to Use**: Complex system design, root cause analysis in full-stack interactions, performance investigation across layers.
        
    - **Example**: `/analyze --seq` (deep system analysis).
        
    - **Web Dev Use**: "Analyze the data flow and potential bottlenecks between my React frontend and Django backend for a real-time chat application using `--seq`."
        
- **Magic (UI Components) `--magic`**:
    
    - **Purpose**: UI component generation & design system integration.
        
    - **When to Use**: React/TypeScript component building, design system implementation (e.g., with Tailwind CSS), rapid UI prototyping.
        
    - **Example**: `/build --react --magic` (component generation).
        
    - **Web Dev Use**: "Generate a responsive `Navbar` component in React with TypeScript and Tailwind CSS, including a logo, navigation links, and a user profile dropdown using `--magic`."
        
- **Puppeteer (Browser Automation) `--pup`**:
    
    - **Purpose**: E2E testing, performance validation, browser automation.
        
    - **When to Use**: End-to-end testing of React applications, performance monitoring, visual validation, user interaction testing.
        
    - **Example**: `/test --e2e --pup` (E2E testing).
        
    - **Web Dev Use**: "Write Playwright scripts to simulate a user journey through a React e-commerce site, from browsing products to completing a purchase, using `--pup`."
        

## 4. Key Commands & When to Use

These commands, combined with personas and flags, enable powerful workflows.

### Analysis Commands

- **`/analyze`**: Comprehensive codebase analysis.
    
    - **Flags**: `--code --arch --security --performance --c7 --seq`
        
    - **When**: Understanding Django project structure, React component dependencies, identifying issues.
        
    - **Web Dev Use**: "`/analyze --code --arch --seq` my entire Django backend project structure and suggest improvements for modularity."
        
- **`/troubleshoot`**: Systematic problem investigation.
    
    - **Flags**: `--investigate --seq --evidence`
        
    - **When**: Debugging complex errors spanning Django and React (e.g., API communication issues).
        
    - **Web Dev Use**: "`/troubleshoot --investigate --seq` this authentication error that occurs when my React app tries to log in to the Django API. `[PASTE RELEVANT CODE/LOGS]`"
        
- **`/scan`**: Security, quality, and compliance scanning.
    
    - **Flags**: `--security --owasp --deps --validate`
        
    - **When**: Auditing Django dependencies, checking React frontend for XSS vulnerabilities.
        
    - **Web Dev Use**: "`/scan --security --owasp` my Django `settings.py` and `urls.py` for common misconfigurations."
        

### Development Commands

- **`/build`**: Feature implementation & project creation.
    
    - **Flags**: `--init --feature --react --api --magic --tdd`
        
    - **When**: Creating new Django models/views, React components, or entire project scaffolds.
        
    - **Web Dev Use**: "`/build --feature --react --magic --tdd` a new `UserProfile` editing form in React with TypeScript, including client-side validation and API integration."
        
- **`/design`**: Architectural design & system planning.
    
    - **Flags**: `--api --ddd --microservices --seq --ultrathink`
        
    - **When**: Designing Django API endpoints, database schemas, or React component hierarchies.
        
    - **Web Dev Use**: "`/design --api --seq` a GraphQL API schema for a social media application, considering Django's `graphene-django`."
        
- **`/test`**: Comprehensive testing & validation.
    
    - **Flags**: `--coverage --e2e --pup --validate`
        
    - **When**: Writing tests for Django models, views, or React components.
        
    - **Web Dev Use**: "`/test --coverage --e2e --pup` for my React application's dashboard page, ensuring all interactive elements are functional."
        

### Quality Commands

- **`/improve`**: Code quality & performance optimization.
    
    - **Flags**: `--quality --performance --security --iterate`
        
    - **When**: Refactoring Django ORM queries, optimizing React component re-renders, enhancing security.
        
    - **Web Dev Use**: "`/improve --quality --iterate` this Django view `[PASTE VIEW CODE]` to follow DRY principles and improve readability."
        
- **`/cleanup`**: Technical debt & maintenance.
    
    - **Flags**: `--code --all --dry-run`
        
    - **When**: Removing unused Django models/views, deprecated React components, or dead code.
        
    - **Web Dev Use**: "`/cleanup --code --dry-run` my Django project to identify and suggest removal of unused imports and functions."
        

### Operations Commands

- **`/deploy`**: Production deployment & operations.
    
    - **Flags**: `--env --validate --monitor --checkpoint`
        
    - **When**: Deploying Django/React applications to production environments.
        
    - **Web Dev Use**: "`/deploy --env production --validate` my Django backend to a cloud provider (e.g., AWS EC2) using Gunicorn and Nginx."
        
- **`/migrate`**: Data & schema migrations.
    
    - **Flags**: `--database --validate --dry-run --rollback`
        
    - **When**: Handling Django database migrations, data seeding.
        
    - **Web Dev Use**: "`/migrate --database --validate` my Django database to add a new `email_verified` field to the `User` model, ensuring no data loss."
        

## 5. Universal Flags: Always Available

These flags modify command behavior and are crucial for precise control.

- **`--plan`**: Show execution plan before running.
    
- **`--dry-run`**: Preview changes without execution (e.g., for refactoring or migrations).
    
- **`--force`**: Override safety checks (use with extreme caution).
    
- **`--interactive`**: Step-by-step guided process.
    
- **`--think`**: Multi-file analysis (4K tokens).
    
- **`--think-hard`**: Deep architectural analysis (10K tokens).
    
- **`--ultrathink`**: Critical system redesign (32K tokens).
    
- **`--uc`**: UltraCompressed mode (~70% token reduction) for large codebases.
    
- **`--profile`**: Detailed performance profiling.
    
- **`--watch`**: Continuous monitoring.
    
- **`--c7`**: Enable Context7 documentation lookup.
    
- **`--seq`**: Enable Sequential complex analysis.
    
- **`--magic`**: Enable Magic UI component generation.
    
- **`--pup`**: Enable Puppeteer browser automation.
    
- **`--all-mcp`**: Enable all MCP servers.
    
- **`--no-mcp`**: Disable all MCP servers.
    

## 6. Task Management System

SuperClaude employs a two-tier task management system for tracking progress and ensuring thoroughness.

- **Level 1 Tasks**: High-level features (`.claudedocs/tasks/`). For session persistence, git branching, and requirement tracking spanning multiple sessions.
    
- **Level 2 Todos**: Immediate actionable steps (TodoWrite/TodoRead). For real-time execution tracking within the current session.
    

**Auto-Trigger Rules**: Complex operations (3+ steps), high-risk tasks (database changes, deployments), long tasks (>30 minutes), or multi-file changes (6+ files) will automatically trigger a TodoList.

## 7. Security Configuration

Security is a core principle. Claude can assist with:

- **OWASP Top 10 Integration**: Automated detection patterns for common web vulnerabilities.
    
- **CVE Scanning**: For known vulnerabilities in dependencies.
    
- **Dependency Security**: With license compliance checks.
    
- **Configuration Security**: Including hardcoded secrets detection.
    

**Security Command Usage Examples**:

- "`/scan --security --owasp`": Full OWASP Top 10 scan of your web application.
    
- "`/analyze --security --seq`": Deep security analysis of a specific Django module or React component.
    
- "`/improve --security --harden`": Suggest security hardening measures for your Django REST API.
    

## 8. Performance Optimization

Claude helps optimize your web applications for speed and efficiency.

- **UltraCompressed Mode (`--uc`)**: Reduces token usage for large codebases, leading to faster responses and cost efficiency. Activates automatically or with the `--uc` flag.
    
- **MCP Caching**: `Context7` (1 hour TTL), `Sequential` (session duration), `Magic` (2 hours TTL) cache their results for faster subsequent operations.
    
- **Parallel Execution**: Independent MCP calls run simultaneously.
    

## 9. Quick Start Workflows for Django & React

Here are some common workflows tailored for your tech stack:

- **New Full-Stack Feature (Django API + React UI)**:
    
    ```
    /design --api --seq --ultrathink # Design the API schema
    /build --feature --api --tdd # Implement Django API endpoint with TDD
    /build --feature --react --magic --tdd # Build React component with TDD and Magic UI
    /test --e2e --pup # Run end-to-end tests
    ```
    
- **Debugging a Full-Stack Issue**:
    
    ```
    /troubleshoot --investigate --seq # Analyze logs and code across layers
    /analyze --code --performance --seq # Deep dive into specific code sections
    /improve --quality --iterate # Apply fixes and refactor
    ```
    
- **Security Audit of Web App**:
    
    ```
    /scan --security --owasp --deps # Scan backend and frontend dependencies
    /analyze --security --seq # Deep security analysis of critical paths
    /improve --security --harden # Implement security hardening
    ```
    
- **Optimizing React Frontend Performance**:
    
    ```
    /analyze --performance --pup --profile # Profile React app in browser
    /improve --performance --iterate # Suggest and apply optimizations (e.g., memoization)
    ```
    

## 10. Best Practices

Adhere to these best practices for optimal results with SuperClaude:

- **Evidence-Based Development**: Use language like "may," "could," "typically," "measured," "documented." Avoid absolute terms like "best," "always." Require citations for external information.
    
- **Quality Standards**: Emphasize Git safety, TDD patterns, and comprehensive test coverage.
    
- **Performance Guidelines**: Select appropriate models (`sonnet`, `opus`) based on task complexity. Prefer native tools for simple tasks.
    
- **Communication**: Use structured formats and symbols (e.g., `→`, `&`, `:`, `»`) for clarity.
    

## 11. Decision Matrix for Django & React Development

|**Scenario**|**Persona**|**MCP**|**Command**|**Flags**|
|---|---|---|---|---|
|**New React Component**|`--persona-frontend`|`--magic --c7`|`/build --feature`|`--react --tdd`|
|**Django API Design**|`--persona-architect`|`--seq --c7`|`/design --api`|`--ddd --ultrathink`|
|**Debug React-Django API**|`--persona-analyzer`|`--all-mcp`|`/troubleshoot`|`--investigate --seq`|
|**Optimize Django ORM**|`--persona-performance`|`--seq`|`/improve --performance`|`--profile --iterate`|
|**Refactor React Hook**|`--persona-refactorer`|`--seq`|`/improve --quality`|`--iterate`|
|**E2E Test React App**|`--persona-qa`|`--pup`|`/test --e2e`|`--coverage --validate`|
|**Explain Django Middleware**|`--persona-mentor`|`--c7`|`/explain`|`--depth`|
|**Deploy Full-Stack App**|`--persona-architect`|`--seq`|`/deploy --env prod`|`--validate --monitor`|

## 12. Directory Structure & File Organization

SuperClaude uses specific paths for documentation and configuration:

### Documentation Paths

- **`Claude_Docs`**: `.claudedocs/`
    
    - `Reports`: `.claudedocs/reports/`
        
    - `Metrics`: `.claudedocs/metrics/`
        
    - `Summaries`: `.claudedocs/summaries/`
        
    - `Checkpoints`: `.claudedocs/checkpoints/`
        
    - `Tasks`: `.claudedocs/tasks/`
        
- **`Project_Documentation`**: `docs/`
    
    - `API_Docs`: `docs/api/` (for Django REST API docs)
        
    - `User_Docs`: `docs/user/` (for React app user guides)
        
    - `Developer_Docs`: `docs/dev/` (for internal dev guides)
        

### Configuration Files Structure

- `Main_Config`: `.claude/settings.local.json`
    
- `Shared_Configs`: `.claude/shared/`
    
- `Command_Patterns`: `.claude/commands/shared/`
    
- `Personas`: `.claude/shared/superclaude-personas.yml`
    
- `MCP_Integration`: `.claude/shared/superclaude-mcp.yml`
    

This comprehensive guide, integrating the SuperClaude configuration system, provides unprecedented power and flexibility for AI-assisted Django and React (TypeScript) web development. Use the personas to match expertise to your task, leverage MCP servers for specialized capabilities, and apply the appropriate flags for optimal results.