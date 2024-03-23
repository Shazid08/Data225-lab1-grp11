import csv
import pymysql

# Define function to determine column data types
def determine_column_types(csv_file):
    # Read first few rows of the CSV file to determine data types
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        sample_data = [row for row in reader]

    # Determine data types for each column based on sample data
    column_types = {}
    for row in sample_data:
        for key, value in row.items():
            if key not in column_types:
                # Try converting the value to int
                try:
                    int(value)
                    column_types[key] = 'INT'
                except ValueError:
                    # Try converting the value to float
                    try:
                        float(value)
                        column_types[key] = 'FLOAT'
                    except ValueError:
                        # If neither int nor float, assume VARCHAR
                        if key == 'overview':
                            column_types[key] = 'VARCHAR(3000)'  # Change to VARCHAR with length 3000
                        else:
                            column_types[key] = 'VARCHAR(255)'
    return column_types

# Define function to create table in SQL database
def create_table(cursor, table_name, column_types):
    # Construct SQL query to create table
    query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
    for column, data_type in column_types.items():
        query += f"`{column}` {data_type}, "  # Enclose column name in backticks
    query = query[:-2] + ")"  # Remove the trailing comma and space, and close the query

    # Execute the SQL query to create table
    cursor.execute(query)

# Connect to MySQL database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Shazid@0000',
    database='The_Movies_Dataset'
)

# Get a cursor object
cursor = connection.cursor()

# Determine column data types
csv_file = 'Preprocessed data/preprocessed_movies_metadata_cleansed.csv'
column_types = determine_column_types(csv_file)

# Create table in database
table_name = 'movies_metadata_cleansed'
create_table(cursor, table_name, column_types)

# Commit changes and close connection
connection.commit()
connection.close()

print(f"Table '{table_name}' created successfully!")
