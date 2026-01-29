# pesaDB — A Minimal Relational Database Engine 

pesaDB is a **simple in-memory relational database management system (RDBMS)** built from scratch in Python as part of the **Pesapal Junior Developer Challenge 2026**.


A SQL-like interface and interactive REPL are provided, along with a Django web application to demonstrate real-world CRUD usage.

---

##  Features

### Core Database Engine
- SQL-like command interface
- Interactive REPL
- In-memory table storage
- Supported data types: `INT`, `TEXT`
- `CREATE TABLE`, `INSERT`, `SELECT`
- Primary key enforcement
- Unique constraints
- Hash-map based indexing
- Indexed `WHERE` queries

### Web Application
- Built with Django
- **No Django ORM usage**
- Views call the custom DB engine directly
- Demonstrates CRUD operations on the database


---
## 🖥️ Running pesaDB (REPL)

### Requirements
- Python **3.12+**
- Ubuntu 24.04 (or similar Linux/macOS)

### Start the REPL
```bash
cd pesadb
python3 repl.py

```

![pesaDB REPL Demo](/docs/repl-demo.png)

## Web Application Demo

The Django web app demonstrates CRUD operations using the custom database engine (no ORM).

### Screenshot 1 — Users List
![users list](/docs/image.png)

### Screenshot 2 — Create User
http://127.0.0.1:8000/users/create/?id=4&email=newdev@pesapal.com
![Create Users](/docs/image2.png)

### Screenshot 3 — JSON Persistence Proof
![Persisted Data](/docs/image3.png)

### Persistence Model

- Tables are stored in memory during runtime
- On shutdown or explicit save, rows are written to:
- - data/<table_name>.json

- On startup:

- - Schema is bootstrapped

- - Data is loaded from disk

- - Indexes are rebuilt

## Request Flow (No ORM)

1. Browser sends HTTP request to Django
2. Django view receives request
3. View calls `db.execute()`
4. Custom database engine parses and executes SQL
5. Data is stored in memory and persisted to disk
6. Response is returned to the browser

## Use of AI Tools

- AI tools were used as assistants for brainstorming, debugging guidance, and review.
- All architectural decisions and core logic were implemented by me.

---
## What I Learned Building pesaDB
### Building pesaDB from scratch helped me deeply understand how real databases and web systems work behind the scenes. Key learnings include:
- Persistence & State
- - Differences between in-memory state and persistent storage
- - How to serialize tables to disk using JSON
- Django Without ORM
- - How Django works beyond its ORM
- - Calling a custom backend directly from Django view


