import pandas as pd
file_path = 'aviation_data.csv'
data = pd.read_csv(file_path)

#Data cleaning
import numpy as np

# Group by 'Airline' and calculate the mean of 'DelayMinutes'
mean_delays = data.groupby('Airline')['DelayMinutes'].mean()

# Fill NaN values in 'DelayMinutes' with the corresponding mean delay for each airline
data['DelayMinutes'] = data.apply(lambda row: mean_delays[row['Airline']] if np.isnan(row['DelayMinutes']) else row['DelayMinutes'], axis=1)

#converting date and time columns to proper formats
data['DepartureDate'] = pd.to_datetime(data['DepartureDate'], format='%m/%d/%Y')
data['ArrivalDate'] = pd.to_datetime(data['ArrivalDate'], format='%m/%d/%Y')

#%I -> 12hour clock (01-12), %M -> min (00-59), %p -> AM or PM  08:30 AM
data['ArrivalTime'] = pd.to_datetime(data['ArrivalTime'],format='%I:%M %p').dt.time
data['DepartureTime'] = pd.to_datetime(data['DepartureTime'], format='%I:%M %p').dt.time


#Identify and handle logical duplicates (e.g., same flight number, same date)

duplicate_flights = data[data.duplicated(subset=['FlightNumber','DepartureDate'],keep=False)]


# Handling logical duplicates by keeping the flight with the latest ArrivalTime
data = data.sort_values(by='ArrivalTime').drop_duplicates(subset=['FlightNumber', 'DepartureDate'], keep='first')

# If the original order was based on the index
data.sort_index(inplace=True)


# Check for rows where ArrivalTime is less than DepartureTime on the same day
inconsistent_rows = data[(data['ArrivalDate'] == data['DepartureDate']) & 
                          (data['ArrivalTime'] < data['DepartureTime'])]



#Fixing the inconsistent time entires

from datetime import datetime

def fix_inconsistent_times(row):    
    if pd.notna(row['DepartureDate']) and pd.notna(row['ArrivalDate']) and pd.notna(row['DepartureTime']) and pd.notna(row['ArrivalTime']):
        dep_time = datetime.combine(row['DepartureDate'],row['DepartureTime'])
        arr_time = datetime.combine(row['ArrivalDate'],row['ArrivalTime'])

        #arr_time is less than dep_time then assume arrival is on next day
        if arr_time < dep_time:
            row['ArrivalDate'] = row['ArrivalDate'] + pd.Timedelta(days=1)
        return row
    
data = data.apply(fix_inconsistent_times,axis=1)

#Data Normalization

from datetime import datetime

data['DepartureDateTime'] = data.apply(lambda row: datetime.combine(row['DepartureDate'], row['DepartureTime']),axis=1)

data['ArrivalDateTime'] = data.apply(lambda row: datetime.combine(row['ArrivalDate'],row['ArrivalTime']),axis=1)

data['FlightDuration'] = data['ArrivalDateTime'] - data['DepartureDateTime']

data['FlightDurationMinutes'] = data['FlightDuration'].dt.total_seconds()/60

data['DayOfWeek'] = data['DepartureDate'].dt.day_name()

data['DepartureHour'] = data['DepartureDateTime'].dt.hour




#export cleaned data to csv file


data.to_csv('cleaned_flight_data.csv', index=False)