import csv
import pymysql

# Define function to insert data from CSV into MySQL table
def insert_data_from_csv(cursor, table_name, csv_file):
    # Open CSV file and read data
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        # Iterate over each row in the CSV file
        for row in reader:
            # Extract values from the row
            movie_id_val = row['id']
            original_title_val = row['original_title']
            release_date_val = row['release_date']
            budget_val = row['budget']
            revenue_val = row['revenue']
            runtime_val = row['runtime']
            vote_average_val = row['vote_average']
            vote_count_val = row['vote_count']
            popularity_val = row['popularity']
            overview_val = row['overview']
            genres_val = row['genres']

            # Construct SQL query to insert data into the table
            query = f"INSERT INTO {table_name} (movie_id, original_title, release_date, budget, revenue, runtime, vote_average, vote_count, popularity, overview, genres) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (movie_id_val, original_title_val, release_date_val, budget_val, revenue_val, runtime_val, vote_average_val, vote_count_val, popularity_val, overview_val, genres_val)

            # Execute the SQL query
            cursor.execute(query, values)

# Connect to MySQL database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Shazid@0000',
    database='The_Movies_Dataset'
)

# Get a cursor object
cursor = connection.cursor()

# CSV file containing the data
csv_file = 'preprocessed data/preprocessed_movies_metadata_cleansed.csv'

# Name of the table in the database
table_name = 'preprocessed_movies_metadata_cleansed'

# Insert data into the table
insert_data_from_csv(cursor, table_name, csv_file)

# Commit changes and close connection
connection.commit()
connection.close()

print("Data inserted successfully!")
