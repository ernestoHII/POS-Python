import random
import pyodbc
import string

# Define the MS SQL Server connection string
server = 'DESKTOP-JDQGAO5'
database = 'easypos'  # Change to your database name
username = 'sa'
password = 'easyfis'

# Establish a connection to the database
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
conn = pyodbc.connect(connection_string)

# Create a cursor
cursor = conn.cursor()

# Get column information for the MstItem table
cursor.execute('''
    SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'MstItem'
''')
column_info = cursor.fetchall()

# Identify the identity column
identity_column = None
for column_name, data_type, max_length in column_info:
    if data_type == 'int':
        identity_column = column_name
        break

# Generate random data for 3000 rows
for _ in range(3000):
    random_row = []
    for column_name, data_type, max_length in column_info:
        if column_name == identity_column:
            continue  # Skip identity column
        if data_type == 'nvarchar':
            max_length = max_length if max_length is not None else 255  # Set a default length for nvarchar columns
            random_value = ''.join(random.choices(string.ascii_letters, k=max_length))
        elif data_type == 'int':
            random_value = random.randint(1, 1000)
        elif data_type == 'bit':
            random_value = random.choice([0, 1])
        else:
            random_value = None  # Handle other data types as needed

        random_row.append(random_value)

    # Create placeholders for the parameters in the SQL query
    placeholders = ', '.join(['?' for _ in range(len(random_row))])

    # Build the SQL query with dynamic column names and placeholders
    query = f'''
        INSERT INTO MstItem ({', '.join([column[0] for column in column_info if column[0] != identity_column])})
        VALUES ({placeholders})
    '''

    # Execute the SQL query with the random row data
    cursor.execute(query, random_row)

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("3000 rows of random data have been inserted into the MstItem table.")
