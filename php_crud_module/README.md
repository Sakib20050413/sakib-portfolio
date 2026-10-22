# PHP + MySQLi Procedural CRUD Module
**Course:** Web Technology Theory (CSE 323) / Sessional (CSE 324)  
**Student:** Md Najmus Sakib Rahatul (`Student ID: 1119003`)  
**Institution:** Dept. of Computer Science & Engineering, BAIUST, Cumilla  

---

## Academic Objective
This standalone directory demonstrates raw, procedural **PHP 8.x + MySQLi** database connectivity and full **Create, Read, Update, Delete (CRUD)** lifecycle alongside the main Python Django 5.x ORM architecture.

## Files Structure
- `db.php`: Database connection, auto-creates database `portfolio_db` and tables `projects` & `messages`. Pre-seeds real BAIUST project rows if table is empty.
- `index.php`: Master dashboard with live search filter, project list, and message inbox.
- `create.php`: Prepared statement SQL INSERT form.
- `update.php`: Prepared statement SQL UPDATE form.
- `delete.php`: Prepared statement SQL DELETE handler.

## How to Run for Lab Demonstration
### Option A: Using Built-in PHP CLI Server
1. Ensure your MySQL server (via XAMPP, WampServer, or native MySQL service) is running on port 3306 with user `root` and empty password (default).
2. Open terminal in the project root and run:
   ```bash
   php -S localhost:8080 -t php_crud_module/
   ```
3. Open your browser and navigate to: `http://localhost:8080/index.php`

### Option B: Using XAMPP / htdocs
Copy this `php_crud_module` folder into your `C:\xampp\htdocs\` directory and visit `http://localhost/php_crud_module/`.
