import os
import subprocess

html_ecommerce = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>E-commerce System - Database Diagram</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
  body {
    background-color: #f0f3f8;
    background-image: radial-gradient(#d5dce6 1px, transparent 1px);
    background-size: 20px 20px;
    padding: 30px;
    width: 1400px;
    height: 850px;
    position: relative;
  }
  .header-bar {
    background: linear-gradient(135deg, #1e3a8a, #2563eb);
    color: white;
    padding: 16px 24px;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 25px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .header-bar h1 { font-size: 22px; font-weight: 700; letter-spacing: 0.5px; }
  .header-bar .subtitle { font-size: 13px; opacity: 0.9; }
  .badge { background: #3b82f6; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 600; }
  
  .canvas {
    position: relative;
    width: 1340px;
    height: 720px;
  }
  
  .table-card {
    position: absolute;
    background: #ffffff;
    border-radius: 8px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08), 0 2px 6px rgba(0,0,0,0.04);
    border: 1px solid #cbd5e1;
    width: 250px;
    overflow: hidden;
    z-index: 2;
  }
  
  .table-header {
    background: #1e293b;
    color: white;
    padding: 10px 14px;
    font-size: 14px;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 2px solid #3b82f6;
  }
  
  .table-header.center-table {
    background: #0f172a;
    border-bottom: 2px solid #10b981;
  }

  .table-body {
    padding: 0;
  }
  
  .column-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 7px 12px;
    border-bottom: 1px solid #f1f5f9;
    font-size: 12px;
  }
  .column-row:last-child { border-bottom: none; }
  .column-row:hover { background: #f8fafc; }
  
  .col-name {
    display: flex;
    align-items: center;
    gap: 6px;
    font-weight: 600;
    color: #1e293b;
  }
  .col-type {
    font-family: 'Consolas', 'Courier New', monospace;
    color: #64748b;
    font-size: 11px;
  }
  
  .key-icon {
    font-size: 10px;
    padding: 2px 5px;
    border-radius: 4px;
    font-weight: 800;
    text-transform: uppercase;
  }
  .pk { background: #fef3c7; color: #b45309; border: 1px solid #fde68a; }
  .fk { background: #e0e7ff; color: #4338ca; border: 1px solid #c7d2fe; }
  .pk-fk { background: #fce7f3; color: #be185d; border: 1px solid #fbcfe8; }
  
  svg.lines {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
    pointer-events: none;
  }
  
  .rel-line {
    fill: none;
    stroke: #3b82f6;
    stroke-width: 2.5;
  }
  .rel-line-alt {
    fill: none;
    stroke: #10b981;
    stroke-width: 2.5;
  }
  .rel-text {
    font-size: 11px;
    font-weight: 700;
    fill: #1e3a8a;
    background: white;
  }
  
  .legend {
    position: absolute;
    bottom: 10px;
    right: 10px;
    background: white;
    padding: 10px 16px;
    border-radius: 8px;
    border: 1px solid #cbd5e1;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    display: flex;
    gap: 15px;
    font-size: 11px;
    color: #334155;
    z-index: 3;
  }
</style>
</head>
<body>

<div class="header-bar">
  <div>
    <h1>Project 1: E-commerce System — Database Diagram</h1>
    <div class="subtitle">Entity Framework Core 5.0 (SQL Server Schema &amp; Navigation Properties)</div>
  </div>
  <div>
    <span class="badge">Code-First &bull; Fluent API</span>
  </div>
</div>

<div class="canvas">
  <svg class="lines">
    <!-- Category to Product (1 to Many) -->
    <!-- Categories right edge: (300, 110), Products left edge: (450, 150) -->
    <path d="M 300 110 L 375 110 L 375 150 L 450 150" class="rel-line" />
    <text x="310" y="102" class="rel-text">1</text>
    <text x="430" y="142" class="rel-text">&infin;</text>

    <!-- Customer to Order (1 to Many) -->
    <!-- Customers right edge: (300, 480), Orders left edge: (450, 480) -->
    <path d="M 300 480 L 450 480" class="rel-line" />
    <text x="310" y="472" class="rel-text">1</text>
    <text x="430" y="472" class="rel-text">&infin;</text>

    <!-- Product to OrderDetail (1 to Many) -->
    <!-- Products right edge: (700, 170), OrderDetails left edge: (850, 270) -->
    <path d="M 700 170 L 775 170 L 775 270 L 850 270" class="rel-line-alt" />
    <text x="710" y="162" class="rel-text">1</text>
    <text x="830" y="262" class="rel-text">&infin;</text>

    <!-- Order to OrderDetail (1 to Many) -->
    <!-- Orders right edge: (700, 470), OrderDetails left edge: (850, 310) -->
    <path d="M 700 470 L 775 470 L 775 310 L 850 310" class="rel-line-alt" />
    <text x="710" y="462" class="rel-text">1</text>
    <text x="830" y="325" class="rel-text">&infin;</text>
  </svg>

  <!-- Categories Table -->
  <div class="table-card" style="left: 50px; top: 40px; width: 250px;">
    <div class="table-header">
      <span>&#128194;</span>
      <span>Categories</span>
    </div>
    <div class="table-body">
      <div class="column-row">
        <div class="col-name"><span class="key-icon pk">PK</span> Id</div>
        <div class="col-type">int (Identity)</div>
      </div>
      <div class="column-row">
        <div class="col-name">Name</div>
        <div class="col-type">nvarchar(100)</div>
      </div>
    </div>
  </div>

  <!-- Products Table -->
  <div class="table-card" style="left: 450px; top: 40px; width: 250px;">
    <div class="table-header">
      <span>&#128230;</span>
      <span>Products</span>
    </div>
    <div class="table-body">
      <div class="column-row">
        <div class="col-name"><span class="key-icon pk">PK</span> Id</div>
        <div class="col-type">int (Identity)</div>
      </div>
      <div class="column-row">
        <div class="col-name">Name</div>
        <div class="col-type">nvarchar(150)</div>
      </div>
      <div class="column-row">
        <div class="col-name">Price</div>
        <div class="col-type">decimal(18,2)</div>
      </div>
      <div class="column-row">
        <div class="col-name"><span class="key-icon fk">FK</span> CategoryId</div>
        <div class="col-type">int</div>
      </div>
    </div>
  </div>

  <!-- Customers Table -->
  <div class="table-card" style="left: 50px; top: 400px; width: 250px;">
    <div class="table-header">
      <span>&#128100;</span>
      <span>Customers</span>
    </div>
    <div class="table-body">
      <div class="column-row">
        <div class="col-name"><span class="key-icon pk">PK</span> Id</div>
        <div class="col-type">int (Identity)</div>
      </div>
      <div class="column-row">
        <div class="col-name">Name</div>
        <div class="col-type">nvarchar(100)</div>
      </div>
      <div class="column-row">
        <div class="col-name">Email</div>
        <div class="col-type">nvarchar(150)</div>
      </div>
    </div>
  </div>

  <!-- Orders Table -->
  <div class="table-card" style="left: 450px; top: 380px; width: 250px;">
    <div class="table-header">
      <span>&#128722;</span>
      <span>Orders</span>
    </div>
    <div class="table-body">
      <div class="column-row">
        <div class="col-name"><span class="key-icon pk">PK</span> Id</div>
        <div class="col-type">int (Identity)</div>
      </div>
      <div class="column-row">
        <div class="col-name">OrderDate</div>
        <div class="col-type">datetime2</div>
      </div>
      <div class="column-row">
        <div class="col-name"><span class="key-icon fk">FK</span> CustomerId</div>
        <div class="col-type">int</div>
      </div>
    </div>
  </div>

  <!-- OrderDetails Table (Bridge / Payload Join Entity) -->
  <div class="table-card" style="left: 850px; top: 200px; width: 280px; border: 2px solid #10b981;">
    <div class="table-header center-table">
      <span>&#128221;</span>
      <span>OrderDetails (Join Table)</span>
    </div>
    <div class="table-body">
      <div class="column-row" style="background: #f0fdf4;">
        <div class="col-name"><span class="key-icon pk-fk">PK, FK</span> OrderId</div>
        <div class="col-type">int</div>
      </div>
      <div class="column-row" style="background: #f0fdf4;">
        <div class="col-name"><span class="key-icon pk-fk">PK, FK</span> ProductId</div>
        <div class="col-type">int</div>
      </div>
      <div class="column-row">
        <div class="col-name">Quantity</div>
        <div class="col-type">int (Default: 1)</div>
      </div>
    </div>
  </div>

  <div class="legend">
    <div><span class="key-icon pk">PK</span> Primary Key</div>
    <div><span class="key-icon fk">FK</span> Foreign Key</div>
    <div><span class="key-icon pk-fk">PK, FK</span> Composite Primary &amp; Foreign Key</div>
    <div><strong style="color: #3b82f6;">&mdash;</strong> 1-to-Many</div>
    <div><strong style="color: #10b981;">&mdash;</strong> Many-to-Many (Bridge)</div>
  </div>
</div>

</body>
</html>
"""

html_library = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Library System - Database Diagram</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
  body {
    background-color: #f0f3f8;
    background-image: radial-gradient(#d5dce6 1px, transparent 1px);
    background-size: 20px 20px;
    padding: 30px;
    width: 1400px;
    height: 750px;
    position: relative;
  }
  .header-bar {
    background: linear-gradient(135deg, #0f766e, #0d9488);
    color: white;
    padding: 16px 24px;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 25px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .header-bar h1 { font-size: 22px; font-weight: 700; letter-spacing: 0.5px; }
  .header-bar .subtitle { font-size: 13px; opacity: 0.9; }
  .badge { background: #14b8a6; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 600; }
  
  .canvas {
    position: relative;
    width: 1340px;
    height: 620px;
  }
  
  .table-card {
    position: absolute;
    background: #ffffff;
    border-radius: 8px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08), 0 2px 6px rgba(0,0,0,0.04);
    border: 1px solid #cbd5e1;
    width: 250px;
    overflow: hidden;
    z-index: 2;
  }
  
  .table-header {
    background: #1e293b;
    color: white;
    padding: 10px 14px;
    font-size: 14px;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 2px solid #0d9488;
  }
  
  .table-header.center-table {
    background: #0f172a;
    border-bottom: 2px solid #f59e0b;
  }

  .table-body {
    padding: 0;
  }
  
  .column-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 7px 12px;
    border-bottom: 1px solid #f1f5f9;
    font-size: 12px;
  }
  .column-row:last-child { border-bottom: none; }
  .column-row:hover { background: #f8fafc; }
  
  .col-name {
    display: flex;
    align-items: center;
    gap: 6px;
    font-weight: 600;
    color: #1e293b;
  }
  .col-type {
    font-family: 'Consolas', 'Courier New', monospace;
    color: #64748b;
    font-size: 11px;
  }
  
  .key-icon {
    font-size: 10px;
    padding: 2px 5px;
    border-radius: 4px;
    font-weight: 800;
    text-transform: uppercase;
  }
  .pk { background: #fef3c7; color: #b45309; border: 1px solid #fde68a; }
  .fk { background: #e0e7ff; color: #4338ca; border: 1px solid #c7d2fe; }
  .pk-fk { background: #fce7f3; color: #be185d; border: 1px solid #fbcfe8; }
  
  svg.lines {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
    pointer-events: none;
  }
  
  .rel-line {
    fill: none;
    stroke: #0d9488;
    stroke-width: 2.5;
  }
  .rel-line-alt {
    fill: none;
    stroke: #f59e0b;
    stroke-width: 2.5;
  }
  .rel-text {
    font-size: 11px;
    font-weight: 700;
    fill: #0f766e;
    background: white;
  }
  
  .legend {
    position: absolute;
    bottom: 10px;
    right: 10px;
    background: white;
    padding: 10px 16px;
    border-radius: 8px;
    border: 1px solid #cbd5e1;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    display: flex;
    gap: 15px;
    font-size: 11px;
    color: #334155;
    z-index: 3;
  }
</style>
</head>
<body>

<div class="header-bar">
  <div>
    <h1>Project 2: Library System — Database Diagram</h1>
    <div class="subtitle">Entity Framework Core 5.0 (SQL Server Schema &amp; Navigation Properties)</div>
  </div>
  <div>
    <span class="badge">Code-First &bull; Fluent API</span>
  </div>
</div>

<div class="canvas">
  <svg class="lines">
    <!-- Author to Book (1 to Many) -->
    <!-- Authors right edge: (320, 150), Books left edge: (470, 150) -->
    <path d="M 320 150 L 470 150" class="rel-line" />
    <text x="330" y="142" class="rel-text">1</text>
    <text x="450" y="142" class="rel-text">&infin;</text>

    <!-- Book to Loan (1 to Many) -->
    <!-- Books right edge: (730, 170), Loans left edge: (880, 230) -->
    <path d="M 730 170 L 805 170 L 805 230 L 880 230" class="rel-line-alt" />
    <text x="740" y="162" class="rel-text">1</text>
    <text x="860" y="222" class="rel-text">&infin;</text>

    <!-- Borrower to Loan (1 to Many) -->
    <!-- Borrowers right edge: (730, 420), Loans left edge: (880, 280) -->
    <path d="M 730 420 L 805 420 L 805 280 L 880 280" class="rel-line-alt" />
    <text x="740" y="412" class="rel-text">1</text>
    <text x="860" y="295" class="rel-text">&infin;</text>
  </svg>

  <!-- Authors Table -->
  <div class="table-card" style="left: 60px; top: 70px; width: 260px;">
    <div class="table-header">
      <span>&#9997;</span>
      <span>Authors</span>
    </div>
    <div class="table-body">
      <div class="column-row">
        <div class="col-name"><span class="key-icon pk">PK</span> Id</div>
        <div class="col-type">int (Identity)</div>
      </div>
      <div class="column-row">
        <div class="col-name">Name</div>
        <div class="col-type">nvarchar(100)</div>
      </div>
      <div class="column-row">
        <div class="col-name">BirthDate</div>
        <div class="col-type">datetime2</div>
      </div>
    </div>
  </div>

  <!-- Books Table -->
  <div class="table-card" style="left: 470px; top: 60px; width: 260px;">
    <div class="table-header">
      <span>&#128218;</span>
      <span>Books</span>
    </div>
    <div class="table-body">
      <div class="column-row">
        <div class="col-name"><span class="key-icon pk">PK</span> Id</div>
        <div class="col-type">int (Identity)</div>
      </div>
      <div class="column-row">
        <div class="col-name">Title</div>
        <div class="col-type">nvarchar(150)</div>
      </div>
      <div class="column-row">
        <div class="col-name">ISBN</div>
        <div class="col-type">nvarchar(20)</div>
      </div>
      <div class="column-row">
        <div class="col-name"><span class="key-icon fk">FK</span> AuthorId</div>
        <div class="col-type">int</div>
      </div>
    </div>
  </div>

  <!-- Borrowers Table -->
  <div class="table-card" style="left: 470px; top: 340px; width: 260px;">
    <div class="table-header">
      <span>&#129489;</span>
      <span>Borrowers</span>
    </div>
    <div class="table-body">
      <div class="column-row">
        <div class="col-name"><span class="key-icon pk">PK</span> Id</div>
        <div class="col-type">int (Identity)</div>
      </div>
      <div class="column-row">
        <div class="col-name">Name</div>
        <div class="col-type">nvarchar(100)</div>
      </div>
      <div class="column-row">
        <div class="col-name">MembershipDate</div>
        <div class="col-type">datetime2</div>
      </div>
    </div>
  </div>

  <!-- Loans Table (Bridge / Join Entity with Payload) -->
  <div class="table-card" style="left: 880px; top: 180px; width: 280px; border: 2px solid #f59e0b;">
    <div class="table-header center-table">
      <span>&#128196;</span>
      <span>Loans (Join Table)</span>
    </div>
    <div class="table-body">
      <div class="column-row" style="background: #fffbeb;">
        <div class="col-name"><span class="key-icon pk-fk">PK, FK</span> BookId</div>
        <div class="col-type">int</div>
      </div>
      <div class="column-row" style="background: #fffbeb;">
        <div class="col-name"><span class="key-icon pk-fk">PK, FK</span> BorrowerId</div>
        <div class="col-type">int</div>
      </div>
      <div class="column-row">
        <div class="col-name">LoanDate</div>
        <div class="col-type">datetime2</div>
      </div>
      <div class="column-row">
        <div class="col-name">ReturnDate</div>
        <div class="col-type">datetime2 (Null)</div>
      </div>
    </div>
  </div>

  <div class="legend">
    <div><span class="key-icon pk">PK</span> Primary Key</div>
    <div><span class="key-icon fk">FK</span> Foreign Key</div>
    <div><span class="key-icon pk-fk">PK, FK</span> Composite Primary &amp; Foreign Key</div>
    <div><strong style="color: #0d9488;">&mdash;</strong> 1-to-Many</div>
    <div><strong style="color: #f59e0b;">&mdash;</strong> Many-to-Many (Loan)</div>
  </div>
</div>

</body>
</html>
"""

html_healthcare = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Health Care System - Database Diagram</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
  body {
    background-color: #f0f3f8;
    background-image: radial-gradient(#d5dce6 1px, transparent 1px);
    background-size: 20px 20px;
    padding: 30px;
    width: 1400px;
    height: 720px;
    position: relative;
  }
  .header-bar {
    background: linear-gradient(135deg, #7c3aed, #6366f1);
    color: white;
    padding: 16px 24px;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 25px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .header-bar h1 { font-size: 22px; font-weight: 700; letter-spacing: 0.5px; }
  .header-bar .subtitle { font-size: 13px; opacity: 0.9; }
  .badge { background: #8b5cf6; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 600; }
  
  .canvas {
    position: relative;
    width: 1340px;
    height: 590px;
  }
  
  .table-card {
    position: absolute;
    background: #ffffff;
    border-radius: 8px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08), 0 2px 6px rgba(0,0,0,0.04);
    border: 1px solid #cbd5e1;
    width: 270px;
    overflow: hidden;
    z-index: 2;
  }
  
  .table-header {
    background: #1e293b;
    color: white;
    padding: 10px 14px;
    font-size: 14px;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 8px;
    border-bottom: 2px solid #8b5cf6;
  }
  
  .table-header.center-table {
    background: #0f172a;
    border-bottom: 2px solid #ec4899;
  }

  .table-body {
    padding: 0;
  }
  
  .column-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 12px;
    border-bottom: 1px solid #f1f5f9;
    font-size: 12px;
  }
  .column-row:last-child { border-bottom: none; }
  .column-row:hover { background: #f8fafc; }
  
  .col-name {
    display: flex;
    align-items: center;
    gap: 6px;
    font-weight: 600;
    color: #1e293b;
  }
  .col-type {
    font-family: 'Consolas', 'Courier New', monospace;
    color: #64748b;
    font-size: 11px;
  }
  
  .key-icon {
    font-size: 10px;
    padding: 2px 5px;
    border-radius: 4px;
    font-weight: 800;
    text-transform: uppercase;
  }
  .pk { background: #fef3c7; color: #b45309; border: 1px solid #fde68a; }
  .fk { background: #e0e7ff; color: #4338ca; border: 1px solid #c7d2fe; }
  .pk-fk { background: #fce7f3; color: #be185d; border: 1px solid #fbcfe8; }
  
  svg.lines {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1;
    pointer-events: none;
  }
  
  .rel-line {
    fill: none;
    stroke: #ec4899;
    stroke-width: 2.5;
  }
  .rel-text {
    font-size: 11px;
    font-weight: 700;
    fill: #be185d;
    background: white;
  }
  
  .legend {
    position: absolute;
    bottom: 10px;
    right: 10px;
    background: white;
    padding: 10px 16px;
    border-radius: 8px;
    border: 1px solid #cbd5e1;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    display: flex;
    gap: 15px;
    font-size: 11px;
    color: #334155;
    z-index: 3;
  }
</style>
</head>
<body>

<div class="header-bar">
  <div>
    <h1>Project 3: Health Care System — Database Diagram</h1>
    <div class="subtitle">Entity Framework Core 5.0 (SQL Server Schema &amp; Navigation Properties)</div>
  </div>
  <div>
    <span class="badge">Code-First &bull; Fluent API</span>
  </div>
</div>

<div class="canvas">
  <svg class="lines">
    <!-- Patient to Appointment (1 to Many) -->
    <!-- Patients right edge: (370, 200), Appointments left edge: (520, 200) -->
    <path d="M 370 200 L 520 200" class="rel-line" />
    <text x="380" y="192" class="rel-text">1</text>
    <text x="500" y="192" class="rel-text">&infin;</text>

    <!-- Doctor to Appointment (1 to Many) -->
    <!-- Doctors left edge: (930, 200), Appointments right edge: (820, 200) -->
    <path d="M 930 200 L 820 200" class="rel-line" />
    <text x="915" y="192" class="rel-text">1</text>
    <text x="835" y="192" class="rel-text">&infin;</text>
  </svg>

  <!-- Patients Table -->
  <div class="table-card" style="left: 100px; top: 120px; width: 270px;">
    <div class="table-header">
      <span>&#129301;</span>
      <span>Patients</span>
    </div>
    <div class="table-body">
      <div class="column-row">
        <div class="col-name"><span class="key-icon pk">PK</span> Id</div>
        <div class="col-type">int (Identity)</div>
      </div>
      <div class="column-row">
        <div class="col-name">Name</div>
        <div class="col-type">nvarchar(100)</div>
      </div>
      <div class="column-row">
        <div class="col-name">DateOfBirth</div>
        <div class="col-type">datetime2</div>
      </div>
    </div>
  </div>

  <!-- Appointments Table (Join Entity with Date Payload) -->
  <div class="table-card" style="left: 520px; top: 110px; width: 300px; border: 2px solid #ec4899;">
    <div class="table-header center-table">
      <span>&#128197;</span>
      <span>Appointments (Join Table)</span>
    </div>
    <div class="table-body">
      <div class="column-row" style="background: #fdf2f8;">
        <div class="col-name"><span class="key-icon pk-fk">PK, FK</span> PatientId</div>
        <div class="col-type">int</div>
      </div>
      <div class="column-row" style="background: #fdf2f8;">
        <div class="col-name"><span class="key-icon pk-fk">PK, FK</span> DoctorId</div>
        <div class="col-type">int</div>
      </div>
      <div class="column-row" style="background: #fdf2f8;">
        <div class="col-name"><span class="key-icon pk">PK</span> AppointmentDate</div>
        <div class="col-type">datetime2</div>
      </div>
    </div>
  </div>

  <!-- Doctors Table -->
  <div class="table-card" style="left: 930px; top: 120px; width: 270px;">
    <div class="table-header">
      <span>&#129658;</span>
      <span>Doctors</span>
    </div>
    <div class="table-body">
      <div class="column-row">
        <div class="col-name"><span class="key-icon pk">PK</span> Id</div>
        <div class="col-type">int (Identity)</div>
      </div>
      <div class="column-row">
        <div class="col-name">Name</div>
        <div class="col-type">nvarchar(100)</div>
      </div>
      <div class="column-row">
        <div class="col-name">Specialization</div>
        <div class="col-type">nvarchar(100)</div>
      </div>
    </div>
  </div>

  <div class="legend">
    <div><span class="key-icon pk">PK</span> Primary Key</div>
    <div><span class="key-icon fk">FK</span> Foreign Key</div>
    <div><span class="key-icon pk-fk">PK, FK</span> Composite Primary &amp; Foreign Key</div>
    <div><strong style="color: #ec4899;">&mdash;</strong> Many-to-Many Relationship (Patient &bull; Doctor)</div>
  </div>
</div>

</body>
</html>
"""

base_dir = "/Users/mac/Desktop/banhaday04/Task"
screenshots_dir = os.path.join(base_dir, "Screenshots")

files = [
    ("ecommerce_diagram.html", html_ecommerce, "Ecommerce_DB_Diagram.png", (1400, 850)),
    ("library_diagram.html", html_library, "Library_DB_Diagram.png", (1400, 750)),
    ("healthcare_diagram.html", html_healthcare, "HealthCare_DB_Diagram.png", (1400, 720))
]

chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

for html_name, html_content, img_name, (w, h) in files:
    html_path = os.path.join(screenshots_dir, html_name)
    img_path = os.path.join(screenshots_dir, img_name)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        f"--window-size={w},{h}",
        f"--screenshot={img_path}",
        f"file://{html_path}"
    ]
    subprocess.run(cmd, check=True)
    print(f"Generated {img_path} ({os.path.getsize(img_path)} bytes)")
