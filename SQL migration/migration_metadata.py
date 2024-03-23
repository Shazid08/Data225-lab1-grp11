import csv
import pymysql

# Define function to insert data into the table
def insert_data(cursor, table_name, csv_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            columns = ', '.join(row.keys())
            values = ', '.join('%s' for _ in row.values())
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
            cursor.execute(query, tuple(row.values()))

# Connect to MySQL database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Shazid@0000',
    database='The_Movies_Dataset'
)

# Get a cursor object
cursor = connection.cursor()

# Insert data into the table
table_name = 'movies_metadata_cleansed'
csv_file = 'Preprocessed data/preprocessed_movies_metadata_cleansed.csv'
insert_data(cursor, table_name, csv_file)

# Commit changes and close connection
connection.commit()
connection.close()

print(f"Data inserted into the '{table_name}' table successfully!")
