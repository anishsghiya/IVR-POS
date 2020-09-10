# -- coding: utf-8 --
"""
Created on Sun Aug 23 15:03:04 2020

@author: ANISH
"""

import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="hi", host="127.0.0.1", port="5432")
print("Database Connected....")

cur = conn.cursor()

# Creating the table
cur.execute("CREATE TABLE category_table(category_id INT,parent_id INT,category_name VARCHAR(25))")
print("Table Created....")

# Inserts into the table

cur.execute("INSERT INTO category_table (category_id,parent_id, category_name) \
      VALUES (1, 1, 'Bakery')");

cur.execute("INSERT INTO category_table (category_id,parent_id, category_name) \
      VALUES (2, 1, 'Bread')");

cur.execute("INSERT INTO category_table (category_id,parent_id, category_name) \
      VALUES (3, 1, 'Bun')");

cur.execute("INSERT INTO category_table (category_id,parent_id, category_name) \
      VALUES (4, 4, 'Dairy')");

cur.execute("INSERT INTO category_table (category_id,parent_id, category_name) \
      VALUES (5, 4, 'Milk')");
      
cur.execute("INSERT INTO category_table (category_id,parent_id, category_name) \
      VALUES (6, 4, 'Cheese')");

cur.execute("INSERT INTO category_table (category_id,parent_id, category_name) \
      VALUES (7, 7, 'Beverages')");
      
conn.commit()
print("Records created successfully");
cur.execute("SELECT * from category_table")
#print("ID   Roll No. Student Name")
print("--------------------------") 
rows = cur.fetchall()
for row in rows:
   #print(row[0],' ',str(row[2]).strip(),'      ',row[1].strip())
    print(row)
conn.close()