import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM invoices WHERE BillingCountry = 'Germany' AND TOTAL > 2")

rows = cursor.fetchall()
for row in rows:
    print(row)