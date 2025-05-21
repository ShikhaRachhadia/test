import pyodbc

# Connection parameters
server = 'flasktest.database.windows.net'  # Replace with your actual server name
database = 'GAIDD'                          # Replace with your actual database name
username = 'flasktest'                      # Replace with your actual username
password = 'Shikha362'                      # Replace with your actual password
driver = '{ODBC Driver 18 for SQL Server}'  # Ensure this matches your installed driver

# Connection string
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # Establish a connection
    conn = pyodbc.connect(connection_string)
    print("Connection successful!")
    
    # Create a cursor from the connection
    cursor = conn.cursor()
    
    # Execute a simple query to test the connection
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    print("Query result:", result)
    
except pyodbc.Error as e:
    print("Error connecting to Azure SQL Database:", e)
finally:
    # Close the connection
    if 'conn' in locals():
        conn.close()
