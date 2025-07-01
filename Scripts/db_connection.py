import mysql.connector

# Database connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123",
  database='lung_disease_DB'
)
