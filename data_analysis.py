import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector
import pandas as pd
import scipy.stats as stats


def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="aviation_data"
    )
    return conn


def fetch_data():
    conn = connect_db()
    query = "SELECT * FROM flights"
    data = pd.read_sql(query, conn)
    conn.close()
    return data


def generate_plots():
    data = fetch_data()

    # Convert date columns to datetime format
    data['DepartureDate'] = pd.to_datetime(data['DepartureDate'])
    data['DepartureDateTime'] = pd.to_datetime(data['DepartureDateTime'])
    data['DayOfWeek'] = data['DepartureDate'].dt.day_name()

    # Distribution of Flight Delays - Histogram and Box Plot
    plt.figure(figsize=(10, 6))
    sns.histplot(data['DelayMinutes'], kde=True, bins=30)
    plt.title('Distribution of Flight Delays')
    plt.xlabel('Delay in Minutes')
    plt.ylabel('Frequency')
    plt.savefig('plots/plot1.png')

    plt.figure(figsize=(10, 6))
    sns.boxplot(x=data['DelayMinutes'])
    plt.title('Box Plot of Flight Delays')
    plt.xlabel('Delay in Minutes')
    plt.savefig('plots/plot2.png')

    # Average Delay by Day of the Week
    average_delay_by_day = data.groupby('DayOfWeek')['DelayMinutes'].mean()
    plt.figure(figsize=(10, 6))
    average_delay_by_day.plot(kind='bar', color='red')
    plt.title('Average Delay by Day of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Average Delay (minutes)')
    plt.xticks(rotation=45)
    plt.savefig('plots/plot3.png')

    # Average Delay per Airline
    average_delay_per_airline = data.groupby('Airline')['DelayMinutes'].mean().reset_index()
    average_delay_per_airline = average_delay_per_airline.sort_values(by='DelayMinutes', ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Airline', y='DelayMinutes', data=average_delay_per_airline)
    plt.title('Average Delay by Airline')
    plt.xlabel('Airline')
    plt.ylabel('Average Delay in Minutes')
    plt.savefig('plots/plot4.png')

    # Delays vs Departure Time
    data['DepartureHour'] = data['DepartureDateTime'].dt.hour

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='DepartureHour', y='DelayMinutes', data=data)
    plt.title('Flight Delays vs Departure Time')
    plt.xlabel('Departure Hour (0-23)')
    plt.ylabel('Delay in Minutes')
    plt.savefig('plots/plot5.png')

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='DepartureHour', y='DelayMinutes', data=data)
    plt.title('Flight Delays vs Departure Hour')
    plt.xlabel('Departure Hour (0-23)')
    plt.ylabel('Delay in Minutes')
    plt.savefig('plots/plot6.png')

    # ANOVA Analysis
    anova_result = stats.f_oneway(*(data[data['Airline'] == airline]['DelayMinutes'] for airline in data['Airline'].unique()))
    print(f'ANOVA p-value: {anova_result.pvalue}')

    # ANOVA Plot
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Airline', y='DelayMinutes', data=data)
    if anova_result.pvalue < 0.05:
        plt.title("Statistically significant difference in delays between airlines")
    else:
        plt.title("No statistically significant difference in delays between airlines")
    plt.savefig('plots/plot7.png')

    plt.close('all')


# Run the plot generation function
generate_plots()
