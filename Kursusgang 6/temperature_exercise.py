import pandas as pd
import requests
from io import StringIO
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def load_dataset(url):
    response = requests.get(url)
    if response.status_code == 200:
        # If the request is successful, read the content into a DataFrame
        content = response.text
        
        # Find the start of the tabular data
        start_index = content.find("Monthly")
        
        # Read the data using pandas, skipping introductory lines
        df = pd.read_csv(StringIO(content[start_index:]), delim_whitespace=True, skiprows=[0])
        
        return df
    else:
        # If the request fails, print an error message
        print("Failed to fetch data from:", url)

def preprocess_data(df):
    # Change column names
    df.columns = ['Year','Month','Monthly Anomaly','Uncertainty','Annual Anomaly','Uncertainty.1',
              'Five-year Anomaly','Uncertainty.2','Ten-year Anomaly','Uncertainty.3',
              'Twenty-year Anomaly','Uncertainty.4','Hej']
    
    # Drop uncertainty columns
    df.drop(['Uncertainty','Uncertainty.1','Uncertainty.2','Uncertainty.3','Uncertainty.4','Hej'], axis=1, inplace=True)
    
    # Fill NaN's with 0
    df.fillna(0, inplace=True)
    
    return df

def calculate_statistics(df):
    # Compute statistics
    statistics = df.describe()
    
    return statistics

def simple_line_plot(df):
    # Replace invalid values with NaN
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    df['Month'] = pd.to_numeric(df['Month'], errors='coerce')
    df['Monthly Anomaly'] = pd.to_numeric(df['Monthly Anomaly'], errors='coerce')

    plt.figure(figsize=(12, 8))

    # Lineplot of temperature over time
    plt.subplot(3, 2, 1)
    plt.plot(df['Year'] + (df['Month'] - 1) / 12, df['Monthly Anomaly'], color='blue')
    plt.title('Global Temperatur over Tid')
    plt.xlabel('År')
    plt.ylabel('Temperaturafvigelse (°C)')

    # Histogram of temperatures
    plt.subplot(3, 2, 2)
    sns.histplot(df['Monthly Anomaly'], kde=True, color='green', bins=30)
    plt.title('Histogram af Temperaturer')
    plt.xlabel('Temperaturafvigelse (°C)')
    plt.ylabel('Antal måneder')

    # Average temperature pr year
    avg_temp_yearly = df.groupby('Year')['Monthly Anomaly'].mean().reset_index()
    avg_temp_yearly['Year'] = avg_temp_yearly['Year'] + 0.5  # Adjustment to center the datapoint on the x-axis

    # Remove duplicates if there are any
    df = df.drop_duplicates(subset=['Year', 'Month'])

    # Lineplot of average temperature pr year
    plt.subplot(3, 2, (3, 4))  
    plt.plot(avg_temp_yearly['Year'], avg_temp_yearly['Monthly Anomaly'], color='red')
    plt.title('Gennemsnitlig Årlig Temperatur')
    plt.xlabel('År')
    plt.ylabel('Gennemsnitlig Temperaturafvigelse (°C)')

    plt.tight_layout()
    plt.show()


def heatmap(df):
    # Convert 'Monthly Anomaly' column to numeric data type
    
    df['Monthly Anomaly'] = pd.to_numeric(df['Monthly Anomaly'], errors='coerce')
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    df['Month'] = pd.to_numeric(df['Month'], errors='coerce')

    # Calculate the mean temperature anomaly for each year and month
    pivot_data = df.groupby(['Year', 'Month'])['Monthly Anomaly'].mean().reset_index()

    # Pivot the DataFrame to have years as index, months as columns, and temperature anomalies as values
    heatmap_data = pivot_data.pivot(index='Month', columns='Year', values='Monthly Anomaly')

    # Plot the heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, cmap='coolwarm', cbar_kws={'label': 'Temperature Anomaly (°C)'})
    plt.title('Temperature Anomalies Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Month')

    plt.show()


def main():
    # URL of the dataset
    url = "https://berkeley-earth-temperature.s3.us-west-1.amazonaws.com/Global/Land_and_Ocean_complete.txt"

    # Call the function to load the dataset into a DataFrame
    df = load_dataset(url)

    # Preprocess the data
    df = preprocess_data(df)

    # Calculate statistics
    statistics = calculate_statistics(df)
    print("Statistiske resuméer:")
    print(statistics)

    # Generate simple line plot
    simple_line_plot(df)

    # Heatmap
    heatmap(df)

if __name__ == '__main__':
    main()
