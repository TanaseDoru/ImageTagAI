import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()
conn_str = os.environ.get("AZURE_SQL_CONNECTIONSTRING")
# print("Connection String:", conn_str)  # Debug print
try:
    conn = pyodbc.connect(conn_str)
    print("Connection successful!")
    conn.close()
except pyodbc.Error as e:
    print("Connection failed:", e)