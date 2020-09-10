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
cur.execute("CREATE TABLE items(item_id INT,category_id INT,item_name VARCHAR(25),cost INT,item_attributes VARCHAR(50))")
print("Table Created....")

# Inserts into the table

cur.execute("INSERT INTO items (item_id,category_id, item_name , cost, item_attributes) \
      VALUES (1, 2, 'Britania milk bread', 40, 'britania,milk,bread')");

cur.execute("INSERT INTO items (item_id,category_id, item_name , cost, item_attributes) \
      VALUES (2, 2, 'Softy milk bread', 35, 'softy,milk,bread')");

cur.execute("INSERT INTO items (item_id,category_id, item_name , cost, item_attributes) \
      VALUES (3, 2, 'Britania wheat bread', 40, 'britania,wheat,bread')");

cur.execute("INSERT INTO items (item_id,category_id, item_name , cost, item_attributes) \
      VALUES (4, 3, 'Softy sweet bun', 25, 'softy,sweet,bun')");

cur.execute("INSERT INTO items (item_id,category_id, item_name , cost, item_attributes) \
      VALUES (5, 5, 'Jersey cow milk', 25, 'jersey,cow,milk')");
      
cur.execute("INSERT INTO items (item_id,category_id, item_name , cost, item_attributes) \
      VALUES (6, 5, 'Heritage cow milk', 25, 'heritage,cow,milk')");

conn.commit()
print("Records created successfully");
cur.execute("SELECT * from items")
#print("ID   Roll No. Student Name")
print("--------------------------") 
rows = cur.fetchall()
for row in rows:
   #print(row[0],' ',str(row[2]).strip(),'      ',row[1].strip())
    print(row)
conn.close()