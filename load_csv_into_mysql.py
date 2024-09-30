import mysql.connector
import pandas as pd

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="aviation_data"
)

cursor = conn.cursor()

# Drop the flights table if it already exists (optional)
cursor.execute("DROP TABLE IF EXISTS flights")

# Create the flights table if it doesn't already exist
create_table_query = '''
CREATE TABLE IF NOT EXISTS flights (
    FlightNumber VARCHAR(10),
    DepartureDate DATE,
    DepartureTime TIME,
    ArrivalDate DATE,
    ArrivalTime TIME,
    Airline VARCHAR(50),
    DelayMinutes FLOAT,
    DepartureDateTime DATETIME,
    ArrivalDateTime DATETIME,
    FlightDuration VARCHAR(50),
    FlightDurationMinutes FLOAT,
    DayOfWeek VARCHAR(12),
    DepartureHour INT
);
'''
cursor.execute(create_table_query)

# Read the CSV file into a DataFrame
data = pd.read_csv('cleaned_flight_data.csv')

# Iterate over each row in the DataFrame and insert the data into the database
for index, row in data.iterrows():
    insert_query = '''
    INSERT INTO flights (
        FlightNumber, DepartureDate, DepartureTime, ArrivalDate, ArrivalTime, Airline, DelayMinutes, 
        DepartureDateTime, ArrivalDateTime, FlightDuration, FlightDurationMinutes, DayOfWeek, DepartureHour
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    cursor.execute(insert_query, tuple(row))

# Commit the transaction to ensure data is saved
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Data inserted successfully!")
