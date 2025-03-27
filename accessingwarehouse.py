
import pyodbc
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials from environment variables
TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
SERVER = os.getenv("SERVER")
DATABASE = os.getenv("DATABASE")

# Debugging: Print to check if values are loaded (remove in production)
print(f"TENANT_ID: {TENANT_ID}")
print(f"CLIENT_ID: {CLIENT_ID}")
print(f"SERVER: {SERVER}")
print(f"DATABASE: {DATABASE}")

# Check if all environment variables are loaded correctly
if not all([TENANT_ID, CLIENT_ID, CLIENT_SECRET, SERVER, DATABASE]):
    raise ValueError("One or more environment variables are missing. Check your .env file.")

# Construct the connection string
conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={SERVER};'
    f'DATABASE={DATABASE};'
    f'UID={CLIENT_ID}@{TENANT_ID};'
    f'PWD={CLIENT_SECRET};'
    f'Authentication=ActiveDirectoryServicePrincipal'
)

try:
    # Establish connection
    cnxn = pyodbc.connect(conn_str)
    cursor = cnxn.cursor()

    # Execute a test query
    cursor.execute("SELECT * FROM [dbo].[employees]")  # Fetch employee data
    rows = cursor.fetchall()

    # Print the retrieved data
    print("Employee Data:")
    for row in rows:
        print(row)

except pyodbc.Error as ex:
    print(f"Error connecting to the database: {ex}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'cnxn' in locals():
        cnxn.close()
