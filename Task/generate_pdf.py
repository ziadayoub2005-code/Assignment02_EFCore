import os
import subprocess

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Navigation Properties in Entity Framework Core - Technical Article &amp; Guide</title>
<style>
  @page {
    size: A4;
    margin: 14mm 14mm 14mm 14mm;
    @bottom-right {
      content: "Page " counter(page);
      font-size: 8.5pt;
      color: #64748b;
    }
    @bottom-left {
      content: "EF Core 5.0 • Navigation Properties & Relationship Mapping";
      font-size: 8.5pt;
      color: #64748b;
    }
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1e293b;
    line-height: 1.55;
    font-size: 10pt;
    background: #ffffff;
  }

  .page-break {
    page-break-before: always;
  }
  .avoid-break {
    page-break-inside: avoid;
  }

  /* Cover / Title Header */
  .cover-header {
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 60%, #2563eb 100%);
    color: white;
    padding: 36px 30px;
    border-radius: 12px;
    margin-bottom: 24px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
  }
  .cover-header .tagline {
    text-transform: uppercase;
    font-size: 9pt;
    letter-spacing: 1.5px;
    color: #93c5fd;
    font-weight: 700;
    margin-bottom: 10px;
  }
  .cover-header h1 {
    font-size: 24pt;
    line-height: 1.25;
    font-weight: 800;
    margin-bottom: 12px;
  }
  .cover-header .subtitle {
    font-size: 11pt;
    color: #e2e8f0;
    font-weight: 400;
    margin-bottom: 18px;
  }
  .cover-meta {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px 20px;
    font-size: 9pt;
    color: #bfdbfe;
    border-top: 1px solid rgba(255,255,255,0.25);
    padding-top: 14px;
  }
  .cover-meta span strong { color: white; }

  .toc-box {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 20px 24px;
    margin-top: 20px;
  }
  .toc-box h3 {
    color: #0f172a;
    font-size: 11.5pt;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .toc-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px 24px;
    font-size: 9pt;
    color: #334155;
  }
  .toc-item {
    display: flex;
    justify-content: space-between;
    padding: 4px 0;
    border-bottom: 1px dashed #cbd5e1;
  }

  /* Headings */
  h2 {
    font-size: 14pt;
    color: #0f172a;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 10px;
    padding-bottom: 5px;
    border-bottom: 2px solid #e2e8f0;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  h3 {
    font-size: 11.5pt;
    color: #1e3a8a;
    font-weight: 700;
    margin-top: 14px;
    margin-bottom: 6px;
  }
  h4 {
    font-size: 10pt;
    color: #334155;
    font-weight: 700;
    margin-top: 10px;
    margin-bottom: 4px;
  }

  p { margin-bottom: 8px; text-align: justify; }

  ul, ol {
    margin-left: 20px;
    margin-bottom: 10px;
  }
  li { margin-bottom: 4px; }

  /* Code block */
  pre {
    background: #0f172a;
    color: #f8fafc;
    padding: 10px 12px;
    border-radius: 6px;
    font-family: "Consolas", "Courier New", monospace;
    font-size: 8.5pt;
    line-height: 1.4;
    margin-bottom: 10px;
    overflow-x: auto;
    border: 1px solid #1e293b;
    page-break-inside: avoid;
  }
  code {
    font-family: "Consolas", "Courier New", monospace;
    background: #f1f5f9;
    color: #0f172a;
    padding: 2px 4px;
    border-radius: 4px;
    font-size: 8.5pt;
  }
  pre code {
    background: transparent;
    color: inherit;
    padding: 0;
  }

  .c-kw { color: #f43f5e; font-weight: 600; }
  .c-typ { color: #38bdf8; font-weight: 600; }
  .c-str { color: #34d399; }
  .c-com { color: #94a3b8; font-style: italic; }
  .c-met { color: #fbbf24; }

  /* Tables */
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 8px;
    margin-bottom: 14px;
    font-size: 9pt;
    page-break-inside: avoid;
  }
  th, td {
    padding: 7px 9px;
    border: 1px solid #cbd5e1;
    text-align: left;
  }
  th {
    background: #f8fafc;
    color: #0f172a;
    font-weight: 700;
  }
  tr:nth-child(even) td { background: #fcfcfd; }

  /* Callout boxes */
  .callout {
    padding: 10px 14px;
    border-radius: 6px;
    margin-bottom: 12px;
    font-size: 9pt;
    page-break-inside: avoid;
  }
  .callout-info {
    background: #eff6ff;
    border-left: 4px solid #3b82f6;
    color: #1e3a8a;
  }
  .callout-tip {
    background: #f0fdf4;
    border-left: 4px solid #10b981;
    color: #065f46;
  }
  .callout-warn {
    background: #fffbeb;
    border-left: 4px solid #f59e0b;
    color: #92400e;
  }
  .callout-post {
    background: #f8fafc;
    border: 1.5px dashed #0a66c2;
    border-radius: 8px;
    padding: 14px 18px;
    margin-bottom: 16px;
    page-break-inside: avoid;
  }

  .post-header {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 10px;
    color: #0a66c2;
    font-weight: 700;
    font-size: 10.5pt;
  }

  .diagram-container {
    text-align: center;
    margin: 12px 0 8px 0;
    page-break-inside: avoid;
  }
  .diagram-container img {
    max-width: 100%;
    height: auto;
    border-radius: 6px;
    border: 1px solid #cbd5e1;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
  }
  .diagram-caption {
    font-size: 8.5pt;
    color: #64748b;
    margin-top: 4px;
    font-style: italic;
  }
</style>
</head>
<body>

<!-- PAGE 1: EXECUTIVE COVER & TOC -->
<div class="cover-header">
  <div class="tagline">Entity Framework Core 5.0 • Masterclass &amp; LinkedIn Technical Article</div>
  <h1>Demystifying Navigation Properties in EF Core</h1>
  <div class="subtitle">The Bridge Between Relational Foreign Keys and Pure Object-Oriented Domain Models</div>
  <div class="cover-meta">
    <span><strong>Author / Student:</strong> .NET Engineer</span>
    <span><strong>Framework:</strong> .NET 5.0 / EF Core 5.0.17</span>
    <span><strong>Course Track:</strong> Database &amp; ORM Architecture</span>
    <span><strong>Assignment:</strong> Day 04 / Part 02</span>
    <span><strong>Tooling:</strong> dotnet-ef CLI, SQL Server, Fluent API</span>
    <span><strong>Deliverables:</strong> Solutions, Migrations, DB Diagrams, Technical Article</span>
  </div>
</div>

<div class="toc-box">
  <h3>📑 Table of Contents</h3>
  <div class="toc-grid">
    <div class="toc-item"><span>1. LinkedIn Technical Article (Ready to Publish)</span> <span>Sec 1</span></div>
    <div class="toc-item"><span>2. What is a Navigation Property? (Definition &amp; Why)</span> <span>Sec 2</span></div>
    <div class="toc-item"><span>3. Foreign Key Property vs Navigation Property</span> <span>Sec 3</span></div>
    <div class="toc-item"><span>4. Types &amp; Directions of Navigation Properties</span> <span>Sec 4</span></div>
    <div class="toc-item"><span>5. Loading Strategies (Eager, Explicit, Lazy, Select)</span> <span>Sec 5</span></div>
    <div class="toc-item"><span>6. Common Pitfalls &amp; Performance Anti-Patterns</span> <span>Sec 6</span></div>
    <div class="toc-item"><span>7. Project 1: E-commerce System (Solution &amp; Diagram)</span> <span>Sec 7</span></div>
    <div class="toc-item"><span>8. Project 2: Library System (Solution &amp; Diagram)</span> <span>Sec 8</span></div>
    <div class="toc-item"><span>9. Project 3: Health Care System (Solution &amp; Diagram)</span> <span>Sec 9</span></div>
    <div class="toc-item"><span>10. Architectural Conclusions &amp; Best Practices</span> <span>Sec 10</span></div>
  </div>
</div>

<div class="callout callout-info" style="margin-top: 20px;">
  <strong>Executive Summary:</strong> This document serves as the formal answer to the written questions for Part 02. It combines an engaging, ready-to-publish LinkedIn article with a comprehensive technical deep-dive into Navigation Properties in Entity Framework Core 5.0, accompanied by complete database diagrams and Fluent API configurations for all three assigned systems.
</div>

<!-- PAGE 2: LINKEDIN ARTICLE -->
<div class="page-break"></div>

<h2>1. Ready-to-Publish LinkedIn Technical Article</h2>
<div class="callout-post">
  <div class="post-header">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="#0a66c2"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 10.9v8.37H9.2V10.9H6.46M7.83 6.64a1.66 1.66 0 1 0 0 3.32 1.66 1.66 0 0 0 0-3.32Z"/></svg>
    <span>LinkedIn Post: Why Foreign Keys Aren't Enough in C# &amp; EF Core</span>
  </div>
  <p>🚀 <strong>Stop treating your C# entities like database tables! Understanding Navigation Properties in Entity Framework Core.</strong></p>
  
  <p>When transitioning from SQL to Entity Framework Core, many developers fall into a classic trap: they focus purely on <code>int CategoryId</code> or <code>int CustomerId</code> and treat their C# classes as simple table mirrors.</p>

  <p>In relational databases, relationships are strictly represented by <strong>Foreign Keys</strong> (scalar values like integers). But in Object-Oriented Programming (OOP), we don't think in primary and foreign keys — we think in <strong>object graphs and references</strong>!</p>

  <p>That is exactly what a <strong>Navigation Property</strong> is: the magical bridge that allows you to traverse from one entity object directly to its related entity objects without writing manual SQL joins.</p>

  <p>🔑 <strong>The Difference at a Glance:</strong></p>
  <ul>
    <li><strong>Foreign Key Property (e.g., <code>DeptId</code>):</strong> A scalar database column holding a primitive key value. It guarantees referential integrity in SQL Server.</li>
    <li><strong>Navigation Property (e.g., <code>Dept</code> or <code>Employees</code>):</strong> A pointer/reference in C# to another entity object or collection. It does <em>not</em> exist as a separate column in the database table!</li>
  </ul>

  <p>⚡ <strong>The Two Flavors:</strong></p>
  <ol>
    <li><strong>Reference Navigation Property:</strong> Points to a single related entity instance (e.g., <code>product.Category</code>). Found on the "one" side of 1:N or in 1:1.</li>
    <li><strong>Collection Navigation Property:</strong> Holds multiple related entities (e.g., <code>category.Products</code>). Found on the "many" side of 1:N or in M:N.</li>
  </ol>

  <p>💡 <strong>How do you load them?</strong></p>
  <ul>
    <li><strong>Eager Loading (<code>.Include()</code>):</strong> Loads everything in a single SQL query with JOINs.</li>
    <li><strong>Explicit Loading (<code>.Load()</code>):</strong> Loads related data on-demand for a tracked entity.</li>
    <li><strong>Lazy Loading:</strong> Transparently fires queries on property access (convenient, but beware the dreaded <strong>N+1 query problem</strong>!).</li>
    <li><strong>Projection (<code>.Select()</code>):</strong> The gold standard for read APIs — retrieves only the exact columns you need.</li>
  </ul>

  <p>📌 <em>Pro-Tip for .NET Developers:</em> Always initialize your collection navigation properties with <code>new HashSet&lt;T&gt;()</code> or <code>new List&lt;T&gt;()</code> in your entity constructors to prevent nasty <code>NullReferenceException</code> bugs!</p>

  <p><em>Have you ever encountered the N+1 problem in production? How do you prefer loading your navigation properties? Let's discuss in the comments! 👇</em></p>
  <p><code>#DotNet #CSharp #EntityFrameworkCore #CleanCode #SoftwareArchitecture #DatabaseDesign #CodingTips</code></p>
</div>

<!-- PAGE 3: DEEP DIVE -->
<div class="page-break"></div>

<h2>2. Deep-Dive: What is a Navigation Property?</h2>
<p>
  In Entity Framework Core, an entity represents a business concept mapped to a database table. In a relational database, associations between tables are represented strictly by <strong>Foreign Key (FK)</strong> constraints. For example, an <code>Employees</code> table stores a <code>DeptId</code> integer pointing to the <code>Departments</code> primary key <code>Id</code>.
</p>
<p>
  However, Object-Oriented Programming (OOP) operates on <strong>object references</strong>. When you write C# code, you want to write <code>employee.Department.Name</code> or <code>department.Employees.Count</code> directly. You should not have to manually execute a second SQL query or look up a department by ID.
</p>
<div class="callout callout-info">
  <strong>Definition:</strong> A <strong>Navigation Property</strong> is an entity property that represents an association to another entity or a collection of entities. It enables navigation from one end of a relationship to another in your C# object graph.
</div>

<h2>3. Foreign Key Property vs. Navigation Property</h2>
<p>
  One of the most fundamental concepts in EF Core architecture is the clear division between Foreign Key Properties and Navigation Properties:
</p>

<table>
  <thead>
    <tr>
      <th>Dimension</th>
      <th>Foreign Key Property (Scalar)</th>
      <th>Navigation Property (Reference / Collection)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Representation</strong></td>
      <td>Primitive type (e.g., <code>int</code>, <code>Guid</code>, <code>int?</code>)</td>
      <td>Entity type or Collection (e.g., <code>Department</code>, <code>ICollection&lt;Employee&gt;</code>)</td>
    </tr>
    <tr>
      <td><strong>Database Presence</strong></td>
      <td>Persisted as an actual column in the database table</td>
      <td><strong>Does NOT exist</strong> as a column in the database</td>
    </tr>
    <tr>
      <td><strong>Purpose</strong></td>
      <td>Maintains referential integrity &amp; foreign key constraints in SQL Server</td>
      <td>Enables object traversal, graph construction, and high-level LINQ queries</td>
    </tr>
    <tr>
      <td><strong>Direction</strong></td>
      <td>Located solely on the <strong>dependent (child)</strong> entity</td>
      <td>Can be configured on <strong>one end (unidirectional)</strong> or <strong>both ends (bidirectional)</strong></td>
    </tr>
    <tr>
      <td><strong>Example in C#</strong></td>
      <td><code>public int DeptId { get; set; }</code></td>
      <td><code>public Department Dept { get; set; }</code> / <code>public ICollection&lt;Employee&gt; Employees { get; set; }</code></td>
    </tr>
  </tbody>
</table>

<h2>4. Types and Directions of Navigation Properties</h2>

<h3>A. Reference Navigation Property</h3>
<p>
  A Reference Navigation Property holds a reference to a <strong>single</strong> instance of a related entity type.
</p>
<pre><code><span class="c-kw">public class</span> <span class="c-typ">Product</span>
{
    <span class="c-kw">public int</span> Id { <span class="c-kw">get</span>; <span class="c-kw">set</span>; }
    <span class="c-kw">public string</span> Name { <span class="c-kw">get</span>; <span class="c-kw">set</span>; }
    <span class="c-kw">public int</span> CategoryId { <span class="c-kw">get</span>; <span class="c-kw">set</span>; } <span class="c-com">// Foreign Key</span>

    <span class="c-com">// Reference Navigation Property (Many-to-One)</span>
    <span class="c-kw">public</span> <span class="c-typ">Category</span> Category { <span class="c-kw">get</span>; <span class="c-kw">set</span>; }
}</code></pre>
<p>
  <strong>When to use:</strong> On the dependent side of a One-to-Many relationship (each product belongs to one category) or on either side of a One-to-One relationship.
</p>

<h3>B. Collection Navigation Property</h3>
<p>
  A Collection Navigation Property holds references to <strong>multiple</strong> related entity instances. It is typically typed as <code>ICollection&lt;T&gt;</code>, <code>IEnumerable&lt;T&gt;</code>, or <code>List&lt;T&gt;</code>.
</p>
<pre><code><span class="c-kw">public class</span> <span class="c-typ">Category</span>
{
    <span class="c-kw">public int</span> Id { <span class="c-kw">get</span>; <span class="c-kw">set</span>; }
    <span class="c-kw">public string</span> Name { <span class="c-kw">get</span>; <span class="c-kw">set</span>; }

    <span class="c-com">// Collection Navigation Property (One-to-Many)</span>
    <span class="c-kw">public</span> <span class="c-typ">ICollection</span>&lt;<span class="c-typ">Product</span>&gt; Products { <span class="c-kw">get</span>; <span class="c-kw">set</span>; } = <span class="c-kw">new</span> <span class="c-typ">HashSet</span>&lt;<span class="c-typ">Product</span>&gt;();
}</code></pre>

<div class="callout callout-tip">
  <strong>Best Practice:</strong> Always initialize your collection navigation properties in the class definition (e.g. <code>= new HashSet&lt;T&gt;();</code>). This ensures that adding items to <code>category.Products</code> won't throw a <code>NullReferenceException</code> before EF Core materializes the collection. <code>HashSet&lt;T&gt;</code> is preferred over <code>List&lt;T&gt;</code> because it prevents duplicate entries and provides $O(1)$ lookup performance.
</div>

<!-- PAGE 4: LOADING STRATEGIES -->
<div class="page-break"></div>

<h2>5. Loading Strategies: How EF Core Fetches Related Data</h2>
<p>
  By default, EF Core does <strong>not</strong> load navigation properties automatically when querying an entity. You must explicitly choose how related data should be fetched from the database:
</p>

<h3>1. Eager Loading (<code>.Include()</code> &amp; <code>.ThenInclude()</code>)</h3>
<p>
  Related data is fetched from the database as part of the initial query using SQL <code>LEFT JOIN</code> or <code>INNER JOIN</code>.
</p>
<pre><code><span class="c-com">// Eagerly load Customer and all OrderDetails + their Products</span>
<span class="c-kw">var</span> orders = context.Orders
    .<span class="c-met">Include</span>(o =&gt; o.Customer)
    .<span class="c-met">Include</span>(o =&gt; o.OrderDetails)
        .<span class="c-met">ThenInclude</span>(od =&gt; od.Product)
    .<span class="c-met">ToList</span>();</code></pre>
<p>
  <strong>New in EF Core 5.0 (Filtered Includes):</strong> You can now apply LINQ filters inside <code>.Include()</code>!
</p>
<pre><code><span class="c-kw">var</span> categories = context.Categories
    .<span class="c-met">Include</span>(c =&gt; c.Products.<span class="c-met">Where</span>(p =&gt; p.Price &gt; 100))
    .<span class="c-met">ToList</span>();</code></pre>
<p>
  <strong>Caution (Cartesian Explosion):</strong> Including multiple collection navigation properties can multiply result rows in SQL. In EF Core 5.0+, use <code>.AsSplitQuery()</code> to split the SQL into separate queries for each collection.
</p>

<h3>2. Explicit Loading</h3>
<p>
  Related data is explicitly loaded at a later point in time for an entity that is already tracked by the <code>DbContext</code>.
</p>
<pre><code><span class="c-kw">var</span> order = context.Orders.<span class="c-met">Find</span>(1);

<span class="c-com">// Explicitly load the reference navigation property</span>
context.<span class="c-met">Entry</span>(order).<span class="c-met">Reference</span>(o =&gt; o.Customer).<span class="c-met">Load</span>();

<span class="c-com">// Explicitly load collection navigation property with filtering</span>
context.<span class="c-met">Entry</span>(order).<span class="c-met">Collection</span>(o =&gt; o.OrderDetails)
    .<span class="c-met">Query</span>()
    .<span class="c-met">Where</span>(od =&gt; od.Quantity &gt; 2)
    .<span class="c-met">Load</span>();</code></pre>

<h3>3. Lazy Loading</h3>
<p>
  Related data is transparently loaded from the database the moment the navigation property is accessed in memory.
  Requires marking navigation properties as <code>virtual</code> and installing <code>Microsoft.EntityFrameworkCore.Proxies</code>:
</p>
<pre><code>optionsBuilder.<span class="c-met">UseLazyLoadingProxies</span>().<span class="c-met">UseSqlServer</span>(connectionString);

<span class="c-kw">public virtual</span> <span class="c-typ">Category</span> Category { <span class="c-kw">get</span>; <span class="c-kw">set</span>; }</code></pre>

<h2>6. Common Pitfalls &amp; Performance Anti-Patterns</h2>
<div class="callout callout-warn">
  <strong>The N+1 Query Problem:</strong> If you loop over 100 products and access <code>product.Category.Name</code> with lazy loading, EF Core will execute <strong>1 query for the products + 100 queries for the categories (101 SQL roundtrips)</strong>! This severely degrades application throughput.
</div>

<h3>4. Projection / Select Loading (The Performance Champion)</h3>
<pre><code><span class="c-kw">var</span> report = context.Products
    .<span class="c-met">Select</span>(p =&gt; <span class="c-kw">new</span> {
        p.Name,
        p.Price,
        CategoryName = p.Category.Name
    })
    .<span class="c-met">ToList</span>();</code></pre>
<p>
  Projection generates SQL that selects <strong>only</strong> the requested columns (no <code>SELECT *</code>), completely bypassing tracking overhead and avoiding Cartesian explosion.
</p>

<!-- PAGE 5: PROJECT 1 -->
<div class="page-break"></div>

<h2>7. Project 1: E-commerce System</h2>
<p>
  <strong>Requirements:</strong> Maps relationships between Products, Categories, Customers, Orders, and OrderDetails.
</p>
<ul>
  <li><code>Category</code> to <code>Product</code>: <strong>One-to-Many</strong></li>
  <li><code>Customer</code> to <code>Order</code>: <strong>One-to-Many</strong></li>
  <li><code>Order</code> to <code>Product</code>: <strong>Many-to-Many</strong> through <code>OrderDetail</code> (Payload: <code>Quantity</code>, Composite PK: <code>OrderId, ProductId</code>)</li>
</ul>

<div class="diagram-container">
  <img src="file:///Users/mac/Desktop/banhaday04/Task/Screenshots/Ecommerce_DB_Diagram.png" alt="E-commerce System DB Diagram">
  <div class="diagram-caption">Figure 1: E-commerce System Relational Schema &amp; Navigation Mapping (SQL Server / EF Core 5.0)</div>
</div>

<div class="avoid-break">
  <h4>Key Fluent API Configuration (OrderDetails Composite Key &amp; Foreign Keys):</h4>
  <pre><code><span class="c-kw">public class</span> <span class="c-typ">OrderDetailConfiguration</span> : <span class="c-typ">IEntityTypeConfiguration</span>&lt;<span class="c-typ">OrderDetail</span>&gt;
{
    <span class="c-kw">public void</span> <span class="c-met">Configure</span>(<span class="c-typ">EntityTypeBuilder</span>&lt;<span class="c-typ">OrderDetail</span>&gt; builder)
    {
        builder.<span class="c-met">ToTable</span>(<span class="c-str">"OrderDetails"</span>);

        <span class="c-com">// Composite Primary Key</span>
        builder.<span class="c-met">HasKey</span>(od =&gt; <span class="c-kw">new</span> { od.OrderId, od.ProductId });

        builder.<span class="c-met">Property</span>(od =&gt; od.Quantity).<span class="c-met">HasDefaultValue</span>(1);

        <span class="c-com">// Order to OrderDetail (1:M)</span>
        builder.<span class="c-met">HasOne</span>(od =&gt; od.Order)
               .<span class="c-met">WithMany</span>(o =&gt; o.OrderDetails)
               .<span class="c-met">HasForeignKey</span>(od =&gt; od.OrderId)
               .<span class="c-met">OnDelete</span>(DeleteBehavior.Cascade);

        <span class="c-com">// Product to OrderDetail (1:M)</span>
        builder.<span class="c-met">HasOne</span>(od =&gt; od.Product)
               .<span class="c-met">WithMany</span>(p =&gt; p.OrderDetails)
               .<span class="c-met">HasForeignKey</span>(od =&gt; od.ProductId)
               .<span class="c-met">OnDelete</span>(DeleteBehavior.Restrict);
    }
}</code></pre>
</div>

<!-- PAGE 6: PROJECT 2 -->
<div class="page-break"></div>

<h2>8. Project 2: Library System</h2>
<p>
  <strong>Requirements:</strong> Maps relationships between Books, Authors, Borrowers, and Loans.
</p>
<ul>
  <li><code>Author</code> to <code>Book</code>: <strong>One-to-Many</strong> (Author has many Books; Book belongs to one Author)</li>
  <li><code>Book</code> to <code>Borrower</code>: <strong>Many-to-Many</strong> through <code>Loan</code> (Payload: <code>LoanDate</code>, <code>ReturnDate</code>, Composite PK: <code>BookId, BorrowerId</code>)</li>
</ul>

<div class="diagram-container">
  <img src="file:///Users/mac/Desktop/banhaday04/Task/Screenshots/Library_DB_Diagram.png" alt="Library System DB Diagram">
  <div class="diagram-caption">Figure 2: Library System Relational Schema &amp; Navigation Mapping (SQL Server / EF Core 5.0)</div>
</div>

<div class="avoid-break">
  <h4>Key Fluent API Configuration (Loan Composite Key &amp; Mappings):</h4>
  <pre><code><span class="c-kw">public class</span> <span class="c-typ">LoanConfiguration</span> : <span class="c-typ">IEntityTypeConfiguration</span>&lt;<span class="c-typ">Loan</span>&gt;
{
    <span class="c-kw">public void</span> <span class="c-met">Configure</span>(<span class="c-typ">EntityTypeBuilder</span>&lt;<span class="c-typ">Loan</span>&gt; builder)
    {
        builder.<span class="c-met">ToTable</span>(<span class="c-str">"Loans"</span>);

        <span class="c-com">// Composite Primary Key</span>
        builder.<span class="c-met">HasKey</span>(l =&gt; <span class="c-kw">new</span> { l.BookId, l.BorrowerId });

        builder.<span class="c-met">Property</span>(l =&gt; l.LoanDate).<span class="c-met">HasDefaultValueSql</span>(<span class="c-str">"GETDATE()"</span>);
        builder.<span class="c-met">Property</span>(l =&gt; l.ReturnDate).<span class="c-met">IsRequired</span>(<span class="c-kw">false</span>);

        <span class="c-com">// Book to Loan (1:M)</span>
        builder.<span class="c-met">HasOne</span>(l =&gt; l.Book)
               .<span class="c-met">WithMany</span>(b =&gt; b.Loans)
               .<span class="c-met">HasForeignKey</span>(l =&gt; l.BookId)
               .<span class="c-met">OnDelete</span>(DeleteBehavior.Cascade);

        <span class="c-com">// Borrower to Loan (1:M)</span>
        builder.<span class="c-met">HasOne</span>(l =&gt; l.Borrower)
               .<span class="c-met">WithMany</span>(b =&gt; b.Loans)
               .<span class="c-met">HasForeignKey</span>(l =&gt; l.BorrowerId)
               .<span class="c-met">OnDelete</span>(DeleteBehavior.Cascade);
    }
}</code></pre>
</div>

<!-- PAGE 7: PROJECT 3 -->
<div class="page-break"></div>

<h2>9. Project 3: Health Care System</h2>
<p>
  <strong>Requirements:</strong> Maps relationships between Patients, Doctors, and Appointments.
</p>
<ul>
  <li><code>Patient</code> to <code>Doctor</code>: <strong>Many-to-Many</strong> through <code>Appointment</code> (Payload: <code>AppointmentDate</code>, Composite PK: <code>PatientId, DoctorId, AppointmentDate</code>)</li>
</ul>

<div class="diagram-container">
  <img src="file:///Users/mac/Desktop/banhaday04/Task/Screenshots/HealthCare_DB_Diagram.png" alt="Health Care System DB Diagram">
  <div class="diagram-caption">Figure 3: Health Care System Relational Schema &amp; Navigation Mapping (SQL Server / EF Core 5.0)</div>
</div>

<div class="avoid-break">
  <h4>Key Fluent API Configuration (Appointment Composite Key &amp; Mappings):</h4>
  <pre><code><span class="c-kw">public class</span> <span class="c-typ">AppointmentConfiguration</span> : <span class="c-typ">IEntityTypeConfiguration</span>&lt;<span class="c-typ">Appointment</span>&gt;
{
    <span class="c-kw">public void</span> <span class="c-met">Configure</span>(<span class="c-typ">EntityTypeBuilder</span>&lt;<span class="c-typ">Appointment</span>&gt; builder)
    {
        builder.<span class="c-met">ToTable</span>(<span class="c-str">"Appointments"</span>);

        <span class="c-com">// Composite Primary Key (Includes AppointmentDate to support multiple visits)</span>
        builder.<span class="c-met">HasKey</span>(a =&gt; <span class="c-kw">new</span> { a.PatientId, a.DoctorId, a.AppointmentDate });

        builder.<span class="c-met">Property</span>(a =&gt; a.AppointmentDate).<span class="c-met">IsRequired</span>();

        <span class="c-com">// Patient to Appointment (1:M)</span>
        builder.<span class="c-met">HasOne</span>(a =&gt; a.Patient)
               .<span class="c-met">WithMany</span>(p =&gt; p.Appointments)
               .<span class="c-met">HasForeignKey</span>(a =&gt; a.PatientId)
               .<span class="c-met">OnDelete</span>(DeleteBehavior.Cascade);

        <span class="c-com">// Doctor to Appointment (1:M)</span>
        builder.<span class="c-met">HasOne</span>(a =&gt; a.Doctor)
               .<span class="c-met">WithMany</span>(d =&gt; d.Appointments)
               .<span class="c-met">HasForeignKey</span>(a =&gt; a.DoctorId)
               .<span class="c-met">OnDelete</span>(DeleteBehavior.Cascade);
    }
}</code></pre>
</div>

<!-- PAGE 8: SUMMARY & ARCHITECTURAL CONCLUSIONS -->
<div class="page-break"></div>

<h2>10. Architectural Conclusions &amp; Best Practices</h2>
<ol>
  <li><strong>Foreign Keys vs Navigation Properties:</strong> Always remember that Foreign Keys are for relational data integrity in the database, whereas Navigation Properties are for object traversal and LINQ queries in C#.</li>
  <li><strong>Keep Collections Safe:</strong> Initialize all collection navigation properties to prevent null reference runtime exceptions (<code>= new HashSet&lt;T&gt;();</code>).</li>
  <li><strong>Explicit Configuration with Fluent API:</strong> Prefer separate configuration classes implementing <code>IEntityTypeConfiguration&lt;T&gt;</code> over data annotations to achieve clean code separation and adhere to the Single Responsibility Principle.</li>
  <li><strong>Watch Out For Performance:</strong> Choose your loading strategy deliberately. Use Eager Loading (<code>Include</code>) for rich graphs, but switch to Projection (<code>Select</code>) for read-heavy API endpoints to minimize memory allocations and network payloads.</li>
  <li><strong>Handling Object Cycles:</strong> In .NET Core APIs, circular references in navigation properties can trigger infinite serialization loops. Resolve this cleanly using <code>JsonSerializerOptions.ReferenceHandler = ReferenceHandler.IgnoreCycles</code> or by projecting directly to DTOs.</li>
</ol>

<div class="callout callout-tip" style="margin-top: 24px;">
  <strong>Solution Verification:</strong> The entire .NET 5 solution containing all three projects (<code>EcommerceSystem</code>, <code>LibrarySystem</code>, <code>HealthCareSystem</code>) compiles with 0 errors and 0 warnings, complete with full EF Core migrations and SQL generation scripts.
</div>

</body>
</html>
"""

html_path = "/Users/mac/Desktop/banhaday04/Task/Navigation_Property_LinkedIn_Article.html"
pdf_path = "/Users/mac/Desktop/banhaday04/Task/Navigation_Property_LinkedIn_Article.pdf"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--print-to-pdf-no-header",
    f"--print-to-pdf={pdf_path}",
    f"file://{html_path}"
]

subprocess.run(cmd, check=True)
print(f"Generated PDF: {pdf_path} ({os.path.getsize(pdf_path)} bytes)")
