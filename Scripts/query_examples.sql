import warnings
warnings.filterwarnings("ignore")

from db_connection import mydb

# Example SQL Queries

# Query 1: Select first 5 rows from covars
with mydb.cursor() as cursor:
    cursor.execute("SELECT * FROM covars LIMIT 5")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Query 2: Join covars and monitor with filters
with mydb.cursor() as cursor:
    cursor.execute("""
    SELECT ID, age_recr, mregion, PM25, NO2 
    FROM covars 
    INNER JOIN monitor 
    ON covars.mo_id = monitor.mo_id 
    WHERE sex = 1 AND age_recr > 40 
    LIMIT 5
    """)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
