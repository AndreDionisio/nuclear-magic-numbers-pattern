# SQL Exercises Database - Nuclear Magic Numbers Project

## 📊 Database Overview

This MySQL database contains exercises for learning SQL queries based on a business scenario with customers, products, orders, and order details.

## 🗂️ Database Schema

### Tables:

1. **CLIENT** - Customer information
   - `NCLI` (VARCHAR): Customer code (Primary Key)
   - `NOM` (VARCHAR): Customer name
   - `LOCALITE` (VARCHAR): City/location
   - `CAT` (VARCHAR): Customer category
   - `COMPTE` (DECIMAL): Account balance

2. **PRODUIT** - Product information
   - `NPRO` (VARCHAR): Product code (Primary Key)
   - `LIBELLE` (VARCHAR): Product description
   - `PRIX` (DECIMAL): Unit price
   - `QSTOCK` (INT): Stock quantity

3. **COMMANDE** - Order information
   - `NCOM` (VARCHAR): Order code (Primary Key)
   - `NCLI` (VARCHAR): Customer code (Foreign Key)
   - `DATECOM` (DATE): Order date

4. **DETAIL** - Order details
   - `NCOM` (VARCHAR): Order code (Foreign Key)
   - `NPRO` (VARCHAR): Product code (Foreign Key)
   - `QCOM` (INT): Ordered quantity
   - Primary Key: (NCOM, NPRO)

## 🚀 Getting Started

### Prerequisites
- MySQL Server 8.4.6 installed
- MySQL client tools

### Database Setup
The database is automatically created by running:
```bash
mysql -u root -p < sql_exercises_setup.sql
```

### Connection
```bash
mysql -u root -p
# Password: password123
USE sql_exercises;
```

## 📋 Sample Data

### Products (PRODUIT)
- CS262: CEEV. SAPIN 200X6X2 (3960.00€, 20 in stock)
- CS264: CEEV. SAPIN 200X6X4 (2310.00€, 15 in stock)
- CS464: CEEV. SAPIN 400X6X4 (1900.00€, 25 in stock)
- PA60: POINTE ACIER 60 (1K) (2250.00€, 140 in stock)
- PA45: POINTE ACIER 45 (1K) (1425.00€, 200 in stock)
- PS222: PL. SAPIN 200X20X2 (6650.00€, 60 in stock)
- PE222: PL. ETRE 200X20X2 (21160.00€, 30 in stock)

### Cities (Localités)
- Lille, Namur, Bruxelles, Poitiers, Toulouse, Paris

### Categories
- BI: Business category

## 🔍 Sample Queries

### Basic Queries
```sql
-- 1.4: Products containing "ACIER" (steel)
SELECT NPRO, LIBELLE, PRIX, QSTOCK
FROM PRODUIT
WHERE LIBELLE LIKE '%ACIER%';

-- 1.7: Customer categories in Toulouse
SELECT DISTINCT CAT
FROM CLIENT
WHERE LOCALITE = 'Toulouse' AND CAT IS NOT NULL;

-- 1.9: Account statistics
SELECT
    SUM(COMPTE) as TOTAL,
    MIN(COMPTE) as MINIMUM,
    AVG(COMPTE) as MOYENNE,
    MAX(COMPTE) as MAXIMUM
FROM CLIENT;
```

### Join Queries
```sql
-- 1.18: Order detail amounts
SELECT
    D.NCOM,
    D.NPRO,
    D.QCOM,
    P.PRIX,
    (D.QCOM * P.PRIX) as MONTANT
FROM DETAIL D
JOIN PRODUIT P ON D.NPRO = P.NPRO;

-- 1.19: Total stock value
SELECT SUM(PRIX * QSTOCK) as VALEUR_TOTALE_STOCKS
FROM PRODUIT;
```

## 📚 Exercise Categories

The exercises are organized in 7 types:

1. **Type 1**: Basic SELECT queries
2. **Type 2**: Advanced filtering and aggregation
3. **Type 3**: Calculations and joins
4. **Type 4**: Complex queries with subqueries
5. **Type 5**: Advanced aggregation and analysis
6. **Type 6**: Unresolved exercises
7. **Type 7**: Complex business logic scripts

## 🛠️ Database Management

### View Tables
```sql
SHOW TABLES;
DESCRIBE CLIENT;
DESCRIBE PRODUIT;
DESCRIBE COMMANDE;
DESCRIBE DETAIL;
```

### Count Records
```sql
SELECT COUNT(*) FROM CLIENT;
SELECT COUNT(*) FROM PRODUIT;
SELECT COUNT(*) FROM COMMANDE;
SELECT COUNT(*) FROM DETAIL;
```

## 📖 Learning Objectives

These exercises cover:
- Basic SQL syntax (SELECT, FROM, WHERE)
- JOIN operations (INNER, LEFT, RIGHT)
- Aggregation functions (SUM, AVG, COUNT, MIN, MAX)
- Subqueries and complex filtering
- Date operations
- String pattern matching (LIKE)
- NULL value handling
- GROUP BY and HAVING clauses
- ORDER BY and LIMIT clauses

## 🎯 Next Steps

1. Start with Type 1 exercises (basic queries)
2. Progress to more complex joins and aggregations
3. Practice subqueries and advanced filtering
4. Attempt the unresolved exercises
5. Create your own business queries

## 🔗 Related Files

- `sql_exercises_setup.sql` - Database creation script
- `mysql_setup.ps1` - MySQL configuration guide
- `README.md` - Main project documentation

---

*Database created for SQL learning exercises in the Nuclear Magic Numbers research project.*