import pandas as pd 
import numpy as np
import pyodbc
import json

server = "LAPTOP-OL5QT5EE\MSSQLSERVER_SC"
database = "AdventureWorks2019"
username = "sa"
password = "Jushank@2021"


# Establishing a connection to the SQL Server
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                      SERVER='+server+';\
                      DATABASE='+database+';\
                      UID='+username+';\
                      PWD='+ password)

cursor = cnxn.cursor()


if cnxn:
    print("Connection Successful")
else:
    print("Connection Failed")

query = "Select * from [HumanResources].[Department]"
# Using Dataframes

# query = "Select * from [HumanResources].[Department]"
# df = pd.read_sql(query,cnxn)
# def Eng_name():
#     eng_name = df["Name"].value_counts()
#     return eng_name

# a = Eng_name()
# print("\nDepartment names with the most employees:\n",a)

def department_data():
    cursor.execute(query)
    # Fetch all rows from the database
    data = cursor.fetchall()
    # Get column names from the cursor description
    columns = [column[0] for column in cursor.description]
    # Convert each row to a dictionary
    data_dict = [dict(zip(columns, row)) for row in data]
    # Serialize to JSON, handling datetime conversion
    return data_dict



