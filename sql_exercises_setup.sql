-- ========================================
-- SQL EXERCISES DATABASE SETUP
-- Nuclear Magic Numbers Project
-- ========================================

-- Create database
CREATE DATABASE IF NOT EXISTS sql_exercises;
USE sql_exercises;

-- ========================================
-- TABLE: CLIENT (Customers)
-- ========================================
CREATE TABLE CLIENT (
    NCLI VARCHAR(10) PRIMARY KEY,
    NOM VARCHAR(50) NOT NULL,
    LOCALITE VARCHAR(50),
    CAT VARCHAR(5),
    COMPTE DECIMAL(10,2)
);

-- Insert CLIENT data
INSERT INTO CLIENT VALUES
('FOIO', 'FRANCK', 'Lille', 'BI', -1250.00),
('KIII', 'MERCIER', 'Lille', 'BI', 0.00),
('S121', 'VAN DER KA', 'Lille', 'BI', 250.00),
('ES12', 'FRANCK', 'Lille', 'BI', 0.00),
('C400', 'FRANCK', 'Lille', 'BI', -250.00),
('F011', 'FRANCK', 'Lille', 'BI', 0.00),
('L422', 'FRANCK', 'Lille', 'BI', 0.00),
('SI12', 'FRANCK', 'Lille', 'BI', 0.00),
('F400', 'FRANCK', 'Lille', 'BI', 0.00),
('E062', 'GOFFIN', 'Namur', 'BI', 0.00),
('C009', 'AVRON', 'Namur', 'BI', 0.00),
('K129', 'NEUMAN', 'Namur', 'BI', 0.00),
('C123', 'FRANCK', 'Bruxelles', 'BI', 0.00),
('E012', 'HANSENNE', 'Poitiers', 'BI', 0.00),
('C122', 'MERCIER', 'Poitiers', 'BI', 0.00),
('C023', 'MONTI', 'Toulouse', 'BI', 0.00),
('F012', 'TAUSSANT', 'Toulouse', 'BI', 0.00),
('S127', 'FRANCK', 'Paris', 'BI', 0.00);

-- ========================================
-- TABLE: PRODUIT (Products)
-- ========================================
CREATE TABLE PRODUIT (
    NPRO VARCHAR(10) PRIMARY KEY,
    LIBELLE VARCHAR(100) NOT NULL,
    PRIX DECIMAL(8,2),
    QSTOCK INT
);

-- Insert PRODUIT data
INSERT INTO PRODUIT VALUES
('CS262', 'CEEV. SAPIN 200X6X2', 3960.00, 20),
('CS264', 'CEEV. SAPIN 200X6X4', 2310.00, 15),
('CS464', 'CEEV. SAPIN 400X6X4', 1900.00, 25),
('PA60', 'POINTE ACIER 60 (1K)', 2250.00, 140),
('PA45', 'POINTE ACIER 45 (1K)', 1425.00, 200),
('PS222', 'PL. SAPIN 200X20X2', 6650.00, 60),
('PE222', 'PL. ETRE 200X20X2', 21160.00, 30);

-- ========================================
-- TABLE: COMMANDE (Orders)
-- ========================================
CREATE TABLE COMMANDE (
    NCOM VARCHAR(10) PRIMARY KEY,
    NCLI VARCHAR(10),
    DATECOM DATE,
    FOREIGN KEY (NCLI) REFERENCES CLIENT(NCLI)
);

-- Insert COMMANDE data
INSERT INTO COMMANDE VALUES
('30119', 'FOIO', '2000-10-15'),
('30122', 'KIII', '2000-10-16'),
('30124', 'S121', '2000-10-18'),
('30126', 'ES12', '2000-10-20'),
('30182', 'S127', '2000-12-23');

-- ========================================
-- TABLE: DETAIL (Order Details)
-- ========================================
CREATE TABLE DETAIL (
    NCOM VARCHAR(10),
    NPRO VARCHAR(10),
    QCOM INT,
    PRIMARY KEY (NCOM, NPRO),
    FOREIGN KEY (NCOM) REFERENCES COMMANDE(NCOM),
    FOREIGN KEY (NPRO) REFERENCES PRODUIT(NPRO)
);

-- Insert DETAIL data
INSERT INTO DETAIL VALUES
('30119', 'CS262', 1),
('30119', 'PA60', 2),
('30122', 'CS464', 1),
('30122', 'PA45', 1),
('30124', 'CS464', 1),
('30124', 'PA60', 1),
('30126', 'CS262', 1),
('30126', 'CS464', 1),
('30126', 'PA45', 1),
('30182', 'PA60', 1);

-- ========================================
-- SAMPLE QUERIES FOR TESTING
-- ========================================

-- 1.4 Afficher les caractéristiques des produits en acier
SELECT NPRO, LIBELLE, PRIX, QSTOCK
FROM PRODUIT
WHERE LIBELLE LIKE '%ACIER%';

-- 1.7 Quelles catégories de clients trouve-t-on à Toulouse ?
SELECT DISTINCT CAT
FROM CLIENT
WHERE LOCALITE = 'Toulouse' AND CAT IS NOT NULL;

-- 1.9 Afficher le total, le minimum, la moyenne et le maximum des comptes
SELECT
    SUM(COMPTE) as TOTAL,
    MIN(COMPTE) as MINIMUM,
    AVG(COMPTE) as MOYENNE,
    MAX(COMPTE) as MAXIMUM
FROM CLIENT;

-- 1.18 Calculer le montant de chaque détail de commande
SELECT
    D.NCOM,
    D.NPRO,
    D.QCOM,
    P.PRIX,
    (D.QCOM * P.PRIX) as MONTANT
FROM DETAIL D
JOIN PRODUIT P ON D.NPRO = P.NPRO;

-- 1.19 Afficher la valeur totale des stocks
SELECT SUM(PRIX * QSTOCK) as VALEUR_TOTALE_STOCKS
FROM PRODUIT;

SELECT 'Database setup completed successfully!' as STATUS;