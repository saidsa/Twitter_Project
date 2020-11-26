#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pyodbc
import sys


# In[45]:


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-A81OQTP\SQLEXPRESS;'
                      'Database=WideWorldImporters-Full;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute("select CustomerID,TransactionDate,TaxAmount from Sales.CustomerTransactions")

for row in cursor:
    print(row)


# In[51]:


cursor.execute("UPDATE Sales.CustomerTransactions SET TaxAmount=200 where CustomerID=832 ")
cursor.execute("select CustomerID,TransactionDate,TaxAmount from Sales.CustomerTransactions where CustomerID>830 and CustomerID<833 ")
for row in cursor:
    print(row)


# In[ ]:


conn.commit()

