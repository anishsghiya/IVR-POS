# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 16:57:12 2020

@author: ANISH
"""

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

cur.execute("CREATE TABLE invoice(invoice_id INT, item_id INT, item_name VARCHAR(25), coster INT, quantity INT, overall INT)")
print("Table Created....")


# Inserts into the table


cur.execute("INSERT INTO invoice (invoice_id, item_id, item_name, coster, quantity, overall) \
      VALUES (1, 1, 'Britania milk bread', 40, 2, 80)");
"""
cur.execute("INSERT INTO category_table (category_id,parent_id, category_name) \
      VALUES (2, 2, 'Bread')");

cur.execute("INSERT INTO category_table (category_id,parent_id, category_name) \
      VALUES (3, 2, 'Bun')");

cur.execute("INSERT INTO category_table (category_id,parent_id, category_name) \
      VALUES (4, 3, 'Dairy')");

cur.execute("INSERT INTO category_table (category_id,parent_id, category_name) \
      VALUES (5, 5, 'Milk')");
      
cur.execute("INSERT INTO category_table (category_id,parent_id, category_name) \
      VALUES (6, 5, 'Cheese')");

cur.execute("INSERT INTO category_table (category_id,parent_id, category_name) \
      VALUES (7, 7, 'Beverages')");
"""      
print("Row created")
conn.commit()